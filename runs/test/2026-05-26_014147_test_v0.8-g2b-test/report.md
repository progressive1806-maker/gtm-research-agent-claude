# FuriosaAI GTM Research Agent Test Run

## 실행 정보

- run_id: `2026-05-26_014147_test_v0.8-g2b-test`
- mode: `test`
- memo: `v0.8-g2b-test`
- executed_at_kst: `2026-05-26T01:49:40.534936+09:00`
- agent_version: `v0.7`
- instructions_loaded_chars: `21592`
- naver_sources_recent_7d_count: `191`
- rss_sources_recent_7d_count: `100`
- merged_sources_recent_7d_count: `291`
- furiosa_docs_successful: `11`
- furiosa_docs_failed: `0`
- llm_called: `True`
- llm_error: ``

## 현재 단계

이 실행은 v0.7 테스트입니다.

이번 버전에서는 네이버 뉴스 API, RSS feed, FuriosaAI 공개 개발자 문서를 수집한 뒤 Gemini로 GTM 후보를 1차 평가하고, 별도 LLM 호출로 매니저용 gtm_report.md를 작성합니다.

아직 나라장터 직접 API, 담당자 심화 탐색, Notion 업로드는 수행하지 않았습니다.

## LLM 실행 요약

- overall_assessment: 최근 7일 동안의 소식을 종합하면, 국내 클라우드 서비스 사업자(CSP/GPUaaS)들의 대형 데이터센터 인프라 투자와 금융/공공 영역의 생성형 AI 플랫폼 구축 수요가 폭발적으로 증가하고 있습니다. 특히 삼성SDS의 구미 60MW 데이터센터 건립 및 동탄 데이터센터 20MW 전력 확보 소식, 우리은행 및 농협은행의 생성형 AI 도입 프로젝트, 그리고 전남소방본부의 Solar LLM 기반 재난 대응 플랫폼 구축 등은 FuriosaAI RNGD 도입의 매우 강력한 GTM 기회입니다. 지원 모델인 Solar 및 EXAONE 기반 솔루션을 확보한 타깃과 데이터센터 전력 고밀도 문제를 겪고 있는 대형 인프라 사업자를 투 트랙으로 정조준하여 적극적인 아웃리치를 전개해야 합니다.
- top_priority_names: 삼성SDS, 엘리스그룹, 건강보험심사평가원, 에코아이티
- noise_ratio_comment: 전반적으로 이번 주 수집된 뉴스는 금융권 및 공공 분야의 대규모 구축 계획과 데이터센터 에너지 공급 이슈가 핵심을 이루어 영업적 가치가 높은 소식이 많았으며, 선거 공약 등 직접 연관성이 낮은 노이즈 기사 비율은 약 10% 미만으로 매우 적은 비중을 차지했습니다.
- model_compatibility_caution: LGAI-EXAONE/EXAONE-4.0 모델은 공식 지원 및 프리컴파일 상태이지만, 농협은행의 기사에서 확인되는 EXAONE 3.5 모델 등은 버전별 세부 최적화 및 아키텍처 정합성이 완벽히 검증되지 않았으므로 영업 제안 시 무조건적인 호환 선언을 피하고 검토 단계를 거치는 신중함이 요구됩니다. 반면 Upstage Solar LLM은 프리컴파일 단계에서 명확히 검증되었으므로 전남소방본부 사업과 같이 Solar를 도입하는 고객사에는 자신감 있는 맞춤형 기술 제안을 적극 진행해도 좋습니다.

## LLM 후보 평가 결과

## 버전 1 — B2B only 우선 검토 요약

- 삼성SDS / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- 엘리스그룹 / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- NH농협은행 / 온프레미스 기업 / classification: `structure_check` / fit: `MID` / outreach: `MID` / 매출시점: `장기`
- 우리은행 / CSP 고객 기업 / classification: `cloud_npuaaS_lead` / fit: `MID` / outreach: `HIGH` / 매출시점: `중기`


## 버전 2 — B2B + B2G 우선 검토 요약

