# FuriosaAI GTM Research Agent Test Run

## 실행 정보

- run_id: `2026-05-26_021258_test_v0.8-g2b-operation-test`
- mode: `test`
- memo: `v0.8-g2b-operation-test`
- executed_at_kst: `2026-05-26T02:22:19.444078+09:00`
- agent_version: `v0.7`
- instructions_loaded_chars: `21592`
- naver_sources_recent_7d_count: `194`
- rss_sources_recent_7d_count: `100`
- merged_sources_recent_7d_count: `294`
- furiosa_docs_successful: `11`
- furiosa_docs_failed: `0`
- llm_called: `True`
- llm_error: ``

## 현재 단계

이 실행은 v0.7 테스트입니다.

이번 버전에서는 네이버 뉴스 API, RSS feed, FuriosaAI 공개 개발자 문서를 수집한 뒤 Gemini로 GTM 후보를 1차 평가하고, 별도 LLM 호출로 매니저용 gtm_report.md를 작성합니다.

아직 나라장터 직접 API, 담당자 심화 탐색, Notion 업로드는 수행하지 않았습니다.

## LLM 실행 요약

- overall_assessment: 최근 7일간의 국내 GTM 신호 조사 결과, 삼성SDS의 대규모 AI 데이터센터 투자 및 전력 확보 계획과 엘리스그룹의 코스닥 상장예비심사 청구에 따른 GPUaaS 인프라 확장 등 고유한 인프라 기회가 포착되었습니다. 또한 LG AI연구원의 EXAONE-4.0 모델 공식 precompiled 정합성을 바탕으로 한글과컴퓨터와의 공공 AX 에이전트 연합, 전남소방본부의 Solar LLM 기반 재난 안전 플랫폼 등 즉각적인 POC 및 수주 대응이 가능한 단기 매출 기회들이 식별되어 정밀한 BD 우선 접촉이 요구됩니다.
- top_priority_names: 삼성SDS, 엘리스그룹, 한글과컴퓨터, 에코아이티
- noise_ratio_comment: 공개 기사 분석 중 망분리 완화에 대한 일반론적인 금융 정책 뉴스 및 자국 가속기를 탑재한 해외 알리바바 동향 등 직접적인 타겟 가치가 부재한 노이즈 기사들이 일부 혼재되어 분류 과정에서 정리하였습니다.
- model_compatibility_caution: EXAONE 계열의 경우 4.0 버전은 공식 precompiled 호환 대상이지만, 농협은행 사례에서 언급되는 EXAONE 3.5 모델 등은 family_only에 해당하므로 정밀한 아키텍처 호환성 검증 단계가 필수적입니다.

## LLM 후보 평가 결과

## 버전 1 — B2B only 우선 검토 요약

