# FuriosaAI GTM Research Agent Test Run

## 실행 정보

- run_id: `2026-05-26_110520_test_post-credential-fix`
- mode: `test`
- memo: `post-credential-fix`
- executed_at_kst: `2026-05-26T11:11:47.902995+09:00`
- agent_version: `v0.7`
- instructions_loaded_chars: `21592`
- naver_sources_recent_7d_count: `204`
- rss_sources_recent_7d_count: `235`
- merged_sources_recent_7d_count: `439`
- furiosa_docs_successful: `11`
- furiosa_docs_failed: `0`
- llm_called: `True`
- llm_error: ``

## 현재 단계

이 실행은 v0.7 테스트입니다.

이번 버전에서는 네이버 뉴스 API, RSS feed, FuriosaAI 공개 개발자 문서를 수집한 뒤 Gemini로 GTM 후보를 1차 평가하고, 별도 LLM 호출로 매니저용 gtm_report.md를 작성합니다.

아직 나라장터 직접 API, 담당자 심화 탐색, Notion 업로드는 수행하지 않았습니다.

## LLM 실행 요약

- overall_assessment: 최근 국내 생성형 AI 및 IT 인프라 시장은 삼성SDS의 대형 금융권 AI 에이전트 수주, NHN클라우드의 팩토리엑스 가동, 그리고 국가적 대형 데이터센터 인프라 모집 등 CSP 및 대형 운영 주체의 자원 확충 동향이 지배하고 있습니다. RNGD의 GTM 활성화를 위해서는 직접 판매 방식 외에 삼성SDS SCP, NHN클라우드 등 주요 CSP 플랫폼 내 NPUaaS 라인업 탑재를 추진하여 채널 경유 판매 경로를 선제적으로 확보하는 전략이 가장 효과적일 것으로 보입니다.
- top_priority_names: 삼성SDS, NHN클라우드, KT클라우드, 네이버클라우드, 광주 국가 AI데이터센터
- noise_ratio_comment: 수집된 40건의 자료 중 단순 플랫폼 민원 기사 1건을 제외한 대다수 소스가 망분리 규제 완화, 대형 AI 프로젝트 개시, 메가 데이터센터 구축 등 유의미한 GTM 신호를 제공하여 전반적인 신뢰도가 대단히 높습니다.
- model_compatibility_caution: 자체 금융/의료 보안 및 에이전트를 개발 중인 온프레미스 기업들의 경우 명확한 AI 모델명이 기재되지 않아 모델 정합성을 보수적으로 UNKNOWN으로 분류하였습니다. 다만, 이들을 고객사로 확보하고 있는 CSP 채널 및 플랫폼 인프라 제공 파트너에 대해서는 예외 규정을 적용하여 GTM 우선순위를 상향 조정하였습니다.

## LLM 후보 평가 결과

## 버전 1 — B2B only 우선 검토 요약

- 삼성SDS / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `중기`
- NHN클라우드 / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- KT클라우드 / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `중기`
- 네이버클라우드 / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `중기`
- 우리은행 / CSP 고객 기업 / classification: `cloud_npuaaS_lead` / fit: `MID` / outreach: `HIGH` / 매출시점: `중기`
- KB금융 / 온프레미스 기업 / classification: `watchlist` / fit: `LOW` / outreach: `LOW` / 매출시점: `장기`
- 서울아산병원 / 온프레미스 기업 / classification: `watchlist` / fit: `LOW` / outreach: `LOW` / 매출시점: `장기`


## 버전 2 — B2B + B2G 우선 검토 요약

