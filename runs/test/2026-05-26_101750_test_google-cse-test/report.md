# FuriosaAI GTM Research Agent Test Run

## 실행 정보

- run_id: `2026-05-26_101750_test_google-cse-test`
- mode: `test`
- memo: `google-cse-test`
- executed_at_kst: `2026-05-26T10:23:56.336422+09:00`
- agent_version: `v0.7`
- instructions_loaded_chars: `21592`
- naver_sources_recent_7d_count: `197`
- rss_sources_recent_7d_count: `230`
- merged_sources_recent_7d_count: `427`
- furiosa_docs_successful: `11`
- furiosa_docs_failed: `0`
- llm_called: `True`
- llm_error: ``

## 현재 단계

이 실행은 v0.7 테스트입니다.

이번 버전에서는 네이버 뉴스 API, RSS feed, FuriosaAI 공개 개발자 문서를 수집한 뒤 Gemini로 GTM 후보를 1차 평가하고, 별도 LLM 호출로 매니저용 gtm_report.md를 작성합니다.

아직 나라장터 직접 API, 담당자 심화 탐색, Notion 업로드는 수행하지 않았습니다.

## LLM 실행 요약

- overall_assessment: 금융권 망분리 규제 완화에 따른 프라이빗 AI 보안 시스템 구축 수요와 국내 주요 CSP 및 AI 클라우드 제공사들의 인프라 증설 움직임이 포착됩니다. 특히 삼성SDS의 대규모 데이터센터 투자 및 전력 확보, 엘리스그룹의 코스닥 상장 추진 및 GPUaaS 확장 등은 NPUaaS 연계 및 대형 채널 확보 관점에서 매우 강력한 GTM 기회를 제공합니다.
- top_priority_names: 삼성SDS, 엘리스그룹, KB금융그룹
- noise_ratio_comment: 수집된 40건의 소스 중 단순 제약계 동향, 이커머스 민원 관련 소식, 전기공사 실적 관련 기사 등 3건을 노이즈로 분류하였습니다. 전반적으로 망분리 완화와 데이터센터 인프라 전력 수급 이슈 등 유효한 GTM 신호의 비중이 높습니다.
- model_compatibility_caution: 본 보고서에 포함된 유효 후보군 중 현재 명확한 타깃 서비스 모델명이 기사 상으로 확인된 사례는 없습니다. 따라서 호환 모델 매칭 점수는 UNKNOWN으로 보수적으로 평가하였으며, 추후 vLLM 연동 및 Triton Server 환경을 통한 드롭인 대체 가능성을 기반으로 한 아키텍처 레벨의 검증 영업이 필요합니다.

## LLM 후보 평가 결과

## 버전 1 — B2B only 우선 검토 요약

- 삼성SDS / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- 엘리스그룹 / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- KB금융그룹 / 온프레미스 기업 / classification: `structure_check` / fit: `MID` / outreach: `MID` / 매출시점: `중기`
- 시스트란 / 온프레미스 기업 / classification: `structure_check` / fit: `MID` / outreach: `MID` / 매출시점: `중기`
- 오픈네트웍시스템 / CSP 고객 기업 / classification: `structure_check` / fit: `MID` / outreach: `MID` / 매출시점: `중기`
- 서울아산병원 / 온프레미스 기업 / classification: `watchlist` / fit: `MID` / outreach: `MID` / 매출시점: `장기`


## 버전 2 — B2B + B2G 우선 검토 요약

- 삼성SDS / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- 엘리스그룹 / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- KB금융그룹 / 온프레미스 기업 / classification: `structure_check` / fit: `MID` / outreach: `MID` / 매출시점: `중기`
- 시스트란 / 온프레미스 기업 / classification: `structure_check` / fit: `MID` / outreach: `MID` / 매출시점: `중기`
- 오픈네트웍시스템 / CSP 고객 기업 / classification: `structure_check` / fit: `MID` / outreach: `MID` / 매출시점: `중기`
- 서울아산병원 / 온프레미스 기업 / classification: `watchlist` / fit: `MID` / outreach: `MID` / 매출시점: `장기`


## 상세 후보 평가

