# FuriosaAI GTM Research Agent Test Run

## 실행 정보

- run_id: `2026-05-25_220626_test_v0.6.2-pages-test`
- mode: `test`
- memo: `v0.6.2-pages-test`
- executed_at_kst: `2026-05-25T22:13:13.631109+09:00`
- agent_version: `v0.6`
- instructions_loaded_chars: `21592`
- naver_sources_recent_7d_count: `216`
- rss_sources_recent_7d_count: `95`
- merged_sources_recent_7d_count: `311`
- furiosa_docs_successful: `11`
- furiosa_docs_failed: `0`
- llm_called: `True`
- llm_error: ``

## 현재 단계

이 실행은 v0.6 테스트입니다.

이번 버전에서는 네이버 뉴스 API, RSS feed, FuriosaAI 공개 개발자 문서를 수집한 뒤 Gemini로 GTM 후보를 1차 평가하고, 별도 LLM 호출로 매니저용 gtm_report.md를 작성합니다.

아직 나라장터 직접 API, 담당자 심화 탐색, Notion 업로드는 수행하지 않았습니다.

## LLM 실행 요약

- overall_assessment: 삼성SDS의 대규모 AI 데이터센터 인프라 투자 및 우리은행 AI 에이전트 수주, 한글과컴퓨터와 LG AI연구원의 공공 AX 시장 공동 대응이 이번 주 핵심 비즈니스 시그널입니다. 모델명이 불명확하더라도 대형 인프라 증설 및 조달/채널 경로가 명확한 CSP 운영사 및 공공 파트너를 집중 타깃으로 설정하여 클라우드 연계 및 온프레미스 패키지 제안을 추진해야 합니다.
- top_priority_names: 삼성SDS, 엘리스그룹, 한글과컴퓨터, 우리은행
- noise_ratio_comment: 중국 시장의 알리바바 신형 가속기 발표 및 삼성전자의 사내 생성형 AI 허용 정책 등 단순 정책 및 동향성 기사는 직접적인 가속기 GTM 액션과 연관이 없어 노이즈로 처리했습니다.
- model_compatibility_caution: 농협은행의 엑사원 3.5 및 한글과컴퓨터의 엑사원 모델군은 당사 공식 지원 사양인 엑사원 4.0과 버전 차이가 있으므로 패밀리 단위의 정밀 기술 검증이 요구되며, 에코아이티의 Solar LLM 적용 플랫폼은 vLLM 호환성을 확인해야 합니다.

## LLM 후보 평가 결과

## 버전 1 — B2B only 우선 검토 요약

- 삼성SDS / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `중기`
- 엘리스그룹 / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- 우리은행 / CSP 고객 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `중기`
- NHN클라우드 / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `중기`
- 에코아이티 / CSP 고객 기업 / classification: `cloud_npuaaS_lead` / fit: `MID` / outreach: `MID` / 매출시점: `중기`
- NH농협은행 / CSP 고객 기업 / classification: `watchlist` / fit: `MID` / outreach: `MID` / 매출시점: `장기`


## 버전 2 — B2B + B2G 우선 검토 요약

