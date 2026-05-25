# FuriosaAI GTM Research Agent Test Run

## 실행 정보

- run_id: `2026-05-25_223853_test_v0.7-decision-maker-test`
- mode: `test`
- memo: `v0.7-decision-maker-test`
- executed_at_kst: `2026-05-25T22:48:03.011404+09:00`
- agent_version: `v0.7`
- instructions_loaded_chars: `21592`
- naver_sources_recent_7d_count: `214`
- rss_sources_recent_7d_count: `96`
- merged_sources_recent_7d_count: `310`
- furiosa_docs_successful: `11`
- furiosa_docs_failed: `0`
- llm_called: `False`
- llm_error: `Server disconnected without sending a response.`

## 현재 단계

이 실행은 v0.7 테스트입니다.

이번 버전에서는 네이버 뉴스 API, RSS feed, FuriosaAI 공개 개발자 문서를 수집한 뒤 Gemini로 GTM 후보를 1차 평가하고, 별도 LLM 호출로 매니저용 gtm_report.md를 작성합니다.

아직 나라장터 직접 API, 담당자 심화 탐색, Notion 업로드는 수행하지 않았습니다.

## LLM 실행 요약

- overall_assessment: 
- top_priority_names: 
- noise_ratio_comment: 
- model_compatibility_caution: 

LLM 평가 실패 또는 미실행: Server disconnected without sending a response.

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

1. **"5~20년 후 관절 건강 예측"…GC녹십자, 혈우병 환자 맞춤형 AI 진단 플랫...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T22:32:00+09:00`
   - matched_query_or_feed: `병원 AI 플랫폼`
   - url: http://www.thefirstmedia.net/news/articleView.html?idxno=199952
   - summary_snippet: 삼성서울병원과 공동으로 보건복지부 '첨단바이오 융합인재 양성 사업' 과제에 선정돼 세계 최초 AI 기반... 업계에서는 향후 해당 기술이 혈우병뿐 아니라 만성 희귀질환 관리 플랫폼으로 확장될 가능성에도 주목하고...

2. **광주연구원 "UN AI 허브 유치로 광주 글로벌 AI 거점 도약해야"**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T22:14:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.mhns.co.kr/news/articleView.html?idxno=748341
   - summary_snippet: 연구원은 광주가 지난 2019년부터 2024년까지 추진한 AI 중심도시 1단계 사업을 통해 국가 AI 데이터센터를 비롯해 인재 양성 체계, 기업 유치, 연구개발 지원 기반 등을 구축하며 AI 산업 기반을 확대해 왔다고...

3. **[인터뷰] 엘칸토, '브랑누아' 별도 법인으로 스핀오프**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T22:04:00+09:00`
   - matched_query_or_feed: `제조 AI 플랫폼`
   - url: http://www.apparelnews.co.kr/news/news_view/?idx=225419
   - summary_snippet: 제조와 공급망은 기존 엘칸토 인프라와 별개로 차별화된 신규 인프라를 활용하며, 향후 채널 확대를 위한... 플랫폼 내에서도 엘칸토 소속 브랜드와 카니발라이제이션을 최소화하고 타깃과 컨셉을 차별화하는...

4. **소상공인 온라인 판로 지원 '소담스퀘어 울산' 들어선다**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T21:43:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.ulsanpress.net/news/articleView.html?idxno=575840
   - summary_snippet: '소담스퀘어 울산'은 인공지능(AI) 디지털 스튜디오를 비롯해 주방(키친)·다중(멀티)·1인 미디어 스튜디오... 울산시는 울산연구원 빅데이터센터, 울산정보산업진흥원, 울산소상공인연합회 등 지역 유관기관 및...

5. **초대 통합특별시 미래 좌우할 공약, 방점은 '미래 먹거리 산업' 육성에**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T21:28:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: http://www.mdilbo.com/detail/tohfpC/755848
   - summary_snippet: 후보들이 AI(인공지능) 등 미래 먹거리 산업 집중 육성을 통한 특별시 발전 전략을 모색하고 있는 것으로 나타났다. 이재명 정부의 ‘5극 3특 국가균형성장’과 맞물려 산업 대전환 필요성과 함께 데이터센터 유치 등...

6. **[투자를IT다] 2026년 5월 3주차 IT기업 주요 소식과 시장 전망**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T21:24:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://it.donga.com/108937/
   - summary_snippet: 데이터센터와 반도체 자동화 테스트 사업은 AI 인프라 투자에 힘입어 가파른 성장 궤도에 올랐으며, 2027년까지 지속될 것으로 확신한다. 항공우주·방위 분야에서는 각국의 국방 자주권 강화 기조가 다년간의...

