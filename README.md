# gtm-research-agent

## GitHub Pages

워크플로우가 실행될 때마다 `agent/build_pages.py`가 세 개의 정적 페이지를 다시 만들어 같은 커밋에 함께 푸시합니다.

- `docs/index.html` — 랜딩 페이지. 최신 `runs/test/<run_id>/`의 요약과 두 리포트로 가는 카드 링크.
- `docs/b2b.html` — B2B 전용 리포트(`runs/test/<run_id>/gtm_report_b2b.md` 렌더링). CSP 운영·CSP 고객·온프레미스 기업 중심이며 B2G/공공 후보는 제외.
- `docs/b2b-b2g.html` — B2B + B2G 통합 리포트(`runs/test/<run_id>/gtm_report_b2b_b2g.md` 렌더링). B2G 후보는 항상 “기사/RSS 기반 · 나라장터 확인: 미수행”으로 표시.

수동 재생성:

```
python agent/build_pages.py
```

GitHub Pages 설정: Settings → Pages → Source `Deploy from a branch`, Branch `main`, Folder `/docs`.

페이지는 외부 CSS/JS 없이 인라인 스타일만 사용하며, HIGH/MID/LOW · B2B/B2G · CSP 운영 기업 / CSP 고객 기업 / 온프레미스 기업 · 모델 매칭 상태(exact_supported/precompiled/planned/family_only/unknown)를 컬러 배지로 강조합니다.

## 리포트 파일

각 실행은 `runs/<mode>/<run_id>/`에 다음 세 개의 마크다운 리포트를 남깁니다.

- `gtm_report_b2b.md` — B2B 전용
- `gtm_report_b2b_b2g.md` — B2B + B2G 통합
- `gtm_report.md` — 두 리포트로 가는 간단한 랜딩(호환용)
