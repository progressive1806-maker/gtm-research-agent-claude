"""
Decision-maker profile discovery for GTM candidates (v0.7).

Constraints:
- Do NOT scrape LinkedIn pages directly.
- Do NOT log in to LinkedIn.
- Do NOT use browser automation.
- Do NOT invent names, titles, or profile URLs.
- Only consume public search-result snippets/URLs returned by the Naver Search APIs.
- If no reliable result is found, mark the candidate as 확인 필요 (UNKNOWN).

This module is intentionally small and side-effect free aside from network calls.
"""

from __future__ import annotations

import os
import re
import time
from html import unescape
from typing import Any

import requests

NAVER_WEB_SEARCH_URL = "https://openapi.naver.com/v1/search/webkr.json"
NAVER_NEWS_SEARCH_URL = "https://openapi.naver.com/v1/search/news.json"
GOOGLE_CSE_URL = "https://www.googleapis.com/customsearch/v1"

# Roles chosen by target_type. Mixed EN/KR so search snippets in both languages have a chance to match.
# Korean BD reality: C-levels rarely have public LinkedIn profiles. The actual
# contactable champions for a PoC are usually team leads + senior engineers +
# AI/MLOps/Platform PMs. Role lists below intentionally mix executive titles
# (for completeness) with team-level and IC-level titles (where the actual
# evaluation and PoC starts).
ROLE_TERMS_BY_TARGET: dict[str, list[str]] = {
    "온프레미스 기업": [
        # Executives
        "CIO", "CTO", "CISO",
        "Head of AI", "Head of Infrastructure",
        # 본부 / 팀 리더 — 한국 대기업에서 자주 보이는 직함
        "정보화 본부장", "정보화실장", "정보화팀장",
        "IT 인프라 임원", "IT팀장", "인프라팀장", "AI팀장",
        # 시니어 IC — 실제 PoC 진행 주체. LinkedIn 사용률 높음
        "AI 엔지니어", "ML 엔지니어", "MLOps 엔지니어",
        "인프라 엔지니어", "시스템 엔지니어", "시니어 엔지니어",
        "Solutions Architect", "솔루션 아키텍트",
        "AI Lead", "ML Lead", "Platform Lead",
    ],
    "CSP 운영 기업": [
        # Executives
        "Head of Cloud", "Head of Infrastructure",
        "클라우드 사업 본부장", "데이터센터 본부장",
        # 사업/제품 리더 — CSP에서 NPU/GPU 도입 결정에 핵심
        "GPU service lead", "NPU service lead",
        "NPUaaS Product Manager", "GPUaaS Product Manager",
        "Cloud Product Manager",
        "사업 개발 담당", "MSP 채널 담당", "파트너십 매니저",
        # 시니어 IC
        "Cloud Engineer", "Platform Engineer", "Data Center Engineer",
        "Cloud Solutions Architect", "DevOps Engineer", "SRE",
        "Platform Lead", "Service Lead",
    ],
    "CSP 고객 기업": [
        # Executives
        "CTO", "Head of AI",
        "AI 본부장", "AI 사업 본부장",
        # 사업/제품 리더
        "AI Product Manager", "Product AI lead",
        "AI 기획자", "AI 전략 담당",
        # 시니어 IC
        "AI 엔지니어", "ML 엔지니어", "MLOps 엔지니어",
        "AI Platform Engineer", "Platform Lead",
        "AI Lead", "ML Lead",
    ],
}

# For B2G/public-sector candidates (market == "B2G").
B2G_ROLE_TERMS: list[str] = [
    # 기관 임원/관리자
    "정보화 담당관", "정보화 책임관", "정보화 책임자",
    "AI 사업 책임자", "IT 사업 책임자",
    # 실무 담당 — 과장/사무관급
    "디지털정부 담당", "AI 사업 담당", "IT 사업 담당", "정보화 사업 담당",
    # 조달
    "조달 담당", "procurement",
    # 운영/실장
    "정보화 운영", "전산실장", "전산팀장",
    # 공공 R&D / 연구소
    "선임 연구원", "책임 연구원", "수석 연구원",
    "AI 연구 책임자", "AI 그룹장",
]

