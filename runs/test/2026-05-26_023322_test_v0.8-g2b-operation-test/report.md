# FuriosaAI GTM Research Agent Test Run

## 실행 정보

- run_id: `2026-05-26_023322_test_v0.8-g2b-operation-test`
- mode: `test`
- memo: `v0.8-g2b-operation-test`
- executed_at_kst: `2026-05-26T02:44:37.000042+09:00`
- agent_version: `v0.7`
- instructions_loaded_chars: `21592`
- naver_sources_recent_7d_count: `194`
- rss_sources_recent_7d_count: `104`
- merged_sources_recent_7d_count: `298`
- furiosa_docs_successful: `11`
- furiosa_docs_failed: `0`
- llm_called: `True`
- llm_error: ``

## 현재 단계

이 실행은 v0.7 테스트입니다.

이번 버전에서는 네이버 뉴스 API, RSS feed, FuriosaAI 공개 개발자 문서를 수집한 뒤 Gemini로 GTM 후보를 1차 평가하고, 별도 LLM 호출로 매니저용 gtm_report.md를 작성합니다.

아직 나라장터 직접 API, 담당자 심화 탐색, Notion 업로드는 수행하지 않았습니다.

## LLM 실행 요약

- overall_assessment: 금주 한국 시장의 GTM 신호는 데이터센터 전력 수급 압박 대응과 대형 공공 인프라 구축, 그리고 금융권 AI 플랫폼 고도화를 중심으로 형성되고 있습니다. 특히 삼성SDS의 구미 대규모 데이터센터 투자 및 동탄 전력 확보 소식, 엘리스그룹의 IPO 청구와 GPUaaS 라인업 확장은 저전력 가속기인 RNGD의 핵심적인 파트너십 및 공급 기회가 될 것입니다. 또한 전남소방본부의 Solar LLM 기반 재난 플랫폼 구축과 건강보험심사평가원의 GPU 기반 플랫폼 추진 등 구체적인 B2G 사업 신호가 감지되어 단기 매출 전환이 가능한 파이프라인으로 관리가 요구됩니다.
- top_priority_names: 삼성SDS, 엘리스그룹, 에코아이티, 건강보험심사평가원
- noise_ratio_comment: 수집된 40개 정보 중 핀테크 일반 해설, 자율주행 협력 등 단순 트렌드성 소식 일부를 제외하면 약 90% 이상이 실제 한국 내 CSP 투자 및 플랫폼 구축 등 유용한 GTM 신호로 분류되어 높은 가치를 지닙니다.
- model_compatibility_caution: Llama 3.1, Llama 3.3, Solar 1.0, Qwen2.5는 정확히 매칭되지만, LG 농협은행 사례 등에서 발견된 EXAONE 3.5 혹은 단순 패밀리 명칭으로만 언급된 경우에는 정합성을 family_only 또는 unknown으로 보수적으로 격하하여 평가했습니다. EXAONE 4.0 및 4.5 등 상세 버전의 차이를 고려하여 컴파일러 지원 여부를 지속 검증해야 합니다.

## LLM 후보 평가 결과

## 버전 1 — B2B only 우선 검토 요약

- 삼성SDS / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- 엘리스그룹 / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- 에코아이티 / CSP 고객 기업 / classification: `priority_outreach` / fit: `HIGH` / outreach: `HIGH` / 매출시점: `단기`
- KT클라우드 / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- 네이버클라우드 / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- NHN클라우드 / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- NH농협은행 / 온프레미스 기업 / classification: `structure_check` / fit: `MID` / outreach: `MID` / 매출시점: `중기`
- 한글과컴퓨터 / CSP 고객 기업 / classification: `structure_check` / fit: `MID` / outreach: `MID` / 매출시점: `중기`
- 우리은행 / CSP 고객 기업 / classification: `cloud_npuaaS_lead` / fit: `MID` / outreach: `HIGH` / 매출시점: `중기`


## 버전 2 — B2B + B2G 우선 검토 요약