- 삼성SDS / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `중기`
- NHN클라우드 / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- KT클라우드 / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `중기`
- 네이버클라우드 / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `중기`
- 광주 국가 AI데이터센터 / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기` / B2G 근거: `기사/RSS 기반` / 나라장터 확인: `미수행`
- 우리은행 / CSP 고객 기업 / classification: `cloud_npuaaS_lead` / fit: `MID` / outreach: `HIGH` / 매출시점: `중기`
- KB금융 / 온프레미스 기업 / classification: `watchlist` / fit: `LOW` / outreach: `LOW` / 매출시점: `장기`
- 서울아산병원 / 온프레미스 기업 / classification: `watchlist` / fit: `LOW` / outreach: `LOW` / 매출시점: `장기`


## 상세 후보 평가

### 1. 삼성SDS

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `CSP 운영 기업`
- 분류: `priority_outreach`
- 확인된 프로젝트/시그널: 경북 구미 신규 AI 데이터센터 투자 계획 수립 및 우리은행 금융 AI 에이전트 구축 사업 우선협상대상자 선정
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 개별 AI 모델 적합성은 확인되지 않았으나 경북 구미에 대규모 AI 데이터센터 신설 계획을 발표하였으며, 우리은행 AI 에이전트 사업 수주 등 국내 대형 엔터프라이즈 GTM 핵심 채널이므로 전략적 최우선순위로 평가함
- hook_type: `PARTNER`
- 핵심 buying signal: 우리은행 대규모 금융 AX 에이전트 프로젝트 우선협상대상자 선정 및 구미 신규 AI 데이터센터 인프라 확장 계획
- 인프라 signal: 경북 구미 지역 내 대형 AI 데이터센터 건립 및 자체 클라우드 플랫폼 SCP 인프라 운영
- timing reason: 우리은행 금융 AX 프로젝트 개시와 맞물려 데이터센터 신규 하드웨어 인프라 및 플랫폼 아키텍처 아웃라인이 구체화되는 시점임
- 고객 win: 삼성 클라우드 플랫폼(SCP)에 최적화된 저전력·고효율 가속기를 추가 장착함으로써 대규모 기업 고객들의 추론 인프라 운영 효율성 개선 가능성 확보
- FuriosaAI win: SCP 플랫폼 내 고성능 추론 가속기로 탑재되어 우리은행 등 엔터프라이즈 금융권 고객군으로의 NPUaaS 간접 공급 교두보 확보
- 직접 판매 가능성: `LOW`
- CSP 경유 판매 가능성: `HIGH`
- NPUaaS 유도 가능성: `HIGH`
- CSP capacity 증설 가능성: `HIGH`
- 수치 근거: 삼성SDS 경북 구미 4273억원 투자, 60MW 규모 AI 데이터센터 건립 (S033) — 근거: 삼성SDS는 경북 구미에 4273억원을 투자해 60MW 규모 AI 데이터센터를 짓기로 했다.
- 컨택 명분: 구미 데이터센터 가동 및 SCP 기반 신규 AI 인프라 라인업 다각화를 위한 고효율 RNGD 하드웨어 탑재 논의
- 실제 컨택 시 사용할 말: 최근 구미 지역 신규 AI 데이터센터 투자 및 대형 금융 프로젝트 수주 소식을 보고 연락드렸습니다. 전력 공급망 한계 극복 및 고집적 랙 가동을 위해, 가상화 환경에 부합하는 고성능 추론 반도체와의 기술 검토를 제안 드립니다.
- 매출 가능 시점: `중기`
- 담당자 후보 힌트: Head of Cloud, Head of Infrastructure, platform lead
- 공개 프로필 URL: 
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 구미 신규 데이터센터 인프라 및 가속기 반도체 조달 일정 상세 조율 여부 | SCP 금융 전용 인프라 영역 내 가속기 탑재 가능 여부
- source_ids: S033, S035, S036
- source_urls: https://www.mt.co.kr/tech/2026/05/23/2026052210211399740 | https://www.sedaily.com/article/20046605?ref=naver

### 2. NHN클라우드

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `CSP 운영 기업`
- 분류: `priority_outreach`
- 확인된 프로젝트/시그널: 풀스택 AI 솔루션 브랜드 팩토리엑스 출시 발표 및 GPUaaS 사업 다각화
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 사용 모델은 미정이나, 신규 통합 브랜드 팩토리엑스를 가동하며 자체 GPUaaS 인프라 영역에서 차별화된 저전력 가속기 제품군을 추가로 확보해야 할 비즈니스 니즈가 강력하여 최우선순위로 분류함
- hook_type: `CLOUD`
- 핵심 buying signal: 초거대 AI 실행 환경 경쟁력 제고를 위한 고성능 풀스택 브랜드 팩토리엑스 가동 및 서비스 영역 다각화 선언
- 인프라 signal: 대규모 가속기 클러스터 자원 운영 및 국가 데이터센터 인프라 기술력 보유
- timing reason: 통합 AI 실행 플랫폼의 초기 파트너 에코시스템과 고성능 하드웨어 솔루션 다양성을 공식 확보하고자 하는 시장 경쟁 단계임
- 고객 win: 팩토리엑스 플랫폼 내부에서 초고효율 가속 인프라 옵션을 저비용으로 제공받아 대규모 트래픽 발생 시 서비스 구동 비용을 대폭 축소 가능
- FuriosaAI win: 국내 주요 민간 및 공공 중심의 GPUaaS 시장 내에 RNGD 가속기를 팩토리엑스 공식 하드웨어 제품군으로 안착시키는 전략적 성과
- 직접 판매 가능성: `LOW`
- CSP 경유 판매 가능성: `HIGH`
- NPUaaS 유도 가능성: `HIGH`
- CSP capacity 증설 가능성: `HIGH`
- 수치 근거: 없음
- 컨택 명분: 팩토리엑스 브랜드 인프라 포트폴리오 다각화를 위한 고성능 국산 AI 반도체 파트너십 구축 제안
- 실제 컨택 시 사용할 말: 새롭게 공개하신 초거대 실행 최적화 브랜드 팩토리엑스 소식을 기쁘게 접하였습니다. 대규모 가속 자원 관리 환경에서 운영 전력 리스크를 효과적으로 완화하고 뛰어난 경제성을 보장하는 고성능 추론 인프라 연계를 논의하고자 합니다.
- 매출 가능 시점: `단기`
- 담당자 후보 힌트: Head of Cloud, Head of Infrastructure, platform lead
- 공개 프로필 URL: 
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 팩토리엑스 포트폴리오 내 비엔비디아 계열 가속기 인터페이스 수용 계획 확인
- source_ids: S026, S027, S031
- source_urls: https://biz.newdaily.co.kr/site/data/html/2026/05/26/2026052600079.html | https://www.techm.kr/news/articleView.html?idxno=152127

### 3. KT클라우드

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `CSP 운영 기업`
- 분류: `priority_outreach`
- 확인된 프로젝트/시그널: 서울 가산 및 판교 데이터센터 가동률 상승에 따른 서비스형 GPU 매출 실적 성장세 본격화
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 기초 모델 정보는 파악되지 않았으나 수도권 주요 데이터센터의 전력 가용 상태를 모니터링하면서 상업용 GPUaaS 및 대안형 NPUaaS 인프라 증설을 지속 조율 중이므로 비즈니스 가치가 최상위 수준임
- hook_type: `CLOUD`
- 핵심 buying signal: 서울 가산 및 판교 등 핵심 데이터센터 가동 본격화 및 상업용 GPUaaS 시장 수요 성장 기조 확보
- 인프라 signal: 수도권에 분산 구축된 초고성능 AI 전용 데이터센터 자원 활용
- timing reason: 실적 발표를 기점으로 차세대 가속기 포트폴리오 조달을 체계적으로 조율하고 있는 적절한 비즈니스 시점임
- 고객 win: 전력 요구량이 매우 낮은 대체 가속 기기를 통해 폭증하는 GPUaaS 수요에 유연하게 대응하고 고객에게 매력적인 단가의 서빙 환경 제공 가능
- FuriosaAI win: KT클라우드의 주요 수도권 데이터센터 가용 구역 내에 RNGD 하드웨어를 직접 적용 및 연계 인프라 확충 기회 획득
- 직접 판매 가능성: `LOW`
- CSP 경유 판매 가능성: `HIGH`
- NPUaaS 유도 가능성: `HIGH`
- CSP capacity 증설 가능성: `HIGH`
- 수치 근거: KT클라우드 1분기 매출 2501억원 기록 (S028) — 근거: KT의 AI DC 사업을 담당하는 KT클라우드의 1분기 매출은 2501억원으로
- 컨택 명분: KT클라우드 전용 하드웨어 인프라 내 저전력·초고성능 추론 가속 옵션 추가를 위한 파트너십 논의
- 실제 컨택 시 사용할 말: 지속적인 성장세를 기록하고 있는 대규모 AI 인프라 사업 소식을 인상적으로 보았습니다. 전력 수급 압박이 큰 수도권 인프라 환경에서 랙 전력 밀도를 획기적으로 안정화하며 vLLM 서빙 최적화를 이루는 RNGD 도입에 대해 말씀 나누고자 합니다.
- 매출 가능 시점: `중기`
- 담당자 후보 힌트: Head of Cloud, Head of Infrastructure, platform lead
- 공개 프로필 URL: 
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 신규 데이터센터 내 저전력 가속 전용 랙 설계 현황 여부
- source_ids: S028
- source_urls: https://www.m-i.kr/news/articleView.html?idxno=1375542

### 4. 네이버클라우드

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `CSP 운영 기업`
- 분류: `priority_outreach`
- 확인된 프로젝트/시그널: 국가AI컴퓨팅센터 구축 참여 및 국내 6대 CSP 공동 전방위 대응 체계 가동
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 해남 국가 컴퓨팅 인프라 프로젝트 등 거대 데이터센터 사업을 공동 이행 중이며, 글로벌 외산 자원 수급 한계를 우회하고 대규모 클라우드 가속기 수요를 분산할 가속기 연계 가치가 강력하여 높은 우선순위를 유지함
- hook_type: `SCALE`
- 핵심 buying signal: 국책 초대형 컴퓨팅 센터 수주 활동 본격 참여 및 외산 수급난 대응 목적의 얼라이언스 연합 가동
- 인프라 signal: 해남 솔라시도 인프라 연동 국가 컴퓨팅 사업 및 자체 보유 대형 플랫폼 데이터센터
- timing reason: 국내 주요 CSP들과 연합 전선을 구성해 수급 이슈와 막대한 전력 요금 부담에 대응하려는 전략적 타이밍임
- 고객 win: 국가 핵심 연구 기관이나 스타트업들에게 전력망의 직접적 제약을 받지 않는 대용량 친환경 고효율 가속 컴퓨팅 자원을 공급 가능
- FuriosaAI win: 국가 주요 컴퓨팅 프로젝트 아키텍처 인프라 사양 내에 국산 가속기를 적용하여 독점적 레퍼런스를 획득하고 사업 영향력을 강화함
- 직접 판매 가능성: `LOW`
- CSP 경유 판매 가능성: `HIGH`
- NPUaaS 유도 가능성: `HIGH`
- CSP capacity 증설 가능성: `HIGH`
- 수치 근거: 없음
- 컨택 명분: 국책 컴퓨팅 인프라 고성능 저전력 추론 세그먼트 전용 하드웨어 공급 방안 협의
- 실제 컨택 시 사용할 말: 최근 대형 국책 AI 컴퓨팅 인프라 프로젝트 참여 소식을 매우 깊이 있게 접하였습니다. 글로벌 하드웨어 장벽 극복과 고집적 서빙 운영비 관리를 위해 친환경적인 고부하 추론 가속기 라인업 조달 방안을 제안 드립니다.
- 매출 가능 시점: `중기`
- 담당자 후보 힌트: Head of Infrastructure, platform lead, procurement department
- 공개 프로필 URL: 
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 해남 프로젝트 내 친환경 저전력 가속 하드웨어 도입 비율 설정 여부 | numeric_claims 미제공 상태에서 숫자성 표현이 포함됨: confirmed_project_or_signal
- source_ids: S029, S032, S033
- source_urls: https://www.ddaily.co.kr/page/view/2026052017342600376 | https://www.mt.co.kr/tech/2026/05/23/2026052210211399740

### 5. 광주 국가 AI데이터센터

- 국가: `KR`
- 시장: `B2G`
- 타깃 유형: `CSP 운영 기업`
- 분류: `priority_outreach`
- 확인된 프로젝트/시그널: 하반기 이용자 공식 모집 및 초고성능 컴퓨팅 자원 중심 인프라 배정
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `MID`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 사용 모델 아키텍처는 가변적이나 정부의 공공 컴퓨팅 풀 확충 목적에 전용 가속 자원을 공급할 직접적인 조달 입찰과 인프라 사업 기회가 확실하게 예측되어 높은 등급으로 배정함
- hook_type: `PROCUREMENT`
- 핵심 buying signal: 공공 중심 신규 초고성능 가속 클라우드 자원 확보를 위한 하반기 이용자 모집 프로그램 공표
- 인프라 signal: 정부 예산 기반의 고성능 대형 데이터센터 인프라 및 가속 클러스터 설비 가동
- timing reason: 하반기 정규 모집 사업 일정에 맞추어 사전에 인프라 고도화와 저전력 기기 구성 검토가 필요한 접촉 적기임
- 고객 win: 공공 연구 과제를 수행하는 스타트업들에게 상대적으로 할당 한계가 적고 vLLM 기반 가상화가 원활한 고집적 서빙 인프라 대량 분배 가능
- FuriosaAI win: 정부 및 공공 성격의 핵심 사업 실적 레퍼런스를 공식 선점하여 국내 공공 및 교육 조달 부문 신뢰성 지표 확보
- 직접 판매 가능성: `MID`
- CSP 경유 판매 가능성: `HIGH`
- NPUaaS 유도 가능성: `HIGH`
- CSP capacity 증설 가능성: `HIGH`
- 수치 근거: 광주 국가 AI데이터센터 최대 6PF 규모 HPC 자원 가동 (S005) — 근거: 특히 하반기 모집은 GPU와 최대 6PF(페타플롭스) 규모의 HPC 자원을 중심으로 운영돼
- 컨택 명분: 국가 컴퓨팅 자원 포트폴리오 고도화를 위한 초고효율 NPU 인프라 직접 납품 논의
- 실제 컨택 시 사용할 말: 하반기 대규모 자원 모집 소식을 보고 연락드렸습니다. 국가 AI 생태계에 할당할 고비용 인프라 운영 부담을 줄이면서 스타트업들에게 컨테이너 기반으로 탁월한 편의성을 제공할 수 있는 RNGD 하드웨어 도입 방안을 제시하고자 합니다.
- 매출 가능 시점: `단기`
- 담당자 후보 힌트: Head of Infrastructure, platform lead, procurement department
- 공개 프로필 URL: 
- 기존 접점: `확인 필요`
- B2G 근거 유형: `기사/RSS 기반`
- 나라장터 직접 확인: `미수행`
- 조달상 다음 액션: 나라장터/RFP 직접 확인 필요
- 확인 필요: 공공 예산 기반의 신규 가속기 인프라 구매 조달 입찰 공고 발표 여정
- source_ids: S005
- source_urls: https://www.jnilbo.com/news/articleView.html?idxno=90000037451

### 6. 우리은행

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `CSP 고객 기업`
- 분류: `cloud_npuaaS_lead`
- 확인된 프로젝트/시그널: 삼성SDS를 전용 금융 AI 에이전트 구축 프로젝트의 우선협상대상자로 공식 지정
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 개별 모델 정합성은 기재되지 않았으나 파트너 구축 주체인 삼성SDS의 인프라 및 SCP(삼성 클라우드 플랫폼)에 RNGD가 연계 적용될 경우 막대한 금융 AI 추론 사용량을 창출하여 CSP 추가 증설로 이어지는 강력한 GTM 기회가 확인되어 높은 평가를 배정함
- hook_type: `PARTNER`
- 핵심 buying signal: 전행 금융 AX 가동 및 지능형 에이전틱 자산 분석 워크플로우 전면 도입 결성
- 인프라 signal: 삼성SDS 주도 금융 프라이빗 망 혹은 SCP 플랫폼 연동 아키텍처 구조
- timing reason: 우선협상대상자 지정 직후 시스템 통합과 물리적 서버 배정 아키텍처 설계를 직접 조율하는 중요한 초기 타이밍임
- 고객 win: 보고서 생성 등 엄청난 컴퓨팅 부하를 요구하는 금융 상담 트래픽 상황에서 운영 보안을 유지하고 추론 서빙 인프라 유지비의 경제성을 확보할 수 있음
- FuriosaAI win: 삼성SDS 공급 채널 파트너십의 대표적인 1차 대형 금융권 성공 사례를 조기에 구축하는 전략적 기회 창출
- 직접 판매 가능성: `LOW`
- CSP 경유 판매 가능성: `HIGH`
- NPUaaS 유도 가능성: `HIGH`
- CSP capacity 증설 가능성: `MID`
- 수치 근거: 없음
- 컨택 명분: 구축사인 삼성SDS와 유기적으로 연계된 가속 최적화 고효율 하드웨어 활용 방안 기술 검토 제안
- 실제 컨택 시 사용할 말: 최근 차세대 AI 에이전트 프로젝트 소식을 뜻깊게 접하였습니다. 파트너사인 삼성SDS 인프라와 결합하여 대용량 자산 보고서 분석 등 지속적인 금융 부하를 획기적으로 조율하는 전력 및 인프라 안정화 방안을 제안합니다.
- 매출 가능 시점: `중기`
- 담당자 후보 힌트: CIO, Head of AI, platform lead
- 공개 프로필 URL: 
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 구축 진행 단계에서의 외부 클라우드 SCP 전용 가속기 망 직접 접근 한계 정보
- source_ids: S035, S036
- source_urls: https://www.sedaily.com/article/20046605?ref=naver

### 7. KB금융

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `온프레미스 기업`
- 분류: `watchlist`
- 확인된 프로젝트/시그널: 상시 작동형 보안 모니터링 에이전틱 아키텍처 및 내부 제로트러스트 방어망 구축
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `MID`
- 채널/CSP fit_score: `MID`
- RNGD fit_score: `LOW`
- outreach priority: `LOW`
- fit vs priority 설명: 사용 모델명이 명시되지 않았고 현재 온프레미스 서버를 대규모로 자체 조달하려는 수요 신호가 뚜렷하지 않은 상태이며, 모델-퍼스트 필터 기준에 따라 감시 대상으로 분류하여 안전하게 리스크를 방지함
- hook_type: `SOVEREIGN`
- 핵심 buying signal: 망분리 정책 기조 완화에 대응하는 금융 보안 모니터링 인프라 가동 및 이상징후 상시 자동 분석 인프라 설계
- 인프라 signal: 자자체 내부에 구축된 폐쇄망 기반 로컬 보안 인프라 구동
- timing reason: 전체적인 금융 보안 정책 방향성에 맞물려 AI 에이전트 중심의 내부 탐지 플랫폼을 실증하는 상황임
- 고객 win: 외부로 민감 금융 데이터가 노출되는 위협을 원천 봉쇄한 상황에서 고성능 내부 추론 전용 하드웨어 가속 성능 확보
- FuriosaAI win: 초기 레벨에서 망분리 금융 영역의 대표적 보안 실증 데이터 기반 구축을 위한 잠재 타겟 선점
- 직접 판매 가능성: `LOW`
- CSP 경유 판매 가능성: `MID`
- NPUaaS 유도 가능성: `MID`
- CSP capacity 증설 가능성: `LOW`
- 수치 근거: 없음
- 컨택 명분: 금융 상시 보안 및 제로트러스트 전용 로컬 저전력 서버 인프라 타당성 검토 제안
- 실제 컨택 시 사용할 말: 지속 가동 중이신 자체 보안 모니터링 플랫폼 성과 소식을 주의 깊게 보았습니다. 외부 통신이 원천 통제된 환경에서도 신속하고 경제적인 이상 탐지 추론 가속이 보장되는 RNGD 하드웨어의 설계 적합성을 제안 드립니다.
- 매출 가능 시점: `장기`
- 담당자 후보 힌트: CIO, Head of AI, Head of Infrastructure
- 공개 프로필 URL: 
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 보안 관제 엔진 내 소형 로컬 LLM 및 임베딩 모델의 오픈소스 호환 규격 파악 | 온프레미스/CSP 고객 후보 모델명 미확인 — 다음 사이클에서 모델 매칭 확인 필요
- source_ids: S001, S004, S011, S012, S013, S014
- source_urls: https://www.viva100.com/article/20260526500346 | https://www.lcnews.co.kr/news/articleView.html?idxno=202602

### 8. 서울아산병원

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `온프레미스 기업`
- 분류: `watchlist`
- 확인된 프로젝트/시그널: 응급 상황 처리 프로토콜 AI의 내부 폐쇄망 기반 온프레미스 작동 실증 검증 완료
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `MID`
- 채널/CSP fit_score: `LOW`
- RNGD fit_score: `LOW`
- outreach priority: `LOW`
- fit vs priority 설명: 폐쇄망 의료 임상 보조 가동 레퍼런스는 훌륭하나 구체적 전용 모델 미비 및 당장의 대량 서버 구축 조달 의사가 파악되지 않아 모델-퍼스트 우선순위 정책에 입각하여 중장기 모니터링 대상으로만 분류함
- hook_type: `SOVEREIGN`
- 핵심 buying signal: 디지털정보혁신본부가 리드하는 병원 내부 규제망 및 폐쇄 인프라 내부에서의 AI 서비스의 완전 구동 성공
- 인프라 signal: 사내 망분리 병원 정보 보안 시스템 인프라 유지
- timing reason: 의료 정보 가치 안전성 확보와 기술 실증 성과를 업계에 공식 표명한 시기임
- 고객 win: 환자 인적 기밀 유실 불안감을 완벽히 차단하며 가동 효율성이 뛰어난 컴팩트형 저전력 로컬 의료 보조 엔진 구성 가능
- FuriosaAI win: 최상급 의료기관의 소버린 헬스케어 가속기 시장 진출 가능성을 지속 추적하기 위한 거점 확보
- 직접 판매 가능성: `LOW`
- CSP 경유 판매 가능성: `LOW`
- NPUaaS 유도 가능성: `MID`
- CSP capacity 증설 가능성: `LOW`
- 수치 근거: 없음
- 컨택 명분: 폐쇄 인프라 내부 의료 정보 전용 저발열 고성능 소형 추론 시스템 로드맵 제안
- 실제 컨택 시 사용할 말: 성공적으로 발표된 응급 의료 AI 임상 실증 성과를 매우 기쁘게 접하였습니다. 민감 데이터 주권 통제 유지가 필수적인 임상 진단 현장에 알맞은 고효율 고출력 전용 가속 사양과의 유기적 연계를 추천 드립니다.
- 매출 가능 시점: `장기`
- 담당자 후보 힌트: CTO, Head of Digital Transformation
- 공개 프로필 URL: 
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 임상 프로토콜에 사용된 학습 모델 규격의 로컬 추론을 위한 최저 요구 메모리 폭 | 온프레미스/CSP 고객 후보 모델명 미확인 — 다음 사이클에서 모델 매칭 확인 필요
- source_ids: S016
- source_urls: https://www.newsis.com/view/NISX20260518_0003634573


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

1. **최명수 소프트제국 대표, 제61회 발명의 날 '산업포장' 수훈**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T11:05:00+09:00`
   - matched_query_or_feed: `공공 생성형 AI 구축`
   - url: https://www.etnews.com/20260526000178
   - summary_snippet: 공공·교육 분야 AI 평가 시스템 시장에서 기술 경쟁력을 확대하고 있다. SWAI for Scoring은 생성형 AI와 RAG... 신뢰서비스와 AI 기반 교육·평가 분야, AI 학습데이터 구축, AI 기반 Agent 자동화 서비스 분야의 인공지능...

