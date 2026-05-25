# FuriosaAI GTM Research Agent Test Run

## 실행 정보

- run_id: `2026-05-26_033640_test_v0.9-report-quality-test`
- mode: `test`
- memo: `v0.9-report-quality-test`
- executed_at_kst: `2026-05-26T03:42:35.376339+09:00`
- agent_version: `v0.7`
- instructions_loaded_chars: `21592`
- naver_sources_recent_7d_count: `192`
- rss_sources_recent_7d_count: `234`
- merged_sources_recent_7d_count: `426`
- furiosa_docs_successful: `11`
- furiosa_docs_failed: `0`
- llm_called: `True`
- llm_error: ``

## 현재 단계

이 실행은 v0.7 테스트입니다.

이번 버전에서는 네이버 뉴스 API, RSS feed, FuriosaAI 공개 개발자 문서를 수집한 뒤 Gemini로 GTM 후보를 1차 평가하고, 별도 LLM 호출로 매니저용 gtm_report.md를 작성합니다.

아직 나라장터 직접 API, 담당자 심화 탐색, Notion 업로드는 수행하지 않았습니다.

## LLM 실행 요약

- overall_assessment: 최근 7일간 국내 GTM 신호는 금융권 망분리 규제 완화 조치와 의료, 공공 기관의 폐쇄망 AI 도입 흐름이 두드러집니다. 특히 대형 CSP들의 인프라 확장 및 신규 데이터센터 투자 발표가 이어지고 있어, 직접 판매뿐 아니라 CSP를 경유한 NPUaaS 공급 기회를 적극 도모해야 합니다. 모델 정보가 기사 내에 명시되지 않은 경우가 많아 적합도 평가는 보수적으로 진행하되, 인프라 및 바이어 신호가 확실한 타깃 위주로 우선순위를 지정하였습니다.
- top_priority_names: 삼성SDS, 건강보험심사평가원, 서울아산병원, 엘리스그룹
- noise_ratio_comment: 수집된 소스 중 선거 공약, 해외 빅테크 단순 인프라 확장, 일반 플랫폼 민원 관련 기사 등 GTM과 무관한 노이즈가 약 15% 수준으로 분류되었습니다.
- model_compatibility_caution: 대다수 공개 기사에서 구체적인 LLM 모델 버전이 언급되지 않아 모델 매칭 상태를 'unknown'으로 분류하고 보수적인 적합도를 부여하였습니다. 실제 접촉 시 사용 모델(Llama-3.1/3.3, Qwen2.5/3 등 RNGD 지원 모델)에 대한 정밀 확인이 수반되어야 합니다.

## LLM 후보 평가 결과

## 버전 1 — B2B only 우선 검토 요약