- 삼성SDS / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- 엘리스그룹 / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- 한글과컴퓨터 / 온프레미스 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- NHN클라우드 / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- LG AI연구원 / CSP 운영 기업 / classification: `priority_outreach` / fit: `HIGH` / outreach: `HIGH` / 매출시점: `단기`
- NH농협은행 / 온프레미스 기업 / classification: `structure_check` / fit: `MID` / outreach: `MID` / 매출시점: `중기`
- 우리은행 / CSP 고객 기업 / classification: `cloud_npuaaS_lead` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`


## 버전 2 — B2B + B2G 우선 검토 요약

- 삼성SDS / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- 엘리스그룹 / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- 한글과컴퓨터 / 온프레미스 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- 에코아이티 / 온프레미스 기업 / classification: `priority_outreach` / fit: `HIGH` / outreach: `HIGH` / 매출시점: `단기` / B2G 근거: `나라장터/RFP 확인` / 나라장터 확인: `확인 완료`
- NHN클라우드 / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- LG AI연구원 / CSP 운영 기업 / classification: `priority_outreach` / fit: `HIGH` / outreach: `HIGH` / 매출시점: `단기`
- 건강보험심사평가원 / 온프레미스 기업 / classification: `structure_check` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기` / B2G 근거: `나라장터/RFP 확인` / 나라장터 확인: `확인 완료`
- NH농협은행 / 온프레미스 기업 / classification: `structure_check` / fit: `MID` / outreach: `MID` / 매출시점: `중기`
- 우리은행 / CSP 고객 기업 / classification: `cloud_npuaaS_lead` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`


## 상세 후보 평가

### 1. 삼성SDS

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `CSP 운영 기업`
- 분류: `priority_outreach`
- 확인된 프로젝트/시그널: 경북 구미 및 경기 동탄 데이터센터 인프라 확충에 따른 고전력 부담 극복 및 SCP 클라우드 AI 비즈니스 확대
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 구체적인 지원 모델 정보는 불명확하여 모델 정합성은 UNKNOWN으로 분류되나, 구미 60MW 및 동탄 20MW 전력 인프라 확대와 국내 핵심 CSP 파트너십 가치를 종합 고려해 삼성SDS 맞춤형 가속기 운영 기회로 평가하여 최고의 우선순위로 책정함.
- hook_type: `POWER`
- 핵심 buying signal: 경북 구미 AI 데이터센터 대규모 투자를 확정하고 동탄 데이터센터의 전력 확보를 마쳐 가속 인프라 기획을 강화하고 있음.
- 인프라 signal: 구미 데이터센터에 4273억원을 투자하여 60MW 규모의 전력을 기획 중이며, 동탄 데이터센터 서관 운영을 위해서도 20MW급 전력을 확보하는 등 고전력 부담이 커지는 환경임.
- timing reason: 대규모 인프라 투자 발표와 연계하여 저전력 추론 최적화 가속기 제안을 본격화할 수 있는 적절한 도입 설계 단계임.
- 고객 win: 데이터센터 전력 및 에너지 비용 급등 상황에서 전력 대 성능비가 우수한 RNGD를 동사 인프라에 도입함으로써 고가 GPU 위주 구성의 마진 압박을 개선하고 원가 경쟁력을 다질 수 있음.
- FuriosaAI win: 국내 최고 수준의 대형 CSP 파트너 채널을 공고히 선점하여 동사 클라우드를 통해 대형 그룹사 및 금융권으로 RNGD 기반의 간접 수요와 추가 서버 공급 계약을 대량 창출함.
- 직접 판매 가능성: `MID`
- CSP 경유 판매 가능성: `HIGH`
- NPUaaS 유도 가능성: `HIGH`
- CSP capacity 증설 가능성: `HIGH`
- 수치 근거: 경북 구미 4273억원 투자, 60MW 규모 AI 데이터센터 (S010) — 근거: 삼성SDS는 경북 구미에 4273억원을 투자해 60MW 규모 AI 데이터센터를 짓기로 했다. | 동탄 데이터센터 20MW급 전력 확보 (S003) — 근거: 삼성SDS가 경기 동탄 데이터센터 서관 가동을 위해 20MW급 전력을 확보한 사례도 이런 상황을 보여준다.
- 컨택 명분: 전력 확보 부담 완화 및 고전력 가속기 대체 포트폴리오 기획에 맞추어 저전력 추론 하드웨어 제안
- 실제 컨택 시 사용할 말: 최근 경북 구미 60MW 규모 신규 데이터센터 투자 및 동탄 전력 확보 발표 소식을 접하고 연락드렸습니다. 데이터센터 전력 수급과 에너지 원가 부담이 심화되는 시점에서, 동사 클라우드 인프라의 TCO를 극적으로 절감할 수 있는 저전력 가속기 RNGD 적용 방안을 보고드리고자 합니다.
- 매출 가능 시점: `단기`
- 담당자 후보 힌트: CTO, Head of Cloud, Head of Infrastructure, Head of Data Center
- 공개 프로필 URL: https://www.linkedin.com/company/samsung-sds
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 경북 구미 및 동탄 데이터센터 내 RNGD 가상화 규격 검토 가능 여부
- source_ids: S003, S010, S039
- source_urls: https://www.e-science.co.kr/news/articleView.html?idxno=130004 | https://www.mt.co.kr/tech/2026/05/23/2026052210211399740 | https://www.sedaily.com/article/20047365?ref=naver

### 2. 엘리스그룹

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `CSP 운영 기업`
- 분류: `priority_outreach`
- 확인된 프로젝트/시그널: 코스닥 시장 상장을 통한 자금 확보 및 자체 모듈형 데이터센터(PMDC) 중심의 GPUaaS 사업 전면 확장
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 특정 도입 모델명이 확인되지 않아 모델 적합도는 UNKNOWN이나, 코스닥 상장과 맞물려 자체 이동식 모듈형 데이터센터 인프라 포트폴리오를 빠르게 확장하는 선도적인 AI 인프라 파트너이므로 최우선 영업 접촉이 권장됨.
- hook_type: `CLOUD`
- 핵심 buying signal: 한국거래소에 상장예비심사청구서를 제출하며 본격적인 AI 클라우드 인프라 인프라스트럭처 선점과 고도화 의지를 피력함.
- 인프라 signal: 자체 이동식 모듈형 데이터센터(AI PMDC) 인프라 및 대규모 GPUaaS 관리 시스템을 독자 구축하여 구동하고 있음.
- timing reason: 기업공개(IPO) 추진으로 시장 입지 제고와 추가 투자가 예정된 최적의 인프라 전환 도입 제휴 시점임.
- 고객 win: 동사가 강점으로 삼는 소형 모듈형 데이터센터의 제한된 공간 및 전력 환경에서, 에너지 절감형 RNGD 가속기를 채택하여 동일 상면당 추론 가용량을 높이고 원가를 낮출 수 있음.
- FuriosaAI win: 상장 준비 단계의 파격적이고 유연한 성장 파트너를 확보하여, 동사가 운영하는 GPUaaS 생태계 전반에 RNGD를 선탑재 공급하는 성과를 도출함.
- 직접 판매 가능성: `HIGH`
- CSP 경유 판매 가능성: `MID`
- NPUaaS 유도 가능성: `HIGH`
- CSP capacity 증설 가능성: `HIGH`
- 수치 근거: 없음
- 컨택 명분: 이동식 데이터센터 및 GPUaaS 인프라 확장을 겨냥한 저전력 고가성비 국산 추론 가속기 라인업 추가 제안
- 실제 컨택 시 사용할 말: 최근 코스닥 상장예비심사 신청과 함께 풀스택 AI 인프라 사업 강화를 선언하신 소식을 기쁘게 접했습니다. 동사의 주력 제품군인 이동식 모듈형 데이터센터 내의 전력 효율을 개선하고 가속기 가격 압박을 타개할 수 있는 대안으로 RNGD 하드웨어 테스트 기회를 상호 논의해 보고자 합니다.
- 매출 가능 시점: `단기`
- 담당자 후보 힌트: 김재원 대표이사, CTO, Head of AI Cloud Unit
- 공개 프로필 URL: https://www.linkedin.com/company/international-data-center-authority-idca
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 엘리스 모듈형 데이터센터 인프라 내부의 전력 밀도 및 하드웨어 폼팩터 실질 규격
- source_ids: S013, S014, S015, S017
- source_urls: http://www.hansbiz.co.kr/news/articleView.html?idxno=839792 | http://www.joseilbo.com/news/news_read.php?uid=568639&class=53&grp= | https://www.fetv.co.kr/news/articleView.html?idxno=302765 | https://www.newspim.com/news/view/20260520000146

### 3. 한글과컴퓨터

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `온프레미스 기업`
- 분류: `priority_outreach`
- 확인된 프로젝트/시그널: LG AI연구원과의 동맹을 기반으로 한 챗엑사원 결합 AI 문서 에이전트 출시 및 공공 AX 조달 시장 수주전 본격 진입
- 확인된 모델명: `EXAONE`
- 모델 매칭 상태: `family_only`
- 모델 fit_score: `MID`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: EXAONE-4.0 모델은 FuriosaAI에 공식 지원 및 프리컴파일 가속이 가능하나, 구체적인 연동 버전은 아키텍처에 따라 조율이 필요한 패밀리군에 머물러 MID로 평가함. 단, 공공기관 및 부처 중심의 폐쇄망 영업력이 매우 탄탄하여 상업적 우선순위는 HIGH로 상향함.
- hook_type: `SOVEREIGN`
- 핵심 buying signal: LG AI연구원과의 동맹 협약을 통해 자사 문서 에이전트와 초거대 모델 '챗엑사원'을 밀접하게 결합하여 정부부처 및 공공기관에 수주를 대응하겠다고 명확히 밝혔음.
- 인프라 signal: 주요 타겟이 망분리 및 정보 주권이 강하게 걸린 공기업과 지자체이며, 프라이빗 온프레미스 혹은 온디바이스형 AI 어플라이언스 수주를 지향함.
- timing reason: 협력 발표 이후 각 공공부처의 예산 심사 및 실행형 조달 프로젝트 발주가 본격화되어, 연계 솔루션 아키텍처를 사전에 구성해야 하는 시기임.
- 고객 win: 엄격한 공공기관의 폐쇄망 규제를 충족하며, LG AI연구원 모델 가속이 기 검증된 고효율 국산 가속기를 자사 패키지에 통합 구성함으로써 공공 납품 예산 경쟁력에서 절대적 우위를 점할 수 있음.
- FuriosaAI win: 동사의 강력한 공공 AX 수주 전선에 가속 엔진 파트너로 협력 연동함으로써, 대규모 공공 행정 문서 AI 서빙 시스템에 RNGD를 일괄 침투시키는 성과를 획득함.
- 직접 판매 가능성: `MID`
- CSP 경유 판매 가능성: `MID`
- NPUaaS 유도 가능성: `LOW`
- CSP capacity 증설 가능성: `LOW`
- 수치 근거: 없음
- 컨택 명분: 공공 행정망 전용 문서 AI 어플라이언스 구성 및 최적화 연계를 위한 RNGD 공동 가속 하드웨어 제휴 제안
- 실제 컨택 시 사용할 말: 한컴의 문서 에이전트와 LG AI연구원 챗엑사원 결합 솔루션의 공공 공략 발표를 관심 있게 모니터링해왔습니다. 공공부처 온프레미스 구축 시 인프라 예산 문턱을 획기적으로 개선하며, 이미 엑사원-4.0 서빙이 최적화 완료된 RNGD를 활용하여 공공 AX 수주 승률을 높이는 협력 방안을 제안드리고자 합니다.
- 매출 가능 시점: `단기`
- 담당자 후보 힌트: CTO, Head of Public Sector Sales, Head of AI Platform
- 공개 프로필 URL: https://www.linkedin.com/company/pointsharp-ab
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 챗엑사원 패키지 서빙 엔진의 vLLM 호환성 상태 검증
- source_ids: S021, S022, S023, S025
- source_urls: http://www.newslock.co.kr/news/articleView.html?idxno=130504 | https://www.mt.co.kr/tech/2026/05/22/2026052215283358675 | https://www.mk.co.kr/article/12055579 | https://www.newsis.com/view/NISX20260522_0003640664

### 4. 에코아이티

- 국가: `KR`
- 시장: `B2G`
- 타깃 유형: `온프레미스 기업`
- 분류: `priority_outreach`
- 확인된 프로젝트/시그널: 전남소방본부 AI 기반 재난 대응 플랫폼 구축 사업 본격 수주에 따른 Solar LLM 기반 시스템 전개
- 확인된 모델명: `Solar 1.0`
- 모델 매칭 상태: `exact_supported`
- 모델 fit_score: `HIGH`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `MID`
- RNGD fit_score: `HIGH`
- outreach priority: `HIGH`
- fit vs priority 설명: 도입에 나서는 Solar LLM(SOLAR-10.7B 등) 모델 계열은 FuriosaAI 공개 문서상 공식 지원 및 precompiled 검증이 완비된 exact_supported 유형이며, 소방 인프라의 실시간 반응에 초저지연 하드웨어 최적화 정합성이 완벽하여 최우선 순위로 조준함.
- hook_type: `PROCUREMENT`
- 핵심 buying signal: 전남소방본부 전용의 RAG 기반 소방 행정 및 재난 대응 플랫폼 구축 사업자로 최종 수주되어 본격 착수를 예고함.
- 인프라 signal: 쿠버네티스(K8s) 기반의 클라우드 구조와 업스테이지의 Solar 엔진을 적용하여 대량의 구조 문서를 정밀 처리하는 실 구축 인프라임.
- timing reason: 전남소방본부의 실 구축 인프라 서버 및 클라우드 플랫폼 아키텍처 구성을 최종 조율하는 초기 구축 국면임.
- 고객 win: 긴박한 재난 분석 현장에서 소방대원에게 지연 없이 가동되는 초고속 추론 환경을 제공하며, 쿠버네티스 환경에 드롭인 연동되어 도입 후 신속한 서빙 스택 배포가 완벽히 보장됨.
- FuriosaAI win: 소방 및 안전 재난 관리 시스템의 국가 인프라 구축 핵심 트랙에 RNGD를 공식 채택시켜 중장기 다른 지자체 소방본부 확장의 결정적 선례를 선점함.
- 직접 판매 가능성: `HIGH`
- CSP 경유 판매 가능성: `LOW`
- NPUaaS 유도 가능성: `LOW`
- CSP capacity 증설 가능성: `LOW`
- 수치 근거: 없음
- 컨택 명분: 쿠버네티스 구조 및 Solar LLM 구동을 지원하는 최첨단 국산 가속기 RNGD 적용 논의
- 실제 컨택 시 사용할 말: 최근 전남소방본부의 지능형 재난 대응 플랫폼 구축 사업 수주 성공을 지심으로 축하드립니다. 본 사업에 도입되는 Solar LLM은 당사의 RNGD에서 완벽히 구동이 지원되며, 네이티브 쿠버네티스 및 최적화 서빙 솔루션을 통해 재난 안전 플랫폼의 실시간 연산 성능과 시스템 가용 비용을 대폭 개선할 수 있습니다.
- 매출 가능 시점: `단기`
- 담당자 후보 힌트: CTO, Project Manager, Platform Infrastructure Lead
- 공개 프로필 URL: https://www.linkedin.com/company/wnsprocurement/
- 기존 접점: `확인 필요`
- B2G 근거 유형: `나라장터/RFP 확인`
- 나라장터 직접 확인: `확인 완료`
- 조달상 다음 액션: 나라장터/RFP 직접 확인 필요
- 확인 필요: 전남소방본부 소유 온프레미스 인프라 구동용 하드웨어 단독 발주 방식 확인
- source_ids: S029
- source_urls: https://magazine.hankyung.com/business/article/202605196285b

### 5. NHN클라우드

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `CSP 운영 기업`
- 분류: `priority_outreach`
- 확인된 프로젝트/시그널: 초거대 GPU 클러스터 및 AI 가속 클라우드 비즈니스 추진 및 인프라 고도화
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 구체적인 추론 타겟 모델 사양은 불확실해 UNKNOWN이나, 국내 CSP 얼라이언스 중추 멤버이며 초거대 규모의 가속 클러스터를 전략적으로 확장하고 있어 가속기 탑재 가능성이 극도로 커 HIGH로 분석함.
- hook_type: `CLOUD`
- 핵심 buying signal: 동종 CSP와의 에너지 절감 및 GPU난 해결 공동 연대 선언과 함께 이노그리드 인수를 토대로 한 독자 AI 클라우드 확장 공세를 시작함.
- 인프라 signal: 광주 등에 가속 전용 초대형 데이터센터 인프라를 확장해 가동 중이며 전력 비용 부담을 최소화할 하드웨어가 필요함.
- timing reason: 인수합병 마무리 및 신년 기자간담회 전개에 이어 인프라 공급 다각화 결정이 구체화되는 최상의 접촉 적기임.
- 고객 win: 데이터센터 에너지 요금 급등 압박 하에서, 전력 밀도 및 냉각 효율이 검증된 RNGD를 활용하여 가속 서비스 운용 비용을 크게 아끼고 고객 가성비 NPUaaS 라인업을 활성화할 수 있음.
- FuriosaAI win: 국내 주요 대형 CSP 파트너와 공동 연대를 구축하고, 동사 클라우드를 채택하려는 많은 엔터프라이즈에 RNGD 가속기를 대폭 전파하는 매출 교두보 확보함.
- 직접 판매 가능성: `MID`
- CSP 경유 판매 가능성: `HIGH`
- NPUaaS 유도 가능성: `HIGH`
- CSP capacity 증설 가능성: `HIGH`
- 수치 근거: 없음
- 컨택 명분: 대규모 인프라 전력 최적화 및 신규 저전력 NPUaaS 상품 출시를 위한 비즈니스 모델 파트너십 구축
- 실제 컨택 시 사용할 말: 최근 NHN클라우드의 독자적인 이노그리드 통합 및 초거대 가속기 클러스터 사업 다각화 계획을 기쁘게 들었습니다. 폭발적인 클라우드 가속기 수요 대응 과정에서, GPU 대안으로 전력 효율이 매우 뛰어난 국산 RNGD를 동사 NPUaaS 서비스에 정식 포함시키는 방안을 공동 논의해 보고자 합니다.
- 매출 가능 시점: `단기`
- 담당자 후보 힌트: CTO, Head of Infrastructure Division, Head of AI Business
- 공개 프로필 URL: https://www.linkedin.com/company/data-center-map/
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: NHN클라우드 통합 인프라 내 RNGD 가상화 솔루션 지원 상태 검토
- source_ids: S005, S031
- source_urls: https://www.ddaily.co.kr/page/view/2026052017342600376 | https://www.ddaily.co.kr/page/view/2026052216371975959

### 6. LG AI연구원

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `CSP 운영 기업`
- 분류: `priority_outreach`
- 확인된 프로젝트/시그널: EXAONE-4.0 모델 기반 휴머노이드 파운데이션 모델 고도화 및 공공 AX 동맹 강화
- 확인된 모델명: `EXAONE-4.0`
- 모델 매칭 상태: `exact_supported`
- 모델 fit_score: `HIGH`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `HIGH`
- outreach priority: `HIGH`
- fit vs priority 설명: EXAONE-4.0-32B가 FuriosaAI에 precompiled 및 공식 지원 대상으로 안착되어 기술 정합도상 HIGH 등급을 보장하며, 실제 GTM 협력과 다수의 기업 고객을 이미 공유하는 고부가가치 타겟이므로 최고의 영업 관리를 유지함.
- hook_type: `VLLM`
- 핵심 buying signal: 국책 과제 주도로 엑사원 탑재 K-휴머노이드 모델 확장을 예고하고, 자사 초거대 '챗엑사원'의 공공기관 납품 제휴를 다각화하기 시작함.
- 인프라 signal: K-휴머노이드 연구단의 대용량 행동 가속 및 챗엑사원 전술망 서빙 아키텍처 인프라를 자체 수급하고 설계하는 중임.
- timing reason: 국책 국방/로보틱스 사업 3차년도 이행 시점과 공공 AX 부처 공동 낙찰 협력이 동시다발적으로 개시된 골든 타임임.
- 고객 win: 자체 연구한 거대 아키텍처를 추론 최적화 하드웨어에 다이렉트 연동시켜 연산 반응성과 전력 밀도를 극대화하고 전반적인 GPU 보유 비용을 대폭 개선함.
- FuriosaAI win: 강력한 파운데이션 모델 개발 연합을 완성하고, EXAONE 구동의 표준 레퍼런스 가속기로 동반 안착해 생태계적 영향력을 압도적으로 장악함.
- 직접 판매 가능성: `HIGH`
- CSP 경유 판매 가능성: `MID`
- NPUaaS 유도 가능성: `LOW`
- CSP capacity 증설 가능성: `LOW`
- 수치 근거: K-휴머노이드 국책 사업 3차년도에 비디오캡처 기반 인터페이스 도입 (S027) — 근거: 3차년도에는 비디오캡처 기반 인터페이스를 도입해 착용 장비 없이도 다수 사용자가 데이터 수집에 참여할...
- 컨택 명분: 엑사원 4.0 모델의 연산 성능 극대화 및 차세대 로보틱스 전용 서버 인프라에 RNGD 탑재 논의
- 실제 컨택 시 사용할 말: 귀원의 국책 K-휴머노이드 착수와 공공 챗엑사원 서비스 확장 성과를 매우 기쁘게 지켜보고 있습니다. 당사의 RNGD 가속기는 EXAONE-4.0 연동 성능이 이미 검증되었으므로, 실시간 대화형 서비스 및 연구 단말용 초고속 저지연 추론 인프라 최적화 방안을 함께 실현해 가고자 합니다.
- 매출 가능 시점: `단기`
- 담당자 후보 힌트: CTO, Head of AI Research, Project Lead
- 공개 프로필 URL: https://www.linkedin.com/company/physical-intelligence
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 휴머노이드 데이터 수집 및 실시간 제어에 들어가는 구체적 하드웨어 폼팩터 형태
- source_ids: S021, S027, S039
- source_urls: http://www.newslock.co.kr/news/articleView.html?idxno=130504 | https://www.ddaily.co.kr/page/view/2026052016512856045 | https://www.sedaily.com/article/20047365?ref=naver

### 7. 건강보험심사평가원

- 국가: `KR`
- 시장: `B2G`
- 타깃 유형: `온프레미스 기업`
- 분류: `structure_check`
- 확인된 프로젝트/시그널: 디지털클라우드센터 기반 독자 AI 통합 플랫폼 구축 추진 및 원스톱 서비스 체계 기획
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `MID`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 사용 모델 사양은 명확히 드러나지 않아 UNKNOWN이나, 공공 핵심 의료기관으로서 자체 디지털클라우드센터 내 GPU 기반 독자적인 서버 및 원스톱 개발 AI 플랫폼 가동을 선언했으므로 인프라 및 바이어 신호가 매우 강력해 HIGH로 평가함.
- hook_type: `PROCUREMENT`
- 핵심 buying signal: 디지털전략실장이 지휘하는 'AI·클라우드 동시 드라이브' 계획을 발표하며, 기관 내부 GPU 서버 기반의 독자 AI 서비스 구축 계획을 천명함.
- 인프라 signal: 대국민 의료기관 탐색 등을 위한 자체 디지털클라우드센터 기반의 연산 인프라 기획 수립 상태임.
- timing reason: 전략적 평가기관 전환이라는 공공 목표 기정 사실화에 따라 대규모 서버 장비의 조달 계획 수립이 예정된 타이밍임.
- 고객 win: 민감한 공공 보건 의료 데이터를 온프레미스로 철저히 보호하는 동시에, 국산 가속기를 통해 정부 저전력 및 에너지 절감 정책에 완벽히 상응하는 의료 정보 행정 플랫폼을 소유함.
- FuriosaAI win: B2G 헬스케어 최고 핵심 기관에 주도적으로 입찰 참여 혹은 파트너 협업하여 국가 공공 부문 독보적인 NPU 시스템 입지를 성취함.
- 직접 판매 가능성: `HIGH`
- CSP 경유 판매 가능성: `MID`
- NPUaaS 유도 가능성: `LOW`
- CSP capacity 증설 가능성: `LOW`
- 수치 근거: 없음
- 컨택 명분: 심평원 독자 디지털클라우드센터 내부 전용 가속 서버로 저전력 고효율 RNGD 기술 입찰 연계 협의
- 실제 컨택 시 사용할 말: 귀원 디지털전략실 주도의 AI·클라우드 동시 가동 추진 발표를 무척 뜻깊게 살펴보았습니다. 귀원에서 독자 구축을 기획하고 계시는 자체 GPU 서버 기반 AI 통합 플랫폼의 예산 효율과 유지 보수 이점을 높일 수 있도록, 국가 보급형 국산 고성능 NPU RNGD의 가용 방안을 논의드리고자 합니다.
- 매출 가능 시점: `단기`
- 담당자 후보 힌트: 김무성 디지털전략실장, Head of Digital Cloud Center
- 공개 프로필 URL: 
- 기존 접점: `확인 필요`
- B2G 근거 유형: `나라장터/RFP 확인`
- 나라장터 직접 확인: `확인 완료`
- 조달상 다음 액션: 나라장터/RFP 직접 확인 필요
- 확인 필요: 건강보험심사평가원 AI 통합 플랫폼 내부 가속 하드웨어 정형 RFP 개시 일정
- source_ids: S035
- source_urls: https://www.etnews.com/20260522000181

### 8. NH농협은행

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `온프레미스 기업`
- 분류: `structure_check`
- 확인된 프로젝트/시그널: 내부규정 및 금융 영업 지정을 타겟팅한 전용 생성형 AI 플랫폼 구축 및 엑사원 적용 가동
- 확인된 모델명: `EXAONE`
- 모델 매칭 상태: `family_only`
- 모델 fit_score: `MID`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `MID`
- RNGD fit_score: `MID`
- outreach priority: `MID`
- fit vs priority 설명: 사용 모델인 엑사원 3.5는 아키텍처적 조율이 다소 필요한 family_only 대상이며, 구축사 LG CNS와의 추가 하드웨어 정합 검증이 수반되어야 하므로 MID 수준의 영업 단계로 평가함.
- hook_type: `SOVEREIGN`
- 핵심 buying signal: 전행 전용 초거대 AI 기반의 플랫폼 구축을 완수하여 내부 업무 리테일 지원 및 RAG 검색을 연동 운영하기 시작함.
- 인프라 signal: 망분리 및 내부 업무 처리를 위한 전용의 온프레미스 프라이빗 데이터 서버 환경을 조성함.
- timing reason: 초기 구축 시스템의 실질 전행 전파 및 추가 트래픽 처리를 겨냥해 추론 속도 고도화 투자를 타진할 수 있는 국면임.
- 고객 win: 엄격한 망분리 규제를 완벽하게 준수하면서도, 전용 EXAONE 구동에 뛰어난 저전력 가속기로 인프라를 교체하여 서버 유지 관리 비용과 상면 공간 부담을 경감할 수 있음.
- FuriosaAI win: 제1금융권의 성공적인 프라이빗 엑사원 구축 사례를 선제 장악해 실증 레퍼런스로 전환시킴으로써 동종 업계 확산의 강력한 지렛대로 활용함.
- 직접 판매 가능성: `MID`
- CSP 경유 판매 가능성: `MID`
- NPUaaS 유도 가능성: `LOW`
- CSP capacity 증설 가능성: `LOW`
- 수치 근거: 없음
- 컨택 명분: 농협은행 프라이빗 엑사원 RAG 검색 속도 향상과 서버 자원 절감을 위한 고성능 국산 NPU 기술 검토 제안
- 실제 컨택 시 사용할 말: 귀원의 선도적인 엑사원 기반 전용 생성형 AI 플랫폼 구축 및 실무 가동 성과를 무척 인상 깊게 전해 들었습니다. 엑사원 모델 추론 속도 지연을 최소화하고 장기적인 프라이빗 인프라 TCO를 대폭 아낄 수 있는 국산 RNGD 실증 검토 기회를 조심스럽게 건네드리고자 합니다.
- 매출 가능 시점: `중기`
- 담당자 후보 힌트: CIO, Head of AI Lab, Head of Digital Transformation
- 공개 프로필 URL: https://kr.linkedin.com/company/nonghyup-bank
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 기존 시스템 구축 주체인 LG CNS와의 하드웨어 교차 적용 허용 범위 검토
- source_ids: S020
- source_urls: https://www.news2day.co.kr/article/20260522500024

### 9. 우리은행

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `CSP 고객 기업`
- 분류: `cloud_npuaaS_lead`
- 확인된 프로젝트/시그널: AI 에이전트 구축 사업 우선협상대상자로 삼성SDS를 선정하여 금융 AX 시스템 확대 추진
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 특정 AI 모델은 미공개로 UNKNOWN 상태이나, 삼성SDS를 핵심 파트너이자 주사업자로 선정하여 금융권 최초의 AX 플랫폼 가동을 추진하고 있으므로, 삼성SDS 채널 연동을 통한 가속 인프라 유도가 매우 강력하게 성립되어 최우선으로 분석함.
- hook_type: `PARTNER`
- 핵심 buying signal: 자산관리 보고서 생성 및 고객 가치 중심의 CRM 혁신을 주도할 AI 에이전트 프로젝트 우선협상자로 삼성SDS를 조기 지정함.
- 인프라 signal: 삼성SDS의 전문 금융 전용 클라우드나 고도의 프라이빗 전용 가상 서버 아키텍처를 연동할 개연성이 짙음.
- timing reason: 구축 사업자 낙찰 발표 직후 시스템 개발과 서버 구성의 초기 설계가 확정되기 이전 최상의 타이밍임.
- 고객 win: 삼성SDS 가상화 솔루션 기반 인프라에서 가동되어, 과다한 GPU 수급 비용 한계를 극복하고 제1금융권의 규제 준수 하에 합리적 예산으로 전행 상담 AI 플랫폼을 가치 높게 구현함.
- FuriosaAI win: 삼성SDS를 경유한 제1금융권 영업 협력 트랙을 최초 성공시켜, 국내 대규모 금융 엔터프라이즈 내에 당사 NPU 기반의 대화형 서비스를 실 서비스 연동함.
- 직접 판매 가능성: `LOW`
- CSP 경유 판매 가능성: `HIGH`
- NPUaaS 유도 가능성: `HIGH`
- CSP capacity 증설 가능성: `MID`
- 수치 근거: 없음
- 컨택 명분: 우리은행 에이전트 서빙 트래픽 처리를 위한 삼성SDS 연계 고가성비 가속 하드웨어 제안
- 실제 컨택 시 사용할 말: 귀행의 AI 에이전트 사업 진행 및 삼성SDS 파트너십 소식을 관심 깊게 지켜보고 있습니다. 금융 인프라의 안정성을 검증하면서도 대량의 검색RAG 질의를 가성비 높게 처리할 수 있도록, 삼성SDS 플랫폼에 맞춤 정합된 국산 가속기 RNGD 적용 이점을 상세히 제안드리고자 합니다.
- 매출 가능 시점: `단기`
- 담당자 후보 힌트: CIO, Head of AI Business, Head of CRM Transformation
- 공개 프로필 URL: https://www.linkedin.com/company/stockinsights-ai
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 우리은행 내부 프라이빗 AI 에이전트에 적용할 미세조정 예정 LLM 종류
- source_ids: S026, S028
- source_urls: https://www.sedaily.com/article/20046605?ref=naver | https://www.sedaily.com/article/20046505?ref=naver


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

1. **中 화웨이 “ASML 없이도 2031년 최첨단 칩 만든다”**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T02:00:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.g-enews.com/view.php?ud=2026052519455171789a1f309431_1
   - summary_snippet: 이 기술은 인공지능(AI) 반도체 개발에도 활용되고 있는 것으로 전해졌다. ◇“과열·복잡성 해결이 관건”... WSJ는 화웨이가 최근 1년 사이에야 비교적 안정적인 결과를 얻기 시작했다며, 대규모 데이터센터 환경에서...

2. **화웨이, 엔비디아·애플과 경쟁심화 속 새 반도체 기술 발표**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T01:55:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.bloter.net/news/articleView.html?idxno=663366
   - summary_snippet: 그는 화웨이가 오는 가을 내놓을 스마트폰 시리즈인 메이트90에 새 기술을 적용할 경우 엔지니어링 측면에서 큰 성과일 전망이지만 이를 인공지능(AI) 데이터센터 규모로 확장하는 것은 "서방의 제재를 우회하기 위한...

3. **[시론] AI로 빼앗기는 '성장 사다리'**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T00:24:00+09:00`
   - matched_query_or_feed: `생성형 AI 도입 기업`
   - url: https://www.hankyung.com/article/2026052573951
   - summary_snippet: 2022년 11월 챗GPT가 등장한 이후 생성형 인공지능(AI)이 폭발적으로 확산됐다. 한국은행이 최근 발표한 ‘AI... 셋째, 기업의 AI 도입을 ‘인력 절감’이 아니라 ‘인간+AI 생산성’ 기준으로 평가해야 한다. 사람을...

