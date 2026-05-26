# FuriosaAI GTM Research Agent Test Run

## 실행 정보

- run_id: `2026-05-26_160733_test_manual-test`
- mode: `test`
- memo: `manual-test`
- executed_at_kst: `2026-05-26T16:13:46.253115+09:00`
- agent_version: `v0.7`
- instructions_loaded_chars: `21592`
- naver_sources_recent_7d_count: `210`
- rss_sources_recent_7d_count: `551`
- merged_sources_recent_7d_count: `761`
- furiosa_docs_successful: `11`
- furiosa_docs_failed: `0`
- llm_called: `True`
- llm_error: ``

## 현재 단계

이 실행은 v0.7 테스트입니다.

이번 버전에서는 네이버 뉴스 API, RSS feed, FuriosaAI 공개 개발자 문서를 수집한 뒤 Gemini로 GTM 후보를 1차 평가하고, 별도 LLM 호출로 매니저용 gtm_report.md를 작성합니다.

아직 나라장터 직접 API, 담당자 심화 탐색, Notion 업로드는 수행하지 않았습니다.

## LLM 실행 요약

- overall_assessment: NHN클라우드와 삼성SDS 등 주요 국내 CSP들이 엑사스케일 규모의 AI 데이터센터와 GPUaaS/NPUaaS 인프라를 본격 가동하며 국산 NPU 도입을 위한 기반을 마련함. 금융권 망분리 규제 완화에 따른 AI 보안 솔루션 수요가 단기 급증 예상.
- top_priority_names: NHN클라우드, 삼성SDS, KB금융그룹
- noise_ratio_comment: 공공/금융 망분리 이슈와 NHN클라우드 신규 인프라 발표 위주의 유의미한 소스 위주로 구성되어 noise는 매우 낮음.
- model_compatibility_caution: NHN클라우드 및 삼성SDS 등이 국산 NPU를 이미 혼합 운영 중임을 명시했으나, 구체적인 Furiosa RNGD 채택 여부는 확인되지 않음. 모델 호환성보다는 인프라/데이터센터 용량 중심의 전략적 접근이 필요함.

## LLM 후보 평가 결과

## 버전 1 — B2B only 우선 검토 요약

- 삼성SDS / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `중기`
- KB금융그룹 / 온프레미스 기업 / classification: `priority_outreach` / fit: `LOW` / outreach: `HIGH` / 매출시점: `단기`
- NHN클라우드 / CSP 운영 기업 / classification: `cloud_npuaaS_lead` / fit: `MID` / outreach: `HIGH` / 매출시점: `중기`


## 버전 2 — B2B + B2G 우선 검토 요약

- 삼성SDS / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `중기`
- KB금융그룹 / 온프레미스 기업 / classification: `priority_outreach` / fit: `LOW` / outreach: `HIGH` / 매출시점: `단기`
- NHN클라우드 / CSP 운영 기업 / classification: `cloud_npuaaS_lead` / fit: `MID` / outreach: `HIGH` / 매출시점: `중기`


## 상세 후보 평가