### 1. 삼성SDS

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `CSP 운영 기업`
- 분류: `priority_outreach`
- 확인된 프로젝트/시그널: 경북 구미 AI 데이터센터 투자 및 경기 동탄 데이터센터 서관 가동 가속화
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 모델 정보는 미확인이지만 경북 구미에 대규모 AI 데이터센터를 짓고 전력을 확보하는 등 클라우드 인프라 확장 속도가 빠르며, SCP 및 NPUaaS 서비스 다각화 측면에서 채널 파트너로서의 우선순위가 매우 높습니다.
- hook_type: `CLOUD`
- 핵심 buying signal: 경북 구미에 인프라를 구축하며 데이터센터 투자를 본격화하고 있으며 동탄 데이터센터 전력 확보와 함께 자체 AI 클라우드인 SCP의 추론 처리량 대응을 위한 국산 NPU 수용 가능성이 증대되고 있습니다.
- 인프라 signal: 경기 동탄 데이터센터 서관 가동을 위한 전력 확보 및 경북 구미 데이터센터 신설을 통한 AI 연산 자원 및 전력 용량 대폭 확장 흐름이 확인됩니다.
- timing reason: 국내 주요 CSP들과 함께 공동 전선을 구축하여 글로벌 CSP의 진입 및 GPU 공급난에 대응하는 시점으로, 비용 효율성이 높은 RNGD 기반 NPUaaS 라인업 확보가 요구되는 적기입니다.
- 고객 win: 삼성SDS의 AI 클라우드(SCP) 고객사들에게 GPU 대비 우수한 비용 효율과 낮은 전력 소모를 보장하는 추론 인프라 옵션을 제공할 수 있습니다. 전력 포화 상태인 수도권 외 지역 데이터센터 운영 시 전력 사용량 저감에 기여합니다.
- FuriosaAI win: 삼성SDS SCP 플랫폼에 RNGD가 핵심 NPUaaS 라인업으로 정식 채택될 경우 엔터프라이즈 및 공공 수요를 아우르는 대규모 CSP 경유 매출과 지속적인 인프라 증설 기회를 확보할 수 있습니다.
- 직접 판매 가능성: `LOW`
- CSP 경유 판매 가능성: `HIGH`
- NPUaaS 유도 가능성: `HIGH`
- CSP capacity 증설 가능성: `HIGH`
- 수치 근거: 삼성SDS 경기 동탄 데이터센터 서관 가동을 위해 20MW급 전력 확보 (S026) — 근거: 삼성SDS가 경기 동탄 데이터센터 서관 가동을 위해 20MW급 전력을 확보한 사례 | 삼성SDS 경북 구미 AI 데이터센터에 4273억원 투자 및 60MW 규모 구축 계획 (S032) — 근거: 삼성SDS는 경북 구미에 4273억원을 투자해 60MW 규모 AI 데이터센터를 짓기로 했다.
- 컨택 명분: 구미와 동탄의 대규모 AI 인프라 구축 및 국내 CSP의 고효율 자원 다각화 추진 시점에 맞추어 SCP 내 NPUaaS 라인업 구성을 제안하고자 합니다.
- 실제 컨택 시 사용할 말: 최근 구미 데이터센터 투자와 동탄 데이터센터 전력 확보 소식을 접하고 연락드렸습니다. 전력 및 상면 제약이 커지는 시점에 초고효율 아키텍처인 RNGD를 활용하여 SCP 내에 차세대 고성능 NPUaaS를 신속히 도입하고 공급망 리스크를 해소하는 방안을 논의하고 싶습니다.
- 매출 가능 시점: `단기`
- 담당자 후보 힌트: 클라우드서비스사업부장, SCP 플랫폼 개발본부장, 인프라아키텍처팀장, AI 인프라 기획 부서장
- 공개 프로필 URL: 
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 삼성SDS 자체 개발 플랫폼 혹은 SCP 고객사 중 Llama-3.1 계열 또는 Qwen2.5 계열의 오픈소스 모델을 활용하는 비중 파악 필요 | SCP NPUaaS 플랫폼의 하이퍼바이저 및 가상화 솔루션 호환 여부 검증
- source_ids: S026, S028, S031, S032, S033
- source_urls: https://www.e-science.co.kr/news/articleView.html?idxno=130004 | https://www.ddaily.co.kr/page/view/2026052017342600376 | https://www.ddaily.co.kr/page/view/2026052509101133595 | https://www.mt.co.kr/tech/2026/05/23/2026052210211399740 | https://www.thepowernews.co.kr/view.php?ud=202605221116568858de3f0aa1be_7

