"""
Optional G2B (Korea Public Procurement Service / 나라장터) integration.

Disabled by default. When all of the following env vars are set, an actual
call is made; otherwise the module returns empty results plus the conventional
"disabled or missing config" error string and the workflow continues.

Env vars (all required to enable):
  ENABLE_G2B=true
  G2B_SERVICE_KEY=...           # supplied via GitHub Actions secret
  G2B_BID_ENDPOINT=https://...  # bid-notice service root (operations are appended)
  G2B_SPEC_ENDPOINT=https://... # pre-spec service root (operations are appended)

Per-keyword fan-out:
  Each bid keyword calls both /getBidPblancListInfoServc and /getBidPblancListInfoThng.
  Each spec keyword calls both /getPublicPrcureThngInfoServc and /getPublicPrcureThngInfoThng.

Operation names are baked into BID_OPERATIONS / SPEC_OPERATIONS below — users
do not need to paste them into the workflow UI.

Constraints:
- No API keys are hardcoded.
- No "나라장터" appears in the search keywords (it is the API itself).
- Planning-only notices (타당성 조사, 기본계획, ISP, BPR, ...) are filtered out.
- Network failures degrade gracefully — never crash the run.
"""

from __future__ import annotations

import os
import time
from datetime import datetime, timedelta
from typing import Any
from zoneinfo import ZoneInfo

import requests

# data.go.kr operation paths — appended to the service-root URL per request.
BID_OPERATIONS: list[str] = [
    "/getBidPblancListInfoServc",
    "/getBidPblancListInfoThng",
]
SPEC_OPERATIONS: list[str] = [
    "/getPublicPrcureThngInfoServc",
    "/getPublicPrcureThngInfoThng",
]

# Recent-window for the inqryBgnDt / inqryEndDt query params.
_LOOKBACK_DAYS = 30

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


def _join_operation(endpoint: str, operation: str) -> str:
    """
    Append a single operation path to a service-root endpoint.
    Strips trailing slash from endpoint, ensures exactly one leading slash
    on operation, leaves `https://` (and similar schemes) untouched.
    Returns "" if endpoint is empty.
    """
    if not endpoint:
        return ""
    if not operation:
        return endpoint
    return endpoint.rstrip("/") + "/" + operation.lstrip("/")


def bid_urls() -> list[str]:
    root = _bid_endpoint()
    if not root:
        return []
    return [_join_operation(root, op) for op in BID_OPERATIONS]


def spec_urls() -> list[str]:
    root = _spec_endpoint()
    if not root:
        return []
    return [_join_operation(root, op) for op in SPEC_OPERATIONS]


def _config_complete() -> bool:
    return bool(_service_key()) and bool(_bid_endpoint()) and bool(_spec_endpoint())


def _date_window() -> tuple[str, str]:
    """Returns (inqryBgnDt, inqryEndDt) for the last _LOOKBACK_DAYS, KST."""
    now = datetime.now(ZoneInfo("Asia/Seoul"))
    begin = (now - timedelta(days=_LOOKBACK_DAYS)).strftime("%Y%m%d") + "0000"
    end = now.strftime("%Y%m%d") + "2359"
    return begin, end


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


def _request(
    url: str,
    keyword: str,
    inqry_bgn: str,
    inqry_end: str,
) -> list[dict[str, Any]]:
    params = {
        "serviceKey": _service_key(),
        "pageNo": 1,
        "numOfRows": 10,
        "type": "json",
        "inqryDiv": 1,
        "bidNtceNm": keyword,
        "inqryBgnDt": inqry_bgn,
        "inqryEndDt": inqry_end,
    }
    response = requests.get(url, params=params, timeout=20)
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


def _short_exc(exc: BaseException) -> str:
    cls = exc.__class__.__name__
    msg = str(exc).strip().splitlines()[0] if str(exc).strip() else ""
    return f"{cls}: {msg}"[:240] if msg else cls


