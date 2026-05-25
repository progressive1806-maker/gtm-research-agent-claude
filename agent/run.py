from __future__ import annotations

import csv
import html
import json
import os
import re
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any
from urllib.parse import urlparse
from zoneinfo import ZoneInfo

import feedparser
import requests
from bs4 import BeautifulSoup
from google import genai

sys.path.insert(0, str(Path(__file__).resolve().parent))
from decision_makers import enrich_candidates_with_profiles  # noqa: E402


ROOT = Path(__file__).resolve().parents[1]
RUNS_DIR = ROOT / "runs"
DOCS_DIR = ROOT / "docs"
PROMPT_PATH = ROOT / "prompts" / "gtm_agent_instructions.md"

NAVER_NEWS_URL = "https://openapi.naver.com/v1/search/news.json"

AGENT_VERSION = "v0.7"


BASE_NAVER_QUERIES = [
    "생성형 AI 도입 기업",
    "LLM 플랫폼 출시",
    "AI 데이터센터",
    "GPU 클라우드",
    "AI inference",
    "private AI",
    "RAG 플랫폼",
    "OpenAI 호환 API",
    "vLLM",
    "AI 상담 에이전트",
    "금융 생성형 AI",
    "병원 AI 플랫폼",
    "제조 AI 플랫폼",
    "클라우드 AI 서비스",
    "삼성SDS SCP AI",
    "NPUaaS",
    "GPU 비용 절감",
    "AI 추론 비용",
    "나라장터 AI 시스템 구축",
    "나라장터 생성형 AI",
    "나라장터 LLM",
    "나라장터 RAG",
    "나라장터 AI CCTV",
    "나라장터 지능형 관제",
    "나라장터 GPU 서버",
    "국방 AI 인프라",
    "망분리 AI",
    "폐쇄망 AI",
]


RSS_FEEDS = [
    {
        "name": "Google News KR 생성형 AI",
        "url": "https://news.google.com/rss/search?q=%EC%83%9D%EC%84%B1%ED%98%95%20AI%20%EA%B8%B0%EC%97%85&hl=ko&gl=KR&ceid=KR:ko",
        "country": "KR",
        "category": "news",
    },
    {
        "name": "Google News KR AI 데이터센터",
        "url": "https://news.google.com/rss/search?q=AI%20%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%84%BC%ED%84%B0&hl=ko&gl=KR&ceid=KR:ko",
        "country": "KR",
        "category": "infrastructure",
    },
    {
        "name": "Google News KR 나라장터 AI",
        "url": "https://news.google.com/rss/search?q=%EB%82%98%EB%9D%BC%EC%9E%A5%ED%84%B0%20AI&hl=ko&gl=KR&ceid=KR:ko",
        "country": "KR",
        "category": "b2g",
    },
    {
        "name": "Google News JP 生成AI 導入",
        "url": "https://news.google.com/rss/search?q=%E7%94%9F%E6%88%90AI%20%E5%B0%8E%E5%85%A5&hl=ja&gl=JP&ceid=JP:ja",
        "country": "JP",
        "category": "news",
    },
    {
        "name": "Google News JP AI cloud",
        "url": "https://news.google.com/rss/search?q=AI%20cloud%20Japan&hl=ja&gl=JP&ceid=JP:ja",
        "country": "JP",
        "category": "cloud",
    },
    {
        "name": "Google News JP LLM platform",
        "url": "https://news.google.com/rss/search?q=LLM%20platform%20Japan&hl=ja&gl=JP&ceid=JP:ja",
        "country": "JP",
        "category": "llm",
    },
]


FURIOSA_DOCS = [
    {
        "name": "Supported Models",
        "url": "https://developer.furiosa.ai/latest/en/overview/supported_models.html",
        "category": "models",
    },
    {
        "name": "Release 2026.2",
        "url": "https://developer.furiosa.ai/docs-dev/PR-3475/en/whatsnew/release-2026.2.html",
        "category": "release",
    },
    {
        "name": "RNGD Overview",
        "url": "https://developer.furiosa.ai/latest/en/overview/rngd.html",
        "category": "hardware",
    },
    {
        "name": "Software Stack",
        "url": "https://developer.furiosa.ai/latest/en/overview/software_stack.html",
        "category": "software",
    },
    {
        "name": "Roadmap",
        "url": "https://developer.furiosa.ai/latest/en/overview/roadmap.html",
        "category": "roadmap",
    },
    {
        "name": "Furiosa LLM Intro",
        "url": "https://developer.furiosa.ai/latest/en/furiosa_llm/intro.html",
        "category": "serving",
    },
    {
        "name": "Cloud Native Toolkit",
        "url": "https://developer.furiosa.ai/latest/en/cloud_native_toolkit/intro.html",
        "category": "cloud_native",
    },
    {
        "name": "System Management Interface",
        "url": "https://developer.furiosa.ai/latest/en/device_management/system_management_interface.html",
        "category": "management",
    },
    {
        "name": "Hugging Face FuriosaAI Org",
        "url": "https://huggingface.co/furiosa-ai",
        "category": "huggingface",
    },
    {
        "name": "Hugging Face FuriosaAI Models",
        "url": "https://huggingface.co/furiosa-ai/models",
        "category": "huggingface_models",
    },
    {
        "name": "Hugging Face FuriosaAI Collections",
        "url": "https://huggingface.co/furiosa-ai/collections",
        "category": "huggingface_collections",
    },
]


def now_kst() -> datetime:
    return datetime.now(ZoneInfo("Asia/Seoul"))


def env_int(name: str, default: int) -> int:
    raw = os.getenv(name, "")
    try:
        return int(raw)
    except Exception:
        return default


MAX_DYNAMIC_MODEL_QUERIES = env_int("MAX_DYNAMIC_MODEL_QUERIES", 300)
MAX_LLM_SOURCES = env_int("MAX_LLM_SOURCES", 40)
MAX_SOURCE_CHARS = env_int("MAX_SOURCE_CHARS", 800)
MAX_OUTPUT_CANDIDATES = env_int("MAX_OUTPUT_CANDIDATES", 12)


def safe_text(value: str | None, default: str) -> str:
    value = value or default
    allowed = []
    for ch in value:
        if ch.isalnum() or ch in "-_.":
            allowed.append(ch)
        else:
            allowed.append("-")
    return "".join(allowed).strip("-") or default


def build_run_id(mode: str, memo: str | None) -> str:
    ts = now_kst().strftime("%Y-%m-%d_%H%M%S")
    memo_part = safe_text(memo, "manual")[:40]
    return f"{ts}_{mode}_{memo_part}"


def load_instructions() -> str:
    if not PROMPT_PATH.exists():
        return ""
    return PROMPT_PATH.read_text(encoding="utf-8")


def strip_html_tags(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text or "")
    return html.unescape(text).strip()


def normalize_url(url: str) -> str:
    if not url:
        return ""
    parsed = urlparse(url)
    return parsed._replace(query="", fragment="").geturl()


def parse_naver_pubdate(pub_date: str) -> str | None:
    try:
        dt = datetime.strptime(pub_date, "%a, %d %b %Y %H:%M:%S %z")
        return dt.astimezone(ZoneInfo("Asia/Seoul")).isoformat()
    except Exception:
        return None


def parse_struct_time_to_kst(entry: Any) -> str | None:
    parsed = getattr(entry, "published_parsed", None) or getattr(entry, "updated_parsed", None)
    if not parsed:
        return None
    try:
        dt_utc = datetime(*parsed[:6], tzinfo=ZoneInfo("UTC"))
        return dt_utc.astimezone(ZoneInfo("Asia/Seoul")).isoformat()
    except Exception:
        return None


def is_recent_kst(iso_date: str | None, days: int = 7) -> bool:
    if not iso_date:
        return False
    try:
        dt = datetime.fromisoformat(iso_date)
    except Exception:
        return False
    cutoff = now_kst() - timedelta(days=days)
    return dt >= cutoff


def fetch_naver_news(query: str, display: int = 10) -> list[dict[str, Any]]:
    client_id = os.getenv("NAVER_CLIENT_ID", "")
    client_secret = os.getenv("NAVER_CLIENT_SECRET", "")

    if not client_id or not client_secret:
        raise RuntimeError(
            "NAVER_CLIENT_ID or NAVER_CLIENT_SECRET is missing. "
            "Add them in GitHub Settings > Secrets and variables > Actions."
        )

    headers = {
        "X-Naver-Client-Id": client_id,
        "X-Naver-Client-Secret": client_secret,
    }
    params = {
        "query": query,
        "display": display,
        "start": 1,
        "sort": "date",
    }

    response = requests.get(
        NAVER_NEWS_URL,
        headers=headers,
        params=params,
        timeout=20,
    )
    response.raise_for_status()

    data = response.json()
    items = data.get("items", [])

    results = []
    for item in items:
        published_at = parse_naver_pubdate(item.get("pubDate", ""))
        result = {
            "query": query,
            "title": strip_html_tags(item.get("title", "")),
            "description": strip_html_tags(item.get("description", "")),
            "originallink": item.get("originallink", ""),
            "link": item.get("link", ""),
            "published_at_kst": published_at,
            "source": "naver_news_api",
        }
        results.append(result)

    return results


def collect_naver_sources(queries: list[str]) -> list[dict[str, Any]]:
    all_items: list[dict[str, Any]] = []

    for query in queries:
        try:
            items = fetch_naver_news(query=query, display=10)
            all_items.extend(items)
            print(f"Naver query OK: {query} ({len(items)} items)")
            time.sleep(0.2)
        except Exception as exc:
            print(f"Naver query FAILED: {query} / {exc}")

    return dedupe_and_filter_recent(all_items)


def fetch_rss_feed(feed: dict[str, str]) -> list[dict[str, Any]]:
    parsed = feedparser.parse(feed["url"])
    results = []

    for entry in parsed.entries:
        published_at = parse_struct_time_to_kst(entry)
        link = getattr(entry, "link", "")
        title = strip_html_tags(getattr(entry, "title", ""))
        summary = strip_html_tags(getattr(entry, "summary", ""))

        results.append(
            {
                "feed_name": feed["name"],
                "feed_url": feed["url"],
                "country": feed.get("country", ""),
                "category": feed.get("category", ""),
                "title": title,
                "description": summary,
                "originallink": link,
                "link": link,
                "published_at_kst": published_at,
                "source": "rss",
            }
        )

    return results


def collect_rss_sources() -> list[dict[str, Any]]:
    all_items: list[dict[str, Any]] = []

    for feed in RSS_FEEDS:
        try:
            items = fetch_rss_feed(feed)
            all_items.extend(items)
            print(f"RSS feed OK: {feed['name']} ({len(items)} items)")
            time.sleep(0.2)
        except Exception as exc:
            print(f"RSS feed FAILED: {feed['name']} / {exc}")

    return dedupe_and_filter_recent(all_items)

MODEL_QUERY_TEMPLATES_ON_PREM_KR = [
    "{model} 도입",
    "{model} 기업",
    "{model} RAG",
    "{model} 금융",
    "{model} 병원",
    "{model} 제조",
    "{model} 온프레미스",
    "{model} 프라이빗 AI",
    "{model} 망분리",
    "{model} 폐쇄망",
    "{model} vLLM",
    "{model} OpenAI 호환",
]

MODEL_QUERY_TEMPLATES_CSP_OPERATOR_KR = [
    "{model} 클라우드",
    "{model} API 서비스",
    "{model} 추론 서비스",
    "{model} inference service",
    "{model} GPU 클라우드",
    "{model} AI 클라우드",
    "{model} CSP",
    "{model} MSP",
    "{model} 데이터센터",
    "{model} vLLM 클라우드",
    "{model} OpenAI 호환 API",
]

MODEL_QUERY_TEMPLATES_CSP_CUSTOMER_KR = [
    "{model} SaaS",
    "{model} AI 서비스",
    "{model} 상담 서비스",
    "{model} 검색 서비스",
    "{model} 에이전트",
    "{model} RAG 서비스",
    "{model} 클라우드 도입",
    "{model} 삼성SDS SCP",
    "{model} SCP",
    "{model} GPU 비용",
    "{model} 추론 비용",
]

MODEL_QUERY_TEMPLATES_JP = [
    "{model} 導入",
    "{model} 企業",
    "{model} RAG",
    "{model} vLLM",
    "{model} オンプレミス",
    "{model} プライベートAI",
    "{model} AIクラウド",
    "{model} inference service",
    "{model} Japan",
]

CSP_ROUTE_QUERIES = [
    "삼성SDS SCP AI",
    "삼성SDS SCP 생성형 AI",
    "삼성SDS 클라우드 AI",
    "삼성SDS 클라우드 GPU",
    "삼성SDS 클라우드 고객 AI",
    "SCP 클라우드 AI 추론",
    "SCP 생성형 AI 고객",
    "국내 CSP AI 추론 서비스",
    "국내 클라우드 GPU 서비스",
    "국내 GPUaaS AI 클라우드",
    "NPUaaS 고객",
    "NPUaaS 추론 서비스",
    "AI inference as a service",
    "클라우드 기반 RAG 서비스",
    "클라우드 AI 상담 서비스",
    "클라우드 AI 에이전트 서비스",
    "프라이빗 AI 클라우드",
]

B2G_ROUTE_QUERIES = [
    "나라장터 AI 시스템 구축",
    "나라장터 생성형 AI",
    "나라장터 LLM",
    "나라장터 RAG",
    "나라장터 AI CCTV",
    "나라장터 지능형 관제",
    "나라장터 GPU 서버",
    "나라장터 AI 인프라",
    "나라장터 망분리 AI",
    "나라장터 폐쇄망 AI",
    "조달청 AI 플랫폼 구축",
    "공공 생성형 AI 구축",
    "공공 RAG 구축",
    "국방 AI 인프라",
    "병원 AI 플랫폼 구축",
]

COMPETITOR_GTM_QUERIES = [
    "리벨리온 고객 납품",
    "리벨리온 클라우드 파트너십",
    "리벨리온 NPUaaS",
    "리벨리온 공공 수주",
    "사피온 고객 납품",
    "사피온 클라우드 파트너십",
    "사피온 공공 수주",
    "하이퍼엑셀 고객 납품",
    "하이퍼엑셀 CSP 파트너십",
    "퓨리오사 경쟁사 NPU 클라우드",
]


def model_to_search_terms(model_name: str) -> list[str]:
    lowered = model_name.strip().lower()
    terms: list[str] = []

    if "exaone-4.0" in lowered or "exaone 4.0" in lowered:
        terms.extend(["EXAONE 4.0", "엑사원 4.0"])

    if "exaone-3.5" in lowered or "exaone 3.5" in lowered:
        terms.extend(["EXAONE 3.5", "엑사원 3.5"])

    if "qwen3" in lowered or "qwen 3" in lowered:
        terms.extend(["Qwen3", "Qwen 3"])

        if "embedding" in lowered:
            terms.extend(["Qwen3 Embedding", "Qwen 3 Embedding"])

        if "reranker" in lowered:
            terms.extend(["Qwen3 Reranker", "Qwen 3 Reranker"])

    if "qwen2.5" in lowered or "qwen 2.5" in lowered:
        terms.extend(["Qwen2.5", "Qwen 2.5"])

    if "qwen2" in lowered or "qwen 2" in lowered:
        terms.extend(["Qwen2", "Qwen 2"])

    if "llama-3.3" in lowered or "llama 3.3" in lowered:
        terms.extend(["Llama 3.3", "Llama-3.3"])

    if "llama-3.1" in lowered or "llama 3.1" in lowered:
        terms.extend(["Llama 3.1", "Llama-3.1"])

    if "deepseek-r1" in lowered or "deepseek r1" in lowered:
        terms.extend(["DeepSeek R1", "DeepSeek-R1"])

    if "solar" in lowered:
        terms.extend(["Solar 1.0", "SOLAR"])

    if "qwq" in lowered:
        terms.extend(["QwQ"])

    if "gpt-oss" in lowered:
        terms.extend(["GPT-OSS"])

    if "k-exaone" in lowered:
        terms.extend(["K-EXAONE"])

    return list(dict.fromkeys(terms))