DEFAULT_ROLE_TERMS: list[str] = [
    "CIO", "CTO", "Head of AI", "Head of Cloud",
    "AI 엔지니어", "MLOps 엔지니어", "AI 팀장", "Platform Lead",
]

MAX_QUERIES_PER_CANDIDATE = 4

CONFIDENCE_RANK = {"HIGH": 3, "MID": 2, "LOW": 1, "UNKNOWN": 0}


def roles_for_candidate(candidate: dict[str, Any]) -> list[str]:
    """Pick role search terms dynamically from target_type / market."""
    if candidate.get("market") == "B2G":
        return list(B2G_ROLE_TERMS)
    target = candidate.get("target_type") or ""
    return list(ROLE_TERMS_BY_TARGET.get(target, DEFAULT_ROLE_TERMS))


def build_queries_for_candidate(
    candidate: dict[str, Any],
    max_queries: int = MAX_QUERIES_PER_CANDIDATE,
) -> list[str]:
    name = (candidate.get("name") or "").strip()
    if not name:
        return []
    roles = roles_for_candidate(candidate)
    queries: list[str] = []
    for role in roles[:max_queries]:
        queries.append(f"{name} {role} LinkedIn")
    return queries[:max_queries]


def build_grounding_query_for_candidate(candidate: dict[str, Any]) -> str:
    """
    Compound query for Gemini grounding — one call per candidate. Bundling
    all target roles into a single query keeps us under the 10 RPM free-tier
    limit while still covering execs + senior ICs + team leads. Korean BD
    contacts often come from manager / engineer levels who actually have
    public LinkedIn profiles (vs. C-levels who typically don't).
    """
    name = (candidate.get("name") or "").strip()
    if not name:
        return ""
    roles = roles_for_candidate(candidate)
    # Use up to 10 roles per query. Search engines accept long OR-trees and
    # this widens the pool from "CTO only" to "CTO OR AI팀장 OR Platform Lead OR ...".
    role_blob = " OR ".join(f'"{r}"' for r in roles[:10])
    return f'site:linkedin.com/in "{name}" ({role_blob})'


def _strip_html(text: str) -> str:
    cleaned = re.sub(r"<[^>]+>", "", text or "")
    return unescape(cleaned).strip()


# Patterns that strip credentials out of any error message we record.
# requests.HTTPError formats include the full request URL with ?key=... &cx=...
_REDACT_PATTERNS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"(?i)(key=)[^&\s\"']+"), r"\1***"),
    (re.compile(r"(?i)(cx=)[^&\s\"']+"), r"\1***"),
    (re.compile(r"(?i)(X-Naver-Client-Secret:\s*)[^\s\"']+"), r"\1***"),
    (re.compile(r"(?i)(serviceKey=)[^&\s\"']+"), r"\1***"),
    (re.compile(r"(AIza[0-9A-Za-z_-]{20,})"), "***"),
]


def _safe_exc(exc: BaseException) -> str:
    """
    Format an exception for logging/metadata while stripping anything that
    looks like a credential — Google API keys, CSE cx, Naver client secret,
    G2B service keys. Never put raw exc into telemetry.
    """
    cls = exc.__class__.__name__
    msg = str(exc).strip().splitlines()[0] if str(exc).strip() else ""
    for pattern, replacement in _REDACT_PATTERNS:
        msg = pattern.sub(replacement, msg)
    return f"{cls}: {msg}"[:240] if msg else cls


