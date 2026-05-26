# FuriosaAI GTM Research Agent Test Run

## 실행 정보

- run_id: `2026-05-26_092440_test_decision-maker-gate-fix`
- mode: `test`
- memo: `decision-maker-gate-fix`
- executed_at_kst: `2026-05-26T09:30:48.927140+09:00`
- agent_version: `v0.7`
- instructions_loaded_chars: `21592`
- naver_sources_recent_7d_count: `190`
- rss_sources_recent_7d_count: `223`
- merged_sources_recent_7d_count: `413`
- furiosa_docs_successful: `11`
- furiosa_docs_failed: `0`
- llm_called: `True`
- llm_error: ``

## 현재 단계

이 실행은 v0.7 테스트입니다.

이번 버전에서는 네이버 뉴스 API, RSS feed, FuriosaAI 공개 개발자 문서를 수집한 뒤 Gemini로 GTM 후보를 1차 평가하고, 별도 LLM 호출로 매니저용 gtm_report.md를 작성합니다.

아직 나라장터 직접 API, 담당자 심화 탐색, Notion 업로드는 수행하지 않았습니다.

## LLM 실행 요약

- overall_assessment: 금융권 및 대형 의료기관의 완전 폐쇄망 프라이빗 생성형 AI 도입 및 대형 CSP사들의 전력/데이터센터 확충 국면이 본격화됨에 따라 온프레미스 주권 AI 요구와 NPUaaS 플랫폼의 필요성이 결합되는 강력한 GTM 시그널이 확인됩니다.
- top_priority_names: 삼성SDS, 엘리스그룹, 서울아산병원
- noise_ratio_comment: 단순 지자체 AI 실무 교육용 홍보 자료나 중고 거래 앱 민원성 챗봇 기사를 제외한 핵심 인프라 증설 및 조달 파트너 발굴 성공 비중이 매우 높아 실질적 영업 기회 발굴에 용이한 양상을 보입니다.
- model_compatibility_caution: 본 리서치에서 확인된 인프라 수요 기업들의 활용 모델 세부 버전이 대다수 기재되지 않았으므로, 영업 진행 시 해당 파이프라인의 핵심 사용 모델 구조(Llama, Qwen2.5, Qwen3 등)에 대한 정합 확인을 최우선적으로 선행해야 합니다.

## LLM 후보 평가 결과

## 버전 1 — B2B only 우선 검토 요약

- 삼성SDS / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `중기`
- 엘리스그룹 / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- 서울아산병원 / 온프레미스 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `중기`
- KB금융그룹 / 온프레미스 기업 / classification: `structure_check` / fit: `MID` / outreach: `MID` / 매출시점: `장기`
- 오픈네트웍시스템 / CSP 운영 기업 / classification: `cloud_npuaaS_lead` / fit: `MID` / outreach: `HIGH` / 매출시점: `중기`


## 버전 2 — B2B + B2G 우선 검토 요약

- 삼성SDS / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `중기`
- 엘리스그룹 / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- 서울아산병원 / 온프레미스 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `중기`
- KB금융그룹 / 온프레미스 기업 / classification: `structure_check` / fit: `MID` / outreach: `MID` / 매출시점: `장기`
- 오픈네트웍시스템 / CSP 운영 기업 / classification: `cloud_npuaaS_lead` / fit: `MID` / outreach: `HIGH` / 매출시점: `중기`


## 상세 후보 평가