- 삼성SDS / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `중기`
- 엘리스그룹 / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- 한글과컴퓨터 / CSP 고객 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기` / B2G 근거: `기사/RSS 기반` / 나라장터 확인: `미수행`
- 우리은행 / CSP 고객 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `중기`
- NHN클라우드 / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `중기`
- 건강보험심사평가원 / 온프레미스 기업 / classification: `structure_check` / fit: `MID` / outreach: `HIGH` / 매출시점: `중기` / B2G 근거: `기사/RSS 기반` / 나라장터 확인: `미수행`
- 에코아이티 / CSP 고객 기업 / classification: `cloud_npuaaS_lead` / fit: `MID` / outreach: `MID` / 매출시점: `중기`
- NH농협은행 / CSP 고객 기업 / classification: `watchlist` / fit: `MID` / outreach: `MID` / 매출시점: `장기`


## 상세 후보 평가

### 1. 삼성SDS

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `CSP 운영 기업`
- 분류: `priority_outreach`
- 확인된 프로젝트/시그널: 경북 구미 대규모 AI 데이터센터 구축 투자 및 동탄 데이터센터 전력 확보, 우리은행 AI 에이전트 사업 우선협상대상자 선정
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 모델 호환성은 미확인 상태이나, 경북 구미에 60MW 규모 AI 데이터센터 구축을 추진 중이며 동탄 데이터센터 20MW 전력 확보 등 대규모 인프라 증설이 구체화되었습니다. 또한 금융권 대형 사업인 우리은행 AI 에이전트 우선협상대상자로 선정되는 등 채널 영향력이 극도로 높아 인프라 공급 및 SCP 클라우드 경유 판매 관점에서 최우선순위로 분류합니다.
- hook_type: ``
- 핵심 buying signal: 동탄 데이터센터 전력 확보 및 경북 구미 4273억원 규모 데이터센터 건립 공식화. 우리은행 AI 에이전트 구축 사업 우선협상대상자 지위 획득.
- 인프라 signal: 동탄 및 구미 지역 데이터센터 인프라의 전력 및 물리적 설비 대규모 확충 추진 중.
- timing reason: 신규 데이터센터의 하드웨어 공급망 구축 시점과 금융권 대용량 생성형 AI 인프라 아키텍처를 설계하는 현재 시점이 최적의 영업 진입기입니다.
- 고객 win: 삼성 클라우드 플랫폼(SCP) 기반 NPUaaS 라인업을 강화하여 클라우드 서비스 경쟁력을 높일 수 있으며, 대규모 데이터센터 가동에 따른 전력 소모 및 전력망 부족 이슈를 고효율 RNGD 가속기 도입으로 완화할 수 있습니다.
- FuriosaAI win: 국내 최대 IT서비스 및 클라우드 운영사인 삼성SDS의 유통망을 경유하여 엔터프라이즈 및 금융권 타깃 대량 공급 기회를 선점할 수 있습니다.
- 직접 판매 가능성: `MID`
- CSP 경유 판매 가능성: `HIGH`
- NPUaaS 유도 가능성: `HIGH`
- CSP capacity 증설 가능성: `HIGH`
- 수치 근거: 경북 구미 AI 데이터센터 4273억원 투자 계획 (S009) — 근거: 삼성SDS는 경북 구미에 4273억원을 투자해 60MW 규모 AI 데이터센터를 짓기로 했다. | 구미 데이터센터 60MW 규모 구축 계획 (S009) — 근거: 60MW 규모 AI 데이터센터를 짓기로 했다. | 동탄 데이터센터 서관 가동용 20MW급 전력 확보 (S003) — 근거: 삼성SDS가 경기 동탄 데이터센터 서관 가동을 위해 20MW급 전력을 확보한 사례
- 컨택 명분: 구미 신규 AI 데이터센터 인프라 효율성 극대화 및 SCP 연계 금융 AI 에이전트 하드웨어 아키텍처 제안
- 실제 컨택 시 사용할 말: 최근 구미 AI 데이터센터 투자 및 우리은행 AI 에이전트 사업 수주 소식을 전해 들었습니다. 대용량 금융권 프라이빗 서빙 및 SCP 클라우드 환경에서 물리적 상면과 전력 소모를 혁신적으로 최적화할 수 있는 당사의 RNGD 가속기 도입 협력을 제안드립니다.
- 매출 가능 시점: `중기`
- 담당자 후보 힌트: Head of Cloud, Head of Infrastructure, Head of Data Center, platform lead
- 공개 프로필 URL: 미확인 — v0.6 담당자 검색 필요
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 신규 AI 데이터센터 구축 일정에 부합하는 하드웨어 납품 벤더 등록 절차 확인 필요 | SCP NPUaaS 제품군 내 당사 가속기 추가를 위한 정합성 검증 일정 확인 필요
- source_ids: S003, S009, S025, S027
- source_urls: https://www.e-science.co.kr/news/articleView.html?idxno=130004 | https://www.mt.co.kr/tech/2026/05/23/2026052210211399740 | https://www.sedaily.com/article/20046605?ref=naver | https://www.sedaily.com/article/20046505?ref=naver

### 2. 엘리스그룹

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `CSP 운영 기업`
- 분류: `priority_outreach`
- 확인된 프로젝트/시그널: 코스닥 상장 예비심사 청구서 제출 및 GPUaaS 및 이동식 모듈형 데이터 센터(AI PMDC) 인프라 사업 확장 본격화
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 추론 모델은 미확인 상태이나 상장 예비심사 청구를 계기로 자체 모듈형 데이터 센터(PMDC) 및 대규모 GPUaaS 인프라 사업의 전폭적인 투자가 예견됩니다. 국산 NPU 기반의 서비스 다각화와 상장 포트폴리오 강화 흐름에 맞춰 강력한 채널 가치를 지니고 있어 우선 순위로 평가합니다.
- hook_type: ``
- 핵심 buying signal: 거래소 코스닥 상장예비심사 청구 완료 및 AI 클라우드 인프라(AI PMDC, ECI) 투자 강화 표명.
- 인프라 signal: 이동식 모듈형 데이터 센터 및 자체 대규모 인프라 관리 솔루션을 통한 GPUaaS 서비스 전개.
- timing reason: 상장 자금 조달 및 인프라 라인업 리뉴얼 단계이므로, 기존 GPUaaS의 한계를 개선할 국산 저비용 NPUaaS 협력을 어필하기에 매우 유리한 타이밍입니다.
- 고객 win: 모듈형 데이터 센터 내 극히 제한적인 전력 및 냉각 설비 환경에서 RNGD의 고성능 저전력 특성을 통해 전력 밀도당 서빙 성능을 극대화하고, 기존 GPU 위주 라인업에 고효율 NPU 기반 저비용 서비스를 신설할 수 있습니다.
- FuriosaAI win: 상장을 추진하는 유망 풀스택 AI 기업을 채널 파트너로 선점하여 클라우드 서비스형 가속기 실적을 신속히 확보할 수 있습니다.
- 직접 판매 가능성: `LOW`
- CSP 경유 판매 가능성: `HIGH`
- NPUaaS 유도 가능성: `HIGH`
- CSP capacity 증설 가능성: `HIGH`
- 수치 근거: 없음
- 컨택 명분: 모듈형 데이터센터(PMDC) 및 ECI 플랫폼 내 RNGD 탑재를 통한 NPUaaS 서비스 공동 개발 제안
- 실제 컨택 시 사용할 말: 코스닥 상장 예비심사 청구서 제출을 매우 축하드립니다. 엘리스그룹의 고도화된 이동식 모듈형 데이터센터(AI PMDC) 및 AI 클라우드 인프라에 당사의 저전력 고효율 RNGD 가속기를 연동하여 가성비가 극대화된 NPUaaS 서비스 라인업을 상장 시점에 맞춰 함께 선보이기를 제안합니다.
- 매출 가능 시점: `단기`
- 담당자 후보 힌트: CTO, Head of Cloud, Head of Infrastructure, platform lead
- 공개 프로필 URL: 미확인 — v0.6 담당자 검색 필요
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 엘리스그룹 내부의 자체 GPUaaS 인프라 아키텍처에 당사 컨테이너 툴킷 연동 가능 여부 검토 필요
- source_ids: S012, S013, S014, S015, S016, S017
- source_urls: http://www.hansbiz.co.kr/news/articleView.html?idxno=839792 | http://www.joseilbo.com/news/news_read.php?uid=568639&class=53&grp= | https://www.fetv.co.kr/news/articleView.html?idxno=302765 | https://www.the-stock.kr/news/articleView.html?idxno=32570 | https://www.newspim.com/news/view/20260520000146 | https://www.cstimes.com/news/articleView.html?idxno=706484

### 3. 한글과컴퓨터

- 국가: `KR`
- 시장: `B2G`
- 타깃 유형: `CSP 고객 기업`
- 분류: `priority_outreach`
- 확인된 프로젝트/시그널: LG AI연구원과 전략적 협약을 통한 AI 문서 에이전트 공동 개발 및 공공 AX 조달 시장 본격 진출 선언
- 확인된 모델명: `EXAONE`
- 모델 매칭 상태: `family_only`
- 모델 fit_score: `MID`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 사용 모델이 엑사원 계열로 당사 엑사원 4.0 지원 사양과 패밀리 범주에서 연계 가능합니다. 한컴의 오랜 공공 부문 도메인 권력과 LG AI연구원의 기술력이 결합한 대형 연합체가 탄생했으며, 망분리 및 프라이빗 클라우드를 강력하게 요구하는 B2G 시장 공동 침투를 타깃으로 하므로 GTM 파트너십 가치가 최고 수준입니다.
- hook_type: ``
- 핵심 buying signal: 한컴의 문서 AI 솔루션과 LG AI연구원의 엑사원(EXAONE) 결합 솔루션을 통한 정부부처, 공공기관, 공기업 대상의 공동 영업망 전개.
- 인프라 signal: B2G 타깃의 온프레미스 망분리 인프라 및 전용 하드웨어 서버 환경 대응 요구 증대.
- timing reason: 양사 제휴를 통한 공공 AX 시장 수주전이 개시되는 초기 단계이므로 조달용 온프레미스 RNGD 탑재 패키지를 공동 발굴하기에 최적기입니다.
- 고객 win: 공공기관의 엄격한 보안 지침인 망분리 환경 내에 대용량 AI 에이전트를 도입할 때, 국산 저전력 가속기인 RNGD를 패키징하여 정부 부처의 비용 절감 요구와 장비 국산화 가점을 충족할 수 있습니다.
- FuriosaAI win: 한컴의 막강한 공공 조달 네트워크를 통해 서버형 RNGD 패키지를 공공기관 및 주요 지자체에 간접 공급하는 고성능 B2G 포트폴리오를 빠르게 구축합니다.
- 직접 판매 가능성: `MID`
- CSP 경유 판매 가능성: `MID`
- NPUaaS 유도 가능성: `MID`
- CSP capacity 증설 가능성: `LOW`
- 수치 근거: 없음
- 컨택 명분: 한컴-LG AI연구원 공공 AX 문서 솔루션 대상 저전력 온프레미스 RNGD 서버 패키징 협력 제안
- 실제 컨택 시 사용할 말: 최근 LG AI연구원과의 공공 AX 시장 연맹 결성 소식을 인상 깊게 보았습니다. 정부부처 및 공공기관의 완전 망분리 및 온프레미스 요구사항에 즉시 대응하고 대규모 조달 경쟁력을 선점하실 수 있도록, 당사의 국산 저전력 RNGD 가속기를 결합한 솔루션 패키지 구성을 제안드립니다.
- 매출 가능 시점: `단기`
- 담당자 후보 힌트: CIO, CTO, Head of Platform, public sector lead
- 공개 프로필 URL: 미확인 — v0.6 담당자 검색 필요
- 기존 접점: `확인 필요`
- B2G 근거 유형: `기사/RSS 기반`
- 나라장터 직접 확인: `미수행`
- 조달상 다음 액션: 나라장터/RFP 직접 확인 필요
- 확인 필요: 챗엑사원 및 한컴 AI 에이전트 결합 모델의 당사 엑사원 4.0 전용 서빙 스택 내 정상 가속 여부 사전 확인 필요
- source_ids: S020, S021, S022, S023, S024
- source_urls: http://www.newslock.co.kr/news/articleView.html?idxno=130504 | https://www.mt.co.kr/tech/2026/05/22/2026052215283358675 | https://www.mk.co.kr/article/12055579 | https://www.getnews.co.kr/news/articleView.html?idxno=870707 | https://www.newsis.com/view/NISX20260522_0003640664

### 4. 우리은행

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `CSP 고객 기업`
- 분류: `priority_outreach`
- 확인된 프로젝트/시그널: 자산관리 및 기업분석 AI 에이전트 구축 사업의 우선협상대상자로 삼성SDS 선정
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 구체적인 추론용 LLM 버전은 아직 비공개이나, 대형 시중은행의 자산관리 핵심 업무를 처리하기 위한 프라이빗 AI 아키텍처 구축 사업이 본격 가동되었습니다. 우선협상대상자인 삼성SDS와의 긴밀한 파트너십을 매개로 금융 CSP 경유 또는 NPUaaS 도입 시너지가 대단히 높으므로 우선순위 타깃으로 산정합니다.
- hook_type: ``
- 핵심 buying signal: 자산관리(WM) 및 고객관계관리(CRM) 고도화를 겨냥한 AI 에이전트 시스템 도입 결정을 내리고 우선협상대상자로 삼성SDS 지정.
- 인프라 signal: 금융권 규제 하에 외부 데이터센터와 분리된 프라이빗 클라우드 혹은 온프레미스 기반의 전용 서빙 서버 요구 가능성 농후.
- timing reason: 우선협상자 선정 직후 솔루션 및 서버 인프라 하드웨어 스택 확정이 이뤄지는 단계이므로 기술적 컨설팅 진입의 적기입니다.
- 고객 win: 대용량 고객 자산 데이터를 프라이빗 클라우드 내에서 항시 서빙하고 RAG 처리를 할 때, 뛰어난 가성비를 자랑하는 RNGD를 도입하여 장기적 시스템 운영비 부담을 혁신적으로 절감할 수 있습니다.
- FuriosaAI win: 금융권 초거대 AI 서빙의 선도적인 랜드마크 레퍼런스를 개척하며, 파트너사인 삼성SDS와의 성공적인 동반 영업 성공 사례를 확보할 수 있습니다.
- 직접 판매 가능성: `LOW`
- CSP 경유 판매 가능성: `HIGH`
- NPUaaS 유도 가능성: `HIGH`
- CSP capacity 증설 가능성: `MID`
- 수치 근거: 없음
- 컨택 명분: 삼성SDS 파트너십 기반 우리은행 AI 에이전트 인프라 고도화용 RNGD 도입 검토 제안
- 실제 컨택 시 사용할 말: 최근 대형 생성형 AI 에이전트 파트너로 삼성SDS를 지정하고 사업을 본궤도에 올리신 점을 축하드립니다. 당사는 사업 수행 파트너인 삼성SDS와 협력하여 은행 내부의 전용 금융 인프라에서 보안을 완벽히 지키면서도 연산 비용을 최적화할 수 있는 RNGD 가속 방안을 제 제안하고자 합니다.
- 매출 가능 시점: `중기`
- 담당자 후보 힌트: CIO, CDO, Head of AI, Head of Infrastructure, procurement department
- 공개 프로필 URL: 미확인 — v0.6 담당자 검색 필요
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 우리은행 시스템의 오프라인 인프라 구축 가능 여부 및 삼성SDS가 구성하는 전용 클라우드 아키텍처 규격 확인 필요
- source_ids: S025, S027
- source_urls: https://www.sedaily.com/article/20046605?ref=naver | https://www.sedaily.com/article/20046505?ref=naver

### 5. NHN클라우드

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `CSP 운영 기업`
- 분류: `priority_outreach`
- 확인된 프로젝트/시그널: 
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 모델 호환성은 미확인 상태이나, 이노그리드 인수 이후 첫 단독 간담회에서 '초거대 GPU 클러스터 기반 AI 서비스' 역량을 주요 성장 동력으로 선언했으며, KACI 연대를 기반으로 글로벌 GPU 공급 불안정에 공동 목소리를 내고 있습니다. 국내 대표 CSP 사업자로서 저비용 NPUaaS 라인업 신설 제안 가치가 매우 커 우선 순위로 분류합니다.
- hook_type: ``
- 핵심 buying signal: 초거대 GPU 클러스터 AI 서비스 공식 선언 및 한국클라우드산업협회(KACI) 파트너들과의 데이터센터 에너지 비용 급등 공동 대응 모색.
- 인프라 signal: 글로벌 CSP에 대적할 자체 초대형 데이터센터 인프라 및 전용 AI 클라우드 인프라 운용 중.
- timing reason: 클라우드 조직 확장 선언 및 대대적인 마케팅 행사가 예고된 지금 시점이 공급망 대안으로서의 RNGD 가치를 선제적으로 제시하기 좋은 시기입니다.
- 고객 win: 외산 GPU의 불안정한 조달 상황과 천정부지로 치솟는 데이터센터 냉각 전력 비용을 압도적인 고효율 저발열 RNGD 카드를 통해 포트폴리오 차원에서 보완할 수 있습니다.
- FuriosaAI win: 민간 및 공공 멀티클라우드 시장 전반에 당사 가속기를 연계 공급하여 안정적인 국산 클라우드 가입형 매출 기회를 확보합니다.
- 직접 판매 가능성: `MID`
- CSP 경유 판매 가능성: `HIGH`
- NPUaaS 유도 가능성: `HIGH`
- CSP capacity 증설 가능성: `HIGH`
- 수치 근거: 없음
- 컨택 명분: NHN클라우드 인프라 비용 최적화 및 국산 가속기 기반 NPUaaS 신규 출시 협의 제안
- 실제 컨택 시 사용할 말: 최근 이노그리드 인수 이후의 초거대 GPU 클러스터 기반 AI 사업 강화 비전을 뜻깊게 보았습니다. 글로벌 클라우드 기업들에 대응하여 인프라 비용 구조를 혁신하고 가입 기업들에게 뛰어난 가성비의 서빙 환경을 제공하기 위한 국산 RNGD 결합 방안을 적극 검토해 보시길 제안합니다.
- 매출 가능 시점: `중기`
- 담당자 후보 힌트: CIO, CTO, Head of Cloud, Head of Infrastructure, platform lead
- 공개 프로필 URL: 미확인 — v0.6 담당자 검색 필요
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: NHN클라우드가 도입하려는 AI 추론 서비스 스택(vLLM 기반 환경 등)과의 소프트웨어 정합성 확인 필요
- source_ids: S005, S008, S030
- source_urls: https://www.ddaily.co.kr/page/view/2026052017342600376 | http://www.boannews.com/media/view.asp?idx=143783&kind=3 | https://www.ddaily.co.kr/page/view/2026052216371975959

### 6. 건강보험심사평가원

- 국가: `KR`
- 시장: `B2G`
- 타깃 유형: `온프레미스 기업`
- 분류: `structure_check`
- 확인된 프로젝트/시그널: GPU 서버 인프라 기반의 AI 통합플랫폼 구축 드라이브 전략 선언
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `MID`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 사용 모델명은 미확인 상태이나, 정보주권이 강력히 보장되어야 하는 공공 의료 평가기관에서 자체 'GPU 서버 기반 AI 통합플랫폼'을 원스톱 프로세스로 직접 도입 및 구축하겠다는 명확한 바이어 신호가 존재합니다. 공공 온프레미스 인프라 시장 진입을 위한 구조 확인용 최우선 타깃입니다.
- hook_type: ``
- 핵심 buying signal: 자체 AI 통합플랫폼을 GPU 인프라 바탕으로 구축하여 원스톱 서비스 개발 및 운영 체계를 마련하겠다는 구체적 로드맵 발표.
- 인프라 signal: 기관 산하 디지털클라우드센터 및 AI융합추진단을 중심으로 자체 물리 서버 하드웨어 인프라 직접 도입 및 관리 예정.
- timing reason: 실무 책임자인 디지털클라우드센터장이 직접 AI 통합 플랫폼 인프라 가속화를 주관하는 시점이므로, 조기 기획 단계에서 국산 가속기 제안이 유효합니다.
- 고객 win: 민감한 개인 보건의료 데이터를 외부 유출 걱정 없이 폐쇄망 온프레미스에서 완벽히 제어하고, 기존 고가 GPU에 의존하던 분석 플랫폼 비용을 국산 RNGD로 대체하여 예산 부담을 대폭 경감할 수 있습니다.
- FuriosaAI win: 전략적 공공 보건 의료 인프라 레퍼런스를 확보하여 타 국가 공공기관 및 대형 병원군으로의 조달 및 SI 침투 기회를 열 수 있습니다.
- 직접 판매 가능성: `HIGH`
- CSP 경유 판매 가능성: `MID`
- NPUaaS 유도 가능성: `MID`
- CSP capacity 증설 가능성: `LOW`
- 수치 근거: 없음
- 컨택 명분: 심평원 독자 AI 통합플랫폼 GPU 인프라 최적화를 위한 국산 RNGD 하드웨어 제안
- 실제 컨택 시 사용할 말: 최근 건강보험심사평가원이 발표한 자체 GPU 서버 기반 AI 통합플랫폼 추진 전략을 대단히 의미 있게 보았습니다. 보건의료 데이터 보안 준수 및 도입 예산 효율 극대화를 달성하기 위해 당사의 국산 저전력 가속기인 RNGD 기반의 온프레미스 시스템 사양 제안을 논의드리고자 합니다.
- 매출 가능 시점: `중기`
- 담당자 후보 힌트: Head of Infrastructure, Head of Data Center, platform lead, procurement department
- 공개 프로필 URL: 미확인 — v0.6 담당자 검색 필요
- 기존 접점: `확인 필요`
- B2G 근거 유형: `기사/RSS 기반`
- 나라장터 직접 확인: `미수행`
- 조달상 다음 액션: 나라장터/RFP 직접 확인 필요
- 확인 필요: 심평원 자체 데이터센터 내 도입될 서버 아키텍처 규격의 당사 PCIe 적합성 여부 확인 필요 | 조달 절차 상 직접 구매 또는 파트너 SI 경유 여부 검증 필요
- source_ids: S036
- source_urls: https://www.etnews.com/20260522000181

### 7. 에코아이티

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `CSP 고객 기업`
- 분류: `cloud_npuaaS_lead`
- 확인된 프로젝트/시그널: 전남소방본부 AI 기반 재난 대응 플랫폼 구축 사업 착수 및 Solar LLM 문서 검색 RAG 엔진 도입 진행
- 확인된 모델명: `Solar LLM`
- 모델 매칭 상태: `family_only`
- 모델 fit_score: `MID`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `MID`
- RNGD fit_score: `MID`
- outreach priority: `MID`
- fit vs priority 설명: 사용 모델이 당사 호환 범위에 드는 Upstage Solar LLM 계열(family_only)로 명시되어 기술적 정합성이 훌륭합니다. 쿠버네티스 기반의 클라우드 인프라 상에서 소방 RAG 및 문서 AI 플랫폼을 실개발하는 구조이므로 클라우드 기반 가속 가치가 돋보여 NPUaaS 유도 관점에서 중요하게 모니터링합니다.
- hook_type: ``
- 핵심 buying signal: 전남소방본부용 'AI 기반 재난 대응 플랫폼' 구축 계약 수행 및 Solar LLM 학습 데이터를 적용한 RAG 시스템 개발 본격화.
- 인프라 signal: 쿠버네티스 기반 클라우드 가상화 기술을 적극 도입하여 활용하고 있는 IT 개발 환경.
- timing reason: 실제 RAG 데이터 학습 및 추론 알고리즘 구축 초기 단계에 진입하였으므로 성능 가속을 담당할 인프라 제안이 통용되는 시기입니다.
- 고객 win: 쿠버네티스 가상화 환경에서 대량의 정형/비정형 문서를 RAG 분석 시, vLLM 오픈소스 에코시스템과 호환성이 높은 RNGD를 연계 사용하여 상시 가속화 전력 비용을 극적으로 줄일 수 있습니다.
- FuriosaAI win: 대민 안전과 직결된 대표적인 공공 재난 시스템에 당사 가속 기술을 녹여내어, Solar LLM 및 RAG 특화용 국산 추론 칩 성과 레퍼런스를 견고히 합니다.
- 직접 판매 가능성: `MID`
- CSP 경유 판매 가능성: `HIGH`
- NPUaaS 유도 가능성: `HIGH`
- CSP capacity 증설 가능성: `LOW`
- 수치 근거: 없음
- 컨택 명분: 전남소방본부 재난 대응 RAG 시스템 내 Solar LLM 추론 가속용 RNGD 연동 방안 검토 제안
- 실제 컨택 시 사용할 말: 에코아이티가 진행 중이신 전남소방본부 AI 재난 대응 플랫폼의 Solar LLM 및 RAG 구축 프로젝트에 깊은 관심이 있습니다. 쿠버네티스 환경 하에서 해당 생성형 문서 가공 모델의 서빙 지연 시간을 줄이고 인프라 비용 경쟁력을 기여할 당사의 고효율 RNGD 기반 최적화 스택 연동 방안을 제안드립니다.
- 매출 가능 시점: `중기`
- 담당자 후보 힌트: CTO, Head of Platform, public sector lead
- 공개 프로필 URL: 미확인 — v0.6 담당자 검색 필요
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 에코아이티가 전남소방본부 망에서 사용하는 Solar LLM 프레임워크의 상세 버전 및 vLLM 서빙 포트와의 호환 확인 필요
- source_ids: S028
- source_urls: https://magazine.hankyung.com/business/article/202605196285b

### 8. NH농협은행

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `CSP 고객 기업`
- 분류: `watchlist`
- 확인된 프로젝트/시그널: LG CNS와 농협 전용 생성형 AI(EXAONE 3.5 기반 파인튜닝) 및 RAG 플랫폼 구축 진행 중
- 확인된 모델명: `EXAONE 3.5`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `MID`
- RNGD fit_score: `MID`
- outreach priority: `MID`
- fit vs priority 설명: 사용 모델이 당사 공식 컴파일된 EXAONE-4.0 사양과 버전 정렬이 맞지 않는 EXAONE 3.5 버전을 채택 중이므로 모델 fit_score는 보수적으로 LOW로 책정하나, 금융 프라이빗 AI 대형 프로젝트를 직접 기동하고 있어 장기 협력 채널 및 로드맵 호환성 검토 대상으로 관리해야 합니다.
- hook_type: ``
- 핵심 buying signal: LG CNS와 전용 초거대 AI 기반의 플랫폼 구축 착수 및 RAG 활용 내부규정 검색 서비스 기시범 전개.
- 인프라 signal: 은행 전용 보안 가상화망 구축 요구 및 온프레미스/전용 금융 AI 가상 인프라 구축 지향.
- timing reason: 현재 사내 행정 및 내부 문서 가공 중심의 시범 운영 단계이므로, 향후 고성능 인프라 전환 단계에 RNGD 검토 가능성을 사전 정지 작업해두기에 알맞은 장기적 접근 시점입니다.
- 고객 win: 엄격한 규제와 망분리가 중시되는 시중은행 사내망에서 가벼운 전력 설계와 고출력 가속이 가능한 NPU를 통해, 상시 RAG 탐색 서버 비용을 획기적으로 낮추고 안정적인 금융 보안 처리를 확립합니다.
- FuriosaAI win: 초거대 엑사원 계열 모델을 변형 활용 중인 시중 금융 대기업에 당사 칩셋의 잠재적 상용 서빙 호환성을 성공적으로 점검하고 간접 영업 파이프라인을 구축합니다.
- 직접 판매 가능성: `LOW`
- CSP 경유 판매 가능성: `MID`
- NPUaaS 유도 가능성: `MID`
- CSP capacity 증설 가능성: `LOW`
- 수치 근거: 엑사원 3.5 모델 기반 파인튜닝 구축 (S019) — 근거: 엑사원 3.5를 파인튜닝하고
- 컨택 명분: 농협 전용 금융 생성형 AI 인프라 최적화를 위한 EXAONE 계열 RNGD 서빙 호환성 사전 연구 협력 제안
- 실제 컨택 시 사용할 말: 최근 LG CNS와 파트너십 하에 진행 중이신 엑사원 3.5 기반 농협 전용 생성형 AI와 RAG 플랫폼 구축 동향을 인상 깊게 살펴보았습니다. 은행 내부망에서 해당 문서 검색 서비스가 최고 효율로 가동될 수 있도록 엑사원 계열 전용 가속 및 최적화 연동 사전 검토를 파트너사들과 공동 추진해 보시길 제안합니다.
- 매출 가능 시점: `장기`
- 담당자 후보 힌트: CIO, CDO, Head of AI, Head of Platform
- 공개 프로필 URL: 미확인 — v0.6 담당자 검색 필요
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: EXAONE 3.5 모델의 아키텍처적 당사 가속 가능 범위 분석 및 솔루션 파트너사인 LG CNS 개발 부서와의 우회 소통 채널 검토
- source_ids: S019
- source_urls: https://www.news2day.co.kr/article/20260522500024


## FuriosaAI 공개 문서 refresh 요약

- docs_total: `11`
- docs_successful: `11`
- docs_failed: `0`

### Successful docs
- Supported Models / chars: `1603` / https://developer.furiosa.ai/latest/en/overview/supported_models.html
- Release 2026.2 / chars: `10480` / https://developer.furiosa.ai/docs-dev/PR-3475/en/whatsnew/release-2026.2.html
- RNGD Overview / chars: `2548` / https://developer.furiosa.ai/latest/en/overview/rngd.html
- Software Stack / chars: `3602` / https://developer.furiosa.ai/latest/en/overview/software_stack.html
- Roadmap / chars: `2750` / https://developer.furiosa.ai/latest/en/overview/roadmap.html
- Furiosa LLM Intro / chars: `1653` / https://developer.furiosa.ai/latest/en/furiosa_llm/intro.html
- Cloud Native Toolkit / chars: `600` / https://developer.furiosa.ai/latest/en/cloud_native_toolkit/intro.html
- System Management Interface / chars: `760` / https://developer.furiosa.ai/latest/en/device_management/system_management_interface.html
- Hugging Face FuriosaAI Org / chars: `3619` / https://huggingface.co/furiosa-ai
- Hugging Face FuriosaAI Models / chars: `1280` / https://huggingface.co/furiosa-ai/models
- Hugging Face FuriosaAI Collections / chars: `1736` / https://huggingface.co/furiosa-ai/collections

### Supported model entries
- DeepSeek R1 / supported_architecture_or_model_family / Supported Models
- EXAONE-4.0 / supported_architecture_or_model_family / Supported Models
- Llama-3.1 / supported_architecture_or_model_family / Supported Models
- Llama-3.3 / supported_architecture_or_model_family / Supported Models
- Solar 1.0 / supported_architecture_or_model_family / Supported Models
- Qwen 2 / supported_architecture_or_model_family / Supported Models
- Qwen2 / supported_architecture_or_model_family / Supported Models
- Qwen2.5 / supported_architecture_or_model_family / Supported Models
- Qwen3 / supported_architecture_or_model_family / Supported Models
- Qwen3 Embedding / supported_architecture_or_model_family / Supported Models
- Qwen3 Reranker / supported_architecture_or_model_family / Supported Models
- Qwen3 / supported_architecture_or_model_family / Release 2026.2
- Qwen2 / supported_architecture_or_model_family / Roadmap
- Qwen2.5 / supported_architecture_or_model_family / Roadmap
- Qwen3 / supported_architecture_or_model_family / Roadmap
- Qwen2 / supported_architecture_or_model_family / Hugging Face FuriosaAI Org
- Qwen 2 / supported_architecture_or_model_family / Hugging Face FuriosaAI Org
- Qwen2.5 / supported_architecture_or_model_family / Hugging Face FuriosaAI Org
- Qwen3 / supported_architecture_or_model_family / Hugging Face FuriosaAI Org
- Qwen3 / supported_architecture_or_model_family / Hugging Face FuriosaAI Models
- DeepSeek R1 / supported_architecture_or_model_family / Hugging Face FuriosaAI Collections
- Llama-3.1 / supported_architecture_or_model_family / Hugging Face FuriosaAI Collections
- Llama-3.3 / supported_architecture_or_model_family / Hugging Face FuriosaAI Collections
- Qwen 2 / supported_architecture_or_model_family / Hugging Face FuriosaAI Collections
- Qwen2.5 / supported_architecture_or_model_family / Hugging Face FuriosaAI Collections
- Qwen3 / supported_architecture_or_model_family / Hugging Face FuriosaAI Collections

### Planned model entries
- GPT-OSS / planned_future_support / Supported Models
- K-EXAONE / planned_future_support / Supported Models
- Solar Open / planned_future_support / Supported Models
- Qwen3 MoE / planned_future_support / Supported Models
- Qwen3 VL / planned_future_support / Supported Models
- GPT-OSS / planned_future_support / Roadmap
- K-EXAONE / planned_future_support / Roadmap
- Solar Open / planned_future_support / Roadmap
- Qwen3 MoE / planned_future_support / Roadmap
- Qwen3 VL / planned_future_support / Roadmap

### Precompiled / example model artifacts
- EXAONE-4.0-32B / precompiled_or_example_hf_artifact / Supported Models
- EXAONE-4.0-32B-FP8 / precompiled_or_example_hf_artifact / Supported Models
- Llama-3.1-8B-Instruct / precompiled_or_example_hf_artifact / Supported Models
- Llama-3.1-70B-Instruct / precompiled_or_example_hf_artifact / Supported Models
- Llama-3.3-70B-Instruct / precompiled_or_example_hf_artifact / Supported Models
- Qwen2.5-Coder-32B-Instruct / precompiled_or_example_hf_artifact / Supported Models
- Qwen3-0.5B-Instruct / precompiled_or_example_hf_artifact / Supported Models
- Qwen3-32B-Instruct / precompiled_or_example_hf_artifact / Supported Models
- Qwen3-Embedding-4B / precompiled_or_example_hf_artifact / Supported Models
- Qwen3-Embedding-8B / precompiled_or_example_hf_artifact / Supported Models
- Qwen3-Reranker-4B / precompiled_or_example_hf_artifact / Supported Models
- Qwen3-Reranker-8B / precompiled_or_example_hf_artifact / Supported Models
- DeepSeek-R1-Distill-Llama-8B / precompiled_or_example_hf_artifact / Supported Models
- DeepSeek-R1-Distill-Llama-70B / precompiled_or_example_hf_artifact / Supported Models
- SOLAR-10.7B-v1.0 / precompiled_or_example_hf_artifact / Supported Models
- SOLAR-10.7B-Instruct-v1.0 / precompiled_or_example_hf_artifact / Supported Models
- LGAI-EXAONE/EXAONE-4.0-32B / precompiled_or_example_hf_artifact / Supported Models
- LGAI-EXAONE/EXAONE-4.0-32B-FP8 / precompiled_or_example_hf_artifact / Supported Models
- meta-llama/Llama-3.1-8B-Instruct / precompiled_or_example_hf_artifact / Supported Models
- meta-llama/Llama-3.1-70B-Instruct / precompiled_or_example_hf_artifact / Supported Models
- meta-llama/Llama-3.3-70B-Instruct / precompiled_or_example_hf_artifact / Supported Models
- Qwen/Qwen2.5-Coder-32B-Instruct / precompiled_or_example_hf_artifact / Supported Models
- Qwen/Qwen2-32B / precompiled_or_example_hf_artifact / Supported Models
- Qwen/Qwen3-0.5B-Instruct / precompiled_or_example_hf_artifact / Supported Models
- Qwen/Qwen3-32B-Instruct / precompiled_or_example_hf_artifact / Supported Models
- Qwen/Qwen3-Embedding-4B / precompiled_or_example_hf_artifact / Supported Models
- Qwen/Qwen3-Embedding-8B / precompiled_or_example_hf_artifact / Supported Models
- Qwen/Qwen3-Reranker-4B / precompiled_or_example_hf_artifact / Supported Models
- Qwen/Qwen3-Reranker-8B / precompiled_or_example_hf_artifact / Supported Models
- upstage/SOLAR-10.7B-v1.0 / precompiled_or_example_hf_artifact / Supported Models
- upstage/SOLAR-10.7B-Instruct-v1.0 / precompiled_or_example_hf_artifact / Supported Models
- Qwen3-32B-FP8 / precompiled_or_example_hf_artifact / Release 2026.2
- Qwen/Qwen3-32B-FP8 / precompiled_or_example_hf_artifact / Release 2026.2
- EXAONE-4.0-32B-FP8 / precompiled_or_example_hf_artifact / Hugging Face FuriosaAI Org
- Llama-3.1-8B-Instruct / precompiled_or_example_hf_artifact / Hugging Face FuriosaAI Org
- Llama-3.1-8B-Instruct-FP8 / precompiled_or_example_hf_artifact / Hugging Face FuriosaAI Org
- Llama-3.3-70B-Instruct / precompiled_or_example_hf_artifact / Hugging Face FuriosaAI Org
- Qwen2.5-0.5B-Instruct / precompiled_or_example_hf_artifact / Hugging Face FuriosaAI Org
- Qwen3-32B-FP8 / precompiled_or_example_hf_artifact / Hugging Face FuriosaAI Org
- Qwen3-Embedding-8B / precompiled_or_example_hf_artifact / Hugging Face FuriosaAI Org
- Qwen3-Reranker-8B / precompiled_or_example_hf_artifact / Hugging Face FuriosaAI Org
- DeepSeek-R1-Distill-Llama-8B / precompiled_or_example_hf_artifact / Hugging Face FuriosaAI Org
- collections / precompiled_or_example_hf_artifact / Hugging Face FuriosaAI Org
- LGAI-EXAONE/EXAONE-4.0-32B-FP8 / precompiled_or_example_hf_artifact / Hugging Face FuriosaAI Org
- meta-llama/Llama-3.1-8B-Instruct / precompiled_or_example_hf_artifact / Hugging Face FuriosaAI Org
- meta-llama/Llama-3.3-70B-Instruct / precompiled_or_example_hf_artifact / Hugging Face FuriosaAI Org
- Qwen/Qwen2.5-0.5B-Instruct / precompiled_or_example_hf_artifact / Hugging Face FuriosaAI Org
- Qwen/Qwen3-Embedding-8B / precompiled_or_example_hf_artifact / Hugging Face FuriosaAI Org
- Qwen/Qwen3-Reranker-8B / precompiled_or_example_hf_artifact / Hugging Face FuriosaAI Org
- Qwen/Qwen3-32B-FP8 / precompiled_or_example_hf_artifact / Hugging Face FuriosaAI Org
- EXAONE-4.0-32B-FP8 / precompiled_huggingface_artifact / Hugging Face FuriosaAI Org
- Qwen3-32B-FP8 / precompiled_huggingface_artifact / Hugging Face FuriosaAI Org
- Llama-3.3-70B-Instruct / precompiled_huggingface_artifact / Hugging Face FuriosaAI Org
- collections / precompiled_huggingface_artifact / Hugging Face FuriosaAI Org
- Llama-3.1-8B-Instruct / precompiled_huggingface_artifact / Hugging Face FuriosaAI Org
- Qwen2.5-0.5B-Instruct / precompiled_huggingface_artifact / Hugging Face FuriosaAI Org
- Qwen3-Embedding-8B / precompiled_huggingface_artifact / Hugging Face FuriosaAI Org
- Qwen3-Reranker-8B / precompiled_huggingface_artifact / Hugging Face FuriosaAI Org
- EXAONE-4.0-32B-FP8 / precompiled_or_example_hf_artifact / Hugging Face FuriosaAI Models
- Llama-3.3-70B-Instruct / precompiled_or_example_hf_artifact / Hugging Face FuriosaAI Models
- Qwen3-32B-FP8 / precompiled_or_example_hf_artifact / Hugging Face FuriosaAI Models
- EXAONE-4.0-32B-FP8 / precompiled_huggingface_artifact / Hugging Face FuriosaAI Models
- Qwen3-32B-FP8 / precompiled_huggingface_artifact / Hugging Face FuriosaAI Models
- Llama-3.3-70B-Instruct / precompiled_huggingface_artifact / Hugging Face FuriosaAI Models
- EXAONE-4.0-32B-FP8 / precompiled_or_example_hf_artifact / Hugging Face FuriosaAI Collections
- Llama-3.3-70B-Instruct / precompiled_or_example_hf_artifact / Hugging Face FuriosaAI Collections
- Qwen3-32B-FP8 / precompiled_or_example_hf_artifact / Hugging Face FuriosaAI Collections
- EXAONE-4.0-32B-FP8 / precompiled_huggingface_artifact / Hugging Face FuriosaAI Collections
- Qwen3-32B-FP8 / precompiled_huggingface_artifact / Hugging Face FuriosaAI Collections
- Llama-3.3-70B-Instruct / precompiled_huggingface_artifact / Hugging Face FuriosaAI Collections

### Keyword hits
- serving_stack: Release 2026.2: OpenAI, Release 2026.2: API, RNGD Overview: Kubernetes, Software Stack: vLLM, Software Stack: OpenAI, Software Stack: OpenAI-Compatible, Software Stack: Kubernetes, Software Stack: container, Software Stack: API, Software Stack: server, Roadmap: Kubernetes, Roadmap: container, Roadmap: API, Furiosa LLM Intro: vLLM, Furiosa LLM Intro: OpenAI, Furiosa LLM Intro: OpenAI-Compatible, Furiosa LLM Intro: Kubernetes, Furiosa LLM Intro: API, Furiosa LLM Intro: server, Cloud Native Toolkit: Kubernetes
- hardware_ops: Release 2026.2: RNGD, RNGD Overview: RNGD, RNGD Overview: HBM, RNGD Overview: power, RNGD Overview: SR-IOV, RNGD Overview: virtualization, RNGD Overview: PCIe, RNGD Overview: thermal, Software Stack: power, Roadmap: RNGD, Hugging Face FuriosaAI Org: RNGD

## 통합 수집 요약

1. **[인터뷰] 엘칸토, '브랑누아' 별도 법인으로 스핀오프**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T22:04:00+09:00`
   - matched_query_or_feed: `제조 AI 플랫폼`
   - url: http://www.apparelnews.co.kr/news/news_view/?idx=225419
   - summary_snippet: 제조와 공급망은 기존 엘칸토 인프라와 별개로 차별화된 신규 인프라를 활용하며, 향후 채널 확대를 위한... 플랫폼 내에서도 엘칸토 소속 브랜드와 카니발라이제이션을 최소화하고 타깃과 컨셉을 차별화하는...

