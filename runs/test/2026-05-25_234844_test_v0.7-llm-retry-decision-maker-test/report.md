# FuriosaAI GTM Research Agent Test Run

## 실행 정보

- run_id: `2026-05-25_234844_test_v0.7-llm-retry-decision-maker-test`
- mode: `test`
- memo: `v0.7-llm-retry-decision-maker-test`
- executed_at_kst: `2026-05-25T23:55:15.812760+09:00`
- agent_version: `v0.7`
- instructions_loaded_chars: `21592`
- naver_sources_recent_7d_count: `213`
- rss_sources_recent_7d_count: `98`
- merged_sources_recent_7d_count: `311`
- furiosa_docs_successful: `11`
- furiosa_docs_failed: `0`
- llm_called: `True`
- llm_error: ``

## 현재 단계

이 실행은 v0.7 테스트입니다.

이번 버전에서는 네이버 뉴스 API, RSS feed, FuriosaAI 공개 개발자 문서를 수집한 뒤 Gemini로 GTM 후보를 1차 평가하고, 별도 LLM 호출로 매니저용 gtm_report.md를 작성합니다.

아직 나라장터 직접 API, 담당자 심화 탐색, Notion 업로드는 수행하지 않았습니다.

## LLM 실행 요약

- overall_assessment: 최근 국내 대형 CSP 및 공공 부문을 중심으로 생성형 AI 서비스 인프라 확장과 민간·공공 전용 AI 플랫폼 구축 수요가 강하게 확인됩니다. 특히 삼성SDS의 동탄 및 구미 데이터센터 인프라 확장, 우리은행 AI 에이전트 사업 수주 등은 대규모 추론 인프라 공급의 핵심 기회입니다. 또한 한글과컴퓨터와 LG AI연구원의 공공 AI 에이전트 동맹, 건강보험심사평가원의 GPU 기반 플랫폼 구축 등 B2G 영역의 실행형 사업이 구체화되고 있어 맞춤형 GTM 전개가 요구됩니다.
- top_priority_names: 삼성SDS, 엘리스그룹, 우리은행, 건강보험심사평가원
- noise_ratio_comment: 수집된 40개 소스 중 선거 공약, 글로벌 거대 기술기업 동향, 전력 인프라 주식 동향 등 직접적인 GTM 신호가 없는 3개 소스를 제외한 대부분의 소스가 국내 CSP 인프라 확장 및 생성형 AI 플랫폼 구축 프로젝트와 관련된 유의미한 비즈니스 신호를 포함하고 있습니다.
- model_compatibility_caution: 본 평가에서는 제공된 FuriosaAI 개발자 문서 기준을 엄격히 적용하여 정확한 모델 및 버전 매칭을 수행했습니다. 농협은행의 EXAONE 3.5 도입 사례와 한글과컴퓨터의 챗엑사원 결합 사례는 EXAONE 모델 제품군에 해당하나 구체적인 지원 버전 검증이 필요하므로 family_only로 분류하여 보수적으로 평가했습니다. 또한 큐엔 모델군 및 업스테이지 솔라 모델의 경우 구체적인 버전 일치 여부를 파트너십 과정에서 추가 확인해야 합니다.

## LLM 후보 평가 결과

## 버전 1 — B2B only 우선 검토 요약

- 삼성SDS / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- 엘리스그룹 / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- NH농협은행 / 온프레미스 기업 / classification: `structure_check` / fit: `MID` / outreach: `MID` / 매출시점: `중기`
- 우리은행 / CSP 고객 기업 / classification: `cloud_npuaaS_lead` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`


## 버전 2 — B2B + B2G 우선 검토 요약

- 삼성SDS / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- 엘리스그룹 / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- 건강보험심사평가원 / 온프레미스 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기` / B2G 근거: `기사/RSS 기반` / 나라장터 확인: `미수행`
- 한글과컴퓨터 / CSP 고객 기업 / classification: `structure_check` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기` / B2G 근거: `기사/RSS 기반` / 나라장터 확인: `미수행`
- NH농협은행 / 온프레미스 기업 / classification: `structure_check` / fit: `MID` / outreach: `MID` / 매출시점: `중기`
- 전남소방본부 / 온프레미스 기업 / classification: `structure_check` / fit: `MID` / outreach: `MID` / 매출시점: `중기` / B2G 근거: `기사/RSS 기반` / 나라장터 확인: `미수행`
- 우리은행 / CSP 고객 기업 / classification: `cloud_npuaaS_lead` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`


## 상세 후보 평가