### 1. 삼성SDS

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `CSP 운영 기업`
- 분류: `priority_outreach`
- 확인된 프로젝트/시그널: 구미 AI 데이터센터 신축 및 동탄 데이터센터 서관 가동용 전력 확보 등을 필두로 한 대규모 AI 인프라 증설 추진
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 사용 모델은 불명확한 단계로 모델 적합성은 UNKNOWN이나, 구미 60MW AI 데이터센터 신축 및 동탄 20MW 전력 확보 등 데이터센터 전력 고밀도 인프라 확장 움직임이 강해 SCP 기반의 NPUaaS 비즈니스 및 CSP 경유 영업 기회가 강력하므로 우선순위를 HIGH로 책정하였습니다.
- hook_type: `CLOUD`
- 핵심 buying signal: 수도권 전력 밀도 포화에 대응하여 동탄 데이터센터 가동을 위해 20MW 전력을 조달하고, 경북 구미에 4273억원을 투자하여 60MW 규모의 대규모 AI 데이터센터 건립을 확정하였습니다.
- 인프라 signal: 동탄 서관 가동 및 구미 AI 데이터센터 설비 투자로 대량의 GPUaaS 인프라 확장 및 이종 NPUaaS 전개 여력을 구축 중입니다.
- timing reason: 국내 주요 CSP 연합체가 결성되어 글로벌 전력 소모 및 고가 장비 수급난 극복 방안을 공동 모색하는 에너지 효율 중점 시점입니다.
- 고객 win: 대규모 고밀도 데이터센터 운영 시 치명적인 발열 완화와 고전력 장치 랙 밀도 제약 상황을 국산 저전력 가속기로 해결할 수 있습니다. 자체 클라우드인 SCP의 가성비 NPU 가상화 라인업을 확보해 차별화된 가격 경쟁력 확보가 가능합니다.
- FuriosaAI win: RNGD의 검증된 대용량 인프라 구축 검증 기회를 확보하여 국내 엔터프라이즈 SCP 유입 기업들의 잠재적 가속 장치 유통망을 일거에 공략할 수 있습니다.
- 직접 판매 가능성: `MID`
- CSP 경유 판매 가능성: `HIGH`
- NPUaaS 유도 가능성: `HIGH`
- CSP capacity 증설 가능성: `HIGH`
- 수치 근거: 4273억원 (S031) — 근거: 삼성SDS는 경북 구미에 4273억원을 투자해 60MW 규모 AI 데이터센터를 짓기로 했다. | 60MW (S031) — 근거: 삼성SDS는 경북 구미에 4273억원을 투자해 60MW 규모 AI 데이터센터를 짓기로 했다. | 20MW (S025) — 근거: 삼성SDS가 경기 동탄 데이터센터 서관 가동을 위해 20MW급 전력을 확보한 사례
- 컨택 명분: 전력 포화 대응 목적 신축 구미 AI 데이터센터 전력 부하 관리 및 동탄 전개형 고효율 가속 장비 도입 제안
- 실제 컨택 시 사용할 말: 최근 동탄 데이터센터 가동을 위한 20MW 전력 취득 및 구미 4273억원 규모의 60MW 데이터센터 투자 결정을 인상 깊게 읽었습니다. 초대형 데이터센터 전력 수급 및 공랭식 한계를 극복하는 전력 대비 가속률이 극대화된 RNGD 솔루션을 도입하여 가용 상용 랙 효율을 최대치로 개선할 방향을 검토해 보실 수 있습니다.
- 매출 가능 시점: `중기`
- 담당자 후보 힌트: CTO, Head of Cloud 또는 Head of Infrastructure
- 공개 프로필 URL: 
- 기존 접점: `삼성SDS ✅`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 신축 구미 및 동탄 데이터센터 가상 가용 전력 내 RNGD 랙 수용 한계량 산출 필요 | SCP의 컨테이너 기반 쿠버네티스 서빙 및 S-Hypervisor 환경의 가상 장치 제어 드라이버 호환 체계 체크
- source_ids: S025, S031, S032
- source_urls: https://www.e-science.co.kr/news/articleView.html?idxno=130004 | https://www.mt.co.kr/tech/2026/05/23/2026052210211399740 | https://www.thepowernews.co.kr/view.php?ud=202605221116568858de3f0aa1be_7