- 삼성SDS / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- 엘리스그룹 / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- 건강보험심사평가원 / 온프레미스 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기` / B2G 근거: `기사/RSS 기반` / 나라장터 확인: `미수행`
- 에코아이티 / CSP 고객 기업 / classification: `priority_outreach` / fit: `HIGH` / outreach: `HIGH` / 매출시점: `단기` / B2G 근거: `기사/RSS 기반` / 나라장터 확인: `미수행`
- 한글과컴퓨터 / 온프레미스 기업 / classification: `structure_check` / fit: `MID` / outreach: `MID` / 매출시점: `중기` / B2G 근거: `기사/RSS 기반` / 나라장터 확인: `미수행`
- NH농협은행 / 온프레미스 기업 / classification: `structure_check` / fit: `MID` / outreach: `MID` / 매출시점: `장기`
- 우리은행 / CSP 고객 기업 / classification: `cloud_npuaaS_lead` / fit: `MID` / outreach: `HIGH` / 매출시점: `중기`


## 상세 후보 평가

### 1. 삼성SDS

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `CSP 운영 기업`
- 분류: `priority_outreach`
- 확인된 프로젝트/시그널: 구미 60MW AI 데이터센터 신축 투자 및 동탄 데이터센터 20MW 전력 확보, 우리은행 AI 에이전트 사업 수주
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 모델 호환성은 미확인 상태이나, 구미 60MW AI 데이터센터 및 동탄 20MW 전력 확보 등 대규모 인프라 확장과 우리은행 AI 에이전트 수주 등의 강력한 비즈니스 모멘텀으로 인해 채널 파트너십 및 인프라 공급 관점의 영업 우선순위는 매우 높습니다.
- hook_type: `CLOUD`
- 핵심 buying signal: 구미시에 대규모 AI 데이터센터 신설을 위해 투자를 진행하며 동탄 데이터센터 전력 확보와 우리은행 우선협상대상자 선정 등 대형 사업을 수주하고 있습니다.
- 인프라 signal: 동탄 데이터센터 가동을 위해 20MW급 전력을 확보하였으며 구미에 4273억원을 투자하여 60MW 규모의 AI 데이터센터를 구축할 계획입니다.
- timing reason: 최근 데이터센터 인프라 확장 투자와 금융권 대형 AI 구축 사업 수주가 잇따르고 있어 GPU 부족에 대응하기 위한 NPU 인프라 제안의 최적기입니다.
- 고객 win: 삼성SDS는 폭발하는 전력 및 인프라 비용 부담 속에서 대규모 AI 데이터센터 운영 효율을 극대화할 수 있습니다. 특히 GPU 공급난 속에서 NPU 기반의 고성능 저전력 추론 인프라를 활용하여 원가 경쟁력과 서비스 안정성을 크게 향상시킬 수 있습니다.
- FuriosaAI win: FuriosaAI는 삼성SDS의 대규모 AI 데이터센터 및 클라우드(SCP) 인프라에 RNGD를 대량 공급하여 핵심적인 하드웨어 파트너로 자리잡을 수 있으며, 금융권 등 다양한 CSP 고객사로의 간접 매출 확장을 도모할 수 있습니다.
- 직접 판매 가능성: `HIGH`
- CSP 경유 판매 가능성: `HIGH`
- NPUaaS 유도 가능성: `HIGH`
- CSP capacity 증설 가능성: `HIGH`
- 수치 근거: 구미 AI 데이터센터 투자 금액 4273억원 (S009) — 근거: 삼성SDS는 경북 구미에 4273억원을 투자해 | 구미 AI 데이터센터 전력 규모 60MW (S009) — 근거: 60MW 규모 AI 데이터센터를 짓기로 했다 | 동탄 데이터센터 전력 확보 규모 20MW (S003) — 근거: 경기 동탄 데이터센터 서관 가동을 위해 20MW급 전력을 확보한
- 컨택 명분: 동탄 데이터센터의 20MW 전력 확보 및 구미 4273억원 투자 기반 60MW 데이터센터 구축 등 하드웨어 확장 상황에서 고전력 GPU를 대체할 저전력 NPU 도입 제안
- 실제 컨택 시 사용할 말: 최근 동탄 데이터센터 20MW 전력 확보 및 구미 4273억원 규모의 60MW AI 데이터센터 투자 소식을 보고 연락드렸습니다. 대규모 데이터센터 가동 시 예상되는 전력 및 냉각 부담을 낮추기 위해, RNGD 가속기를 활용한 저전력·고밀도 추론 플랫폼 도입을 제안드립니다.
- 매출 가능 시점: `단기`
- 담당자 후보 힌트: Head of Cloud, Head of Data Center, 또는 인프라 사업부 임원
- 공개 프로필 URL: https://www.linkedin.com/company/samsung-sds
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 구미 AI 데이터센터 착공 일정 및 세부 서버 조달 계획 | 우리은행 AI 에이전트 인프라의 NPU 도입 가능 여부
- source_ids: S003, S009, S025, S027
- source_urls: https://www.e-science.co.kr/news/articleView.html?idxno=130004 | https://www.mt.co.kr/tech/2026/05/23/2026052210211399740 | https://www.sedaily.com/article/20046605?ref=naver | https://www.sedaily.com/article/20046505?ref=naver

### 2. 엘리스그룹

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `CSP 운영 기업`
- 분류: `priority_outreach`
- 확인된 프로젝트/시그널: 코스닥 상장 추진 및 AI PMDC, ECI 기반 GPUaaS 인프라 비즈니스 본격화
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 적용 모델은 구체적으로 명시되지 않아 모델 적합성은 UNKNOWN으로 평가되나, 모듈형 데이터센터(PMDC) 및 GPUaaS 기반 클라우드 서비스를 적극 확장하며 기업공개를 추진 중인 단계이므로 원가 개선을 위한 하드웨어 다변화 파트너십 구축 관점에서 최우선 접촉 대상입니다.
- hook_type: `PARTNER`
- 핵심 buying signal: 코스닥 상장 예비심사를 청구하며 독자적인 모듈형 데이터센터 및 클라우드 인프라 사업 확장에 적극적으로 투자하고 있습니다.
- 인프라 signal: 이동식 모듈형 데이터 센터(AI PMDC) 및 GPU 자원을 배치하고 관리하는 클라우드 인프라(ECI)를 자체적으로 운영하고 있습니다.
- timing reason: 상장 추진과 함께 클라우드 인프라의 실적 가시성이 중요해진 시점으로, 저비용·고효율 NPU 도입을 통한 마진율 극대화 전략 제안이 효과적인 시기입니다.
- 고객 win: 엘리스그룹은 전력 및 인프라 비용 부담이 큰 상황에서 저전력·고효율의 NPU를 도입하여 클라우드 서비스의 마진율을 향상시킬 수 있습니다. 특히 모듈형 데이터센터의 제한된 전력 한도 내에서 밀도를 높일 수 있습니다.
- FuriosaAI win: FuriosaAI는 상장 단계에 진입하는 유망 클라우드 플랫폼 사업자에게 RNGD를 공급함으로써 실질적인 매출 레퍼런스를 확보하고, NPUaaS 활성화를 위한 전략적 파트너를 확보할 수 있습니다.
- 직접 판매 가능성: `HIGH`
- CSP 경유 판매 가능성: `MID`
- NPUaaS 유도 가능성: `HIGH`
- CSP capacity 증설 가능성: `MID`
- 수치 근거: 없음
- 컨택 명분: 자체 이동식 모듈형 데이터 센터 운영 및 GPUaaS 비즈니스 확장 과정에서 전력 효율 극대화 및 하드웨어 다각화를 위한 RNGD 연동 제안
- 실제 컨택 시 사용할 말: 최근 코스닥 상장 추진 및 모듈형 데이터 센터 인프라 확장 소식을 인상 깊게 보았습니다. 모듈형 데이터 센터의 전력 한계 극대화와 서비스 운영 비용 효율화를 위해, vLLM 및 쿠버네티스 환경에 즉시 호환되는 국산 고성능 NPU 도입 협력을 제안드립니다.
- 매출 가능 시점: `단기`
- 담당자 후보 힌트: 김재원 대표이사 또는 CTO, AI 클라우드 인프라 사업부 리더
- 공개 프로필 URL: https://www.linkedin.com/company/international-data-center-authority-idca
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 자체 PMDC에 배치된 GPU 장비 수량 및 물리적 공간 제약 사항 | RNGD 도입을 위한 가상화 스택 및 쿠버네티스 연동 요건
- source_ids: S012, S013, S014, S015, S016, S017
- source_urls: http://www.hansbiz.co.kr/news/articleView.html?idxno=839792 | http://www.joseilbo.com/news/news_read.php?uid=568639&class=53&grp= | https://www.fetv.co.kr/news/articleView.html?idxno=302765 | https://www.the-stock.kr/news/articleView.html?idxno=32570 | https://www.newspim.com/news/view/20260520000146 | https://www.cstimes.com/news/articleView.html?idxno=706484

### 3. 건강보험심사평가원

- 국가: `KR`
- 시장: `B2G`
- 타깃 유형: `온프레미스 기업`
- 분류: `priority_outreach`
- 확인된 프로젝트/시그널: GPU 서버 기반의 AI 통합플랫폼 구축 추진 및 AI·클라우드 동시 드라이브 가속
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 사용 모델은 확정되지 않았으나 GPU 서버 기반의 AI 통합플랫폼 개발을 추진하고 있어 폐쇄망 및 개인정보 가이드라인을 고려한 공공 의료 인프라 공급 기회로서 영업적 가치가 매우 높습니다.
- hook_type: `PROCUREMENT`
- 핵심 buying signal: 심평원 자체 AI 플랫폼 구축을 통해 GPU 서버 기반의 대민 및 행정 AI 서비스를 원스톱 프로세스로 운영하려는 계획을 가지고 있습니다.
- 인프라 signal: 의료 데이터 및 국민 건강 정보를 다루는 폐쇄형 GPU 인프라와 독자적인 AI 서비스 개발·운영 플랫폼이 필요합니다.
- timing reason: AI 통합플랫폼 구축 드라이브가 본격 시작되고 디지털클라우드센터 및 AI융합추진단 주도의 인프라 구성이 검토되는 중입니다.
- 고객 win: 건강보험심사평가원은 대규모 의료 심사 및 데이터 분석 과정에서 발생하는 엄청난 서버 운영 비용과 전력 문제를 완화할 수 있으며, 정부의 국산 하드웨어 장려 정책과 일치하여 우수한 도입 명분을 가질 수 있습니다.
- FuriosaAI win: FuriosaAI는 최상위 공공 의료 평가 기관에 국산 AI 반도체 기반 플랫폼 아키텍처를 납품하여, 공공 B2G 시장 전체로 파급 효과를 전파할 수 있는 독보적인 상징성을 획득합니다.
- 직접 판매 가능성: `HIGH`
- CSP 경유 판매 가능성: `MID`
- NPUaaS 유도 가능성: `LOW`
- CSP capacity 증설 가능성: `LOW`
- 수치 근거: 없음
- 컨택 명분: GPU 서버 기반 AI 통합플랫폼 구축 단계에 맞춰 공공 의료 보안 규제 적합성 및 운영 단가 절감을 제공하는 국산 NPU 서버 제안
- 실제 컨택 시 사용할 말: 최근 GPU 서버 기반 AI 통합플랫폼 및 클라우드 동시 드라이브 추진 소식을 접하고 연락드렸습니다. 의료 정보 보안과 대규모 민원 분석 업무 환경에서 서버 유지비 및 전력량을 획기적으로 낮출 수 있는 RNGD 가속 솔루션을 소개드리고자 합니다.
- 매출 가능 시점: `단기`
- 담당자 후보 힌트: 김무성 디지털전략실장 (디지털클라우드센터장 겸 AI융합추진단장)
- 공개 프로필 URL: 
- 기존 접점: `확인 필요`
- B2G 근거 유형: `기사/RSS 기반`
- 나라장터 직접 확인: `미수행`
- 조달상 다음 액션: 나라장터/RFP 직접 확인 필요
- 확인 필요: AI 통합플랫폼에 채택 예정인 주력 오픈소스 모델군 | 자체 조달 또는 SI 파트너 선정 시점 및 하드웨어 가점 규정
- source_ids: S034
- source_urls: https://www.etnews.com/20260522000181

### 4. 에코아이티

- 국가: `KR`
- 시장: `B2G`
- 타깃 유형: `CSP 고객 기업`
- 분류: `priority_outreach`
- 확인된 프로젝트/시그널: 전남소방본부 AI 기반 재난 대응 플랫폼 구축 사업 본격 수주 및 개발 착수
- 확인된 모델명: `Solar LLM`
- 모델 매칭 상태: `exact_supported`
- 모델 fit_score: `HIGH`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `HIGH`
- outreach priority: `HIGH`
- fit vs priority 설명: 당사가 완전하게 호환하여 지원하는 SOLAR-10.7B 계열 모델을 주력으로 쿠버네티스 클라우드 상에 재난 대응 소방 행정 서비스와 RAG를 결합 중이므로 기술 적합성 및 비즈니스 전환 가능성이 모두 최상입니다.
- hook_type: `VLLM`
- 핵심 buying signal: 정형 및 비정형 소방행정 데이터를 학습시키고 클라우드 및 RAG 기반 소방 행정 AI 문서 서비스를 개발하기 위해 실제 사업에 착수하였습니다.
- 인프라 signal: 쿠버네티스(K8s) 기반의 클라우드 인프라와 RAG 아키텍처 상에서 유연한 자원 배치와 컨테이너 최적화가 필수적입니다.
- timing reason: 플랫폼 구축 사업이 본격화되어 서비스 최적화 및 가속 하드웨어 적정성 평가가 이루어지는 적절한 시점입니다.
- 고객 win: 에코아이티는 전남소방본부 사업의 서비스 인프라 운영 비용을 큰 폭으로 경감하여 실질 프로젝트 마진을 높일 수 있습니다. 또한, K8s 환경에서 최상의 추론 속도를 보장해 긴급한 재난 대피 및 소방 검색 속도를 확보할 수 있습니다.
- FuriosaAI win: FuriosaAI는 공공 안전 영역의 실제 구체적 솔루션 구축에 당사 프리컴파일 지원 모델(Solar) 레퍼런스를 완벽하게 매칭시켜 단기적인 매출 성과와 공공 수주 성공기를 확보할 수 있습니다.
- 직접 판매 가능성: `HIGH`
- CSP 경유 판매 가능성: `HIGH`
- NPUaaS 유도 가능성: `MID`
- CSP capacity 증설 가능성: `LOW`
- 수치 근거: 없음
- 컨택 명분: K8s 기반 클라우드 상에서 Solar LLM 및 RAG 기반 서비스 가동 시 뛰어난 성능과 저렴한 TCO를 보장하는 RNGD 및 K8s 드롭인 연동 솔루션 제공
- 실제 컨택 시 사용할 말: 최근 전남소방본부의 Solar LLM 기반 재난 대응 플랫폼 구축 소식을 축하드립니다. 저희 가속기는 Solar-10.7B 계열 모델에 대해 최상의 프리컴파일 성능과 K8s 기반 최적 연동을 완벽하게 보장하므로, 본 소방 인프라의 처리 비용 저감 방안을 의논하고자 합니다.
- 매출 가능 시점: `단기`
- 담당자 후보 힌트: 김성훈 대표이사 또는 소방 RAG 프로젝트 PM
- 공개 프로필 URL: https://www.linkedin.com/company/wnsprocurement/
- 기존 접점: `확인 필요`
- B2G 근거 유형: `기사/RSS 기반`
- 나라장터 직접 확인: `미수행`
- 조달상 다음 액션: 나라장터/RFP 직접 확인 필요
- 확인 필요: 전남소방본부 인프라가 민간 퍼블릭 클라우드인지 아니면 공공 자체 클라우드인지 여부 | RNGD 가속기의 K8s 패키지 연동 타당성 사전 기술 리뷰
- source_ids: S028
- source_urls: https://magazine.hankyung.com/business/article/202605196285b

### 5. 한글과컴퓨터

- 국가: `KR`
- 시장: `B2G`
- 타깃 유형: `온프레미스 기업`
- 분류: `structure_check`
- 확인된 프로젝트/시그널: LG AI연구원과 손잡고 '챗엑사원' 결합을 통한 공공 AX 시장 공동 수주 전선 구축
- 확인된 모델명: `EXAONE`
- 모델 매칭 상태: `family_only`
- 모델 fit_score: `MID`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `MID`
- RNGD fit_score: `MID`
- outreach priority: `MID`
- fit vs priority 설명: 지원 아키텍처인 엑사원(EXAONE) 계열을 주력으로 활용하나 구체적인 세부 모델 버전 파악이 요구되므로, 공공망 대상의 온프레미스 공동 영업 기회를 모색하기 위해 아키텍처 검증이 필요한 단계입니다.
- hook_type: `SOVEREIGN`
- 핵심 buying signal: 정부부처 및 공공기관 등을 겨냥한 온프레미스 및 보안 특화 문서 AI 에이전트 시장 진입을 위해 공동 대응 체계를 출범하였습니다.
- 인프라 signal: 공공 및 행정 보안 규정을 충족하는 국가 폐쇄망이나 공공 클라우드 환경 내에서의 배포 및 가속 솔루션이 필요합니다.
- timing reason: 공공 AX 시장 공략을 선언하고 초기 수주 및 영업망 확보를 위해 기술 파트너십을 다지고 있는 시점입니다.
- 고객 win: 한글과컴퓨터는 보안이 생명인 공공 온프레미스 환경에 문서 AI 에이전트를 공급할 때, GPU 대비 저렴하고 강력한 보안 성능을 지닌 국산 하드웨어 패키지를 결합하여 조달 시장에서 강력한 단가 경쟁력을 확보할 수 있습니다.
- FuriosaAI win: FuriosaAI는 국산 문서 오피스 분야의 지배적 사업자인 한컴과의 연동을 통해 공공 및 행정 망분리 프로젝트 진입을 위한 강력한 영업 파트너를 확보하고 대규모 단기 조달 실적을 기대할 수 있습니다.
- 직접 판매 가능성: `MID`
- CSP 경유 판매 가능성: `MID`
- NPUaaS 유도 가능성: `LOW`
- CSP capacity 증설 가능성: `LOW`
- 수치 근거: 없음
- 컨택 명분: 공공 기관 대상의 온프레미스 및 폐쇄망 문서 AI 공급을 타깃으로 엑사원-4.0 모델 기반의 고전력 GPU 대체용 RNGD 서버 결합 패키지 공동 제안
- 실제 컨택 시 사용할 말: 최근 LG AI연구원과의 '챗엑사원' 기반 공공 AX 동맹 소식을 유심히 보았습니다. 공공기관의 민감한 보안 규정과 국산 하드웨어 조달 선호 경향에 대응하기 위해, 당사의 고성능·저전력 RNGD를 결합한 패키지 형태의 온프레미스 어플라이언스 공동 영업을 제안드립니다.
- 매출 가능 시점: `중기`
- 담당자 후보 힌트: 공공사업 담당 임원 또는 AI 에이전트 제품 플랫폼 리드
- 공개 프로필 URL: https://www.linkedin.com/company/procuredesk
- 기존 접점: `확인 필요`
- B2G 근거 유형: `기사/RSS 기반`
- 나라장터 직접 확인: `미수행`
- 조달상 다음 액션: 나라장터/RFP 직접 확인 필요
- 확인 필요: 챗엑사원에 결합되는 엑사원 모델의 구체적인 세부 버전 | 공공 폐쇄망 구축 사업의 서버 조달 및 납품 요건
- source_ids: S020, S021, S022, S023, S024
- source_urls: http://www.newslock.co.kr/news/articleView.html?idxno=130504 | https://www.mt.co.kr/tech/2026/05/22/2026052215283358675 | https://www.mk.co.kr/article/12055579 | https://www.getnews.co.kr/news/articleView.html?idxno=870707 | https://www.newsis.com/view/NISX20260522_0003640664

### 6. NH농협은행

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `온프레미스 기업`
- 분류: `structure_check`
- 확인된 프로젝트/시그널: LG CNS 주도로 엑사원 3.5를 파인튜닝하여 전용 생성형 AI 및 RAG 플랫폼 구축 운영
- 확인된 모델명: `EXAONE 3.5`
- 모델 매칭 상태: `family_only`
- 모델 fit_score: `MID`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `MID`
- RNGD fit_score: `MID`
- outreach priority: `MID`
- fit vs priority 설명: 지원 아키텍처인 엑사원 계열을 전용 AI 서비스에 도입하였으나, 당사 프리컴파일 대상인 EXAONE-4.0 버전과의 차이인 EXAONE 3.5 버전을 사용하므로 실무 검증 및 파인튜닝 호환성에 대한 사전 구조 파악이 요구되어 구조 확인 단계로 설정하였습니다.
- hook_type: `SOVEREIGN`
- 핵심 buying signal: 은행 업무 규정과 내부 자료 검색을 위해 전용 프라이빗 RAG 플랫폼을 전사 구축하여 운영 중인 단계입니다.
- 인프라 signal: 망분리 규제를 적용받는 은행 업무망의 폐쇄적인 보안 환경 내에서 기밀 데이터를 처리할 독자적인 전용 서버 인프라가 필수적입니다.
- timing reason: 내부 규정 검색 및 영업 지원 AI 플랫폼 고도화를 가속화하며 전사 확산 단계에 도달해 안정적인 서버 연산량 확보가 중요해진 시점입니다.
- 고객 win: NH농협은행은 내부 업무 처리 시 발생하는 고비용의 인프라 연산 비용을 대폭 낮출 수 있습니다. 또한, 폐쇄망 내부에서 완벽하게 구동되는 국산 NPU 서버를 장착함으로써 규제 준수 및 금융 혁신 모델 개발에 기여할 수 있습니다.
- FuriosaAI win: FuriosaAI는 대형 시중은행의 프라이빗 AI 추론 인프라에 RNGD를 안착시킴으로써 엄격한 금융 보안 검증을 통과한 국산 대표 NPU로서 위상을 입증하고 금융 수주 가시성을 증폭시킬 수 있습니다.
- 직접 판매 가능성: `MID`
- CSP 경유 판매 가능성: `MID`
- NPUaaS 유도 가능성: `LOW`
- CSP capacity 증설 가능성: `LOW`
- 수치 근거: 없음
- 컨택 명분: 금융 폐쇄망 상에 구축된 엑사원 3.5 기반 RAG 플랫폼의 고정적인 클라우드 비용을 저감하고 속도를 높일 수 있는 RNGD 금융 서버 결합 솔루션 구조 제시
- 실제 컨택 시 사용할 말: 최근 엑사원 모델을 활용한 RAG 플랫폼 구축 및 전사 업무 혁신 소식을 관심 깊게 보았습니다. 은행 내부 폐쇄망 환경에서 대규모 자산 보고서 분석과 검색증강생성(RAG) 트래픽 처리 비용을 완화하기 위해, 당사 RNGD 기반의 프라이빗 AI 추론 인프라 도입 타당성 검토를 제안드립니다.
- 매출 가능 시점: `장기`
- 담당자 후보 힌트: CIO, CTO, CDO, 또는 금융 디지털 트랜스포메이션 사업부장
- 공개 프로필 URL: https://kr.linkedin.com/company/nonghyup-bank
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 엑사원 3.5 모델에 대한 당사 RNGD의 하이퍼파라미터 최적화 및 서빙 호환성 | 농협은행 전용 AI 시스템 구축을 담당한 LG CNS 파트너 채널 연동성
- source_ids: S019
- source_urls: https://www.news2day.co.kr/article/20260522500024

### 7. 우리은행

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `CSP 고객 기업`
- 분류: `cloud_npuaaS_lead`
- 확인된 프로젝트/시그널: AI 에이전트 구축 사업 추진 및 우선협상대상자로 삼성SDS 선정
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `MID`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 모델 정합성은 미확인 상태이나 우선협상대상자인 삼성SDS를 경유하여 금융 플랫폼 상에 AI 추론 수요를 일으킬 수 있는 핵심 바이어이므로, 삼성SDS 채널을 연계한 공동 영업 전략 관점에서 높은 영업 우선순위를 가집니다.
- hook_type: `PARTNER`
- 핵심 buying signal: 금융망 내부의 AI 에이전트 및 자산분석 보고서 자동화 플랫폼 구축을 추진하며 우선협상대상자를 지정하였습니다.
- 인프라 signal: 금융 보안 규제 준수를 고려한 하이브리드 환경 또는 프라이빗 클라우드 상에서의 고신뢰 추론 시스템이 요구됩니다.
- timing reason: 우선협상대상자가 최근 선정되어 상세 인프라 아키텍처 및 하드웨어 구성 논의가 진행 중인 시점입니다.
- 고객 win: 우리은행은 AI 에이전트 도입에 따른 트래픽 처리 비용을 경감하고, 금융 보안 가이드라인에 부합하는 안정적이고 신속한 응답 속도를 가진 추론 인프라를 확보할 수 있습니다.
- FuriosaAI win: FuriosaAI는 삼성SDS의 클라우드 플랫폼을 경유하여 금융권 고객사에 NPUaaS 추론 레퍼런스를 확보하고, 대기업 CSP가 당사 NPU 용량을 증설하도록 유도할 수 있습니다.
- 직접 판매 가능성: `LOW`
- CSP 경유 판매 가능성: `HIGH`
- NPUaaS 유도 가능성: `HIGH`
- CSP capacity 증설 가능성: `HIGH`
- 수치 근거: 없음
- 컨택 명분: 삼성SDS 컨소시엄의 우선협상대상자 선정에 대응하여 금융권 특화 AI 추론 시 고비용 GPU를 대체할 고효율 NPU 인프라 아키텍처 역제안
- 실제 컨택 시 사용할 말: 최근 AI 에이전트 구축 사업의 우선협상대상자로 삼성SDS가 선정된 건을 기쁘게 생각합니다. 금융 업무 특유의 철저한 보안 규정과 트래픽 처리를 위해, 삼성SDS SCP 인프라와 연계된 초고속·고효율의 NPU 가속 환경 도입 방안을 제안드리고자 합니다.
- 매출 가능 시점: `중기`
- 담당자 후보 힌트: CIO, CTO, CDO, 또는 금융 플랫폼 사업부 의사결정자
- 공개 프로필 URL: https://www.linkedin.com/company/stockinsights-ai
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: AI 에이전트 서비스에 적용될 기반 LLM 아키텍처 정보 | 망분리 환경 완화 시점과 클라우드 연동 범위
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

1. **[시론] AI로 빼앗기는 '성장 사다리'**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T00:24:00+09:00`
   - matched_query_or_feed: `생성형 AI 도입 기업`
   - url: https://www.hankyung.com/article/2026052573951
   - summary_snippet: 2022년 11월 챗GPT가 등장한 이후 생성형 인공지능(AI)이 폭발적으로 확산됐다. 한국은행이 최근 발표한 ‘AI... 셋째, 기업의 AI 도입을 ‘인력 절감’이 아니라 ‘인간+AI 생산성’ 기준으로 평가해야 한다. 사람을...