### 1. 삼성SDS

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `CSP 운영 기업`
- 분류: `priority_outreach`
- 확인된 프로젝트/시그널: 구미 데이터센터 60MW급 AI 전력 확보 및 SCP 고도화
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: CSP 운영 및 대규모 데이터센터 확장 기조가 명확하며 SCP/NPUaaS 경로로의 파급력이 매우 큼.
- hook_type: `POWER`
- 핵심 buying signal: 구미 데이터센터 60MW급 AI 인프라 증설
- 인프라 signal: 데이터센터 가동을 위한 대규모 전력 확보 단계
- timing reason: 전력 효율이 핵심인 신규 데이터센터 구축 단계에서 고효율 NPU 도입 명분 강화
- 고객 win: 전력 효율이 우수한 국산 RNGD 도입을 통해 데이터센터 운영 안정성 및 비용 절감 가능.
- FuriosaAI win: 삼성SDS CSP/SCP 생태계 내 주요 NPU 벤더로 진입하여 대규모 공공/금융 고객 확보 기회.
- 직접 판매 가능성: `MID`
- CSP 경유 판매 가능성: `HIGH`
- NPUaaS 유도 가능성: `HIGH`
- CSP capacity 증설 가능성: `HIGH`
- 수치 근거: 60MW급 AI 데이터센터 증설 (S037) — 근거: 삼성SDS는 경북 구미에 4273억원을 투자해 60MW 규모 AI 데이터센터를 짓기로 했다.
- 컨택 명분: 구미 데이터센터 신규 구축에 따른 추론 인프라 다변화 논의
- 실제 컨택 시 사용할 말: 삼성SDS의 구미 데이터센터 구축을 통한 AI 인프라 확장을 확인했습니다. 전력 제약이 심화되는 데이터센터 환경에서 RNGD의 전력 효율을 기반으로 한 NPUaaS 운영 최적화 방안을 검토 요청드립니다.
- 매출 가능 시점: `중기`
- 담당자 후보 힌트: Head of Data Center, Head of Cloud Infrastructure
- 공개 프로필 URL: 
- 기존 접점: `삼성SDS ✅`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 구미 데이터센터 내 AI 가속기 선정 일정
- source_ids: S026, S031, S036, S037
- source_urls: https://www.e-science.co.kr/news/articleView.html?idxno=130004 | https://www.ddaily.co.kr/page/view/2026052017342600376 | https://www.ddaily.co.kr/page/view/2026052509101133595 | https://www.mt.co.kr/tech/2026/05/23/2026052210211399740

### 2. KB금융그룹

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `온프레미스 기업`
- 분류: `priority_outreach`
- 확인된 프로젝트/시그널: 망분리 규제 예외에 따른 AI 보안 에이전트 도입 및 사이버보안 체계 고도화
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `none`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `MID`
- RNGD fit_score: `LOW`
- outreach priority: `HIGH`
- fit vs priority 설명: 금융권 망분리 규제 완화로 인해 온프레미스 AI 수요가 즉각적으로 발생할 수 있는 가장 강력한 B2B 타겟임.
- hook_type: `SOVEREIGN`
- 핵심 buying signal: 금융위 망분리 규제 1년 한시적 면제에 따른 보안용 AI 솔루션 도입 필요
- 인프라 signal: 금융권 폐쇄망 내 AI 에이전트 구축 수요
- timing reason: 규제 완화 발표 직후 보안 에이전트 도입 추진 시점
- 고객 win: 외부망 접속 없이 폐쇄망 내에서 동작하는 RNGD 기반의 온프레미스 보안 에이전트로 데이터 유출 우려 원천 차단.
- FuriosaAI win: 가장 규제가 까다로운 금융권 폐쇄망 내 레퍼런스 확보를 통해 여타 금융사 및 공공기관으로 확산 가능.
- 직접 판매 가능성: `HIGH`
- CSP 경유 판매 가능성: `MID`
- NPUaaS 유도 가능성: `LOW`
- CSP capacity 증설 가능성: `LOW`
- 수치 근거: 없음
- 컨택 명분: 금융권 망분리 예외 적용에 따른 프라이빗 보안 에이전트 인프라 도입 논의
- 실제 컨택 시 사용할 말: 금융권 망분리 규제 완화에 발맞춘 보안 에이전트 도입 소식을 접했습니다. 데이터 주권이 중요한 환경에서 RNGD의 폐쇄망/온프레미스 특화 성능을 활용해 안전한 AI 인프라를 구축하는 방안을 함께 확인하고 싶습니다.
- 매출 가능 시점: `단기`
- 담당자 후보 힌트: CISO, Head of Digital Transformation, Head of AI Lab
- 공개 프로필 URL: 
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 보안 에이전트 구체 구축 인프라 사양
- source_ids: S007, S010, S012, S013
- source_urls: https://www.todayeconomic.com/news/article.html?no=30719 | http://www.thevaluenews.co.kr/news/view.php?idx=198982 | https://www.ekn.kr/web/view.php?key=20260526029567819 | https://www.factin.co.kr/news/articleView.html?idxno=6365