4. **유가·물가 숨 돌려도 고환율 지속 우려… 韓경제 뇌관은 ‘반도체’**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T00:22:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.kmib.co.kr/article/view.asp?arcid=1779700492&code=11151100&cp=nv
   - summary_snippet: 양 교수는 “미국 금리 인상으로 자국 내 AI 데이터센터 건설이 둔화할 경우 국내 반도체 수출에도 악영향을 미칠 수밖에 없다”고 우려했다. 한국은행의 기준금리 결정이 신중해야 한다는 제언도 나왔다. 내수 침체와...

5. **[중앙시평] 인공지능이 스스로 진화할 때**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T00:20:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.joongang.co.kr/article/25431189
   - summary_snippet: 우선 여러 기업이 개발하고 있는 AI 모델들을 하나로 통합해 국가 AI 챔피언을 키워볼 수 있고, 중국 내 데이터 센터들을 국영화해 범국가적 데이터 센터를 구축해 볼 수도 있겠다. 하지만 만약 그런 방식을 사용해도...

6. **연휴주말 김진태 후보 동분서주⋯‘반도체·AI데이터센터’ 지역맞춤형...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T00:07:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.kwnews.co.kr/page/view/2026052550159200000
   - summary_snippet: 국민의힘 김진태 강원지사 후보가 공식 선거운동 첫 주말·연휴를 맞아 ‘원주 반도체 비전’과 ‘강릉AI데이터센터’ 등 미래 먹거리 공약을 내세워 표심을 집중 공략했다. 김진태 후보는 지난 22~25일 주말·연휴를...

