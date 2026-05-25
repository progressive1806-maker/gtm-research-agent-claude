# FuriosaAI GTM Research Agent Test Run

## 실행 정보

- run_id: `2026-05-25_211534_test_v0.6-refactor-smoke`
- mode: `test`
- memo: `v0.6-refactor-smoke`
- executed_at_kst: `2026-05-25T21:21:10.977042+09:00`
- agent_version: `v0.6`
- instructions_loaded_chars: `21592`
- naver_sources_recent_7d_count: `214`
- rss_sources_recent_7d_count: `96`
- merged_sources_recent_7d_count: `310`
- furiosa_docs_successful: `11`
- furiosa_docs_failed: `0`
- llm_called: `True`
- llm_error: ``

## 현재 단계

이 실행은 v0.6 테스트입니다.

이번 버전에서는 네이버 뉴스 API, RSS feed, FuriosaAI 공개 개발자 문서를 수집한 뒤 Gemini로 GTM 후보를 1차 평가하고, 별도 LLM 호출로 매니저용 gtm_report.md를 작성합니다.

아직 나라장터 직접 API, 담당자 심화 탐색, Notion 업로드는 수행하지 않았습니다.

## LLM 실행 요약

- overall_assessment: 최근 국내 클라우드 서비스 제공업체(CSP) 및 온프레미스 인프라를 확장하려는 엔터프라이즈의 움직임이 매우 활발하게 전개되고 있습니다. 특히 삼성SDS, NHN클라우드, 엘리스그룹과 같은 기업들이 데이터센터 증설 및 대형 인공지능 인프라 투자를 발표함에 따라 저전력 고효율 NPU 수요가 더욱 가시화되고 있습니다. 공공 및 금융 분야에서도 자체적인 생성형 인공지능 솔루션 도입과 하이브리드 RAG 플랫폼 구축을 본격화하면서, 국산 가속기를 포함한 다양한 연산 자원 다각화 기조가 뚜렷해지고 있어 단기 및 중기 매출 기회 창출에 긍정적인 상황입니다.
- top_priority_names: 삼성SDS, 엘리스그룹, 한글과컴퓨터, NHN클라우드
- noise_ratio_comment: 수집된 정보 중 전반적인 정책 수립이나 구체적인 가속기 도입 요구사항이 결여된 주식 시장 정보 및 전력망 포화에 관한 거시적 동향은 영업 활동 관점에서 직접적인 가치 부여가 낮아 노이즈로 처리하고 필터링하였습니다.
- model_compatibility_caution: 본 평가에서는 모델의 버전 및 제품명을 엄밀히 분석하였습니다. 기사에서 확인된 엑사원 제품의 경우, 특정 버전 정보가 불분명하거나 precompiled 대상에서 제외된 하위 버전인 경우 'family_only'로 규정하고 적합성을 보수적으로 책정하였습니다. 향후 미확인 모델에 대해서는 아키텍처 연동 및 컴파일 라이브러리 검증에 주의가 필요합니다.

## LLM 후보 평가 결과

## 버전 1 — B2B only 우선 검토 요약

- 삼성SDS / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- 엘리스그룹 / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- NHN클라우드 / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- NH농협은행 / 온프레미스 기업 / classification: `structure_check` / fit: `MID` / outreach: `MID` / 매출시점: `중기`


## 버전 2 — B2B + B2G 우선 검토 요약

