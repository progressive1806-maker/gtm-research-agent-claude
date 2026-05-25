"""
Optional G2B (Korea Public Procurement Service / 나라장터) integration.

Disabled by default. When all of the following env vars are set, an actual
call is made; otherwise the module returns empty results plus the conventional
"disabled or missing config" error string and the workflow continues.

Env vars (all required to enable):
  ENABLE_G2B=true
  G2B_SERVICE_KEY=...           # supplied via GitHub Actions secret
  G2B_BID_ENDPOINT=https://...  # bid-notice API endpoint
  G2B_SPEC_ENDPOINT=https://... # pre-specification API endpoint

Constraints:
- No API keys are hardcoded.
- No "나라장터" appears in the search keywords (it is the API itself).
- Planning-only notices (타당성 조사, 기본계획, ISP, BPR, ...) are filtered out.
- Network failures degrade gracefully — never crash the run.
"""

from __future__ import annotations

import os
import time
from typing import Any

import requests

# Procurement keywords — the actual buying signals. Do NOT include "나라장터".
G2B_KEYWORDS: list[str] = [
    "AI 시스템 구축",
    "인공지능 시스템 구축",
    "생성형 AI",
    "생성AI",
    "LLM",
    "RAG",
    "AI 에이전트",
    "AI 플랫폼",
    "AI CCTV",
    "지능형 관제",
    "GPU 서버",
    "GPU 클러스터",
    "AI 인프라",
    "망분리 AI",
    "폐쇄망 AI",
    "프라이빗 AI",
    "온프레미스 AI",
    "NPU",
    "NPU 서버",
    "AI 반도체",
    "추론 서버",
    "추론 가속기",
]

# Planning-only notices we never want surfaced as buying signals.
G2B_PLANNING_FILTERS: list[str] = [
    "타당성 조사",
    "기본계획 수립",
    "연구용역",
    "정책연구",
    "컨설팅",
    "마스터플랜",
    "정보화전략계획",
    "ISP",
    "BPR",
]

DISABLED_MSG = "disabled or missing config"


def is_enabled() -> bool:
    return os.getenv("ENABLE_G2B", "false").strip().lower() == "true"


def _service_key() -> str:
    return os.getenv("G2B_SERVICE_KEY", "").strip()


def _bid_endpoint() -> str:
    return os.getenv("G2B_BID_ENDPOINT", "").strip()


def _spec_endpoint() -> str:
    return os.getenv("G2B_SPEC_ENDPOINT", "").strip()


def _config_complete() -> bool:
    return bool(_service_key()) and bool(_bid_endpoint()) and bool(_spec_endpoint())


def is_planning_only(title: str) -> bool:
    if not title:
        return False
    return any(token in title for token in G2B_PLANNING_FILTERS)


def _extract_items(payload: Any) -> list[dict[str, Any]]:
    """Be tolerant of the various nested shapes the G2B JSON APIs use."""
    if not isinstance(payload, dict):
        return []
    response = payload.get("response", payload)
    body = response.get("body", response) if isinstance(response, dict) else {}
    items = body.get("items") if isinstance(body, dict) else None
    if isinstance(items, dict):
        items = items.get("item")
    if isinstance(items, list):
        return [i for i in items if isinstance(i, dict)]
    if isinstance(items, dict):
        return [items]
    return []


def _request(endpoint: str, keyword: str) -> list[dict[str, Any]]:
    params = {
        "serviceKey": _service_key(),
        "numOfRows": 10,
        "pageNo": 1,
        "type": "json",
        "bidNtceNm": keyword,
        "inqryDiv": 1,
    }
    response = requests.get(endpoint, params=params, timeout=20)
    response.raise_for_status()
    try:
        return _extract_items(response.json())
    except ValueError:
        return []


def _normalize_bid(item: dict[str, Any], keyword: str) -> dict[str, Any]:
    title = (
        item.get("bidNtceNm")
        or item.get("bsnsNm")
        or item.get("ntceNm")
        or ""
    )
    return {
        "source": "g2b_bid",
        "keyword": keyword,
        "title": title,
        "agency": item.get("ntceInsttNm", ""),
        "url": item.get("bidNtceUrl") or item.get("ntceUrl") or "",
        "deadline": item.get("bidNtceDt") or item.get("ntceDt") or "",
        "raw": item,
    }


def _normalize_spec(item: dict[str, Any], keyword: str) -> dict[str, Any]:
    title = (
        item.get("prdctClsfcNoNm")
        or item.get("dtlsBsnsNm")
        or item.get("bsnsNm")
        or ""
    )
    return {
        "source": "g2b_spec",
        "keyword": keyword,
        "title": title,
        "agency": item.get("dminsttNm", ""),
        "url": item.get("specPblancUrl") or item.get("specDocFileUrl") or "",
        "raw": item,
    }


def fetch_bid_notices() -> list[dict[str, Any]]:
    endpoint = _bid_endpoint()
    if not endpoint or not _service_key():
        return []
    items: list[dict[str, Any]] = []
    for keyword in G2B_KEYWORDS:
        try:
            raw_items = _request(endpoint, keyword)
        except Exception as exc:
            print(f"G2B bid keyword failed '{keyword}': {exc}")
            continue
        for raw in raw_items:
            norm = _normalize_bid(raw, keyword)
            if is_planning_only(norm["title"]):
                continue
            items.append(norm)
        time.sleep(0.2)
    return items


def fetch_pre_specs() -> list[dict[str, Any]]:
    endpoint = _spec_endpoint()
    if not endpoint or not _service_key():
        return []
    items: list[dict[str, Any]] = []
    for keyword in G2B_KEYWORDS:
        try:
            raw_items = _request(endpoint, keyword)
        except Exception as exc:
            print(f"G2B spec keyword failed '{keyword}': {exc}")
            continue
        for raw in raw_items:
            norm = _normalize_spec(raw, keyword)
            if is_planning_only(norm["title"]):
                continue
            items.append(norm)
        time.sleep(0.2)
    return items


def collect() -> tuple[list[dict[str, Any]], list[dict[str, Any]], str]:
    """
    Returns (bid_items, spec_items, error_string).
      error_string == "" on success (data may still be empty).
      error_string == DISABLED_MSG when ENABLE_G2B!=true or any required
        config var is missing — this is the no-op path.
      error_string == <message> on actual network/parse failure.
    """
    if not is_enabled():
        return [], [], DISABLED_MSG
    if not _config_complete():
        return [], [], DISABLED_MSG
    try:
        bid = fetch_bid_notices()
        spec = fetch_pre_specs()
        return bid, spec, ""
    except Exception as exc:
        return [], [], str(exc)