def _naver_headers() -> dict[str, str]:
    client_id = os.getenv("NAVER_CLIENT_ID", "")
    client_secret = os.getenv("NAVER_CLIENT_SECRET", "")
    if not client_id or not client_secret:
        raise RuntimeError("NAVER credentials are missing")
    return {
        "X-Naver-Client-Id": client_id,
        "X-Naver-Client-Secret": client_secret,
    }


def naver_web_search(query: str, display: int = 5) -> list[dict[str, Any]]:
    response = requests.get(
        NAVER_WEB_SEARCH_URL,
        headers=_naver_headers(),
        params={"query": query, "display": display, "start": 1},
        timeout=15,
    )
    response.raise_for_status()
    return response.json().get("items", [])


def google_cse_configured() -> bool:
    """True when both GOOGLE_CSE_API_KEY (secret) and GOOGLE_CSE_ID are set."""
    return bool(os.getenv("GOOGLE_CSE_API_KEY", "").strip()) and bool(
        os.getenv("GOOGLE_CSE_ID", "").strip()
    )


def gemini_grounding_configured() -> bool:
    """
    True when GEMINI_API_KEY is set AND grounding is not explicitly disabled.
    Gemini search grounding has no per-day quota (it's part of the model call
    quota), so this is the preferred LinkedIn discovery backend.
    """
    if not os.getenv("GEMINI_API_KEY", "").strip():
        return False
    return os.getenv("ENABLE_GEMINI_GROUNDING", "true").strip().lower() != "false"


def gemini_grounded_search(query: str, display: int = 5) -> list[dict[str, Any]]:
    """
    Use Gemini's built-in google_search grounding tool to find URLs for a query.
    Returns items in the same {link, title, description} shape as the other
    backends so _run_search can treat them uniformly.

    The grounding tool is part of the standard Gemini model call — no extra
    API key, no per-day search quota beyond the model call budget itself.
    """
    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not configured for grounded search")

    # Search grounding is FREE only on the Gemini 2.5 family (Flash / Pro:
    # up to 500 RPD shared with Flash-Lite). On 3.5 Flash and 3.1 Flash-Lite
    # grounding is paid-only ($14/1000 prompts after 5,000 shared free).
    # We pin to 2.5-flash unless LLM_GROUNDING_MODEL explicitly picks another
    # 2.5 variant — anything else is downgraded silently so the workflow can
    # never accidentally hit paid grounding usage.
    model = os.getenv("LLM_GROUNDING_MODEL", "").strip() or "gemini-2.5-flash"
    if "2.5" not in model:
        model = "gemini-2.5-flash"

    # Lazy import to keep selftest fast and avoid pulling SDK if disabled.
    from google import genai as _genai

    try:
        from google.genai import types as _types
        tools = [_types.Tool(google_search=_types.GoogleSearch())]
        config = _types.GenerateContentConfig(tools=tools)
    except Exception:
        tools = [{"google_search": {}}]
        config = {"tools": tools}

    client = _genai.Client(api_key=api_key)
    prompt = (
        f"Search the web for: {query}\n\n"
        "Return only a JSON array of up to "
        f"{max(1, min(display, 10))} results, each with keys "
        "{\"link\": <url>, \"title\": <title>, \"description\": <snippet>}. "
        "Strongly prefer linkedin.com/in/<slug> individual profile URLs."
    )
    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config=config,
    )

    text = (response.text or "").strip()
    items_from_json: list[dict[str, Any]] = []
    if text:
        cleaned = re.sub(r"^```(?:json)?\s*", "", text.strip())
        cleaned = re.sub(r"\s*```$", "", cleaned)
        try:
            import json as _json
            parsed = _json.loads(cleaned)
            if isinstance(parsed, list):
                for entry in parsed:
                    if not isinstance(entry, dict):
                        continue
                    items_from_json.append(
                        {
                            "link": entry.get("link") or entry.get("url") or "",
                            "title": entry.get("title") or "",
                            "description": entry.get("description") or entry.get("snippet") or "",
                        }
                    )
        except Exception:
            pass

    # Also harvest URLs from the grounding metadata (the SDK exposes them on
    # response.candidates[0].grounding_metadata.grounding_chunks). Combining
    # both surfaces gives us the broadest coverage.
    items_from_metadata: list[dict[str, Any]] = []
    try:
        candidates = getattr(response, "candidates", None) or []
        for cand in candidates:
            gm = getattr(cand, "grounding_metadata", None)
            chunks = getattr(gm, "grounding_chunks", None) or []
            for ch in chunks:
                web = getattr(ch, "web", None)
                if not web:
                    continue
                items_from_metadata.append(
                    {
                        "link": getattr(web, "uri", "") or "",
                        "title": getattr(web, "title", "") or "",
                        "description": "",
                    }
                )
    except Exception:
        pass

    merged: list[dict[str, Any]] = []
    seen: set[str] = set()
    for item in items_from_json + items_from_metadata:
        link = (item.get("link") or "").strip()
        if not link or link in seen:
            continue
        seen.add(link)
        merged.append(item)
        if len(merged) >= max(1, min(display, 10)):
            break
    return merged