### 2. 엘리스그룹

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `CSP 운영 기업`
- 분류: `priority_outreach`
- 확인된 프로젝트/시그널: 코스닥 상장예비심사 청구를 바탕으로 자체 전용 클라우드 인프라인 PMDC 및 GPUaaS의 대규모 확충 자금 조달 개시
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 사용 모델 사양이 명기되지 않아 model_fit_score는 UNKNOWN으로 한정되나, 자체 AI 컨테이너 데이터센터 및 실사용 GPUaaS 인프라 확장을 상장 조달 자금으로 공격적으로 추진하고 있어 RNGD 기반 가성비 가속 기지 구축 파트너십 가치가 크므로 우선순위 HIGH를 배정했습니다.
- hook_type: `CLOUD`
- 핵심 buying signal: 상장 공모 자금을 토대로 한 전력 절감형 특수 인프라 확장 및 클라우드 중심의 AX 솔루션 자본 장치 구축이 최우선 목표로 대두되었습니다.
- 인프라 signal: 자체 특허 구조인 소형 이동식 모듈형 데이터센터(PMDC) 및 분산 GPU 클라우드 오케스트레이션 제어 기반을 갖추고 있습니다.
- timing reason: 실적 및 장비 경쟁력 강화 중심의 코스닥 예심 청구 시기로 단시간 내 성과 도출형 고효율 가속 설비 도입 논의가 먹히기 쉬운 환경입니다.
- 고객 win: 물리적 공간과 냉각이 정교하게 제한된 컨테이너 데이터센터 내부의 고밀도 연산 부하 제약을 RNGD의 저소음 고효율 가동성으로 즉시 격파할 수 있습니다. 상장 이후 대형 고객 유입 시 가용 원가 소모율을 가파르게 줄여 높은 이익률에 도달합니다.
- FuriosaAI win: 컨테이너 특화 인프라의 국산 실적을 얻는 것과 동시에, 상장 궤도에 진입한 대규모 GPUaaS/NPUaaS 가상 유통 허브를 장악할 수 있습니다.
- 직접 판매 가능성: `MID`
- CSP 경유 판매 가능성: `LOW`
- NPUaaS 유도 가능성: `HIGH`
- CSP capacity 증설 가능성: `HIGH`
- 수치 근거: 없음
- 컨택 명분: 모듈러 데이터센터 효율 향상 목적 고밀도 가속 연동 체계 제안
- 실제 컨택 시 사용할 말: 최근 코스닥 상장 예비심사 청구와 함께 고도화되는 모듈러 PMDC 및 GPUaaS 확장 행보를 응원하며 연락드렸습니다. 물리 공간 제한 극복 및 가상 인프라 전력 최적화에 탁월한 RNGD 추론 엔진을 연계 유기적으로 배포하여 설비 비용 효율을 제고하는 파트너십을 의논하고자 합니다.
- 매출 가능 시점: `단기`
- 담당자 후보 힌트: CTO 또는 Head of Infrastructure
- 공개 프로필 URL: 
- 기존 접점: `엘리스 ✅`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 엘리스그룹 독자 모듈형 구조물 인프라 환경 내부의 가용 전력 한계 확인 | ECI 플랫폼의 쿠버네티스 스케줄러와 RNGD 컨테이너 디렉터 연계 검토
- source_ids: S033, S034, S035, S036
- source_urls: http://www.hansbiz.co.kr/news/articleView.html?idxno=839792 | http://www.joseilbo.com/news/news_read.php?uid=568639&class=53&grp= | https://www.the-stock.kr/news/articleView.html?idxno=32570 | https://www.newspim.com/news/view/20260520000146