### 2. 엘리스그룹

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `CSP 운영 기업`
- 분류: `priority_outreach`
- 확인된 프로젝트/시그널: 코스닥 상장예비심사 청구 및 이동식 모듈형 데이터 센터(AI PMDC) 자원 확장
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 자체 AI 인프라 솔루션인 PMDC 및 인프라 서비스 ECI를 직접 제조/운영하고 있으며 상장 예심 청구를 기점으로 대규모 인프라 다각화를 꾀하는 만큼, 모델 정보 미확인 상태에서도 높은 인프라 채널 시너지를 기대할 수 있습니다.
- hook_type: `CLOUD`
- 핵심 buying signal: 상장예비심사 청구를 시작으로 국내 및 글로벌 시장 선점을 고도화하고 있으며, 자체적인 이동식 모듈형 데이터센터(AI PMDC) 인프라 비용 절감과 전력 효율 확보가 필요한 시점입니다.
- 인프라 signal: 이동식 모듈형 데이터 센터(AI PMDC) 및 컨테이너 가상화 인프라인 ECI 환경을 구축하고 있으며 대규모 GPUaaS 자원을 관리하고 있습니다.
- timing reason: 코스닥 상장 절차 착수에 따른 자금 유입과 국내외 비즈니스 영토 확장 타이밍이 맞물려 있어, 차별화된 고성능 저비용 NPU 인프라 라인업을 파트너 포트폴리오로 조기 편입시키기에 적절한 시기입니다.
- 고객 win: 엘리스그룹의 ECI 및 PMDC 인프라 솔루션 내부의 운영 전력량과 비용 부담을 대폭 경감시킬 수 있으며, 자사 GPUaaS 고객들에게 경쟁력 있는 요금제의 추론 전용 옵션을 신규 제공할 수 있습니다.
- FuriosaAI win: 국내 교육 및 엔터프라이즈 AI 클라우드 영역에서 급성장하는 파트너의 인프라 내에 하드웨어 레벨로 내장되어 고정 매출을 확보하고 글로벌 동반 진출 교두보를 마련할 수 있습니다.
- 직접 판매 가능성: `MID`
- CSP 경유 판매 가능성: `HIGH`
- NPUaaS 유도 가능성: `HIGH`
- CSP capacity 증설 가능성: `MID`
- 수치 근거: 없음
- 컨택 명분: 모듈형 데이터센터 및 ECI 인프라 고도화와 GPUaaS 요금 경쟁력 제고를 위한 하이브리드 NPU 연동 방안 제안 목적입니다.
- 실제 컨택 시 사용할 말: 최근 IPO 예비심사 청구와 AI 클라우드 부문 확장 소식을 기쁘게 접하였습니다. 엘리스의 AI PMDC 및 ECI 플랫폼 아키텍처에 컨테이너 환경 호환성이 검증된 RNGD를 통합 적용하여 인프라 전력 사용량을 개선하고 비용을 최적화하는 방안을 제안드리고 싶습니다.
- 매출 가능 시점: `단기`
- 담당자 후보 힌트: CTO, 클라우드인프라본부장, 인프라개발팀장, 하드웨어 플랫폼 아키텍트
- 공개 프로필 URL: 
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 엘리스 PMDC에 사용되는 서버 하우징 규격 및 PCIe 슬롯 가용성 조사 | ECI 내 컨테이너 오케스트레이션 환경에서 Furiosa Kubernetes Toolkit 적용 여부 확인
- source_ids: S034, S035, S036, S037
- source_urls: http://www.joseilbo.com/news/news_read.php?uid=568639&class=53&grp= | https://www.fetv.co.kr/news/articleView.html?idxno=302765 | https://www.the-stock.kr/news/articleView.html?idxno=32570 | https://www.newspim.com/news/view/20260520000146

