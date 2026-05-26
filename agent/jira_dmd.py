"""
Optional Jira DMD (Demand_Manufacture_Delivery) integration.

The board lists every active customer/prospect deal at Furiosa. When we match
a GTM candidate against an existing DMD issue summary, we surface it as
"기존 접점: <회사명> ✅" in the report. Used to gate that signal so BD does not
re-contact a company that's already being handled.

The Jira name itself never appears in the manager-facing report (per spec).
We just need the summary field for substring matching.

Env vars (all required to enable):
  ENABLE_JIRA=true
  JIRA_URL=https://furiosa-ai.atlassian.net
  JIRA_EMAIL=boyoon.jung@furiosa.ai
  JIRA_API_TOKEN=ATAT...            (Atlassian API token; starts with "ATAT")
  JIRA_DMD_PROJECT_KEY=DMD          (optional, defaults to "DMD")

API token is created at id.atlassian.com → Security → API tokens.
Basic auth uses (email, api_token) as the username/password pair.

Network failures degrade silently — every existing_touchpoint becomes
"확인 필요" in that case, so we never invent a contact.
"""

from __future__ import annotations

import base64
import os
import re
from typing import Any

import requests

DISABLED_MSG = "disabled or missing config"


def is_enabled() -> bool:
    if os.getenv("ENABLE_JIRA", "false").strip().lower() != "true":
        return False
    return all(
        bool(os.getenv(name, "").strip())
        for name in ("JIRA_URL", "JIRA_EMAIL", "JIRA_API_TOKEN")
    )


def _project_key() -> str:
    return (os.getenv("JIRA_DMD_PROJECT_KEY") or "DMD").strip()


def _auth_header() -> dict[str, str]:
    email = os.getenv("JIRA_EMAIL", "").strip()
    token = os.getenv("JIRA_API_TOKEN", "").strip()
    basic = base64.b64encode(f"{email}:{token}".encode("utf-8")).decode("ascii")
    return {
        "Authorization": f"Basic {basic}",
        "Accept": "application/json",
    }


def _short_exc(exc: BaseException) -> str:
    cls = exc.__class__.__name__
    msg = str(exc).strip().splitlines()[0] if str(exc).strip() else ""
    # Strip basic-auth credentials and any URL token leaks from logs.
    msg = re.sub(r"(?i)(Authorization[^,]*)", "Authorization: ***", msg)
    msg = re.sub(r"(?i)(token=)[^&\s\"']+", r"\1***", msg)
    return f"{cls}: {msg}"[:240] if msg else cls


def fetch_dmd_summaries() -> tuple[list[dict[str, Any]], str]:
    """
    Returns (summaries, error). summaries is a list of {key, summary, status}.
    error is "" on success, DISABLED_MSG when not enabled, or a short message
    on network/auth failure.

    Uses POST /rest/api/3/search/jql — the legacy GET /rest/api/3/search
    endpoint started returning 410 Gone after Atlassian's 2025 migration.
    The new endpoint paginates with nextPageToken instead of startAt.
    """
    if not is_enabled():
        return [], DISABLED_MSG

    base = os.getenv("JIRA_URL", "").strip().rstrip("/")
    project = _project_key()
    url = f"{base}/rest/api/3/search/jql"
    headers = {
        **_auth_header(),
        "Content-Type": "application/json",
    }

    out: list[dict[str, Any]] = []
    next_page_token: str | None = None
    try:
        for _ in range(10):  # safety cap: 10 pages × 100 issues = 1000 max
            body: dict[str, Any] = {
                "jql": f"project = {project} ORDER BY updated DESC",
                "fields": ["summary", "status"],
                "maxResults": 100,
            }
            if next_page_token:
                body["nextPageToken"] = next_page_token
            response = requests.post(url, headers=headers, json=body, timeout=20)
            response.raise_for_status()
            payload = response.json() or {}
            issues = payload.get("issues") or []
            for issue in issues:
                if not isinstance(issue, dict):
                    continue
                fields = issue.get("fields") or {}
                summary = fields.get("summary") or ""
                status_obj = fields.get("status") or {}
                status_name = (
                    status_obj.get("name") if isinstance(status_obj, dict) else ""
                ) or ""
                out.append(
                    {
                        "key": issue.get("key") or "",
                        "summary": str(summary),
                        "status": str(status_name),
                    }
                )
            next_page_token = payload.get("nextPageToken")
            if not next_page_token:
                break
    except Exception as exc:
        return [], _short_exc(exc)

    return out, ""


# Used to normalize both candidate names and DMD summary text so substring
# matching survives spacing / punctuation / case differences.
_NAME_NORMALIZE_RE = re.compile(r"[\s\(\)\[\]\{\}\.\,\-_/]+")


def normalize_company_name(name: str) -> str:
    if not name:
        return ""
    base = name.strip().lower()
    base = base.replace("주식회사", "").replace("(주)", "").replace("inc.", "")
    base = base.replace("corporation", "").replace("corp.", "").replace("ltd.", "")
    return _NAME_NORMALIZE_RE.sub("", base)


def match_candidate_to_summaries(
    candidate_name: str,
    summaries: list[dict[str, Any]],
) -> dict[str, Any] | None:
    """
    Return the first DMD issue whose summary contains the normalized candidate
    name (or the candidate name contains the summary's first token — rare).
    None when no match.
    """
    if not candidate_name or not summaries:
        return None
    norm_cand = normalize_company_name(candidate_name)
    if len(norm_cand) < 2:
        return None
    for issue in summaries:
        norm_sum = normalize_company_name(issue.get("summary", ""))
        if norm_cand in norm_sum:
            return issue
    return None


def apply_existing_touchpoints(
    candidates: list[dict[str, Any]],
) -> tuple[int, str]:
    """
    Mutates candidates in place. Sets existing_touchpoint to "<company> ✅"
    when matched, otherwise "확인 필요". Returns (match_count, error).
    The string Jira never appears in the value the report sees.
    """
    summaries, error = fetch_dmd_summaries()
    if error:
        # Already-normalised state from _enforce_existing_touchpoint_when_jira_off
        # is acceptable on failure — keep silent and let the no-op rule stand.
        return 0, error

    match_count = 0
    for candidate in candidates:
        if not isinstance(candidate, dict):
            continue
        name = candidate.get("name") or ""
        matched = match_candidate_to_summaries(name, summaries)
        if matched:
            candidate["existing_touchpoint"] = f"{name} ✅"
            match_count += 1
        else:
            candidate["existing_touchpoint"] = "확인 필요"
    return match_count, ""