2. **유가·물가 숨 돌려도 고환율 지속 우려… 韓경제 뇌관은 ‘반도체’**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T00:22:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.kmib.co.kr/article/view.asp?arcid=1779700492&code=11151100&cp=nv
   - summary_snippet: 양 교수는 “미국 금리 인상으로 자국 내 AI 데이터센터 건설이 둔화할 경우 국내 반도체 수출에도 악영향을 미칠 수밖에 없다”고 우려했다. 한국은행의 기준금리 결정이 신중해야 한다는 제언도 나왔다. 내수 침체와...

3. **[중앙시평] 인공지능이 스스로 진화할 때**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T00:20:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.joongang.co.kr/article/25431189
   - summary_snippet: 우선 여러 기업이 개발하고 있는 AI 모델들을 하나로 통합해 국가 AI 챔피언을 키워볼 수 있고, 중국 내 데이터 센터들을 국영화해 범국가적 데이터 센터를 구축해 볼 수도 있겠다. 하지만 만약 그런 방식을 사용해도...

4. **연휴주말 김진태 후보 동분서주⋯‘반도체·AI데이터센터’ 지역맞춤형...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T00:07:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.kwnews.co.kr/page/view/2026052550159200000
   - summary_snippet: 국민의힘 김진태 강원지사 후보가 공식 선거운동 첫 주말·연휴를 맞아 ‘원주 반도체 비전’과 ‘강릉AI데이터센터’ 등 미래 먹거리 공약을 내세워 표심을 집중 공략했다. 김진태 후보는 지난 22~25일 주말·연휴를...