### 3. KB금융그룹

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `온프레미스 기업`
- 분류: `structure_check`
- 확인된 프로젝트/시그널: 예방형 사이버보안 체계 구축 및 정보보호 실태 점검 내 AI 에이전트 도입 추진
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `MID`
- RNGD fit_score: `MID`
- outreach priority: `MID`
- fit vs priority 설명: 사용 모델은 미확인이지만 망분리 완화 가이드라인에 부합하는 사내 보안용 온프레미스/프라이빗 AI 시스템 구축 니즈가 명확하여, 하드웨어 보안 주권 관점에서의 접촉 명분이 충분합니다.
- hook_type: `SOVEREIGN`
- 핵심 buying signal: 금융위의 금융권 망분리 완화 가이드라인에 맞추어 보안 강화를 목적으로 한 내부 AI 에이전트 및 악성메일 대응 피싱 시나리오 자동화 시스템 도입을 본격 가속화하고 있습니다.
- 인프라 signal: 망분리 및 MFA 다중인증, 접근통제 체계를 유지하는 폐쇄망 중심의 사내 인프라 환경을 가동 중입니다.
- timing reason: 보안용 목적에 한해 망분리 규제가 선제 완화되면서 연내 정보보호 시스템에 AI 기술을 우선 도입하는 로드맵이 설정되어 즉각적인 아키텍처 제안 기회가 존재합니다.
- 고객 win: 사내 내부망의 극도로 안전한 폐쇄형 온프레미스 환경 하에서 외부 통신 없이도 보안성 높고 지연 시간이 짧은 생성형 AI 에이전트를 저전력으로 구동할 수 있습니다.
- FuriosaAI win: 금융권 망분리 규제 완화의 첫 상징적 레퍼런스로서 타 제1금융권 및 대형 증권사로의 온프레미스 프라이빗 패키지 수평 확장을 도모할 수 있습니다.
- 직접 판매 가능성: `MID`
- CSP 경유 판매 가능성: `HIGH`
- NPUaaS 유도 가능성: `LOW`
- CSP capacity 증설 가능성: `LOW`
- 수치 근거: 없음
- 컨택 명분: 망분리 규제 완화에 따른 내부 정보보안 시스템 내 온프레미스 추론 서버 인프라 제안 목적입니다.
- 실제 컨택 시 사용할 말: 최근 망분리 완화 가이드를 반영한 KB금융그룹의 AI 기반 사이버 보안 체계 구축 발표를 인상 깊게 보았습니다. 외부 인터넷 접속이 제한된 사내 보안망 안에서도 vLLM 컴패티블 환경을 통해 대형 모델을 보안 유출 없이 저비용 고성능으로 서비스할 수 있는 온프레미스 최적 가속기 RNGD에 대해 검토를 제안드립니다.
- 매출 가능 시점: `중기`
- 담당자 후보 힌트: CISO, 그룹정보보호부장, IT기획부장, 보안AI 아키텍처 실무 파트장
- 공개 프로필 URL: 
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 보안 에이전트 서비스 및 악성메일 피싱 생성 솔루션 내 탑재 예정인 경량 LLM(SMM) 규격 파악 | 자체 구축 예정인지 혹은 SI 파트너(예: 삼성SDS, KB데이타시스템 등)를 경유하는지 구조 파악 필요
- source_ids: S001, S006, S008, S009, S010
- source_urls: https://www.gosiweek.com/article/1065608272873992 | https://biz.heraldcorp.com/article/10755783?ref=naver | https://www.straightnews.co.kr/news/articleView.html?idxno=303329 | https://www.seoultimes.news/news/article.html?no=2000095985 | https://www.ziksir.com/news/articleView.html?idxno=134842

### 4. 시스트란

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `온프레미스 기업`
- 분류: `structure_check`
- 확인된 프로젝트/시그널: 'AI EXPO Korea 2026'서 폐쇄망 맞춤형 온프레미스 AI 솔루션 4종 공개
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `MID`
- RNGD fit_score: `MID`
- outreach priority: `MID`
- fit vs priority 설명: 사용하는 구체적인 프라이빗 모델은 미공개 상태이나, 기업 내부 독립 온프레미스 폐쇄망 공급을 위해 자사 패키지에 특화 가속기를 탑재/번들링할 수 있는 잠재적 파트너 파이프라인으로 적합합니다.
- hook_type: `PARTNER`
- 핵심 buying signal: 사내 정보 유출 우려를 해소하는 폐쇄망 독립형 AI 솔루션에 특화하여 AI 엑스포 등지에서 온프레미스 맞춤 포트폴리오를 대대적으로 홍보하고 있습니다.
- 인프라 signal: 외부 클라우드 연결이 완벽히 차단된 순수 내부 온프레미스 환경에 단독 배포 가능한 소프트웨어 패키징 방식을 지원합니다.
- timing reason: 최근 온프레미스 폐쇄망 기반 4종 맞춤형 솔루션을 정식 출시 및 마케팅하는 타이밍으로 하드웨어 번들 협의를 전개하기에 우호적인 여건입니다.
- 고객 win: 고객사 구축 시 GPU 서버 공급 단가 상승으로 인한 제안 경쟁력 저하 문제를 가성비와 전력비 우위의 RNGD 연동을 통해 해결할 수 있습니다.
- FuriosaAI win: 폐쇄망 엔터프라이즈 AI 번역 및 문서 처리 시장의 선도적 패키지 소프트웨어사와의 연동을 기반으로 다수의 소규모 프라이빗 AI 수주 레퍼런스를 확보할 수 있습니다.
- 직접 판매 가능성: `LOW`
- CSP 경유 판매 가능성: `LOW`
- NPUaaS 유도 가능성: `LOW`
- CSP capacity 증설 가능성: `LOW`
- 수치 근거: 없음
- 컨택 명분: 프라이빗 폐쇄망 AI 솔루션의 고성능 저비용 제안을 위한 하드웨어 연동 및 파트너십 구축 목적입니다.
- 실제 컨택 시 사용할 말: 최근 AI 엑스포에서 공개하신 폐쇄망 맞춤형 온프레미스 AI 제품군을 매우 인상 깊게 보았습니다. 기업 보안을 확보하면서 연산 효율을 높여야 하는 시스트란의 고객사들에게 뛰어난 전력 효율의 RNGD가 탑재된 온프레미스 서버 패키지를 공동 제안하여 윈윈 구조를 만들고 싶습니다.
- 매출 가능 시점: `중기`
- 담당자 후보 힌트: CTO, 솔루션연구소장, 비즈니스개발(BD) 부서장
- 공개 프로필 URL: 
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 시스트란 온프레미스 시스템의 주요 기반 LLM 아키텍처(Llama 기반 여부 등) 기술 규격 확인 | 번들 판매를 위한 가속기 탑재 전용 어플라이언스 기획 가능성 검토
- source_ids: S002
- source_urls: https://www.etnews.com/20260522000276