- 삼성SDS / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- 엘리스그룹 / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- NHN클라우드 / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- NH농협은행 / 온프레미스 기업 / classification: `structure_check` / fit: `MID` / outreach: `MID` / 매출시점: `중기`
- 건강보험심사평가원 / 온프레미스 기업 / classification: `structure_check` / fit: `MID` / outreach: `MID` / 매출시점: `중기` / B2G 근거: `기사/RSS 기반` / 나라장터 확인: `미수행`
- 한글과컴퓨터 / CSP 고객 기업 / classification: `cloud_npuaaS_lead` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기` / B2G 근거: `기사/RSS 기반` / 나라장터 확인: `미수행`
- 에코아이티 / CSP 고객 기업 / classification: `cloud_npuaaS_lead` / fit: `MID` / outreach: `MID` / 매출시점: `단기` / B2G 근거: `기사/RSS 기반` / 나라장터 확인: `미수행`


## 상세 후보 평가

### 1. 삼성SDS

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `CSP 운영 기업`
- 분류: `priority_outreach`
- 확인된 프로젝트/시그널: 동탄 데이터센터 전력 확보 및 구미 AI 데이터센터 투자, 우리은행 AI 에이전트 우선협상대상자 선정
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 삼성SDS는 신규 데이터센터 가동 및 금융권 AI 구축 우선협상대상자 선정 등 핵심적인 구매자 신호가 확인되는 주요 사업자입니다. 모델 정합성은 미확인 상태이나, SCP 및 NPUaaS 인프라 확장을 위한 채널 협력 가치가 매우 높으므로 최우선 순위로 분류합니다.
- hook_type: `CLOUD`
- 핵심 buying signal: 우리은행 AI 에이전트 구축 사업의 우선협상대상자로 선정되었으며, 인공지능 인프라 플랫폼 사업 확대를 지속하고 있습니다.
- 인프라 signal: 경기 동탄 데이터센터 서관 가동을 위해 20MW급 전력을 확보하였고, 경북 구미에 4273억원을 투자해 60MW 규모 AI 데이터센터를 구축할 계획입니다.
- timing reason: 대형 데이터센터 인프라 및 전력 수급 이슈가 화두가 되는 시점에서 저전력 가속기를 통한 인프라 효율성을 제안할 최적의 시기입니다.
- 고객 win: 데이터센터 가동 전력의 한계를 겪는 상황에서 저전력 NPU를 배치하여 운영 전력 소모를 제어하고 효율성을 제고할 수 있습니다. 또한 공공 및 금융권의 private 클라우드 요구사항에 최적화된 저비용 고효율 인프라 라인업을 확보하게 됩니다.
- FuriosaAI win: 삼성SDS의 SCP 플랫폼 및 클라우드 서비스 라인업에 RNGD를 등재함으로써 기업 및 금융 인프라 전반에 대규모 추론 가속기 공급 기회를 넓힐 수 있습니다.
- 직접 판매 가능성: `MID`
- CSP 경유 판매 가능성: `HIGH`
- NPUaaS 유도 가능성: `HIGH`
- CSP capacity 증설 가능성: `HIGH`
- 수치 근거: 경기 동탄 데이터센터 서관 가동을 위해 20MW급 전력을 확보 (S003) — 근거: 삼성SDS가 경기 동탄 데이터센터 서관 가동을 위해 20MW급 전력을 확보한 사례 | 경북 구미에 4273억원을 투자해 60MW 규모 AI 데이터센터 구축 예정 (S009) — 근거: 삼성SDS는 경북 구미에 4273억원을 투자해 60MW 규모 AI 데이터센터를 짓기로 했다.
- 컨택 명분: 우리은행 인공지능 시스템 수주 및 구미 AI 데이터센터 투자 구체화에 발맞추어, 전력 제한 데이터센터 운영을 최적화할 수 있는 RNGD 도입을 제안하고자 합니다.
- 실제 컨택 시 사용할 말: 최근 우리은행 인공지능 사업 수주와 구미에 계획 중인 60MW 규모 신규 데이터센터 인프라 구축 소식을 접하고 연락드렸습니다. 동탄 데이터센터 가동을 위한 20MW급 전력 확보 사례처럼 인프라 효율화가 핵심 과제인 상황에서, 저전력 고효율 RNGD를 활용하여 전력 소모와 상면 공간을 획기적으로 최적화하는 협력 방안을 논의하고자 합니다.
- 매출 가능 시점: `단기`
- 담당자 후보 힌트: 삼성SDS 클라우드서비스사업부장, AI서비스 및 인프라 담당 임원, 또는 구미 데이터센터 인프라 기획 부서장
- 공개 프로필 URL: 미확인 — v0.6 담당자 검색 필요
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 구미 및 동탄 데이터센터 내 NPU PoC 기회 확보 가능 여부 | 우리은행 AI 에이전트 인프라 환경의 하이브리드 요구조건 유무
- source_ids: S003, S009, S024, S026
- source_urls: https://www.e-science.co.kr/news/articleView.html?idxno=130004 | https://www.mt.co.kr/tech/2026/05/23/2026052210211399740 | https://www.sedaily.com/article/20046605?ref=naver | https://www.sedaily.com/article/20046505?ref=naver

### 2. 엘리스그룹

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `CSP 운영 기업`
- 분류: `priority_outreach`
- 확인된 프로젝트/시그널: 코스닥 상장예비심사 청구 및 AI 클라우드(ECI, GPUaaS, AI PMDC) 인프라 확장 추진
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 엘리스그룹은 자체 모듈형 데이터센터 및 클라우드 환경을 설계·가동하는 대표적 인프라 혁신 기업입니다. 모델 정보는 미확인 상태이나 상장을 통한 인프라 자본 투자 및 플랫폼 고도화 시점이므로 가치가 커 최우선 순위로 지정합니다.
- hook_type: `CLOUD`
- 핵심 buying signal: 코스닥 상장예비심사 신청을 본격화하며 확보된 자금력을 바탕으로 대규모 인프라 선점과 플랫폼 다각화를 선언하였습니다.
- 인프라 signal: 이동식 모듈형 데이터센터(AI PMDC) 인프라를 확장하고 있으며, 효율적으로 가속기를 배치하는 자체 클라우드 아키텍처를 보유하고 있습니다.
- timing reason: 상장 자금을 인프라에 할당하는 조율기이므로, 외산 GPU 일변도를 탈피하여 가격 경쟁력을 극대화할 수 있는 고효율 국산 NPU 제품군 결합 제안의 적기입니다.
- 고객 win: 수익성 제고가 중요한 상장 추진 시점에서 고가의 하드웨어 및 열관리 전기요금을 통제하고, 연산 서비스 단가를 효율화할 수 있습니다. 차별화된 모듈형 국산 하드웨어 패키지를 완성하여 서비스 포트폴리오를 넓힙니다.
- FuriosaAI win: 엘리스의 탄력적인 클라우드 서빙 플랫폼에 RNGD를 연동하여 상징적인 에듀테크 및 산업용 AI 클라우드 레퍼런스를 다수 획득할 수 있습니다.
- 직접 판매 가능성: `MID`
- CSP 경유 판매 가능성: `HIGH`
- NPUaaS 유도 가능성: `HIGH`
- CSP capacity 증설 가능성: `HIGH`
- 수치 근거: 없음
- 컨택 명분: 상장 준비 일정에 발맞추어, 이동식 데이터센터 인프라 및 클라우드 플랫폼의 성능 효율화를 달성하는 RNGD 도입을 제안하기 위함입니다.
- 실제 컨택 시 사용할 말: 최근 코스닥 상장예비심사 청구와 함께 국내외 클라우드 인프라 확장 계획을 접하고 연락드렸습니다. 엘리스의 모듈형 데이터센터 및 ECI 플랫폼에 저전력·고효율 RNGD를 통합 적용하신다면, 효율적인 에너지 관리와 자원 운영비 최소화를 동시에 실현하여 차세대 AI 클라우드 가치를 입증하실 수 있습니다.
- 매출 가능 시점: `단기`
- 담당자 후보 힌트: 김재원 대표이사, 또는 AI 클라우드 플랫폼 및 데이터센터 사업 총괄 임원
- 공개 프로필 URL: 미확인 — v0.6 담당자 검색 필요
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 엘리스 PMDC 내 냉각 및 전력 공급 설계상 RNGD 하드웨어 최적 규격 적합성 여부 | 상장 완료 이전 조기 시범 평가용 NPU 서버 도입 가능성
- source_ids: S012, S013, S014, S015, S016
- source_urls: http://www.joseilbo.com/news/news_read.php?uid=568639&class=53&grp= | https://www.fetv.co.kr/news/articleView.html?idxno=302765 | https://www.the-stock.kr/news/articleView.html?idxno=32570 | https://www.newspim.com/news/view/20260520000146 | https://www.cstimes.com/news/articleView.html?idxno=706484

### 3. NHN클라우드

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `CSP 운영 기업`
- 분류: `priority_outreach`
- 확인된 프로젝트/시그널: 초거대 GPU 클러스터 기반 AI 클라우드 운영 및 가속기 인프라 고도화 추진
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: NHN클라우드는 광주 데이터센터 등 국가적인 초거대 인프라를 실제 구축해 이끌어가는 선두 기업입니다. 특정 모델 정보는 한정적이나 국가 인프라 주권 준수 및 가속기 다각화 기조가 뚜렷하여 최우선 순위로 분류합니다.
- hook_type: `CLOUD`
- 핵심 buying signal: 초거대 GPU 클러스터를 보유하고 있으며, 수급난 타개와 전력 비용 폭증에 맞대응하기 위해 국산 가속기 연동을 검토하고 있습니다.
- 인프라 signal: 광주 인공지능 전용 데이터센터 등 대형 컴퓨팅 전용 공간과 강력한 멀티 테넌트 퍼블릭 클라우드 서비스를 가동하고 있습니다.
- timing reason: 전력 공급량 포화 및 전력량 인상 상황에서 비용 안정화를 꾀하는 CSP의 대안 인프라 제안 최적기입니다.
- 고객 win: 초고밀도 고전력 센터의 냉각 유지 관리에 최적화된 고효율 RNGD를 연동해 상면 배치를 밀집시키고 전력 효율을 획득합니다. 합리적인 연산 서빙 수수료를 제시해 클라우드 고객 유치력을 넓힙니다.
- FuriosaAI win: 정부가 신뢰하는 주요 퍼블릭 클라우드 사업자 인프라에 RNGD를 표준 국산 가속기로 안착시켜 연쇄적인 대규모 도입 레퍼런스를 확보하게 됩니다.
- 직접 판매 가능성: `MID`
- CSP 경유 판매 가능성: `HIGH`
- NPUaaS 유도 가능성: `HIGH`
- CSP capacity 증설 가능성: `HIGH`
- 수치 근거: 없음
- 컨택 명분: 국가 규모 연산 자원 고도화 방침에 따라 RNGD 연계를 통한 초저비용 클라우드 상용 NPUaaS 런칭을 협의하기 위함입니다.
- 실제 컨택 시 사용할 말: 국내외 에너지 단가 폭등 상황 속에서 NHN클라우드가 추진하시는 초거대 데이터센터 전력 고도화 계획을 잘 알고 있습니다. 당사의 고밀도 저전력 RNGD 카드는 랙당 소모 에너지를 유의미하게 억제하면서 뛰어난 오픈소스 인공지능 구동 성능을 발휘하여, 클라우드 가치가 혁신되는 훌륭한 대안 인프라가 될 수 있습니다.
- 매출 가능 시점: `단기`
- 담당자 후보 힌트: NHN클라우드 공동대표이사, 클라우드인프라본부 총괄, 또는 AI연구소 수석 임원
- 공개 프로필 URL: 미확인 — v0.6 담당자 검색 필요
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 광주 데이터센터 내 국산 가속기 가상화 솔루션 지원 규격 호환 검증 가능성 | 공공 CSAP 구역에 배정할 예정인 가속기 평가 수량 규모
- source_ids: S005, S008, S029
- source_urls: https://www.ddaily.co.kr/page/view/2026052017342600376 | http://www.boannews.com/media/view.asp?idx=143783&kind=3 | https://www.ddaily.co.kr/page/view/2026052216371975959

### 4. NH농협은행

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `온프레미스 기업`
- 분류: `structure_check`
- 확인된 프로젝트/시그널: 내부 생성형 AI 플랫폼 구축 및 LG CNS 파트너십을 통한 엑사원 3.5 파인튜닝
- 확인된 모델명: `EXAONE-3.5`
- 모델 매칭 상태: `family_only`
- 모델 fit_score: `MID`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `MID`
- outreach priority: `MID`
- fit vs priority 설명: 농협은행은 내부 플랫폼을 고도화하기 위해 LG CNS와 협력하여 자체 전용 생성형 AI를 업무에 도입하고 있습니다. precompiled 대상군인 엑사원 계열 모델을 쓰므로 연동 가능성을 점검할 가치가 있으며, 폐쇄망 등 엄격한 금융 정보 환경 대응을 목적으로 제안이 유효합니다.
- hook_type: `SOVEREIGN`
- 핵심 buying signal: 내부 규정 및 상품 정보 검색을 위해 검색증강생성(RAG) 및 파인튜닝 모델을 결합한 내부 전용 AI 시스템을 구축하였습니다.
- 인프라 signal: 금융 보안상 외부 퍼블릭 연결을 완전히 차단하는 엄격한 폐쇄망 온프레미스 데이터센터 내에 가동할 자원이 요구됩니다.
- timing reason: 장기적으로 유지되어 온 금융 망분리 규제 완화 움직임과 맞물려, 전용 생성형 시스템의 전력 요금 한계 완화를 검토하기 좋은 순간입니다.
- 고객 win: 데이터 유출 위협이 배제된 폐쇄형 온프레미스 인프라를 마련하면서도 고전력 GPU 대비 서버 전력과 실시간 운영 비용을 유의미하게 억제할 수 있습니다. 농협 전용 지능형 시스템의 안정된 하드웨어 공급원을 내재화하게 됩니다.
- FuriosaAI win: 금융 보안 요건이 매우 엄밀한 제1금융권 핵심 은행 시스템 내부에 RNGD 구축 사례를 남겨 높은 공신력과 확산성을 획득할 수 있습니다.
- 직접 판매 가능성: `MID`
- CSP 경유 판매 가능성: `MID`
- NPUaaS 유도 가능성: `LOW`
- CSP capacity 증설 가능성: `LOW`
- 수치 근거: 없음
- 컨택 명분: 농협은행 전용 생성형 AI 구동에 탑재할 수 있는 저전력 RNGD 가속 장치를 제안하여 연산 효율화 실증 가능성을 모색하기 위함입니다.
- 실제 컨택 시 사용할 말: 최근 LG CNS와 연계하여 엑사원 기반 전용 생성형 AI 및 사내 RAG 플랫폼을 가동하시는 소식을 전해 들었습니다. 금융권의 엄격한 폐쇄망 하이브리드 환경에서 안정적인 온프레미스 시스템을 확보하기 위해, 전력 대비 성능이 우수하고 엑사원 아키텍처에 대응 가능한 저전력 가속기 RNGD 적용 방안을 논의하고 싶습니다.
- 매출 가능 시점: `중기`
- 담당자 후보 힌트: NH농협은행 IT부문장, 디지털전략사업부장, 또는 정보보호본부 최고보안책임자
- 공개 프로필 URL: 미확인 — v0.6 담당자 검색 필요
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 금융 보안상 국산 NPU 전용 서빙 툴 및 vLLM 최적화 패키지 사용 제약이 있는지 여부 | 사용 중인 엑사원 3.5 모델에서 4.0 계열로의 이전 계획 존재 여부
- source_ids: S018
- source_urls: https://www.news2day.co.kr/article/20260522500024

### 5. 건강보험심사평가원

- 국가: `KR`
- 시장: `B2G`
- 타깃 유형: `온프레미스 기업`
- 분류: `structure_check`
- 확인된 프로젝트/시그널: AI 통합플랫폼 구축 및 GPU 서버 기반 인프라 도입 드라이브
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `MID`
- RNGD fit_score: `MID`
- outreach priority: `MID`
- fit vs priority 설명: 심평원은 대민 편의를 도모하고 업무 체계를 가다듬고자 자체적인 GPU 연산 플랫폼의 예산과 구축 추진 계획을 명문화했습니다. 도입할 하드웨어 사양을 확정해 나가는 중이므로 비용 및 전력 요건을 충족할 RNGD 도입 설득을 조기에 전개하기 수월합니다.
- hook_type: ``
- 핵심 buying signal: 디지털전략실(디지털클라우드센터) 명의로 대민 약국 찾기 등 원스톱 보건 서비스 처리가 가능한 통합 연산 플랫폼 기획을 수립하고 기계를 도입하려 합니다.
- 인프라 signal: 보건 심사 데이터 유출을 막고 신뢰성을 지키기 위해 자체 센터 내에 하드웨어 가속기 클러스터 서버를 운용할 예정입니다.
- timing reason: 전체 사업 수립 기획서 마련 단계이므로, 국산 전용 NPU 사양을 조달 규격서 상에 포함시킬 수 있는 아주 시기적절한 단계입니다.
- 고객 win: 민감한 의료 정보를 사내에서 고성능으로 파인튜닝하고 추론하되, 과다한 고비용 외산 연산 카드 대비 효율적인 하드웨어 예산 배정이 가능합니다. 저전력 공급 설계로 준정부 공공 자산의 전기료 소모 요건을 만족합니다.
- FuriosaAI win: 국내 주요 보건 의료 공공기관의 대표적인 추론 플랫폼에 자사 전용 RNGD 서버를 안착시키는 상징적 납품 레퍼런스를 개척합니다.
- 직접 판매 가능성: `MID`
- CSP 경유 판매 가능성: `MID`
- NPUaaS 유도 가능성: `MID`
- CSP capacity 증설 가능성: `LOW`
- 수치 근거: 없음
- 컨택 명분: 심평원의 통합 플랫폼 구축을 선도하는 부서에 국산 NPU 성능 실증 보고서 및 전력량 개선 비교 자료를 발송하여 공공 입찰 참여 여건을 마련하기 위함입니다.
- 실제 컨택 시 사용할 말: 귀원의 AI 통합 플랫폼 드라이브 및 전용 연산 센터 기획 소식을 듣고 연락드렸습니다. 전력 공급 수급 부담과 냉각 관리에 민감한 데이터센터 환경에서, 고비용 외산 인프라를 대폭 보완할 수 있는 저전력 가속기 RNGD 적용 이점과 공공 도입을 위한 규격 제안 자료를 소개해 드리고자 합니다.
- 매출 가능 시점: `중기`
- 담당자 후보 힌트: 건강보험심사평가원 디지털전략실장 (디지털클라우드센터장 겸 AI융합추진단장) 또는 정보인프라 실무 책임자
- 공개 프로필 URL: 미확인 — v0.6 담당자 검색 필요
- 기존 접점: `확인 필요`
- B2G 근거 유형: `기사/RSS 기반`
- 나라장터 직접 확인: `미수행`
- 조달상 다음 액션: 나라장터/RFP 직접 확인 필요
- 확인 필요: 기획 단계에서의 의료 텍스트 및 이미지 분석용 핵심 모델 후보군 | 조달 절차 상의 조기 PoC 평가용 자원 무상 제공 여건
- source_ids: S035
- source_urls: https://www.etnews.com/20260522000181

### 6. 한글과컴퓨터

- 국가: `KR`
- 시장: `B2G`
- 타깃 유형: `CSP 고객 기업`
- 분류: `cloud_npuaaS_lead`
- 확인된 프로젝트/시그널: LG AI연구원의 엑사원(EXAONE) 모델과 자사 문서 AI 에이전트 결합, 공공 AX 시장 공동 공략 추진
- 확인된 모델명: `EXAONE (버전 미명시)`
- 모델 매칭 상태: `family_only`
- 모델 fit_score: `MID`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 한컴은 LG AI연구원과 긴밀히 협력해 공공 시장을 겨냥한 AI 에이전트 제품군을 확대하고 있습니다. precompiled 지원 제품군인 엑사원 아키텍처를 적극 사용하므로 고도로 정합하며, 정부부처 및 공공기관에 최적화된 저전력 패키지 구성 제안이 가능하여 높은 우선순위를 지닙니다.
- hook_type: `PROCUREMENT`
- 핵심 buying signal: 정부부처, 공공기관, 공기업을 대상으로 '챗엑사원' 및 한컴 AI 에이전트 결합 솔루션 제안을 활발하게 공동 전개하고 있습니다.
- 인프라 signal: 다양한 공공 환경에 맞추어 온프레미스 폐쇄망 구축형 사업과 공공 안전 클라우드 연동 요구사항에 모두 대처하고 있습니다.
- timing reason: 양사 공동 수주 전선이 본격 가동되고 공공 조달 사업 발주가 예상되는 현 시점에서, 비용 경쟁력을 지닌 저전력 NPU를 제안 구성에 선제 탑재하기 좋은 시기입니다.
- 고객 win: 공공기관의 온프레미스 요구 시, 값비싼 외산 가속기를 국산 고성능 NPU로 대체하여 인프라 도입 비용 부담을 덜고 전력 한계 요건을 준수할 수 있습니다. 조달 과정에서 전력 감소 및 국산 가속기 사용에 따른 유리한 평점을 획득하게 됩니다.
- FuriosaAI win: 정부 및 주요 공공기관에 자사 고성능 NPU인 RNGD가 대량 구축되어 대규모 조달 시장 진입을 위한 모범 선례를 도출할 수 있습니다.
- 직접 판매 가능성: `MID`
- CSP 경유 판매 가능성: `HIGH`
- NPUaaS 유도 가능성: `HIGH`
- CSP capacity 증설 가능성: `MID`
- 수치 근거: 없음
- 컨택 명분: 공공 행정 및 문서 처리 솔루션에 연계될 신형 엑사원 기반 가속 장치 제안서 내 규격 탑재를 위한 기술 교류를 희망합니다.
- 실제 컨택 시 사용할 말: 최근 LG AI연구원과의 '챗엑사원' 문서 에이전트 솔루션 협력 및 공공 AX 시장 공동 수주 공략 소식을 접하고 연락드렸습니다. 정부부처와 공기업의 하이브리드 인프라 구축 제안 시, 엑사원 구동에 특화되어 precompiled 지원을 마친 당사 RNGD 가속기를 연계하신다면, 뛰어난 전력 효율성과 비용 경쟁력을 입증하여 사업 수주율을 크게 제고하실 수 있습니다.
- 매출 가능 시점: `단기`
- 담당자 후보 힌트: 한글과컴퓨터 대표이사, 공공사업본부장, 또는 AI 에이전트 서비스 개발 실무 책임자
- 공개 프로필 URL: 미확인 — v0.6 담당자 검색 필요
- 기존 접점: `확인 필요`
- B2G 근거 유형: `기사/RSS 기반`
- 나라장터 직접 확인: `미수행`
- 조달상 다음 액션: 나라장터/RFP 직접 확인 필요
- 확인 필요: 공공 전용 챗엑사원 구동 시 엑사원 4.0-32B 등의 정합 지원 버전 사용 가능 여부 | 조달 공고에 명시된 가속기 조달 국가인증 기준 준수 여부
- source_ids: S019, S020, S021, S022, S023
- source_urls: http://www.newslock.co.kr/news/articleView.html?idxno=130504 | https://www.mt.co.kr/tech/2026/05/22/2026052215283358675 | https://www.mk.co.kr/article/12055579 | https://www.getnews.co.kr/news/articleView.html?idxno=870707 | https://www.newsis.com/view/NISX20260522_0003640664

### 7. 에코아이티

- 국가: `KR`
- 시장: `B2G`
- 타깃 유형: `CSP 고객 기업`
- 분류: `cloud_npuaaS_lead`
- 확인된 프로젝트/시그널: 전남소방본부 AI 기반 재난 대응 플랫폼 구축 본격화 (Solar LLM 적용 및 쿠버네티스 환경)
- 확인된 모델명: `Solar LLM`
- 모델 매칭 상태: `family_only`
- 모델 fit_score: `MID`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `MID`
- RNGD fit_score: `MID`
- outreach priority: `MID`
- fit vs priority 설명: 에코아이티는 공공 소방 행정 및 재난 플랫폼 구축 사업을 실제 수행하는 기업으로, 당사 precompiled에 포함되는 Solar 모델을 활용하고 있습니다. 쿠버네티스 플랫폼 연동 요구사항이 뚜렷하여 가속기 지원 타당성이 높아 클라우드 수요 유도군으로 분류합니다.
- hook_type: ``
- 핵심 buying signal: 전남소방본부의 소방행정 보조 AI 플랫폼 구축 프로젝트 수주를 발표하고 본격적으로 시스템 아키텍처 수립을 전개하고 있습니다.
- 인프라 signal: 다양한 유형의 정형·비정형 데이터를 소화하기 위해 쿠버네티스(K8s) 기반의 클라우드 인프라를 설계하여 탑재할 예정입니다.
- timing reason: 인프라 자원 연동과 플랫폼 세부 기획이 전개되는 시기이므로 개발 단계에서 RNGD의 클라우드 네이티브 툴킷과 최적화 라이브러리를 소개하기 적절합니다.
- 고객 win: 쿠버네티스 기반의 고밀도 컨테이너 자원 관리를 지원하여 인프라 연산 효율을 높이고, 신속한 소방 재난 응답 성능을 이끌어내며 전력 유지 소모량을 축소합니다.
- FuriosaAI win: 공공 안전 및 재난 보조 분야의 신규 Solar LLM 적용 패키지에 가속 장비 구동 레퍼런스를 확보하여 신뢰도를 축적할 수 있습니다.
- 직접 판매 가능성: `LOW`
- CSP 경유 판매 가능성: `HIGH`
- NPUaaS 유도 가능성: `HIGH`
- CSP capacity 증설 가능성: `MID`
- 수치 근거: 없음
- 컨택 명분: 전남소방본부의 소방행정 플랫폼에 최적화된 Solar 연동 및 쿠버네티스 환경 내 RNGD 가용성 조사를 권장하기 위함입니다.
- 실제 컨택 시 사용할 말: 최근 전남소방본부의 인공지능 재난 대응 플랫폼 구축 사업을 수주하신 소식을 접하였습니다. 해당 서비스가 쿠버네티스 기반 클라우드 아키텍처를 취하고 Solar LLM을 적용하는 만큼, 당사의 Solar 지원 모델 라이브러리와 컨테이너 관리 툴킷을 결합해 저비용·고성능 인프라를 구성하는 방안을 제안하고자 합니다.
- 매출 가능 시점: `단기`
- 담당자 후보 힌트: 에코아이티 솔루션개발센터장, 또는 전남소방본부 시스템 구축 총괄 PM
- 공개 프로필 URL: 미확인 — v0.6 담당자 검색 필요
- 기존 접점: `확인 필요`
- B2G 근거 유형: `기사/RSS 기반`
- 나라장터 직접 확인: `미수행`
- 조달상 다음 액션: 나라장터/RFP 직접 확인 필요
- 확인 필요: 전남소방본부 시스템이 배포되는 인프라가 공공 클라우드(CSAP)에 위치하는지 여부 | Solar LLM 외에 기타 오픈소스 인공지능 모델 혼용 가능성
- source_ids: S027
- source_urls: https://magazine.hankyung.com/business/article/202605196285b


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

1. **2026 남도의 선택)강진군수 선거, 현직이냐 민주당이냐**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T21:14:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://mpmbc.co.kr/NewsArticle/1520163
   - summary_snippet: 그 재원은 강진군에 전국에서 가장 큰 규모의 AI 데이터센터 유치를 통해서.. 이번 선거는 민주당 조직력과 현역 군수의 인지도, 그리고 공천 갈등 이후 형성된 지역 민심이 판세를 가를 핵심 변수로 꼽힙니다. 다가올...

2. **(시장 후보에게 듣는다) 청년일자리 분야**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T20:54:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: http://web.ubc.co.kr/wp/archives/127773
   - summary_snippet: ' AI데이터센터 건립에 따른 관련 기업 유치, 지역 대학· 기업과의 취업 연계 활성화 등이 청년 유출을 막기 위한 주요 과제로 떠오르고 있습니다. 유비씨 뉴스 전병주입니다. -2026/05/25

3. **[미리보는 이데일리 신문]'사회적 감수성' 놓친 마케팅…기업 생존 위협...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T20:52:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.edaily.co.kr/news/newspath.asp?newsid=02082806645452528
   - summary_snippet: 올리고…AI 데이터센터 짓고 시멘트 기업, 부동산 개발 ‘큰손’ 변신 △이데일리가 만났습니다 -“파키스탄은 美·이란 모두 설득할 수 있는 나라…종전 이끌어 낼 것” -“백제에 불교 전한 1700년 인연…CEPA 체결로...

4. **“스페이스X 투자 놓쳤다?” 또다른 기회…오픈AI 수혜주가 있다 [투자...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T20:41:00+09:00`
   - matched_query_or_feed: `생성형 AI 도입 기업`
   - url: https://biz.heraldcorp.com/article/10743640?ref=naver
   - summary_snippet: [게티이미지] 일론 머스크의 우주기업 스페이스X에 이어 생성형 인공지능(AI) 대표 기업 오픈AI도 기업공개... 이처럼 국내 기업들의 협업 범위가 단순 제휴를 넘어 실제 서비스 도입과 구축 단계까지 확대되면서...

