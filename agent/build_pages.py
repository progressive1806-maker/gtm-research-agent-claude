from __future__ import annotations

import html
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
RUNS_DIR = ROOT / "runs"
DOCS_DIR = ROOT / "docs"

INDEX_PATH = DOCS_DIR / "index.html"
B2B_PATH = DOCS_DIR / "b2b.html"
B2B_B2G_PATH = DOCS_DIR / "b2b-b2g.html"

LINKED_FILES = [
    "gtm_report.md",
    "gtm_report_b2b.md",
    "gtm_report_b2b_b2g.md",
    "report.md",
    "candidates.json",
    "metadata.json",
    "sources_merged.json",
    "decision_maker_profiles.json",
]

METADATA_DISPLAY_FIELDS = [
    ("run_id", "run id"),
    ("executed_at_kst", "executed (KST)"),
    ("mode", "mode"),
    ("agent_version", "agent version"),
    ("llm_provider", "LLM provider"),
    ("llm_model", "LLM model"),
    ("llm_retry_count", "LLM retries"),
    ("merged_sources_recent_7d_count", "sources (7d)"),
    ("furiosa_docs_successful", "furiosa docs ok"),
    ("report_writer", "report writer"),
    ("report_writer_retry_count", "rewrite retries"),
    ("report_validation_passed", "validation passed"),
    ("decision_maker_search_called", "DM search ran"),
    ("decision_maker_profiles_count", "DM profiles"),
]


def find_latest_run_dir(mode: str = "test") -> Path | None:
    base = RUNS_DIR / mode
    if not base.exists():
        return None
    dirs = [p for p in base.iterdir() if p.is_dir()]
    if not dirs:
        return None
    dirs.sort(key=lambda p: p.name, reverse=True)
    return dirs[0]


# -- Markdown rendering --------------------------------------------------

def render_inline(text: str) -> str:
    text = html.escape(text)
    text = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        lambda m: f'<a href="{m.group(2)}" target="_blank" rel="noopener">{m.group(1)}</a>',
        text,
    )
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*\s][^*]*?)\*(?!\*)", r"<em>\1</em>", text)
    return text


def render_table(table_lines: list[str]) -> str:
    pipe_sentinel = "\x00PIPE\x00"
    rows: list[list[str]] = []
    for raw in table_lines:
        line = raw.strip()
        if not line.startswith("|"):
            continue
        line = line.replace(r"\|", pipe_sentinel)
        line = line.strip("|").strip()
        cells = [c.strip().replace(pipe_sentinel, "|") for c in line.split("|")]
        rows.append(cells)

    if not rows:
        return ""

    def is_separator(cells: list[str]) -> bool:
        return all(re.fullmatch(r":?-{3,}:?", c) for c in cells if c)

    if len(rows) >= 2 and is_separator(rows[1]):
        header = rows[0]
        body = rows[2:]
    else:
        header = []
        body = rows

    parts = ['<div class="table-wrap"><table>']
    if header:
        parts.append(
            "<thead><tr>"
            + "".join(f"<th>{render_inline(c)}</th>" for c in header)
            + "</tr></thead>"
        )
    parts.append("<tbody>")
    col_count = max((len(header), *(len(r) for r in body)) or [0])
    for row in body:
        padded = row + [""] * (col_count - len(row))
        parts.append(
            "<tr>"
            + "".join(f"<td>{render_inline(c)}</td>" for c in padded)
            + "</tr>"
        )
    parts.append("</tbody></table></div>")
    return "".join(parts)


def render_markdown(md: str) -> str:
    lines = md.splitlines()
    out: list[str] = []
    in_section = False

    def close_section() -> None:
        nonlocal in_section
        if in_section:
            out.append("</section>")
            in_section = False

    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        if stripped.startswith("```"):
            code: list[str] = []
            i += 1
            while i < n and not lines[i].strip().startswith("```"):
                code.append(lines[i])
                i += 1
            if i < n:
                i += 1
            body = html.escape("\n".join(code))
            out.append(f"<pre><code>{body}</code></pre>")
            continue

        if stripped == "---":
            out.append("<hr/>")
            i += 1
            continue

        if stripped.startswith("# "):
            close_section()
            out.append(f'<h1 class="doc-title">{render_inline(stripped[2:])}</h1>')
            i += 1
            continue

        if stripped.startswith("## "):
            close_section()
            out.append(f'<section class="card"><h2>{render_inline(stripped[3:])}</h2>')
            in_section = True
            i += 1
            continue

        if stripped.startswith("### "):
            out.append(f'<h3 class="cand-name">{render_inline(stripped[4:])}</h3>')
            i += 1
            continue

        if line.lstrip().startswith("|"):
            tbl: list[str] = []
            while i < n and lines[i].lstrip().startswith("|"):
                tbl.append(lines[i])
                i += 1
            out.append(render_table(tbl))
            continue

        if stripped.startswith("- ") or stripped.startswith("* "):
            items: list[str] = []
            while i < n:
                ls = lines[i].lstrip()
                if not (ls.startswith("- ") or ls.startswith("* ")):
                    break
                items.append(f"<li>{render_inline(ls[2:])}</li>")
                i += 1
            out.append("<ul>" + "".join(items) + "</ul>")
            continue

        out.append(f"<p>{render_inline(stripped)}</p>")
        i += 1

    close_section()
    return "\n".join(out)


