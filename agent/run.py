from __future__ import annotations

import csv
import html
import json
import os
import re
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


ROOT = Path(__file__).resolve().parents[1]
RUNS_DIR = ROOT / "runs"
DOCS_DIR = ROOT / "docs"
PROMPT_PATH = ROOT / "prompts" / "gtm_agent_instructions.md"

NAVER_NEWS_URL = "https://openapi.naver.com/v1/search/news.json"


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
- Do not generate numeric claims unless the number appears explicitly in the provided sources or Furiosa docs summary.
- This includes percentages, multipliers, cost reduction, power consumption, GPU counts, server counts, budgets, MW, timelines, performance claims, server counts, data center capacity, and procurement amounts.
- If the source does not provide a number, write qualitative language only.
- Do not write "2배", "60% 절감", "반값", "75W", "최고", "압도적", "24시간", "수백", "수천", "대규모", "대폭", "크게 절감", "MW", "억원", "장", "대" unless directly supported by source text.
- Every numeric claim in buying_signal, infrastructure_signal, customer_win, furiosa_win, contact_reason, outreach_talk_track, or timing_reason must also appear in numeric_claims with source_id and evidence_text.
- If numeric_claims is empty, do not include numeric-looking expressions in candidate narrative, including "24시간", "수백", "수천", "%", "MW", "억원", "장", "대", "배", "반값", "절감률", "전력량", or "서버 수".
- If the evidence text only supports a customer's announced number, do not convert it into an RNGD performance claim.
- Dates from source metadata may be used without numeric_claims, but do not turn dates into performance, budget, or sales claims.


Anti-hype hard rules:
- Do not use the following words or close variants in Korean narrative: "완벽", "획기", "독보", "극적", "대대적", "압도", "최고", "최상", "최정상", "막강", "엄청난", "탁월", "보장", "장악", "선점", "돌파".
- Replace hype language with conservative terms such as "검토 가능", "개선 가능성", "확인 필요", "논의 가치", "구조 확인 필요", "우선 검토 후보".
- Do not write that RNGD will reduce cost, power, rack space, latency, server count, or budget unless the provided source or Furiosa docs explicitly supports that exact claim.
- If the evidence is indirect, use "가능성", "확인 필요", or "구조 확인 필요".
- In outreach_talk_track, use a calm BD tone. Do not use promotional copy.

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