5. **"치유로 잇는 한·베 연대"…봄재단, 고엽제 지원 확대**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T20:40:00+09:00`
   - matched_query_or_feed: `병원 AI 플랫폼`
   - url: https://view.asiae.co.kr/article/2026052520233985334
   - summary_snippet: 협력 플랫폼 구축 방안도 논의했다. 논의 안에는 ▲고엽제 피해 환우 전문 치료·재활 병원 ▲건강검진센터 ▲AI·디지털 헬스케어 기반 예방의학 시스템 ▲줄기세포 연구·치료센터 ▲메디컬 뷰티 시스템 구축 등이...

6. **“스페이스X 투자 놓쳤다?” 또다른 기회…오픈AI 수혜주가 있다 [투자360] - 헤럴드경제**
   - source: `rss`
   - published_at_kst: `2026-05-25T20:40:00+09:00`
   - matched_query_or_feed: `Google News KR 생성형 AI`
   - url: https://news.google.com/rss/articles/CBMiVkFVX3lxTE5ROUE4TW1Sc0JrRS1fV2FhelVMYzQyQ3h2Uk8tbnp5MnpKS2NXVjVLeGo3RGthWWZXTmJiNE40UVlrOU5fbmtqcjRyTWp4dGlsOTAtM1hn?oc=5
   - summary_snippet: “스페이스X 투자 놓쳤다?” 또다른 기회…오픈AI 수혜주가 있다 [투자360]  헤럴드경제

7. **[중국증시 주간 포인트] 5월 PMI, D램 리더 '창신메모리' IPO, 화웨이 '에...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T20:29:00+09:00`
   - matched_query_or_feed: `제조 AI 플랫폼`
   - url: https://www.newspim.com/news/view/20260525000259
   - summary_snippet: 5월 제조업 PMI 발표 △中 D램 선도기업 '창신메모리' IPO 심의 △화웨이, '에이전트아트' 오픈소스... 화웨이, '에이전트아트' 오픈소스 강화판 공개 중국 화웨이가 5월 30일 기업용 AI 에이전트 개발 플랫폼...