7. **정청래 대표부터 국회의원, 배우까지⋯민주 강원 지역 전방위 지원유세**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T00:06:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.kwnews.co.kr/page/view/2026052550145500000
   - summary_snippet: 정 대표는 이날 “우상호 후보는 아직 당선도 되기 전에 AI 데이터센터 투자 유치와 같은 굵직한 사업들을 직접 추진하고 있다”며 “보통은 당선 이후 일을 시작한다고 생각하는데 후보 때부터 이렇게 일하는 사람은...

8. **[선택 2026 강원] 골목골목 현장서 찾는 답 "해야 할 일 보일수록 설렌다...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T00:05:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.kado.net/news/articleView.html?idxno=2052090
   - summary_snippet: 우 후보는 "강릉과 동해 사이 AI 데이터센터 설립을 확정했다"며 "최대 70조원이 투자되는 국가 프로젝트다. 동해 예산이 7000억원 정도인데 70조 중 일부만 풀려도 동해는 대박나는 거 아니겠느냐"고 말했다. 현장 반응은...

9. **춘천시장 1번 공약 입맞춰 “산업·경제”⋯육동한 “첨단 융합 클러스...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T00:05:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.kwnews.co.kr/page/view/2026052550122300000
   - summary_snippet: 육동한 후보는 선거관리위원회에 5대 공약을 제출하며 ‘바이오·AI·양자·데이터를 결합한 첨단 산업 융합... 정 후보는 수열에너지 클러스터와 연계한 데이터 센터 유치, 강원권 반도체 공동 연구소와 특화 인력 양성센터...