def build_dynamic_model_queries(furiosa_docs_summary: dict[str, Any]) -> list[str]:
    entries: list[dict[str, Any]] = []

    for key in [
        "supported_model_entries",
        "precompiled_model_entries",
        "planned_model_entries",
    ]:
        entries.extend(furiosa_docs_summary.get(key, []))

    search_terms: list[str] = []

    for entry in entries:
        model_name = entry.get("model_name", "")
        status = entry.get("status", "")

        terms = model_to_search_terms(model_name)

        # planned 모델은 아직 현재 지원 확정이 아니므로 검색량을 줄임
        if "planned" in status:
            terms = terms[:1]

        search_terms.extend(terms)

    # 중복 제거
    search_terms = list(dict.fromkeys(search_terms))

    # 너무 비슷한 alias가 쿼리를 다 먹지 않게 대표 term 중심으로 압축
    preferred_order = [
        "EXAONE 4.0",
        "엑사원 4.0",
        "EXAONE 3.5",
        "엑사원 3.5",
        "Llama 3.3",
        "Llama 3.1",
        "Qwen3",
        "Qwen 3",
        "Qwen2.5",
        "Qwen 2.5",
        "Qwen2",
        "Qwen 2",
        "DeepSeek R1",
        "DeepSeek-R1",
        "Solar 1.0",
        "SOLAR",
        "QwQ",
        "GPT-OSS",
        "K-EXAONE",
    ]

    ordered_terms: list[str] = []
    for term in preferred_order:
        if term in search_terms:
            ordered_terms.append(term)

    for term in search_terms:
        if term not in ordered_terms:
            ordered_terms.append(term)

    # 모델 하나가 40개씩 먹지 않게 모델별 핵심 쿼리 수를 제한
    per_model_templates_kr = [
        "{model} 도입",
        "{model} 기업",
        "{model} RAG",
        "{model} vLLM",
        "{model} 클라우드",
        "{model} 추론 서비스",
        "{model} 온프레미스",
        "{model} 삼성SDS SCP",
    ]

    per_model_templates_jp = [
        "{model} 導入",
        "{model} 企業",
        "{model} RAG",
        "{model} AIクラウド",
    ]

    queries: list[str] = []

    for term in ordered_terms:
        for template in per_model_templates_kr:
            queries.append(template.format(model=term))

        # 한글 alias에는 일본어 쿼리 붙이지 않음
        if not any(korean in term for korean in ["엑사원"]):
            for template in per_model_templates_jp:
                queries.append(template.format(model=term))

    queries = list(dict.fromkeys(queries))

    # 전체 제한은 유지하되, 모델별로 골고루 들어가게 만든 뒤 자름
    return queries[:MAX_DYNAMIC_MODEL_QUERIES]