8. **[인터뷰] "다양한 현장 경험, 제주 변화로 연결하겠다"**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T20:28:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.jemin.com/news/articleView.html?idxno=838036
   - summary_snippet: AI 데이터센터 유치, 제주과학기술원 설립, 해상풍력 슈퍼그리드 사업을 통해 제주를 대한민국 미래산업의 전진기지로 만들겠다. 청년들이 제주에서도 좋은 일자리와 미래를 꿈꿀 수 있도록 하겠다. 셋째는 생활밀착형...

9. **日 화낙-구글, 피지컬 AI 분야 전략적 제휴**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T20:18:00+09:00`
   - matched_query_or_feed: `생성형 AI 도입 기업`
   - url: https://www.irobotnews.com/news/articleView.html?idxno=46545
   - summary_snippet: 일본 산업용 로봇 기업 화낙(FANUC)이 구글과 전략적 협력을 통해 '피지컬 AI(Physical AI)' 기반 산업용 로봇... 기술을 도입한 바 있다. 여기에 구글의 생성형 AI와 추론 기술까지 더해지면서, AI 기반 공장 자동화...

10. **울산에도 판로 확대 돕는 '소담스퀘어'**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T20:16:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: http://www.ujeil.com/news/articleView.html?idxno=386198
   - summary_snippet: 이번에 조성되는 '소담스퀘어 울산'은 인공지능(AI) 디지털 스튜디오를 비롯해 주방(키친)·다중(멀티)·1인... 이와 함께 울산연구원 빅데이터센터, 울산정보산업진흥원, 울산소상공인연합회 등 지역 유관기관 및...

11. **[6.3 지방선거-광주] 이정현 후보 "광주·전남 미래산업 국가특구 지정...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T20:14:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.newscj.com/news/articleView.html?idxno=3403798
   - summary_snippet: 또 여수·광양 지역의 화학·철강 산업 전환과 해남·고흥 지역 데이터센터 및 우주항공 산업 연계 가능성도 제시했다. 이 후보는 AI·데이터 산업의 전력 수요 증가와 RE100 기반 산업 전환 흐름을 언급하며 "청년 인구와...

12. **이정현 "광주·전남, AI·데이터·에너지 산업 국가 거점 육성"**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T20:13:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.nocutnews.co.kr/news/6522307?utm_source=naver&utm_medium=article&utm_campaign=20260525081256
   - summary_snippet: 지역으로 AI·데이터 산업 육성에 최적의 조건을 갖추고 있다"고 설명했다. 구체적으로는 광주에 AI·데이터... 또 "여수·광양은 미래 화학·수소·철강 산업 전환 거점으로, 해남·고흥은 데이터센터와 우주항공 산업을...

13. **[인터뷰] 고진석 텐스페이스 대표 "데이터센터 멈춘 진짜 이유는 불신"**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T20:10:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: http://www.hansbiz.co.kr/news/articleView.html?idxno=840342
   - summary_snippet: 현재는 AI·블록체인 기반 핀테크 회사인 텐스페이스를 이끌며 최근에는 전남 장성군의 AI 데이터센터 구축 전략 컨설팅을 마무리했다. 그가 본 '데이터센터 포비아'의 본질은 무엇일까. 지난 22일 그와 이야기를 나누어...

14. **[인터뷰] 고진석 텐스페이스 대표 "데이터센터 멈춘 진짜 이유는 불신" - 한스경제**
   - source: `rss`
   - published_at_kst: `2026-05-25T20:09:57+09:00`
   - matched_query_or_feed: `Google News KR AI 데이터센터`
   - url: https://news.google.com/rss/articles/CBMia0FVX3lxTE5YWmo5ZXkzSko0R3E2cHFfblZYQ09FU091dUh5cnBjREtOTUlQRWVGdHFsNVY2ZDZfT0R0Y3llX0tEd2ZHQWJOSTFwZG1wdmxnQ05qRzJDRHVSNkx1bURnUXF6bjA2Q19NQlJz?oc=5
   - summary_snippet: [인터뷰] 고진석 텐스페이스 대표 "데이터센터 멈춘 진짜 이유는 불신"  한스경제

15. **[직설]AI로 일자리를 만든다고요?**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T20:02:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.khan.co.kr/article/202605252002025
   - summary_snippet: 또한 미국과 달리 한국에서는 AI 데이터센터 유치 경쟁이 치열하다. 그뿐만이 아니다. “우리 지역을 ‘피지컬 AI 테스트베드로 내놓겠다”고 공약하는 정치인도 여럿이다. 피지컬 AI는 인간의 행동과 생체 정보를...

16. **“세 번의 창업 끝에 찾은 답”…넥스테인 양병석 대표가 만드는 로컬 ...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T19:56:00+09:00`
   - matched_query_or_feed: `클라우드 AI 서비스`
   - url: https://www.venturesquare.net/1085242/
   - summary_snippet: 핵심은 클라우드가 아니라 ‘내 컴퓨터 안에서 직접 돌아가는 AI’라는 점이다. 기존 거대 AI 서비스들은 사용자의 대화와 데이터를 외부 서버에서 처리한다. 편리함은 있지만, 회사...