- 삼성SDS / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `중기`
- 서울아산병원 / 온프레미스 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `중기`
- 두산 / CSP 고객 기업 / classification: `structure_check` / fit: `MID` / outreach: `MID` / 매출시점: `장기`
- 엘리스그룹 / CSP 운영 기업 / classification: `cloud_npuaas_lead` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`


## 버전 2 — B2B + B2G 우선 검토 요약

- 삼성SDS / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `중기`
- 건강보험심사평가원 / 온프레미스 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기` / B2G 근거: `기사/RSS 기반` / 나라장터 확인: `미수행`
- 서울아산병원 / 온프레미스 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `중기`
- 두산 / CSP 고객 기업 / classification: `structure_check` / fit: `MID` / outreach: `MID` / 매출시점: `장기`
- 디토닉 / 온프레미스 기업 / classification: `structure_check` / fit: `MID` / outreach: `MID` / 매출시점: `장기` / B2G 근거: `기사/RSS 기반` / 나라장터 확인: `미수행`
- 오픈네트웍시스템 / CSP 고객 기업 / classification: `watchlist` / fit: `MID` / outreach: `MID` / 매출시점: `장기` / B2G 근거: `기사/RSS 기반` / 나라장터 확인: `미수행`
- 엘리스그룹 / CSP 운영 기업 / classification: `cloud_npuaas_lead` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`


## 상세 후보 평가

### 1. 삼성SDS

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `CSP 운영 기업`
- 분류: `priority_outreach`
- 확인된 프로젝트/시그널: 경기 동탄 및 경북 구미 AI 데이터센터 인프라 확장 및 GPUaaS/NPUaaS 사업 추진
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 공개 기사 내 구체적인 구동 모델은 미확인 상태이나, 신규 AI 데이터센터 전력 확보 및 대규모 인프라 투자 신호가 매우 강력합니다. SCP 및 NPUaaS 가속기 파트너십 경로를 통한 용량 증설 목적으로 접근하므로 모델 정합성과 무관하게 outreach priority를 최고 등급으로 설정하였습니다.
- hook_type: `CLOUD`
- 핵심 buying signal: 경북 구미에 대규모 투자를 통한 신규 AI 데이터센터 건립 계획을 발표하였으며 동탄 데이터센터 가동을 위한 추가 전력을 확보하는 등 클라우드 인프라 자원을 지속적으로 확충하고 있습니다.
- 인프라 signal: 구미 데이터센터의 전력 용량 및 동탄 데이터센터의 가동 전력 확보 등 하이퍼스케일급 데이터센터 인프라를 직접 운영하고 있습니다.
- timing reason: 최근 AI 데이터센터 투자 확대 분석 및 증권사 호평이 이어지는 시점으로, 전력 수급 및 가속기 비용 효율화가 시급한 시점입니다.
- 고객 win: 대규모 전력 인프라 확보에 따른 운영비 부담을 경감할 수 있으며, 고효율 추론용 NPUaaS 라인업을 추가하여 클라우드 서비스 경쟁력을 강화할 수 있습니다.
- FuriosaAI win: 삼성SDS 클라우드 플랫폼인 SCP에 가속기를 공급하여 엔터프라이즈향 대형 레퍼런스를 확보하고 지속적인 capacity 증설 매출을 기대할 수 있습니다.
- 직접 판매 가능성: `LOW`
- CSP 경유 판매 가능성: `HIGH`
- NPUaaS 유도 가능성: `HIGH`
- CSP capacity 증설 가능성: `HIGH`
- 수치 근거: 동탄 데이터센터 가동을 위한 20MW급 전력 확보 (S028) — 근거: 삼성SDS가 경기 동탄 데이터센터 서관 가동을 위해 20MW급 전력을 확보한 사례 | 경북 구미 데이터센터 건립을 위한 4273억원 투자 및 60MW 전력 계획 (S034) — 근거: 삼성SDS는 경북 구미에 4273억원을 투자해 60MW 규모 AI 데이터센터를 짓기로 했다.
- 컨택 명분: 동탄 및 구미의 하이퍼스케일급 AI 데이터센터 전력 확보와 인프라 증설 타이밍에 맞추어 저전력 고효율 추론 카드 도입을 제안하기 위함입니다.
- 실제 컨택 시 사용할 말: 최근 구미 AI 데이터센터에 대한 4273억원 규모의 투자 및 동탄 데이터센터의 20MW 전력 확보 소식을 접하고 연락드렸습니다. 전력 밀도 최적화가 요구되는 대형 인프라 환경에서 RNGD가 제공하는 전력 대비 고성능 추론 효율성과 가상화 적합성을 바탕으로 SCP의 NPUaaS 경쟁력 확보 방안을 논의하고자 합니다.
- 매출 가능 시점: `중기`
- 담당자 후보 힌트: Head of Cloud, Head of Data Center, 인프라 개발 부서 담당 이사
- 공개 프로필 URL: https://www.linkedin.com/company/samsung-sds
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 삼성SDS 클라우드 인프라 부서 내 국산 NPUaaS 가속기 검토 현황 분석 필요
- source_ids: S028, S030, S034, S035, S038
- source_urls: https://www.e-science.co.kr/news/articleView.html?idxno=130004 | https://www.ddaily.co.kr/page/view/2026052017342600376 | https://www.mt.co.kr/tech/2026/05/23/2026052210211399740 | https://www.thepowernews.co.kr/view.php?ud=202605221116568858de3f0aa1be_7 | http://www.newsroad.co.kr/news/articleView.html?idxno=59549

### 2. 건강보험심사평가원

- 국가: `KR`
- 시장: `B2G`
- 타깃 유형: `온프레미스 기업`
- 분류: `priority_outreach`
- 확인된 프로젝트/시그널: GPU 서버 기반 자체 AI 통합플랫폼 구축 및 AI·클라우드 도입 가속화
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `MID`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 기사상 도입 예정 모델은 구체적으로 명시되지 않았으나, 공공 보건의료 영역에서 대형 GPU 인프라를 온프레미스로 직접 도입하여 개발과 운영 체계를 일원화하려는 실질적인 인프라 구축 신호입니다.
- hook_type: `PROCUREMENT`
- 핵심 buying signal: 자체 AI 통합플랫폼을 GPU 서버 기반으로 구축하여 원스톱 서비스 개발 및 운영 프로세스를 구현하겠다는 계획을 구체적으로 발표하였습니다.
- 인프라 signal: 자체 디지털클라우드센터 및 GPU 기반 AI 인프라를 원격 혹은 자체 전산실에 직접 구성하려는 인프라 신호가 뚜렷합니다.
- timing reason: AI융합추진단 주도의 AI 플랫폼 구축 사업 기획 단계로, 조달 발주 또는 규격 설계 시점에 선제적 대응이 가능합니다.
- 고객 win: 정부 예산 한도 내에서 가속기 도입 효율성을 보장하고, 고전력 소모를 방지하여 원내 전력 제약을 완화할 수 있습니다.
- FuriosaAI win: 공공 의료 분야의 대표적인 대형 GPU/NPU 통합 구축 사례를 선점하여 B2G 시장에서의 입지를 확보할 수 있습니다.
- 직접 판매 가능성: `MID`
- CSP 경유 판매 가능성: `MID`
- NPUaaS 유도 가능성: `LOW`
- CSP capacity 증설 가능성: `LOW`
- 수치 근거: 없음
- 컨택 명분: GPU 기반 자체 AI 통합플랫폼 기획에 발맞추어 저전력 고효율 서버형 가속기 설계 규격 반영을 유도하기 위함입니다.
- 실제 컨택 시 사용할 말: 최근 심평원의 디지털클라우드센터와 AI융합추진단이 추진하시는 GPU 서버 기반 AI 통합플랫폼 구축 소식을 접하였습니다. 의료 및 행정 서비스 추론 환경에서 비용과 전력 효율성을 균형 있게 확보할 수 있는 국산 NPU 가속기 RNGD 도입 가치를 공유해 드리고자 합니다.
- 매출 가능 시점: `단기`
- 담당자 후보 힌트: 김무성 디지털전략실장 겸 AI융합추진단장, 정보화본부 IT 인프라 도입 담당자
- 공개 프로필 URL: 
- 기존 접점: `확인 필요`
- B2G 근거 유형: `기사/RSS 기반`
- 나라장터 직접 확인: `미수행`
- 조달상 다음 액션: 나라장터/RFP 직접 확인 필요
- 확인 필요: 심평원 자체 인프라 장비 조달 방식 및 선호하는 사업자 정보 확인 필요
- source_ids: S004
- source_urls: https://www.etnews.com/20260522000181

### 3. 서울아산병원

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `온프레미스 기업`
- 분류: `priority_outreach`
- 확인된 프로젝트/시그널: 의료 정보 보안 강화를 위한 폐쇄망 환경 AI 시스템 구축
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `MID`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 사용 모델에 관한 명확한 정보는 없으나 병원 내부 보안 가이드라인에 따른 폐쇄망 온프레미스 AI 가동이 확정된 구조입니다. 컴플라이언스 및 배치 적합성이 우수하므로 우선 지원 대상군으로 설정하였습니다.
- hook_type: `SOVEREIGN`
- 핵심 buying signal: 폐쇄망 환경에서도 의료 AI 프로토콜을 온전히 가동할 수 있는 시스템을 구축하였음을 공식적으로 확인해 주었습니다.
- 인프라 signal: 병원 전산망 특성상 외부 연결이 완전 차단된 독립적 온프레미스 서버 인프라를 운용하고 있습니다.
- timing reason: 폐쇄망 내부 AI 적용 성공 사례를 확보한 상태이므로 타 분과 및 타 의료 플랫폼으로의 추가 장비 확장 영업이 용이합니다.
- 고객 win: 민감한 환자 정보 유출 위협이 없는 완벽한 원내 독립형 온프레미스 환경에서 인공지능 연산 장치 비용을 개선할 수 있습니다.
- FuriosaAI win: 대형 상급종합병원의 대표적인 보안 전술용 추론 플랫폼에 탑재되는 하드웨어 납품 실적을 확보할 수 있습니다.
- 직접 판매 가능성: `HIGH`
- CSP 경유 판매 가능성: `LOW`
- NPUaaS 유도 가능성: `LOW`
- CSP capacity 증설 가능성: `LOW`
- 수치 근거: 없음
- 컨택 명분: 의료 프라이버시가 엄격한 원내 폐쇄망 인프라 고도화 시점에 저전력 PCIe 서버 카드 도입을 타진하기 위함입니다.
- 실제 컨택 시 사용할 말: 아산병원의 디지털정보혁신본부에서 폐쇄망 환경을 기반으로 보안과 인공지능 적용을 양립시킨 성공 사례를 접하였습니다. 고성능 병원 내부 데이터 처리를 외부 클라우드 의존 없이 수행하기 위해 국산 추론 전용 가속기 도입에 관해 협의를 희망합니다.
- 매출 가능 시점: `중기`
- 담당자 후보 힌트: 김영학 디지털정보혁신본부장, 의료정보실 인프라 관리 부서
- 공개 프로필 URL: 
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 현재 폐쇄망 서버에 사용 중인 서버 장비 제조업체 및 추가 증설 계획 존재 여부 검증
- source_ids: S011
- source_urls: https://www.newsis.com/view/NISX20260518_0003634573

### 4. 두산

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `CSP 고객 기업`
- 분류: `structure_check`
- 확인된 프로젝트/시그널: 엔터프라이즈 멀티클라우드 기반 인프라 운영 및 자체 AI 활용 로드맵 구현
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `MID`
- 채널/CSP fit_score: `MID`
- RNGD fit_score: `MID`
- outreach priority: `MID`
- fit vs priority 설명: 특정 AI 모델을 단정할 수는 없으나, 복수의 퍼블릭 클라우드 및 외산 가속기를 운영해 본 숙련도 높은 조직으로 향후 비용 효율적 인프라 대체를 위한 구조 검토 단계입니다.
- hook_type: `SCALE`
- 핵심 buying signal: 과거 세대부터 최근 세대까지 다양한 범위의 인프라를 대기업 엔터프라이즈 스케일에서 다뤄온 연산 자원 관리 경험을 축적하고 있습니다.
- 인프라 signal: 다각적인 퍼블릭 클라우드 서비스 및 가속 하드웨어 연동을 수행하는 하이브리드 클라우드 형태를 취하고 있습니다.
- timing reason: 클라우드 서비스 최적화 서밋 등에서 자사 아키텍처를 소개한 만큼, 실질적인 운용 단계의 비효율 개선 방안 수립 시기입니다.
- 고객 win: 기존의 외산 가속기 가용성 부담을 경감하고, 자체 생성형 인프라 운영에 들어가는 고정비 지출을 조절할 수 있습니다.
- FuriosaAI win: 전통 제조 대기업의 IT 계열사 및 공통 전산 환경에 진입할 수 있는 비즈니스 네트워크 통로를 개척할 수 있습니다.
- 직접 판매 가능성: `LOW`
- CSP 경유 판매 가능성: `HIGH`
- NPUaaS 유도 가능성: `MID`
- CSP capacity 증설 가능성: `LOW`
- 수치 근거: 없음
- 컨택 명분: 대형 인프라 운영 중 발생하는 고정 비용을 개선하기 위하여 가용 대안으로서 저비용 추론 가속기 옵션을 소개하기 위함입니다.
- 실제 컨택 시 사용할 말: 귀사의 축적된 고성능 컴퓨팅 및 대규모 인프라 운영 성공 사례를 주의 깊게 분석해 왔습니다. 멀티클라우드 최적화를 수행하시는 여정에서 추론 워크로드 중심의 경제성을 추가로 확보할 수 있도록 당사의 가속 솔루션 검토를 권해 드립니다.
- 매출 가능 시점: `장기`
- 담당자 후보 힌트: 인프라사업부 총괄 임원, CIO, 디지털 혁신 실무 총괄 부서장
- 공개 프로필 URL: https://www.linkedin.com/company/synthomer
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 자체 전산망 및 온프레미스 인하우스 AI 모델 도입 방향성에 관한 세부 계획 파악
- source_ids: S038
- source_urls: http://www.newsroad.co.kr/news/articleView.html?idxno=59549

### 5. 디토닉

- 국가: `KR`
- 시장: `B2G`
- 타깃 유형: `온프레미스 기업`
- 분류: `structure_check`
- 확인된 프로젝트/시그널: 폐쇄망 및 군 전술망 타깃 소버린 국방 AI 인프라 솔루션 개발
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `MID`
- RNGD fit_score: `MID`
- outreach priority: `MID`
- fit vs priority 설명: 특정 모델 탑재 여부는 규명되지 않았으나, 통신 단절 환경 및 특수 안보용 폐쇄망 적용 타깃이므로 하드웨어 보안 및 물리 배치 호환성이 요구되는 구조 검토 대상입니다.
- hook_type: `SOVEREIGN`
- 핵심 buying signal: 외부 통신 네트워크가 제한된 지휘소나 군용 차량 등 소버린 국방 AI 구동이 가능한 소프트웨어 솔루션을 활발히 제안하고 있습니다.
- 인프라 signal: 전술망 특화형 소형 하드웨어 장치나 특화 온프레미스 서버 환경 위주로 설계되어 있습니다.
- timing reason: 전술 통신 환경 제품 라인업을 보강하고 실증 사업을 모색 중인 시점이므로 임베디드 장치 연동 논의에 유리합니다.
- 고객 win: 전술망 하부 하드웨어의 엄격한 전력 소모량 한계 및 협소한 공간적 제약을 가속 카드의 우수한 물리적 사양으로 해소할 수 있습니다.
- FuriosaAI win: 방산 및 군 특수 장비 등 엄밀한 신뢰도가 요구되는 새로운 민관 안보 공급 라인 레퍼런스를 개척하게 됩니다.
- 직접 판매 가능성: `HIGH`
- CSP 경유 판매 가능성: `LOW`
- NPUaaS 유도 가능성: `LOW`
- CSP capacity 증설 가능성: `LOW`
- 수치 근거: 없음
- 컨택 명분: 특수 폐쇄망 전술 통신 장치 내에 저전력 가속 보드를 함께 탑재하는 공동 패키징 가능성을 진단하기 위함입니다.
- 실제 컨택 시 사용할 말: 귀사에서 전술 통신 중단 상태를 이겨낼 수 있는 폐쇄망 국방 AI 연구를 진행하신 내역을 접하였습니다. 좁은 공간과 열악한 전력 상황을 견뎌야 하는 군 작전 장비 사양에 맞춘 저전력 소형 가속 카드 파트너십을 의논하고자 연락드렸습니다.
- 매출 가능 시점: `장기`
- 담당자 후보 힌트: 대표이사, 소버린 국방 AI 프로젝트 기술 총괄, 방산 사업 제안 담당자
- 공개 프로필 URL: https://www.linkedin.com/company/wnsprocurement/
- 기존 접점: `확인 필요`
- B2G 근거 유형: `기사/RSS 기반`
- 나라장터 직접 확인: `미수행`
- 조달상 다음 액션: 나라장터/RFP 직접 확인 필요
- 확인 필요: 군 전술망 인프라 납품 시 요구되는 보안성 평가 표준 절차 및 규범 검토 필요
- source_ids: S013
- source_urls: https://www.newsis.com/view/NISX20260522_0003640230

### 6. 오픈네트웍시스템

- 국가: `KR`
- 시장: `B2G`
- 타깃 유형: `CSP 고객 기업`
- 분류: `watchlist`
- 확인된 프로젝트/시그널: 나라장터 대상 AI 에이전트 및 스마트 브리핑 시스템 구축 전개
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `MID`
- 채널/CSP fit_score: `MID`
- RNGD fit_score: `MID`
- outreach priority: `MID`
- fit vs priority 설명: 사용 언어 모델은 미확인 상태이나 Dify 에이전트 연계를 기반으로 한 조달 타깃 소프트웨어 공급 기업으로, 추후 조달 하드웨어 결합 패키지 판매를 위해 모니터링이 필요합니다.
- hook_type: `PARTNER`
- 핵심 buying signal: 나라장터 및 공공 행정 분석을 목표로 한 대화형 AI 시스템 도입 제안을 현장에 본격 선보이기 시작했습니다.
- 인프라 signal: 주로 소프트웨어 및 API 플랫폼 구동에 강하며, 고객 전산 인프라와의 결합이나 클라우드 상의 호스팅 연계가 중심이 될 것입니다.
- timing reason: 공공용 AI 에이전트 기술 시연을 통한 발주 상담이 지속 진행되는 시장 개척 타이밍입니다.
- 고객 win: 에이전트 구동 과정에 수반되는 텍스트 분석 워크로드 비용을 낮추고, 공공 조달 환경에 특화된 국산화 솔루션을 구축할 수 있습니다.
- FuriosaAI win: 에이전트 오케스트레이션 전문 프레임워크 연계 기회를 창출하고, 공공 조달 시장 내의 기술 동맹을 형성할 수 있습니다.
- 직접 판매 가능성: `LOW`
- CSP 경유 판매 가능성: `MID`
- NPUaaS 유도 가능성: `MID`
- CSP capacity 증설 가능성: `LOW`
- 수치 근거: 없음
- 컨택 명분: 에이전트 인공지능 워크로드를 저비용으로 서빙할 수 있도록 소프트웨어-하드웨어 최적화 협력을 설계하기 위함입니다.
- 실제 컨택 시 사용할 말: 귀사에서 소개하신 Dify 프레임워크 기반의 지능형 에이전트 구축 기술을 인상적으로 평가하고 있습니다. 공공 및 기업 부서용 API 서빙 단계에서 추론 최적화를 보조해 드릴 수 있는 전용 가속기 시너지 방안에 대해 사전 협의하고자 연락드렸습니다.
- 매출 가능 시점: `장기`
- 담당자 후보 힌트: 공공사업본부 이사, 솔루션 개발 총괄 부서 책임자
- 공개 프로필 URL: 
- 기존 접점: `확인 필요`
- B2G 근거 유형: `기사/RSS 기반`
- 나라장터 직접 확인: `미수행`
- 조달상 다음 액션: 나라장터/RFP 직접 확인 필요
- 확인 필요: ONS가 활용 중인 클라우드 호스팅 파트너 및 온프레미스 연동 선호 모델 검증
- source_ids: S020, S021, S023
- source_urls: https://www.joongang.co.kr/article/25430014 | https://www.gokorea.kr/news/articleView.html?idxno=866999 | https://www.sentv.co.kr/article/view/sentv202605190084

### 7. 엘리스그룹

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `CSP 운영 기업`
- 분류: `cloud_npuaas_lead`
- 확인된 프로젝트/시그널: 코스닥 상장 추진 및 자체 인프라를 활용한 GPUaaS 서비스 라인업 확장
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 자체 AI 클라우드와 GPU 가상화 자원을 적극 운용 중인 하이퍼스케일러형 스타트업으로, 상장 공모 자금을 통한 인프라 투자와 국산 가속기 채택 가능성이 높아 우선 순위가 매우 높습니다.
- hook_type: `CLOUD`
- 핵심 buying signal: 자체 개발한 AI 클라우드 인프라 솔루션을 토대로 독자적인 GPUaaS 비즈니스를 전개 중이며, 예비심사 청구 등 기업공개 단계에 돌입하였습니다.
- 인프라 signal: 대규모 AI 클라우드 및 컨테이너 가상화 인프라를 직접 컨트롤하는 역량을 보유하고 있습니다.
- timing reason: 예비심사 통과 및 대규모 투자 자본 유치로 인프라 확충에 예산 유연성이 확대되는 최적의 기기 검토 구간입니다.
- 고객 win: 인프라 운영에 동반되는 전력 설계 및 대규모 가속기 확보 비용을 개선하고, 독자적인 국산 NPUaaS 옵션을 추가 확보할 수 있습니다.
- FuriosaAI win: 풀스택 클라우드 전문 기업에 당사 칩을 공급하고, 교육 및 기업 연수용 GPUaaS 수요를 국산 가속기로 선점하는 계기가 마련됩니다.
- 직접 판매 가능성: `HIGH`
- CSP 경유 판매 가능성: `LOW`
- NPUaaS 유도 가능성: `HIGH`
- CSP capacity 증설 가능성: `MID`
- 수치 근거: 없음
- 컨택 명분: 기업공개 추진 및 인프라 추가 확충 로드맵에 맞추어 저전력 추론 가속 카드 도입 파트너십을 추진하고자 합니다.
- 실제 컨택 시 사용할 말: 최근 예심 청구 등 코스닥 상장 본격화 소식을 무척 축하드립니다. 자체 인프라와 컨테이너 가상화 플랫폼을 적극 운영하시는 단계에서 전력 및 공급 가격 한계를 해결할 수 있는 RNGD 가속기를 새로운 클라우드 서비스 옵션으로 검토 제안 드립니다.
- 매출 가능 시점: `단기`
- 담당자 후보 힌트: 김재원 대표이사, 기술 부서 아키텍처 및 클라우드 담당 총괄 리더
- 공개 프로필 URL: https://www.linkedin.com/company/international-data-center-authority-idca
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 엘리스그룹의 가상화 컨테이너 환경 내 국산 가속기 소프트웨어 라이브러리 연동 타당성 분석
- source_ids: S036, S037
- source_urls: http://www.hansbiz.co.kr/news/articleView.html?idxno=839792 | http://www.joseilbo.com/news/news_read.php?uid=568639&class=53&grp=


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

1. **스페이스X, 6월 12일 나스닥 상장 확정…기업가치 최대 3000조 원**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T03:30:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.g-enews.com/view.php?ud=2026052521024974772bd56fbc3c_1
   - summary_snippet: 우주와 인공지능(AI)을 하나로 묶은 일론 머스크의 스페이스X가 오는 6월 12일 미국 나스닥 상장을 앞두고... 스타링크 성장세·우주 데이터센터 구상…3000조 원 몸값 정당한가 스페이스X는 현재 9600기 이상의...

2. **半導体大手クアルコムの決算が映した"メモリー連鎖" データセンターのAI需要が中国スマホの生産を絞らせている - 東洋経済オンライン**
   - source: `rss`
   - published_at_kst: `2026-05-26T03:05:33+09:00`
   - matched_query_or_feed: `Google News JP AIデータセンター`
   - url: https://news.google.com/rss/articles/CBMiUkFVX3lxTE91X09PQVAwZWVWQzJESXpnbGZaVzRJWGNBb2xtX2FyLVpRZ0xpeUNxYWk2SExXbFVSaGQwMVhWU2RwdHd6aHhVUDFPa1ZjQ1V3VEE?oc=5
   - summary_snippet: 半導体大手クアルコムの決算が映した"メモリー連鎖" データセンターのAI需要が中国スマホの生産を絞らせている  東洋経済オンライン

3. **화웨이, 엔비디아·애플과 경쟁심화 속 새 반도체 기술 발표**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T01:55:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.bloter.net/news/articleView.html?idxno=663366
   - summary_snippet: 그는 화웨이가 오는 가을 내놓을 스마트폰 시리즈인 메이트90에 새 기술을 적용할 경우 엔지니어링 측면에서 큰 성과일 전망이지만 이를 인공지능(AI) 데이터센터 규모로 확장하는 것은 "서방의 제재를 우회하기 위한...

4. **AI特化型データセンター開発の合弁会社「AI Data Partners株式会社」、監査役に岸博幸氏が就任予定 - ニコニコニュース**
   - source: `rss`
   - published_at_kst: `2026-05-26T00:48:34+09:00`
   - matched_query_or_feed: `Google News JP AIデータセンター`
   - url: https://news.google.com/rss/articles/CBMie0FVX3lxTE43d0tDV3dDSWV3c09DcHZwdVNnR05ycG9tZWNIZUhMMnhtRk9uUTdqYXAwUV92MEJPOEFlOHlyQlFnamZFLTl4QlZDeVpTaXRVcXBJLVNWQVNJT3lYbTY3OHlZaTVwUGgwWWl1cjF6Uk8ydlJtRUw5c3dqaw?oc=5
   - summary_snippet: AI特化型データセンター開発の合弁会社「AI Data Partners株式会社」、監査役に岸博幸氏が就任予定  ニコニコニュース

5. **[시론] AI로 빼앗기는 '성장 사다리'**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T00:24:00+09:00`
   - matched_query_or_feed: `생성형 AI 도입 기업`
   - url: https://www.hankyung.com/article/2026052573951
   - summary_snippet: 2022년 11월 챗GPT가 등장한 이후 생성형 인공지능(AI)이 폭발적으로 확산됐다. 한국은행이 최근 발표한 ‘AI... 셋째, 기업의 AI 도입을 ‘인력 절감’이 아니라 ‘인간+AI 생산성’ 기준으로 평가해야 한다. 사람을...