### 1. 삼성SDS

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `CSP 운영 기업`
- 분류: `priority_outreach`
- 확인된 프로젝트/시그널: 동탄 데이터센터 및 경북 구미 AI 데이터센터 투자 및 우리은행 AI 에이전트 구축 사업 우선협상대상자 선정
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 도입 모델이 구체적으로 확인되지 않아 모델 적합성은 UNKNOWN으로 분류되었으나, 동탄 데이터센터 전력 확보 및 구미 데이터센터 대규모 투자를 통한 인프라 확장 계획과 우리은행 AI 에이전트 사업 수주 등 강력한 비즈니스 신호가 존재합니다. 따라서 인프라 파트너십 및 대규모 CSP 용량 증설 경로를 고려하여 outreach_priority를 HIGH로 책정하였습니다.
- hook_type: `CLOUD`
- 핵심 buying signal: 경기 동탄 데이터센터에 20MW급 전력을 확보하고, 경북 구미에 4273억원을 투자해 60MW 규모의 AI 데이터센터를 구축하기로 결정함
- 인프라 signal: 동탄 및 구미 지역에 대규모 데이터센터를 확보하여 GPUaaS 인프라 공급 능력을 확장하고 있음
- timing reason: 대규모 인프라 확장 및 전력 확보 시점에 맞추어 하드웨어 효율성 및 운영 비용 개선을 위한 가속기 도입 제안이 가능한 시점임
- 고객 win: 대규모 AI 추론 서비스 운영 시 발생하는 전력 및 냉각 비용을 절감하고, 가속기 도입 효율성을 높여 인프라 구축 및 운영 부담을 최소화할 수 있음
- FuriosaAI win: 대규모 AI 인프라를 보유한 핵심 CSP 파트너를 확보함으로써 국산 NPU 기반의 NPUaaS 비즈니스 협력 및 추가적인 가속기 대량 공급 기회를 선점할 수 있음
- 직접 판매 가능성: `MID`
- CSP 경유 판매 가능성: `HIGH`
- NPUaaS 유도 가능성: `HIGH`
- CSP capacity 증설 가능성: `HIGH`
- 수치 근거: 경북 구미에 4273억원을 투자해 60MW 규모 AI 데이터센터를 구축하기로 결정 (S009) — 근거: 삼성SDS는 경북 구미에 4273억원을 투자해 60MW 규모 AI 데이터센터를 짓기로 했다. | 경기 동탄 데이터센터 서관 가동을 위해 20MW급 전력 확보 (S003) — 근거: 삼성SDS가 경기 동탄 데이터센터 서관 가동을 위해 20MW급 전력을 확보한 사례
- 컨택 명분: 동탄 및 구미 데이터센터 인프라 확장 계획과 금융권 AI 수주 성과에 맞추어 고성능 저전력 가속기 기반의 추론 비용 절감 방안 제안 필요
- 실제 컨택 시 사용할 말: 최근 동탄 및 구미 데이터센터 인프라 투자 소식을 보고 연락드렸습니다. 대규모 GPUaaS 인프라 및 금융권 AI 서비스 운영 시 전력과 냉각 효율을 대폭 개선할 수 있는 가속기 도입 협력 방안을 제안드리고자 합니다.
- 매출 가능 시점: `단기`
- 담당자 후보 힌트: 클라우드 서비스 및 인프라 부문 CIO, CTO, Head of Cloud, 플랫폼 및 데이터센터 구축 담당 부서장
- 공개 프로필 URL: https://www.linkedin.com/company/samsung-sds
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 구미 및 동탄 데이터센터 내 국산 NPU 및 가속기 평가/도입 로드맵 확인 필요 | 우리은행 AI 에이전트 서비스 플랫폼에 RNGD 기술 규격 접목 가능성 타진
- source_ids: S003, S009, S025, S027
- source_urls: https://www.e-science.co.kr/news/articleView.html?idxno=130004 | https://www.mt.co.kr/tech/2026/05/23/2026052210211399740 | https://www.sedaily.com/article/20046605?ref=naver | https://www.sedaily.com/article/20046505?ref=naver

### 2. 엘리스그룹

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `CSP 운영 기업`
- 분류: `priority_outreach`
- 확인된 프로젝트/시그널: 코스닥 상장 예비심사 청구 및 자체 GPUaaS 및 인프라 비즈니스 본격화
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 도입 모델이 구체화되지 않아 model_fit_score는 UNKNOWN이나, 코스닥 상장 추진을 계기로 자체 AI 클라우드 인프라(ECI, AI PMDC) 및 GPUaaS 서비스를 적극적으로 고도화하고 확장하는 성장 단계에 있어 인프라 파트너십 구축 및 NPUaaS 협력 강화를 위한 접촉 가치가 매우 크므로 outreach_priority를 HIGH로 판정했습니다.
- hook_type: `CLOUD`
- 핵심 buying signal: 코스닥 상장 예비심사를 신청하며 AI 클라우드 인프라 솔루션 및 자체 이동식 모듈형 데이터센터 등의 서비스 사업 확대를 공식화함
- 인프라 signal: 자체 클라우드 인프라 및 AI PMDC를 직접 설계·운영하며 대규모 가속기 리소스 확보에 높은 관심을 보이고 있음
- timing reason: 상장 추진을 통해 유입될 투자 재원을 바탕으로 인프라 확장 투자가 예정되어 있어, 저비용·고효율 NPU 하드웨어 솔루션 제안의 최적기임
- 고객 win: 효율적인 하드웨어 설계를 바탕으로 인프라 투자 비용을 절감하고 가성비 높은 NPUaaS 라인업을 구성하여 서비스 경쟁력을 제고할 수 있음
- FuriosaAI win: 성장세가 가파른 신흥 AI 클라우드 전문 플랫폼을 확보하여 국산 NPU 레퍼런스를 다각화하고 중장기적인 가속기 공급 파이프라인을 구축할 수 있음
- 직접 판매 가능성: `MID`
- CSP 경유 판매 가능성: `HIGH`
- NPUaaS 유도 가능성: `HIGH`
- CSP capacity 증설 가능성: `HIGH`
- 수치 근거: 없음
- 컨택 명분: AI 클라우드 인프라 확장 및 고도화 시점에 발맞춘 저전력 가속기 솔루션 기반 NPUaaS 파트너십 제안
- 실제 컨택 시 사용할 말: 최근 코스닥 상장 추진 및 AI 클라우드 서비스 고도화 소식을 보고 연락드렸습니다. 엘리스그룹의 모듈형 데이터센터 및 클라우드 인프라에 당사의 RNGD를 연계하여 비용 효율적인 차세대 NPUaaS 라인업을 공동 구축하는 방안을 논의하고자 합니다.
- 매출 가능 시점: `단기`
- 담당자 후보 힌트: 대표이사(CEO), CTO, AI 클라우드 인프라 본부장, 인프라 아키텍처 및 하드웨어 조달 담당 부서장
- 공개 프로필 URL: https://www.venturesquare.net/950953/
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 엘리스그룹이 현재 기획 중인 신규 가속기 라인업 내 국산 NPU 채택 가능 여부 검토 | RNGD 기반의 AI 가상화 및 Kubernetes 스택 정합성 검증 일정 조율
- source_ids: S012, S013, S014, S015, S016, S017
- source_urls: http://www.hansbiz.co.kr/news/articleView.html?idxno=839792 | http://www.joseilbo.com/news/news_read.php?uid=568639&class=53&grp= | https://www.fetv.co.kr/news/articleView.html?idxno=302765 | https://www.the-stock.kr/news/articleView.html?idxno=32570 | https://www.newspim.com/news/view/20260520000146 | https://www.cstimes.com/news/articleView.html?idxno=706484