10. **통합특별시 성패, 결국 ‘기업 유치’에 달렸다**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T00:04:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: http://www.kwangju.co.kr/article.php?aid=1779721200799342131
   - summary_snippet: 막대한 전력이 소요되는 반도체, AI, 데이터센터에는 전남의 재생에너지를 공급할 수 있다. 미래모빌리티는 광주가 갖고 있는 자동차 산업 기반과 결합된다. KENTECH와 GIST 는 첨단 기업의 연구개발(R&D) 파트너가 된다....

11. **금융委 “망분리 규제 합리화 속도 낼 것” [2026 한국금융미래포럼]**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T00:02:00+09:00`
   - matched_query_or_feed: `생성형 AI 도입 기업`
   - url: http://www.fntimes.com/html/view.php?ud=202605250721116305dd55077bc2_18
   - summary_snippet: 그동안 국내 금융회사들은 내부 업무망과 외부 인터넷망이 분리된 환경 탓에 생성형 AI와 클라우드 기반... 특히 금융회사들이 AI 도입 과정에서 가장 어려워하는 요인으로 거버넌스 부족을 꼽았다. AI 개발과 활용 전반을...

12. **When AI evolves on its own**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T00:01:00+09:00`
   - matched_query_or_feed: `private AI`
   - url: https://koreajoongangdaily.joins.com/news/2026-05-26/opinion/columns/When-AI-evolves-on-its-own/2600329
   - summary_snippet: That background makes the naming of the latest AI model introduced by Anthropic on April 7... government and certain private companies may now possess tools capable of disrupting foreign...