6. **유가·물가 숨 돌려도 고환율 지속 우려… 韓경제 뇌관은 ‘반도체’**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T00:22:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.kmib.co.kr/article/view.asp?arcid=1779700492&code=11151100&cp=nv
   - summary_snippet: 양 교수는 “미국 금리 인상으로 자국 내 AI 데이터센터 건설이 둔화할 경우 국내 반도체 수출에도 악영향을 미칠 수밖에 없다”고 우려했다. 한국은행의 기준금리 결정이 신중해야 한다는 제언도 나왔다. 내수 침체와...

7. **[중앙시평] 인공지능이 스스로 진화할 때**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T00:20:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.joongang.co.kr/article/25431189
   - summary_snippet: 우선 여러 기업이 개발하고 있는 AI 모델들을 하나로 통합해 국가 AI 챔피언을 키워볼 수 있고, 중국 내 데이터 센터들을 국영화해 범국가적 데이터 센터를 구축해 볼 수도 있겠다. 하지만 만약 그런 방식을 사용해도...

8. **연휴주말 김진태 후보 동분서주⋯‘반도체·AI데이터센터’ 지역맞춤형...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T00:07:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.kwnews.co.kr/page/view/2026052550159200000
   - summary_snippet: 국민의힘 김진태 강원지사 후보가 공식 선거운동 첫 주말·연휴를 맞아 ‘원주 반도체 비전’과 ‘강릉AI데이터센터’ 등 미래 먹거리 공약을 내세워 표심을 집중 공략했다. 김진태 후보는 지난 22~25일 주말·연휴를...