### 3. NHN클라우드

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `CSP 운영 기업`
- 분류: `cloud_npuaaS_lead`
- 확인된 프로젝트/시그널: AI 풀스택 브랜드 '팩토리X' 공개 및 27.4EF 규모 엑사스케일 AI 인프라 구축
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 모델 적합성은 미확인이지만, NHN이 팩토리X를 통해 대규모 GPU/NPU 혼합 운영 환경을 구축 중이며 인프라 확충이 필수적인 CSP 운영사이므로 우선순위가 높음.
- hook_type: `CLOUD`
- 핵심 buying signal: 27.4EF 규모의 엑사스케일 AI 인프라를 위한 가속기 다변화 필요성
- 인프라 signal: 엔비디아 B200 7,656장 기반 팩토리X 서울 데이터센터 운영
- timing reason: 팩토리X 브랜드 런칭 시점에 맞춰 국산 NPUaaS 연계 전략 논의 가능
- 고객 win: 외산 GPU 의존도를 낮추고 국산 NPU 기반의 효율적 추론 인프라를 구축하여 운영 효율성 제고 가능.
- FuriosaAI win: 국내 최대 규모 GPU 클러스터 사업자에 Furiosa RNGD 솔루션을 PoC/도입할 수 있는 전략적 요충지 확보.
- 직접 판매 가능성: `MID`
- CSP 경유 판매 가능성: `HIGH`
- NPUaaS 유도 가능성: `HIGH`
- CSP capacity 증설 가능성: `HIGH`
- 수치 근거: B200 GPU 7,656장 규모 데이터센터 (S005) — 근거: B200 7656장으로 구성한 27.4EF(엑사플롭스) 규모의 국내 최초 엑사스케일 AI
- 컨택 명분: 국내 엑사스케일 AI 인프라 확장에 따른 추론용 NPUaaS 협력 논의
- 실제 컨택 시 사용할 말: NHN클라우드의 팩토리X 런칭을 축하드립니다. 대규모 엑사스케일 인프라에서 추론 비용 효율을 극대화하기 위한 Furiosa RNGD의 Kubernetes 기반 Cloud Native Toolkit 활용 방안을 논의하고 싶습니다.
- 매출 가능 시점: `중기`
- 담당자 후보 힌트: Head of AI Infrastructure, Head of Cloud, NPUaaS Product Lead
- 공개 프로필 URL: 
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 기존 국산 NPU 운영 구체 사양 확인
- source_ids: S005, S027, S039, S040
- source_urls: https://www.lcnews.co.kr/news/articleView.html?idxno=202630 | https://www.metroseoul.co.kr/article/20260526500320 | https://www.getnews.co.kr/news/articleView.html?idxno=870933 | http://www.inews24.com/view/1971407


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
- Llama-3.1-8B-Instruct-FP8 / precompiled_huggingface_api / HuggingFace API furiosa-ai
- EXAONE-3.5-7.8B-Instruct / precompiled_huggingface_api / HuggingFace API furiosa-ai
- Llama-3.1-8B-Instruct / precompiled_huggingface_api / HuggingFace API furiosa-ai
- EXAONE-3.5-32B-Instruct / precompiled_huggingface_api / HuggingFace API furiosa-ai
- Llama-3.3-70B-Instruct / precompiled_huggingface_api / HuggingFace API furiosa-ai
- DeepSeek-R1-Distill-Llama-70B / precompiled_huggingface_api / HuggingFace API furiosa-ai
- Llama-3.3-70B-Instruct-INT8 / precompiled_huggingface_api / HuggingFace API furiosa-ai
- DeepSeek-R1-Distill-Llama-8B / precompiled_huggingface_api / HuggingFace API furiosa-ai
- Qwen2.5-Coder-32B-Instruct / precompiled_huggingface_api / HuggingFace API furiosa-ai
- Qwen2.5-Coder-14B-Instruct / precompiled_huggingface_api / HuggingFace API furiosa-ai
- Qwen2.5-32B-Instruct / precompiled_huggingface_api / HuggingFace API furiosa-ai
- Qwen2.5-7B-Instruct / precompiled_huggingface_api / HuggingFace API furiosa-ai
- DeepSeek-R1-Distill-Qwen-7B / precompiled_huggingface_api / HuggingFace API furiosa-ai
- DeepSeek-R1-Distill-Qwen-14B / precompiled_huggingface_api / HuggingFace API furiosa-ai
- Qwen2.5-14B-Instruct / precompiled_huggingface_api / HuggingFace API furiosa-ai
- Qwen2.5-Coder-7B-Instruct / precompiled_huggingface_api / HuggingFace API furiosa-ai
- DeepSeek-R1-Distill-Qwen-32B / precompiled_huggingface_api / HuggingFace API furiosa-ai
- QwQ-32B / precompiled_huggingface_api / HuggingFace API furiosa-ai
- Qwen3-Embedding-8B / precompiled_huggingface_api / HuggingFace API furiosa-ai
- Qwen2.5-0.5B-Instruct / precompiled_huggingface_api / HuggingFace API furiosa-ai
- Qwen3-Reranker-8B / precompiled_huggingface_api / HuggingFace API furiosa-ai
- Qwen3-32B-FP8 / precompiled_huggingface_api / HuggingFace API furiosa-ai
- EXAONE-4.0-32B-FP8 / precompiled_huggingface_api / HuggingFace API furiosa-ai

