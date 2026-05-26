# FuriosaAI GTM Research Agent Test Run

## 실행 정보

- run_id: `2026-05-26_174435_test_manual-test`
- mode: `test`
- memo: `manual-test`
- executed_at_kst: `2026-05-26T17:50:36.938380+09:00`
- agent_version: `v0.7`
- instructions_loaded_chars: `21592`
- naver_sources_recent_7d_count: `213`
- rss_sources_recent_7d_count: `562`
- merged_sources_recent_7d_count: `775`
- furiosa_docs_successful: `11`
- furiosa_docs_failed: `0`
- llm_called: `True`
- llm_error: ``

## 현재 단계

이 실행은 v0.7 테스트입니다.

이번 버전에서는 네이버 뉴스 API, RSS feed, FuriosaAI 공개 개발자 문서를 수집한 뒤 Gemini로 GTM 후보를 1차 평가하고, 별도 LLM 호출로 매니저용 gtm_report.md를 작성합니다.

아직 나라장터 직접 API, 담당자 심화 탐색, Notion 업로드는 수행하지 않았습니다.

## LLM 실행 요약

- overall_assessment: NHN클라우드의 'FactoryX' 출시와 국내 CSP들의 AI 데이터센터 경쟁이 본격화됨에 따라 NPUaaS 및 CSP capacity expansion 타깃이 구체화됨. 공공/금융 망분리 완화와 연계된 폐쇄망 온프레미스 기회 또한 중요한 GTM 포인트.
- top_priority_names: NHN클라우드, KB금융, 삼성SDS
- noise_ratio_comment: 수집된 40건 중 대부분이 데이터센터 인프라 및 금융 보안 관련 전략 보도로 GTM 관련성이 매우 높음.
- model_compatibility_caution: NHN클라우드 등이 국산 NPU를 이미 도입 중이나, FuriosaAI 모델 호환은 버전별 확인이 필수.

## LLM 후보 평가 결과

## 버전 1 — B2B only 우선 검토 요약

- KB금융 / 온프레미스 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- NHN클라우드 / CSP 운영 기업 / classification: `cloud_npuaaS_lead` / fit: `MID` / outreach: `HIGH` / 매출시점: `중기`


## 버전 2 — B2B + B2G 우선 검토 요약

- KB금융 / 온프레미스 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- NHN클라우드 / CSP 운영 기업 / classification: `cloud_npuaaS_lead` / fit: `MID` / outreach: `HIGH` / 매출시점: `중기`


## 상세 후보 평가

### 1. KB금융

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `온프레미스 기업`
- 분류: `priority_outreach`
- 확인된 프로젝트/시그널: 제로트러스트 및 망분리 완화에 따른 AI 보안 고도화
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `MID`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 금융권 망분리 완화로 인해 폐쇄망 환경 내 고성능 추론 수요가 급증함. 모델명은 확인되지 않았으나 규제 대응형 폐쇄망 구축 신호가 매우 강함.
- hook_type: `SOVEREIGN`
- 핵심 buying signal: 망분리 완화 정책에 따른 AI 에이전트 및 폐쇄망 내부 플랫폼 구축
- 인프라 signal: 제로트러스트 기반의 사내 구축형 보안 시스템 및 망분리 환경 유지
- timing reason: 금융위 망분리 완화 정책 시행 및 그룹 차원의 AI 보안 체계 고도화 시점
- 고객 win: 보안 규제를 준수하면서도 최신 AI 에이전트를 폐쇄망 내부에서 운영하여 데이터 보안성 확보
- FuriosaAI win: 금융권 레퍼런스 확보 및 망분리 환경에서 요구되는 온프레미스 AI 인프라 최적화 기회
- 직접 판매 가능성: `HIGH`
- CSP 경유 판매 가능성: `MID`
- NPUaaS 유도 가능성: `LOW`
- CSP capacity 증설 가능성: `LOW`
- 수치 근거: 없음
- 컨택 명분: 금융권 제로트러스트 보안 체계에 적합한 온프레미스 인프라 제공 논의
- 실제 컨택 시 사용할 말: 금융권 망분리 완화와 AI 에이전트 도입 전략에 대해 깊은 관심을 가지고 있습니다. 당사의 온프레미스 최적화 인프라가 KB금융의 보안 신뢰성을 강화하며 AI 성능을 높이는 데 기여할 수 있는지 검토하고 싶습니다.
- 매출 가능 시점: `단기`
- 담당자 후보 힌트: CIO / CISO / Head of AI, KB금융 디지털/AI 전략 부문
- 공개 프로필 URL: 
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 금융 데이터센터 내 인프라 증설 계획 | 폐쇄망용 LLM 도입 로드맵
- source_ids: S001, S005, S012, S015, S016
- source_urls: http://www.dailypop.kr/news/articleView.html?idxno=99156 | https://news.bizwatch.co.kr/article/finance/2026/05/22/0043 | https://www.socialvalue.kr/news/view/1065600234596663 | http://www.thefirstmedia.net/news/articleView.html?idxno=199980 | https://www.todayeconomic.com/news/article.html?no=30719