9. **정청래 대표부터 국회의원, 배우까지⋯민주 강원 지역 전방위 지원유세**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T00:06:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.kwnews.co.kr/page/view/2026052550145500000
   - summary_snippet: 정 대표는 이날 “우상호 후보는 아직 당선도 되기 전에 AI 데이터센터 투자 유치와 같은 굵직한 사업들을 직접 추진하고 있다”며 “보통은 당선 이후 일을 시작한다고 생각하는데 후보 때부터 이렇게 일하는 사람은...

10. **[선택 2026 강원] 골목골목 현장서 찾는 답 "해야 할 일 보일수록 설렌다...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T00:05:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.kado.net/news/articleView.html?idxno=2052090
   - summary_snippet: 우 후보는 "강릉과 동해 사이 AI 데이터센터 설립을 확정했다"며 "최대 70조원이 투자되는 국가 프로젝트다. 동해 예산이 7000억원 정도인데 70조 중 일부만 풀려도 동해는 대박나는 거 아니겠느냐"고 말했다. 현장 반응은...

11. **춘천시장 1번 공약 입맞춰 “산업·경제”⋯육동한 “첨단 융합 클러스...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T00:05:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.kwnews.co.kr/page/view/2026052550122300000
   - summary_snippet: 육동한 후보는 선거관리위원회에 5대 공약을 제출하며 ‘바이오·AI·양자·데이터를 결합한 첨단 산업 융합... 정 후보는 수열에너지 클러스터와 연계한 데이터 센터 유치, 강원권 반도체 공동 연구소와 특화 인력 양성센터...