7. **[2026 대구경북 이노비즈 기업을 찾아서] (2) 고품질 건강기능식품 전문...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T21:24:00+09:00`
   - matched_query_or_feed: `제조 AI 플랫폼`
   - url: https://www.idaegu.co.kr/news/articleView.html?idxno=549132
   - summary_snippet: 제안하는 'AI 헬스케어 어드바이징 프로그램'을 고도화하고 있으며, 고객 개개인에게 맞춤형 건강 설루션을 제공하는 차세대 플랫폼 구축을 목표로 하고 있다. 에이팜건강은 이 같은 기술 혁신의 원동력은 임직원의...

8. **장수군수 선거, 전·현직 재대결…기본사회 해법은?**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T21:17:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://news.kbs.co.kr/news/pc/view/view.do?ncd=8569474&ref=A
   - summary_snippet: 양수발전소 유치와 햇빛소득마을, AI 데이터센터를 연계해 신재생에너지 소득을 기반으로 한 기본사회로 나아가겠다는 구상입니다. [최훈식/민주당 장수군수 후보 : "기본소득을 바탕으로 해서 의료, 돌봄, 교육, 정주...

9. **사대와 왜색의 굴레 언제 벗을까?**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T21:16:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: http://www.gnmaeil.com/news/articleView.html?idxno=587263
   - summary_snippet: AI 시대에 살고 있다. 잘못된 사대와 왜색의 문화를 바로잡지 못한다면 그 폐해는 눈덩이처럼 불어날 것이다. 왜곡된 정보로 채워진 데이터 센터의 클라우드는 가상의 세계를 혼탁하게 만들 것이다. 그리고 이를 바로...

10. **2026 남도의 선택)강진군수 선거, 현직이냐 민주당이냐**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T21:14:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://mpmbc.co.kr/NewsArticle/1520163
   - summary_snippet: 그 재원은 강진군에 전국에서 가장 큰 규모의 AI 데이터센터 유치를 통해서.. 이번 선거는 민주당 조직력과 현역 군수의 인지도, 그리고 공천 갈등 이후 형성된 지역 민심이 판세를 가를 핵심 변수로 꼽힙니다. 다가올...

11. **(시장 후보에게 듣는다) 청년일자리 분야**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T20:54:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: http://web.ubc.co.kr/wp/archives/127773
   - summary_snippet: ' AI데이터센터 건립에 따른 관련 기업 유치, 지역 대학· 기업과의 취업 연계 활성화 등이 청년 유출을 막기 위한 주요 과제로 떠오르고 있습니다. 유비씨 뉴스 전병주입니다. -2026/05/25

12. **[미리보는 이데일리 신문]'사회적 감수성' 놓친 마케팅…기업 생존 위협...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T20:52:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.edaily.co.kr/news/newspath.asp?newsid=02082806645452528
   - summary_snippet: 올리고…AI 데이터센터 짓고 시멘트 기업, 부동산 개발 ‘큰손’ 변신 △이데일리가 만났습니다 -“파키스탄은 美·이란 모두 설득할 수 있는 나라…종전 이끌어 낼 것” -“백제에 불교 전한 1700년 인연…CEPA 체결로...

13. **“스페이스X 투자 놓쳤다?” 또다른 기회…오픈AI 수혜주가 있다 [투자...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T20:41:00+09:00`
   - matched_query_or_feed: `생성형 AI 도입 기업`
   - url: https://biz.heraldcorp.com/article/10743640?ref=naver
   - summary_snippet: [게티이미지] 일론 머스크의 우주기업 스페이스X에 이어 생성형 인공지능(AI) 대표 기업 오픈AI도 기업공개... 이처럼 국내 기업들의 협업 범위가 단순 제휴를 넘어 실제 서비스 도입과 구축 단계까지 확대되면서...