### 2. NHN클라우드

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `CSP 운영 기업`
- 분류: `cloud_npuaaS_lead`
- 확인된 프로젝트/시그널: AI 풀스택 브랜드 'FactoryX' 출시 및 광주/서울 AI 데이터센터 운영
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 모델 호환성은 미확인이지만, NHN클라우드의 팩토리X와 광주 AI 데이터센터에서 국산 NPU 통합 운영 의지를 밝혀 CSP capacity expansion 및 NPUaaS 연계 가능성이 매우 높음.
- hook_type: `CLOUD`
- 핵심 buying signal: GPU 수급난 대응 및 AI 추론 효율 극대화를 위한 국산 NPU 도입 가속화
- 인프라 signal: 서울/광주 AI 전용 데이터센터 내 엔비디아 GPU 및 국산 NPU 하이브리드 운영
- timing reason: FactoryX 브랜드 공식 출범 및 팩토리X 서울 데이터센터 구축 시점
- 고객 win: 엔비디아 의존도를 낮추고 국산 NPU를 통한 추론 최적화 및 비용 효율화
- FuriosaAI win: 국내 주요 AI CSP 파트너 확보 및 대규모 추론 인프라 레퍼런스 구축
- 직접 판매 가능성: `MID`
- CSP 경유 판매 가능성: `HIGH`
- NPUaaS 유도 가능성: `HIGH`
- CSP capacity 증설 가능성: `HIGH`
- 수치 근거: B200 GPU 7656장 투입 (S038) — 근거: 엔비디아 B200 GPU 7656장을 기반으로 총 27...
- 컨택 명분: FactoryX 내 국산 NPU 생태계 구축 관련 FuriosaAI의 최적화 스택 연동 논의
- 실제 컨택 시 사용할 말: 최근 팩토리X 출시 소식을 확인했습니다. 당사의 RNGD 인프라가 NHN클라우드의 AI 추론 풀스택 환경에서 효율적으로 구동될 수 있도록 기술적 협력을 검토하고 싶습니다.
- 매출 가능 시점: `중기`
- 담당자 후보 힌트: 김태형 CTO / AI 인프라 사업 총괄 임원
- 공개 프로필 URL: 
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: NPU 통합 운영 구체적 사양 | 팩토리X 내 FuriosaAI 솔루션 탑재 로드맵
- source_ids: S006, S026, S033, S035, S038, S039, S040
- source_urls: http://www.biztribune.co.kr/news/articleView.html?idxno=354147 | https://www.megaeconomy.co.kr/news/newsview.php?ncode=1065579909469061 | https://www.mhj21.com/news/articleView.html?idxno=252348 | https://biz.chosun.com/it-science/ict/2026/05/26/K73CFXG73NGZLDYOLJYKKMARGM/?utm_source=naver&utm_medium=original&utm_campaign=biz | https://www.hankyung.com/article/2026052699161 | https://www.sedaily.com/article/20048370?ref=naver | https://news.mtn.co.kr/news-detail/2026052616115639487


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

1. **위즈코어, AI 팩토리 전환 전략 제시… "설비 데이터 연결 구조 재설계...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T17:44:00+09:00`
   - matched_query_or_feed: `제조 AI 플랫폼`
   - url: https://www.industrynews.co.kr/news/articleView.html?idxno=81436
   - summary_snippet: 실제 제조 현장에 적용 가능한 AI 활용 기반을 마련할 수 있다고 설명했다. 위즈코어는 자사의 산업용 데이터 플랫폼 'NEXEDGE(넥스엣지)'를 통해 이러한 데이터 연결 구조의 기반 기술을 고도화하고 있다....