### 5. 오픈네트웍시스템

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `CSP 고객 기업`
- 분류: `structure_check`
- 확인된 프로젝트/시그널: Dify 운영사 랭지니어스 국내 독점 공식 계약 체결 및 에이전트 플랫폼 구축 상담 확대
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `MID`
- 채널/CSP fit_score: `MID`
- RNGD fit_score: `MID`
- outreach priority: `MID`
- fit vs priority 설명: 자체 생성 모델보다는 LLM 게이트웨이 및 에이전틱 프레임워크인 Dify의 연동에 특화되어 있어 특정 단일 모델 적합도는 UNKNOWN이지만, 고성능 멀티 모델 서빙 허브 인프라 구축 수요를 견인하는 역할로 유효합니다.
- hook_type: `VLLM`
- 핵심 buying signal: Dify 기반 AI 에이전트 서비스, 스마트 브로슈어 OCR 및 자연어 기반 SQL 데이터 조회 등 다채로운 상담 사례를 구축하며 엔터프라이즈 에이전트 엔진 수요를 확대하고 있습니다.
- 인프라 signal: 다중 LLM 서빙 환경 및 멀티모델 추론 백엔드 오케스트레이션 설계를 다루고 있습니다.
- timing reason: AI 엑스포 참가 후 다수 기업 고객들을 상대로 구체적인 에이전틱 플랫폼 구축 및 클라우드/온프레미스 인프라 하이브리드 제안 영업을 구체화하는 국면입니다.
- 고객 win: 고객사들이 Dify 인프라를 백엔드에서 지탱하는 추론 비용을 극적으로 줄이면서 대량의 API 호출 및 토큰 처리를 원활히 관리하도록 도움을 줍니다.
- FuriosaAI win: Dify 프레임워크와 vLLM/RNGD 백엔드 통합 레퍼런스를 개척하여, 에이전트 플랫폼 단위로 NPU 인프라가 표준 통합되는 대형 GTM 고리를 확보할 수 있습니다.
- 직접 판매 가능성: `LOW`
- CSP 경유 판매 가능성: `MID`
- NPUaaS 유도 가능성: `HIGH`
- CSP capacity 증설 가능성: `LOW`
- 수치 근거: 없음
- 컨택 명분: Dify 프라이빗 에이전틱 플랫폼의 온프레미스/클라우드 추론 백엔드 고효율 최적화 공동 영업 제의 목적입니다.
- 실제 컨택 시 사용할 말: Dify 운영사인 랭지니어스와의 공식 파트너십 및 에이전틱 워크플로우 기술 지원 사례를 높이 평가합니다. Dify 기반의 기업용 프라이빗 서비스 시 추론 백엔드의 리소스를 대폭 경감하고 API 처리량을 늘려주는 RNGD-vLLM 통합 서빙 플랫폼 구성에 대해 논의를 희망합니다.
- 매출 가능 시점: `중기`
- 담당자 후보 힌트: 솔루션개발본부장, 기술영업총괄, AI 비즈니스본부장
- 공개 프로필 URL: 
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: Dify 백엔드 오케스트레이션 엔진 내 vLLM / OpenAI API 규격 완벽 대응 여부 확인 | 실무 PoC 고객군 중 특정 CSP 클라우드를 가호스팅 영역으로 사용하는지 조사
- source_ids: S020, S021, S023
- source_urls: https://www.joongang.co.kr/article/25430014 | https://www.gokorea.kr/news/articleView.html?idxno=866999 | https://www.sentv.co.kr/article/view/sentv202605190084