2. **소상공인 온라인 판로 지원 '소담스퀘어 울산' 들어선다**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T21:43:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.ulsanpress.net/news/articleView.html?idxno=575840
   - summary_snippet: '소담스퀘어 울산'은 인공지능(AI) 디지털 스튜디오를 비롯해 주방(키친)·다중(멀티)·1인 미디어 스튜디오... 울산시는 울산연구원 빅데이터센터, 울산정보산업진흥원, 울산소상공인연합회 등 지역 유관기관 및...

3. **초대 통합특별시 미래 좌우할 공약, 방점은 '미래 먹거리 산업' 육성에**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T21:28:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: http://www.mdilbo.com/detail/tohfpC/755848
   - summary_snippet: 후보들이 AI(인공지능) 등 미래 먹거리 산업 집중 육성을 통한 특별시 발전 전략을 모색하고 있는 것으로 나타났다. 이재명 정부의 ‘5극 3특 국가균형성장’과 맞물려 산업 대전환 필요성과 함께 데이터센터 유치 등...

4. **[투자를IT다] 2026년 5월 3주차 IT기업 주요 소식과 시장 전망**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T21:24:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://it.donga.com/108937/
   - summary_snippet: 데이터센터와 반도체 자동화 테스트 사업은 AI 인프라 투자에 힘입어 가파른 성장 궤도에 올랐으며, 2027년까지 지속될 것으로 확신한다. 항공우주·방위 분야에서는 각국의 국방 자주권 강화 기조가 다년간의...