### 3. 건강보험심사평가원

- 국가: `KR`
- 시장: `B2G`
- 타깃 유형: `온프레미스 기업`
- 분류: `priority_outreach`
- 확인된 프로젝트/시그널: GPU 서버 기반의 원스톱 AI 통합 플랫폼 및 클라우드 구축 드라이브
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 도입 예정 모델이 알려지지 않아 model_fit_score는 UNKNOWN으로 설정했으나, GPU 서버에 기반을 둔 자체적인 AI 통합 플랫폼을 신규 설계하고 클라우드 드라이브를 공동 추진하는 강한 인프라 도입 조달 신호가 존재합니다. 공공 성격의 의료 공공기관의 강한 B2G 도입 구조를 보유하므로 outreach_priority를 HIGH로 결정했습니다.
- hook_type: `PROCUREMENT`
- 핵심 buying signal: 김무성 디지털전략실장을 중심으로 GPU 서버 기반의 AI 통합플랫폼 구축 및 클라우드 동시 드라이브 계획을 대외적으로 선언함
- 인프라 signal: 자체 클라우드 센터를 중심으로 가상화 기반의 GPU 서버 및 추론 처리 시스템을 대규모로 가동하고자 함
- timing reason: 평가기관 전환 총력 및 클라우드/AI 통합 플랫폼 로드맵 수립 발표 직후 시점으로, 하드웨어 사양 및 예산 편성 전 단계에서의 규격 협의가 절실한 타이밍임
- 고객 win: 대규모 진료 정보 및 의료 관련 검색 서비스를 처리할 때 급증할 수 있는 공공 데이터 인프라의 운영 비용을 절감하고, 전력 및 상면 부담을 대폭 해소할 수 있음
- FuriosaAI win: 국내 주요 의료 공공기관의 핵심 추론 인프라 영역에 성공적으로 공급하여 의료 공공 도메인의 강력한 국산 NPU 모범 구축 사례를 획득함
- 직접 판매 가능성: `HIGH`
- CSP 경유 판매 가능성: `MID`
- NPUaaS 유도 가능성: `LOW`
- CSP capacity 증설 가능성: `LOW`
- 수치 근거: 없음
- 컨택 명분: 심평원 자체 GPU 기반 AI 플랫폼 계획에 맞춤화된 고효율 NPU 하드웨어 아키텍처 제안 기회 포착
- 실제 컨택 시 사용할 말: 최근 발표하신 AI·클라우드 드라이브 및 GPU 기반 통합 플랫폼 구축 전략을 보고 연락드렸습니다. 심평원의 AI 공공 서비스 활성화를 위한 고성능·저전력 기반의 하드웨어 운영 효율성 달성에 국산 RNGD 솔루션이 제공할 기여 요소를 소개해 드리고자 합니다.
- 매출 가능 시점: `단기`
- 담당자 후보 힌트: 디지털전략실장(디지털클라우드센터장 겸 AI융합추진단장), 정보화실 총괄책임, 공공 플랫폼 조달 담당자
- 공개 프로필 URL: 확인 필요
- 기존 접점: `확인 필요`
- B2G 근거 유형: `기사/RSS 기반`
- 나라장터 직접 확인: `미수행`
- 조달상 다음 액션: 나라장터/RFP 직접 확인 필요
- 확인 필요: 신규 AI 시스템 구축 관련 공공 입찰/나라장터 RFP 조달 규격 확인 필요 | 의료 영상 및 문서 처리를 위해 검토 예정인 내부 백엔드 모델과의 호환성 조율
- source_ids: S036
- source_urls: https://www.etnews.com/20260522000181

### 4. 한글과컴퓨터