HYPE_REPLACEMENTS = {
    "완벽한": "검토 가치가 있는",
    "완벽히": "보수적으로 검토 가능한",
    "완벽하게": "보수적으로 검토 가능한 수준으로",
    "획기적으로": "개선 가능성이 있는 방향으로",
    "획기적인": "개선 가능성이 있는",
    "독보적": "중요한",
    "극적으로": "유의미하게",
    "대대적인": "상당한",
    "대대적으로": "상당한 수준으로",
    "압도적": "강한",
    "최고 수준": "높은 수준",
    "최상위": "우선 검토",
    "최정상급": "우선 검토 가능한",
    "막강한": "중요한",
    "엄청난": "큰",
    "탁월하게": "개선 가능성이 있게",
    "탁월한": "검토 가치가 있는",
    "보장된": "확인 필요한",
    "보장하는": "확인 필요한",
    "장악": "진입",
    "선점": "확보 가능성",
    "돌파": "완화 가능성 검토",
    "저에너지 고출력": "전력 효율 개선 가능성이 있는",
    "초저전력": "전력 효율 개선 가능성이 있는",
    "가성비": "비용 효율",
    "무수히 많은": "다수의",
    "최적의": "검토 가능한",
    "최적화된": "검토 가능한",
    "최적화": "개선 가능성 검토",
    "최소화": "완화 가능성 검토",
    "저비용": "비용 효율 개선 가능성이 있는",
    "고효율": "효율 개선 가능성이 있는",
    "신뢰성 높은": "안정성 확인이 필요한",
    "실시간 추론": "추론 처리",
    "수주율 개선": "제안 경쟁력 개선 가능성",
    "매력적인": "검토 가능한",
    "연쇄적으로 공급": "확대 공급 가능성 검토",
    "대규모 납품": "공급 가능성 검토",
    "과감히": "보수적으로",
    "핵심적인 방향타": "중요한 참고 신호",
    "확보 가능성해야": "확보할 수 있는지 검토해야",
    "저전력 효율 개선 가능성이 있는": "전력 효율 개선 가능성을 검토할 수 있는",
    "효율 개선 가능성이 있는로": "효율 개선 가능성을 검토하며",
    "비용 효율성이 확인된": "비용 구조를 검토할 수 있는",
    "국산 고성능 가속기": "국산 가속기",
    "시너지를 극대화": "협력 가능성을 검토",
    "상당한 규모의 가속기": "가속기",
    "안정적인 호환이 검증된": "호환성 검토가 필요한",
    "수익성을 추가 제고": "수익성 개선 가능성을 검토",
    "공급 레퍼런스를 공고히": "공급 레퍼런스 가능성을 검토",
    "경쟁력을 증명": "경쟁력 검토 근거를 마련",
    "실적을 단기에 축적": "실적 확보 가능성을 검토",
    "상징성 높은 활용 사례를 획득": "공공 활용 사례 가능성을 검토",
    "대표적인 AI 통합 플랫폼 레퍼런스를 확보": "AI 통합 플랫폼 레퍼런스 가능성을 검토",
    "확실한 표적 기회": "구조 확인 가치가 있는 후보",
    "명확한 기회": "구조 확인 가치가 있는 후보",
    "명확합니다": "검토할 수 있습니다",
    "충분합니다": "확인할 필요가 있습니다",
    "용이해집니다": "용이해질 수 있습니다",
    "달성합니다": "검토할 수 있습니다",
    "입증됩니다": "확인할 필요가 있습니다",
    "기본 연동": "연동 검토",
    "수주하여": "수주 가능성을 검토하여",
    "획득할 수 있습니다": "검토할 수 있습니다",
    "확보하여": "확보 가능성을 검토하여",
    "고성능": "성능 검토가 필요한",
    "저전력": "전력 효율 검토가 필요한",
}

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

SUMMARY_FIELDS = [
    "overall_assessment",
    "noise_ratio_comment",
    "model_compatibility_caution",
]


def sanitize_hype_text(value: Any) -> Any:
    if not isinstance(value, str):
        return value

    text = value
    for bad, replacement in HYPE_REPLACEMENTS.items():
        text = text.replace(bad, replacement)

    # clean_conservative_text is defined below; it exists by runtime before this function is called.
    if "clean_conservative_text" in globals():
        text = clean_conservative_text(text)

    return text