17. **조선소 인수 나선 부산 기자재사들…해양종합기업 박차**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T19:30:00+09:00`
   - matched_query_or_feed: `제조 AI 플랫폼`
   - url: http://www.kookje.co.kr/news2011/asp/newsbody.asp?code=0200&key=20260526.22010006486
   - summary_snippet: 스마트 선박 운영 플랫폼 구축 등 해양 AX 분야 투자도 확대한다. 적극적인 투자로 지난해에는 창사 이래 역대 매출 1316억 원을 기록하기도 했다. 회의에 참석한 전문가들은 “AI 역량이 다소 떨어지는 지역 제조업계에...

18. **[6·3지선 인터뷰] 박찬대 "유정복과 차이는 실행력…중앙 힘으로 인천...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T19:28:00+09:00`
   - matched_query_or_feed: `제조 AI 플랫폼`
   - url: https://weekly.hankooki.com/news/articleView.html?idxno=7165793
   - summary_snippet: AI·바이오·반도체·에너지와 연결해 오래된 제조업을 청년이 일하고 싶은 산업으로 바꾸겠다. 우리 인천... 이 곳에 방치된 상상플랫폼을 활성화하고, 내항 개발을 통해 역사가 살아있는 대표 관광 거점으로 이 곳을...

19. **"지능도 무상급식 시대로" ···최윤홍 부산교육감 후보, 공공 AI 도서관...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T19:26:00+09:00`
   - matched_query_or_feed: `공공 생성형 AI 구축`
   - url: https://www.smartbizn.com/news/articleView.html?idxno=144640
   - summary_snippet: | 스마트비즈 = 정선 기자 | 21세기 생성형 인공지능(AI) 시대의 도래와 함께 부모의 경제력이 교육 격차로... 표방한 공공 AI 도서관 'AI 노드(AI Node)' 설립 공약을 발표했다. 최 후보는 이번 공약 발표를 통해 "부모의 지갑...

20. **양윤녕 후보 “위성곤 후보 AI·해상풍력 공약, 제주를 전력 먹는 데이터섬으로 만들 우려” - 일간제주**
   - source: `rss`
   - published_at_kst: `2026-05-25T19:23:22+09:00`
   - matched_query_or_feed: `Google News KR AI 데이터센터`
   - url: https://news.google.com/rss/articles/CBMia0FVX3lxTE15UDBKZ0c3UjNFZlBfcEFTdDFGcThRMnRxVUZCZmVpSGY3NWFXZVJiVS1MLVc2eVNwUHBtZDBmZFVNU0VVQTRraDc1X2dvQXhEWnIxdGlBaHl0RHE4NjVsdUdnM2lERG9JY0xz?oc=5
   - summary_snippet: 양윤녕 후보 “위성곤 후보 AI·해상풍력 공약, 제주를 전력 먹는 데이터섬으로 만들 우려”  일간제주


## 다음 단계

1. LLM 후보 품질 확인
2. 노이즈가 많으면 NAVER_QUERIES / RSS_FEEDS 개선
3. 후보가 너무 적으면 MAX_LLM_SOURCES 상향
4. Gemini 3.5 Flash vs 2.5 Flash 품질 비교
5. 나라장터/B2G 수집 추가
6. 담당자/의사결정자 탐색 추가
7. Notion 또는 Google Docs 업로드 추가