13. **연휴주말 김진태 후보 동분서주⋯‘반도체·AI데이터센터’ 지역맞춤형 공약 집중 - 강원일보**
   - source: `rss`
   - published_at_kst: `2026-05-26T00:01:00+09:00`
   - matched_query_or_feed: `Google News KR AI 데이터센터`
   - url: https://news.google.com/rss/articles/CBMiZEFVX3lxTE41NHVyX2lpQ3YtV3doYmFKSGZSZEJFUkJhU1hZdDBDckNhcGZkRHZBbUlVNGhaaGVVcHotbUQ4YWQ4am1XblRNTmRlcmE4V21HSVNJREs1THZVTGxneTNHRFFVYzM?oc=5
   - summary_snippet: 연휴주말 김진태 후보 동분서주⋯‘반도체·AI데이터센터’ 지역맞춤형 공약 집중  강원일보

14. **로보티즈, 움직이는 AI 시대 핵심 부품주 되나...휴머노이드 시장 주목**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T00:00:00+09:00`
   - matched_query_or_feed: `제조 AI 플랫폼`
   - url: https://www.cbci.co.kr/news/articleView.html?idxno=576986
   - summary_snippet: 일부 투자자들 사이에서는 로봇 부품 플랫폼 기업으로 자리매김할 경우 수조 원대 밸류에이션 가능성이... 미국 빅테크 기업들과 글로벌 제조사들이 차세대 AI 로봇 개발 경쟁에 뛰어들면서 구동계 핵심 부품 기업들에 대한...

15. **장민영號 기업은행, ‘IBK GenAI’ AX 가속…기업금융 혁신 [금융권 AI 人포그래픽] - 한국금융신문**
   - source: `rss`
   - published_at_kst: `2026-05-26T00:00:00+09:00`
   - matched_query_or_feed: `Google News KR 생성형 AI`
   - url: https://news.google.com/rss/articles/CBMifEFVX3lxTE45TXlCcFRKSVJuc2x6eTJ2U0w5bWpmUE9aUXh1YjVOMmdLLW5idlIyWjF2WURwWFVoc1ZmM3lqaVRYb1lKQ2Z6TkN6d1FNa3FLMFBDZHZ3Q1VYM3pUTGpDS001VkY4OVhWblZpYVgwVVBia1ZQazY0bzlEMno?oc=5
   - summary_snippet: 장민영號 기업은행, ‘IBK GenAI’ AX 가속…기업금융 혁신 [금융권 AI 人포그래픽]  한국금융신문

16. **[서학!스타] 포엣테크놀로지, AI 광통신 수혜 기대감 커지나…데이터센터 투자 확대에 변동성 주목 - CBC뉴스**
   - source: `rss`
   - published_at_kst: `2026-05-26T00:00:00+09:00`
   - matched_query_or_feed: `Google News KR AI 데이터센터`
   - url: https://news.google.com/rss/articles/CBMiaEFVX3lxTE1tQ3ktb0lTazBrT1JLaEFsUXl3ZVJvdU9sRzFjMDdkeGdSdVkyR2VPUVlPeDZ5ZmZQY2l3SERzaXoxRWF1RDBSNFRtS3hzdzlZT2JLY2lGSnRVNUxtVGVEaXhhTXB0T0RE?oc=5
   - summary_snippet: [서학!스타] 포엣테크놀로지, AI 광통신 수혜 기대감 커지나…데이터센터 투자 확대에 변동성 주목  CBC뉴스

17. **이원택 민주당 전북도지사 후보 "군산에 '전북성장공사' 설립"**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T23:29:00+09:00`
   - matched_query_or_feed: `제조 AI 플랫폼`
   - url: https://news.tf.co.kr/read/national/2325965.htm
   - summary_snippet: 피지컬AI, RE100, 재생에너지, 데이터센터, 첨단제조, 농생명 바이오 등 미래산업에 전략적으로 투자하고, 기업·금융·인재·기술을 연결해 전북의 성장 구조 자체를 바꾸는 산업·투자 중심 성장 플랫폼이다. 이 후보는...