### Keyword hits
- serving_stack: Release 2026.2: OpenAI, Release 2026.2: API, RNGD Overview: Kubernetes, Software Stack: vLLM, Software Stack: OpenAI, Software Stack: OpenAI-Compatible, Software Stack: Kubernetes, Software Stack: container, Software Stack: API, Software Stack: server, Roadmap: Kubernetes, Roadmap: container, Roadmap: API, Furiosa LLM Intro: vLLM, Furiosa LLM Intro: OpenAI, Furiosa LLM Intro: OpenAI-Compatible, Furiosa LLM Intro: Kubernetes, Furiosa LLM Intro: API, Furiosa LLM Intro: server, Cloud Native Toolkit: Kubernetes
- hardware_ops: Release 2026.2: RNGD, RNGD Overview: RNGD, RNGD Overview: HBM, RNGD Overview: power, RNGD Overview: SR-IOV, RNGD Overview: virtualization, RNGD Overview: PCIe, RNGD Overview: thermal, Software Stack: power, Roadmap: RNGD, Hugging Face FuriosaAI Org: RNGD

## 통합 수집 요약

1. **『ネコぱら セカイコネクト』が「グッドスマイルフェス2026 グッスマ ゲーム企画展」に出展決定！**
   - source: `rss`
   - published_at_kst: `2026-05-26T16:10:00+09:00`
   - matched_query_or_feed: `ASCII.jp Tech`
   - url: https://ascii.jp/elem/000/004/405/4405122/?rss
   - summary_snippet: グッドスマイルカンパニーは、iOS／Android／PC（Steam）向けゲーム『ネコぱら セカイコネクト』について、「グッドスマイルフェス2026 グッスマゲーム企画展」に出展すると2026年5月26日に発表。

