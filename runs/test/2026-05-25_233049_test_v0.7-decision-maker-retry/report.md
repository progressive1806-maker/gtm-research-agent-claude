# FuriosaAI GTM Research Agent Test Run

## 실행 정보

- run_id: `2026-05-25_233049_test_v0.7-decision-maker-retry`
- mode: `test`
- memo: `v0.7-decision-maker-retry`
- executed_at_kst: `2026-05-25T23:35:39.089899+09:00`
- agent_version: `v0.7`
- instructions_loaded_chars: `21592`
- naver_sources_recent_7d_count: `213`
- rss_sources_recent_7d_count: `97`
- merged_sources_recent_7d_count: `310`
- furiosa_docs_successful: `11`
- furiosa_docs_failed: `0`
- llm_called: `False`
- llm_error: `503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}`

## 현재 단계

이 실행은 v0.7 테스트입니다.

이번 버전에서는 네이버 뉴스 API, RSS feed, FuriosaAI 공개 개발자 문서를 수집한 뒤 Gemini로 GTM 후보를 1차 평가하고, 별도 LLM 호출로 매니저용 gtm_report.md를 작성합니다.

아직 나라장터 직접 API, 담당자 심화 탐색, Notion 업로드는 수행하지 않았습니다.

## LLM 실행 요약

- overall_assessment: 
- top_priority_names: 
- noise_ratio_comment: 
- model_compatibility_caution: 

LLM 평가 실패 또는 미실행: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}

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

8. **"AI로 건강수명 관리"…차헬스케어, '소요한남'에 AI 기반 시니어 헬스케...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T22:32:00+09:00`
   - matched_query_or_feed: `병원 AI 플랫폼`
   - url: http://www.thefirstmedia.net/news/articleView.html?idxno=199949
   - summary_snippet: 경험, AI 디지털 플랫폼 역량을 결합한 것이 특징이다. 차헬스케어는 입주자 전원에게 전담 헬스케어... 특히 초고령사회 진입과 함께 건강수명 연장에 대한 관심이 커지는 가운데, 병원 중심 치료에서 예방·상시 관리...

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