def remove_unsupported_numeric_phrases(value: Any, numeric_claims: Any) -> Any:
    if not isinstance(value, str):
        return value

    if isinstance(numeric_claims, list) and numeric_claims:
        return value

    text = value

    # numeric_claims가 비어 있으면 숫자성 영업 표현을 보수적으로 치환
    text = re.sub(r"\d+(?:\.\d+)?\s*(?:MW|억원|장|대|배|%)", "수치 근거 미확인", text)
    text = text.replace("24시간", "상시")
    text = text.replace("수백", "다수")
    text = text.replace("수천", "다수")
    text = text.replace("대규모", "상당한 규모의")
    text = text.replace("대폭", "일부")
    text = text.replace("크게 절감", "개선 가능성 검토")
    text = text.replace("반값", "비용 구조 확인 필요")

    risky_phrases = {
        "전력 비용 부담을 최소화": "전력 비용 구조를 확인할 필요가 있음",
        "전력 부담을 낮추고": "전력 부담 완화 가능성을 검토하고",
        "공간 밀도를 향상시킬 수 있는": "공간 밀도 개선 가능성을 검토할 수 있는",
        "비용 격차 개선 가능성": "비용 구조 확인 필요",
        "장비 비용과 전력 부담을 낮추는": "장비 비용과 전력 부담 완화 가능성을 검토하는",
        "운영 효율성을 제공": "운영 효율 개선 가능성을 검토",
        "운영 원가를 절감": "운영 원가 구조를 확인",
        "비용 절감": "비용 구조 확인",
        "원가를 절감": "원가 구조를 확인",
        "성능을 유지하고": "성능 유지 가능성을 확인하고",
        "가속 성능 점검": "가속 가능성 점검",
        "효율성을 확보": "효율 개선 가능성을 검토",
        "효율성을 제고": "효율 개선 가능성을 검토",
        "전력 효율성을 개선": "전력 효율 개선 가능성을 검토",
        "상면 부담을 경감": "상면 부담 완화 가능성을 검토",
        "트래픽 부하를 감소": "트래픽 부하 완화 가능성을 검토",
        "추론 병목 대응": "추론 병목 가능성 확인",
        "연산 비용을 개선": "연산 비용 구조를 확인",
        "전력 제약 내 가용 연산 밀도를 극대화": "전력 제약 내 연산 밀도 개선 가능성을 검토",
        "고밀도 추론 환경을 안정적으로 설계": "고밀도 추론 환경의 설계 가능성을 확인",
        "전력 소모 한계를 제어": "전력 소모 구조를 확인",
        "비용 부담을 줄일 수 있는": "비용 구조를 검토할 수 있는",
        "하드웨어 비용 부담을 줄일 수 있는": "하드웨어 비용 구조를 검토할 수 있는",
        "서버 구축 단가를 절감할 수 있는": "서버 구축 단가 구조를 검토할 수 있는",
        "유지비 부담을 경감할": "유지비 구조를 검토할",
        "전력 비용 부담을 최소화": "전력 비용 구조를 확인",
        "전력 소모량 부담을 완화": "전력 소모량 구조를 확인",
        "전력 효율성을 개선": "전력 효율 개선 가능성을 검토",
        "총판 경쟁 요소를 더하고": "총판 경쟁 요소를 검토하고",
        "사업 성공률을 높일 수 있습니다": "사업 구조를 개선할 수 있는지 확인할 필요가 있습니다",
        "수익성을 추가 제고": "수익성 개선 가능성을 검토",
        "비용 대비 효율 개선": "비용 대비 효율 구조 검토",
        "비용 저감": "비용 구조 검토",
        "비용 절감": "비용 구조 검토",
        "단가 확보": "단가 구조 확인",
        "단가 편차 극복": "단가 구조 확인",
        "가격 경쟁력": "가격 구조",
        "전력 소모량 부담": "전력 소모량 구조",
        "하드웨어 운영 부담을 완화": "하드웨어 운영 구조를 검토",
        "예산 대비 성능 제고": "예산 대비 성능 구조 검토",
        "성능 제고": "성능 구조 검토",
        "인프라 비용 개선": "인프라 비용 구조 검토",
        "서버 개선 가능성": "서버 구조 검토",
        "운영 개선 가능성": "운영 구조 검토",
        "개선 가능성 검토 성능": "개선 가능성 검토",
    }

    for bad, replacement in risky_phrases.items():
        text = text.replace(bad, replacement)

    text = clean_conservative_text(text)

    return text


def clean_conservative_text(value: Any) -> Any:
    if not isinstance(value, str):
        return value

    text = value
    cleanup_replacements = {
        "가능성 가능성": "가능성",
        "가능성 검토 가능성": "가능성 검토",
        "확보 가능성해야": "확보할 수 있는지 검토해야",
        "효율 개선 가능성이 있는로": "효율 개선 가능성을 검토하며",
        "전력 효율 검토가 필요한 효율": "전력 효율",
        "전력 효율 검토가 필요한 기반": "전력 효율 검토 기반",
        "성능 검토가 필요한 가속기": "가속기",
        "전력 효율 검토가 필요한 가속기": "전력 효율 개선 가능성을 검토할 수 있는 가속기",
        "전력 효율 검토가 필요한 하드웨어": "전력 효율 개선 가능성을 검토할 수 있는 하드웨어",
        "비용 구조 확인성이": "비용 구조가",
        "검의": "검토",
        "가입 조율": "편입 가능성",
        "가속화할 기회": "확대 가능성을 검토할 기회",
        "손쉽게 창출": "확대 가능성을 검토",
        "대리 창출": "간접적으로 발굴",
        "가벼운 AI": "경량 AI",
        "정합 가능하게": "정합성을 확인하며",
        "제고할 방안": "검토할 방안",
        "저전력 기반": "전력 효율 개선 가능성 기반",
        "저전력 하드웨어": "전력 효율 개선 가능성을 검토할 수 있는 하드웨어",
    }
    for bad, replacement in cleanup_replacements.items():
        text = text.replace(bad, replacement)

    text = re.sub(r"\s+", " ", text).strip()
    return text