### 6. 서울아산병원

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `온프레미스 기업`
- 분류: `watchlist`
- 확인된 프로젝트/시그널: 응급환자 프로토콜 지원 폐쇄망 내부 온프레미스 AI 시스템 성공적 실증
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `LOW`
- RNGD fit_score: `MID`
- outreach priority: `MID`
- fit vs priority 설명: 사용 모델 정보는 미확인이지만 환자 정보 보안을 극대화하기 위해 폐쇄망 하드웨어 인프라를 지향하는 확실한 도메인 신호가 존재하여 향후 하드웨어 수급 제안 대상군으로 적합합니다.
- hook_type: `SOVEREIGN`
- 핵심 buying signal: 디지털정보혁신본부의 주도 하에 환자 민감 정보 보호를 위해 외부 클라우드가 차단된 온프레미스 폐쇄망 환경에서 정상 작동하는 응급 프로토콜 AI 시스템을 성공적으로 실증 완료했습니다.
- 인프라 signal: 원내에 폐쇄형 GPU 인프라 혹은 보안 온프레미스 서버 인프라를 직접 구동 중입니다.
- timing reason: 원내 응급실 등 실전 배치와 의료 데이터 활용 인프라 고도화 계획이 구체화되는 현 시점에 적격 제안 타이밍입니다.
- 고객 win: 외부 클라우드로의 의료 데이터 유출 리스크를 원천 차단하면서, 온프레미스 랙 내에서 환자 생명과 연관된 의료 대용량 임상 매뉴얼 데이터 추론 속도를 높이고 서버실 전력 비용을 줄일 수 있습니다.
- FuriosaAI win: 보수적인 대형 병원 도메인에서 폐쇄형 온프레미스 의료 AI 구동용 인프라 표준 레퍼런스를 확보하여 타 주요 대학병원으로 확산할 기반을 마련합니다.
- 직접 판매 가능성: `MID`
- CSP 경유 판매 가능성: `LOW`
- NPUaaS 유도 가능성: `LOW`
- CSP capacity 증설 가능성: `LOW`
- 수치 근거: 없음
- 컨택 명분: 보안망 내 고성능 저지연 응급 의료 LLM 실무 운영을 위한 온프레미스 가속기 공급 제안 목적입니다.
- 실제 컨택 시 사용할 말: 최근 폐쇄망 환경에서 응급환자 프로토콜 AI 시스템을 완벽히 구축해내신 행보를 전해 들었습니다. 민감 정보 처리를 위한 내부 서버실의 전력 부담과 랙 상면 문제를 획기적으로 낮추면서도 의료진의 다중 동시 추론 질의를 지연 없이 처리해내는 국산 추론 칩 RNGD 도입 방안을 제안드리고자 합니다.
- 매출 가능 시점: `장기`
- 담당자 후보 힌트: 디지털정보혁신본부장, 의료정보센터 파트장, 전산정보팀 인프라 담당 임원
- 공개 프로필 URL: 
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 병원 원내 전산실 서버 랙 전력 한계치 및 추가 확장 한계 검증 | 응급환자 프로토콜 솔루션 자체에 적용된 소형 특화 모델 아키텍처 정보 확인 필요
- source_ids: S012
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

1. **부산시·네이버클라우드, 스타트업 AI 실무교육 추진 - 네이트**
   - source: `rss`
   - published_at_kst: `2026-05-26T10:19:00+09:00`
   - matched_query_or_feed: `Google News KR 생성형 AI`
   - url: https://news.google.com/rss/articles/CBMiYEFVX3lxTFBrbV81MmVrNXhkVkJGbDZnSFZtd2RhZXBjZTRTVUI2b1pVVm5wd25UTnYyZ2ZPcWR2bU1VSnJHRTE1MWVxU3NTVzNQRnEzYjAxbnlWd2FkdHF6b3R1dGRLNQ?oc=5
   - summary_snippet: 부산시·네이버클라우드, 스타트업 AI 실무교육 추진  네이트

2. **아리바이오, 경구용 치매약 기술수출 계약금 150억 수령**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T10:16:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: http://www.hansbiz.co.kr/news/articleView.html?idxno=840690
   - summary_snippet: 한편 아리바이오는 코스닥 상장사 소룩스와의 합병도 추진 중이다. 회사는 향후 인공지능(AI)과 데이터센터, 바이오를 연계한 미래 융합 플랫폼 기업으로 사업 영역을 확대해 나간다는 전략이다.

3. **글로벌 사모펀드들, 中 데이터센터 시장 철수 막바지**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T10:14:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: http://www.fnnews.com/news/202605260937364544
   - summary_snippet: 여기에 인공지능(AI) 수요 급증으로 자산 가치가 높아지면서 외국 자본 입장에서는 중국 내 매수자에게 매각하고 자금을 재배치할 적기가 됐다는 평가다. 베인캐피털은 지난해 중국 데이터센터 자산을 선전 둥양광...

4. **구덕본 DU난임대응센터장, “난임센터는 단순 치료 지원 아닌 연구·교육...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T10:14:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.kbmaeil.com/article/20260525500476
   - summary_snippet: 구 센터장은 “일반적인 AI 서비스가 아닌, 실제 난임 데이터를 기반으로 개인 상태에 맞는 정보를 제공하는 시스템을 구축하는 것이 목표”라며 “경북도와 협력해 우선 지역 난임 인구를 대상으로 서비스를 추진하고...