2. **서버부터 클라우드까지 … IT 올인원 서비스**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T17:44:00+09:00`
   - matched_query_or_feed: `국방 AI 인프라`
   - url: https://www.mk.co.kr/article/12058031
   - summary_snippet: 관리하는 'AI 통합 구축 및 활용 플랫폼'을 개발한 후 만족도는 상당히 높았다. 국방 보안을 위해 외부와... 서버, 네트워크, 데이터 등 IT 인프라의 통합 모니터링이 핵심이다. 브레인즈컴퍼니는 2022년 AI 기업...

3. **NHN클라우드, AI 풀스택 ‘팩토리X’ 공개…“내년 AI 매출 비중 50%로”**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T17:44:00+09:00`
   - matched_query_or_feed: `국내 클라우드 GPU 서비스`
   - url: https://www.hani.co.kr/arti/economy/it/1260467.html
   - summary_snippet: (NHN)클라우드가 고성능 그래픽처리장치(GPU) 임대 서비스를 본격화하며 “내년까지 인공지능 분야 매출... 묶어 국내 최대 수준의 연산 성능(단일 클러스터 기준·27.4 엑사플롭스)을 구현하는 등 차별화된 인공지능...

4. **「Stella AI for Biz」がデジタル化・AI導入補助金2026に認定 - ニュースメディアVOIX**
   - source: `rss`
   - published_at_kst: `2026-05-26T17:42:19+09:00`
   - matched_query_or_feed: `Google News JP 生成AI 導入`
   - url: https://news.google.com/rss/articles/CBMicEFVX3lxTE93cXBOdTdleFA1R0Foenc5T2lTMnk3c1RqUDZSOTg0bHpvTy1WX1FUeUh5cmMtdTZVNTJiTlVZWGxhemlUUXhqLS1VVmI1bi1PVlIxcVFCVXFGRURQdkZjVzl3X0tmRXd1Qlh6MWpRYVA?oc=5
   - summary_snippet: 「Stella AI for Biz」がデジタル化・AI導入補助金2026に認定  ニュースメディアVOIX

5. **SK하이닉스 'iHBM' 기술로 고대역폭메모리 발열 잡는다, 차세대 제품부...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T17:42:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.huffingtonpost.kr/article/257464
   - summary_snippet: SK하이닉스는 iHBM 기술을 8세대(HBM5) 등 차세대 제품부터 적용해 고성능 컴퓨팅(HPC), AI 데이터센터 등 초고집적·초고대역폭 환경에서 요구되는 열 관리 수준을 충족하며 시스템 전반의 안정성과 운영 효율을...

6. **딥시크, 사용료 75% 파격 인하…AI 모델 업계 가격 경쟁 신호탄**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T17:42:00+09:00`
   - matched_query_or_feed: `GPU 클라우드`
   - url: https://www.thelec.kr/news/articleView.html?idxno=57160
   - summary_snippet: 클라우드 산업 초창기에 아마존(AWS)식 가격 파괴 전략과 유사하다. 해외 개발자 커뮤니티에서는 "이제 AI... 미국의 대중국 반도체 규제로 인해 엔비디아 최신 GPU 확보가 어려워진 중국 기업들이 자체 생태계...

7. **'빨리빨리'의 나라에서 웰니스는 어떻게 '트렌드'가 되었나**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T17:42:00+09:00`
   - matched_query_or_feed: `병원 AI 플랫폼`
   - url: http://www.ktnews.com/news/articleView.html?idxno=146224
   - summary_snippet: 병원 시술, 피부 관리, 기능성 화장품, 이너뷰티, 웨어러블 디바이스와 AI 기반 헬스케어 플랫폼까지 서로 유기적으로 연결되어 발전한다. 메디큐브는 총매출액 1조 4000억 원을 돌파하며 국내 단일 브랜드 최고 매출을...

8. **"1만피 벽도 깬다" 전망 쏟아져 … 고개드는 금리 인상론은 복병**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T17:41:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.mk.co.kr/article/12058022
   - summary_snippet: 현재 시장은 유가 상승 부담을 AI와 데이터센터 중심의 투자 증가세로 흡수하고 있지만, 유가가 다시 뛰고 금리가 높아지면 강세장 종료 신호로 작용할 수 있다. AI 투자 사이클을 둘러싼 불확실성도 변수다. 미국에서...

9. **"위성 100만기면 HBM이 도대체 몇 개야"…초유의 상황에 개미 '들썩'**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T17:41:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.wowtv.co.kr/NewsCenter/News/Read?articleId=A202605260270&t=NNv
   - summary_snippet: 이 때문에 24시간 데이터를 써야하고, 지상에 있는 게이트웨이와 AI 데이터센터 연결망을 확대해야 합니다. 통신 역할을 하는 게이트웨이에는 통신용 RF 장비, 네트워크 서버, 광통신 장비 등이 들어가는데, 반도체로는...