# -- Badge styling --------------------------------------------------------
# Tokens are wrapped in <span class="badge ..."> after HTML rendering. The
# walker skips content inside HTML tags so attributes/URLs are never touched.

BADGE_RULES: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"\bHIGH\b"), "badge badge-high"),
    (re.compile(r"\bMID\b"), "badge badge-mid"),
    (re.compile(r"\bLOW\b"), "badge badge-low"),
    (re.compile(r"\bWATCH\b"), "badge badge-low"),
    (re.compile(r"\bUNKNOWN\b"), "badge badge-unknown"),
    (re.compile(r"\bNONE\b"), "badge badge-unknown"),
    (re.compile(r"\bB2B\b"), "badge badge-b2b"),
    (re.compile(r"\bB2G\b"), "badge badge-b2g"),
    (re.compile(r"CSP 운영 기업"), "badge badge-csp-op"),
    (re.compile(r"CSP 고객 기업"), "badge badge-csp-cust"),
    (re.compile(r"온프레미스 기업"), "badge badge-onprem"),
    (re.compile(r"\bexact_supported\b"), "badge badge-model-exact"),
    (re.compile(r"\bprecompiled\b"), "badge badge-model-precompiled"),
    (re.compile(r"\bplanned\b"), "badge badge-model-planned"),
    (re.compile(r"\bfamily_only\b"), "badge badge-model-family"),
    (re.compile(r"(?<![A-Za-z_])unknown(?![A-Za-z_])"), "badge badge-model-unknown"),
]


def apply_badges(html_text: str) -> str:
    """Wrap badge tokens in plain-text segments; never touch HTML tag interiors."""
    parts = re.split(r"(<[^>]+>)", html_text)
    inside_pre = False
    for idx, part in enumerate(parts):
        if part.startswith("<"):
            tag = part.lower()
            if tag.startswith("<pre"):
                inside_pre = True
            elif tag.startswith("</pre"):
                inside_pre = False
            continue
        if inside_pre:
            continue
        new_part = part
        for pattern, css_class in BADGE_RULES:
            new_part = pattern.sub(
                lambda m, cls=css_class: f'<span class="{cls}">{m.group(0)}</span>',
                new_part,
            )
        parts[idx] = new_part
    return "".join(parts)


# -- Page components -----------------------------------------------------

def render_metadata_strip(metadata: dict[str, Any]) -> str:
    pairs: list[str] = []
    for key, label in METADATA_DISPLAY_FIELDS:
        if key not in metadata:
            continue
        value = metadata.get(key)
        if isinstance(value, bool):
            display = "yes" if value else "no"
        elif value is None or value == "":
            display = "—"
        else:
            display = str(value)
        pairs.append(
            f'<div><span class="k">{html.escape(label)}</span>'
            f'<span class="v">{html.escape(display)}</span></div>'
        )

    violations = metadata.get("report_validation_violations") or []
    if isinstance(violations, list) and violations:
        cats = sorted({str(v.get("category", "")) for v in violations if isinstance(v, dict)})
        pairs.append(
            '<div><span class="k">remaining violations</span>'
            f'<span class="v">{html.escape(", ".join(cats))}</span></div>'
        )

    if not pairs:
        return ""
    return '<div class="meta-strip">' + "".join(pairs) + "</div>"


def render_files_block(run_dir: Path) -> str:
    rel_base = f"../runs/{run_dir.parent.name}/{run_dir.name}"
    links: list[str] = []
    for name in LINKED_FILES:
        path = run_dir / name
        if not path.exists():
            continue
        href = f"{rel_base}/{name}"
        links.append(
            f'<a href="{html.escape(href)}">{html.escape(name)}</a>'
        )
    if not links:
        return ""
    return '<div class="files-list">' + "".join(links) + "</div>"