5. **아리바이오, 푸싱제약 기술수출 선급금 1000만 달러 실수령**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T10:14:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.pharmnews.com/news/articleView.html?idxno=303748
   - summary_snippet: 한편 아리바이오는 코스닥 상장사 소룩스와의 합병을 추진 중이며, 향후 인공지능(AI), 데이터센터, 바이오를 연결하는 융합 플랫폼 기업으로 사업을 확장할 계획이다.

6. **[단독] 한미반도체, HBF용 TC본더 만든다**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T10:14:00+09:00`
   - matched_query_or_feed: `AI inference`
   - url: https://news.mtn.co.kr/news-detail/2026052608515364392
   - summary_snippet: 26일 반도체 업계에 따르면 한미반도체는 최근 AI 추론(Inference)용 차세대 메모리로 주목받는 HBF 전용 TC본더를 개발, 하반기 초도 물량 출하를 계획 중이다. 업계에선 사실상 글로벌 낸드 업체의 HBF 양산 로드맵에...

7. **잇피, 의료 AI 바우처 사업 선정…서울아산·삼성서울병원과 임상 데이...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T10:14:00+09:00`
   - matched_query_or_feed: `병원 AI 플랫폼`
   - url: https://www.biotimes.co.kr/news/articleView.html?idxno=31963
   - summary_snippet: 서울바이오허브 입주기업인 잇피가 보건복지부 의료 AI 데이터 활용 사업에 선정되며 근골격계 의료 AI 플랫폼 고도화에 속도를 낸다. 국내 주요 상급종합병원들과의 다기관 임상 데이터 구축을 통해 실제 진료 현장에서...

8. **KB금융, 사이버 보안위협에 'AI 대 AI' 방어체계 대응**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T10:14:00+09:00`
   - matched_query_or_feed: `클라우드 AI 서비스`
   - url: https://www.newsfreezone.co.kr/news/articleView.html?idxno=691533
   - summary_snippet: 특히 그룹 클라우드 환경에 대한 제로트러스트 3단계 구축 완료 사례는 금융업권에서 선제적인 구축 사례로 평가받는다. 아울러 지난해 3월 수립한 AI 거버넌스를 바탕으로 AI 서비스 수명주기 전 단계에서 31개 위험...

9. **"AI는 AI로 막는다"…KB금융, 사이버보안 '운영체계' 다시 짰다**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T10:14:00+09:00`
   - matched_query_or_feed: `클라우드 AI 서비스`
   - url: https://www.the-pr.co.kr/news/articleView.html?idxno=61422
   - summary_snippet: 특히 클라우드 환경에 대한 제로트러스트 3단계 구축을 완료하며 선제적 대응 사례를 마련했다. AI 리스크... KB금융은 AI 거버넌스를 기반으로 서비스 전 단계에서 31개 위험 항목을 통제하고 있으며, 자체 화이트해커와...

10. **[서울데이터랩]개장 직후 인기 검색 종목 20選**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T10:13:00+09:00`
   - matched_query_or_feed: `금융 생성형 AI`
   - url: https://www.seoul.co.kr/news/economy/securities/2026/05/26/20260526500052?wlog_tag3=naver
   - summary_snippet: 26일 오전 9시 5분 기준 네이버 금융 검색 상위 종목은 반도체 대형주와 자동차, 건설, 2차전지... 그리고 건설주로 집중되는 모습이다. [서울신문과 MetaVX의 생성형 AI가 함께 작성한 기사입니다]

11. **한컴위드, AI 기반 지속 인증 '한컴 엑스씨오스' 출시**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T10:12:00+09:00`
   - matched_query_or_feed: `망분리 AI`
   - url: https://www.pointe.co.kr/news/articleView.html?idxno=79859
   - summary_snippet: 정부가 지난 10월 발표한 '범부처 정보보호 종합대책'은 기존의 물리적 망분리 정책을 데이터 중요도 중심으로 전환하고, 다중 인증과 AI 기반 이상 탐지 시스템을 도입하는 것이 골자다. '한컴 엑스씨오스'는 이러한...

12. **SK하이닉스, 발열 잡는 차세대 'iHBM' 기술 공개**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T10:10:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: http://www.queen.co.kr/news/articleView.html?idxno=457476
   - summary_snippet: SK하이닉스는 iHBM 기술을 HBM5 등 차세대 제품부터 적용해 고성능 컴퓨팅(HPC), AI 데이터센터 등 초고집적·초고대역폭 환경에서 요구되는 열 관리 수준을 충족할 계획이다. 이강욱 SK하이닉스 부사장은 "iHBM은...

13. **HBM 발열 대응 경쟁 본격화…SK하이닉스, 냉각 일체형 패키지 공개**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T10:10:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.ngetnews.com/news/articleView.html?idxno=550467
   - summary_snippet: SK하이닉스는 해당 기술을 HBM5 등 차세대 제품에 적용해 고성능 컴퓨팅과 AI 데이터센터 환경에서 요구되는 열 관리 수준을 충족할 계획이다. 이를 통해 시스템 안정성과 운영 효율을 동시에 끌어올린다는...