2. **[미리보는 데이터센터 서밋] 〈2〉 발열 잡는 냉각 솔루션부터 스스로 치유하는 자율화 운영까지 - 전자신문**
   - source: `rss`
   - published_at_kst: `2026-05-26T11:04:15+09:00`
   - matched_query_or_feed: `Google News KR AI 데이터센터`
   - url: https://news.google.com/rss/articles/CBMiTkFVX3lxTFBzME9rTzNwaWJYTmU5TXJWZThLbzBmOUcwM0dvZ3Exajg4dVpTOGJHS21ScXo1eUNIOHNjbzlvUy1uZFNxaThKTEJmX21wZw?oc=5
   - summary_snippet: [미리보는 데이터센터 서밋] 〈2〉 발열 잡는 냉각 솔루션부터 스스로 치유하는 자율화 운영까지  전자신문

3. **인천TP, '스마트제조 AX 아카데미' 완료…AI 전환 지원 본격화**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T11:04:00+09:00`
   - matched_query_or_feed: `생성형 AI 도입 기업`
   - url: https://www.gukjenews.com/news/articleView.html?idxno=3591860
   - summary_snippet: 스마트공장 도입과 AI 전환(AX) 확산을 지원하기 위한 목적으로 마련됐다. 교육은 안산 중소벤처기업연수원에서 '스마트제조 AX를 위한 기본 개념 톺아보기'라는 주제로 진행됐으며, 제조 데이터의 중요성, 생성형 AI의...

4. **경희대-한국부동산원, ‘AI 및 데이터 기반 기술 협력·공공분야 혁신’...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T11:04:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://dhnews.co.kr/news/view/1065578352826116
   - summary_snippet: AX센터장, 박종현 데이터인프라팀장, 신현배 ICT운영부장 등 양 기관의 핵심 관계자가 참석했다. 양 기관은 협약에 따라 ▲AI, 데이터 분석 등 첨단 기술 분야 공동 연구 및 기술개발 ▲중앙정부 및 지자체 공모사업 공동...

5. **車 메모리는 마이크론이 1위···"국내 기업 진입 강화해 다운사이클 대...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T11:04:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.todaykorea.co.kr/news/articleView.html?idxno=402001
   - summary_snippet: 이 같은 차량용 메모리 수요 증가 전망과 함께 상대적으로 수익성이 큰 AI 데이터센터용 메모리 중심으로 공급이 이뤄져 자동차 산업에서도 '칩플레이션(반도체 가격 상승)'이 나타날 것으로 관측되고 있다. 다만...

6. **​SK하이닉스, 차세대 냉각 기술 'iHBM' 공개…​"칩 내부에 냉각길 뚫어...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T11:04:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.onews.tv/news/articleView.html?idxno=280651
   - summary_snippet: 고성능 컴퓨팅 및 AI 데이터센터 등 초고집적 환경에서 요구되는 엄격한 열 관리 기준을 충족시키겠다는 구상이다. 이강욱 SK하이닉스 부사장(PKG개발 담당)은 "iHBM은 당사의 메모리 설계 역량과 첨단 패키징 기술을...

7. **HBM 발열 잡았다...SK하이닉스, 신기술 공개**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T11:04:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.newsinside.kr/news/articleView.html?idxno=4705025
   - summary_snippet: 이를 통해 고성능 컴퓨팅(HPC), AI 데이터센터 등 초고집적·초고대역폭 환경에서 요구되는 열 관리 수준을 충족하며 시스템 전반의 안정성과 운영 효율을 높인다는 계획이다. 이강욱 SK하이닉스 부사장(PKG개발...

8. **코리아써키트·티엘비, AI 서버·고사양 메모리 기판 시장 성장 수혜 기...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T11:04:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.pinpointnews.co.kr/news/articleView.html?idxno=455284
   - summary_snippet: 글로벌 빅테크 기업들의 AI 데이터센터 투자 확대가 국내 반도체 밸류체인 전반에 긍정적인 영향을 미치고 있다는 평가다. 한국거래소에 따르면 이날 ISC와 코리아써키트, 티엘비가 테마 상승을 이끌고 있다. ISC는...

9. **"AI 공격은 AI로 방어"…금융권 망분리 규제 예외 적용**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T11:04:00+09:00`
   - matched_query_or_feed: `AI 상담 에이전트`
   - url: http://www.4th.kr/news/articleView.html?idxno=2112222
   - summary_snippet: 특히 스스로 탐색·판단·실행하는 에이전트형 AI가 보안 취약점 탐지와 공격 실행을 자동화할 수 있다는... 전면 해제가 이뤄질 경우 해당 금융회사는 AI 기반 보안체계 구축뿐 아니라 챗봇 상담, 자산관리, 여신심사...