- 국가: `KR`
- 시장: `B2G`
- 타깃 유형: `CSP 고객 기업`
- 분류: `structure_check`
- 확인된 프로젝트/시그널: LG AI연구원과 AI 문서 에이전트 및 공공 AX 시장 공동 진출 협력
- 확인된 모델명: `EXAONE`
- 모델 매칭 상태: `family_only`
- 모델 fit_score: `MID`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `MID`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: LG AI연구원의 EXAONE 모델군을 기반으로 사업을 전개하므로 model_match_status는 family_only로 분류하여 model_fit_score와 rngd_fit_score는 MID로 책정했습니다. 다만 공공 AX 시장 수주를 목표로 정부부처 및 공기업에 대규모 납품을 추진하는 파트너십 구축이 활발하므로, 공공망 및 규제 환경을 위한 국산 하드웨어 최적화 가치를 평가하여 outreach_priority를 HIGH로 판정했습니다.
- hook_type: `PROCUREMENT`
- 핵심 buying signal: 정부부처, 공공기관, 공기업을 대상으로 문서 AI 역량과 LG의 '챗엑사원'을 결합한 통합 에이전트 솔루션 공급을 확대하고 있음
- 인프라 signal: 공공기관의 특수 보안 요건을 준수하기 위해 온프레미스 구축 및 행안부 보안 기준을 만족하는 프라이빗 클라우드 인프라 배포를 고려 중임
- timing reason: 공공 AX 공동 수주 및 정부 주도의 AI 플랫폼 인프라 도입 사업이 연달아 구체화되는 단계로, 하드웨어 주권 확보 차원의 국산 NPU 도입 제안을 추진하기에 최적의 시기임
- 고객 win: 공공 전용 AI 문서 에이전트 서비스 전개 시 엄격한 데이터 보안 요구사항을 충족하고 전력 소비와 도입 비용을 한층 합리적으로 제어할 수 있음
- FuriosaAI win: 대표적인 한글 문서 기반 AI 서비스에 가속기 최적화를 실현하여 공공 부문 비즈니스 영역에서 지배적인 국산 가속기 레퍼런스를 확보할 수 있음
- 직접 판매 가능성: `MID`
- CSP 경유 판매 가능성: `MID`
- NPUaaS 유도 가능성: `MID`
- CSP capacity 증설 가능성: `MID`
- 수치 근거: 없음
- 컨택 명분: 공공 부문 AX 연합 진출에 따른 저전력 국산 NPU 기반 AI 문서 솔루션 최적화 논의 제안
- 실제 컨택 시 사용할 말: 최근 LG AI연구원과의 '챗엑사원' 및 AI 문서 에이전트 공공 시장 동맹 강화 소식을 확인하고 연락드렸습니다. 공공 및 정부부처의 보안 규제를 완벽히 준수하며 대규모 문서 요약 및 생성 인프라를 합리적으로 제어할 수 있는 국산 RNGD 가속기 도입 방안을 논의하고자 합니다.
- 매출 가능 시점: `단기`
- 담당자 후보 힌트: 공공사업본부장, CTO, AI 연구소장, AI 플랫폼 개발 팀장 또는 솔루션 설계 부서장
- 공개 프로필 URL: 확인 필요
- 기존 접점: `확인 필요`
- B2G 근거 유형: `기사/RSS 기반`
- 나라장터 직접 확인: `미수행`
- 조달상 다음 액션: 나라장터/RFP 직접 확인 필요
- 확인 필요: 공공부문 사업 추진 시 가속기에 대한 기술적 요구 사양(K8s 연동성 등) 충족 여부 확인 | EXAONE 4.0 계열 등 최신 모델 버전 적용을 위한 가속기 컴파일 최적화 정합성 평가
- source_ids: S020, S021, S022, S023, S024
- source_urls: http://www.newslock.co.kr/news/articleView.html?idxno=130504 | https://www.mt.co.kr/tech/2026/05/22/2026052215283358675 | https://www.mk.co.kr/article/12055579 | https://www.getnews.co.kr/news/articleView.html?idxno=870707 | https://www.newsis.com/view/NISX20260522_0003640664