5. **[2026 대구경북 이노비즈 기업을 찾아서] (2) 고품질 건강기능식품 전문...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T21:24:00+09:00`
   - matched_query_or_feed: `제조 AI 플랫폼`
   - url: https://www.idaegu.co.kr/news/articleView.html?idxno=549132
   - summary_snippet: 제안하는 'AI 헬스케어 어드바이징 프로그램'을 고도화하고 있으며, 고객 개개인에게 맞춤형 건강 설루션을 제공하는 차세대 플랫폼 구축을 목표로 하고 있다. 에이팜건강은 이 같은 기술 혁신의 원동력은 임직원의...

6. **장수군수 선거, 전·현직 재대결…기본사회 해법은?**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T21:17:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://news.kbs.co.kr/news/pc/view/view.do?ncd=8569474&ref=A
   - summary_snippet: 양수발전소 유치와 햇빛소득마을, AI 데이터센터를 연계해 신재생에너지 소득을 기반으로 한 기본사회로 나아가겠다는 구상입니다. [최훈식/민주당 장수군수 후보 : "기본소득을 바탕으로 해서 의료, 돌봄, 교육, 정주...

7. **사대와 왜색의 굴레 언제 벗을까?**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T21:16:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: http://www.gnmaeil.com/news/articleView.html?idxno=587263
   - summary_snippet: AI 시대에 살고 있다. 잘못된 사대와 왜색의 문화를 바로잡지 못한다면 그 폐해는 눈덩이처럼 불어날 것이다. 왜곡된 정보로 채워진 데이터 센터의 클라우드는 가상의 세계를 혼탁하게 만들 것이다. 그리고 이를 바로...

8. **2026 남도의 선택)강진군수 선거, 현직이냐 민주당이냐**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T21:14:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://mpmbc.co.kr/NewsArticle/1520163
   - summary_snippet: 그 재원은 강진군에 전국에서 가장 큰 규모의 AI 데이터센터 유치를 통해서.. 이번 선거는 민주당 조직력과 현역 군수의 인지도, 그리고 공천 갈등 이후 형성된 지역 민심이 판세를 가를 핵심 변수로 꼽힙니다. 다가올...

9. **(시장 후보에게 듣는다) 청년일자리 분야**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T20:54:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: http://web.ubc.co.kr/wp/archives/127773
   - summary_snippet: ' AI데이터센터 건립에 따른 관련 기업 유치, 지역 대학· 기업과의 취업 연계 활성화 등이 청년 유출을 막기 위한 주요 과제로 떠오르고 있습니다. 유비씨 뉴스 전병주입니다. -2026/05/25

10. **[미리보는 이데일리 신문]'사회적 감수성' 놓친 마케팅…기업 생존 위협...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T20:52:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.edaily.co.kr/news/newspath.asp?newsid=02082806645452528
   - summary_snippet: 올리고…AI 데이터센터 짓고 시멘트 기업, 부동산 개발 ‘큰손’ 변신 △이데일리가 만났습니다 -“파키스탄은 美·이란 모두 설득할 수 있는 나라…종전 이끌어 낼 것” -“백제에 불교 전한 1700년 인연…CEPA 체결로...

11. **“스페이스X 투자 놓쳤다?” 또다른 기회…오픈AI 수혜주가 있다 [투자...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T20:41:00+09:00`
   - matched_query_or_feed: `생성형 AI 도입 기업`
   - url: https://biz.heraldcorp.com/article/10743640?ref=naver
   - summary_snippet: [게티이미지] 일론 머스크의 우주기업 스페이스X에 이어 생성형 인공지능(AI) 대표 기업 오픈AI도 기업공개... 이처럼 국내 기업들의 협업 범위가 단순 제휴를 넘어 실제 서비스 도입과 구축 단계까지 확대되면서...

