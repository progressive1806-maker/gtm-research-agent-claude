# gtm-research-agent

## GitHub Pages

`docs/index.html`은 가장 최신 `runs/test/<run_id>/gtm_report.md`를 보기 좋게 렌더링한 단일 페이지입니다. GitHub Actions 워크플로우가 실행될 때마다 `agent/build_pages.py`가 자동으로 다시 만들고, 같은 커밋에 포함되어 푸시됩니다.

수동으로 다시 만들고 싶으면:

```
python agent/build_pages.py
```

GitHub Pages는 `docs/index.html`을 서빙하도록 설정해 두세요(Settings → Pages → Source: `Deploy from a branch`, Branch: `main`, Folder: `/docs`). 페이지에는 후보 표·우선 연락 대상·B2G 안내와 함께 `runs/test/<run_id>/`의 주요 파일 링크가 함께 노출됩니다.