def google_cse_search(query: str, display: int = 5) -> list[dict[str, Any]]:
    """
    Google Programmable Search Engine (Custom Search JSON API).

    Why this exists: Naver web search rarely indexes linkedin.com/in/<slug>
    profile pages — LinkedIn blocks most crawlers. Google indexes the public
    profile snippets and CSE gives us official, API-rate-limited access.

    Free tier: 100 queries/day. After that the API returns 429 and we fall
    back to Naver. No scraping involved — this is Google's official API.

    Returns items in the same {link, title, description} shape as the
    Naver helpers so the rest of the pipeline doesn't care which backend
    produced the result.
    """
    api_key = os.getenv("GOOGLE_CSE_API_KEY", "").strip()
    cse_id = os.getenv("GOOGLE_CSE_ID", "").strip()
    if not api_key or not cse_id:
        raise RuntimeError("Google CSE is not configured")
    response = requests.get(
        GOOGLE_CSE_URL,
        params={
            "key": api_key,
            "cx": cse_id,
            "q": query,
            "num": max(1, min(display, 10)),
        },
        timeout=15,
    )
    response.raise_for_status()
    payload = response.json() or {}
    items_raw = payload.get("items") or []
    return [
        {
            "link": it.get("link", ""),
            "title": it.get("title", ""),
            "description": it.get("snippet", ""),
        }
        for it in items_raw
        if isinstance(it, dict)
    ]


def naver_news_search(query: str, display: int = 5) -> list[dict[str, Any]]:
    """Safe fallback when the web search endpoint is unavailable for this app."""
    response = requests.get(
        NAVER_NEWS_SEARCH_URL,
        headers=_naver_headers(),
        params={"query": query, "display": display, "start": 1, "sort": "sim"},
        timeout=15,
    )
    response.raise_for_status()
    return response.json().get("items", [])


def is_valid_linkedin_url(url: str) -> bool:
    """
    BD use case: we want INDIVIDUAL decision-maker profiles, not company pages.
    Only linkedin.com/in/<slug> qualifies. linkedin.com/company/<slug> is
    a company landing page and is explicitly rejected — it doesn't tell us
    who to contact.
    """
    if not url:
        return False
    return "linkedin.com/in/" in url.lower()