2. **정부, 글래스윙 대안 찾기 ‘사활’…보안·과기 분야 AI 접근권 확보 특...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T16:06:00+09:00`
   - matched_query_or_feed: `생성형 AI 도입 기업`
   - url: https://www.ddaily.co.kr/page/view/2026052615450616185
   - summary_snippet: 26일 업계에 따르면 과학기술정보통신부 관계자들은 최근 오픈AI·구글 등 글로벌 기업 관계자들과 만나... ◆‘AI 접근권’이 곧 안보…글래스윙, TAC 참여 타진 생성형 AI가 확산된 이후 ‘AI 경쟁력이 곧 국가 안보’라는...

3. **인피니틱스, 대만 컴퓨텍스서 AI 인프라·클라우드 전략 공개**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T16:06:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://it.chosun.com/news/articleView.html?idxno=2023092162771
   - summary_snippet: AI 게이트웨이, BOSS 과금 시스템, AI 스택 리소스 관리 기능을 통합 제공하며, 기업과 통신사, 데이터센터가 GaaS·MaaS·TaaS 등 다양한 AI 서비스 모델을 구축할 수 있도록 지원한다. 인피니틱스는 AI...

4. **[병원계 소식] 5월 26일**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T16:06:00+09:00`
   - matched_query_or_feed: `병원 AI 플랫폼`
   - url: http://www.doctorstimes.com/news/articleView.html?idxno=238213
   - summary_snippet: 한편, 이화 AI 특화 공동훈련센터는 향후 협력 기업 확대와 의료 AI 데이터 플랫폼 고도화를 추진하고, 병원 기반 의료 AI 교육·연구 허브로서 역할을 강화해 나갈 예정이다. ■SCL그룹·강남세브란스·몽골국립의대병원...

5. **셀트리온, 신약 개발부터 제조·사무까지 AI 도입… 업무 효율화 속도**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T16:06:00+09:00`
   - matched_query_or_feed: `제조 AI 플랫폼`
   - url: http://www.newslock.co.kr/news/articleView.html?idxno=130552
   - summary_snippet: 셀트리온이 주요 업무 영역에 AI를 도입하며 글로벌 경쟁력 강화에 나선다. 셀트리온은 신약 개발, 제조... 임직원이 단순한 AI 플랫폼을 이용하는 데 그치지 않고 각 부서에 필요한 자동화 툴을 직접 구현하는 동시에...

6. **アークのキャシー・ウッド：「イーロンはデータセンターを宇宙へ移行中 ― 驚異的な垂直統合」 - Moomoo**
   - source: `rss`
   - published_at_kst: `2026-05-26T16:05:59+09:00`
   - matched_query_or_feed: `Google News JP AIデータセンター`
   - url: https://news.google.com/rss/articles/CBMiqwFBVV95cUxOanYyN2NnQlBROVY4bThIQ1Zqa3doa1hDSUhlMmZRbFUtRURHNHNKNEx4ZDFhVnk1VU5BanRyMFNPbU1JM1RRZzRuVVBxXzNLV0FscHhlRG5jVVVzOUlwZTBYblk5dGtKZ2tYZlJRY2NkR2x0RFg1Ujc1MDBpMkJpazRPUlQxaTgwT0NsN0lPUDlIcXNpLUh2NHdoZUJ0V0wwUlpaQmJJTXhBRjA?oc=5
   - summary_snippet: アークのキャシー・ウッド：「イーロンはデータセンターを宇宙へ移行中 ― 驚異的な垂直統合」  Moomoo

7. **지역 국립대에 들어온 글로벌 기업들…전북대선 테슬라 핸들 만들고, 전...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T16:05:00+09:00`
   - matched_query_or_feed: `제조 AI 플랫폼`
   - url: https://www.joongang.co.kr/article/25431369
   - summary_snippet: 대상 제조DX 교육에 활용할 계획이다. 조성준 전남대 기획처장(화학공학부 교수)은 “학생들이 기업 현장에서... 만들기' 정책이 성공하려면 지역거점국립대가 글로벌 기업이 오고 싶어하는 플랫폼이 돼야 한다”고 말했다.