def _fetch_keyword_loop(
    urls: list[str],
    normalize: Any,
    label: str,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """
    Shared loop. For each G2B_KEYWORDS entry, calls every URL in `urls`.
    Returns (items, telemetry). called_count is the total number of HTTP
    attempts (keywords × operations). last_error is the most recent failure
    so the caller can surface a real summary when every attempt failed.
    """
    telemetry: dict[str, Any] = {
        "called_count": 0,
        "error_count": 0,
        "last_error": "",
    }
    items: list[dict[str, Any]] = []
    if not urls or not _service_key():
        return items, telemetry

    inqry_bgn, inqry_end = _date_window()

    for keyword in G2B_KEYWORDS:
        for url in urls:
            telemetry["called_count"] += 1
            try:
                raw_items = _request(url, keyword, inqry_bgn, inqry_end)
            except Exception as exc:
                telemetry["error_count"] += 1
                telemetry["last_error"] = _short_exc(exc)
                print(
                    f"G2B {label} '{keyword}' @ "
                    f"{url.rsplit('/', 1)[-1]} failed: {telemetry['last_error']}"
                )
                continue
            for raw in raw_items:
                norm = normalize(raw, keyword)
                if is_planning_only(norm["title"]):
                    continue
                items.append(norm)
            time.sleep(0.2)
    return items, telemetry


def fetch_bid_notices() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    return _fetch_keyword_loop(bid_urls(), _normalize_bid, "bid")


def fetch_pre_specs() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    return _fetch_keyword_loop(spec_urls(), _normalize_spec, "spec")


def collect() -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[str, Any]]:
    """
    Returns (bid_items, spec_items, telemetry_dict). telemetry_dict shape:
      {
        "error":              "" | DISABLED_MSG | <concise failure summary>,
        "bid_called_count":   int,
        "bid_error_count":    int,
        "bid_last_error":     str,
        "spec_called_count":  int,
        "spec_error_count":   int,
        "spec_last_error":    str,
      }

    error == "" only when no failures occurred. When every bid call or every
    spec call failed, error is a concise summary so metadata never claims
    "none" while in fact every request 404'd.
    """
    empty_telemetry = {
        "error": "",
        "bid_called_count": 0,
        "bid_error_count": 0,
        "bid_last_error": "",
        "spec_called_count": 0,
        "spec_error_count": 0,
        "spec_last_error": "",
    }

    if not is_enabled():
        return [], [], {**empty_telemetry, "error": DISABLED_MSG}
    if not _config_complete():
        return [], [], {**empty_telemetry, "error": DISABLED_MSG}

    try:
        bid_items, bid_t = fetch_bid_notices()
        spec_items, spec_t = fetch_pre_specs()
    except Exception as exc:
        return [], [], {**empty_telemetry, "error": _short_exc(exc)}

    parts: list[str] = []
    all_bid_failed = bid_t["called_count"] > 0 and bid_t["error_count"] == bid_t["called_count"]
    all_spec_failed = spec_t["called_count"] > 0 and spec_t["error_count"] == spec_t["called_count"]
    if all_bid_failed:
        parts.append(
            f"all bid keyword calls failed "
            f"({bid_t['error_count']}/{bid_t['called_count']}): {bid_t['last_error']}"
        )
    if all_spec_failed:
        parts.append(
            f"all spec keyword calls failed "
            f"({spec_t['error_count']}/{spec_t['called_count']}): {spec_t['last_error']}"
        )

    telemetry = {
        "error": "; ".join(parts),
        "bid_called_count": bid_t["called_count"],
        "bid_error_count": bid_t["error_count"],
        "bid_last_error": bid_t["last_error"],
        "spec_called_count": spec_t["called_count"],
        "spec_error_count": spec_t["error_count"],
        "spec_last_error": spec_t["last_error"],
    }
    return bid_items, spec_items, telemetry