10. **「日本DX大賞2026」サステナビリティ部門のファイナリストに選出**
   - source: `rss`
   - published_at_kst: `2026-05-26T17:40:39+09:00`
   - matched_query_or_feed: `PR TIMES JP (AI keyword)`
   - url: https://prtimes.jp/main/html/rd/p/000000143.000020176.html
   - summary_snippet: [株式会社フォーラムエイト]
株式会社フォーラムエイト（本社：東京都港区港南2-15-1、社長：伊藤裕二、URL：https://www.forum8.co.jp）は、松江土建株式会社（本社：島根県松江市、代表取締役社長：尾添純一）との共同の取り組みである「3D...

11. **🔹 ORICO、40Gbps超高速USB4.0 NVMe SSDケースを発表⚡ 読込3700MB/s・最大4TB対応・Thunderbolt 4互換・高放熱設計**
   - source: `rss`
   - published_at_kst: `2026-05-26T17:40:39+09:00`
   - matched_query_or_feed: `PR TIMES JP (AI keyword)`
   - url: https://prtimes.jp/main/html/rd/p/000000157.000145928.html
   - summary_snippet: [深圳市奥睿科电子商务有限公司]
[画像1: https://prcdn.freetls.fastly.net/release_image/145928/157/145928-157-315143de460c84c91967ccf90f224568-1071x1500.jpg?width=536&quality=85%2C75&format=jpeg&auto=webp&fit=bound...

12. **出羽三山神社の朝の神事を見学できるリゾートホテル「休暇村庄内羽黒」　お客様アンケート「体験」部門で3年連続全国１位を獲得　午年の “御縁年”となる2026年は、羽黒山参拝の好機**
   - source: `rss`
   - published_at_kst: `2026-05-26T17:40:39+09:00`
   - matched_query_or_feed: `PR TIMES JP (AI keyword)`
   - url: https://prtimes.jp/main/html/rd/p/000000755.000085653.html
   - summary_snippet: [自然にときめくリゾート 休暇村]
[画像1: https://prcdn.freetls.fastly.net/release_image/85653/755/85653-755-06b79c614546bbec4a15c631a1471d7e-3900x2601.jpg?width=536&quality=85%2C75&format=jpeg&auto=webp&fit=bounds&...

13. **九州大学に「GAKUEN RX 2.0」シリーズを導入決定**
   - source: `rss`
   - published_at_kst: `2026-05-26T17:40:39+09:00`
   - matched_query_or_feed: `PR TIMES JP (AI keyword)`
   - url: https://prtimes.jp/main/html/rd/p/000000169.000092153.html
   - summary_snippet: [日本システム技術株式会社]
　日本システム技術株式会社（本社：大阪市北区、代表取締役社長：平林 卓、以下「JAST」）は、国立大学法人九州大学（本部：福岡市西区、総長：石橋 達朗、以下「九州大学」）において、戦略的大学経営システム...

14. **【横浜/大宮】夏が旬のマンゴーやパイナップル、ハーゲンダッツ アイスクリームが織りなす至福のスイーツ　　　「トロピカルサンセットパフェwithハーゲンダッツ」**
   - source: `rss`
   - published_at_kst: `2026-05-26T17:40:39+09:00`
   - matched_query_or_feed: `PR TIMES JP (AI keyword)`
   - url: https://prtimes.jp/main/html/rd/p/000001312.000004975.html
   - summary_snippet: [ベストブライダル]
　株式会社ベストブライダル（本社：東京都港区、代表取締役：塚田正之）では、運営するレストラン「リストランテ マンジャーレ 伊勢山」「リストランテ マンジャーレ ウォーターエッジ YOKOHAMA」（ともに神奈川...

15. **ゲームアプリ『ヒプノシスマイク -Alternative Rap Battle-』イベント「正鵠射るはひとすじの矢～無段の弓あそび～」**
   - source: `rss`
   - published_at_kst: `2026-05-26T17:40:39+09:00`
   - matched_query_or_feed: `PR TIMES JP (AI keyword)`
   - url: https://prtimes.jp/main/html/rd/p/000000333.000053906.html
   - summary_snippet: [株式会社オルトプラス]
[画像1: https://prcdn.freetls.fastly.net/release_image/53906/333/53906-333-b8958ae052989b3f751c99bc88297610-960x540.jpg?width=536&quality=85%2C75&format=jpeg&auto=webp&fit=bounds&am...

16. **2026年7月6日（月）より放送開始決定！TVアニメ『ここは俺に任せて先に行けと言ってから10年がたったら伝説になっていた。』ロックと仲間たちを描くキービジュアルが解禁！**
   - source: `rss`
   - published_at_kst: `2026-05-26T17:40:39+09:00`
   - matched_query_or_feed: `PR TIMES JP (AI keyword)`
   - url: https://prtimes.jp/main/html/rd/p/000000156.000090815.html
   - summary_snippet: [グリーエンターテインメント株式会社]
[画像1: https://prcdn.freetls.fastly.net/release_image/90815/156/90815-156-7f9b150bc4673cc6d03f32166742316d-3541x2213.jpg?width=536&quality=85%2C75&format=jpeg&auto=webp&fit=bounds&...

17. **クリエイティブ現場で起こりがちなすれ違いは、共感型の対話スキルで解消できる！6/9（火）『正論よりも「共感」が欲しい ～クリエイターの心を開く 1on1 の技術～』のアーカイブ映像を無料配信！**
   - source: `rss`
   - published_at_kst: `2026-05-26T17:40:39+09:00`
   - matched_query_or_feed: `PR TIMES JP (AI keyword)`
   - url: https://prtimes.jp/main/html/rd/p/000004825.000003670.html
   - summary_snippet: [クリーク・アンド・リバー社]
[画像1: https://prcdn.freetls.fastly.net/release_image/3670/4825/3670-4825-7e3db20e970d3af2f0017f81c335f671-910x511.png?width=536&quality=85%2C75&format=jpeg&auto=webp&fit=bounds&am...

18. **セブンプレミアムの冷凍食品からお腹を満たす「大盛り チャーハン」が登場！5月26日（火）より全国のセブン‐イレブンにて順次発売**
   - source: `rss`
   - published_at_kst: `2026-05-26T17:40:39+09:00`
   - matched_query_or_feed: `PR TIMES JP (AI keyword)`
   - url: https://prtimes.jp/main/html/rd/p/000000866.000155396.html
   - summary_snippet: [株式会社セブン‐イレブン・ジャパン]
[画像1: https://prcdn.freetls.fastly.net/release_image/155396/866/155396-866-fbff3c9078a54cd0a0d5b884c7242924-1340x1000.jpg?width=536&quality=85%2C75&format=jpeg&auto=webp&fit=bound...

19. **玄人志向から、Realtek RTL8127AT 搭載 10GBase-T LANカード(イーサネットボード)『GBE10R-PCIE』を発売**
   - source: `rss`
   - published_at_kst: `2026-05-26T17:40:39+09:00`
   - matched_query_or_feed: `PR TIMES JP (AI keyword)`
   - url: https://prtimes.jp/main/html/rd/p/000001107.000032645.html
   - summary_snippet: [CFD販売株式会社]
[画像1: https://prcdn.freetls.fastly.net/release_image/32645/1107/32645-1107-3f178a0c487ca8dc675c2d608c891f66-550x400.png?width=536&quality=85%2C75&format=jpeg&auto=webp&fit=bounds&...

20. **【Dior】カンヌ国際映画祭の閉会式でルース・ネッガ、ローラ・ワンデル、イリス・ノブロックがディオールを着用**
   - source: `rss`
   - published_at_kst: `2026-05-26T17:40:39+09:00`
   - matched_query_or_feed: `PR TIMES JP (AI keyword)`
   - url: https://prtimes.jp/main/html/rd/p/000002951.000008795.html
   - summary_snippet: [クリスチャン・ディオール合同会社]
2026年5月23日、カンヌ国際映画祭の閉会式に、ルース・ネッガ、ローラ・ワンデル、イリス・ノブロックが、ディオールを纏い登場しました。

[画像1: https://prcdn.freetls.fastly.net/release_image/8795/2951/8...


## 다음 단계

1. LLM 후보 품질 확인
2. 노이즈가 많으면 NAVER_QUERIES / RSS_FEEDS 개선
3. 후보가 너무 적으면 MAX_LLM_SOURCES 상향
4. Gemini 3.5 Flash vs 2.5 Flash 품질 비교
5. 나라장터/B2G 수집 추가
6. 담당자/의사결정자 탐색 추가
7. Notion 또는 Google Docs 업로드 추가