# -- Page template -------------------------------------------------------

CSS = """
:root { color-scheme: light dark; }
* { box-sizing: border-box; }
body {
  margin: 0;
  font: 16px/1.65 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
        "Apple SD Gothic Neo", "Noto Sans KR", "Malgun Gothic", sans-serif;
  color: #1c1f23; background: #f4f5f7;
}
header.site { background: #0f172a; color: #f4f5f7; padding: 26px 16px; }
header.site .inner { max-width: 980px; margin: 0 auto; }
header.site .crumb { color: #94a3b8; font-size: 0.85em; margin-bottom: 6px; }
header.site .crumb a { color: #cbd5e1; }
header.site h1 { margin: 0 0 4px; font-size: 1.55em; font-weight: 700; letter-spacing: -0.01em; }
header.site .sub { color: #94a3b8; font-size: 0.95em; }
.container { max-width: 980px; margin: 0 auto; padding: 20px 16px 80px; }
.card {
  background: #fff; border: 1px solid #e3e5e8; border-radius: 12px;
  padding: 20px 22px; margin: 16px 0;
  box-shadow: 0 1px 2px rgba(0,0,0,0.03);
}
.card.tight { padding: 16px 18px; }
.card h2 {
  margin: 0 0 12px; font-size: 1.2em; color: #1c1f23;
  border-bottom: 1px solid #eef0f3; padding-bottom: 8px;
}
.card h3.cand-name {
  margin: 18px 0 6px; font-size: 1.06em; color: #2a2f36;
  display: inline-block; padding: 4px 10px;
  background: #f1f5f9; border-radius: 8px;
}
.card p { margin: 8px 0; }
.card ul { padding-left: 22px; margin: 8px 0; }
.card li { margin: 4px 0; }
.doc-title { margin: 0 0 6px; font-size: 1.3em; font-weight: 700; }
a { color: #2563eb; text-decoration: none; word-break: break-all; }
a:hover { text-decoration: underline; }
code {
  background: #f1f3f5; padding: 1px 6px; border-radius: 4px;
  font-size: 0.92em;
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
}
pre code { display: block; padding: 12px 14px; background: #0f1115; color: #e5e7eb; overflow-x: auto; }
hr { border: none; border-top: 1px solid #e3e5e8; margin: 20px 0; }
.meta-strip {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 10px 18px; font-size: 0.93em;
}
.meta-strip .k { display: block; color: #64748b; font-size: 0.78em; text-transform: uppercase; letter-spacing: 0.04em; }
.meta-strip .v { font-family: ui-monospace, SFMono-Regular, Menlo, monospace; word-break: break-all; }
.files-list { display: flex; flex-wrap: wrap; gap: 8px; }
.files-list a {
  display: inline-block; padding: 5px 12px; background: #eef2ff;
  border-radius: 999px; font-size: 0.9em; color: #1d4ed8;
}
.table-wrap { overflow-x: auto; margin: 8px 0; border: 1px solid #eef0f3; border-radius: 8px; }
table { border-collapse: collapse; width: 100%; font-size: 0.94em; }
th, td { padding: 9px 11px; border-bottom: 1px solid #eef0f3; text-align: left; vertical-align: top; }
th { background: #f8fafc; font-weight: 600; color: #334155; }
tr:hover td { background: #fafbfc; }

/* Landing tiles */
.scope-tiles {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 14px;
  margin-top: 10px;
}
.scope-tile {
  display: block; text-decoration: none; color: inherit;
  background: linear-gradient(135deg, #1e3a8a, #2563eb);
  border-radius: 14px; padding: 22px 22px; min-height: 130px;
  color: #f8fafc; box-shadow: 0 2px 6px rgba(15,23,42,0.12);
  transition: transform 0.1s ease;
}
.scope-tile:hover { transform: translateY(-1px); text-decoration: none; }
.scope-tile.b2b { background: linear-gradient(135deg, #1e3a8a, #2563eb); }
.scope-tile.b2b-b2g { background: linear-gradient(135deg, #6d28d9, #9333ea); }
.scope-tile .name { font-size: 1.15em; font-weight: 700; margin-bottom: 4px; }
.scope-tile .desc { font-size: 0.94em; opacity: 0.92; }
.scope-tile .arrow { float: right; font-size: 1.4em; opacity: 0.85; }

/* Badges */
.badge {
  display: inline-block;
  padding: 1px 8px;
  border-radius: 999px;
  font-size: 0.82em;
  font-weight: 600;
  margin: 0 1px;
  letter-spacing: 0.01em;
  vertical-align: middle;
  line-height: 1.5;
  white-space: nowrap;
}
.badge-high { background: #fee2e2; color: #b91c1c; }
.badge-mid { background: #fef3c7; color: #92400e; }
.badge-low { background: #e5e7eb; color: #374151; }
.badge-unknown { background: #f3f4f6; color: #6b7280; }
.badge-b2b { background: #dbeafe; color: #1e40af; }
.badge-b2g { background: #ede9fe; color: #6d28d9; }
.badge-csp-op { background: #e0e7ff; color: #3730a3; }
.badge-csp-cust { background: #cffafe; color: #155e75; }
.badge-onprem { background: #d1fae5; color: #065f46; }
.badge-model-exact { background: #d1fae5; color: #065f46; }
.badge-model-precompiled { background: #dbeafe; color: #1e40af; }
.badge-model-planned { background: #fef3c7; color: #92400e; }
.badge-model-family { background: #f3f4f6; color: #6b7280; }
.badge-model-unknown { background: #f3f4f6; color: #6b7280; }

footer.site { text-align: center; color: #94a3b8; font-size: 0.85em; padding: 24px 16px 40px; }

@media (max-width: 600px) {
  .container { padding: 14px 12px 60px; }
  .card { padding: 16px; }
  header.site { padding: 22px 14px; }
  .scope-tile { padding: 18px; min-height: 110px; }
}

@media (prefers-color-scheme: dark) {
  body { background: #0b0d11; color: #e5e7eb; }
  header.site { background: #06080c; }
  .card { background: #161a21; border-color: #232831; box-shadow: none; }
  .card h2 { color: #e5e7eb; border-color: #232831; }
  .card h3.cand-name { color: #cbd0d8; background: #1d232c; }
  .doc-title { color: #e5e7eb; }
  a { color: #60a5fa; }
  code { background: #232831; color: #e5e7eb; }
  .table-wrap { border-color: #232831; }
  table th { background: #1c222b; color: #cbd5e1; }
  table th, table td { border-color: #232831; }
  tr:hover td { background: #1c222b; }
  .meta-strip .k { color: #94a3b8; }
  .files-list a { background: #1e293b; color: #c7d2fe; }
  .badge-high { background: #7f1d1d; color: #fecaca; }
  .badge-mid { background: #78350f; color: #fde68a; }
  .badge-low { background: #374151; color: #d1d5db; }
  .badge-unknown { background: #1f242b; color: #9ca3af; }
  .badge-b2b { background: #1e3a8a; color: #bfdbfe; }
  .badge-b2g { background: #4c1d95; color: #ddd6fe; }
  .badge-csp-op { background: #312e81; color: #c7d2fe; }
  .badge-csp-cust { background: #164e63; color: #a5f3fc; }
  .badge-onprem { background: #065f46; color: #a7f3d0; }
  .badge-model-exact { background: #065f46; color: #a7f3d0; }
  .badge-model-precompiled { background: #1e3a8a; color: #bfdbfe; }
  .badge-model-planned { background: #78350f; color: #fde68a; }
  .badge-model-family { background: #1f242b; color: #9ca3af; }
  .badge-model-unknown { background: #1f242b; color: #9ca3af; }
}
"""