### 3. 서울아산병원

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `온프레미스 기업`
- 분류: `priority_outreach`
- 확인된 프로젝트/시그널: 외부망 차단 폐쇄 환경 내 의료진 전용 응급환자 프로토콜 실시간 대응 AI 시스템 정상 연동 검증
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `MID`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 사용 모델 사양이 공개되지 않아 model_fit_score는 UNKNOWN으로 조율되었으나, 인터넷이 완전히 유실된 상태에서도 구동이 필수적인 극도의 폐쇄망 프라이빗 AI 구현 실증을 최초 완료한 특수 의료기관인 만큼, 저소음 온프레미스 소버린 랙 인프라 납품 가치가 대단히 높아 우선순위 HIGH를 배정했습니다.
- hook_type: `SOVEREIGN`
- 핵심 buying signal: 보안성과 임상 긴급 상황 실시간 대응력 확보를 목적으로 폐쇄 내부망에 완전히 정합된 오프라인 지능형 의료 추론 환경 확충을 희망하고 있습니다.
- 인프라 signal: 원내 전산동 내부 소형 전산실 및 별도 완전 격리 전산 보안 클러스터를 사용하여 실내 구동이 보장되는 고효율 장비가 필요합니다.
- timing reason: 병원 최초의 생성형 AI 폐쇄 가동 안정성이 입증되어 타 분과 및 의료 프로세스 내부망 전면 확대를 의사결정하는 핵심 기조가 생성되었습니다.
- 고객 win: 진료 정보 및 환자 기밀 누출 우려를 원천 차단하면서도, 지연율을 극도로 줄인 즉각적 응급 구호 응답 환경을 항시 유지할 수 있습니다. 자체 전산 자원을 과다하게 잠식하는 무겁고 뜨거운 범용 칩을 배제하고 의료 전용 소형 시스템 전개가 가능해집니다.
- FuriosaAI win: 국내 상징적 의료 기관에 프라이빗 소버린 가속 장비를 단독 공급하여 병원 전문 폐쇄 연산 플랫폼의 표준 레퍼런스를 확보하게 됩니다.
- 직접 판매 가능성: `HIGH`
- CSP 경유 판매 가능성: `LOW`
- NPUaaS 유도 가능성: `LOW`
- CSP capacity 증설 가능성: `LOW`
- 수치 근거: 없음
- 컨택 명분: 원내 오프라인 폐쇄 의료 진단 에이전트 구동 효율 강화를 위한 온프레미스 가속 하드웨어 제안
- 실제 컨택 시 사용할 말: 최근 서울아산병원 디지털정보혁신본부의 오프라인 폐쇄 응급 AI 프로토콜 검증 성공 소식을 기쁘게 접했습니다. 병원 내부망에서의 고성능 대형 지능 엔진 유지를 위해 발열이 차단되고 높은 데이터 주권을 제공하는 온프레미스 전용 RNGD 연동 가능성을 논의해 보고자 제안 드립니다.
- 매출 가능 시점: `중기`
- 담당자 후보 힌트: CIO, CTO 또는 디지털정보혁신본부장
- 공개 프로필 URL: 
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 병원 원내 사용 중인 미세 조정 지능 알고리즘의 소형 프레임워크 규격 사양 | 자체 의료 장비 관리 기준 상의 전기/발열 및 연산 정합 적격 요건 확인
- source_ids: S010
- source_urls: https://www.newsis.com/view/NISX20260518_0003634573

### 4. KB금융그룹

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `온프레미스 기업`
- 분류: `structure_check`
- 확인된 프로젝트/시그널: 다중인증 및 차단망 통제를 보존하면서 사이버 보안 위협 대처용 훈련 에이전틱 구조 구축 추진
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `MID`
- RNGD fit_score: `MID`
- outreach priority: `MID`
- fit vs priority 설명: 내부 구동 모델 미확정 상태로 model_fit_score는 UNKNOWN이나, 금융권 특유의 보안망 고수와 연동된 다량의 에이전트 시뮬레이션 연산 수요가 포착되어 중기적 온프레미스 도입 타당성 파악을 위해 MID로 분류하였습니다.
- hook_type: `SOVEREIGN`
- 핵심 buying signal: 기본 통제 체계를 엄밀히 유지하는 한편 위협 메일 모사 등 수시 훈련 목적의 고품질 에이전트를 실내망에서 가동하려는 구체적 니즈가 표출되었습니다.
- 인프라 signal: 그룹 사이버보안센터 기지 내부 전용 온프레미스 망 및 사내 자체 구축형 AI 워크스테이션 인프라 추정 환경입니다.
- timing reason: 13년 만의 금융권 망분리 규제 완화 결정 소식과 동반하여 본 사내망 지능형 방어 체계의 다변화를 모색하기에 좋은 진입 명분이 확보되었습니다.
- 고객 win: 연속적인 수천 종의 악성 패턴 지능 자동 생성 시 수반되는 대형 하드웨어 수급 예산 절약과 완벽한 폐쇄망 요건 준수를 양립할 수 있습니다.
- FuriosaAI win: 금융 보안 관제 도메인의 선도적 레퍼런스를 확보해 보수적인 제1금융권 온프레미스 전개 속도를 획기적으로 향상합니다.
- 직접 판매 가능성: `HIGH`
- CSP 경유 판매 가능성: `MID`
- NPUaaS 유도 가능성: `MID`
- CSP capacity 증설 가능성: `LOW`
- 수치 근거: 없음
- 컨택 명분: 금융 격리망 내 AI 방어 에이전트 대규모 처리를 위한 오프라인 전용 인프라 전개 방안 점검
- 실제 컨택 시 사용할 말: 최근 그룹 사이버보안센터의 AI 기반 메일 차단 및 다중 모사 훈련 에이전트 연계 전략을 뜻깊게 읽었습니다. 금융권 소버린 보안 준칙을 보존하면서 최신 AI 에이전트 추론 가속 성능을 보완하는 국산 NPU RNGD의 물리 서버 연계 전개 방향에 대해 실무 협의를 희망합니다.
- 매출 가능 시점: `장기`
- 담당자 후보 힌트: CIO 또는 platform lead
- 공개 프로필 URL: 
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 악성메일 모의 자동 생성 에이전트가 활용하는 프레임워크 규격 분석
- source_ids: S005, S006
- source_urls: https://www.fetv.co.kr/news/articleView.html?idxno=303015 | http://www.efnews.co.kr/news/articleView.html?idxno=129934