12. **박상진號 산업은행, AI로 여신심사 [금융권 AI 人포그래픽]**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T00:02:00+09:00`
   - matched_query_or_feed: `생성형 AI 도입 기업`
   - url: http://www.fntimes.com/html/view.php?ud=202605250739132315dd55077bc2_18
   - summary_snippet: 생성형 AI 활용 과정에서 금융권이 우려해온 데이터 보안 문제를 최소화하면서도, 실무에 필요한 분석 기능을 구현했다는 점에서 의미가 있다. 이번 서비스 도입은 산업은행의 핵심 업무인 기업금융과 여신 심사 영역에...

13. **When AI evolves on its own**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T00:01:00+09:00`
   - matched_query_or_feed: `private AI`
   - url: https://koreajoongangdaily.joins.com/news/2026-05-26/opinion/columns/When-AI-evolves-on-its-own/2600329
   - summary_snippet: That background makes the naming of the latest AI model introduced by Anthropic on April 7... government and certain private companies may now possess tools capable of disrupting foreign...

14. **연휴주말 김진태 후보 동분서주⋯‘반도체·AI데이터센터’ 지역맞춤형 공약 집중 - 강원일보**
   - source: `rss`
   - published_at_kst: `2026-05-26T00:01:00+09:00`
   - matched_query_or_feed: `Google News KR AI 데이터센터`
   - url: https://news.google.com/rss/articles/CBMiZEFVX3lxTE41NHVyX2lpQ3YtV3doYmFKSGZSZEJFUkJhU1hZdDBDckNhcGZkRHZBbUlVNGhaaGVVcHotbUQ4YWQ4am1XblRNTmRlcmE4V21HSVNJREs1THZVTGxneTNHRFFVYzM?oc=5
   - summary_snippet: 연휴주말 김진태 후보 동분서주⋯‘반도체·AI데이터센터’ 지역맞춤형 공약 집중  강원일보