12. **"치유로 잇는 한·베 연대"…봄재단, 고엽제 지원 확대**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T20:40:00+09:00`
   - matched_query_or_feed: `병원 AI 플랫폼`
   - url: https://view.asiae.co.kr/article/2026052520233985334
   - summary_snippet: 협력 플랫폼 구축 방안도 논의했다. 논의 안에는 ▲고엽제 피해 환우 전문 치료·재활 병원 ▲건강검진센터 ▲AI·디지털 헬스케어 기반 예방의학 시스템 ▲줄기세포 연구·치료센터 ▲메디컬 뷰티 시스템 구축 등이...

13. **“스페이스X 투자 놓쳤다?” 또다른 기회…오픈AI 수혜주가 있다 [투자360] - 헤럴드경제**
   - source: `rss`
   - published_at_kst: `2026-05-25T20:40:00+09:00`
   - matched_query_or_feed: `Google News KR 생성형 AI`
   - url: https://news.google.com/rss/articles/CBMiVkFVX3lxTE5ROUE4TW1Sc0JrRS1fV2FhelVMYzQyQ3h2Uk8tbnp5MnpKS2NXVjVLeGo3RGthWWZXTmJiNE40UVlrOU5fbmtqcjRyTWp4dGlsOTAtM1hn?oc=5
   - summary_snippet: “스페이스X 투자 놓쳤다?” 또다른 기회…오픈AI 수혜주가 있다 [투자360]  헤럴드경제

14. **[중국증시 주간 포인트] 5월 PMI, D램 리더 '창신메모리' IPO, 화웨이 '에...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T20:29:00+09:00`
   - matched_query_or_feed: `제조 AI 플랫폼`
   - url: https://www.newspim.com/news/view/20260525000259
   - summary_snippet: 5월 제조업 PMI 발표 △中 D램 선도기업 '창신메모리' IPO 심의 △화웨이, '에이전트아트' 오픈소스... 화웨이, '에이전트아트' 오픈소스 강화판 공개 중국 화웨이가 5월 30일 기업용 AI 에이전트 개발 플랫폼...

