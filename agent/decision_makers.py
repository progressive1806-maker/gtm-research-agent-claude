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
    """Only linkedin.com/in/<slug> and linkedin.com/company/<slug> count as profile URLs."""
    if not url:
        return False
    lower = url.lower()
    return "linkedin.com/in/" in lower or "linkedin.com/company/" in lower


def classify_result(
    item: dict[str, Any],
    company_name: str,
    role_terms: list[str],
) -> str:
    """
    HIGH/MID/LOW require a real linkedin.com/in or linkedin.com/company URL.
    News/blog/article URLs (venturesquare.net, sanctionlab.com, naver.com, …)
    never reach HIGH/MID/LOW — they return UNKNOWN even if title/desc happen
    to mention the company and a role.
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

    is_linkedin_profile = "linkedin.com/in/" in url
    is_linkedin_company = "linkedin.com/company/" in url
    company_match = company in blob or company in url
    role_match = any(role.strip().lower() in blob for role in role_terms if role)

    if (is_linkedin_profile or is_linkedin_company) and company_match and role_match:
        return "HIGH"
    if (is_linkedin_profile or is_linkedin_company) and (company_match or role_match):
        return "MID"
    return "LOW"


def find_profile_for_candidate(
    candidate: dict[str, Any],
    rate_limit_sleep: float = 0.25,
) -> tuple[dict[str, Any] | None, list[str], str | None]:
    """
    Returns (best_record, queries_used, error).
      best_record is None when no useful items came back at all (e.g., total search failure).
      Otherwise best_record["confidence"] is HIGH / MID / LOW / UNKNOWN.
    """
    queries = build_queries_for_candidate(candidate)
    if not queries:
        return None, [], None

    roles = roles_for_candidate(candidate)
    company = (candidate.get("name") or "").strip()

    best: dict[str, Any] | None = None
    used_queries: list[str] = []
    error: str | None = None

    for query in queries:
        used_queries.append(query)
        items: list[dict[str, Any]] = []
        source = ""
        try:
            items = naver_web_search(query)
            source = "naver_web"
        except Exception as exc_web:
            try:
                items = naver_news_search(query)
                source = "naver_news_fallback"
                if error is None:
                    error = f"naver_web unavailable: {exc_web}"
            except Exception as exc_news:
                error = f"naver_web: {exc_web}; naver_news: {exc_news}"
                items = []

        for item in items:
            confidence = classify_result(item, company, roles)
            record = {
                "url": item.get("link"),
                "title": _strip_html(item.get("title", "")),
                "source": source,
                "confidence": confidence,
                "matched_query": query,
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
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], str | None]:
    """
    Mutates each non-noise candidate in place. Adds:
      - decision_maker_profile_url
      - decision_maker_profile_title
      - decision_maker_profile_source
      - decision_maker_profile_confidence
      - decision_maker_search_queries

    Returns (candidates, per-candidate records for JSON dump, aggregate_error_or_None).
    """
    records: list[dict[str, Any]] = []
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

        # Strict URL gate: only real LinkedIn profile/company URLs are surfaced.
        # Article/news/blog URLs never become decision_maker_profile_url, even
        # if classify_result somehow returned MID/LOW.
        if confidence in ("HIGH", "MID", "LOW") and is_valid_linkedin_url(url):
            candidate["decision_maker_profile_url"] = url
            candidate["decision_maker_profile_title"] = best.get("title") or "확인 필요"
            candidate["decision_maker_profile_source"] = best.get("source") or ""
            candidate["decision_maker_profile_confidence"] = confidence
        else:
            candidate["decision_maker_profile_url"] = ""
            candidate["decision_maker_profile_title"] = "확인 필요"
            candidate["decision_maker_profile_source"] = ""
            candidate["decision_maker_profile_confidence"] = "UNKNOWN"

    return candidates, records, aggregate_error