10. **"인터넷 사용 시간 5% 줄었고 AI는 빠른 성장세"**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T11:04:00+09:00`
   - matched_query_or_feed: `금융 생성형 AI`
   - url: https://theopiniontimes.news/%ec%9d%b8%ed%84%b0%eb%84%b7-%ec%82%ac%ec%9a%a9-%ec%8b%9c%ea%b0%84-5-%ec%a4%84%ec%97%88%ea%b3%a0-ai%eb%8a%94-%eb%b9%a0%eb%a5%b8-%ec%84%b1%ec%9e%a5%ec%84%b8/
   - summary_snippet: 글로벌 웹 트래픽이 2025년 처음으로 감소세로 돌아선 가운데, 생성형 AI 플랫폼만이 이 흐름을 거슬렀다.... 분야가 가장 높은 비중을 차지했으며, 뉴스(10%), 법률·정부(9%), 블로그(7%), 쇼핑(6%), 금융 서비스(5%) 순이었다.

11. **마이허브, 의료 AI 통합 플랫폼 앞세워 글로벌 플랫폼 시장 정조준**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T11:04:00+09:00`
   - matched_query_or_feed: `병원 AI 플랫폼`
   - url: http://www.doctorstimes.com/news/articleView.html?idxno=238212
   - summary_snippet: 채택했다"며 "병원 내부에서는 암호화 및 비식별화, 데이터 정규화만 수행하고 무거운 AI 분석은 클라우드에서 처리해 초기 도입 비용을 획기적으로 낮췄다"고 설명했다. 현재 플랫폼에는 루닛, 뷰노, 뉴로핏 등 20개...