15. **[인터뷰] "다양한 현장 경험, 제주 변화로 연결하겠다"**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T20:28:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.jemin.com/news/articleView.html?idxno=838036
   - summary_snippet: AI 데이터센터 유치, 제주과학기술원 설립, 해상풍력 슈퍼그리드 사업을 통해 제주를 대한민국 미래산업의 전진기지로 만들겠다. 청년들이 제주에서도 좋은 일자리와 미래를 꿈꿀 수 있도록 하겠다. 셋째는 생활밀착형...

16. **日 화낙-구글, 피지컬 AI 분야 전략적 제휴**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T20:18:00+09:00`
   - matched_query_or_feed: `생성형 AI 도입 기업`
   - url: https://www.irobotnews.com/news/articleView.html?idxno=46545
   - summary_snippet: 일본 산업용 로봇 기업 화낙(FANUC)이 구글과 전략적 협력을 통해 '피지컬 AI(Physical AI)' 기반 산업용 로봇... 기술을 도입한 바 있다. 여기에 구글의 생성형 AI와 추론 기술까지 더해지면서, AI 기반 공장 자동화...

17. **[인터뷰] 고진석 텐스페이스 대표 "데이터센터 멈춘 진짜 이유는 불신" - 한스경제**
   - source: `rss`
   - published_at_kst: `2026-05-25T20:09:57+09:00`
   - matched_query_or_feed: `Google News KR AI 데이터센터`
   - url: https://news.google.com/rss/articles/CBMia0FVX3lxTE5YWmo5ZXkzSko0R3E2cHFfblZYQ09FU091dUh5cnBjREtOTUlQRWVGdHFsNVY2ZDZfT0R0Y3llX0tEd2ZHQWJOSTFwZG1wdmxnQ05qRzJDRHVSNkx1bURnUXF6bjA2Q19NQlJz?oc=5
   - summary_snippet: [인터뷰] 고진석 텐스페이스 대표 "데이터센터 멈춘 진짜 이유는 불신"  한스경제

18. **“세 번의 창업 끝에 찾은 답”…넥스테인 양병석 대표가 만드는 로컬 ...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T19:56:00+09:00`
   - matched_query_or_feed: `클라우드 AI 서비스`
   - url: https://www.venturesquare.net/1085242/
   - summary_snippet: 핵심은 클라우드가 아니라 ‘내 컴퓨터 안에서 직접 돌아가는 AI’라는 점이다. 기존 거대 AI 서비스들은 사용자의 대화와 데이터를 외부 서버에서 처리한다. 편리함은 있지만, 회사...