def dedupe_and_filter_recent(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    deduped: dict[str, dict[str, Any]] = {}

    for item in items:
        url = normalize_url(item.get("originallink") or item.get("link") or "")
        if not url:
            key = item.get("title", "")
        else:
            key = url

        if key and key not in deduped:
            deduped[key] = item

    recent_items = [
        item for item in deduped.values()
        if is_recent_kst(item.get("published_at_kst"), days=7)
    ]

    recent_items.sort(
        key=lambda x: x.get("published_at_kst") or "",
        reverse=True,
    )

    return recent_items


def merge_sources(
    naver_sources: list[dict[str, Any]],
    rss_sources: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    return dedupe_and_filter_recent(naver_sources + rss_sources)


def extract_clean_text_from_html(html_text: str) -> str:
    soup = BeautifulSoup(html_text, "html.parser")

    for tag in soup(["script", "style", "nav", "footer", "header"]):
        tag.decompose()

    main = soup.find("main")
    if main:
        text = main.get_text("\n")
    else:
        text = soup.get_text("\n")

    lines = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        if len(line) <= 2:
            continue
        lines.append(line)

    cleaned = "\n".join(lines)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned.strip()


def fetch_furiosa_doc(doc: dict[str, str]) -> dict[str, Any]:
    headers = {
        "User-Agent": "gtm-research-agent/0.5",
    }

    result: dict[str, Any] = {
        "name": doc["name"],
        "url": doc["url"],
        "category": doc["category"],
        "fetched_at_kst": now_kst().isoformat(),
        "ok": False,
        "status_code": None,
        "text_chars": 0,
        "excerpt": "",
        "error": "",
    }

    try:
        response = requests.get(doc["url"], headers=headers, timeout=25)
        result["status_code"] = response.status_code
        response.raise_for_status()

        text = extract_clean_text_from_html(response.text)
        result["ok"] = True
        result["text_chars"] = len(text)
        result["excerpt"] = text[:5000]
        return result
    except Exception as exc:
        result["error"] = str(exc)
        return result


def collect_furiosa_docs() -> list[dict[str, Any]]:
    docs = []

    for doc in FURIOSA_DOCS:
        item = fetch_furiosa_doc(doc)
        docs.append(item)
        status = "OK" if item.get("ok") else "FAILED"
        print(f"Furiosa doc {status}: {doc['name']} ({item.get('text_chars')} chars)")
        time.sleep(0.2)

    return docs


def build_furiosa_snapshot(docs: list[dict[str, Any]]) -> str:
    lines = [
        "# FuriosaAI Public Docs Snapshot",
        "",
        f"- fetched_at_kst: `{now_kst().isoformat()}`",
        f"- docs_count: `{len(docs)}`",
        "",
    ]

    for doc in docs:
        lines.extend(
            [
                "---",
                "",
                f"## {doc.get('name')}",
                "",
                f"- url: {doc.get('url')}",
                f"- category: `{doc.get('category')}`",
                f"- ok: `{doc.get('ok')}`",
                f"- status_code: `{doc.get('status_code')}`",
                f"- text_chars: `{doc.get('text_chars')}`",
                f"- error: `{doc.get('error')}`",
                "",
                "### Excerpt",
                "",
                doc.get("excerpt") or "",
                "",
            ]
        )

    return "\n".join(lines)


def normalize_model_name(value: str) -> str:
    value = value.strip()
    value = re.sub(r"\s+", " ", value)
    value = value.replace("Qwen 2.5", "Qwen2.5")
    value = value.replace("Qwen 3", "Qwen3")
    value = value.replace("Llama 3.1", "Llama-3.1")
    value = value.replace("Llama 3.3", "Llama-3.3")
    value = value.replace("EXAONE 4.0", "EXAONE-4.0")
    value = value.replace("EXAONE 3.5", "EXAONE-3.5")
    return value


def extract_model_entries_from_text(text: str) -> dict[str, list[str]]:
    supported_patterns = [
        r"\bDeepSeek\s*R1\b",
        r"\bEXAONE\s*4\.0\b",
        r"\bLlama\s*3\.1\b",
        r"\bLlama\s*3\.3\b",
        r"\bSolar\s*1\.0\b",
        r"\bQwen\s*2(?:\.0)?\b",
        r"\bQwen\s*2\.5\b",
        r"\bQwen\s*3\b",
        r"\bQwen\s*3\s*Embedding\b",
        r"\bQwen\s*3\s*Reranker\b",
    ]

    planned_patterns = [
        r"\bGPT-OSS\b",
        r"\bK-EXAONE\b",
        r"\bSolar\s*Open\b",
        r"\bQwen3\s*MoE\b",
        r"\bQwen3\s*VL\b",
    ]

    precompiled_patterns = [
        r"\bEXAONE-4\.0-[A-Za-z0-9._\-]+",
        r"\bEXAONE-3\.5-[A-Za-z0-9._\-]+",
        r"\bLGAI-EXAONE/EXAONE-3\.5-[A-Za-z0-9._\-]+",
        r"\bLlama-3\.1-[A-Za-z0-9._\-]+",
        r"\bLlama-3\.3-[A-Za-z0-9._\-]+",
        r"\bQwen2\.5-[A-Za-z0-9._\-]+",
        r"\bQwen3-[A-Za-z0-9._\-]+",
        r"\bDeepSeek-R1-[A-Za-z0-9._\-]+",
        r"\bSOLAR-[A-Za-z0-9._\-]+",
        r"\bfuriosa-ai/[A-Za-z0-9._\-]+",
        r"\bLGAI-EXAONE/EXAONE-4\.0-[A-Za-z0-9._\-]+",
        r"\bmeta-llama/Llama-3\.[13]-[A-Za-z0-9._\-]+",
        r"\bQwen/Qwen[23][A-Za-z0-9._\-]+",
        r"\bupstage/SOLAR-[A-Za-z0-9._\-]+",
    ]

    def collect(patterns: list[str]) -> list[str]:
        values = []
        for pattern in patterns:
            for match in re.finditer(pattern, text, flags=re.IGNORECASE):
                value = match.group(0).strip()
                value = normalize_model_name(value)
                if value not in values:
                    values.append(value)
        return values

    return {
        "supported": collect(supported_patterns),
        "planned": collect(planned_patterns),
        "precompiled": collect(precompiled_patterns),
    }


def build_furiosa_summary(docs: list[dict[str, Any]]) -> dict[str, Any]:
    successful = [doc for doc in docs if doc.get("ok")]
    failed = [doc for doc in docs if not doc.get("ok")]

    keyword_map = {
        "serving_stack": [
            "vLLM",
            "OpenAI",
            "OpenAI-Compatible",
            "Kubernetes",
            "Helm",
            "Docker",
            "container",
            "API",
            "server",
        ],
        "hardware_ops": [
            "RNGD",
            "HBM",
            "power",
            "Watt",
            "SR-IOV",
            "virtualization",
            "PCIe",
            "thermal",
        ],
    }

    hits: dict[str, list[str]] = {key: [] for key in keyword_map}

    supported_model_entries: list[dict[str, str]] = []
    planned_model_entries: list[dict[str, str]] = []
    precompiled_model_entries: list[dict[str, str]] = []

    def add_unique(target: list[dict[str, str]], entry: dict[str, str]) -> None:
        key = (
            entry.get("model_name", "").lower(),
            entry.get("source_doc", "").lower(),
            entry.get("status", "").lower(),
        )
        existing_keys = {
            (
                x.get("model_name", "").lower(),
                x.get("source_doc", "").lower(),
                x.get("status", "").lower(),
            )
            for x in target
        }
        if key not in existing_keys:
            target.append(entry)

    for doc in successful:
        text = doc.get("excerpt", "")
        doc_name = doc.get("name", "")
        doc_url = doc.get("url", "")
        category = doc.get("category", "")

        extracted = extract_model_entries_from_text(text)

        for model_name in extracted["supported"]:
            add_unique(
                supported_model_entries,
                {
                    "model_name": model_name,
                    "status": "supported_architecture_or_model_family",
                    "source_doc": doc_name,
                    "source_url": doc_url,
                },
            )

        for model_name in extracted["planned"]:
            add_unique(
                planned_model_entries,
                {
                    "model_name": model_name,
                    "status": "planned_future_support",
                    "source_doc": doc_name,
                    "source_url": doc_url,
                },
            )

        for model_name in extracted["precompiled"]:
            if model_name.startswith("furiosa-ai/"):
                model_name = model_name.split("/", 1)[1]

            add_unique(
                precompiled_model_entries,
                {
                    "model_name": model_name,
                    "status": "precompiled_or_example_hf_artifact",
                    "source_doc": doc_name,
                    "source_url": doc_url,
                },
            )

        for bucket, keywords in keyword_map.items():
            for keyword in keywords:
                if keyword.lower() in text.lower():
                    hit = f"{doc_name}: {keyword}"
                    if hit not in hits[bucket]:
                        hits[bucket].append(hit)

        if category.startswith("huggingface"):
            for match in re.finditer(r"furiosa-ai/[A-Za-z0-9._\-]+", text):
                repo_id = match.group(0)
                model_name = repo_id.split("/", 1)[1]
                add_unique(
                    precompiled_model_entries,
                    {
                        "model_name": model_name,
                        "status": "precompiled_huggingface_artifact",
                        "source_doc": doc_name,
                        "source_url": doc_url,
                    },
                )

    return {
        "fetched_at_kst": now_kst().isoformat(),
        "docs_total": len(docs),
        "docs_successful": len(successful),
        "docs_failed": len(failed),
        "successful_docs": [
            {
                "name": doc.get("name"),
                "url": doc.get("url"),
                "category": doc.get("category"),
                "text_chars": doc.get("text_chars"),
            }
            for doc in successful
        ],
        "failed_docs": [
            {
                "name": doc.get("name"),
                "url": doc.get("url"),
                "category": doc.get("category"),
                "status_code": doc.get("status_code"),
                "error": doc.get("error"),
            }
            for doc in failed
        ],
        "supported_model_entries": supported_model_entries,
        "planned_model_entries": planned_model_entries,
        "precompiled_model_entries": precompiled_model_entries,
        "keyword_hits": hits,
        "model_compatibility_note": (
            "Use exact model/version matching for GTM evaluation. "
            "EXAONE 4.0 and EXAONE 4.5 must be treated as different. "
            "Qwen 2.5 and Qwen 3 must be treated as different. "
            "Llama 3.1 and Llama 3.3 must be treated as different. "
            "Supported model architecture/family, planned future support, and precompiled Hugging Face artifacts are different evidence types."
        ),
    }


def summarize_sources_for_report(
    sources: list[dict[str, Any]],
    limit: int = 20,
) -> str:
    if not sources:
        return "최근 7일 내 수집 결과가 없습니다."

    lines = []
    for idx, item in enumerate(sources[:limit], start=1):
        title = item.get("title", "")
        published = item.get("published_at_kst", "")
        query = item.get("query") or item.get("feed_name") or ""
        url = item.get("originallink") or item.get("link") or ""
        desc = item.get("description", "")
        source = item.get("source", "")

        lines.append(
            f"{idx}. **{title}**\n"
            f"   - source: `{source}`\n"
            f"   - published_at_kst: `{published}`\n"
            f"   - matched_query_or_feed: `{query}`\n"
            f"   - url: {url}\n"
            f"   - summary_snippet: {desc[:300]}\n"
        )

    return "\n".join(lines)


def summarize_furiosa_docs_for_report(summary: dict[str, Any]) -> str:
    lines = [
        f"- docs_total: `{summary.get('docs_total')}`",
        f"- docs_successful: `{summary.get('docs_successful')}`",
        f"- docs_failed: `{summary.get('docs_failed')}`",
        "",
        "### Successful docs",
    ]

    for doc in summary.get("successful_docs", []):
        lines.append(
            f"- {doc.get('name')} / chars: `{doc.get('text_chars')}` / {doc.get('url')}"
        )

    failed_docs = summary.get("failed_docs", [])
    if failed_docs:
        lines.extend(["", "### Failed docs"])
        for doc in failed_docs:
            lines.append(
                f"- {doc.get('name')} / status: `{doc.get('status_code')}` / error: `{doc.get('error')}`"
            )

    lines.extend(["", "### Supported model entries"])
    supported_items = summary.get("supported_model_entries", [])
    if supported_items:
        for item in supported_items[:80]:
            lines.append(
                f"- {item.get('model_name')} / {item.get('status')} / {item.get('source_doc')}"
            )
    else:
        lines.append("- none")

    lines.extend(["", "### Planned model entries"])
    planned_items = summary.get("planned_model_entries", [])
    if planned_items:
        for item in planned_items[:80]:
            lines.append(
                f"- {item.get('model_name')} / {item.get('status')} / {item.get('source_doc')}"
            )
    else:
        lines.append("- none")

    lines.extend(["", "### Precompiled / example model artifacts"])
    precompiled_items = summary.get("precompiled_model_entries", [])
    if precompiled_items:
        for item in precompiled_items[:120]:
            lines.append(
                f"- {item.get('model_name')} / {item.get('status')} / {item.get('source_doc')}"
            )
    else:
        lines.append("- none")

    lines.extend(["", "### Keyword hits"])

    for bucket, hits in summary.get("keyword_hits", {}).items():
        lines.append(f"- {bucket}: {', '.join(hits[:20]) if hits else 'none'}")

    return "\n".join(lines)


def choose_llm_sources(sources: list[dict[str, Any]]) -> list[dict[str, Any]]:
    high_signal_terms = [
        "EXAONE",
        "엑사원",
        "Qwen",
        "Llama",
        "DeepSeek",
        "Solar",
        "QwQ",
        "삼성SDS",
        "SCP",
        "NPUaaS",
        "GPUaaS",
        "CSP",
        "MSP",
        "inference service",
        "추론 서비스",
        "API 서비스",
        "클라우드 AI",
        "AI 클라우드",
        "온프레미스",
        "프라이빗 AI",
        "망분리",
        "폐쇄망",
        "LLM",
        "생성형",
        "AI",
        "데이터센터",
        "GPU",
        "NPU",
        "클라우드",
        "inference",
        "추론",
        "RAG",
        "vLLM",
        "OpenAI",
        "프라이빗",
        "나라장터",
        "조달",
        "국방",
        "병원",
        "금융",
        "生成AI",
        "AI cloud",
        "sovereign",
    ]

    model_terms = ["EXAONE", "엑사원", "Qwen", "Llama", "DeepSeek", "Solar", "QwQ"]
    csp_terms = [
        "삼성SDS",
        "SCP",
        "NPUaaS",
        "GPUaaS",
        "CSP",
        "MSP",
        "클라우드",
        "추론 서비스",
        "inference service",
        "API 서비스",
        "AI 클라우드",
    ]
    deployment_terms = [
        "온프레미스",
        "프라이빗",
        "망분리",
        "폐쇄망",
        "데이터센터",
        "국방",
        "병원",
        "금융",
    ]

    scored = []

    for item in sources:
        text = (
            f"{item.get('title', '')} "
            f"{item.get('description', '')} "
            f"{item.get('query', '')} "
            f"{item.get('feed_name', '')} "
            f"{item.get('category', '')}"
        )

        score = 0

        for term in high_signal_terms:
            if term.lower() in text.lower():
                score += 1

        for term in model_terms:
            if term.lower() in text.lower():
                score += 5

        for term in csp_terms:
            if term.lower() in text.lower():
                score += 3

        for term in deployment_terms:
            if term.lower() in text.lower():
                score += 3

        if item.get("source") == "naver_news_api":
            score += 1

        scored.append((score, item))

    scored.sort(
        key=lambda pair: (
            pair[0],
            pair[1].get("published_at_kst") or "",
        ),
        reverse=True,
    )

    return [item for _, item in scored[:MAX_LLM_SOURCES]]

def build_llm_payload_sources(sources: list[dict[str, Any]]) -> list[dict[str, Any]]:
    payload = []

    for idx, item in enumerate(sources, start=1):
        payload.append(
            {
                "source_id": f"S{idx:03d}",
                "title": item.get("title", "")[:300],
                "description": item.get("description", "")[:MAX_SOURCE_CHARS],
                "published_at_kst": item.get("published_at_kst"),
                "url": item.get("originallink") or item.get("link"),
                "source": item.get("source"),
                "matched_query_or_feed": item.get("query") or item.get("feed_name"),
                "country_hint": item.get("country", ""),
                "category_hint": item.get("category", ""),
            }
        )

    return payload


def build_llm_prompt(
    instructions: str,
    llm_sources: list[dict[str, Any]],
    furiosa_docs_summary: dict[str, Any],
) -> str:
    trimmed_instructions = instructions[:15000]

    payload = {
        "agent_instructions_excerpt": trimmed_instructions,
        "limits": {
            "max_output_candidates": MAX_OUTPUT_CANDIDATES,
            "max_llm_sources": MAX_LLM_SOURCES,
            "max_source_chars": MAX_SOURCE_CHARS,
        },
        "furiosa_ground_truth": {
            "supported_model_entries": furiosa_docs_summary.get("supported_model_entries", []),
            "planned_model_entries": furiosa_docs_summary.get("planned_model_entries", []),
            "precompiled_model_entries": furiosa_docs_summary.get("precompiled_model_entries", []),
            "model_compatibility_note": furiosa_docs_summary.get("model_compatibility_note", ""),
            "keyword_hits": furiosa_docs_summary.get("keyword_hits", {}),
        },
        "sources": llm_sources,
    }

    return f"""
You are evaluating public GTM signals for FuriosaAI.

Return ONLY valid JSON. Do not use Markdown. Do not include comments.

Fit score hard rules:
- If confirmed_model_name is "미확인", model_fit_score must be "UNKNOWN". It must never be "HIGH".
- If model_match_status is "unknown", model_fit_score must be "UNKNOWN" or "LOW". It must never be "HIGH".
- If model_match_status is "family_only", model_fit_score must be "MID" or lower.
- If model_match_status is "unknown" or "family_only", rngd_fit_score must usually be "MID" or lower.
- CSP/operator/channel strength must be reflected in channel_fit_score and outreach_priority, not model_fit_score.
- For Samsung SDS-like CSP operators, use this pattern: model_fit_score UNKNOWN, deployment_fit_score HIGH, channel_fit_score HIGH, rngd_fit_score MID, outreach_priority HIGH.
- A candidate can have HIGH outreach_priority even when model_fit_score is UNKNOWN, but only if the reason is infrastructure, buyer signal, CSP route, NPUaaS route, or capacity expansion.

Important GTM targeting rules:
- Do not treat rngd_fit_score and outreach_priority as the same thing.
- If model_match_status is "unknown" or "family_only", rngd_fit_score should usually be MID or lower.
- Exception: CSP 운영 기업, AI data center operators, NPUaaS/GPUaaS operators, or major infrastructure buyers can have HIGH outreach_priority even if model_match_status is unknown.
- In that exception, explain clearly that the outreach priority is driven by infrastructure/channel/CSP capacity expansion, not model compatibility.
- If confirmed_model_name is only a family name such as "EXAONE" without exact version, do not claim exact support.
- Classify every non-noise candidate into one of three target types: 온프레미스 기업, CSP 운영 기업, CSP 고객 기업.
- Do not over-focus on on-premise only.
- If a company is likely to consume AI inference through a cloud platform, classify it as CSP 고객 기업.
- If a company operates cloud, GPUaaS, NPUaaS, IDC, MSP, inference-as-a-service, or AI API platform, classify it as CSP 운영 기업.
- Samsung SDS SCP and NPUaaS route is strategically important. If a candidate can create demand for SCP/NPUaaS, explain the CSP-routed sales logic.
- For each candidate, separate direct sales possibility, CSP-routed sales possibility, NPUaaS adoption possibility, and CSP capacity expansion possibility.
- Do not include an excluded-news section in the final report. Only include useful candidates, structure-check items, NPUaaS/cloud demand leads, competitor GTM movements, and next actions.
- For decision_maker_hint, suggest likely title/function to search for, such as CIO, CTO, CDO, Head of AI, Head of Cloud, Head of Infrastructure, platform lead, or procurement department. Do not invent names.
- Competitor updates should focus only on GTM actions: customer wins, deliveries, public sector wins, CSP/MSP partnerships, NPUaaS/GPUaaS/inference service launches, and customer PoCs. Ignore pure fundraising news.


Important model compatibility rules:
- Use exact model/version matching.
- EXAONE-4.0 and EXAONE-4.5 are different.
- Qwen2.5 and Qwen3 are different.
- Llama-3.1 and Llama-3.3 are different.
- supported_model_entries, planned_model_entries, and precompiled_model_entries are different evidence types.
- If a model family matches but exact version does not match, do not mark it as supported. Use "확인 필요" or conservative fit.
- Do not invent budgets, GPU counts, people, titles, partnerships, or model names.
- Use only the provided sources and Furiosa public-doc summary.
- If a source is just general AI policy, stock market, election, or unrelated news, classify it as "noise".


Numeric evidence rules:
- Do not invent numbers. Percentages, multipliers, cost/power reductions, GPU/server counts, MW, budgets, timelines, and performance claims must appear verbatim in a provided source or Furiosa doc excerpt.
- Every numeric expression that appears in any narrative field (buying_signal, infrastructure_signal, timing_reason, customer_win, furiosa_win, contact_reason, outreach_talk_track, fit_vs_priority_explanation) must also appear in numeric_claims with source_id and evidence_text.
- If numeric_claims is empty, write narrative fields with qualitative language only — no digits, no "수백/수천/대규모/대폭/반값" style proxies for unsupported numbers.
- A number announced by the customer is not an RNGD performance claim.

Tone rules:
- Write narrative fields in calm, natural Korean. Do not use promotional, sales-pitch, or hype language. Prefer conservative phrasing such as "검토 가능", "개선 가능성", "확인 필요", "구조 확인 필요".
- Do not promise that RNGD will cut cost, power, rack space, latency, or headcount unless a provided source or Furiosa doc states that exact claim.
- Korean grammar must be natural. Do not produce awkward direct-translation phrases or broken endings.

Output JSON schema:
{{
  "run_summary": {{
    "overall_assessment": "string",
    "top_priority_names": ["string"],
    "noise_ratio_comment": "string",
    "model_compatibility_caution": "string"
  }},
  "candidates": [
    {{
      "name": "company or institution name",
      "country": "KR | JP | UNKNOWN",
      "market": "B2B | B2G | UNKNOWN",
      "target_type": "온프레미스 기업 | CSP 운영 기업 | CSP 고객 기업 | 확인 필요",
      "classification": "priority_outreach | structure_check | cloud_npuaaS_lead | watchlist | noise",
      "confirmed_project_or_signal": "string",
      "confirmed_model_name": "string or 미확인",
      "model_match_status": "exact_supported | planned | precompiled | family_only | unknown | none",
      "model_fit_score": "HIGH | MID | LOW | UNKNOWN | NONE",
      "deployment_fit_score": "HIGH | MID | LOW | UNKNOWN",
      "channel_fit_score": "HIGH | MID | LOW | UNKNOWN",
      "rngd_fit_score": "HIGH | MID | LOW | NONE",
      "outreach_priority": "HIGH | MID | LOW | WATCH",
      "fit_vs_priority_explanation": "string",
      "hook_type": "POWER | VLLM | SOVEREIGN | SCALE | PARTNER | CLOUD | PROCUREMENT | NONE",
      "buying_signal": "string",
      "infrastructure_signal": "string",
      "timing_reason": "string",
      "customer_win": "string",
      "furiosa_win": "string",
      "numeric_claims": [
        {{
          "claim": "string",
          "source_id": "S001",
          "source_url": "string",
          "evidence_text": "string"
        }}
      ],
      "direct_sales_possibility": "HIGH | MID | LOW | UNKNOWN",
      "csp_routed_sales_possibility": "HIGH | MID | LOW | UNKNOWN",
      "npuaas_adoption_possibility": "HIGH | MID | LOW | UNKNOWN",
      "csp_capacity_expansion_possibility": "HIGH | MID | LOW | UNKNOWN",
      "contact_reason": "string",
      "outreach_talk_track": "string",
      "revenue_timing": "단기 | 중기 | 장기 | 불명확",
      "decision_maker_hint": "string",
      "existing_touchpoint": "확인 필요",
      "verification_needed": ["string"],
      "source_ids": ["S001"],
      "source_urls": ["string"]
    }}
  ],
  "noise_examples": [
    {{
      "source_id": "S001",
      "title": "string",
      "reason": "string"
    }}
  ],
  "eval_notes": [
    "string"
  ]
}}

Maximum candidates: {MAX_OUTPUT_CANDIDATES}.
Make the report useful for BD/GTM, not a generic news summary.

INPUT:
{json.dumps(payload, ensure_ascii=False, indent=2)}
""".strip()


def extract_json_from_text(text: str) -> dict[str, Any]:
    text = text.strip()

    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?", "", text).strip()
        text = re.sub(r"```$", "", text).strip()

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    match = re.search(r"\{.*\}", text, flags=re.DOTALL)
    if not match:
        raise ValueError("No JSON object found in LLM response.")

    return json.loads(match.group(0))


NARRATIVE_FIELDS = [
    "confirmed_project_or_signal",
    "fit_vs_priority_explanation",
    "buying_signal",
    "infrastructure_signal",
    "timing_reason",
    "customer_win",
    "furiosa_win",
    "contact_reason",
    "outreach_talk_track",
]


# 숫자성 표현 감지용 패턴. 발견되면 텍스트를 고쳐쓰지 않고 verification_needed에 표시만 한다.
NUMERIC_EXPRESSION_PATTERN = re.compile(
    r"(?:\d+(?:[.,]\d+)?\s*(?:%|배|MW|kW|W|억|만|장|대|GB|TB)"
    r"|\b\d+(?:[.,]\d+)?\s*(?:percent|x|times)\b)",
    flags=re.IGNORECASE,
)


def enforce_candidate_fit_rules(candidate: dict[str, Any]) -> dict[str, Any]:
    """
    Structural validation only. Adjusts score fields when they contradict
    the declared model_match_status / confirmed_model_name. No phrase rewriting.
    """
    model_status = str(candidate.get("model_match_status", "")).lower()
    confirmed_model = str(candidate.get("confirmed_model_name", "")).strip()
    target_type = str(candidate.get("target_type", ""))
    deployment_fit = str(candidate.get("deployment_fit_score", ""))
    channel_fit = str(candidate.get("channel_fit_score", ""))

    if confirmed_model in ["", "미확인"] or model_status == "unknown":
        candidate["model_fit_score"] = "UNKNOWN"

        if target_type == "CSP 운영 기업" and deployment_fit == "HIGH" and channel_fit == "HIGH":
            if candidate.get("rngd_fit_score") == "HIGH":
                candidate["rngd_fit_score"] = "MID"
        else:
            if candidate.get("rngd_fit_score") == "HIGH":
                candidate["rngd_fit_score"] = "MID"

    if model_status == "family_only":
        if candidate.get("model_fit_score") == "HIGH":
            candidate["model_fit_score"] = "MID"
        if candidate.get("rngd_fit_score") == "HIGH":
            candidate["rngd_fit_score"] = "MID"

    return candidate


def enrich_candidate_defaults(candidate: dict[str, Any]) -> dict[str, Any]:
    # 담당자 디스커버리(v0.7)가 실행되기 전 단계의 기본값.
    candidate.setdefault("decision_maker_profile_url", "확인 필요")
    candidate.setdefault("decision_maker_profile_confidence", "UNKNOWN")

    # B2G는 G2B 직접 확인 구현 전까지 항상 보수 라벨로 강제한다.
    if candidate.get("market") == "B2G":
        candidate["b2g_evidence_type"] = "기사/RSS 기반"
        candidate["g2b_checked"] = "미수행"
        candidate.setdefault("procurement_next_action", "나라장터/RFP 직접 확인 필요")

    return candidate


def flag_unsupported_numeric_claims(candidate: dict[str, Any]) -> dict[str, Any]:
    """
    If numeric_claims is empty but a narrative field contains numeric-looking
    expressions (%, 배, MW, 억, ...), add a verification_needed note.
    The Korean text itself is left untouched. Downstream the report-writer
    LLM is instructed to drop unsupported numbers naturally.
    """
    numeric_claims = candidate.get("numeric_claims", [])
    if isinstance(numeric_claims, list) and numeric_claims:
        return candidate

    flagged = []
    for field in NARRATIVE_FIELDS:
        value = candidate.get(field, "")
        if isinstance(value, str) and NUMERIC_EXPRESSION_PATTERN.search(value):
            flagged.append(field)

    if flagged:
        verification = candidate.get("verification_needed")
        if not isinstance(verification, list):
            verification = []
        verification.append(
            f"numeric_claims 미제공 상태에서 숫자성 표현이 포함됨: {', '.join(flagged)}"
        )
        candidate["verification_needed"] = verification

    return candidate


def postprocess_eval_result(result: dict[str, Any]) -> dict[str, Any]:
    candidates = result.get("candidates", [])
    if isinstance(candidates, list):
        cleaned = []
        for candidate in candidates:
            if not isinstance(candidate, dict):
                continue
            candidate = enforce_candidate_fit_rules(candidate)
            candidate = enrich_candidate_defaults(candidate)
            candidate = flag_unsupported_numeric_claims(candidate)
            cleaned.append(candidate)
        result["candidates"] = cleaned

    return result



def evaluate_candidates_with_gemini(
    instructions: str,
    sources: list[dict[str, Any]],
    furiosa_docs_summary: dict[str, Any],
) -> tuple[dict[str, Any], str]:
    model = os.getenv("LLM_MODEL", "gemini-3.5-flash")

    llm_sources = build_llm_payload_sources(choose_llm_sources(sources))
    prompt = build_llm_prompt(
        instructions=instructions,
        llm_sources=llm_sources,
        furiosa_docs_summary=furiosa_docs_summary,
    )

    raw_text = gemini_generate_with_retry(prompt)
    result = extract_json_from_text(raw_text)
    result = postprocess_eval_result(result)

    result["_llm_metadata"] = {
        "provider": "gemini",
        "model": model,
        "llm_sources_count": len(llm_sources),
        "max_llm_sources": MAX_LLM_SOURCES,
        "max_source_chars": MAX_SOURCE_CHARS,
        "max_output_candidates": MAX_OUTPUT_CANDIDATES,
        "evaluated_at_kst": now_kst().isoformat(),
    }

    return result, raw_text


def _trim_candidate_for_report(candidate: dict[str, Any]) -> dict[str, Any]:
    fields = [
        "name",
        "country",
        "market",
        "target_type",
        "classification",
        "confirmed_project_or_signal",
        "confirmed_model_name",
        "model_match_status",
        "model_fit_score",
        "deployment_fit_score",
        "channel_fit_score",
        "rngd_fit_score",
        "outreach_priority",
        "fit_vs_priority_explanation",
        "hook_type",
        "buying_signal",
        "infrastructure_signal",
        "timing_reason",
        "customer_win",
        "furiosa_win",
        "numeric_claims",
        "direct_sales_possibility",
        "csp_routed_sales_possibility",
        "npuaas_adoption_possibility",
        "csp_capacity_expansion_possibility",
        "contact_reason",
        "outreach_talk_track",
        "revenue_timing",
        "decision_maker_hint",
        "existing_touchpoint",
        "verification_needed",
        "source_ids",
        "source_urls",
        "b2g_evidence_type",
        "g2b_checked",
        "procurement_next_action",
        "decision_maker_profile_url",
        "decision_maker_profile_title",
        "decision_maker_profile_source",
        "decision_maker_profile_confidence",
        "decision_maker_search_queries",
    ]
    return {field: candidate.get(field) for field in fields}


REPORT_SCOPE_B2B = "b2b"
REPORT_SCOPE_B2B_B2G = "b2b_b2g"


_COMMON_PROMPT_RULES = """
[톤·문체 규칙]
- 자연스러운 한국어 문장으로 쓰세요. 직역체나 어색한 어미 결합("확보 가능성하고", "검토할 수 있습니다 명분", "개선 가능성 검토할 수 있습니다"처럼 끊긴 문장)은 금지합니다.
- 과장 표현 금지: "완벽", "획기적", "독보적", "압도적", "최고", "보장", "선점" 같은 단어와 그 변형을 쓰지 마세요.
- RNGD가 비용·전력·랙·지연·서버 수를 줄여준다고 단정하지 마세요. 출처가 그대로 말하지 않으면 "검토 가능", "확인 필요", "구조 확인 필요"로 표현하세요.

[수치 규칙]
- candidate의 numeric_claims에 명시된 수치만 인용할 수 있습니다.
- numeric_claims가 비어 있는 후보에 대해서는 비용·전력·성능·MW·%·배수·대수·억원 등 숫자를 본문에 쓰지 마세요. 정성적으로만 묘사하세요.
- numeric_claims에 있는 수치를 인용할 때는 그대로 인용하고, "(출처: source_id)" 형태로 표시하세요.

[모델 규칙]
- confirmed_model_name이 "미확인"이거나 model_match_status가 "unknown"이면 모델 적합성을 단정하지 말고 인프라/채널/타이밍 관점으로만 설명하세요.
- model_match_status가 "family_only"이면 정확한 버전 지원이 확인되지 않았다고 표기하세요.

[출처 규칙]
- 각 후보의 source_urls가 있으면 마크다운 링크로 1~3개 노출. 비어 있으면 "출처 미확인"으로 표기.
- 후보별 표/상세에는 항상 출처 열/항목을 포함하세요.

[담당자/LinkedIn 표기 규칙]
- decision_maker_profile_confidence가 "HIGH" 또는 "MID"이면 decision_maker_profile_url을 마크다운 링크로 노출하고 "후보 — 신뢰도 HIGH" 또는 "후보 — 신뢰도 MID"로 표시. 단정 어조 금지.
- "LOW" 또는 "UNKNOWN"이면 "확인 필요"라고만 적고 URL을 노출하지 마세요.
- decision_maker_profile_title이 있고 신뢰도가 HIGH/MID이면 짧은 직함 단서로만 표기. 사람 이름을 발명하지 마세요.

[출력 형식]
- 마크다운 본문만 출력. 코드펜스(```), JSON, 영문 안내 문장 금지.
""".strip()


def _filter_candidates_for_scope(
    candidates: list[dict[str, Any]],
    scope: str,
) -> list[dict[str, Any]]:
    cleaned = [
        c for c in candidates
        if isinstance(c, dict) and c.get("classification") != "noise"
    ]
    if scope == REPORT_SCOPE_B2B:
        return [c for c in cleaned if (c.get("market") or "").upper() != "B2G"]
    return cleaned


def build_report_writer_prompt(
    eval_result: dict[str, Any],
    furiosa_docs_summary: dict[str, Any],
    scope: str = REPORT_SCOPE_B2B_B2G,
) -> str:
    filtered = _filter_candidates_for_scope(eval_result.get("candidates", []), scope)
    candidates = [_trim_candidate_for_report(c) for c in filtered]

    payload = {
        "today_kst": now_kst().strftime("%Y-%m-%d"),
        "scope": scope,
        "run_summary": eval_result.get("run_summary", {}),
        "candidates": candidates,
        "furiosa_supported_models": furiosa_docs_summary.get("supported_model_entries", [])[:40],
        "furiosa_planned_models": furiosa_docs_summary.get("planned_model_entries", [])[:20],
        "furiosa_precompiled_models": furiosa_docs_summary.get("precompiled_model_entries", [])[:40],
    }

    if scope == REPORT_SCOPE_B2B:
        sections = """
[리포트 구조 — 정확히 이 순서, 이 헤더로 / 이번 리포트는 B2B 전용입니다]
# FuriosaAI GTM 리서치 — B2B — {TODAY}
(TODAY는 INPUT의 today_kst 값을 사용)

## 1. 한 줄 결론
run_summary.overall_assessment를 보수적인 한 문장으로 정리. 새 사실 추가 금지.

## 2. 이번 주 우선 연락 Top 3 (B2B)
outreach_priority HIGH 우선, 그다음 MID. 노이즈 제외. 최대 3개.
표 헤더: 순위 | 대상 | 유형 | 확인 모델 | 핵심 이유 | 다음 액션 | 출처

## 3. B2B 후보 표
INPUT.candidates 전부(이미 B2B만 들어 있음). 표 헤더: 우선순위 | 대상 | 유형 | 확인 모델 | 모델 매칭 | RNGD fit | outreach | 왜 지금 | 출처

## 4. 우선 연락 후보 상세
상위 후보 최대 6개. 후보마다 다음 항목을 한국어 자연문으로 풀어쓰기:
- 확인된 모델 / 모델 매칭 상태
- RNGD fit / outreach priority
- 고객 win
- FuriosaAI win
- 컨택 명분
- 제안 토크 트랙
- 담당자/LinkedIn 후보 (위 표기 규칙 적용)
- 출처 링크

## 5. NPUaaS / CSP 경유 기회
target_type=="CSP 운영 기업" 또는 csp_routed_sales_possibility=="HIGH" 또는 npuaas_adoption_possibility=="HIGH"인 후보 중심.
후보별로 CSP 경유 / NPUaaS / capacity 증설 가능성과 한 줄 사유.

## 6. 담당자 / 컨택 경로
표 헤더: 대상 | 담당자 힌트 | LinkedIn/공개 프로필 후보 | 신뢰도 | 기존 접점
- decision_maker_hint는 직함/조직 단위로만 표현. 사람 이름 발명 금지.

## 7. 경쟁사 GTM 동향
다음 문장만 포함하고 추측 금지: "이번 버전은 후보 평가 중심이며, 경쟁사 GTM(고객 납품, 파트너십, NPUaaS/GPUaaS 출시, 공공 수주) 별도 구조화는 다음 버전에서 추가할 예정입니다."

## 8. 주의 사항
- 모델명이 미확인인 후보는 인프라/채널/타이밍 관점으로만 해석.
- 수치 근거가 없는 비용·전력·성능 단정은 포함하지 않았음을 명시.
- 이 리포트는 B2B 전용입니다. B2G/공공 후보는 별도 B2B+B2G 리포트에서만 다룹니다.
""".strip()
        b2g_rules_block = (
            "[B2G 규칙]\n"
            "- 이번 리포트는 B2B 전용입니다. INPUT.candidates에는 B2G 후보가 들어 있지 않습니다.\n"
            "- 본문에 B2G/공공/나라장터/RFP 관련 섹션이나 문장을 만들지 마세요. 그런 내용은 별도 B2B+B2G 리포트에서 다룹니다."
        )
    else:
        sections = """
[리포트 구조 — 정확히 이 순서, 이 헤더로 / 이번 리포트는 B2B + B2G 통합입니다]
# FuriosaAI GTM 리서치 — B2B + B2G — {TODAY}
(TODAY는 INPUT의 today_kst 값을 사용)

## 1. 한 줄 결론
run_summary.overall_assessment를 보수적인 한 문장으로 정리. 새 사실 추가 금지.

## 2. 이번 주 우선 연락 Top 3
outreach_priority HIGH 우선, 그다음 MID. 노이즈 제외. 최대 3개.
표 헤더: 순위 | 대상 | 유형 | 확인 모델 | 핵심 이유 | 다음 액션 | 출처

## 3. B2B 후보 표
market=="B2B" 후보만. 표 헤더: 우선순위 | 대상 | 유형 | 확인 모델 | 모델 매칭 | RNGD fit | outreach | 왜 지금 | 출처

## 4. B2B + B2G 통합 표
모든 비-노이즈 후보. 표 헤더는 §3과 동일하되 market=="B2G" 행은 "왜 지금" 칸 끝에 "B2G 근거: 기사/RSS 기반 · 나라장터 확인: 미수행"을 함께 표기.

## 5. 우선 연락 후보 상세
상위 후보 최대 6개. 후보마다 다음 항목을 한국어 자연문으로 풀어쓰기:
- 확인된 모델 / 모델 매칭 상태
- RNGD fit / outreach priority
- 고객 win
- FuriosaAI win
- 컨택 명분
- 제안 토크 트랙
- 담당자/LinkedIn 후보 (위 표기 규칙 적용)
- 출처 링크

## 6. NPUaaS / CSP 경유 기회
target_type=="CSP 운영 기업" 또는 csp_routed_sales_possibility=="HIGH" 또는 npuaas_adoption_possibility=="HIGH"인 후보 중심.
후보별로 CSP 경유 / NPUaaS / capacity 증설 가능성과 한 줄 사유.

## 7. B2G 후보 — 나라장터/RFP 직접 확인 전
섹션 첫 문장에 다음 문장을 그대로 포함: "현재 B2G 후보는 기사/RSS 기반이며, 나라장터/RFP 직접 확인은 미수행 상태입니다."
market=="B2G" 후보별: 근거 유형, 나라장터 확인 여부, 다음 액션, 출처.

## 8. 담당자 / 컨택 경로
표 헤더: 대상 | 담당자 힌트 | LinkedIn/공개 프로필 후보 | 신뢰도 | 기존 접점
- decision_maker_hint는 직함/조직 단위로만 표현. 사람 이름 발명 금지.

## 9. 경쟁사 GTM 동향
다음 문장만 포함하고 추측 금지: "이번 버전은 후보 평가 중심이며, 경쟁사 GTM(고객 납품, 파트너십, NPUaaS/GPUaaS 출시, 공공 수주) 별도 구조화는 다음 버전에서 추가할 예정입니다."

## 10. 주의 사항
- B2G 후보는 나라장터/RFP 직접 확인 전이므로 watchlist/구조 확인으로 해석.
- 모델명이 미확인인 후보는 인프라/채널/타이밍 관점으로만 해석.
- 수치 근거가 없는 비용·전력·성능 단정은 포함하지 않았음을 명시.
""".strip()
        b2g_rules_block = (
            "[B2G 규칙]\n"
            "- market이 \"B2G\"인 후보는 본문/표에 반드시 \"B2G 근거: 기사/RSS 기반\", \"나라장터 확인: 미수행\"을 함께 노출하세요.\n"
            "- B2G 섹션 첫 문장은 다음 문장을 그대로 포함하세요: \"현재 B2G 후보는 기사/RSS 기반이며, 나라장터/RFP 직접 확인은 미수행 상태입니다.\""
        )

    return f"""
당신은 FuriosaAI BD 매니저용 주간 GTM 리포트를 한국어 마크다운으로 작성합니다.

다음 INPUT JSON의 run_summary와 candidates만을 근거로 리포트를 작성하세요. 새 회사, 새 모델, 새 숫자를 발명하지 마세요.

{_COMMON_PROMPT_RULES}

{b2g_rules_block}

{sections}

INPUT:
{json.dumps(payload, ensure_ascii=False, indent=2)}
""".strip()


def _strip_code_fence(text: str) -> str:
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:markdown|md)?", "", text).strip()
        text = re.sub(r"```$", "", text).strip()
    return text


# Transport-level retry counter for Gemini calls. Surfaced in metadata.json as
# llm_retry_count. Reset at the start of each main() run.
_LLM_TRANSPORT_RETRY_COUNT = 0

_TRANSIENT_ERROR_TOKENS = (
    "503",
    "504",
    "unavailable",
    "high demand",
    "server disconnected",
    "remote end closed",
    "remote disconnected",
    "connection reset",
    "connectionreseterror",
    "timeout",
    "timed out",
    "deadline exceeded",
    "deadlineexceeded",
    "429",
    "too many requests",
    "rate limit",
    "resource exhausted",
    "resourceexhausted",
    "temporarily unavailable",
    "serviceunavailable",
)


def _is_transient_llm_error(exc: BaseException) -> bool:
    msg = str(exc).lower()
    cls = exc.__class__.__name__.lower()
    blob = f"{cls} {msg}"
    return any(token in blob for token in _TRANSIENT_ERROR_TOKENS)


def _retry_delays(max_attempts: int) -> list[int]:
    """
    Returns the delay (in seconds) to sleep *before* each attempt.
    Defaults follow the spec: 0, 10, 30, 60. Extra attempts double the last.
    """
    base = [0, 10, 30, 60]
    if max_attempts <= len(base):
        return base[:max_attempts]
    out = list(base)
    while len(out) < max_attempts:
        out.append(out[-1] * 2)
    return out


def _short_exc(exc: BaseException | None) -> str:
    if exc is None:
        return ""
    first_line = str(exc).strip().splitlines()[0] if str(exc).strip() else exc.__class__.__name__
    return first_line[:200]


def reset_llm_retry_count() -> None:
    global _LLM_TRANSPORT_RETRY_COUNT
    _LLM_TRANSPORT_RETRY_COUNT = 0


def get_llm_retry_count() -> int:
    return _LLM_TRANSPORT_RETRY_COUNT


def gemini_generate_with_retry(prompt: str) -> str:
    """
    Single chokepoint for every Gemini generate_content call.
    Retries transient errors (503/429/UNAVAILABLE/timeout/disconnected/...) with
    exponential-ish backoff. Non-transient errors are raised on the first failure.
    """
    global _LLM_TRANSPORT_RETRY_COUNT

    api_key = os.getenv("GEMINI_API_KEY", "")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is missing.")
    model = os.getenv("LLM_MODEL", "gemini-3.5-flash")

    max_attempts = env_int("LLM_MAX_RETRIES", 4)
    if max_attempts < 1:
        max_attempts = 1
    delays = _retry_delays(max_attempts)

    client = genai.Client(api_key=api_key)

    last_exc: BaseException | None = None
    for attempt in range(1, max_attempts + 1):
        delay = delays[attempt - 1]
        if delay > 0:
            print(
                f"Gemini retry: attempt {attempt}/{max_attempts} after {delay}s "
                f"(last: {_short_exc(last_exc)})"
            )
            time.sleep(delay)
            _LLM_TRANSPORT_RETRY_COUNT += 1

        try:
            response = client.models.generate_content(model=model, contents=prompt)
            text = (response.text or "").strip()
            if not text:
                raise RuntimeError("Gemini returned empty response text.")
            return text
        except Exception as exc:
            last_exc = exc
            is_last = attempt >= max_attempts
            transient = _is_transient_llm_error(exc)
            if is_last or not transient:
                if transient:
                    print(
                        f"Gemini transient error after {attempt}/{max_attempts} attempts: "
                        f"{_short_exc(exc)}"
                    )
                raise

    raise last_exc if last_exc is not None else RuntimeError("Gemini call failed without error")


def _call_gemini(prompt: str) -> str:
    text = _strip_code_fence(gemini_generate_with_retry(prompt))
    if not text:
        raise RuntimeError("Report-writer LLM returned empty text after strip.")
    return text


def write_gtm_report_with_llm(
    eval_result: dict[str, Any],
    furiosa_docs_summary: dict[str, Any],
    scope: str = REPORT_SCOPE_B2B_B2G,
) -> str:
    return _call_gemini(build_report_writer_prompt(eval_result, furiosa_docs_summary, scope=scope))


# Category-level risk detectors. Patterns are intentionally small — they only
# label the *category* of a risky claim. They never rewrite Korean text.
RISK_CATEGORIES: dict[str, list[str]] = {
    "unsupported_cost_reduction_claim": [
        r"비용\s*절감",
        r"원가\s*절감",
        r"단가\s*절감",
        r"비용을?\s*줄(?:이|여|인|일)",
        r"반값",
    ],
    "unsupported_power_reduction_claim": [
        r"전력\s*절감",
        r"전력\s*소모를?\s*줄(?:이|여|인|일)",
        r"전력을?\s*낮(?:추|춰|춤)",
        r"초저전력",
        r"\d+\s*MW\b",
    ],
    "unsupported_performance_guarantee": [
        r"\d+\s*배\s*(?:빠|향상|개선)",
        r"성능을?\s*보장",
        r"최고\s*성능",
        r"성능\s*우위\s*확정",
    ],
    "unsupported_revenue_guarantee": [
        r"수주\s*(?:확정|보장)",
        r"수주율을?\s*(?:높이|개선|향상)",
        r"매출\s*(?:확대|보장|증가)\s*(?:확정|보장)?",
        r"수익\s*보장",
    ],
    "unsupported_scale_claim": [
        r"대규모",
        r"수백\s*(?:대|장|건|곳|개)",
        r"수천\s*(?:대|장|건|곳|개)",
    ],
    "hype_language": [
        r"완벽(?:한|히|하게)",
        r"획기적",
        r"독보적",
        r"압도적",
        r"보장(?:합니다|한다|된다|됩니다|되는)",
        r"선점",
        r"돌파(?:합니다|한다|된다|됩니다)",
    ],
}

NUMERIC_GATED_CATEGORIES = {
    "unsupported_cost_reduction_claim",
    "unsupported_power_reduction_claim",
    "unsupported_performance_guarantee",
    "unsupported_revenue_guarantee",
    "unsupported_scale_claim",
}

MAX_VIOLATIONS_RECORDED = 30


def detect_report_violations(
    report_text: str,
    eval_result: dict[str, Any] | None,
) -> list[dict[str, Any]]:
    """
    Walk the rendered markdown line by line, attribute each match to the
    closest ## section / ### candidate, and return a list of violation
    descriptors. Numeric-gated categories are suppressed for candidates
    whose numeric_claims is non-empty.

    The detector only labels categories. It does not rewrite Korean.
    """
    candidates_by_name: dict[str, dict[str, Any]] = {}
    if eval_result and isinstance(eval_result.get("candidates"), list):
        for c in eval_result["candidates"]:
            if isinstance(c, dict) and c.get("name"):
                candidates_by_name[c["name"]] = c

    violations: list[dict[str, Any]] = []
    current_section = ""
    current_candidate = ""

    for line in report_text.splitlines():
        stripped = line.strip()

        if stripped.startswith("## "):
            current_section = stripped.lstrip("#").strip()
            current_candidate = ""
            continue
        if stripped.startswith("### "):
            current_candidate = stripped.lstrip("#").strip()
            continue
        if stripped.startswith("#"):
            continue

        cand_data = candidates_by_name.get(current_candidate)
        cand_has_numeric = bool(
            cand_data
            and isinstance(cand_data.get("numeric_claims"), list)
            and cand_data["numeric_claims"]
        )

        for category, patterns in RISK_CATEGORIES.items():
            if category in NUMERIC_GATED_CATEGORIES and cand_has_numeric:
                continue
            for pattern in patterns:
                for match in re.finditer(pattern, line):
                    violations.append(
                        {
                            "category": category,
                            "section": current_section or "(상단/머리말)",
                            "candidate": current_candidate or "(전역)",
                            "match": match.group(0),
                            "evidence": stripped[:240],
                        }
                    )
                    if len(violations) >= MAX_VIOLATIONS_RECORDED:
                        return violations

    return violations


def build_report_rewrite_prompt(
    current_report: str,
    violations: list[dict[str, Any]],
) -> str:
    return f"""
당신은 직전에 작성한 한국어 GTM 리포트를 보수적으로 다시 작성합니다.

[유지해야 하는 것]
- 섹션 구조와 헤더(§1~§10) 그대로 유지.
- 모든 후보, 표 행, 출처 링크 그대로 유지. 새로 만들지도, 지우지도 마세요.
- 후보의 source_urls 링크는 마크다운 링크 형태로 그대로 유지.

[금지]
- 새 회사, 새 모델, 새 숫자 발명 금지.
- 코드펜스(```), JSON, 영문 안내 문장 출력 금지.
- 직역체나 어색한 어미 결합("확보 가능성하고", "검토할 수 있습니다 명분" 같은 끊긴 문장) 금지.

[수정 지침]
- 아래 위반 사항을 모두 해소하세요. 각 위반은 (카테고리, 후보, 섹션, 근거 문장)으로 보고됩니다.
- 위반 표현을 같은 의미의 보수적 한국어로 자연스럽게 다시 쓰세요. 예: "비용 절감" 류는 "비용 구조 확인 필요"·"비용 구조 검토 가능"으로, "압도적" 같은 과장 어휘는 정성적 표현으로.
- 후보의 numeric_claims에 없는 수치(%, 배, MW, 억, 대, 장 등)는 본문에서 제거하고 정성적으로 표현하세요.
- 의미를 잃지 마세요. 위반된 문장이 전하던 사실(예: 인프라/CSP/타이밍 관점)은 보수적 표현으로 다시 전달하세요.

[위반 사항]
{json.dumps(violations, ensure_ascii=False, indent=2)}

[현재 리포트]
{current_report}

마크다운 본문만 출력하세요.
""".strip()


def rewrite_report_with_llm(
    current_report: str,
    violations: list[dict[str, Any]],
) -> str:
    return _call_gemini(build_report_rewrite_prompt(current_report, violations))


def write_gtm_report_with_validation(
    eval_result: dict[str, Any],
    furiosa_docs_summary: dict[str, Any],
    max_retries: int = 2,
    scope: str = REPORT_SCOPE_B2B_B2G,
) -> tuple[str, list[dict[str, Any]], int]:
    """
    Two-step pipeline (per scope):
      1. LLM writes the report from validated candidates (filtered by scope).
      2. Category detector scans the rendered markdown.
      3. If violations remain, ask the LLM to rewrite up to `max_retries` times.

    The detector ignores candidates that were filtered out for the scope.
    Returns (text, remaining_violations, retry_count).
    """
    scoped_result = dict(eval_result)
    scoped_result["candidates"] = _filter_candidates_for_scope(
        eval_result.get("candidates", []), scope
    )

    text = write_gtm_report_with_llm(scoped_result, furiosa_docs_summary, scope=scope)
    violations = detect_report_violations(text, scoped_result)
    retry_count = 0

    while violations and retry_count < max_retries:
        retry_count += 1
        text = rewrite_report_with_llm(text, violations)
        violations = detect_report_violations(text, scoped_result)

    return text, violations, retry_count


def write_candidates_csv(path: Path, candidates: list[dict[str, Any]]) -> None:
    fieldnames = [
        "name",
        "country",
        "market",
        "target_type",
        "classification",
        "confirmed_project_or_signal",
        "confirmed_model_name",
        "model_match_status",
        "model_fit_score",
        "deployment_fit_score",
        "channel_fit_score",
        "rngd_fit_score",
        "outreach_priority",
        "fit_vs_priority_explanation",
        "hook_type",
        "buying_signal",
        "infrastructure_signal",
        "timing_reason",
        "customer_win",
        "furiosa_win",
        "direct_sales_possibility",
        "csp_routed_sales_possibility",
        "npuaas_adoption_possibility",
        "csp_capacity_expansion_possibility",
        "numeric_claims",
        "contact_reason",
        "revenue_timing",
        "decision_maker_hint",
        "decision_maker_profile_url",
        "decision_maker_profile_title",
        "decision_maker_profile_source",
        "decision_maker_profile_confidence",
        "decision_maker_search_queries",
        "existing_touchpoint",
        "b2g_evidence_type",
        "g2b_checked",
        "procurement_next_action",
        "source_urls",
    ]

    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for candidate in candidates:
            row = {}
            for field in fieldnames:
                value = candidate.get(field, "")

                if field == "numeric_claims":
                    value = format_numeric_claims(value)
                elif isinstance(value, list):
                    value = " | ".join(str(x) for x in value)

                row[field] = value
            writer.writerow(row)


def build_eval_markdown(eval_result: dict[str, Any], raw_llm_text: str) -> str:
    metadata = eval_result.get("_llm_metadata", {})
    summary = eval_result.get("run_summary", {})
    notes = eval_result.get("eval_notes", [])

    lines = [
        "# LLM Evaluation Notes",
        "",
        "## LLM metadata",
        "",
        f"- provider: `{metadata.get('provider')}`",
        f"- model: `{metadata.get('model')}`",
        f"- llm_sources_count: `{metadata.get('llm_sources_count')}`",
        f"- max_llm_sources: `{metadata.get('max_llm_sources')}`",
        f"- max_source_chars: `{metadata.get('max_source_chars')}`",
        f"- max_output_candidates: `{metadata.get('max_output_candidates')}`",
        f"- evaluated_at_kst: `{metadata.get('evaluated_at_kst')}`",
        "",
        "## Run summary",
        "",
        f"- overall_assessment: {summary.get('overall_assessment', '')}",
        f"- top_priority_names: {', '.join(summary.get('top_priority_names', []))}",
        f"- noise_ratio_comment: {summary.get('noise_ratio_comment', '')}",
        f"- model_compatibility_caution: {summary.get('model_compatibility_caution', '')}",
        "",
        "## Eval notes",
        "",
    ]

    for note in notes:
        lines.append(f"- {note}")

    lines.extend(
        [
            "",
            "## Raw LLM response",
            "",
            "```json",
            raw_llm_text,
            "```",
        ]
    )

    return "\n".join(lines)


def format_numeric_claims(numeric_claims: Any) -> str:
    if not isinstance(numeric_claims, list) or not numeric_claims:
        return "없음"

    parts = []
    for item in numeric_claims[:5]:
        if not isinstance(item, dict):
            continue

        claim = item.get("claim", "")
        source_id = item.get("source_id", "")
        evidence_text = item.get("evidence_text", "")

        text = claim
        if source_id:
            text += f" ({source_id})"
        if evidence_text:
            text += f" — 근거: {evidence_text[:120]}"

        parts.append(text)

    return " | ".join(parts) if parts else "없음"

def build_version_summary(candidates: list[dict[str, Any]], include_b2g: bool) -> str:
    if include_b2g:
        scoped = candidates
        title = "## 버전 2 — B2B + B2G 우선 검토 요약"
    else:
        scoped = [c for c in candidates if c.get("market") == "B2B"]
        title = "## 버전 1 — B2B only 우선 검토 요약"

    if not scoped:
        return f"{title}\n\n- 후보 없음\n"

    lines = [title, ""]

    for c in scoped:
        if c.get("classification") == "noise":
            continue

        line = (
            f"- {c.get('name', '미확인')} / "
            f"{c.get('target_type', '')} / "
            f"classification: `{c.get('classification', '')}` / "
            f"fit: `{c.get('rngd_fit_score', '')}` / "
            f"outreach: `{c.get('outreach_priority', '')}` / "
            f"매출시점: `{c.get('revenue_timing', '')}`"
        )

        if c.get("market") == "B2G":
            line += (
                f" / B2G 근거: `{c.get('b2g_evidence_type', '기사/RSS 기반')}`"
                f" / 나라장터 확인: `{c.get('g2b_checked', '미수행')}`"
            )

        lines.append(line)

    return "\n".join(lines) + "\n"

def build_candidate_report_section(eval_result: dict[str, Any]) -> str:
    candidates = eval_result.get("candidates", [])
    candidates = [
        candidate for candidate in candidates
        if candidate.get("classification") != "noise"
    ]

    if not candidates:
        return "LLM 평가 후보가 없습니다."

    priority_order = {
        "priority_outreach": 0,
        "structure_check": 1,
        "cloud_npuaaS_lead": 2,
        "watchlist": 3,
        "noise": 4,
    }

    def sort_key(candidate: dict[str, Any]) -> tuple[int, int]:
        classification = candidate.get("classification", "watchlist")
        priority = candidate.get("outreach_priority", "WATCH")
        priority_score = {"HIGH": 0, "MID": 1, "LOW": 2, "WATCH": 3}.get(priority, 4)
        return (priority_order.get(classification, 9), priority_score)

    candidates_sorted = sorted(candidates, key=sort_key)
    
    lines = [
        "## LLM 후보 평가 결과",
        "",
        build_version_summary(candidates_sorted, include_b2g=False),
        "",
        build_version_summary(candidates_sorted, include_b2g=True),
        "",
        "## 상세 후보 평가",
        "",
    ]

    for idx, c in enumerate(candidates_sorted, start=1):
        lines.extend(
            [
                f"### {idx}. {c.get('name', '미확인')}",
                "",
                f"- 국가: `{c.get('country', '')}`",
                f"- 시장: `{c.get('market', '')}`",
                f"- 타깃 유형: `{c.get('target_type', '')}`",
                f"- 분류: `{c.get('classification', '')}`",
                f"- 확인된 프로젝트/시그널: {c.get('confirmed_project_or_signal', '')}",
                f"- 확인된 모델명: `{c.get('confirmed_model_name', '')}`",
                f"- 모델 매칭 상태: `{c.get('model_match_status', '')}`",
                f"- 모델 fit_score: `{c.get('model_fit_score', '')}`",
                f"- 배포/인프라 fit_score: `{c.get('deployment_fit_score', '')}`",
                f"- 채널/CSP fit_score: `{c.get('channel_fit_score', '')}`",
                f"- RNGD fit_score: `{c.get('rngd_fit_score', '')}`",
                f"- outreach priority: `{c.get('outreach_priority', '')}`",
                f"- fit vs priority 설명: {c.get('fit_vs_priority_explanation', '')}",
                f"- hook_type: `{c.get('hook_type', '')}`",
                f"- 핵심 buying signal: {c.get('buying_signal', '')}",
                f"- 인프라 signal: {c.get('infrastructure_signal', '')}",
                f"- timing reason: {c.get('timing_reason', '')}",
                f"- 고객 win: {c.get('customer_win', '')}",
                f"- FuriosaAI win: {c.get('furiosa_win', '')}",
                f"- 직접 판매 가능성: `{c.get('direct_sales_possibility', '')}`",
                f"- CSP 경유 판매 가능성: `{c.get('csp_routed_sales_possibility', '')}`",
                f"- NPUaaS 유도 가능성: `{c.get('npuaas_adoption_possibility', '')}`",
                f"- CSP capacity 증설 가능성: `{c.get('csp_capacity_expansion_possibility', '')}`",
                f"- 수치 근거: {format_numeric_claims(c.get('numeric_claims', []))}",
                f"- 컨택 명분: {c.get('contact_reason', '')}",
                f"- 실제 컨택 시 사용할 말: {c.get('outreach_talk_track', '')}",
                f"- 매출 가능 시점: `{c.get('revenue_timing', '')}`",
                f"- 담당자 후보 힌트: {c.get('decision_maker_hint', '')}",
                f"- 공개 프로필 URL: {c.get('decision_maker_profile_url', '미확인')}",
                f"- 기존 접점: `{c.get('existing_touchpoint', '')}`",
                f"- B2G 근거 유형: `{c.get('b2g_evidence_type', '해당 없음')}`",
                f"- 나라장터 직접 확인: `{c.get('g2b_checked', '해당 없음')}`",
                f"- 조달상 다음 액션: {c.get('procurement_next_action', '해당 없음')}",
                f"- 확인 필요: {' | '.join(c.get('verification_needed', [])) if isinstance(c.get('verification_needed'), list) else c.get('verification_needed', '')}",
                f"- source_ids: {', '.join(c.get('source_ids', [])) if isinstance(c.get('source_ids'), list) else c.get('source_ids', '')}",
                f"- source_urls: {' | '.join(c.get('source_urls', [])) if isinstance(c.get('source_urls'), list) else c.get('source_urls', '')}",
                "",
            ]
        )

    return "\n".join(lines)

def short_text(value: Any, limit: int = 180) -> str:
    text = str(value or "").strip()
    text = re.sub(r"\s+", " ", text)
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"

def format_source_links(urls: Any, max_links: int = 2) -> str:
    if not isinstance(urls, list) or not urls:
        return "미확인"

    links = []
    for idx, url in enumerate(urls[:max_links], start=1):
        if not url:
            continue
        links.append(f"[출처{idx}]({url})")

    return " ".join(links) if links else "미확인"


def display_list_or_text(value: Any, limit: int = 180) -> str:
    if isinstance(value, list):
        joined = " | ".join(str(item) for item in value if item)
        return short_text(joined, limit)
    return short_text(value, limit)


def business_candidate_table(
    candidates: list[dict[str, Any]],
    include_b2g: bool,
    max_rows: int = 8,
) -> str:
    if include_b2g:
        scoped = candidates
    else:
        scoped = [c for c in candidates if c.get("market") == "B2B"]

    scoped = [
        c for c in scoped
        if c.get("classification") != "noise"
    ][:max_rows]

    if not scoped:
        return "후보 없음"

    lines = [
        "| 우선순위 | 대상 | 시장 | 유형 | 확인 모델 | 모델 매칭 | RNGD 종합 Fit | 연락 우선순위 | 왜 지금 | 권장 액션 | 출처 |",
        "|---:|---|---|---|---|---|---|---|---|---|---|",
    ]

    for idx, c in enumerate(scoped, start=1):
        why_now = short_text(c.get("timing_reason") or c.get("buying_signal"), 110)
        action = short_text(c.get("contact_reason"), 110)

        source_links = format_source_links(c.get("source_urls", []), max_links=2)
        
        lines.append(
            f"| {idx} "
            f"| {c.get('name', '미확인')} "
            f"| {c.get('market', '')} "
            f"| {c.get('target_type', '')} "
            f"| {c.get('confirmed_model_name', '미확인')} "
            f"| {c.get('model_match_status', '')} "
            f"| {c.get('rngd_fit_score', '')} "
            f"| {c.get('outreach_priority', '')} "
            f"| {why_now} "
            f"| {action} "
            f"| {source_links} |"
        )

    return "\n".join(lines)


def build_business_report(
    run_id: str,
    eval_result: dict[str, Any] | None,
    furiosa_docs_summary: dict[str, Any],
    scope: str = REPORT_SCOPE_B2B_B2G,
) -> str:
    if not eval_result:
        return "# FuriosaAI GTM 리서치\n\nLLM 평가 실패로 실전용 리포트를 생성하지 못했습니다.\n"

    if scope == REPORT_SCOPE_B2B:
        return _build_business_report_b2b(run_id, eval_result, furiosa_docs_summary)

    run_summary = eval_result.get("run_summary", {})
    candidates = eval_result.get("candidates", [])
    candidates = [
        c for c in candidates
        if isinstance(c, dict) and c.get("classification") != "noise"
    ]

    priority_order = {
        "HIGH": 0,
        "MID": 1,
        "LOW": 2,
        "WATCH": 3,
    }
    class_order = {
        "priority_outreach": 0,
        "cloud_npuaaS_lead": 1,
        "structure_check": 2,
        "watchlist": 3,
    }

    candidates_sorted = sorted(
        candidates,
        key=lambda c: (
            class_order.get(c.get("classification", "watchlist"), 9),
            priority_order.get(c.get("outreach_priority", "WATCH"), 9),
        ),
    )

    top_candidates = candidates_sorted[:3]
    b2g_candidates = [c for c in candidates_sorted if c.get("market") == "B2G"]

    today = now_kst().strftime("%Y-%m-%d")

    lines = [
        f"# FuriosaAI GTM 리서치 — {today}",
        "",
        "## 1. 한 줄 결론",
        "",
        short_text(run_summary.get("overall_assessment", ""), 450),
        "",
        "## 2. 이번 주 우선 연락 Top 3",
        "",
        "| 순위 | 대상 | 유형 | 확인 모델 | 핵심 이유 | 다음 액션 | 출처 |",
        "|---:|---|---|---|---|---|---|",
    ]

    for idx, c in enumerate(top_candidates, start=1):
        lines.append(
            f"| {idx} "
            f"| {c.get('name', '미확인')} "
            f"| {c.get('target_type', '')} "
            f"| {c.get('confirmed_model_name', '미확인')} "
            f"| {short_text(c.get('fit_vs_priority_explanation') or c.get('buying_signal'), 120)} "
            f"| {short_text(c.get('contact_reason'), 120)} "
            f"| {format_source_links(c.get('source_urls', []), max_links=2)} |"
        )

    lines.extend(
        [
            "",
            "## 3. 버전 1 — B2B only",
            "",
            business_candidate_table(candidates_sorted, include_b2g=False),
            "",
            "## 4. 버전 2 — B2B + B2G",
            "",
            business_candidate_table(candidates_sorted, include_b2g=True),
            "",
            "## 5. 우선 연락 후보 상세",
            "",
        ]
    )

    for c in candidates_sorted[:6]:
        lines.extend(
            [
                f"### {c.get('name', '미확인')}",
                "",
                f"- **시장/유형**: {c.get('market', '')} / {c.get('target_type', '')}",
                f"- **확인 모델**: {c.get('confirmed_model_name', '미확인')} / `{c.get('model_match_status', '')}`",
                f"- **RNGD 종합 Fit / 연락 우선순위**: `{c.get('rngd_fit_score', '')}` / `{c.get('outreach_priority', '')}`",
                f"- **왜 지금**: {short_text(c.get('timing_reason') or c.get('buying_signal'), 260)}",
                f"- **고객 win**: {short_text(c.get('customer_win'), 260)}",
                f"- **FuriosaAI win**: {short_text(c.get('furiosa_win'), 260)}",
                f"- **컨택 시 사용할 말**: {short_text(c.get('outreach_talk_track'), 260)}",
                f"- **담당자 힌트**: {short_text(c.get('decision_maker_hint'), 160)}",
                f"- **출처**: {format_source_links(c.get('source_urls', []), max_links=3)}",
                "",
            ]
        )

    lines.extend(
        [
            "",
            "## 6. NPUaaS / CSP 경유 기회",
            "",
        ]
    )

    cloud_leads = [
        c for c in candidates_sorted
        if c.get("target_type") in ["CSP 운영 기업", "CSP 고객 기업"]
        or c.get("csp_routed_sales_possibility") == "HIGH"
        or c.get("npuaas_adoption_possibility") == "HIGH"
    ]

    if cloud_leads:
        for c in cloud_leads[:5]:
            lines.append(
                f"- **{c.get('name', '미확인')}**: "
                f"CSP 경유 `{c.get('csp_routed_sales_possibility', '')}`, "
                f"NPUaaS `{c.get('npuaas_adoption_possibility', '')}`, "
                f"capacity 증설 `{c.get('csp_capacity_expansion_possibility', '')}`. "
                f"{short_text(c.get('fit_vs_priority_explanation'), 160)} "
                f"{format_source_links(c.get('source_urls', []), max_links=2)}"
            )
    else:
        lines.append("- 해당 후보 없음")

    lines.extend(
        [
            "",
            "## 7. B2G 후보 — 나라장터/RFP 직접 확인 전",
            "",
            "현재 B2G 후보는 기사/RSS 기반입니다. 나라장터/RFP 직접 확인 전까지는 우선 연락이 아니라 구조 확인 또는 watchlist로 해석해야 합니다.",
            "",
        ]
    )

    if b2g_candidates:
        for c in b2g_candidates[:5]:
            lines.append(
                f"- **{c.get('name', '미확인')}**: "
                f"{c.get('b2g_evidence_type', '기사/RSS 기반')}, "
                f"나라장터 확인 `{c.get('g2b_checked', '미수행')}`. "
                f"다음 액션: {c.get('procurement_next_action', '나라장터/RFP 직접 확인 필요')}. "
                f"{format_source_links(c.get('source_urls', []), max_links=2)}"
            )
    else:
        lines.append("- 이번 실행에서 B2G 후보 없음")

    lines.extend(
        [
            "",
            "## 8. 담당자 / 컨택 경로",
            "",
            "| 대상 | 담당자 힌트 | LinkedIn/공개 프로필 후보 | 신뢰도 | 기존 접점 |",
            "|---|---|---|---|---|",
        ]
    )

    for c in candidates_sorted[:8]:
        confidence = c.get("decision_maker_profile_confidence", "UNKNOWN")
        if confidence in ("HIGH", "MID"):
            url = c.get("decision_maker_profile_url") or "확인 필요"
            url_cell = f"[{url}]({url})"
            confidence_cell = confidence
        else:
            url_cell = "확인 필요"
            confidence_cell = "확인 필요"
        lines.append(
            f"| {c.get('name', '미확인')} "
            f"| {short_text(c.get('decision_maker_hint'), 80)} "
            f"| {url_cell} "
            f"| {confidence_cell} "
            f"| {c.get('existing_touchpoint', '확인 필요')} |"
        )

    lines.extend(
        [
            "",
            "## 9. 오늘/이번 주 액션",
            "",
            "### 오늘 바로 확인",
        ]
    )

    high_items = [c for c in candidates_sorted if c.get("outreach_priority") == "HIGH"]
    if high_items:
        for c in high_items:
            lines.append(
                f"- **{c.get('name', '미확인')}**: {short_text(c.get('contact_reason'), 160)}"
            )
    else:
        lines.append("- 해당 후보 없음")

    lines.extend(
        [
            "",
            "### 이번 주 구조 확인",
        ]
    )

    check_items = [c for c in candidates_sorted if c.get("outreach_priority") != "HIGH"]
    if check_items:
        for c in check_items:
            lines.append(
                f"- **{c.get('name', '미확인')}**: {display_list_or_text(c.get('verification_needed'), 180)}"
            )
    else:
        lines.append("- 해당 후보 없음")

    lines.extend(
        [
            "",
            "## 10. 경쟁사 / 시장 GTM 동향",
            "",
            "- 이번 버전에서는 후보 기업 중심으로 평가했으며, 경쟁사 GTM 동향은 별도 구조화가 필요합니다.",
            "- 다음 버전에서 고객 납품, CSP/MSP 파트너십, NPUaaS/GPUaaS 출시, 공공 수주 중심으로 분리 수집해야 합니다.",
            "",
            "## 11. 주의 사항",
            "",
            "- B2G 후보는 아직 나라장터/RFP 직접 확인 전이므로 watchlist 또는 구조 확인 후보로 해석해야 합니다.",
            "- 담당자/LinkedIn 후보는 공개 검색 결과를 기반으로 한 추정입니다. 신뢰도가 HIGH/MID가 아니면 \"확인 필요\"로 표시했으며, 단정된 담당자가 아닙니다.",
            "- 모델명이 미확인인 후보는 모델 적합성이 아니라 인프라/채널/타이밍 관점의 outreach priority로 해석해야 합니다.",
            "",
            "## 12. 핵심 출처",
            "",
        ]
    )

    seen_urls = []
    for c in candidates_sorted:
        urls = c.get("source_urls", [])
        if not isinstance(urls, list):
            continue
        for url in urls:
            if url and url not in seen_urls:
                seen_urls.append(url)

    for url in seen_urls[:20]:
        lines.append(f"- {url}")

    lines.extend(
        [
            "",
            "---",
            "",
            f"debug_run_id: `{run_id}`",
            f"furiosa_docs_successful: `{furiosa_docs_summary.get('docs_successful')}`",
        ]
    )

    return "\n".join(lines)

def _build_business_report_b2b(
    run_id: str,
    eval_result: dict[str, Any],
    furiosa_docs_summary: dict[str, Any],
) -> str:
    """Deterministic fallback for the B2B-only report (no B2G content)."""
    run_summary = eval_result.get("run_summary", {})
    candidates = [
        c for c in eval_result.get("candidates", [])
        if isinstance(c, dict)
        and c.get("classification") != "noise"
        and (c.get("market") or "").upper() != "B2G"
    ]

    priority_order = {"HIGH": 0, "MID": 1, "LOW": 2, "WATCH": 3}
    class_order = {
        "priority_outreach": 0,
        "cloud_npuaaS_lead": 1,
        "structure_check": 2,
        "watchlist": 3,
    }
    candidates_sorted = sorted(
        candidates,
        key=lambda c: (
            class_order.get(c.get("classification", "watchlist"), 9),
            priority_order.get(c.get("outreach_priority", "WATCH"), 9),
        ),
    )

    top_candidates = candidates_sorted[:3]
    today = now_kst().strftime("%Y-%m-%d")

    lines = [
        f"# FuriosaAI GTM 리서치 — B2B — {today}",
        "",
        "## 1. 한 줄 결론",
        "",
        short_text(run_summary.get("overall_assessment", ""), 450),
        "",
        "## 2. 이번 주 우선 연락 Top 3 (B2B)",
        "",
        "| 순위 | 대상 | 유형 | 확인 모델 | 핵심 이유 | 다음 액션 | 출처 |",
        "|---:|---|---|---|---|---|---|",
    ]
    for idx, c in enumerate(top_candidates, start=1):
        lines.append(
            f"| {idx} "
            f"| {c.get('name', '미확인')} "
            f"| {c.get('target_type', '')} "
            f"| {c.get('confirmed_model_name', '미확인')} "
            f"| {short_text(c.get('fit_vs_priority_explanation') or c.get('buying_signal'), 120)} "
            f"| {short_text(c.get('contact_reason'), 120)} "
            f"| {format_source_links(c.get('source_urls', []), max_links=2)} |"
        )

    lines.extend(
        [
            "",
            "## 3. B2B 후보 표",
            "",
            business_candidate_table(candidates_sorted, include_b2g=False),
            "",
            "## 4. 우선 연락 후보 상세",
            "",
        ]
    )
    for c in candidates_sorted[:6]:
        lines.extend(
            [
                f"### {c.get('name', '미확인')}",
                "",
                f"- **시장/유형**: {c.get('market', '')} / {c.get('target_type', '')}",
                f"- **확인 모델**: {c.get('confirmed_model_name', '미확인')} / `{c.get('model_match_status', '')}`",
                f"- **RNGD 종합 Fit / 연락 우선순위**: `{c.get('rngd_fit_score', '')}` / `{c.get('outreach_priority', '')}`",
                f"- **왜 지금**: {short_text(c.get('timing_reason') or c.get('buying_signal'), 260)}",
                f"- **고객 win**: {short_text(c.get('customer_win'), 260)}",
                f"- **FuriosaAI win**: {short_text(c.get('furiosa_win'), 260)}",
                f"- **컨택 시 사용할 말**: {short_text(c.get('outreach_talk_track'), 260)}",
                f"- **담당자 힌트**: {short_text(c.get('decision_maker_hint'), 160)}",
                f"- **출처**: {format_source_links(c.get('source_urls', []), max_links=3)}",
                "",
            ]
        )

    lines.extend(
        [
            "",
            "## 5. NPUaaS / CSP 경유 기회",
            "",
        ]
    )
    cloud_leads = [
        c for c in candidates_sorted
        if c.get("target_type") in ["CSP 운영 기업", "CSP 고객 기업"]
        or c.get("csp_routed_sales_possibility") == "HIGH"
        or c.get("npuaas_adoption_possibility") == "HIGH"
    ]
    if cloud_leads:
        for c in cloud_leads[:5]:
            lines.append(
                f"- **{c.get('name', '미확인')}**: "
                f"CSP 경유 `{c.get('csp_routed_sales_possibility', '')}`, "
                f"NPUaaS `{c.get('npuaas_adoption_possibility', '')}`, "
                f"capacity 증설 `{c.get('csp_capacity_expansion_possibility', '')}`. "
                f"{short_text(c.get('fit_vs_priority_explanation'), 160)} "
                f"{format_source_links(c.get('source_urls', []), max_links=2)}"
            )
    else:
        lines.append("- 해당 후보 없음")

    lines.extend(
        [
            "",
            "## 6. 담당자 / 컨택 경로",
            "",
            "| 대상 | 담당자 힌트 | LinkedIn/공개 프로필 후보 | 신뢰도 | 기존 접점 |",
            "|---|---|---|---|---|",
        ]
    )
    for c in candidates_sorted[:8]:
        confidence = c.get("decision_maker_profile_confidence", "UNKNOWN")
        if confidence in ("HIGH", "MID"):
            url = c.get("decision_maker_profile_url") or "확인 필요"
            url_cell = f"[{url}]({url})"
            confidence_cell = confidence
        else:
            url_cell = "확인 필요"
            confidence_cell = "확인 필요"
        lines.append(
            f"| {c.get('name', '미확인')} "
            f"| {short_text(c.get('decision_maker_hint'), 80)} "
            f"| {url_cell} "
            f"| {confidence_cell} "
            f"| {c.get('existing_touchpoint', '확인 필요')} |"
        )

    lines.extend(
        [
            "",
            "## 7. 경쟁사 GTM 동향",
            "",
            "- 이번 버전은 후보 평가 중심이며, 경쟁사 GTM(고객 납품, 파트너십, NPUaaS/GPUaaS 출시, 공공 수주) 별도 구조화는 다음 버전에서 추가할 예정입니다.",
            "",
            "## 8. 주의 사항",
            "",
            "- 이 리포트는 B2B 전용입니다. B2G/공공 후보는 별도 B2B+B2G 리포트를 확인하세요.",
            "- 담당자/LinkedIn 후보는 공개 검색 결과 기반의 추정입니다. 신뢰도가 HIGH/MID가 아니면 \"확인 필요\"로 표시했습니다.",
            "- 모델명이 미확인인 후보는 인프라/채널/타이밍 관점으로만 해석해야 합니다.",
            "",
            "---",
            "",
            f"debug_run_id: `{run_id}`",
            f"furiosa_docs_successful: `{furiosa_docs_summary.get('docs_successful')}`",
            "scope: `b2b`",
        ]
    )
    return "\n".join(lines)


def build_landing_markdown(
    eval_result: dict[str, Any] | None,
    run_id: str,
) -> str:
    today = now_kst().strftime("%Y-%m-%d")
    overall = ""
    n_b2b = 0
    n_b2g = 0
    n_total = 0
    if eval_result and isinstance(eval_result.get("candidates"), list):
        cands = [
            c for c in eval_result["candidates"]
            if isinstance(c, dict) and c.get("classification") != "noise"
        ]
        n_total = len(cands)
        n_b2g = sum(1 for c in cands if (c.get("market") or "").upper() == "B2G")
        n_b2b = n_total - n_b2g
        overall = short_text(eval_result.get("run_summary", {}).get("overall_assessment", ""), 450)

    lines = [
        f"# FuriosaAI GTM 리서치 — {today}",
        "",
        "## 한 줄 결론",
        "",
        overall or "이번 실행에서 후보 평가 결과를 확인하지 못했습니다.",
        "",
        "## 리포트 페이지",
        "",
        "- [B2B 전용 리포트](gtm_report_b2b.md)",
        "- [B2B + B2G 통합 리포트](gtm_report_b2b_b2g.md)",
        "",
        "## 실행 요약",
        "",
        f"- run_id: `{run_id}`",
        f"- agent_version: `{AGENT_VERSION}`",
        f"- 비-노이즈 후보 수: `{n_total}`",
        f"- B2B 후보 수: `{n_b2b}`",
        f"- B2G 후보 수: `{n_b2g}`",
        "",
    ]
    return "\n".join(lines)


def write_business_report(
    run_dir: Path,
    run_id: str,
    furiosa_docs_summary: dict[str, Any],
    eval_result: dict[str, Any] | None,
) -> dict[str, Any]:
    """
    Produces three markdown files per run:
      - gtm_report_b2b.md       (B2B-only)
      - gtm_report_b2b_b2g.md   (B2B + B2G)
      - gtm_report.md           (compatibility landing page that links to both)

    Each scoped report is written by the LLM (with validation/rewrite loop);
    failures degrade to the deterministic builder for that scope. The landing
    page is always generated deterministically from eval_result.

    Returns aggregated metadata for the metadata.json + footer.
    """
    meta: dict[str, Any] = {
        "writer": "deterministic_fallback",
        "llm_error": "",
        "scopes": {
            REPORT_SCOPE_B2B: {
                "writer": "deterministic_fallback",
                "validation_passed": False,
                "violations": [],
                "retry_count": 0,
                "llm_error": "",
            },
            REPORT_SCOPE_B2B_B2G: {
                "writer": "deterministic_fallback",
                "validation_passed": False,
                "violations": [],
                "retry_count": 0,
                "llm_error": "",
            },
        },
        "pages_written": [],
    }

    scope_file = {
        REPORT_SCOPE_B2B: "gtm_report_b2b.md",
        REPORT_SCOPE_B2B_B2G: "gtm_report_b2b_b2g.md",
    }

    def _write_one(scope: str) -> None:
        out_path = run_dir / scope_file[scope]
        scope_meta = meta["scopes"][scope]

        if eval_result and eval_result.get("candidates"):
            try:
                text, violations, retry_count = write_gtm_report_with_validation(
                    eval_result=eval_result,
                    furiosa_docs_summary=furiosa_docs_summary,
                    scope=scope,
                )
                scope_meta["writer"] = "llm"
                scope_meta["validation_passed"] = not violations
                scope_meta["violations"] = violations
                scope_meta["retry_count"] = retry_count

                footer_lines = [
                    "",
                    "---",
                    "",
                    f"debug_run_id: `{run_id}`  ",
                    f"scope: `{scope}`  ",
                    f"furiosa_docs_successful: `{furiosa_docs_summary.get('docs_successful')}`  ",
                    "report_writer: `llm`  ",
                    f"report_writer_retry_count: `{retry_count}`  ",
                    f"report_validation_passed: `{scope_meta['validation_passed']}`  ",
                ]
                if violations:
                    footer_lines.append(
                        "report_validation_violations: "
                        + ", ".join(sorted({v["category"] for v in violations}))
                    )
                out_path.write_text(text + "\n" + "\n".join(footer_lines) + "\n", encoding="utf-8")
                meta["pages_written"].append(scope_file[scope])
                return
            except Exception as exc:
                scope_meta["llm_error"] = str(exc)
                if not meta["llm_error"]:
                    meta["llm_error"] = str(exc)
                print(f"Report-writer LLM FAILED for scope={scope}, falling back: {exc}")

        fallback = build_business_report(
            run_id=run_id,
            eval_result=eval_result,
            furiosa_docs_summary=furiosa_docs_summary,
            scope=scope,
        )
        out_path.write_text(fallback, encoding="utf-8")
        meta["pages_written"].append(scope_file[scope])

    _write_one(REPORT_SCOPE_B2B)
    _write_one(REPORT_SCOPE_B2B_B2G)

    # Compatibility landing page (deterministic, links to both scopes).
    landing = build_landing_markdown(eval_result, run_id)
    (run_dir / "gtm_report.md").write_text(landing, encoding="utf-8")
    meta["pages_written"].append("gtm_report.md")

    # Top-level writer label = "llm" if either scope succeeded via LLM.
    if any(
        meta["scopes"][s]["writer"] == "llm"
        for s in (REPORT_SCOPE_B2B, REPORT_SCOPE_B2B_B2G)
    ):
        meta["writer"] = "llm"

    # Flat top-level keys for the existing metadata schema (worst-case across scopes).
    meta["validation_passed"] = all(
        meta["scopes"][s]["validation_passed"]
        for s in (REPORT_SCOPE_B2B, REPORT_SCOPE_B2B_B2G)
    )
    meta["violations"] = (
        list(meta["scopes"][REPORT_SCOPE_B2B]["violations"])
        + list(meta["scopes"][REPORT_SCOPE_B2B_B2G]["violations"])
    )
    meta["retry_count"] = (
        meta["scopes"][REPORT_SCOPE_B2B]["retry_count"]
        + meta["scopes"][REPORT_SCOPE_B2B_B2G]["retry_count"]
    )
    return meta

def write_json(path: Path, data: Any) -> None:
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def write_report(
    run_dir: Path,
    run_id: str,
    mode: str,
    memo: str | None,
    naver_sources: list[dict[str, Any]],
    rss_sources: list[dict[str, Any]],
    merged_sources: list[dict[str, Any]],
    furiosa_docs_summary: dict[str, Any],
    eval_result: dict[str, Any] | None,
    llm_error: str | None,
) -> None:
    instructions = load_instructions()
    instruction_chars = len(instructions)

    furiosa_summary_text = summarize_furiosa_docs_for_report(furiosa_docs_summary)
    source_summary = summarize_sources_for_report(merged_sources)
    eval_section = (
        build_candidate_report_section(eval_result)
        if eval_result
        else f"LLM 평가 실패 또는 미실행: {llm_error or 'unknown'}"
    )

    run_summary = eval_result.get("run_summary", {}) if eval_result else {}

    report = f"""# FuriosaAI GTM Research Agent Test Run

## 실행 정보

- run_id: `{run_id}`
- mode: `{mode}`
- memo: `{memo or ""}`
- executed_at_kst: `{now_kst().isoformat()}`
- agent_version: `{AGENT_VERSION}`
- instructions_loaded_chars: `{instruction_chars}`
- naver_sources_recent_7d_count: `{len(naver_sources)}`
- rss_sources_recent_7d_count: `{len(rss_sources)}`
- merged_sources_recent_7d_count: `{len(merged_sources)}`
- furiosa_docs_successful: `{furiosa_docs_summary.get("docs_successful")}`
- furiosa_docs_failed: `{furiosa_docs_summary.get("docs_failed")}`
- llm_called: `{bool(eval_result)}`
- llm_error: `{llm_error or ""}`

## 현재 단계

이 실행은 {AGENT_VERSION} 테스트입니다.

이번 버전에서는 네이버 뉴스 API, RSS feed, FuriosaAI 공개 개발자 문서를 수집한 뒤 Gemini로 GTM 후보를 1차 평가하고, 별도 LLM 호출로 매니저용 gtm_report.md를 작성합니다.

아직 나라장터 직접 API, 담당자 심화 탐색, Notion 업로드는 수행하지 않았습니다.

## LLM 실행 요약

- overall_assessment: {run_summary.get("overall_assessment", "")}
- top_priority_names: {", ".join(run_summary.get("top_priority_names", [])) if isinstance(run_summary.get("top_priority_names"), list) else ""}
- noise_ratio_comment: {run_summary.get("noise_ratio_comment", "")}
- model_compatibility_caution: {run_summary.get("model_compatibility_caution", "")}

{eval_section}

## FuriosaAI 공개 문서 refresh 요약

{furiosa_summary_text}

## 통합 수집 요약

{source_summary}

## 다음 단계

1. LLM 후보 품질 확인
2. 노이즈가 많으면 NAVER_QUERIES / RSS_FEEDS 개선
3. 후보가 너무 적으면 MAX_LLM_SOURCES 상향
4. Gemini 3.5 Flash vs 2.5 Flash 품질 비교
5. 나라장터/B2G 수집 추가
6. 담당자/의사결정자 탐색 추가
7. Notion 또는 Google Docs 업로드 추가
"""

    (run_dir / "report.md").write_text(report, encoding="utf-8")


def write_metadata(
    run_dir: Path,
    run_id: str,
    mode: str,
    memo: str | None,
    naver_sources: list[dict[str, Any]],
    rss_sources: list[dict[str, Any]],
    merged_sources: list[dict[str, Any]],
    furiosa_docs_summary: dict[str, Any],
    eval_result: dict[str, Any] | None,
    llm_error: str | None,
    report_writer_meta: dict[str, Any] | None = None,
    decision_maker_meta: dict[str, Any] | None = None,
) -> None:
    writer_meta = report_writer_meta or {}
    dm_meta = decision_maker_meta or {}
    metadata = {
        "run_id": run_id,
        "mode": mode,
        "memo": memo or "",
        "executed_at_kst": now_kst().isoformat(),
        "agent_version": AGENT_VERSION,
        "prompt_file": str(PROMPT_PATH.relative_to(ROOT)),
        "notion_uploaded": False,
        "google_docs_uploaded": False,
        "naver_api_called": True,
        "naver_sources_recent_7d_count": len(naver_sources),
        "rss_called": True,
        "rss_sources_recent_7d_count": len(rss_sources),
        "merged_sources_recent_7d_count": len(merged_sources),
        "furiosa_docs_called": True,
        "furiosa_docs_successful": furiosa_docs_summary.get("docs_successful"),
        "furiosa_docs_failed": furiosa_docs_summary.get("docs_failed"),
        "llm_called": bool(eval_result),
        "llm_provider": "gemini" if eval_result else "",
        "llm_model": os.getenv("LLM_MODEL", "gemini-3.5-flash") if eval_result else "",
        "llm_error": llm_error or "",
        "report_writer": writer_meta.get("writer", ""),
        "report_writer_llm_error": writer_meta.get("llm_error", ""),
        "report_writer_retry_count": writer_meta.get("retry_count", 0),
        "report_validation_passed": writer_meta.get("validation_passed", False),
        "report_validation_violations": writer_meta.get("violations", []),
        "report_pages_generated": writer_meta.get(
            "pages_written",
            ["gtm_report_b2b.md", "gtm_report_b2b_b2g.md", "gtm_report.md"],
        ),
        "report_scopes": writer_meta.get("scopes", {}),
        "pages_generated": [
            "docs/index.html",
            "docs/b2b.html",
            "docs/b2b-b2g.html",
        ],
        "llm_retry_count": get_llm_retry_count(),
        "llm_max_retries": env_int("LLM_MAX_RETRIES", 4),
        "max_llm_sources": MAX_LLM_SOURCES,
        "max_source_chars": MAX_SOURCE_CHARS,
        "max_output_candidates": MAX_OUTPUT_CANDIDATES,
        "g2b_called": False,
        "decision_maker_search_called": bool(dm_meta.get("called", False)),
        "decision_maker_profiles_count": int(dm_meta.get("count", 0)),
        "decision_maker_search_error": dm_meta.get("error", "") or "",
    }

    write_json(run_dir / "metadata.json", metadata)


def update_index(run_id: str, mode: str, memo: str | None) -> None:
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    index_path = DOCS_DIR / "index.md"

    if index_path.exists():
        existing = index_path.read_text(encoding="utf-8")
    else:
        existing = """# FuriosaAI GTM Research Agent Runs

이 페이지는 GitHub Actions로 실행된 GTM Research Agent 테스트/운영 결과 목록입니다.

## Runs

"""

    run_time = now_kst().strftime("%Y-%m-%d %H:%M:%S KST")
    link = (
        f"- {run_time} / `{mode}` / {memo or ''} "
        f"— [B2B](../runs/{mode}/{run_id}/gtm_report_b2b.md) "
        f"/ [B2B+B2G](../runs/{mode}/{run_id}/gtm_report_b2b_b2g.md) "
        f"/ [landing](../runs/{mode}/{run_id}/gtm_report.md) "
        f"/ [debug](../runs/{mode}/{run_id}/report.md) "
        f"/ [candidates](../runs/{mode}/{run_id}/candidates.json) "
        f"/ [merged_sources](../runs/{mode}/{run_id}/sources_merged.json) "
        f"/ [furiosa_docs](../runs/{mode}/{run_id}/furiosa_docs_snapshot.md)\n"
    )

    existing = existing.rstrip() + "\n" + link
    index_path.write_text(existing, encoding="utf-8")


SAMPLE_EVAL_RESULT_FOR_TEST: dict[str, Any] = {
    "run_summary": {
        "overall_assessment": "샘플: 보수적으로 검토할 가치가 있는 후보가 일부 확인되었습니다.",
        "top_priority_names": ["샘플 CSP운영사", "샘플 금융사"],
        "noise_ratio_comment": "샘플 데이터.",
        "model_compatibility_caution": "샘플 데이터.",
    },
    "candidates": [
        {
            "name": "샘플 CSP운영사",
            "country": "KR",
            "market": "B2B",
            "target_type": "CSP 운영 기업",
            "classification": "priority_outreach",
            "confirmed_project_or_signal": "AI 클라우드 신규 inference 서비스 공지",
            "confirmed_model_name": "미확인",
            "model_match_status": "unknown",
            "model_fit_score": "HIGH",
            "deployment_fit_score": "HIGH",
            "channel_fit_score": "HIGH",
            "rngd_fit_score": "HIGH",
            "outreach_priority": "HIGH",
            "fit_vs_priority_explanation": "CSP 운영사라 채널/인프라 관점에서 검토 가능.",
            "buying_signal": "신규 inference 서비스 출시 발표",
            "infrastructure_signal": "데이터센터 추가 발표",
            "timing_reason": "최근 한 달 내 공지",
            "customer_win": "AI 추론 capacity 확보 가능성",
            "furiosa_win": "NPUaaS 편입 가능성",
            "numeric_claims": [],
            "contact_reason": "신규 서비스 공지 직후 구조 확인",
            "outreach_talk_track": "신규 서비스 라인업 관련 RNGD 적합성 논의",
            "revenue_timing": "중기",
            "decision_maker_hint": "Head of AI Cloud",
            "existing_touchpoint": "확인 필요",
            "verification_needed": ["모델 확정 시점"],
            "source_ids": ["S001"],
            "source_urls": ["https://example.com/csp-news"],
        },
        {
            "name": "샘플 금융사",
            "country": "KR",
            "market": "B2B",
            "target_type": "온프레미스 기업",
            "classification": "structure_check",
            "confirmed_project_or_signal": "EXAONE 도입 발표",
            "confirmed_model_name": "EXAONE",
            "model_match_status": "family_only",
            "model_fit_score": "HIGH",
            "deployment_fit_score": "MID",
            "channel_fit_score": "MID",
            "rngd_fit_score": "HIGH",
            "outreach_priority": "MID",
            "fit_vs_priority_explanation": "EXAONE family 도입 발표는 확인됨, 정확한 버전은 미확인.",
            "buying_signal": "EXAONE 도입 발표",
            "infrastructure_signal": "프라이빗 AI 구축 계획",
            "timing_reason": "최근 공지",
            "customer_win": "프라이빗 AI 구조 확보 가능성",
            "furiosa_win": "EXAONE 정확 버전 매칭 시 적합도 검토 가능",
            "numeric_claims": [],
            "contact_reason": "EXAONE 정확 버전 확인 후 구조 논의",
            "outreach_talk_track": "EXAONE 버전과 추론 처리량 가정 확인",
            "revenue_timing": "중기",
            "decision_maker_hint": "CTO / Head of AI",
            "existing_touchpoint": "확인 필요",
            "verification_needed": ["정확한 EXAONE 버전"],
            "source_ids": ["S002"],
            "source_urls": ["https://example.com/finance-news"],
        },
        {
            "name": "샘플 공공기관",
            "country": "KR",
            "market": "B2G",
            "target_type": "온프레미스 기업",
            "classification": "structure_check",
            "confirmed_project_or_signal": "공공 RAG 구축 사업 공고",
            "confirmed_model_name": "미확인",
            "model_match_status": "unknown",
            "model_fit_score": "MID",
            "deployment_fit_score": "MID",
            "channel_fit_score": "LOW",
            "rngd_fit_score": "MID",
            "outreach_priority": "LOW",
            "fit_vs_priority_explanation": "공공 사업이라 G2B 직접 확인 전까지 보수적으로 본다.",
            "buying_signal": "RAG 구축 사업 공고",
            "infrastructure_signal": "공공 데이터센터 활용 가능성",
            "timing_reason": "공고 게시 직후",
            "customer_win": "공공 활용 사례 가능성",
            "furiosa_win": "공공 reference 가능성 검토",
            "numeric_claims": [],
            "contact_reason": "공고 구조 확인 후 사업자 매핑",
            "outreach_talk_track": "사업 구조와 NPU 적합성 논의",
            "revenue_timing": "장기",
            "decision_maker_hint": "정보화 담당관",
            "existing_touchpoint": "확인 필요",
            "verification_needed": ["사업자/RFP 상세"],
            "source_ids": ["S003"],
            "source_urls": ["https://example.com/g2b-news"],
        },
    ],
    "eval_notes": ["샘플 데이터로 오프라인 검증."],
}


def run_selftest() -> int:
    """
    Offline validation. Does not call any network or LLM.

    Verifies:
      - unknown model_match_status forces model_fit_score=UNKNOWN and never HIGH
      - family_only never produces HIGH model_fit_score or HIGH rngd_fit_score
      - B2G candidates carry the 기사/RSS 기반 + 미수행 labels
      - The deterministic gtm_report.md fallback renders without crashing
    """
    failures: list[str] = []

    result = postprocess_eval_result(json.loads(json.dumps(SAMPLE_EVAL_RESULT_FOR_TEST)))
    cands = {c["name"]: c for c in result["candidates"]}

    csp = cands["샘플 CSP운영사"]
    if csp.get("model_fit_score") == "HIGH":
        failures.append("unknown 모델인데 model_fit_score가 HIGH로 남았다.")
    if csp.get("model_fit_score") != "UNKNOWN":
        failures.append(f"unknown 모델이면 model_fit_score=UNKNOWN이어야 한다 (got {csp.get('model_fit_score')}).")
    if csp.get("rngd_fit_score") == "HIGH":
        failures.append("unknown 모델인데 rngd_fit_score가 HIGH로 남았다.")

    fin = cands["샘플 금융사"]
    if fin.get("model_fit_score") == "HIGH":
        failures.append("family_only인데 model_fit_score가 HIGH로 남았다.")
    if fin.get("rngd_fit_score") == "HIGH":
        failures.append("family_only인데 rngd_fit_score가 HIGH로 남았다.")

    gov = cands["샘플 공공기관"]
    if gov.get("b2g_evidence_type") != "기사/RSS 기반":
        failures.append(f"B2G 후보에 기사/RSS 기반 라벨이 없다 (got {gov.get('b2g_evidence_type')}).")
    if gov.get("g2b_checked") != "미수행":
        failures.append(f"B2G 후보에 나라장터 미수행 라벨이 없다 (got {gov.get('g2b_checked')}).")

    try:
        markdown = build_business_report(
            run_id="selftest",
            eval_result=result,
            furiosa_docs_summary={"docs_successful": 0, "docs_failed": 0},
        )
        required_headers = [
            "## 1.",
            "## 2.",
            "## 3. 버전 1 — B2B only",
            "## 4. 버전 2 — B2B + B2G",
            "## 5.",
            "## 6. NPUaaS / CSP 경유 기회",
            "## 7. B2G 후보 — 나라장터/RFP 직접 확인 전",
            "## 8.",
        ]
        for header in required_headers:
            if header not in markdown:
                failures.append(f"deterministic gtm_report.md에 필수 섹션이 없다: {header}")
    except Exception as exc:
        failures.append(f"deterministic gtm_report.md 빌드가 예외로 실패: {exc}")

    # scope='b2b' must omit B2G content and the §7 B2G section.
    try:
        b2b_md = build_business_report(
            run_id="selftest",
            eval_result=result,
            furiosa_docs_summary={"docs_successful": 0, "docs_failed": 0},
            scope=REPORT_SCOPE_B2B,
        )
        if "B2G 후보 — 나라장터" in b2b_md:
            failures.append("B2B 전용 리포트에 B2G 섹션이 남아 있다.")
        if "샘플 공공기관" in b2b_md:
            failures.append("B2B 전용 리포트에 B2G 후보가 본문에 노출되었다.")
        if "버전 2 — B2B + B2G" in b2b_md:
            failures.append("B2B 전용 리포트에 B2B+B2G 통합 표가 남아 있다.")
        if "## 3. B2B 후보 표" not in b2b_md:
            failures.append("B2B 전용 리포트에 §3 B2B 후보 표 헤더가 없다.")
    except Exception as exc:
        failures.append(f"build_business_report(scope='b2b')가 예외로 실패: {exc}")

    # scope='b2b_b2g' must include the B2G candidate.
    try:
        bbg_md = build_business_report(
            run_id="selftest",
            eval_result=result,
            furiosa_docs_summary={"docs_successful": 0, "docs_failed": 0},
            scope=REPORT_SCOPE_B2B_B2G,
        )
        if "샘플 공공기관" not in bbg_md:
            failures.append("B2B+B2G 리포트에 B2G 후보가 노출되지 않았다.")
        if "B2G 후보 — 나라장터" not in bbg_md:
            failures.append("B2B+B2G 리포트에 §7 B2G 섹션 헤더가 없다.")
    except Exception as exc:
        failures.append(f"build_business_report(scope='b2b_b2g')가 예외로 실패: {exc}")

    # _filter_candidates_for_scope shape check.
    raw = result.get("candidates", [])
    filtered_b2b = _filter_candidates_for_scope(raw, REPORT_SCOPE_B2B)
    if any((c.get("market") or "").upper() == "B2G" for c in filtered_b2b):
        failures.append("_filter_candidates_for_scope('b2b')가 B2G 후보를 남겼다.")
    filtered_all = _filter_candidates_for_scope(raw, REPORT_SCOPE_B2B_B2G)
    if not any((c.get("market") or "").upper() == "B2G" for c in filtered_all):
        failures.append("_filter_candidates_for_scope('b2b_b2g')가 B2G 후보를 모두 빼버렸다.")

    # Landing markdown links to both reports.
    landing = build_landing_markdown(result, "selftest-run")
    for needle in ("gtm_report_b2b.md", "gtm_report_b2b_b2g.md", "B2B 전용 리포트", "B2B + B2G 통합 리포트"):
        if needle not in landing:
            failures.append(f"landing markdown에 '{needle}'가 없다.")

    sample_report = (
        "# FuriosaAI GTM 리서치 — 2026-05-25\n"
        "\n"
        "## 1. 한 줄 결론\n"
        "샘플.\n"
        "\n"
        "## 5. 우선 연락 후보 상세\n"
        "\n"
        "### 샘플 CSP운영사\n"
        "- 압도적 비용 절감 가능\n"
        "- 전력 절감 확실\n"
        "- 2배 빠른 추론을 보장합니다\n"
        "- 대규모 도입 예상\n"
        "- 출처: [출처1](https://example.com)\n"
        "\n"
        "### 샘플 금융사\n"
        "- 비용 구조 확인 필요\n"
        "- 출처: [출처1](https://example.com)\n"
    )

    violations = detect_report_violations(sample_report, result)
    found = {(v["category"], v["candidate"]) for v in violations}
    expected_pairs = [
        ("hype_language", "샘플 CSP운영사"),
        ("unsupported_cost_reduction_claim", "샘플 CSP운영사"),
        ("unsupported_power_reduction_claim", "샘플 CSP운영사"),
        ("unsupported_performance_guarantee", "샘플 CSP운영사"),
        ("unsupported_scale_claim", "샘플 CSP운영사"),
    ]
    for cat, cand in expected_pairs:
        if (cat, cand) not in found:
            failures.append(f"detector가 {cand} 섹션의 {cat}를 잡지 못했다.")

    for v in violations:
        if v["candidate"] == "샘플 금융사":
            failures.append(
                f"detector가 보수적 표현인 '샘플 금융사' 섹션을 잘못 잡았다: {v['category']} / {v['match']}"
            )

    result_with_numeric = json.loads(json.dumps(result))
    for c in result_with_numeric["candidates"]:
        if c["name"] == "샘플 CSP운영사":
            c["numeric_claims"] = [
                {
                    "claim": "도입 규모 명시",
                    "source_id": "S001",
                    "source_url": "https://example.com",
                    "evidence_text": "샘플 근거",
                }
            ]
    gated = detect_report_violations(sample_report, result_with_numeric)
    numeric_categories_under_csp = {
        v["category"]
        for v in gated
        if v["candidate"] == "샘플 CSP운영사" and v["category"] in NUMERIC_GATED_CATEGORIES
    }
    if numeric_categories_under_csp:
        failures.append(
            "numeric_claims가 있는 후보의 섹션에서 수치-게이팅 카테고리가 여전히 잡혔다: "
            + ", ".join(sorted(numeric_categories_under_csp))
        )
    if not any(v["category"] == "hype_language" for v in gated):
        failures.append("hype_language는 numeric_claims와 무관하게 항상 잡혀야 한다.")

    # v0.7: decision-maker discovery — 네트워크 없이 순수 로직만 검증.
    from decision_makers import (
        B2G_ROLE_TERMS,
        ROLE_TERMS_BY_TARGET,
        build_queries_for_candidate,
        classify_result,
        roles_for_candidate,
    )

    csp_roles = roles_for_candidate({"target_type": "CSP 운영 기업", "market": "B2B"})
    if "Head of Cloud" not in csp_roles:
        failures.append("CSP 운영 기업 후보의 role 목록에 Head of Cloud가 없다.")

    b2g_roles = roles_for_candidate({"target_type": "온프레미스 기업", "market": "B2G"})
    if b2g_roles != B2G_ROLE_TERMS:
        failures.append("B2G 후보는 market=B2G일 때 B2G 전용 role 목록을 사용해야 한다.")

    onprem_roles = roles_for_candidate({"target_type": "온프레미스 기업", "market": "B2B"})
    if onprem_roles != ROLE_TERMS_BY_TARGET["온프레미스 기업"]:
        failures.append("온프레미스 기업 role 목록이 ROLE_TERMS_BY_TARGET과 다르다.")

    queries = build_queries_for_candidate(
        {"name": "샘플 CSP운영사", "target_type": "CSP 운영 기업", "market": "B2B"}
    )
    if not queries:
        failures.append("build_queries_for_candidate가 빈 리스트를 반환했다.")
    elif not all("샘플 CSP운영사" in q and "LinkedIn" in q for q in queries):
        failures.append("쿼리에 회사명과 LinkedIn이 모두 포함되어야 한다.")
    elif len(queries) > 4:
        failures.append(f"쿼리 수가 4를 초과했다: {len(queries)}")

    high = classify_result(
        {
            "link": "https://www.linkedin.com/in/janedoe",
            "title": "Jane Doe – Head of AI at 샘플 CSP운영사",
            "description": "Head of AI at 샘플 CSP운영사",
        },
        "샘플 CSP운영사",
        ["Head of AI"],
    )
    if high != "HIGH":
        failures.append(f"linkedin.com/in + 회사명 + role 조합은 HIGH여야 한다 (got {high}).")

    mid = classify_result(
        {
            "link": "https://news.example.com/article",
            "title": "샘플 CSP운영사, 신임 Head of Cloud 임명",
            "description": "샘플 CSP운영사가 신임 Head of Cloud로 김 모씨를 임명했다",
        },
        "샘플 CSP운영사",
        ["Head of Cloud"],
    )
    if mid != "MID":
        failures.append(f"회사명 + role(뉴스)은 MID여야 한다 (got {mid}).")

    low = classify_result(
        {
            "link": "https://www.linkedin.com/in/unrelated-person",
            "title": "Unrelated Profile",
            "description": "",
        },
        "샘플 CSP운영사",
        ["Head of Cloud"],
    )
    if low not in ("LOW", "UNKNOWN"):
        failures.append(f"LinkedIn URL만 있고 회사·role 매칭 없으면 LOW 이하여야 한다 (got {low}).")

    unknown = classify_result(
        {
            "link": "https://blog.example.com/random",
            "title": "다른 회사 이야기",
            "description": "전혀 관련 없는 내용",
        },
        "샘플 CSP운영사",
        ["Head of Cloud"],
    )
    if unknown != "UNKNOWN":
        failures.append(f"매칭이 전혀 없으면 UNKNOWN이어야 한다 (got {unknown}).")

    # v0.7.1: Gemini retry helpers — pure logic, no network.
    if _retry_delays(4) != [0, 10, 30, 60]:
        failures.append(f"_retry_delays(4)는 [0,10,30,60]이어야 한다 (got {_retry_delays(4)}).")
    if _retry_delays(1) != [0]:
        failures.append(f"_retry_delays(1)는 [0]이어야 한다 (got {_retry_delays(1)}).")
    five = _retry_delays(5)
    if len(five) != 5 or five[:4] != [0, 10, 30, 60] or five[4] <= 60:
        failures.append(f"_retry_delays(5)는 4개 기본값 뒤로 더 큰 값이 추가되어야 한다 (got {five}).")

    transient_samples = [
        Exception("503 UNAVAILABLE The service is currently unavailable."),
        Exception("Server disconnected without sending a response"),
        RuntimeError("Read timed out after 30s"),
        Exception("429 Too Many Requests"),
        ConnectionResetError("Connection reset by peer"),
        Exception("ServiceUnavailable: model is overloaded due to high demand"),
        Exception("DeadlineExceeded: 504"),
    ]
    for exc in transient_samples:
        if not _is_transient_llm_error(exc):
            failures.append(
                f"_is_transient_llm_error가 transient 예외를 잡지 못했다: {type(exc).__name__}: {exc}"
            )

    non_transient_samples = [
        ValueError("invalid prompt"),
        KeyError("missing field"),
        Exception("PERMISSION_DENIED: invalid API key"),
        Exception("INVALID_ARGUMENT: prompt too long"),
    ]
    for exc in non_transient_samples:
        if _is_transient_llm_error(exc):
            failures.append(
                f"_is_transient_llm_error가 non-transient를 잘못 transient로 판정했다: {exc}"
            )

    if failures:
        print("SELFTEST FAILED")
        for f in failures:
            print(f"  - {f}")
        return 1

    print("SELFTEST OK")
    print(f"  candidates validated: {len(result['candidates'])}")
    print(f"  detector violations on sample report: {len(violations)}")
    return 0


def main() -> None:
    mode = os.getenv("RUN_MODE", "test")
    memo = os.getenv("RUN_MEMO", "manual-test")

    reset_llm_retry_count()

    run_id = build_run_id(mode, memo)

    run_dir = RUNS_DIR / mode / run_id
    run_dir.mkdir(parents=True, exist_ok=True)

    instructions = load_instructions()

    furiosa_docs = collect_furiosa_docs()
    furiosa_docs_snapshot = build_furiosa_snapshot(furiosa_docs)
    furiosa_docs_summary = build_furiosa_summary(furiosa_docs)

    dynamic_model_queries = build_dynamic_model_queries(furiosa_docs_summary)

    naver_queries = (
        BASE_NAVER_QUERIES
        + CSP_ROUTE_QUERIES
        + B2G_ROUTE_QUERIES
        + COMPETITOR_GTM_QUERIES
        + dynamic_model_queries
    )
    naver_queries = list(dict.fromkeys(naver_queries))

    write_json(
        run_dir / "naver_queries.json",
        {
            "base_queries_count": len(BASE_NAVER_QUERIES),
            "csp_route_queries_count": len(CSP_ROUTE_QUERIES),
            "b2g_route_queries_count": len(B2G_ROUTE_QUERIES),
            "competitor_gtm_queries_count": len(COMPETITOR_GTM_QUERIES),
            "dynamic_model_queries_count": len(dynamic_model_queries),
            "total_naver_queries_count": len(naver_queries),
            "dynamic_model_queries": dynamic_model_queries,
            "all_naver_queries": naver_queries,
        },
    )
    
    naver_sources = collect_naver_sources(naver_queries)
    rss_sources = collect_rss_sources()
    merged_sources = merge_sources(naver_sources, rss_sources)

    write_json(run_dir / "sources_naver.json", naver_sources)
    write_json(run_dir / "sources_rss.json", rss_sources)
    write_json(run_dir / "sources_merged.json", merged_sources)
    (run_dir / "furiosa_docs_snapshot.md").write_text(
        furiosa_docs_snapshot,
        encoding="utf-8",
    )
    write_json(run_dir / "furiosa_docs_summary.json", furiosa_docs_summary)

    eval_result: dict[str, Any] | None = None
    raw_llm_text = ""
    llm_error: str | None = None

    dm_meta: dict[str, Any] = {
        "called": False,
        "count": 0,
        "error": "",
    }

    try:
        eval_result, raw_llm_text = evaluate_candidates_with_gemini(
            instructions=instructions,
            sources=merged_sources,
            furiosa_docs_summary=furiosa_docs_summary,
        )

        try:
            dm_meta["called"] = True
            (
                eval_result["candidates"],
                dm_records,
                dm_error,
            ) = enrich_candidates_with_profiles(
                eval_result.get("candidates", [])
            )
            dm_meta["count"] = sum(
                1
                for c in eval_result.get("candidates", [])
                if isinstance(c, dict)
                and c.get("decision_maker_profile_confidence") in ("HIGH", "MID", "LOW")
            )
            dm_meta["error"] = dm_error or ""
            write_json(
                run_dir / "decision_maker_profiles.json",
                {
                    "called": True,
                    "count": dm_meta["count"],
                    "error": dm_meta["error"],
                    "records": dm_records,
                },
            )
            print(
                f"Decision-maker discovery: count={dm_meta['count']} "
                f"error={dm_meta['error'] or 'none'}"
            )
        except Exception as exc_dm:
            dm_meta["error"] = str(exc_dm)
            print(f"Decision-maker discovery FAILED: {exc_dm}")
            write_json(
                run_dir / "decision_maker_profiles.json",
                {
                    "called": True,
                    "count": 0,
                    "error": dm_meta["error"],
                    "records": [],
                },
            )

        write_json(run_dir / "candidates.json", eval_result)
        write_candidates_csv(
            run_dir / "candidates.csv",
            eval_result.get("candidates", []),
        )
        (run_dir / "eval.md").write_text(
            build_eval_markdown(eval_result, raw_llm_text),
            encoding="utf-8",
        )

    except Exception as exc:
        llm_error = str(exc)
        print(f"LLM evaluation FAILED: {llm_error}")
        write_json(
            run_dir / "candidates.json",
            {
                "error": llm_error,
                "candidates": [],
                "eval_notes": ["LLM evaluation failed."],
            },
        )
        (run_dir / "eval.md").write_text(
            f"# LLM Evaluation Failed\n\n{llm_error}\n",
            encoding="utf-8",
        )

    write_report(
        run_dir=run_dir,
        run_id=run_id,
        mode=mode,
        memo=memo,
        naver_sources=naver_sources,
        rss_sources=rss_sources,
        merged_sources=merged_sources,
        furiosa_docs_summary=furiosa_docs_summary,
        eval_result=eval_result,
        llm_error=llm_error,
    )
    report_writer_meta = write_business_report(
        run_dir=run_dir,
        run_id=run_id,
        furiosa_docs_summary=furiosa_docs_summary,
        eval_result=eval_result,
    )

    write_metadata(
        run_dir=run_dir,
        run_id=run_id,
        mode=mode,
        memo=memo,
        naver_sources=naver_sources,
        rss_sources=rss_sources,
        merged_sources=merged_sources,
        furiosa_docs_summary=furiosa_docs_summary,
        eval_result=eval_result,
        llm_error=llm_error,
        report_writer_meta=report_writer_meta,
        decision_maker_meta=dm_meta,
    )
    update_index(run_id, mode, memo)

    print(f"Created run: {run_id}")
    print(f"Dynamic model queries: {len(dynamic_model_queries)}")
    print(f"Total Naver queries: {len(naver_queries)}")
    print(f"Naver sources recent 7d: {len(naver_sources)}")
    print(f"RSS sources recent 7d: {len(rss_sources)}")
    print(f"Merged sources recent 7d: {len(merged_sources)}")
    print(f"Furiosa docs successful: {furiosa_docs_summary.get('docs_successful')}")
    print(f"Furiosa docs failed: {furiosa_docs_summary.get('docs_failed')}")
    print(f"LLM called: {bool(eval_result)}")
    print(f"LLM error: {llm_error or ''}")
    print(f"Report: {run_dir / 'report.md'}")
    
if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(run_selftest())
    main()