15. **로보티즈, 움직이는 AI 시대 핵심 부품주 되나...휴머노이드 시장 주목**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T00:00:00+09:00`
   - matched_query_or_feed: `제조 AI 플랫폼`
   - url: https://www.cbci.co.kr/news/articleView.html?idxno=576986
   - summary_snippet: 일부 투자자들 사이에서는 로봇 부품 플랫폼 기업으로 자리매김할 경우 수조 원대 밸류에이션 가능성이... 미국 빅테크 기업들과 글로벌 제조사들이 차세대 AI 로봇 개발 경쟁에 뛰어들면서 구동계 핵심 부품 기업들에 대한...

16. **장민영號 기업은행, ‘IBK GenAI’ AX 가속…기업금융 혁신 [금융권 AI 人포그래픽] - 한국금융신문**
   - source: `rss`
   - published_at_kst: `2026-05-26T00:00:00+09:00`
   - matched_query_or_feed: `Google News KR 생성형 AI`
   - url: https://news.google.com/rss/articles/CBMifEFVX3lxTE45TXlCcFRKSVJuc2x6eTJ2U0w5bWpmUE9aUXh1YjVOMmdLLW5idlIyWjF2WURwWFVoc1ZmM3lqaVRYb1lKQ2Z6TkN6d1FNa3FLMFBDZHZ3Q1VYM3pUTGpDS001VkY4OVhWblZpYVgwVVBia1ZQazY0bzlEMno?oc=5
   - summary_snippet: 장민영號 기업은행, ‘IBK GenAI’ AX 가속…기업금융 혁신 [금융권 AI 人포그래픽]  한국금융신문

17. **[서학!스타] 포엣테크놀로지, AI 광통신 수혜 기대감 커지나…데이터센터 투자 확대에 변동성 주목 - CBC뉴스**
   - source: `rss`
   - published_at_kst: `2026-05-26T00:00:00+09:00`
   - matched_query_or_feed: `Google News KR AI 데이터센터`
   - url: https://news.google.com/rss/articles/CBMiaEFVX3lxTE1tQ3ktb0lTazBrT1JLaEFsUXl3ZVJvdU9sRzFjMDdkeGdSdVkyR2VPUVlPeDZ5ZmZQY2l3SERzaXoxRWF1RDBSNFRtS3hzdzlZT2JLY2lGSnRVNUxtVGVEaXhhTXB0T0RE?oc=5
   - summary_snippet: [서학!스타] 포엣테크놀로지, AI 광통신 수혜 기대감 커지나…데이터센터 투자 확대에 변동성 주목  CBC뉴스

18. **ReYuu Japan、共同出資による「AI Data Partners株式会社」の設立に関するお知らせ - ニコニコニュース**
   - source: `rss`
   - published_at_kst: `2026-05-25T23:45:18+09:00`
   - matched_query_or_feed: `Google News JP AIデータセンター`
   - url: https://news.google.com/rss/articles/CBMie0FVX3lxTFBseFdFaGRDYldhV3JkajJVSDFwVmxTUDgzbU16R0VqaE5NTVVCTnkwUEZNYjU3QnhaT05tdWhUUml3YU9yLVZ5cXVHS01LcllXdWlYMVZNNC1WVWJEUl9vM3hsYXNDa1h1VlJFRjRKaXZpTmo5OENKbmFFbw?oc=5
   - summary_snippet: ReYuu Japan、共同出資による「AI Data Partners株式会社」の設立に関するお知らせ  ニコニコニュース

19. **이원택 민주당 전북도지사 후보 "군산에 '전북성장공사' 설립"**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T23:29:00+09:00`
   - matched_query_or_feed: `제조 AI 플랫폼`
   - url: https://news.tf.co.kr/read/national/2325965.htm
   - summary_snippet: 피지컬AI, RE100, 재생에너지, 데이터센터, 첨단제조, 농생명 바이오 등 미래산업에 전략적으로 투자하고, 기업·금융·인재·기술을 연결해 전북의 성장 구조 자체를 바꾸는 산업·투자 중심 성장 플랫폼이다. 이 후보는...

20. **AI로 가장 먼저 대체될 직업은?…업종별 AI 대체 기상도 나왔다**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T23:17:00+09:00`
   - matched_query_or_feed: `금융 생성형 AI`
   - url: https://www.munhwa.com/article/11591124?ref=naver
   - summary_snippet: 생성형 인공지능(AI)의 급격한 확산 속에서 건설이나 생산직과 같은 현장 기술 중심의 직업이 가장... 미생물학자나 금융분석가처럼 AI를 통해 업무 효율을 극대화할 수 있는 직업들도 존재하기 때문이다. 예를 들어...


## 다음 단계

1. LLM 후보 품질 확인
2. 노이즈가 많으면 NAVER_QUERIES / RSS_FEEDS 개선
3. 후보가 너무 적으면 MAX_LLM_SOURCES 상향
4. Gemini 3.5 Flash vs 2.5 Flash 품질 비교
5. 나라장터/B2G 수집 추가
6. 담당자/의사결정자 탐색 추가
7. Notion 또는 Google Docs 업로드 추가