14. **"치유로 잇는 한·베 연대"…봄재단, 고엽제 지원 확대**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T20:40:00+09:00`
   - matched_query_or_feed: `병원 AI 플랫폼`
   - url: https://view.asiae.co.kr/article/2026052520233985334
   - summary_snippet: 협력 플랫폼 구축 방안도 논의했다. 논의 안에는 ▲고엽제 피해 환우 전문 치료·재활 병원 ▲건강검진센터 ▲AI·디지털 헬스케어 기반 예방의학 시스템 ▲줄기세포 연구·치료센터 ▲메디컬 뷰티 시스템 구축 등이...

15. **“스페이스X 투자 놓쳤다?” 또다른 기회…오픈AI 수혜주가 있다 [투자360] - 헤럴드경제**
   - source: `rss`
   - published_at_kst: `2026-05-25T20:40:00+09:00`
   - matched_query_or_feed: `Google News KR 생성형 AI`
   - url: https://news.google.com/rss/articles/CBMiVkFVX3lxTE5ROUE4TW1Sc0JrRS1fV2FhelVMYzQyQ3h2Uk8tbnp5MnpKS2NXVjVLeGo3RGthWWZXTmJiNE40UVlrOU5fbmtqcjRyTWp4dGlsOTAtM1hn?oc=5
   - summary_snippet: “스페이스X 투자 놓쳤다?” 또다른 기회…오픈AI 수혜주가 있다 [투자360]  헤럴드경제

16. **[중국증시 주간 포인트] 5월 PMI, D램 리더 '창신메모리' IPO, 화웨이 '에...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T20:29:00+09:00`
   - matched_query_or_feed: `제조 AI 플랫폼`
   - url: https://www.newspim.com/news/view/20260525000259
   - summary_snippet: 5월 제조업 PMI 발표 △中 D램 선도기업 '창신메모리' IPO 심의 △화웨이, '에이전트아트' 오픈소스... 화웨이, '에이전트아트' 오픈소스 강화판 공개 중국 화웨이가 5월 30일 기업용 AI 에이전트 개발 플랫폼...

17. **日 화낙-구글, 피지컬 AI 분야 전략적 제휴**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T20:18:00+09:00`
   - matched_query_or_feed: `생성형 AI 도입 기업`
   - url: https://www.irobotnews.com/news/articleView.html?idxno=46545
   - summary_snippet: 일본 산업용 로봇 기업 화낙(FANUC)이 구글과 전략적 협력을 통해 '피지컬 AI(Physical AI)' 기반 산업용 로봇... 기술을 도입한 바 있다. 여기에 구글의 생성형 AI와 추론 기술까지 더해지면서, AI 기반 공장 자동화...

18. **[인터뷰] 고진석 텐스페이스 대표 "데이터센터 멈춘 진짜 이유는 불신" - 한스경제**
   - source: `rss`
   - published_at_kst: `2026-05-25T20:09:57+09:00`
   - matched_query_or_feed: `Google News KR AI 데이터센터`
   - url: https://news.google.com/rss/articles/CBMia0FVX3lxTE5YWmo5ZXkzSko0R3E2cHFfblZYQ09FU091dUh5cnBjREtOTUlQRWVGdHFsNVY2ZDZfT0R0Y3llX0tEd2ZHQWJOSTFwZG1wdmxnQ05qRzJDRHVSNkx1bURnUXF6bjA2Q19NQlJz?oc=5
   - summary_snippet: [인터뷰] 고진석 텐스페이스 대표 "데이터센터 멈춘 진짜 이유는 불신"  한스경제

19. **“세 번의 창업 끝에 찾은 답”…넥스테인 양병석 대표가 만드는 로컬 ...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T19:56:00+09:00`
   - matched_query_or_feed: `클라우드 AI 서비스`
   - url: https://www.venturesquare.net/1085242/
   - summary_snippet: 핵심은 클라우드가 아니라 ‘내 컴퓨터 안에서 직접 돌아가는 AI’라는 점이다. 기존 거대 AI 서비스들은 사용자의 대화와 데이터를 외부 서버에서 처리한다. 편리함은 있지만, 회사...

20. **조선소 인수 나선 부산 기자재사들…해양종합기업 박차**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-25T19:30:00+09:00`
   - matched_query_or_feed: `제조 AI 플랫폼`
   - url: http://www.kookje.co.kr/news2011/asp/newsbody.asp?code=0200&key=20260526.22010006486
   - summary_snippet: 스마트 선박 운영 플랫폼 구축 등 해양 AX 분야 투자도 확대한다. 적극적인 투자로 지난해에는 창사 이래 역대 매출 1316억 원을 기록하기도 했다. 회의에 참석한 전문가들은 “AI 역량이 다소 떨어지는 지역 제조업계에...


## 다음 단계

1. LLM 후보 품질 확인
2. 노이즈가 많으면 NAVER_QUERIES / RSS_FEEDS 개선
3. 후보가 너무 적으면 MAX_LLM_SOURCES 상향
4. Gemini 3.5 Flash vs 2.5 Flash 품질 비교
5. 나라장터/B2G 수집 추가
6. 담당자/의사결정자 탐색 추가
7. Notion 또는 Google Docs 업로드 추가