def page_shell(title: str, crumb_html: str, subtitle: str, body_html: str) -> str:
    return (
        "<!DOCTYPE html>\n"
        "<html lang=\"ko\">\n"
        "<head>\n"
        "<meta charset=\"utf-8\" />\n"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />\n"
        f"<title>{title}</title>\n"
        f"<style>{CSS}</style>\n"
        "</head>\n"
        "<body>\n"
        "<header class=\"site\">\n"
        "  <div class=\"inner\">\n"
        f"    {crumb_html}\n"
        "    <h1>FuriosaAI GTM Research</h1>\n"
        f"    <div class=\"sub\">{subtitle}</div>\n"
        "  </div>\n"
        "</header>\n"
        "<main class=\"container\">\n"
        f"{body_html}\n"
        "</main>\n"
        "<footer class=\"site\">build_pages.py · GitHub Pages</footer>\n"
        "</body>\n"
        "</html>\n"
    )


# -- Page builders -------------------------------------------------------

def _read_metadata(run_dir: Path) -> dict[str, Any]:
    path = run_dir / "metadata.json"
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def build_landing_page(run_dir: Path | None) -> str:
    if run_dir is None:
        body = (
            '<section class="card"><h2>아직 실행 결과가 없습니다</h2>'
            "<p><code>runs/test/</code> 디렉터리에 결과가 생성되면 이 페이지가 자동으로 채워집니다.</p>"
            "</section>"
        )
        return page_shell(
            "FuriosaAI GTM Research",
            "",
            "아직 생성된 리포트가 없습니다.",
            body,
        )

    metadata = _read_metadata(run_dir)
    executed = metadata.get("executed_at_kst") or run_dir.name
    subtitle = f"latest run · {html.escape(str(executed))}"

    summary_card = (
        '<section class="card tight"><h2>Run summary</h2>'
        + render_metadata_strip(metadata)
        + "<h3>Files for this run</h3>"
        + (render_files_block(run_dir) or "<p>—</p>")
        + "</section>"
    )

    tiles = (
        '<section class="card"><h2>리포트 보기</h2>'
        '<div class="scope-tiles">'
        '<a class="scope-tile b2b" href="b2b.html">'
        '<span class="arrow">›</span>'
        '<div class="name">B2B 전용 리포트</div>'
        '<div class="desc">CSP 운영·CSP 고객·온프레미스 기업 중심. 공공/B2G 후보는 제외됩니다.</div>'
        '</a>'
        '<a class="scope-tile b2b-b2g" href="b2b-b2g.html">'
        '<span class="arrow">›</span>'
        '<div class="name">B2B + B2G 통합 리포트</div>'
        '<div class="desc">B2B 후보 + B2G(기사/RSS 기반, 나라장터 확인 미수행) 후보를 함께 표기합니다.</div>'
        '</a>'
        '</div></section>'
    )

    body = summary_card + tiles
    return page_shell(
        f"FuriosaAI GTM Research · {html.escape(run_dir.name)}",
        "",
        subtitle,
        body,
    )