### 5. 오픈네트웍시스템

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `CSP 운영 기업`
- 분류: `cloud_npuaaS_lead`
- 확인된 프로젝트/시그널: Dify 공식 라이선스 총판 파트너십 취득 후 공공 및 나라장터용 에이전트 플랫폼 대량 납품 및 DB 연동 스마트 브리핑 연계 개발
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 사용 모델 사양이 기재되지 않아 model_fit_score는 UNKNOWN이나, Dify를 기반으로 한 공공 조달 조준 대규모 지능 에이전트 통합 SI 사업을 이끌고 있어 고부하 추론 다중 호출을 효율적으로 지원할 국산 NPUaaS 가상 머신 유입 파트너 시너지가 뚜렷해 HIGH로 산출했습니다.
- hook_type: `VLLM`
- 핵심 buying signal: Dify 플랫폼을 중심으로 공공 입찰 시장용 지능형 솔루션 기획 및 맞춤형 AI 상담 조달 연계 수주 상담을 활발히 유치하고 있습니다.
- 인프라 signal: 외부 클라우드 가상 인스턴스 또는 호스팅 클러스터에 Dify 오케스트레이션을 배포하는 구조로 작동합니다.
- timing reason: 전시 참관 후 대외 수주 협상이 시작되는 시점으로 실서비스 유통 원가를 절감하고 공공 가점을 얻을 솔루션 세트 구안이 필요한 계제입니다.
- 고객 win: 대화 한 편당 발생하는 방대한 API 비용 부하를 국산 NPU 단독 호스팅 인프라로 전환해 서비스 이윤율을 높일 수 있습니다. 나라장터 공공 제안 시 국산 신기술 및 고보안성 인증 요건을 동시 탑재해 경쟁 우위를 점합니다.
- FuriosaAI win: Dify 생태계와 밀결합된 RNGD 가속 플랫폼 템플릿을 개발하여 에이전트 도입 기업들로 이어지는 추가 인프라 확장 물량을 선확보하게 됩니다.
- 직접 판매 가능성: `LOW`
- CSP 경유 판매 가능성: `HIGH`
- NPUaaS 유도 가능성: `HIGH`
- CSP capacity 증설 가능성: `MID`
- 수치 근거: 없음
- 컨택 명분: Dify 기반 대화형 지능 에이전트 원가 제어 목적 전용 국산 가속 서버 결합 유통 방안 제안
- 실제 컨택 시 사용할 말: 귀사의 Dify 공식 파트너십 구축 및 나라장터 스마트 브리핑 상담 확대 성과를 눈여겨보았습니다. AI 에이전트 구동 과정의 방대한 모델 서빙 요건에 맞춰, vLLM 연동성이 정교한 RNGD 인프라와 Dify 통합 전용 패키지를 구안해 공공에 제시하는 방안을 의논하고자 합니다.
- 매출 가능 시점: `중기`
- 담당자 후보 힌트: CTO 또는 platform lead
- 공개 프로필 URL: 
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: Dify 컨테이너의 NPU 물리 장치 드라이버 바인딩 시 호환성 여부 검증
- source_ids: S019, S020, S022
- source_urls: https://www.joongang.co.kr/article/25430014 | https://www.gokorea.kr/news/articleView.html?idxno=866999 | https://www.sentv.co.kr/article/view/sentv202605190084


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