8. **민간LNG산업협회, Kpler AI 공개…업무 방식 대변혁 신호**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T16:04:00+09:00`
   - matched_query_or_feed: `생성형 AI 도입 기업`
   - url: https://www.pinpointnews.co.kr/news/articleView.html?idxno=455396
   - summary_snippet: 협회는 이번 프로그램을 통해 회원사들이 생성형 AI의 실질적 활용 가능성을 체감하고, 각 기업의 업무 환경에 맞는 AI 도입 전략을 검토하는 계기가 될 것으로 기대하고 있다. 아울러 급변하는 에너지 시장 환경...

9. **고유가에 급등한 배터리 원료…캐즘 터널 끝이 보인다**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T16:04:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.hankyung.com/article/2026052684251
   - summary_snippet: AI 데이터센터와 태양광·풍력발전소 바로 옆에 설치되는 ESS 주문이 늘었고, 동시에 니켈 수요도 반등했다는 분석이 나온다. 공급 요인도 있다. 세계 최대 배터리 업체 중국 CATL의 장시성 리튬 광산이 지난해 8월부터...

10. **가온전선, AI 데이터센터 수요 확대에…북미 공략 강화**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T16:04:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://daily.hankooki.com/news/articleView.html?idxno=1370697
   - summary_snippet: 실적 상승 배경에는 미국 AI 데이터센터 시장 확대가 자리잡고 있다. AI 인프라 투자 확대로 전력망 수요가 급증하면서 미국 수출 물량이 확대됐다. 이 같은 수요 증가에 힘입어 가온전선은 AI 데이터센터와 태양광...

11. **가온전선, AI 데이터센터 수요 확대에…북미 공략 강화 - 네이트**
   - source: `rss`
   - published_at_kst: `2026-05-26T16:04:00+09:00`
   - matched_query_or_feed: `Google News KR AI 데이터센터`
   - url: https://news.google.com/rss/articles/CBMiU0FVX3lxTE5uSFRSLURXeHpPX19Tc1VaUU5RNnZaOXM2cG1hXzJpdnlSNHZfdGdNeW1laWwyZWJDNUxydXhpc1kwOER2TEJWUk5PdGQ4YWZRVkZR?oc=5
   - summary_snippet: 가온전선, AI 데이터센터 수요 확대에…북미 공략 강화  네이트

12. **챗GPT, 조회 기준 웹사이트 세계 6위…사용시간 기준 세계 3위**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T16:03:00+09:00`
   - matched_query_or_feed: `금융 생성형 AI`
   - url: https://biz.sbs.co.kr/article_hub/20000312571?division=NAVER
   - summary_snippet: 글로벌 웹사이트 방문 수가 소폭 감소한 가운데 생성형 AI 서비스 트래픽은 큰 폭으로 증가했다는 분석... 센서타워는 이러한 흐름에 대해 "AI 어시스턴트가 단순 검색 도구를 넘어 소비 의사결정과 금융 판단, 규제 이해...

13. **민간LNG산업협회, Kpler AI 공개…업무 방식 대변혁 신호 - 핀포인트뉴스**
   - source: `rss`
   - published_at_kst: `2026-05-26T16:02:50+09:00`
   - matched_query_or_feed: `Google News KR 생성형 AI`
   - url: https://news.google.com/rss/articles/CBMic0FVX3lxTFBvaDdiYjNBNkgyblNhNUxzR0NTejB2dThiV0NPSnY3eFJBQ2VwbzB2dTJRN2xEOWRJTkV6QnQtZ3pMck00ZUxBZVRMeGVpZ09ONkFsN3BGZExXY01yT3E5SWp0STFRWU5SWmNpTDFOd0F4TWvSAXdBVV95cUxQS2hlRUEzaEx1dDdSUDFVLWphM1N5OXVmNWdmT3U4MDlUNWV5aGhzVFVOMkNpQlZXTkoxR05DY3k0c1pQRzItMW9MRmZ2Q1c1STlkdE9nMDRPajNNUS14OG1seDlCa3dpT2g4bkRxVERWRXJsREVDYw?oc=5
   - summary_snippet: 민간LNG산업협회, Kpler AI 공개…업무 방식 대변혁 신호  핀포인트뉴스