5. **정청래 대표부터 국회의원, 배우까지⋯민주 강원 지역 전방위 지원유세**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T00:06:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.kwnews.co.kr/page/view/2026052550145500000
   - summary_snippet: 정 대표는 이날 “우상호 후보는 아직 당선도 되기 전에 AI 데이터센터 투자 유치와 같은 굵직한 사업들을 직접 추진하고 있다”며 “보통은 당선 이후 일을 시작한다고 생각하는데 후보 때부터 이렇게 일하는 사람은...

6. **춘천시장 1번 공약 입맞춰 “산업·경제”⋯육동한 “첨단 융합 클러스...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T00:05:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.kwnews.co.kr/page/view/2026052550122300000
   - summary_snippet: 육동한 후보는 선거관리위원회에 5대 공약을 제출하며 ‘바이오·AI·양자·데이터를 결합한 첨단 산업 융합... 정 후보는 수열에너지 클러스터와 연계한 데이터 센터 유치, 강원권 반도체 공동 연구소와 특화 인력 양성센터...

7. **[선택 2026 강원] 골목골목 현장서 찾는 답 "해야 할 일 보일수록 설렌다...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T00:05:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.kado.net/news/articleView.html?idxno=2052090
   - summary_snippet: 우 후보는 "강릉과 동해 사이 AI 데이터센터 설립을 확정했다"며 "최대 70조원이 투자되는 국가 프로젝트다. 동해 예산이 7000억원 정도인데 70조 중 일부만 풀려도 동해는 대박나는 거 아니겠느냐"고 말했다. 현장 반응은...