1. **KB금융, AI 사이버 위협에 'AI 대 AI' 보안체계 강화**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T09:24:00+09:00`
   - matched_query_or_feed: `망분리 AI`
   - url: https://www.fetv.co.kr/news/articleView.html?idxno=303015
   - summary_snippet: 악성메일 대응 훈련에도 AI 에이전트를 적용해 최신 피싱 유형을 반영한 훈련 시나리오를 자동 생성·배포하고 있다. KB금융은 기존 망분리와 다중인증(MFA), 접근통제 체계를 유지하는 동시에 '절대 신뢰하지 않고 항상...

2. **[경제일보] "AI 돌리려면 결국 클라우드"…AI 투자 몰리자 웃는 클라우드...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T09:24:00+09:00`
   - matched_query_or_feed: `국내 클라우드 GPU 서비스`
   - url: https://www.ajunews.com/view/20260522143936317
   - summary_snippet: NHN 클라우드 역시 공공·게임·커머스 분야 수요 증가와 함께 AI 반도체 기반 클라우드 서비스와 GPU 인프라 사업 확대에 나서는 모습이다. 국내 기업들의 움직임은 글로벌 빅테크 흐름과도 맞물린다. 유진투자증권의...

3. **119에 AI 접목하는 소방 IT기업들…대구 위니텍의 30년 노하우**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T09:23:00+09:00`
   - matched_query_or_feed: `생성형 AI 도입 기업`
   - url: https://www.imaeil.com/page/view/2026052609222234981
   - summary_snippet: 구축해온 기업들이 기존 운영 체계에 AI를 얹는 작업에 속도를 내고 있다. 소방청은 시·도별로 나뉘어... AI 도입은 정책 청사진에 머물지 않는다. 충남도 소방본부는 올해 초 생성형 AI와 빅데이터 기술을 적용한 '지능형...

4. **솔루엠, ESL 마진 개선·AI데이터센터 모멘텀 기대…목표가↑-미래에셋 - 네이트**
   - source: `rss`
   - published_at_kst: `2026-05-26T09:23:00+09:00`
   - matched_query_or_feed: `Google News KR AI 데이터센터`
   - url: https://news.google.com/rss/articles/CBMiYEFVX3lxTE5lY3NQWmk2WkVWUWQxTVVVb211LU1reE55dkVwd1ZtbkxOams3Tmc5QUhQeS1oREdyYmFicy1uU0ZxQlZrMlE5YjRYbWpnT1NpWW1fTWZmRFJsSGFSVGZJXw?oc=5
   - summary_snippet: 솔루엠, ESL 마진 개선·AI데이터센터 모멘텀 기대…목표가↑-미래에셋  네이트

5. **119에 AI 접목하는 소방 IT기업들…대구 위니텍의 30년 노하우 - 매일신문**
   - source: `rss`
   - published_at_kst: `2026-05-26T09:22:30+09:00`
   - matched_query_or_feed: `Google News KR 생성형 AI`
   - url: https://news.google.com/rss/articles/CBMiYkFVX3lxTE56dEpzQk9uNDYzME5SWVFua1B5ZGJsVWZnSFp5SGs4UUtwOVF6YklmVEY4SXlRNGdwTmlIY3Y4TjREcDNRZ3o2SlhfamdxQVFrZzY0RVNaMktPME5XR0xrMWl3?oc=5
   - summary_snippet: 119에 AI 접목하는 소방 IT기업들…대구 위니텍의 30년 노하우  매일신문

6. **솔루엠, ESL 마진 개선·AI데이터센터 모멘텀 기대…목표가↑-미래에셋**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T09:22:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.mt.co.kr/stock/2026/05/26/2026052609185046705
   - summary_snippet: 미래에셋증권은 또 글로벌 빅테크 인공지능(AI) 데이터센터 전력(파워모듈) 진입이 구체화되고 있어 추가 모멘텀도 기대된다고 했다. 박준서 미래에셋증권 연구원은 "솔루엠의 ESL 가동률 상승과 신제품 비중 확대로...

7. **SK하이닉스, HBM 내장 냉각 기술 'iHBM' 공개**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T09:22:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.digitaltoday.co.kr/news/articleView.html?idxno=668849
   - summary_snippet: 고성능 컴퓨팅(HPC)과 AI 데이터센터 등 초고집적·초고대역폭 환경에서 요구되는 열 관리 기준을 충족하고, 시스템 전반의 안정성과 운영 효율을 높이겠다는 방향이다. 이강욱 SK하이닉스 부사장(PKG개발 담당)은...

8. **밀양시, 파워큐브세미㈜와 100억 원 규모 투자협약 체결**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T09:22:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.dnews.co.kr/uhtml/view.jsp?idxno=202605252006571380883
   - summary_snippet: 최근 AI, 전기차, 데이터센터, 신재생에너지 산업 확대와 함께 전력반도체 시장이 빠르게 성장하고 있는 가운데, 이번 투자는 밀양나노융합국가산단이 첨단 반도체 산업의 새로운 거점으로 도약하는 중요한 계기가 될...

9. **삼화전자, AI 서버·전기차 확산 최대 수혜…전자부품 수요 폭발에 들썩**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T09:22:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.pinpointnews.co.kr/news/articleView.html?idxno=455228
   - summary_snippet: 최근 글로벌 빅테크 기업들의 AI 투자 확대와 데이터센터 증설 움직임이 이어지면서 국내 전자부품 업체들에 대한 실적 기대감이 빠르게 반영되는 분위기다. 고다층 PCB와 AI 서버용 부품 공급 기업들이 시장의 중심으로...

10. **SK하이닉스, ‘iHBM’ 기술 공개…“발열 최소화 위한 설루션”**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T09:22:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: http://www.segyebiz.com/newsView/20260526503099?OutUrl=naver
   - summary_snippet: SK하이닉스는 iHBM 기술을 HBM5 등 차세대 제품부터 적용해 고성능 컴퓨팅(HPC), AI 데이터센터 등 초고집적·초고대역폭 환경에서 요구되는 열 관리 수준을 충족하며 시스템 전반의 안정성과 운영 효율을 높인다는...

11. **“금융권도 AI 풀어준다”…망분리 규제 푼다, 보안용 AI 긴급 허용**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T09:20:00+09:00`
   - matched_query_or_feed: `생성형 AI 도입 기업`
   - url: https://www.gosiweek.com/article/1065608272873992
   - summary_snippet: 그동안 금융회사는 외부 인터넷망과 내부 업무망을 분리해야 해 생성형 AI와 클라우드 기반 보안서비스... 이번 대책은 최근 미국 AI 기업 앤트로픽의 고성능 AI ‘미토스(Mithos)’ 이슈가 계기가 됐다. 금융위는 미토스가...

