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
ROLE_TERMS_BY_TARGET: dict[str, list[str]] = {
    "온프레미스 기업": [
        "CIO",
        "CTO",
        "CISO",
        "Head of Infrastructure",
        "Head of AI",
        "정보화 본부장",
        "IT 인프라 임원",
    ],
    "CSP 운영 기업": [
        "Head of Cloud",
        "Head of Infrastructure",
        "Data Center",
        "Platform Lead",
        "GPU service lead",
        "NPU service lead",
        "클라우드 사업 본부장",
        "데이터센터 본부장",
    ],
    "CSP 고객 기업": [
        "Head of AI",
        "Product AI lead",
        "CTO",
        "Platform lead",
        "AI 본부장",
    ],
}

# For B2G/public-sector candidates (market == "B2G").
B2G_ROLE_TERMS: list[str] = [
    "procurement",
    "정보화 담당관",
    "AI 사업 책임자",
    "디지털정부 담당",
    "조달 담당",
]

DEFAULT_ROLE_TERMS: list[str] = ["CIO", "CTO", "Head of AI", "Head of Cloud"]

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


def _strip_html(text: str) -> str:
    cleaned = re.sub(r"<[^>]+>", "", text or "")
    return unescape(cleaned).strip()


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


def _run_search(query: str, prefer_cse: bool) -> tuple[list[dict[str, Any]], str, str | None]:
    """
    Backend ladder for a single query:
      1. Google CSE (when configured) with site:linkedin.com/in bias
      2. Naver web search (general)
      3. Naver news search (last resort)

    Returns (items, backend_label, soft_error). The soft_error captures the
    first failure so the caller can record it; absence of a working backend
    is itself recorded.
    """
    soft_error: str | None = None

    if prefer_cse:
        cse_query = _cse_biased_query(query)
        try:
            items = google_cse_search(cse_query)
            return items, "google_cse", soft_error
        except Exception as exc_cse:
            soft_error = f"google_cse: {exc_cse.__class__.__name__}: {exc_cse}"

    try:
        items = naver_web_search(query)
        return items, "naver_web", soft_error
    except Exception as exc_web:
        if soft_error is None:
            soft_error = f"naver_web: {exc_web.__class__.__name__}: {exc_web}"
        else:
            soft_error = f"{soft_error}; naver_web: {exc_web}"

    try:
        items = naver_news_search(query)
        return items, "naver_news_fallback", soft_error
    except Exception as exc_news:
        return [], "", f"{soft_error}; naver_news: {exc_news}"


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
    queries = build_queries_for_candidate(candidate)
    if not queries:
        return None, [], None

    roles = roles_for_candidate(candidate)
    company = (candidate.get("name") or "").strip()
    prefer_cse = google_cse_configured()

    best: dict[str, Any] | None = None
    used_queries: list[str] = []
    error: str | None = None

    for query in queries:
        used_queries.append(query)
        items, source, soft_error = _run_search(query, prefer_cse=prefer_cse)
        if soft_error and error is None:
            error = soft_error

        matched_query = _cse_biased_query(query) if source == "google_cse" else query

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

        time.sleep(rate_limit_sleep)
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