def classify_result(
    item: dict[str, Any],
    company_name: str,
    role_terms: list[str],
) -> str:
    """
    Returns:
      HIGH    — linkedin.com/in/<slug> URL whose title/desc mentions BOTH
                the target company name and a role term.
      MID     — linkedin.com/in/<slug> URL with EITHER company OR role match.
      UNKNOWN — anything else: company pages (linkedin.com/company/...),
                news/article URLs, bare individual profiles without context,
                or profiles where neither the company nor a role appears.

    LOW is no longer produced. A bare /in/ URL with no contextual match is
    treated as UNKNOWN because we cannot tell whose profile it is.
    """
    url = (item.get("link") or "").lower()
    title = _strip_html(item.get("title", "")).lower()
    desc = _strip_html(item.get("description", "")).lower()
    blob = f"{title} {desc}"

    company = company_name.strip().lower()
    if not company:
        return "UNKNOWN"

    if not is_valid_linkedin_url(url):
        return "UNKNOWN"

    # Now we know it's a linkedin.com/in/<slug> URL.
    company_match = company in blob or company in url
    role_match = any(role.strip().lower() in blob for role in role_terms if role)

    if company_match and role_match:
        return "HIGH"
    if company_match or role_match:
        return "MID"
    return "UNKNOWN"


def _cse_biased_query(query: str) -> str:
    """Bias the CSE query toward LinkedIn individual profiles."""
    if "site:" in query.lower():
        return query
    return f"{query} site:linkedin.com/in"


def _run_search(
    query: str,
    prefer_cse: bool,
    prefer_grounding: bool = False,
) -> tuple[list[dict[str, Any]], str, str | None]:
    """
    Backend ladder for a single query:
      1. Gemini search grounding (when GEMINI_API_KEY set; cheap, large quota)
      2. Google CSE (when configured) with site:linkedin.com/in bias
      3. Naver web search (general)
      4. Naver news search (last resort)

    Returns (items, backend_label, soft_error). The soft_error captures the
    first failure so the caller can record it; absence of a working backend
    is itself recorded.
    """
    soft_error: str | None = None

    if prefer_grounding:
        grounded_query = _cse_biased_query(query)
        try:
            items = gemini_grounded_search(grounded_query)
            return items, "gemini_grounding", soft_error
        except Exception as exc_g:
            soft_error = f"gemini_grounding: {_safe_exc(exc_g)}"

    if prefer_cse:
        cse_query = _cse_biased_query(query)
        try:
            items = google_cse_search(cse_query)
            return items, "google_cse", soft_error
        except Exception as exc_cse:
            if soft_error is None:
                soft_error = f"google_cse: {_safe_exc(exc_cse)}"
            else:
                soft_error = f"{soft_error}; google_cse: {_safe_exc(exc_cse)}"

    try:
        items = naver_web_search(query)
        return items, "naver_web", soft_error
    except Exception as exc_web:
        if soft_error is None:
            soft_error = f"naver_web: {_safe_exc(exc_web)}"
        else:
            soft_error = f"{soft_error}; naver_web: {_safe_exc(exc_web)}"

    try:
        items = naver_news_search(query)
        return items, "naver_news_fallback", soft_error
    except Exception as exc_news:
        return [], "", f"{soft_error}; naver_news: {_safe_exc(exc_news)}"


def find_profile_for_candidate(
    candidate: dict[str, Any],
    rate_limit_sleep: float = 0.25,
) -> tuple[dict[str, Any] | None, list[str], str | None]:
    """
    Returns (best_record, queries_used, error).
      best_record is None when no useful items came back at all.
      Otherwise best_record["confidence"] is HIGH / MID / UNKNOWN.

    Prefers Google CSE when configured; falls back to Naver web/news search.
    """
    roles = roles_for_candidate(candidate)
    company = (candidate.get("name") or "").strip()
    prefer_grounding = gemini_grounding_configured()
    prefer_cse = google_cse_configured()

    # When grounding is on, use ONE compound query per candidate instead of
    # building N role-specific queries. Gemini 2.5 Flash free tier is 10 RPM,
    # so we'd burn through quota fast otherwise. The compound query packs
    # every role into a single grounded search.
    if prefer_grounding:
        compound = build_grounding_query_for_candidate(candidate)
        queries = [compound] if compound else []
        # 10 RPM = 6s between calls; pad to 6.5 for safety.
        effective_sleep = max(rate_limit_sleep, 6.5)
    else:
        queries = build_queries_for_candidate(candidate)
        effective_sleep = rate_limit_sleep

    if not queries:
        return None, [], None

    best: dict[str, Any] | None = None
    used_queries: list[str] = []
    error: str | None = None

    for query in queries:
        used_queries.append(query)
        items, source, soft_error = _run_search(
            query,
            prefer_cse=prefer_cse,
            prefer_grounding=prefer_grounding,
        )
        if soft_error and error is None:
            error = soft_error

        if source in ("google_cse", "gemini_grounding"):
            matched_query = _cse_biased_query(query)
        else:
            matched_query = query

        for item in items:
            confidence = classify_result(item, company, roles)
            record = {
                "url": item.get("link"),
                "title": _strip_html(item.get("title", "")),
                "source": source,
                "confidence": confidence,
                "matched_query": matched_query,
                "description_snippet": _strip_html(item.get("description", ""))[:200],
            }
            if best is None or CONFIDENCE_RANK[confidence] > CONFIDENCE_RANK[best["confidence"]]:
                best = record

        time.sleep(effective_sleep)
        if best and best["confidence"] == "HIGH":
            break

    return best, used_queries, error