def enforce_candidate_fit_rules(candidate: dict[str, Any]) -> dict[str, Any]:
    model_status = str(candidate.get("model_match_status", "")).lower()
    confirmed_model = str(candidate.get("confirmed_model_name", "")).strip()
    target_type = str(candidate.get("target_type", ""))
    deployment_fit = str(candidate.get("deployment_fit_score", ""))
    channel_fit = str(candidate.get("channel_fit_score", ""))

    if confirmed_model in ["", "미확인"] or model_status == "unknown":
        candidate["model_fit_score"] = "UNKNOWN"

        # 모델 미확인 CSP/operator는 outreach는 HIGH 가능하지만 rngd fit은 MID로 보수화
        if target_type == "CSP 운영 기업" and deployment_fit == "HIGH" and channel_fit == "HIGH":
            candidate["rngd_fit_score"] = "MID"
            if candidate.get("outreach_priority") == "HIGH":
                candidate["fit_vs_priority_explanation"] = (
                    "모델명은 미확인이나, CSP/인프라/채널 관점의 논의 가치가 높아 "
                    "outreach priority는 HIGH로 유지한다. 모델 적합성은 UNKNOWN으로 보수 판단한다."
                )
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
    candidate.setdefault("decision_maker_profile_url", "미확인 — v0.6 담당자 검색 필요")

    if candidate.get("market") == "B2G":
        candidate.setdefault("b2g_evidence_type", "기사/RSS 기반")
        candidate.setdefault("g2b_checked", "미수행")
        candidate.setdefault("procurement_next_action", "나라장터/RFP 직접 확인 필요")

    return candidate


def postprocess_eval_result(result: dict[str, Any]) -> dict[str, Any]:
    run_summary = result.get("run_summary", {})
    if isinstance(run_summary, dict):
        for field in SUMMARY_FIELDS:
            value = run_summary.get(field, "")
            value = sanitize_hype_text(value)
            value = remove_unsupported_numeric_phrases(value, [])
            run_summary[field] = value
        result["run_summary"] = run_summary

    eval_notes = result.get("eval_notes", [])
    if isinstance(eval_notes, list):
        result["eval_notes"] = [
            remove_unsupported_numeric_phrases(
                sanitize_hype_text(note),
                [],
            )
            if isinstance(note, str)
            else note
            for note in eval_notes
        ]

    candidates = result.get("candidates", [])
    if isinstance(candidates, list):
        cleaned_candidates = []

        for candidate in candidates:
            if not isinstance(candidate, dict):
                continue

            candidate = enforce_candidate_fit_rules(candidate)
            candidate = enrich_candidate_defaults(candidate)

            numeric_claims = candidate.get("numeric_claims", [])

            for field in NARRATIVE_FIELDS:
                value = candidate.get(field, "")
                value = sanitize_hype_text(value)
                value = remove_unsupported_numeric_phrases(value, numeric_claims)
                candidate[field] = value

            cleaned_candidates.append(candidate)

        result["candidates"] = cleaned_candidates

    return result
    