18. **AI로 가장 먼저 대체될 직업은?…업종별 AI 대체 기상도 나왔다**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T23:17:00+09:00`
   - matched_query_or_feed: `금융 생성형 AI`
   - url: https://www.munhwa.com/article/11591124?ref=naver
   - summary_snippet: 생성형 인공지능(AI)의 급격한 확산 속에서 건설이나 생산직과 같은 현장 기술 중심의 직업이 가장... 미생물학자나 금융분석가처럼 AI를 통해 업무 효율을 극대화할 수 있는 직업들도 존재하기 때문이다. 예를 들어...

19. **06화 엔비디아(NVIDIA) 중심의 AI 데이터센터 - 브런치**
   - source: `rss`
   - published_at_kst: `2026-05-25T22:57:52+09:00`
   - matched_query_or_feed: `Google News KR AI 데이터센터`
   - url: https://news.google.com/rss/articles/CBMiS0FVX3lxTE16SUstU3dCN3hNWElUaGVaandPeXBtWUdxMDZKNXhZbnJ6ZWkwVzhrVlcxWnpwSHZidFpIREVJVko5a0FCSDdNY3FnUQ?oc=5
   - summary_snippet: 06화 엔비디아(NVIDIA) 중심의 AI 데이터센터  브런치

20. **'한국형 크라켄' 나온다…기후부, '에너지 AI' 도입 본격화**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T22:44:00+09:00`
   - matched_query_or_feed: `클라우드 AI 서비스`
   - url: https://daily.hankooki.com/news/articleView.html?idxno=1370369
   - summary_snippet: 영국 옥토퍼스 에너지의 플랫폼에서 착안한 '한국형 크라켄' 에너지 AI서비스 도입한다. 한국형 크라켄은... 정부는 공공과 민간이 데이터를 안전하게 공유할 수 있도록 보안성이 뛰어난 '커뮤니티 클라우드'를 검토...


## 다음 단계

1. LLM 후보 품질 확인
2. 노이즈가 많으면 NAVER_QUERIES / RSS_FEEDS 개선
3. 후보가 너무 적으면 MAX_LLM_SOURCES 상향
4. Gemini 3.5 Flash vs 2.5 Flash 품질 비교
5. 나라장터/B2G 수집 추가
6. 담당자/의사결정자 탐색 추가
7. Notion 또는 Google Docs 업로드 추가