19. **조선소 인수 나선 부산 기자재사들…해양종합기업 박차**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T19:30:00+09:00`
   - matched_query_or_feed: `제조 AI 플랫폼`
   - url: http://www.kookje.co.kr/news2011/asp/newsbody.asp?code=0200&key=20260526.22010006486
   - summary_snippet: 스마트 선박 운영 플랫폼 구축 등 해양 AX 분야 투자도 확대한다. 적극적인 투자로 지난해에는 창사 이래 역대 매출 1316억 원을 기록하기도 했다. 회의에 참석한 전문가들은 “AI 역량이 다소 떨어지는 지역 제조업계에...

20. **[6·3지선 인터뷰] 박찬대 "유정복과 차이는 실행력…중앙 힘으로 인천...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T19:28:00+09:00`
   - matched_query_or_feed: `제조 AI 플랫폼`
   - url: https://weekly.hankooki.com/news/articleView.html?idxno=7165793
   - summary_snippet: AI·바이오·반도체·에너지와 연결해 오래된 제조업을 청년이 일하고 싶은 산업으로 바꾸겠다. 우리 인천... 이 곳에 방치된 상상플랫폼을 활성화하고, 내항 개발을 통해 역사가 살아있는 대표 관광 거점으로 이 곳을...


## 다음 단계

1. LLM 후보 품질 확인
2. 노이즈가 많으면 NAVER_QUERIES / RSS_FEEDS 개선
3. 후보가 너무 적으면 MAX_LLM_SOURCES 상향
4. Gemini 3.5 Flash vs 2.5 Flash 품질 비교
5. 나라장터/B2G 수집 추가
6. 담당자/의사결정자 탐색 추가
7. Notion 또는 Google Docs 업로드 추가