### 5. NH농협은행

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `온프레미스 기업`
- 분류: `structure_check`
- 확인된 프로젝트/시그널: LG CNS와 협력하여 전용 생성형 AI 플랫폼 구축 및 RAG 소방/금융 업무 적용
- 확인된 모델명: `EXAONE`
- 모델 매칭 상태: `family_only`
- 모델 fit_score: `MID`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `MID`
- RNGD fit_score: `MID`
- outreach priority: `MID`
- fit vs priority 설명: LG CNS를 통해 커스텀 튜닝된 EXAONE 3.5 기반 전용 AI 플랫폼을 구축하였으며, 이는 당사 지원 모델군인 EXAONE 패밀리에 속하지만 구체적인 버전에 관한 컴파일 유효성 검토가 요구되므로 model_fit_score를 MID로 배정했습니다. 보안 중심의 금융 폐쇄망 및 전용 온프레미스 인프라 성격이 뚜렷하여 구조 검토 목적의 우선순위 MID로 책정했습니다.
- hook_type: `SOVEREIGN`
- 핵심 buying signal: 내부 규정 및 상품 정보 검색, 리테일 영업 지원을 수행하기 위해 전용 생성형 AI 및 RAG 기반 고도화 플랫폼을 실제 가동하며 업무 범위를 점진적으로 확대하고 있음
- 인프라 signal: 보안 및 규정을 준수하기 위해 대외 망과 분리된 금융사 전용의 폐쇄형/프라이빗 인프라 환경을 가동하고 있음
- timing reason: 전용 생성형 AI의 실무 도입이 완료된 상태로, 업무용 트래픽 증가 및 검색 모델 다각화에 대응하여 가속기 효율성을 정밀 검토할 적기임
- 고객 win: 엄격한 보안 기준을 우수하게 만족시키면서, 금융 전용 온프레미스 가속 서버의 소모 전력을 최소화하고 내부 생성형 인프라 유지 관리 부담을 대폭 경감할 수 있음
- FuriosaAI win: 금융권 자체 생성형 AI 및 RAG 서버 구축 분야에서 최적의 파트너십 레퍼런스를 개척하고, 특수 도메인 프라이빗 하드웨어 공급을 본격 다각화할 수 있음
- 직접 판매 가능성: `MID`
- CSP 경유 판매 가능성: `MID`
- NPUaaS 유도 가능성: `LOW`
- CSP capacity 증설 가능성: `LOW`
- 수치 근거: 없음
- 컨택 명분: 금융사 전용 프라이빗 AI 모델 서빙의 비용 및 운영 전력 절감을 위한 NPU 최적화 검토 제안
- 실제 컨택 시 사용할 말: 최근 LG CNS와 구축하신 전용 생성형 AI 플랫폼 및 RAG 기반 금융 업무 혁신 성과를 보고 연락드렸습니다. 금융 폐쇄망 환경의 고유 요구사항을 충족하면서도 가속 장치의 전력과 상면 효율을 극대화할 수 있는 당사 RNGD 기반의 최적화 방안을 함께 제안드립니다.
- 매출 가능 시점: `중기`
- 담당자 후보 힌트: 디지털금융부문장, IT보안기획실장, AI 개발총괄 임원, 시스템운영 플랫폼 부서장
- 공개 프로필 URL: https://www.sanctionlab.com/?p=46854
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 기 도입된 EXAONE 3.5 모델에 대응하여 RNGD 컴파일러 환경 연동 가능성 조율 | 자체 IDC 내에 하드웨어 가속기 추가 설치 가능성 및 전력 예산 여유 확인
- source_ids: S019
- source_urls: https://www.news2day.co.kr/article/20260522500024

### 6. 전남소방본부

- 국가: `KR`
- 시장: `B2G`
- 타깃 유형: `온프레미스 기업`
- 분류: `structure_check`
- 확인된 프로젝트/시그널: 에코아이티와 협력하여 Solar LLM 기반 재난 대응 플랫폼 구축 본격화
- 확인된 모델명: `Solar LLM`
- 모델 매칭 상태: `family_only`
- 모델 fit_score: `MID`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `MID`
- RNGD fit_score: `MID`
- outreach priority: `MID`
- fit vs priority 설명: 도입 모델이 Upstage Solar LLM 계열로 당사 지원 제품군에 부합하지만 정확한 버전 최적화 검증이 사전에 필요하므로 family_only로 판단하여 model_fit_score와 rngd_fit_score는 MID로 책정했습니다. 소방 업무의 폐쇄망 성격과 K8s 클라우드 기반 구축 사업을 직접 전개하고 있으므로 구조 확인 목적의 MID 우선순위로 매칭했습니다.
- hook_type: `PROCUREMENT`
- 핵심 buying signal: 에코아이티를 개발 주체로 선정하여 Solar LLM 및 RAG 기술을 적용하는 지능형 소방행정 지원 및 문서 생성 플랫폼 사업에 착수함
- 인프라 signal: 안정성과 복구 능력을 확보하기 위해 쿠버네티스(K8s) 기반의 독립 클라우드 인프라 아키텍처 환경에 추론 서버 배포를 기획함
- timing reason: 본격적인 플랫폼 구축 및 학습데이터 연계 적용 초기 단계로, 서빙 인프라 단에서의 GPU 부족 해결을 위한 가속 장치 성능 시험을 연계 검토하기 적합함
- 고객 win: 재난 관리 현장 및 대민 지원 영역에서 빠른 응답성과 고가용성을 지닌 LLM 인프라를 가혹한 환경 하에서도 비용 효율적으로 확보 및 운영할 수 있음
- FuriosaAI win: 안전행정 및 공공 재난 대응이라는 고신뢰성 특수 조달 분야에서 대표적인 국산 추론 가속기 배포 레퍼런스를 다지는 기회가 됨
- 직접 판매 가능성: `MID`
- CSP 경유 판매 가능성: `MID`
- NPUaaS 유도 가능성: `LOW`
- CSP capacity 증설 가능성: `LOW`
- 수치 근거: 없음
- 컨택 명분: Solar LLM 기반 공공 솔루션 전개 시 K8s 가상화 연동 규격 및 저전력 고효율 가속 인프라 제시
- 실제 컨택 시 사용할 말: 최근 전남소방본부와 에코아이티가 추진하는 Solar LLM 기반 재난 대응 플랫폼 구축 사업을 확인하고 연락드렸습니다. 당사의 RNGD는 쿠버네티스 환경에 유연하게 작동하는 만큼 지능형 소방행정 인프라의 완성도를 저비용으로 개선하는 데 많은 기여를 도울 수 있습니다.
- 매출 가능 시점: `중기`
- 담당자 후보 힌트: 전남소방본부 소방정보화팀장, 에코아이티 프로젝트 수행 PM, 소방 인프라 조달 부서장
- 공개 프로필 URL: 확인 필요
- 기존 접점: `확인 필요`
- B2G 근거 유형: `기사/RSS 기반`
- 나라장터 직접 확인: `미수행`
- 조달상 다음 액션: 나라장터/RFP 직접 확인 필요
- 확인 필요: 도입 추진 예정인 Solar LLM의 구체적 파라미터 규격 및 RNGD 상에서의 동작 테스트 일정 확인 | 소방본부 자체 전산센터 내 물리적 전력 한도 정보 확인
- source_ids: S028
- source_urls: https://magazine.hankyung.com/business/article/202605196285b