14. **통신업계, AX 가속화···AI 기반 사내 챌린지·인재 육성 지원**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T10:10:00+09:00`
   - matched_query_or_feed: `클라우드 AI 서비스`
   - url: http://www.wsobi.com/news/articleView.html?idxno=312443
   - summary_snippet: 완성된 서비스를 시연하고 발표했다. 최종 결선에서는 △A.X K1 기반 오토 품질 관리 시스템 '오토파일럿... 기존 시스템ㆍ네트워크 중심의 보안을 넘어 AI, 클라우드, 통신 인프라, 개인정보보호, 보안 거버넌스까지...

15. **B&R코리아, 'Innovation Day 2026' 성료…“적응형 자동화가 경쟁력 좌우...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T10:09:00+09:00`
   - matched_query_or_feed: `제조 AI 플랫폼`
   - url: https://www.etnews.com/20260526000095
   - summary_snippet: 있다”며 “AI·데이터·모듈형 자동화를 결합한 적응형 제조가 지속가능한 제조 혁신의 핵심”이라고... 발표 행사가 아니라 한국 제조 생태계 전체의 변화를 논의하는 플랫폼으로 발전시켜 나갈 것”이라고 밝혔다.

16. **SK하이닉스, 차세대 HBM 발열 해법…‘iHBM’ 기술 공개**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T10:08:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.mydaily.co.kr/page/view/2026052610070391879
   - summary_snippet: SK하이닉스는 이 기술을 HBM5 등 차세대 제품부터 적용해 고성능 컴퓨팅(HPC)과 AI 데이터센터 등 초고집적·초고대역폭 환경에서 요구되는 열 관리 수준을 충족시킨다는 계획이다. 이강욱 SK하이닉스 부사장(PKG개발...

17. **GPU 수천개 연결하려면…답은 광섬유…AI 인프라 판 바뀐다**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T10:08:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.digitaltoday.co.kr/news/articleView.html?idxno=668877
   - summary_snippet: AI 데이터센터 확산으로 광섬유가 단순 배선 자재를 넘어 핵심 인프라로 부상하고 있다. [사진: 셔터스톡] 인공지능(AI) 데이터센터 확산으로 광섬유가 단순 배선 자재를 넘어 핵심 인프라로 부상하고 있다. 25일...

18. **SK하이닉스, 발열 잡는 메모리 솔루션 ‘iHBM’ 기술 공개**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T10:08:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://economist.co.kr/article/view/ecn202605260016
   - summary_snippet: SK하이닉스는 iHBM 기술을 HBM5 등 차세대 제품부터 적용해 고성능 컴퓨팅(HPC), AI 데이터센터 등 초고집적·초고대역폭 환경에서 요구되는 열 관리 수준을 충족하며 시스템 전반의 안정성과 운영 효율을...

19. **한컴위드, AI 기반 지속 인증 솔루션 '한컴 엑스씨오스' 출시**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T10:08:00+09:00`
   - matched_query_or_feed: `망분리 AI`
   - url: https://www.nextdaily.co.kr/news/articleView.html?idxno=249727
   - summary_snippet: 정부는 지난해 10월 '범부처 정보보호 종합대책'을 발표하며 기존 물리적 망분리 정책을 데이터 중요도 중심으로 전환하고, 설치형 보안 소프트웨어 대신 다중 인증과 AI 기반 이상 탐지 시스템 도입으로 보안 실효성을...

20. **GPU 수천개 연결하려면…답은 광섬유…AI 인프라 판 바뀐다 - 네이트**
   - source: `rss`
   - published_at_kst: `2026-05-26T10:08:00+09:00`
   - matched_query_or_feed: `Google News KR AI 데이터센터`
   - url: https://news.google.com/rss/articles/CBMiU0FVX3lxTE4tbGFxRnVYd1dmZHloU3BfcnN3b2tob0Q5NXhfWEc3SXA1ME9LM0hBOHRESGlvRm5UeEU2NHhVTmZIMVh5QjhxQndkWWdSWlBpdm9n?oc=5
   - summary_snippet: GPU 수천개 연결하려면…답은 광섬유…AI 인프라 판 바뀐다  네이트


## 다음 단계

1. LLM 후보 품질 확인
2. 노이즈가 많으면 NAVER_QUERIES / RSS_FEEDS 개선
3. 후보가 너무 적으면 MAX_LLM_SOURCES 상향
4. Gemini 3.5 Flash vs 2.5 Flash 품질 비교
5. 나라장터/B2G 수집 추가
6. 담당자/의사결정자 탐색 추가
7. Notion 또는 Google Docs 업로드 추가