12. **R&D 심의에 노인 돌봄까지… 'K-AI' 공공행정 등 전방위 확산**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T11:04:00+09:00`
   - matched_query_or_feed: `클라우드 AI 서비스`
   - url: https://www.newscj.com/news/articleView.html?idxno=3403903
   - summary_snippet: 서비스 중이며 치매 어르신의 우울감을 낮추고 기억 기능을 향상시켰다는 연구 결과가 국제 학술지에 게재되기도 했다. 이에 대해 옥상훈 네이버클라우드 네이버 케어콜 사업전략 리더는 "네이버 케어콜은 AI가 독거...

13. **[더벨][상장 2년 HD현대마린솔루션] 신성장축 '전력용 엔진·FSRU 개조'**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T11:02:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.thebell.co.kr/free/content/ArticleView.asp?key=202605211607121280106733
   - summary_snippet: AI 산업이 새롭게 열리면서 AI 데이터센터의 전력 수요가 급증하고 있어, 발전용 엔진의 유지보수 시장의 성장세도 탄탄할 것이란 시각에서다. 선박 대형엔진의 회전 동력을 활용해 전기를 생산하는 ‘축 발전기(Shaft...

14. **S-OIL, AI 데이터센터 '열 관리' 시장 공략… 액침냉각 실증 테스트 추진**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T11:02:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.ilyoseoul.co.kr/news/articleView.html?idxno=517533
   - summary_snippet: S-OIL, 어니언소프트웨어, GST, 웰메이드컴퓨터 관계자들이 어니언소프트웨어 기흥 AI데이터센터에서 데이터센터 액침냉각 실증 추진 기념촬영을 하고 있다. [홍보팀] S-OIL이 AI 데이터센터 '열 관리' 시장을 공략하기...

15. **SK하이닉스, HBM 발열 잡는 'iHBM' 공개 … AI 메모리 경쟁, 속도 넘어 냉...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T11:02:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://biz.newdaily.co.kr/site/data/html/2026/05/26/2026052600124.html
   - summary_snippet: AI 데이터센터처럼 장시간 대규모 연산이 이어지는 환경에서는 발열 제어가 성능 유지, 전력 효율, 냉각 비용을 좌우하는 핵심 요소다. 양산성과 고객 적용 편의성도 강조됐다. SK하이닉스는 iHBM에 Advanced MR-MUF 기반...

16. **[단독] 기업 AI 전략 논의한다는 한경협 … 실상은 '골프·관광·연예인...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T11:02:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://biz.newdaily.co.kr/site/data/html/2026/05/26/2026052600096.html
   - summary_snippet: 이세돌 전 바둑기사는 'AI를 이긴 유일한 인간, 그리고 그 이후의 질문'을 주제로 강연하며, 백준호 퓨리오사AI 대표는 AI 인프라와 데이터센터 경쟁을 주제로 발표에 나선다. 이 밖에도 에이블리·뤼튼테크놀로지스...

17. **[제약+] 셀트리온, '신약개발·제조·사무' AI 도입 박차 外**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T11:02:00+09:00`
   - matched_query_or_feed: `병원 AI 플랫폼`
   - url: https://dealsite.co.kr/articles/162448
   - summary_snippet: 이달 들어 회사는 농림축산식품부가 주관하는 '칸나비디올 원료의약품 플랫폼 개발 및 원료 재배 기술... ◆뉴로핏, 스페인 발데브론과 '뉴로핏 아쿠아 MS' 공동 연구 진행 뉴로핏이 스페인 발데브론대학병원 산하...