### 7. 우리은행

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `CSP 고객 기업`
- 분류: `cloud_npuaaS_lead`
- 확인된 프로젝트/시그널: AI 에이전트 구축 사업 우선협상대상자로 삼성SDS 선정
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 사용 모델명이 명시되지 않아 model_fit_score는 UNKNOWN으로 평가했으나, 금융권 AI 플랫폼 고도화를 위해 삼성SDS의 클라우드 기반 및 전용 인프라를 활용하여 사업을 대규모로 전개할 예정입니다. 삼성SDS와의 파트너십 채널을 활용한 CSP 경유 도입 또는 NPUaaS 도입 시나리오의 가치가 매우 높기 때문에 outreach_priority를 HIGH로 결정했습니다.
- hook_type: `PARTNER`
- 핵심 buying signal: 자산관리 분석 보고서 작성 및 기업 분석 등의 기능을 수행하기 위해 대규모 AI 에이전트 구축 사업을 진행하며 우선협상대상자로 삼성SDS를 최종 선정함
- 인프라 signal: 삼성SDS의 금융 AI 플랫폼 인프라를 연계 사용하거나 보안 요건을 충족하기 위한 전용 인프라 아키텍처 환경 구축을 검토 중임
- timing reason: 우선협상대상자 선정 직후 구체적인 인프라 아키텍처 및 가속기 규격을 검토하고 확정하는 단계로, 파트너사인 삼성SDS와 공동으로 최적의 비용 효율을 제공하는 NPU 규격을 제안할 적절한 타이밍임
- 고객 win: 보안 제약을 해소하며 금융권 전용 AI 에이전트 서빙 환경을 대규모로 운영할 때 발생하는 연산 비용 및 인프라 구축 단가를 크게 낮출 수 있음
- FuriosaAI win: 국내 대형 금융권 고객의 핵심 서비스 플랫폼에 삼성SDS 협력 채널을 경유하여 RNGD 추론 서버를 성공적으로 도입하고 주요 금융권 모범 사례를 확보할 수 있음
- 직접 판매 가능성: `LOW`
- CSP 경유 판매 가능성: `HIGH`
- NPUaaS 유도 가능성: `HIGH`
- CSP capacity 증설 가능성: `MID`
- 수치 근거: 없음
- 컨택 명분: 삼성SDS 우선협상대상자 선정에 따라 대규모 추론 서비스용 저전력 고효율 NPU 도입 방안 제안
- 실제 컨택 시 사용할 말: 최근 생성형 AI 기반 금융 비즈니스 고도화 사업의 우선협상대상자로 삼성SDS가 선정된 것을 보고 연락드렸습니다. 삼성SDS 인프라와 결합하여 대규모 금융 데이터 분석 및 문서 요약 서비스를 한층 경제적이고 안정적으로 구동할 수 있는 NPU 솔루션을 소개드리고자 합니다.
- 매출 가능 시점: `단기`
- 담당자 후보 힌트: 디지털그룹 임원, AI 플랫폼 센터장, CDO, IT 인프라 기획 부서장 및 조달 담당 부서
- 공개 프로필 URL: 확인 필요
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 금융위의 망분리 규제 완화 기조 속에서 클라우드 및 전용 온프레미스 인프라 비중 확인 필요 | 삼성SDS의 해당 구축 본부와의 연계 파트너십 가능 여부 점검
- source_ids: S025, S027
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

1. **이원택 민주당 전북도지사 후보 "군산에 '전북성장공사' 설립"**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T23:29:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://news.tf.co.kr/read/national/2325965.htm
   - summary_snippet: 이 후보의 1호 공약인 '전북성장공사'는 피지컬AI, RE100, 재생에너지, 데이터센터, 첨단제조, 농생명 바이오 등 미래산업에 전략적으로 투자하고, 기업·금융·인재·기술을 연결해 전북의 성장 구조 자체를 바꾸는 산업·투자...