12. **[정태철 칼럼] 21세기 세계 구석구석의 권위주의 부상, 그리고 민주주의...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T09:20:00+09:00`
   - matched_query_or_feed: `제조 AI 플랫폼`
   - url: http://www.civicnews.com/news/articleView.html?idxno=39877
   - summary_snippet: 최근에는 우리가 잘 아는 것처럼 전기차, 로봇, 드론, 반도체, 심지어 AI 산업까지도 비약적으로 도약하고... 디지털 플랫폼 임시 프리랜서 직업 위주 경제를 뜻함)가 주류를 이루면서 전통적인 제조업이 쇠퇴해서 남성...

13. **[금융권 이모저모]KB금융, AI 기반 사이버 보안위협에 'AI 대 AI' 방어 체...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T09:20:00+09:00`
   - matched_query_or_feed: `클라우드 AI 서비스`
   - url: https://www.businessplus.kr/news/articleView.html?idxno=112182
   - summary_snippet: 전문기관의 'AI 에이전트'를 도입해 정보보호 실태점검(모의해킹)과 보안업무 자동화를 추진하고 있다. 또 '절대 신뢰하지 않고 항상 검증'하는 제로트러스트 원칙을 그룹 클라우드 환경 등 전반에 확대 적용하고...

14. **SK하이닉스, AI 발열 잡는 ‘iHBM’ 공개**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T09:19:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.dt.co.kr/article/12064225?ref=naver
   - summary_snippet: 최근 AI 데이터센터와 고성능컴퓨팅(HPC) 시장 확대에 따라 HBM은 더 많은 D램을 수직으로 쌓는 고적층 구조와 초고속 동작이 요구되고 있다. 다만 성능 향상과 함께 발열도 급증하면서, HBM과 그래픽처리장치(GPU)...

15. **"AI 데이터센터 발열 잡는다" 에쓰오일, 액침냉각 실증 추진**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T09:19:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: http://www.wowtv.co.kr/NewsCenter/News/Read?articleId=A202605260119&t=NN
   - summary_snippet: 실제 AI 데이터센터 환경을 기반으로 진행된다. 이번 테스트에서 에쓰오일은 액침냉각유 '에쓰오일 e-쿨링 솔루션' 공급 및 기술 지원을 담당한다. 데이터센터 인프라 관리 솔루션 업체 '어니언소프트웨어', 액침냉각 장비...