8. **통합특별시 성패, 결국 ‘기업 유치’에 달렸다**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T00:04:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: http://www.kwangju.co.kr/article.php?aid=1779721200799342131
   - summary_snippet: 막대한 전력이 소요되는 반도체, AI, 데이터센터에는 전남의 재생에너지를 공급할 수 있다. 미래모빌리티는 광주가 갖고 있는 자동차 산업 기반과 결합된다. KENTECH와 GIST 는 첨단 기업의 연구개발(R&D) 파트너가 된다....

9. **황기연號 수출입은행, ‘KEXIM AI’ 구축…신용평가 AX 속도 [금융권 AI ...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T00:02:00+09:00`
   - matched_query_or_feed: `생성형 AI 도입 기업`
   - url: http://www.fntimes.com/html/view.php?ud=202605250743058272dd55077bc2_18
   - summary_snippet: 수은은 이를 통해 비대면 대출·보증 심사 프로세스 단축과 해외 진출 중소기업 대상 맞춤형 상담지원 서비스 강화 등이 가능할 것으로 기대하고 있다. 수은 관계자는 "업무에 AI를 도입함으로써 업무 방식 혁신과...

10. **When AI evolves on its own**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T00:01:00+09:00`
   - matched_query_or_feed: `private AI`
   - url: https://koreajoongangdaily.joins.com/news/2026-05-26/opinion/columns/When-AI-evolves-on-its-own/2600329
   - summary_snippet: That background makes the naming of the latest AI model introduced by Anthropic on April 7... government and certain private companies may now possess tools capable of disrupting foreign...

11. **연휴주말 김진태 후보 동분서주⋯‘반도체·AI데이터센터’ 지역맞춤형 공약 집중 - 강원일보**
   - source: `rss`
   - published_at_kst: `2026-05-26T00:01:00+09:00`
   - matched_query_or_feed: `Google News KR AI 데이터센터`
   - url: https://news.google.com/rss/articles/CBMiZEFVX3lxTE41NHVyX2lpQ3YtV3doYmFKSGZSZEJFUkJhU1hZdDBDckNhcGZkRHZBbUlVNGhaaGVVcHotbUQ4YWQ4am1XblRNTmRlcmE4V21HSVNJREs1THZVTGxneTNHRFFVYzM?oc=5
   - summary_snippet: 연휴주말 김진태 후보 동분서주⋯‘반도체·AI데이터센터’ 지역맞춤형 공약 집중  강원일보

12. **로보티즈, 움직이는 AI 시대 핵심 부품주 되나...휴머노이드 시장 주목**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T00:00:00+09:00`
   - matched_query_or_feed: `제조 AI 플랫폼`
   - url: https://www.cbci.co.kr/news/articleView.html?idxno=576986
   - summary_snippet: 일부 투자자들 사이에서는 로봇 부품 플랫폼 기업으로 자리매김할 경우 수조 원대 밸류에이션 가능성이... 미국 빅테크 기업들과 글로벌 제조사들이 차세대 AI 로봇 개발 경쟁에 뛰어들면서 구동계 핵심 부품 기업들에 대한...

13. **장민영號 기업은행, ‘IBK GenAI’ AX 가속…기업금융 혁신 [금융권 AI 人포그래픽] - 한국금융신문**
   - source: `rss`
   - published_at_kst: `2026-05-26T00:00:00+09:00`
   - matched_query_or_feed: `Google News KR 생성형 AI`
   - url: https://news.google.com/rss/articles/CBMifEFVX3lxTE45TXlCcFRKSVJuc2x6eTJ2U0w5bWpmUE9aUXh1YjVOMmdLLW5idlIyWjF2WURwWFVoc1ZmM3lqaVRYb1lKQ2Z6TkN6d1FNa3FLMFBDZHZ3Q1VYM3pUTGpDS001VkY4OVhWblZpYVgwVVBia1ZQazY0bzlEMno?oc=5
   - summary_snippet: 장민영號 기업은행, ‘IBK GenAI’ AX 가속…기업금융 혁신 [금융권 AI 人포그래픽]  한국금융신문

14. **[서학!스타] 포엣테크놀로지, AI 광통신 수혜 기대감 커지나…데이터센터 투자 확대에 변동성 주목 - CBC뉴스**
   - source: `rss`
   - published_at_kst: `2026-05-26T00:00:00+09:00`
   - matched_query_or_feed: `Google News KR AI 데이터센터`
   - url: https://news.google.com/rss/articles/CBMiaEFVX3lxTE1tQ3ktb0lTazBrT1JLaEFsUXl3ZVJvdU9sRzFjMDdkeGdSdVkyR2VPUVlPeDZ5ZmZQY2l3SERzaXoxRWF1RDBSNFRtS3hzdzlZT2JLY2lGSnRVNUxtVGVEaXhhTXB0T0RE?oc=5
   - summary_snippet: [서학!스타] 포엣테크놀로지, AI 광통신 수혜 기대감 커지나…데이터센터 투자 확대에 변동성 주목  CBC뉴스

15. **이원택 민주당 전북도지사 후보 "군산에 '전북성장공사' 설립"**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T23:29:00+09:00`
   - matched_query_or_feed: `제조 AI 플랫폼`
   - url: https://news.tf.co.kr/read/national/2325965.htm
   - summary_snippet: 피지컬AI, RE100, 재생에너지, 데이터센터, 첨단제조, 농생명 바이오 등 미래산업에 전략적으로 투자하고, 기업·금융·인재·기술을 연결해 전북의 성장 구조 자체를 바꾸는 산업·투자 중심 성장 플랫폼이다. 이 후보는...

16. **AI로 가장 먼저 대체될 직업은?…업종별 AI 대체 기상도 나왔다**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T23:17:00+09:00`
   - matched_query_or_feed: `금융 생성형 AI`
   - url: https://www.munhwa.com/article/11591124?ref=naver
   - summary_snippet: 생성형 인공지능(AI)의 급격한 확산 속에서 건설이나 생산직과 같은 현장 기술 중심의 직업이 가장... 미생물학자나 금융분석가처럼 AI를 통해 업무 효율을 극대화할 수 있는 직업들도 존재하기 때문이다. 예를 들어...

17. **06화 엔비디아(NVIDIA) 중심의 AI 데이터센터 - 브런치**
   - source: `rss`
   - published_at_kst: `2026-05-25T22:57:52+09:00`
   - matched_query_or_feed: `Google News KR AI 데이터센터`
   - url: https://news.google.com/rss/articles/CBMiS0FVX3lxTE16SUstU3dCN3hNWElUaGVaandPeXBtWUdxMDZKNXhZbnJ6ZWkwVzhrVlcxWnpwSHZidFpIREVJVko5a0FCSDdNY3FnUQ?oc=5
   - summary_snippet: 06화 엔비디아(NVIDIA) 중심의 AI 데이터센터  브런치

18. **'한국형 크라켄' 나온다…기후부, '에너지 AI' 도입 본격화**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T22:44:00+09:00`
   - matched_query_or_feed: `클라우드 AI 서비스`
   - url: https://daily.hankooki.com/news/articleView.html?idxno=1370369
   - summary_snippet: 영국 옥토퍼스 에너지의 플랫폼에서 착안한 '한국형 크라켄' 에너지 AI서비스 도입한다. 한국형 크라켄은... 정부는 공공과 민간이 데이터를 안전하게 공유할 수 있도록 보안성이 뛰어난 '커뮤니티 클라우드'를 검토...

19. **[조선규의 문제 핵심] AI 황금기 뒤 숨은 진실 '속도와 전력' 벽 깨야**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T22:44:00+09:00`
   - matched_query_or_feed: `AI 추론 비용`
   - url: https://www.newsclaim.co.kr/news/articleView.html?idxno=3064585
   - summary_snippet: 빠른 추론을 구현했고, 국내 리벨리온, 퓨리오사AI 등도 NPU 영역을 개척 중이다. 중요한 사실은 어떤 연산... 하드웨어 비용 부담을 줄이기 위해 구글이 발표한 '터보컨트(TurboQuant)' 등 소프트웨어 압축 알고리즘도...

20. **에이수스, 하이브리드 에이전틱 AI 인프라 공개…추론 비용 최대 70% 절...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T22:42:00+09:00`
   - matched_query_or_feed: `생성형 AI 도입 기업`
   - url: https://www.aitimes.kr/news/articleView.html?idxno=40186
   - summary_snippet: 온프레미스 배포에 최적화된 이 아키텍처는 기업이 생성형 AI 애플리케이션을 도입할 때 성능과 비용의 균형을 맞출 수 있도록 설계됐다. 최근 대형언어모델(LLM)과 AI 에이전트 기반 애플리케이션 도입이...


## 다음 단계

1. LLM 후보 품질 확인
2. 노이즈가 많으면 NAVER_QUERIES / RSS_FEEDS 개선
3. 후보가 너무 적으면 MAX_LLM_SOURCES 상향
4. Gemini 3.5 Flash vs 2.5 Flash 품질 비교
5. 나라장터/B2G 수집 추가
6. 담당자/의사결정자 탐색 추가
7. Notion 또는 Google Docs 업로드 추가