def build_report_page(
    run_dir: Path | None,
    source_md: str,
    title_suffix: str,
    subtitle_label: str,
) -> str:
    if run_dir is None:
        body = (
            '<section class="card"><h2>아직 실행 결과가 없습니다</h2>'
            "<p>워크플로우가 한 번 실행되면 이 페이지가 자동으로 채워집니다.</p>"
            "</section>"
        )
        return page_shell(
            f"FuriosaAI GTM Research · {html.escape(title_suffix)}",
            '<div class="crumb"><a href="index.html">← 인덱스</a></div>',
            "아직 생성된 리포트가 없습니다.",
            body,
        )

    metadata = _read_metadata(run_dir)
    md_path = run_dir / source_md

    crumb_html = '<div class="crumb"><a href="index.html">← 인덱스</a></div>'
    executed = metadata.get("executed_at_kst") or run_dir.name
    subtitle = f"{subtitle_label} · {html.escape(str(executed))}"

    intro = (
        '<section class="card tight"><h2>Run summary</h2>'
        + render_metadata_strip(metadata)
        + "<h3>Files for this run</h3>"
        + (render_files_block(run_dir) or "<p>—</p>")
        + "</section>"
    )

    if not md_path.exists():
        report_html = (
            '<section class="card"><h2>리포트 파일이 없습니다</h2>'
            f"<p><code>{source_md}</code>를 찾을 수 없습니다. 다음 실행 후 다시 확인해 주세요.</p>"
            "</section>"
        )
    else:
        md_text = md_path.read_text(encoding="utf-8")
        report_html = apply_badges(render_markdown(md_text))

    return page_shell(
        f"FuriosaAI GTM Research · {html.escape(title_suffix)}",
        crumb_html,
        subtitle,
        intro + report_html,
    )


def main() -> int:
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    run_dir = find_latest_run_dir("test")

    INDEX_PATH.write_text(build_landing_page(run_dir), encoding="utf-8")
    B2B_PATH.write_text(
        build_report_page(run_dir, "gtm_report_b2b.md", "B2B", "B2B 전용 리포트"),
        encoding="utf-8",
    )
    B2B_B2G_PATH.write_text(
        build_report_page(run_dir, "gtm_report_b2b_b2g.md", "B2B + B2G", "B2B + B2G 통합 리포트"),
        encoding="utf-8",
    )

    if run_dir is None:
        print("No runs/test/* found. Wrote placeholder pages.")
    else:
        print(f"Built {INDEX_PATH.name}, {B2B_PATH.name}, {B2B_B2G_PATH.name} from {run_dir.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