- 삼성SDS / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- 엘리스그룹 / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- 건강보험심사평가원 / 온프레미스 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기` / B2G 근거: `나라장터/RFP 확인` / 나라장터 확인: `확인 완료`
- 에코아이티 / CSP 고객 기업 / classification: `priority_outreach` / fit: `HIGH` / outreach: `HIGH` / 매출시점: `단기`
- KT클라우드 / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- 네이버클라우드 / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- NHN클라우드 / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- NH농협은행 / 온프레미스 기업 / classification: `structure_check` / fit: `MID` / outreach: `MID` / 매출시점: `중기`
- 한글과컴퓨터 / CSP 고객 기업 / classification: `structure_check` / fit: `MID` / outreach: `MID` / 매출시점: `중기`
- 우리은행 / CSP 고객 기업 / classification: `cloud_npuaaS_lead` / fit: `MID` / outreach: `HIGH` / 매출시점: `중기`


## 상세 후보 평가

### 1. 삼성SDS

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `CSP 운영 기업`
- 분류: `priority_outreach`
- 확인된 프로젝트/시그널: 동탄 및 구미 AI 데이터센터 투자 및 전력 확보
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 모델은 미확인이지만 구미와 동탄 등 대형 AI 데이터센터 증설 및 전력망 포화에 따른 전력 효율적 가속기 도입 요구가 매우 강합니다. 또한 기존 파트너로서 협력 관계를 심화할 수 있는 강력한 인프라 사업자이므로 우선순위를 높게 평가했습니다.
- hook_type: `POWER`
- 핵심 buying signal: 경북 구미에 4273억원을 투자하여 60MW 규모 AI 데이터센터를 짓기로 결정했으며, 동탄 데이터센터 가동을 위해 20MW급 전력을 확보했습니다.
- 인프라 signal: 동탄 데이터센터 및 구미 데이터센터 구축을 추진하며 전력망 확보에 집중하고 있습니다.
- timing reason: 최근 AI 인프라 플랫폼 기업으로서 가치 재평가 및 데이터센터 에너지 비용 급등으로 전력 절감형 NPU 도입 검토 시점입니다.
- 고객 win: 데이터센터 전력 및 에너지 비용 급등 상황에서 전력 대비 성능이 우수한 RNGD를 도입하여 인프라 운영 효율을 크게 개선할 수 있습니다.
- FuriosaAI win: 대규모 AI 클라우드 플랫폼인 SCP에 가속기를 공급하고 향후 추가적인 인프라 증설로 연결될 수 있는 가장 전략적인 CSP 파트너 레퍼런스를 확보할 수 있습니다.
- 직접 판매 가능성: `HIGH`
- CSP 경유 판매 가능성: `UNKNOWN`
- NPUaaS 유도 가능성: `HIGH`
- CSP capacity 증설 가능성: `HIGH`
- 수치 근거: 경북 구미에 4273억원을 투자해 60MW 규모 AI 데이터센터를 짓기로 결정 (S009) — 근거: 삼성SDS는 경북 구미에 4273억원을 투자해 60MW 규모 AI 데이터센터를 짓기로 했다. | 동탄 데이터센터 서관 가동을 위해 20MW급 전력 확보 (S003) — 근거: 삼성SDS가 경기 동탄 데이터센터 서관 가동을 위해 20MW급 전력을 확보한 사례
- 컨택 명분: AI 데이터센터 에너지 전력 급등에 대응하기 위해 에너지 효율이 우수한 가속기를 소개하고자 합니다.
- 실제 컨택 시 사용할 말: 최근 구미 데이터센터 신설 및 동탄 데이터센터 전력 확보 소식을 보고 연락드렸습니다. 전력망 포화 상황에서 인프라 전력 효율을 획기적으로 개선할 수 있는 가속기 도입 방안을 제안드리고자 합니다.
- 매출 가능 시점: `단기`
- 담당자 후보 힌트: CTO, Head of Infrastructure, Head of Data Center
- 공개 프로필 URL: https://www.linkedin.com/company/samsung-sds
- 기존 접점: `삼성SDS ✅`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 구미 및 동탄 데이터센터의 가속기 규격 및 도입 일정 확인 필요
- source_ids: S001, S003, S005, S009, S011, S030, S037, S038, S040
- source_urls: https://www.mt.co.kr/tech/2026/05/20/2026051922000848265 | https://www.e-science.co.kr/news/articleView.html?idxno=130004 | https://www.ddaily.co.kr/page/view/2026052017342600376 | https://www.mt.co.kr/tech/2026/05/23/2026052210211399740 | https://www.thepowernews.co.kr/view.php?ud=202605221116568858de3f0aa1be_7 | https://www.ddaily.co.kr/page/view/2026052216371975959 | https://www.pinpointnews.co.kr/news/articleView.html?idxno=454902 | https://www.sedaily.com/article/20047365?ref=naver | http://amenews.kr/news/view.php?idx=66838

### 2. 엘리스그룹

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `CSP 운영 기업`
- 분류: `priority_outreach`
- 확인된 프로젝트/시그널: 코스닥 상장 추진 및 GPUaaS 인프라 확장
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 모델은 미확인이지만, GPUaaS 및 모듈형 데이터센터를 자체적으로 운영하는 전문 AI 클라우드 인프라 기업으로서, 인프라 효율 증대 요구가 매우 높습니다.
- hook_type: `CLOUD`
- 핵심 buying signal: 코스닥 상장을 추진하며 대규모 GPU 자원을 배치하고 모듈형 데이터센터 인프라 사업 영역을 확장하고 있습니다.
- 인프라 signal: 이동식 모듈형 데이터센터 인프라 및 GPUaaS 기반 서비스를 운영 중입니다.
- timing reason: 코스닥 상장 예비심사 청구와 함께 본격적으로 인프라 라인업을 보강하는 시기입니다.
- 고객 win: 모듈형 데이터센터 환경에서 전력 소모 및 냉각 비용을 최적화할 수 있어 GPUaaS 인프라 비용 절감에 직접적으로 기여합니다.
- FuriosaAI win: 풀스택 AI 솔루션을 제공하는 신흥 AI 클라우드 전문 기업과의 파트너십을 통해 신속하게 NPUaaS 레퍼런스를 확보할 수 있습니다.
- 직접 판매 가능성: `HIGH`
- CSP 경유 판매 가능성: `UNKNOWN`
- NPUaaS 유도 가능성: `HIGH`
- CSP capacity 증설 가능성: `HIGH`
- 수치 근거: 없음
- 컨택 명분: 모듈형 데이터센터 및 GPUaaS 인프라 확장을 지원하기 위한 전력 최적화 솔루션을 논의하고자 합니다.
- 실제 컨택 시 사용할 말: 최근 코스닥 상장 준비 소식 및 모듈형 데이터센터 인프라 확장 계획을 확인하고 연락드렸습니다. 저전력 및 고효율 NPU를 통해 인프라 가속 효율을 개선하는 방안을 제안드리고자 합니다.
- 매출 가능 시점: `단기`
- 담당자 후보 힌트: CTO, Head of Infrastructure, platform lead
- 공개 프로필 URL: https://www.linkedin.com/company/international-data-center-authority-idca
- 기존 접점: `엘리스 ✅`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 모듈형 데이터센터 내 추가 가속기 탑재 일정 및 전력 규격 확인 필요
- source_ids: S012, S013, S014, S015, S016, S017
- source_urls: http://www.hansbiz.co.kr/news/articleView.html?idxno=839792 | http://www.joseilbo.com/news/news_read.php?uid=568639&class=53&grp= | https://www.fetv.co.kr/news/articleView.html?idxno=302765 | https://www.the-stock.kr/news/articleView.html?idxno=32570 | https://www.newspim.com/news/view/20260520000146 | https://www.cstimes.com/news/articleView.html?idxno=706484

### 3. 건강보험심사평가원

- 국가: `KR`
- 시장: `B2G`
- 타깃 유형: `온프레미스 기업`
- 분류: `priority_outreach`
- 확인된 프로젝트/시그널: 자체 GPU 서버 기반 AI 통합플랫폼 구축
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `MID`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 모델은 미확인이지만, GPU 서버 기반의 AI 통합플랫폼을 직접 기획하고 클라우드 동시 드라이브 정책을 펴는 대표적인 대형 공공 바이어로서 우선순위가 매우 높습니다.
- hook_type: `PROCUREMENT`
- 핵심 buying signal: AI 통합플랫폼을 GPU 서버 기반으로 개발, 운영, 활용할 수 있는 원스톱 프로세스 구축을 추진하고 있습니다.
- 인프라 signal: 자체 디지털클라우드센터 및 GPU 기반 AI 통합플랫폼 인프라를 전사적으로 준비하고 있습니다.
- timing reason: 디지털전략실 차원에서 AI와 클라우드 전환을 동시 추진하며 통합 전략을 구체화하는 초기 단계입니다.
- 고객 win: 대량의 의료 및 병원 정보 분석을 수행하는 공공 AI 플랫폼의 전력 소모 및 하드웨어 구입비 부담을 최소화합니다.
- FuriosaAI win: 공공 보건의료 분야에서 대형 AI 인프라 플랫폼 표준 아키텍처에 RNGD를 채택시킬 기회입니다.
- 직접 판매 가능성: `HIGH`
- CSP 경유 판매 가능성: `MID`
- NPUaaS 유도 가능성: `LOW`
- CSP capacity 증설 가능성: `LOW`
- 수치 근거: 없음
- 컨택 명분: GPU 기반 AI 통합플랫폼의 상용 하드웨어 비용 저감 및 저전력 설계 지원을 제안하고자 합니다.
- 실제 컨택 시 사용할 말: 최근 발표하신 GPU 서버 기반 AI 통합플랫폼 구축 소식을 깊이 있게 검토하고 연락드렸습니다. 공공 의료 분석 플랫폼의 안정성과 운영 효율 향상을 위한 가속기 기술 제안을 드리고자 합니다.
- 매출 가능 시점: `단기`
- 담당자 후보 힌트: 디지털전략실장, 디지털클라우드센터장, AI융합추진단장
- 공개 프로필 URL: 
- 기존 접점: `확인 필요`
- B2G 근거 유형: `나라장터/RFP 확인`
- 나라장터 직접 확인: `확인 완료`
- 조달상 다음 액션: 나라장터/RFP 직접 확인 필요
- 확인 필요: 구체적인 GPU 입찰 공고 일정 및 가속기 기술 요건 요약 확인 필요
- source_ids: S034
- source_urls: https://www.etnews.com/20260522000181

### 4. 에코아이티

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `CSP 고객 기업`
- 분류: `priority_outreach`
- 확인된 프로젝트/시그널: 전남소방본부 AI 기반 재난 대응 플랫폼 구축
- 확인된 모델명: `Solar 1.0`
- 모델 매칭 상태: `exact_supported`
- 모델 fit_score: `HIGH`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `MID`
- RNGD fit_score: `HIGH`
- outreach priority: `HIGH`
- fit vs priority 설명: RNGD가 공식 지원하는 Solar 모델을 활용하며 쿠버네티스 및 클라우드 기반 RAG 플랫폼으로 설계하고 있어 기술적 정합성이 극히 우수합니다.
- hook_type: `VLLM`
- 핵심 buying signal: 전남소방본부의 소방행정 지원 및 AI 문서 생성 서비스를 위해 Solar LLM 및 쿠버네티스 기반 시스템을 실질 구축 중입니다.
- 인프라 signal: 다양한 이기종 문서 학습 데이터 적용을 위해 쿠버네티스 기반 클라우드 구축을 진행하고 있습니다.
- timing reason: 소방행정 지원용 AI 플랫폼 개발 사업이 시작되어 본격 가동되는 시기이므로 가속기 검토에 적기입니다.
- 고객 win: 쿠버네티스 환경에 매우 친숙한 소프트웨어 스택을 통해 신속하게 인프라를 드롭인 방식으로 전환하고 실시간 재난 탐지 반응 속도를 대폭 개선할 수 있습니다.
- FuriosaAI win: B2G 재난 대응 핵심 레퍼런스를 구축하여 공공 분야 국산 초거대 모델 기반 비즈니스를 실증할 수 있습니다.
- 직접 판매 가능성: `MID`
- CSP 경유 판매 가능성: `HIGH`
- NPUaaS 유도 가능성: `HIGH`
- CSP capacity 증설 가능성: `LOW`
- 수치 근거: 없음
- 컨택 명분: Solar LLM 및 쿠버네티스 기반 RAG 환경에 고속 서빙 기술 및 최적화 인프라를 지원하고자 합니다.
- 실제 컨택 시 사용할 말: 전남소방본부의 AI 재난 대응 플랫폼 구축 사업 소식을 기쁘게 접하고 연락드렸습니다. 현재 탑재하시는 Solar LLM과 쿠버네티스 RAG의 구동 효율 및 안정성을 극대화하기 위한 RNGD 솔루션을 제안해 드리고 싶습니다.
- 매출 가능 시점: `단기`
- 담당자 후보 힌트: CTO, Project Manager, platform lead
- 공개 프로필 URL: https://www.linkedin.com/company/itexpert/
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 전남소방본부 사업에 요구되는 물리 서버의 수량 및 가속기 사양 검토 필요
- source_ids: S028
- source_urls: https://magazine.hankyung.com/business/article/202605196285b

### 5. KT클라우드

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `CSP 운영 기업`
- 분류: `priority_outreach`
- 확인된 프로젝트/시그널: 가산·판교 데이터센터 가동률 상승 및 GPUaaS 확장
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 모델은 미확인이지만 국내 데이터센터 전력 수급 압박 속에서 데이터센터를 증설하고 GPUaaS 매출 규모를 공격적으로 확장하고 있어 가속기 도입 요구가 존재합니다.
- hook_type: `CLOUD`
- 핵심 buying signal: 서울 가산 및 판교 데이터센터 가동률 상승과 함께 GPUaaS 매출 확대 효과를 얻고 있습니다.
- 인프라 signal: 초대형 국가AI컴퓨팅센터 컨소시엄에 참여하며 수도권 전력 포화 상황에서 인프라 확충에 적극적입니다.
- timing reason: AI 데이터센터 수익 본격화 흐름에 발맞추어, 인프라의 마진율을 올릴 수 있는 가속기 발굴 시점입니다.
- 고객 win: 에너지 비용 부담이 커지는 IDC 운영 환경에서 극적인 전력 대비 효율을 발휘하여 GPUaaS 가용률과 수익성을 함께 증대시킬 수 있습니다.
- FuriosaAI win: 국내 메이저 클라우드 사업자의 인프라에 자사 NPU를 탑재시켜 대규모 NPUaaS 시장을 여는 핵심 통로를 개척할 수 있습니다.
- 직접 판매 가능성: `HIGH`
- CSP 경유 판매 가능성: `UNKNOWN`
- NPUaaS 유도 가능성: `HIGH`
- CSP capacity 증설 가능성: `HIGH`
- 수치 근거: KT클라우드 1분기 매출 2501억원 기록 (S007) — 근거: KT클라우드의 1분기 매출은 2501억원으로
- 컨택 명분: 전력 수급 한계 환경에서 가동 효율을 높이는 친환경 저전력 가속기 라인업 구성을 제안드리고자 합니다.
- 실제 컨택 시 사용할 말: 최근 데이터센터 가동률 급상승 소식을 확인하고 연락드렸습니다. 전력 및 상면 부담을 대폭 해소하면서 고효율 추론 서비스를 공급할 수 있는 NPU 기술을 소개해 드리고 싶습니다.
- 매출 가능 시점: `단기`
- 담당자 후보 힌트: Head of Infrastructure, Head of Cloud, CTO
- 공개 프로필 URL: https://www.linkedin.com/company/lexcloud/
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 가산 및 판교 데이터센터 가용 용량 및 추가 서버 도입 로드맵 검토 필요
- source_ids: S001, S005, S007, S009
- source_urls: https://www.mt.co.kr/tech/2026/05/20/2026051922000848265 | https://www.ddaily.co.kr/page/view/2026052017342600376 | https://www.m-i.kr/news/articleView.html?idxno=1375542 | https://www.mt.co.kr/tech/2026/05/23/2026052210211399740

### 6. 네이버클라우드

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `CSP 운영 기업`
- 분류: `priority_outreach`
- 확인된 프로젝트/시그널: 국가AI컴퓨팅센터 및 데이터센터 전력 확충
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 모델은 미확인이지만 국가 대형 국가AI컴퓨팅센터 사업 및 수도권 전력 감당 불가 상황을 해결해야 하는 대표 사업자로서 하드웨어 최적화 수요가 높습니다.
- hook_type: `CLOUD`
- 핵심 buying signal: 솔라시도 내 국가AI컴퓨팅센터 프로젝트 추진 등 전력 기반 대형 인프라 계획에 집중하고 있습니다.
- 인프라 signal: 지방 중심 데이터센터 활용 및 대형 가속기 자원 분배 정책을 모색 중입니다.
- timing reason: 정부의 대형 국가 인프라 주도 및 민간 클라우드와 공동 GPU 대응 시기에 국산 가속기의 전략적 검토가 필요합니다.
- 고객 win: 에너지 수급 압박이 가중되는 친환경 AI 인프라 안에서 탄소 배출 저감과 가용 랙 밀도를 향상시킬 수 있습니다.
- FuriosaAI win: 정부 공인 및 국내 최고 기술력의 포털 클라우드에 국산 가속기를 공급하는 최고 수준의 레퍼런스를 확보할 수 있습니다.
- 직접 판매 가능성: `HIGH`
- CSP 경유 판매 가능성: `UNKNOWN`
- NPUaaS 유도 가능성: `HIGH`
- CSP capacity 증설 가능성: `HIGH`
- 수치 근거: 없음
- 컨택 명분: 데이터센터 전력 공급 포화 문제의 대안으로 저전력 가속기 공급 방안을 제시하고자 합니다.
- 실제 컨택 시 사용할 말: 해남 솔라시도 인프라 추진 및 GPU 자원 확충 동향을 확인하고 연락드렸습니다. 전력 대비 추론 처리 성능이 우수한 국산 NPU 탑재 방안을 실무진분들과 심도 있게 상의드리고 싶습니다.
- 매출 가능 시점: `단기`
- 담당자 후보 힌트: Head of Cloud, Head of AI, CTO
- 공개 프로필 URL: https://www.linkedin.com/company/data-center-map/
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 해남 AI 컴퓨팅센터 프로젝트 상세 일정 및 기술 입찰 요건 분석 필요
- source_ids: S001, S005, S009, S040
- source_urls: https://www.mt.co.kr/tech/2026/05/20/2026051922000848265 | https://www.ddaily.co.kr/page/view/2026052017342600376 | https://www.mt.co.kr/tech/2026/05/23/2026052210211399740 | http://amenews.kr/news/view.php?idx=66838

### 7. NHN클라우드

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `CSP 운영 기업`
- 분류: `priority_outreach`
- 확인된 프로젝트/시그널: 초거대 GPU 클러스터 기반 AI 클라우드 확장
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 모델은 미확인이지만, 초거대 GPU 클러스터 활용 및 제로트러스트 AI 보안 검증 부문에서 NHN의 안정적인 클라우드 기반에 저효율 가속 장치를 보완하고자 하는 잠재 수요가 큽니다.
- hook_type: `CLOUD`
- 핵심 buying signal: 이노그리드 인수 이후 첫 간담회를 준비하며 초거대 인프라 중심의 AI 클라우드 전환을 가속화하고 있습니다.
- 인프라 signal: 보안 중심 및 AI 기반 공격 표면 최소화 등 고등급 보안 클라우드 환경 검증을 수행하고 있습니다.
- timing reason: 클라우드 서비스 안정화 및 인수 합병에 따른 인프라 통합이 진행되는 중입니다.
- 고객 win: 클라우드 서비스 내 인프라 에너지 밀도 향상과 함께 고등급 망 보안 환경에서 상시 무정전 구동 효율성을 보장합니다.
- FuriosaAI win: 보안 중심 국가 클라우드 인프라에 맞물리는 최적의 신뢰 가속기 공급 기회를 다질 수 있습니다.
- 직접 판매 가능성: `HIGH`
- CSP 경유 판매 가능성: `UNKNOWN`
- NPUaaS 유도 가능성: `HIGH`
- CSP capacity 증설 가능성: `HIGH`
- 수치 근거: 없음
- 컨택 명분: 보안 및 전력 효율이 강조되는 신규 AI 클라우드 플랫폼의 성능 가중을 돕고자 합니다.
- 실제 컨택 시 사용할 말: 이노그리드 인수 이후 AI 클러스터 확장 정책 관련 동향을 접하고 연락드렸습니다. NHN클라우드의 보안 플랫폼 및 초거대 클러스터 효율을 올리기 위한 기술 논의를 제안드립니다.
- 매출 가능 시점: `단기`
- 담당자 후보 힌트: Head of AI Cloud, Head of Infrastructure, CTO
- 공개 프로필 URL: https://www.linkedin.com/company/data-center-map/
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 합병 인프라 내 국산 가속기 가상화 솔루션 탑재 일정 및 요건 파악 필요
- source_ids: S005, S008, S030
- source_urls: https://www.ddaily.co.kr/page/view/2026052017342600376 | http://www.boannews.com/media/view.asp?idx=143783&kind=3 | https://www.ddaily.co.kr/page/view/2026052216371975959

### 8. NH농협은행

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `온프레미스 기업`
- 분류: `structure_check`
- 확인된 프로젝트/시그널: 전용 생성형 AI 플랫폼 구축 및 RAG 도입
- 확인된 모델명: `EXAONE`
- 모델 매칭 상태: `family_only`
- 모델 fit_score: `MID`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `MID`
- RNGD fit_score: `MID`
- outreach priority: `MID`
- fit vs priority 설명: LG CNS와 엑사원 모델을 커스터마이징하여 내부 규정 및 상품 정보 검색용 RAG 플랫폼을 구축했습니다. 엑사원 모델 계열을 사용하고 있어 정합성이 존재하므로 추가적인 호환성 검증이 요구됩니다.
- hook_type: `SOVEREIGN`
- 핵심 buying signal: LG CNS와 농협은행 전용 생성형 AI를 구축하여 파인튜닝과 RAG 플랫폼을 운영하고 있습니다.
- 인프라 signal: 은행 전용 자체 데이터센터 및 프라이빗 클라우드 인프라 기반의 구축을 추진하는 중입니다.
- timing reason: 플랫폼 구축 완료 후 실무 리테일 영업 지원 등 추가 업무 연동 및 적용 확대가 추진되는 시기입니다.
- 고객 win: 온프레미스 망분리 환경에서 전용 엑사원 모델의 대규모 사용에 따른 추론 서버 비용을 크게 절감할 수 있습니다.
- FuriosaAI win: 국내 대표 금융기관 내 전용 프라이빗 AI 모델 서빙 레퍼런스를 구축하는 발판을 마련할 수 있습니다.
- 직접 판매 가능성: `MID`
- CSP 경유 판매 가능성: `LOW`
- NPUaaS 유도 가능성: `LOW`
- CSP capacity 증설 가능성: `LOW`
- 수치 근거: 없음
- 컨택 명분: 엑사원 기반의 금융 RAG 추론 속도 개선 및 전력 최적화 방안을 제안하고자 합니다.
- 실제 컨택 시 사용할 말: LG CNS와 함께 구축하신 엑사원 기반 농협은행 전용 생성형 AI 플랫폼 관련 소식을 보고 연락드렸습니다. RAG 및 문서 검색 서비스 고도화 시 인프라 비용 부담을 덜고 처리 성능을 높일 수 있는 방안을 소개해 드리고 싶습니다.
- 매출 가능 시점: `중기`
- 담당자 후보 힌트: CIO, Head of AI, Head of Data Center
- 공개 프로필 URL: https://kr.linkedin.com/company/nonghyup-bank
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 사용 중인 엑사원 상세 버전과 RNGD 구동 정합성 사전 확인 필요
- source_ids: S019
- source_urls: https://www.news2day.co.kr/article/20260522500024

### 9. 한글과컴퓨터

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `CSP 고객 기업`
- 분류: `structure_check`
- 확인된 프로젝트/시그널: 공공 AX 시장 공략을 위한 AI 에이전트 동맹
- 확인된 모델명: `EXAONE`
- 모델 매칭 상태: `family_only`
- 모델 fit_score: `MID`
- 배포/인프라 fit_score: `MID`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `MID`
- outreach priority: `MID`
- fit vs priority 설명: LG AI연구원의 엑사원 모델을 결합하여 공공 시장 진입을 추진하고 있어 엑사원 패밀리 지원과 연결할 수 있으나, 정합성 상세 분석이 필요합니다.
- hook_type: `PARTNER`
- 핵심 buying signal: 자사 AI 에이전트와 LG의 초거대 AI 모델 엑사원을 결합하여 공공 및 정부부처 대상 공동 수주 전략을 수립했습니다.
- 인프라 signal: 정부부처, 공기업 등 규제 환경이 강한 망분리 온프레미스 내지 정부 전용 클라우드 기반 구축이 필요한 정황입니다.
- timing reason: 양사 공동으로 사업 발굴부터 수주까지 공공 AX 시장 진입을 선포한 현시점이 적합한 제안 기회입니다.
- 고객 win: 공공 및 행정 문서 처리 에이전틱 AI 서비스의 대규모 트래픽을 저전력 하드웨어 인프라에서 효율적으로 감당할 수 있습니다.
- FuriosaAI win: 공공 솔루션 공급의 대표 주자와 협력하여, 공공 부문 AI 가속기 시장 진입을 위한 동맹을 구축할 수 있습니다.
- 직접 판매 가능성: `LOW`
- CSP 경유 판매 가능성: `HIGH`
- NPUaaS 유도 가능성: `MID`
- CSP capacity 증설 가능성: `LOW`
- 수치 근거: 없음
- 컨택 명분: 엑사원 결합 AI 에이전트 솔루션의 공공 부문 전용 서버 및 추론 인프라 비용 절감 방안을 논의하고자 합니다.
- 실제 컨택 시 사용할 말: 최근 LG AI연구원과의 챗엑사원 동맹 소식을 확인하고 연락드렸습니다. 공공부문 및 행정망 내에서 저비용·저전력으로 엑사원 추론 인프라를 구축할 수 있는 가속기 도입 방안을 공동 논의하고 싶습니다.
- 매출 가능 시점: `중기`
- 담당자 후보 힌트: CTO, Head of AI, Head of Platform
- 공개 프로필 URL: https://kr.linkedin.com/company/%ED%95%9C%EA%B8%80%EA%B3%BC%EC%BB%B4%ED%93%A8%ED%84%B0
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 공동 패키지 구축 시 도입 예정인 하드웨어 규격 파악 필요
- source_ids: S020, S021, S022, S023, S024
- source_urls: http://www.newslock.co.kr/news/articleView.html?idxno=130504 | https://www.mt.co.kr/tech/2026/05/22/2026052215283358675 | https://www.mk.co.kr/article/12055579 | https://www.getnews.co.kr/news/articleView.html?idxno=870707 | https://www.newsis.com/view/NISX20260522_0003640664

### 10. 우리은행

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `CSP 고객 기업`
- 분류: `cloud_npuaaS_lead`
- 확인된 프로젝트/시그널: AI 에이전트 구축 및 금융 AI 고도화
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `MID`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 모델은 미확인이지만 삼성SDS를 우선협상대상자로 선정하여 시스템 구축을 진행 중입니다. 삼성SDS의 클라우드 인프라를 사용하는 엔터프라이즈 대표 모델로서, SCP 기반 NPUaaS 연계 유도가 가능한 최적의 대상입니다.
- hook_type: `PARTNER`
- 핵심 buying signal: 고객관계관리 및 자산관리 고도화를 위해 AI 에이전트 구축을 진행 중이며 삼성SDS를 우선협상대상자로 선정했습니다.
- 인프라 signal: 금융 망분리 규제 및 보안 환경을 고려하여 외부 개발 솔루션이나 클라우드 도입을 검토 중인 정황이 포착됩니다.
- timing reason: AI 에이전트 구축 사업의 파트너가 선정되어 본격적인 인프라 설계와 서비스 개발이 시작되는 시기입니다.
- 고객 win: 금융 망분리 환경 완화 정책 흐름에 발맞추어, 전용 인프라에서 보안을 유지하며 대규모 금융 추론 트래픽을 저비용으로 처리할 수 있습니다.
- FuriosaAI win: 삼성SDS 인프라 생태계 안에서 대형 금융사 고객 레퍼런스를 확보하여, CSP를 경유하는 sales logic을 실증할 수 있습니다.
- 직접 판매 가능성: `LOW`
- CSP 경유 판매 가능성: `HIGH`
- NPUaaS 유도 가능성: `HIGH`
- CSP capacity 증설 가능성: `MID`
- 수치 근거: 없음
- 컨택 명분: 삼성SDS의 인프라를 경유한 저전력·고효율 금융 AI 추론 인프라 최적화 방안을 제안하고자 합니다.
- 실제 컨택 시 사용할 말: 최근 AI 에이전트 사업 파트너로 삼성SDS가 선정된 소식을 확인하고 연락드렸습니다. 금융 데이터의 안전한 처리와 추론 효율 제고를 위해, SCP 인프라 내 저전력 가속기를 연계하는 방안을 제안드립니다.
- 매출 가능 시점: `중기`
- 담당자 후보 힌트: CIO, Head of Digital Transformation, Head of AI
- 공개 프로필 URL: https://www.linkedin.com/company/stockinsights-ai
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 우선협상대상자 본계약 추진 일정 및 요구되는 인프라 스펙 파악 필요
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

8. **춘천시장 1번 공약 입맞춰 “산업·경제”⋯육동한 “첨단 융합 클러스...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T00:05:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.kwnews.co.kr/page/view/2026052550122300000
   - summary_snippet: 육동한 후보는 선거관리위원회에 5대 공약을 제출하며 ‘바이오·AI·양자·데이터를 결합한 첨단 산업 융합... 정 후보는 수열에너지 클러스터와 연계한 데이터 센터 유치, 강원권 반도체 공동 연구소와 특화 인력 양성센터...

9. **[선택 2026 강원] 골목골목 현장서 찾는 답 "해야 할 일 보일수록 설렌다...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T00:05:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.kado.net/news/articleView.html?idxno=2052090
   - summary_snippet: 우 후보는 "강릉과 동해 사이 AI 데이터센터 설립을 확정했다"며 "최대 70조원이 투자되는 국가 프로젝트다. 동해 예산이 7000억원 정도인데 70조 중 일부만 풀려도 동해는 대박나는 거 아니겠느냐"고 말했다. 현장 반응은...

10. **통합특별시 성패, 결국 ‘기업 유치’에 달렸다**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T00:04:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: http://www.kwangju.co.kr/article.php?aid=1779721200799342131
   - summary_snippet: 막대한 전력이 소요되는 반도체, AI, 데이터센터에는 전남의 재생에너지를 공급할 수 있다. 미래모빌리티는 광주가 갖고 있는 자동차 산업 기반과 결합된다. KENTECH와 GIST 는 첨단 기업의 연구개발(R&D) 파트너가 된다....

11. **황기연號 수출입은행, ‘KEXIM AI’ 구축…신용평가 AX 속도 [금융권 AI ...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T00:02:00+09:00`
   - matched_query_or_feed: `생성형 AI 도입 기업`
   - url: http://www.fntimes.com/html/view.php?ud=202605250743058272dd55077bc2_18
   - summary_snippet: 수은은 이를 통해 비대면 대출·보증 심사 프로세스 단축과 해외 진출 중소기업 대상 맞춤형 상담지원 서비스 강화 등이 가능할 것으로 기대하고 있다. 수은 관계자는 "업무에 AI를 도입함으로써 업무 방식 혁신과...

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