2. **AI로 가장 먼저 대체될 직업은?…업종별 AI 대체 기상도 나왔다**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T23:17:00+09:00`
   - matched_query_or_feed: `금융 생성형 AI`
   - url: https://www.munhwa.com/article/11591124?ref=naver
   - summary_snippet: 생성형 인공지능(AI)의 급격한 확산 속에서 건설이나 생산직과 같은 현장 기술 중심의 직업이 가장... 미생물학자나 금융분석가처럼 AI를 통해 업무 효율을 극대화할 수 있는 직업들도 존재하기 때문이다. 예를 들어...

3. **우상호 “철원 군사시설 보호구역 대폭 해제”**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T23:11:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.pressian.com/pages/articles/2026052522035575615?utm_source=naver&utm_medium=search
   - summary_snippet: ◇ “이재명-우상호-한금석 라인업, 4년만 써달라” 또 우 후보는 지역 경제와 청년 일자리를 위해 동해안권에 유치한 70조 규모의 대기업 AI 데이터센터와 원주의 국방 첨단 산업 클러스터 조성을 언급하며 고향 철원의...

4. **06화 엔비디아(NVIDIA) 중심의 AI 데이터센터 - 브런치**
   - source: `rss`
   - published_at_kst: `2026-05-25T22:57:52+09:00`
   - matched_query_or_feed: `Google News KR AI 데이터센터`
   - url: https://news.google.com/rss/articles/CBMiS0FVX3lxTE16SUstU3dCN3hNWElUaGVaandPeXBtWUdxMDZKNXhZbnJ6ZWkwVzhrVlcxWnpwSHZidFpIREVJVko5a0FCSDdNY3FnUQ?oc=5
   - summary_snippet: 06화 엔비디아(NVIDIA) 중심의 AI 데이터센터  브런치

5. **[조선규의 문제 핵심] AI 황금기 뒤 숨은 진실 '속도와 전력' 벽 깨야**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T22:44:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.newsclaim.co.kr/news/articleView.html?idxno=3064585
   - summary_snippet: 우주 데이터 센터 역시 대안으로 꼽히지만, 이 또한 위성 간 광통신 대역폭 한계를 먼저 해결해야 한다. 현재 시장 일각에서는 AI 버블론을 제기하지만, 데이터 과학 관점에서 AI는 이미 실질적 생산성을 증명하고...

6. **'한국형 크라켄' 나온다…기후부, '에너지 AI' 도입 본격화**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T22:44:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://daily.hankooki.com/news/articleView.html?idxno=1370369
   - summary_snippet: 기후부(당시 산업통상자원부)는 2024년 12월 제32차 에너지위원회를 열고 'AI를 활용한 에너지 시스템 전환 정책방향'을 발표했다. 첨단산업과 데이터센터 확대로 급증하는 전력 수요에 대응하고, 기후변화와 재생에너지...

7. **에이수스, 하이브리드 에이전틱 AI 인프라 공개…추론 비용 최대 70% 절...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T22:42:00+09:00`
   - matched_query_or_feed: `생성형 AI 도입 기업`
   - url: https://www.aitimes.kr/news/articleView.html?idxno=40186
   - summary_snippet: 온프레미스 배포에 최적화된 이 아키텍처는 기업이 생성형 AI 애플리케이션을 도입할 때 성능과 비용의 균형을 맞출 수 있도록 설계됐다. 최근 대형언어모델(LLM)과 AI 에이전트 기반 애플리케이션 도입이...

8. **"5~20년 후 관절 건강 예측"…GC녹십자, 혈우병 환자 맞춤형 AI 진단 플랫...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T22:32:00+09:00`
   - matched_query_or_feed: `병원 AI 플랫폼`
   - url: http://www.thefirstmedia.net/news/articleView.html?idxno=199952
   - summary_snippet: 삼성서울병원과 공동으로 보건복지부 '첨단바이오 융합인재 양성 사업' 과제에 선정돼 세계 최초 AI 기반... 업계에서는 향후 해당 기술이 혈우병뿐 아니라 만성 희귀질환 관리 플랫폼으로 확장될 가능성에도 주목하고...

9. **광주연구원 "UN AI 허브 유치로 광주 글로벌 AI 거점 도약해야"**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T22:14:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.mhns.co.kr/news/articleView.html?idxno=748341
   - summary_snippet: 연구원은 광주가 지난 2019년부터 2024년까지 추진한 AI 중심도시 1단계 사업을 통해 국가 AI 데이터센터를 비롯해 인재 양성 체계, 기업 유치, 연구개발 지원 기반 등을 구축하며 AI 산업 기반을 확대해 왔다고...

10. **광주연구원 “UN AI 허브 유치로 광주 글로벌 AI 거점 도약해야” - 더쎈뉴스**
   - source: `rss`
   - published_at_kst: `2026-05-25T22:13:18+09:00`
   - matched_query_or_feed: `Google News KR AI 데이터센터`
   - url: https://news.google.com/rss/articles/CBMiaEFVX3lxTFBwOVFqaVB4Wk5GcHJVSmZpMUU3aDE4cEtjaWlNLWw1MWk1TFRfOVlLR2JXMkxReGlMOHo3UEhFcEprWm5pRnRCZjhMM29QNFRHdUpqemtPOWpNRXlUSVpKV0U3enFXVk9m?oc=5
   - summary_snippet: 광주연구원 “UN AI 허브 유치로 광주 글로벌 AI 거점 도약해야”  더쎈뉴스

11. **[인터뷰] 엘칸토, '브랑누아' 별도 법인으로 스핀오프**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T22:04:00+09:00`
   - matched_query_or_feed: `제조 AI 플랫폼`
   - url: http://www.apparelnews.co.kr/news/news_view/?idx=225419
   - summary_snippet: 제조와 공급망은 기존 엘칸토 인프라와 별개로 차별화된 신규 인프라를 활용하며, 향후 채널 확대를 위한... 플랫폼 내에서도 엘칸토 소속 브랜드와 카니발라이제이션을 최소화하고 타깃과 컨셉을 차별화하는...

12. **소상공인 온라인 판로 지원 '소담스퀘어 울산' 들어선다**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T21:43:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.ulsanpress.net/news/articleView.html?idxno=575840
   - summary_snippet: '소담스퀘어 울산'은 인공지능(AI) 디지털 스튜디오를 비롯해 주방(키친)·다중(멀티)·1인 미디어 스튜디오... 울산시는 울산연구원 빅데이터센터, 울산정보산업진흥원, 울산소상공인연합회 등 지역 유관기관 및...