def enrich_candidates_with_profiles(
    candidates: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[str, Any], str | None]:
    """
    Mutates each non-noise candidate in place. Adds:
      - decision_maker_profile_url
      - decision_maker_profile_title
      - decision_maker_profile_source
      - decision_maker_profile_confidence
      - decision_maker_search_queries

    Returns:
      (candidates, per-candidate records for JSON dump, telemetry dict, aggregate_error_or_None)

    telemetry dict shape:
      {
        "valid_count":      candidates with a real linkedin.com/in or linkedin.com/company profile (HIGH/MID)
        "suppressed_count": candidates whose best search hit was a non-LinkedIn URL (Data Center Map style)
        "unknown_count":    candidates with no useful search result at all
      }
    """
    records: list[dict[str, Any]] = []
    telemetry = {"valid_count": 0, "suppressed_count": 0, "unknown_count": 0}
    aggregate_error: str | None = None

    for candidate in candidates:
        if not isinstance(candidate, dict):
            continue
        if candidate.get("classification") == "noise":
            continue

        best, queries, error = find_profile_for_candidate(candidate)
        if error and aggregate_error is None:
            aggregate_error = error

        records.append(
            {
                "name": candidate.get("name"),
                "market": candidate.get("market"),
                "target_type": candidate.get("target_type"),
                "queries": queries,
                "best": best,
                "error": error,
            }
        )

        candidate["decision_maker_search_queries"] = queries

        url = (best or {}).get("url") or ""
        confidence = (best or {}).get("confidence") or "UNKNOWN"

        # Strict URL gate: only HIGH/MID + real LinkedIn profile/company URLs
        # are surfaced. Article/news/blog URLs (Data Center Map, IDCA, ...) and
        # LOW-confidence LinkedIn hits never become decision_maker_profile_url.
        if confidence in ("HIGH", "MID") and is_valid_linkedin_url(url):
            candidate["decision_maker_profile_url"] = url
            candidate["decision_maker_profile_title"] = best.get("title") or "확인 필요"
            candidate["decision_maker_profile_source"] = best.get("source") or ""
            candidate["decision_maker_profile_confidence"] = confidence
            telemetry["valid_count"] += 1
        else:
            candidate["decision_maker_profile_url"] = ""
            candidate["decision_maker_profile_title"] = "확인 필요"
            candidate["decision_maker_profile_source"] = ""
            candidate["decision_maker_profile_confidence"] = "UNKNOWN"
            if best:
                # We had a search hit but it failed the LinkedIn gate (Data Center
                # Map, IDCA, news article, LOW-confidence LinkedIn hit, etc.).
                telemetry["suppressed_count"] += 1
            else:
                telemetry["unknown_count"] += 1

    return candidates, records, telemetry, aggregate_error