16. **(수요광장)AI 시대, 지역산업 정책의 방향**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T09:18:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.electimes.com/news/articleView.html?idxno=368360
   - summary_snippet: 이번 전국 지방자치단체장 후보들의 공약 중에서 눈에 띄는 것은 '반도체 제조 공장(Fab)'과 'AI 데이터센터' 등 첨단산업 유치를 통해 지역 경제를 살리겠다고 강조하는 것이다. 선거 공약이 그대로 이행된다면 대한민국...

17. **The E-STATION - 에너지 미디어**
   - source: `rss`
   - published_at_kst: `2026-05-26T09:16:37+09:00`
   - matched_query_or_feed: `Google News KR AI 데이터센터`
   - url: https://news.google.com/rss/articles/CBMikgFBVV95cUxQbEZ0ekZ1cGJNbHN2LVBSVXBuVVYwcWVtbG9MTW5jQ3p6cFZMSzZvQnRINEJ3c0JRczJfODdKbm1QbzV3bmZ3T2dva1BCMXVlT2JrSnJDVXJ2Z3dJRlVQZm12aVhSUUhmRjE1dlVGZ2pJV05NOHEyeFJ2eTI4eHRfeFBkVUxOSE9ZTF9FdUlJMFBJQQ?oc=5
   - summary_snippet: The E-STATION  에너지 미디어

18. **에쓰오일, AI 데이터센터 액침냉각 실증 나선다 - 이뉴스투데이**
   - source: `rss`
   - published_at_kst: `2026-05-26T09:15:00+09:00`
   - matched_query_or_feed: `Google News KR AI 데이터센터`
   - url: https://news.google.com/rss/articles/CBMickFVX3lxTE1CVndCbmxpR1FUQWFvYXA0S3JJbFktMXE1RzRlR1hZaE85X250TTVRX3NFb1hjNlZXTjRFQmdFWWNUdFpJYnplTzRqeE1MS2dOUkJUU3ktTjByUmkwVVVNbkphUmRkV1J1QU40YXVseEl5UdIBdEFVX3lxTFBJc0xQNy1Vajgxa2c1ME1lQzEtNFc3a1lsQm5aUWdBcENPZXJLWUJnY3NDdmw0TEFBS0pPbVJhSmI4eFhrVmV5S3B5MEJ1LUdpOXZ2LW9nZE93NGJtMExldVVuNEJ1d1ZIRkNzY0xGbHRmanJr?oc=5
   - summary_snippet: 에쓰오일, AI 데이터센터 액침냉각 실증 나선다  이뉴스투데이

19. **KB금융, AI 사이버 보안위협 대비 그룹 통합 보안체계 운영**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T09:14:00+09:00`
   - matched_query_or_feed: `클라우드 AI 서비스`
   - url: https://www.joongangenews.com/news/articleView.html?idxno=521503
   - summary_snippet: 특히 그룹 클라우드 환경에 대한 제로트러스트 3단계 구축 완료 사례는 금융업권에서 가장 선제적 구축 사례로 평가받고 있다. 아울러 지난해 3월 수립한 AI 거버넌스를 바탕으로 AI 서비스 수명주기 전 단계에서 31개...

20. **KB금융, 'AI 대 AI' 보안체계 강화…사이버보안센터 출범**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T09:14:00+09:00`
   - matched_query_or_feed: `클라우드 AI 서비스`
   - url: https://www.cstimes.com/news/articleView.html?idxno=707129
   - summary_snippet: 그룹 클라우드 환경에 대한 제로 트러스트 3단계 구축을 완료했으며, 주요 AI 서비스는 금융보안원 AI 레드티밍을 통해 취약점을 사전 점검하고 있다. 아울러 금융권 최초로 모의침투 기반 사전 예방 조직인 '그룹...


## 다음 단계

1. LLM 후보 품질 확인
2. 노이즈가 많으면 NAVER_QUERIES / RSS_FEEDS 개선
3. 후보가 너무 적으면 MAX_LLM_SOURCES 상향
4. Gemini 3.5 Flash vs 2.5 Flash 품질 비교
5. 나라장터/B2G 수집 추가
6. 담당자/의사결정자 탐색 추가
7. Notion 또는 Google Docs 업로드 추가
