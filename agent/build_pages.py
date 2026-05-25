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
PAGE_PATH = DOCS_DIR / "index.html"

LINKED_FILES = [
    "gtm_report.md",
    "report.md",
    "candidates.json",
    "metadata.json",
    "sources_merged.json",
]

METADATA_DISPLAY_FIELDS = [
    ("run_id", "run id"),
    ("executed_at_kst", "executed (KST)"),
    ("mode", "mode"),
    ("agent_version", "agent version"),
    ("llm_provider", "LLM provider"),
    ("llm_model", "LLM model"),
    ("merged_sources_recent_7d_count", "sources (7d)"),
    ("furiosa_docs_successful", "furiosa docs ok"),
    ("report_writer", "report writer"),
    ("report_writer_retry_count", "rewrite retries"),
    ("report_validation_passed", "validation passed"),
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
            out.append(f"<h3>{render_inline(stripped[4:])}</h3>")
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
            '<div><span class="k">remaining violation categories</span>'
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


PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{title}</title>
<style>
:root {{ color-scheme: light dark; }}
* {{ box-sizing: border-box; }}
body {{
  margin: 0;
  font: 16px/1.65 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
        "Apple SD Gothic Neo", "Noto Sans KR", "Malgun Gothic", sans-serif;
  color: #1c1f23;
  background: #f4f5f7;
}}
header.site {{ background: #1c1f23; color: #f4f5f7; padding: 28px 16px; }}
header.site .inner {{ max-width: 880px; margin: 0 auto; }}
header.site h1 {{ margin: 0 0 4px; font-size: 1.55em; font-weight: 700; letter-spacing: -0.01em; }}
header.site .sub {{ color: #b9bdc4; font-size: 0.95em; }}
.container {{ max-width: 880px; margin: 0 auto; padding: 20px 16px 80px; }}
.card {{
  background: #fff; border: 1px solid #e3e5e8; border-radius: 12px;
  padding: 20px 22px; margin: 16px 0;
  box-shadow: 0 1px 2px rgba(0,0,0,0.03);
}}
.card.tight {{ padding: 16px 18px; }}
.card h2 {{
  margin: 0 0 12px; font-size: 1.2em; color: #1c1f23;
  border-bottom: 1px solid #eef0f3; padding-bottom: 8px;
}}
.card h3 {{ margin: 18px 0 6px; font-size: 1.04em; color: #2a2f36; }}
.card p {{ margin: 8px 0; }}
.card ul {{ padding-left: 22px; margin: 8px 0; }}
.card li {{ margin: 4px 0; }}
.doc-title {{ margin: 0 0 6px; font-size: 1.3em; font-weight: 700; }}
a {{ color: #2563eb; text-decoration: none; }}
a:hover {{ text-decoration: underline; word-break: break-all; }}
code {{
  background: #f1f3f5; padding: 1px 6px; border-radius: 4px;
  font-size: 0.92em;
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
}}
pre code {{ display: block; padding: 12px 14px; background: #0f1115; color: #e5e7eb; overflow-x: auto; }}
hr {{ border: none; border-top: 1px solid #e3e5e8; margin: 20px 0; }}
.meta-strip {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 10px 18px; font-size: 0.93em;
}}
.meta-strip .k {{ display: block; color: #6b7280; font-size: 0.82em; text-transform: uppercase; letter-spacing: 0.04em; }}
.meta-strip .v {{ font-family: ui-monospace, SFMono-Regular, Menlo, monospace; word-break: break-all; }}
.files-list {{ display: flex; flex-wrap: wrap; gap: 8px; }}
.files-list a {{
  display: inline-block; padding: 5px 12px; background: #eef2ff;
  border-radius: 999px; font-size: 0.9em; color: #1d4ed8;
}}
.table-wrap {{ overflow-x: auto; margin: 8px 0; }}
table {{ border-collapse: collapse; width: 100%; font-size: 0.95em; }}
th, td {{ padding: 9px 11px; border-bottom: 1px solid #eef0f3; text-align: left; vertical-align: top; }}
th {{ background: #f8fafc; font-weight: 600; }}
tr:hover td {{ background: #fafbfc; }}
footer.site {{ text-align: center; color: #9aa0a8; font-size: 0.85em; padding: 24px 16px 40px; }}
@media (max-width: 600px) {{
  .container {{ padding: 14px 12px 60px; }}
  .card {{ padding: 16px; }}
  header.site {{ padding: 22px 14px; }}
}}
@media (prefers-color-scheme: dark) {{
  body {{ background: #15171b; color: #e5e7eb; }}
  header.site {{ background: #0f1115; }}
  .card {{ background: #1c1f24; border-color: #2a2f36; box-shadow: none; }}
  .card h2 {{ color: #e5e7eb; border-color: #2a2f36; }}
  .card h3 {{ color: #cbd0d8; }}
  .doc-title {{ color: #e5e7eb; }}
  a {{ color: #60a5fa; }}
  code {{ background: #2a2f36; color: #e5e7eb; }}
  table th {{ background: #1f242b; }}
  table th, table td {{ border-color: #2a2f36; }}
  tr:hover td {{ background: #20262d; }}
  .meta-strip .k {{ color: #9aa0a8; }}
  .files-list a {{ background: #1e293b; color: #c7d2fe; }}
}}
</style>
</head>
<body>
<header class="site">
  <div class="inner">
    <h1>FuriosaAI GTM Research</h1>
    <div class="sub">{subtitle}</div>
  </div>
</header>
<main class="container">
{intro_card}
{report_body}
</main>
<footer class="site">build_pages.py · GitHub Pages</footer>
</body>
</html>
"""


def build_intro_card(metadata: dict[str, Any], run_dir: Path | None) -> str:
    parts = ['<section class="card tight"><h2>Run summary</h2>']
    if metadata:
        parts.append(render_metadata_strip(metadata))
    if run_dir is not None:
        files_html = render_files_block(run_dir)
        if files_html:
            parts.append("<h3>Files for this run</h3>")
            parts.append(files_html)
    parts.append("</section>")
    return "\n".join(parts)


def build_empty_page() -> str:
    body = (
        '<section class="card"><h2>No run available yet</h2>'
        "<p>아직 <code>runs/test/</code> 디렉터리에 리포트가 생성되지 않았습니다. "
        "워크플로우를 한 번 실행하면 이 페이지가 최신 리포트로 채워집니다.</p>"
        "</section>"
    )
    return PAGE_TEMPLATE.format(
        title="FuriosaAI GTM Research",
        subtitle="아직 생성된 리포트가 없습니다.",
        intro_card="",
        report_body=body,
    )


def build_page(run_dir: Path) -> str:
    report_path = run_dir / "gtm_report.md"
    if not report_path.exists():
        return build_empty_page()

    md_text = report_path.read_text(encoding="utf-8")
    metadata: dict[str, Any] = {}
    metadata_path = run_dir / "metadata.json"
    if metadata_path.exists():
        try:
            metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            metadata = {}

    intro = build_intro_card(metadata, run_dir)
    body = render_markdown(md_text)

    executed = metadata.get("executed_at_kst") or run_dir.name
    subtitle = f"latest run · {html.escape(str(executed))}"

    return PAGE_TEMPLATE.format(
        title=f"FuriosaAI GTM Research · {html.escape(run_dir.name)}",
        subtitle=subtitle,
        intro_card=intro,
        report_body=body,
    )


def main() -> int:
    DOCS_DIR.mkdir(parents=True, exist_ok=True)

    run_dir = find_latest_run_dir("test")
    if run_dir is None:
        PAGE_PATH.write_text(build_empty_page(), encoding="utf-8")
        print("No runs/test/* found. Wrote placeholder docs/index.html.")
        return 0

    html_doc = build_page(run_dir)
    PAGE_PATH.write_text(html_doc, encoding="utf-8")
    print(f"Built {PAGE_PATH} from {run_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