14. **이파피루스 '파이뮤PDF 프로', AI 데이터 전처리 시장 공략 나선다**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T16:02:00+09:00`
   - matched_query_or_feed: `생성형 AI 도입 기업`
   - url: http://www.itdaily.kr/news/articleView.html?idxno=239492
   - summary_snippet: 없이 AI 데이터로 전환할 것인가가 가장 큰 숙제였다"고 말했다. 이어 그는 "새롭게 도입되는 HWPX 뿐만 아니라, 기관과 기업 내에 쌓여 있는 기존 HWP 포맷 문서까지 완벽하게 파싱하고 구조화할 수 있어야 진정한...

15. **[지선 D-7] 전북지사 선거 ‘서진 대결’ 격화…이원택·김관영, 군산·...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T16:02:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.jjan.kr/article/20260526500217
   - summary_snippet: 이 후보는 피지컬AI와 RE100, 재생에너지, 데이터센터, 첨단제조 등 미래산업 유치를 통해 군산을 대한민국 미래산업 거점으로 육성하겠다는 전략을 강조했다. 특히 군산은 김 후보의 고향이자 과거 국회의원 재선을 한...

16. **세미파이브, AI 반도체 계약·최대 실적 겹호재에 18%↑ [특징주]**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T16:02:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.dailian.co.kr/news/view/1648747/?sc=Naver
   - summary_snippet: 양산 사업도 데이터센터 AI와 비전 AI 수요 증가에 힘입어 확대되는 모습이다. 올해 1분기 양산 신규 수주액은 지난해 연간 양산 수주액의 74% 수준에 달했다. 업계에서는 세미파이브가 AI 반도체 설계부터 양산까지...

17. **NHN클라우드, AI 풀스택 브랜드 '팩토리X' 공개…"AI 매출 50% 목표"**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T16:02:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.lcnews.co.kr/news/articleView.html?idxno=202630
   - summary_snippet: NHN클라우드는 광구 국가 AI 데이터센터에서 H100 GPU와 국산 NPU를 통합 운영하고 있다. '팩토리X' 서울에서는 정부 주도 GPU 사업을 통해 B200 7656장으로 구성한 27.4EF(엑사플롭스) 규모의 국내 최초 엑사스케일 AI...

18. **[人사이트] 밴 컨 포티넷 지사장 “韓 OT 보안, 기술검증 넘어 전사 구축...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T16:01:00+09:00`
   - matched_query_or_feed: `생성형 AI 도입 기업`
   - url: https://www.etnews.com/20260526000166
   - summary_snippet: 기업이 전 세계 3000개 이상 지점의 네트워크와 보안을 중앙에서 관리하기 위해 'SD-브랜치(Branch)'를 도입하... 컨 지사장 대행은 “포티넷은 20년 이상 축적한 OT 보안 역량에 생성형 AI와 에이전틱 AI를 결합해 산업 현장의...

19. **화웨이, '무어의 법칙' 우회 카드 꺼냈다···EUV 없이 1.4나노 도전**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T16:01:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: http://www.enewstoday.co.kr/news/articleView.html?idxno=2432972
   - summary_snippet: 엔비디아는 미국의 대중국 수출 통제로 첨단 AI 칩 판매에 제약을 받고 있다. 젠슨 황 엔비디아... 로직폴딩이 스마트폰용 모바일 칩에서 성과를 내더라도, 이를 인공지능 데이터센터용 고성능 칩으로 확장하려면 전력...

20. **AI 투자 끝물 아니다…모건스탠리 “반도체 시장 2천조까지 커진다”**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T16:01:00+09:00`
   - matched_query_or_feed: `GPU 클라우드`
   - url: http://www.joseilbo.com/news/news_read.php?uid=568938&class=17&grp=
   - summary_snippet: 모건스탠리는 글로벌 클라우드 서비스 기업(CSP)들의 공격적인 AI 인프라 투자 확대에 주목했다.... 모건스탠리는 AI 서비스가 단순 추론(Inference) 중심에서 실제 실행 단계로 발전하면서 GPU뿐 아니라 작업...


## 다음 단계

1. LLM 후보 품질 확인
2. 노이즈가 많으면 NAVER_QUERIES / RSS_FEEDS 개선
3. 후보가 너무 적으면 MAX_LLM_SOURCES 상향
4. Gemini 3.5 Flash vs 2.5 Flash 품질 비교
5. 나라장터/B2G 수집 추가
6. 담당자/의사결정자 탐색 추가
7. Notion 또는 Google Docs 업로드 추가