13. **초대 통합특별시 미래 좌우할 공약, 방점은 '미래 먹거리 산업' 육성에**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T21:28:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: http://www.mdilbo.com/detail/tohfpC/755848
   - summary_snippet: 후보들이 AI(인공지능) 등 미래 먹거리 산업 집중 육성을 통한 특별시 발전 전략을 모색하고 있는 것으로 나타났다. 이재명 정부의 ‘5극 3특 국가균형성장’과 맞물려 산업 대전환 필요성과 함께 데이터센터 유치 등...

14. **[투자를IT다] 2026년 5월 3주차 IT기업 주요 소식과 시장 전망**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T21:24:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://it.donga.com/108937/
   - summary_snippet: 데이터센터와 반도체 자동화 테스트 사업은 AI 인프라 투자에 힘입어 가파른 성장 궤도에 올랐으며, 2027년까지 지속될 것으로 확신한다. 항공우주·방위 분야에서는 각국의 국방 자주권 강화 기조가 다년간의...

15. **[2026 대구경북 이노비즈 기업을 찾아서] (2) 고품질 건강기능식품 전문...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T21:24:00+09:00`
   - matched_query_or_feed: `제조 AI 플랫폼`
   - url: https://www.idaegu.co.kr/news/articleView.html?idxno=549132
   - summary_snippet: 제안하는 'AI 헬스케어 어드바이징 프로그램'을 고도화하고 있으며, 고객 개개인에게 맞춤형 건강 설루션을 제공하는 차세대 플랫폼 구축을 목표로 하고 있다. 에이팜건강은 이 같은 기술 혁신의 원동력은 임직원의...

16. **장수군수 선거, 전·현직 재대결…기본사회 해법은?**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T21:17:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://news.kbs.co.kr/news/pc/view/view.do?ncd=8569474&ref=A
   - summary_snippet: 양수발전소 유치와 햇빛소득마을, AI 데이터센터를 연계해 신재생에너지 소득을 기반으로 한 기본사회로 나아가겠다는 구상입니다. [최훈식/민주당 장수군수 후보 : "기본소득을 바탕으로 해서 의료, 돌봄, 교육, 정주...

17. **사대와 왜색의 굴레 언제 벗을까?**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T21:16:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: http://www.gnmaeil.com/news/articleView.html?idxno=587263
   - summary_snippet: AI 시대에 살고 있다. 잘못된 사대와 왜색의 문화를 바로잡지 못한다면 그 폐해는 눈덩이처럼 불어날 것이다. 왜곡된 정보로 채워진 데이터 센터의 클라우드는 가상의 세계를 혼탁하게 만들 것이다. 그리고 이를 바로...

18. **“스페이스X 투자 놓쳤다?” 또다른 기회…오픈AI 수혜주가 있다 [투자...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T20:41:00+09:00`
   - matched_query_or_feed: `생성형 AI 도입 기업`
   - url: https://biz.heraldcorp.com/article/10743640?ref=naver
   - summary_snippet: [게티이미지] 일론 머스크의 우주기업 스페이스X에 이어 생성형 인공지능(AI) 대표 기업 오픈AI도 기업공개... 이처럼 국내 기업들의 협업 범위가 단순 제휴를 넘어 실제 서비스 도입과 구축 단계까지 확대되면서...

19. **"치유로 잇는 한·베 연대"…봄재단, 고엽제 지원 확대**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T20:40:00+09:00`
   - matched_query_or_feed: `병원 AI 플랫폼`
   - url: https://view.asiae.co.kr/article/2026052520233985334
   - summary_snippet: 협력 플랫폼 구축 방안도 논의했다. 논의 안에는 ▲고엽제 피해 환우 전문 치료·재활 병원 ▲건강검진센터 ▲AI·디지털 헬스케어 기반 예방의학 시스템 ▲줄기세포 연구·치료센터 ▲메디컬 뷰티 시스템 구축 등이...

20. **“스페이스X 투자 놓쳤다?” 또다른 기회…오픈AI 수혜주가 있다 [투자360] - 헤럴드경제**
   - source: `rss`
   - published_at_kst: `2026-05-25T20:40:00+09:00`
   - matched_query_or_feed: `Google News KR 생성형 AI`
   - url: https://news.google.com/rss/articles/CBMiVkFVX3lxTE5ROUE4TW1Sc0JrRS1fV2FhelVMYzQyQ3h2Uk8tbnp5MnpKS2NXVjVLeGo3RGthWWZXTmJiNE40UVlrOU5fbmtqcjRyTWp4dGlsOTAtM1hn?oc=5
   - summary_snippet: “스페이스X 투자 놓쳤다?” 또다른 기회…오픈AI 수혜주가 있다 [투자360]  헤럴드경제


## 다음 단계

1. LLM 후보 품질 확인
2. 노이즈가 많으면 NAVER_QUERIES / RSS_FEEDS 개선
3. 후보가 너무 적으면 MAX_LLM_SOURCES 상향
4. Gemini 3.5 Flash vs 2.5 Flash 품질 비교
5. 나라장터/B2G 수집 추가
6. 담당자/의사결정자 탐색 추가
7. Notion 또는 Google Docs 업로드 추가