18. **'강원-공급망 플랫폼, 전북-RE100 산단, 제주-관광 활성화'가 숙제**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T11:02:00+09:00`
   - matched_query_or_feed: `제조 AI 플랫폼`
   - url: http://www.kbiznews.co.kr/news/articleView.html?idxno=114203
   - summary_snippet: 통합 플랫폼과 연동하는 방안이 제시됐다. 결국 강원경제가 한 단계 도약하기 위해서는 미래산업 육성과 지역 중소기업 경쟁력 강화가 함께 이뤄져야 한다. 제조업의 공급망 대응력과 AI 전환 역량을 높이고, 관광...

19. **KB금융, AI 사이버 공격 AI로 대응하는 보안 체계 강화**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T11:02:00+09:00`
   - matched_query_or_feed: `클라우드 AI 서비스`
   - url: http://www.techholic.co.kr/news/articleView.html?idxno=221361
   - summary_snippet: 특히 그룹 클라우드 환경에 대한 제로트러스트 3단계 구축 완료 사례는 금융업권에서 가장 선제적 구축 사례로 평가받고 있다. 아울러 지난해 3월 수립한 AI 거버넌스를 바탕으로 AI 서비스 수명주기 전 단계에서 31개...

20. **李대통령 "냉엄한 국제 현실 맞서 국방력 강화해야…핵잠 도입·전작권...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T11:02:00+09:00`
   - matched_query_or_feed: `국방 AI 인프라`
   - url: https://www.polinews.co.kr/news/articleView.html?idxno=732218
   - summary_snippet: 이 대통령은 "인공지능(AI)과 드론 기술 도입을 가속화하고 미래 국방력 핵심 전략자산인 핵잠 도입에 속도를... 물류 인프라, 탄탄한 배후지를 갖춘 동남권은 세계적인 해양 경제권으로 성장할 충분한 잠재력을 가진 지역...


## 다음 단계

1. LLM 후보 품질 확인
2. 노이즈가 많으면 NAVER_QUERIES / RSS_FEEDS 개선
3. 후보가 너무 적으면 MAX_LLM_SOURCES 상향
4. Gemini 3.5 Flash vs 2.5 Flash 품질 비교
5. 나라장터/B2G 수집 추가
6. 담당자/의사결정자 탐색 추가
7. Notion 또는 Google Docs 업로드 추가