def evaluate_candidates_with_gemini(
    instructions: str,
    sources: list[dict[str, Any]],
    furiosa_docs_summary: dict[str, Any],
) -> tuple[dict[str, Any], str]:
    api_key = os.getenv("GEMINI_API_KEY", "")
    model = os.getenv("LLM_MODEL", "gemini-3.5-flash")

    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY is missing. Add it in GitHub Settings > Secrets and variables > Actions."
        )

    llm_sources = build_llm_payload_sources(choose_llm_sources(sources))
    prompt = build_llm_prompt(
        instructions=instructions,
        llm_sources=llm_sources,
        furiosa_docs_summary=furiosa_docs_summary,
    )

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model=model,
        contents=prompt,
    )

    raw_text = response.text or ""
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
) -> str:
    if not eval_result:
        return "# FuriosaAI GTM 리서치\n\nLLM 평가 실패로 실전용 리포트를 생성하지 못했습니다.\n"

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
            "| 대상 | 담당자 힌트 | 공개 프로필 URL | 기존 접점 |",
            "|---|---|---|---|",
        ]
    )

    for c in candidates_sorted[:8]:
        lines.append(
            f"| {c.get('name', '미확인')} "
            f"| {short_text(c.get('decision_maker_hint'), 80)} "
            f"| {c.get('decision_maker_profile_url', '미확인 — v0.6 담당자 검색 필요')} "
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
            "- 공개 프로필 URL은 아직 자동 검색하지 않았습니다. v0.6에서 담당자/LinkedIn 또는 공식 프로필 탐색을 추가해야 합니다.",
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

def write_business_report(
    run_dir: Path,
    run_id: str,
    furiosa_docs_summary: dict[str, Any],
    eval_result: dict[str, Any] | None,
) -> None:
    business_report = build_business_report(
        run_id=run_id,
        eval_result=eval_result,
        furiosa_docs_summary=furiosa_docs_summary,
    )
    (run_dir / "gtm_report.md").write_text(business_report, encoding="utf-8")

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
- agent_version: `v0.5`
- instructions_loaded_chars: `{instruction_chars}`
- naver_sources_recent_7d_count: `{len(naver_sources)}`
- rss_sources_recent_7d_count: `{len(rss_sources)}`
- merged_sources_recent_7d_count: `{len(merged_sources)}`
- furiosa_docs_successful: `{furiosa_docs_summary.get("docs_successful")}`
- furiosa_docs_failed: `{furiosa_docs_summary.get("docs_failed")}`
- llm_called: `{bool(eval_result)}`
- llm_error: `{llm_error or ""}`

## 현재 단계

이 실행은 v0.5 테스트입니다.

이번 버전에서는 네이버 뉴스 API, RSS feed, FuriosaAI 공개 개발자 문서를 수집한 뒤 Gemini로 GTM 후보를 1차 평가합니다.

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
) -> None:
    metadata = {
        "run_id": run_id,
        "mode": mode,
        "memo": memo or "",
        "executed_at_kst": now_kst().isoformat(),
        "agent_version": "v0.5",
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
        "max_llm_sources": MAX_LLM_SOURCES,
        "max_source_chars": MAX_SOURCE_CHARS,
        "max_output_candidates": MAX_OUTPUT_CANDIDATES,
        "g2b_called": False,
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
        f"— [gtm_report](../runs/{mode}/{run_id}/gtm_report.md) "
        f"/ [debug_report](../runs/{mode}/{run_id}/report.md) "
        f"/ [candidates](../runs/{mode}/{run_id}/candidates.json) "
        f"/ [merged_sources](../runs/{mode}/{run_id}/sources_merged.json) "
        f"/ [furiosa_docs](../runs/{mode}/{run_id}/furiosa_docs_snapshot.md)\n"
    )

    existing = existing.rstrip() + "\n" + link
    index_path.write_text(existing, encoding="utf-8")


def main() -> None:
    mode = os.getenv("RUN_MODE", "test")
    memo = os.getenv("RUN_MEMO", "manual-test")

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

    try:
        eval_result, raw_llm_text = evaluate_candidates_with_gemini(
            instructions=instructions,
            sources=merged_sources,
            furiosa_docs_summary=furiosa_docs_summary,
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
    write_business_report(
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
    main()
