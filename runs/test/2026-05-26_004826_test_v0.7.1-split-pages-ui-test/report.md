# FuriosaAI GTM Research Agent Test Run

## 실행 정보

- run_id: `2026-05-26_004826_test_v0.7.1-split-pages-ui-test`
- mode: `test`
- memo: `v0.7.1-split-pages-ui-test`
- executed_at_kst: `2026-05-26T00:54:48.890271+09:00`
- agent_version: `v0.7`
- instructions_loaded_chars: `21592`
- naver_sources_recent_7d_count: `191`
- rss_sources_recent_7d_count: `97`
- merged_sources_recent_7d_count: `288`
- furiosa_docs_successful: `11`
- furiosa_docs_failed: `0`
- llm_called: `True`
- llm_error: ``

## 현재 단계

이 실행은 v0.7 테스트입니다.

이번 버전에서는 네이버 뉴스 API, RSS feed, FuriosaAI 공개 개발자 문서를 수집한 뒤 Gemini로 GTM 후보를 1차 평가하고, 별도 LLM 호출로 매니저용 gtm_report.md를 작성합니다.

아직 나라장터 직접 API, 담당자 심화 탐색, Notion 업로드는 수행하지 않았습니다.

## LLM 실행 요약

- overall_assessment: 최근 7일 국내 GTM 환경은 민간 및 공공 대형 데이터센터의 전력 공급난 심화와 국내 CSP들의 합작 대응 기조가 돋보입니다. 특히 삼성SDS의 지속적인 자체 데이터센터 확장과 대형 금융사 AI 에이전트 사업 수주, 엘리스그룹의 코스닥 상장 청구에 따른 독자 인프라 고도화 움직임은 고성능 저전력 국산 NPU에 매우 강력한 기회 요인입니다. 또한 금융권 망분리 규제 합리화 흐름과 의료 공공기관의 자체 AI 통합 플랫폼 구축 드라이브가 가속화되고 있어, 비용 효율적이고 보안성이 높은 프라이빗 온프레미스 인프라 수요 역시 강력하게 포착되고 있습니다.
- top_priority_names: 삼성SDS, 엘리스그룹, KT클라우드
- noise_ratio_comment: 수집된 데이터 중 중국 시장 중심의 알리바바 및 텐센트 등의 인프라 동향이나 실질적 한국 및 일본 GTM 접점이 없는 머스크의 xAI 대규모 컴퓨터 확장 뉴스는 전략적 노이즈로 분류하고 제외하였습니다.
- model_compatibility_caution: NH농협은행 및 한글과컴퓨터 사례의 경우 엑사원 계열 모델 도입 정황이 명확히 포착되었으나, 구체적인 모델 아키텍처 버전과 커스텀 파인튜닝 수준이 당사 지원 목록과 일치하는지에 대한 검증이 필요합니다. 엑사원 계열의 경우 버전 간 연산 특성 차이가 존재하므로 제품 제안 전 세부 호환 성능 체크를 선행 조치해야 합니다.

## LLM 후보 평가 결과

## 버전 1 — B2B only 우선 검토 요약

- 삼성SDS / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- KT클라우드 / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- NH농협은행 / 온프레미스 기업 / classification: `structure_check` / fit: `MID` / outreach: `MID` / 매출시점: `중기`
- 엘리스그룹 / CSP 운영 기업 / classification: `cloud_npuaaS_lead` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- 우리은행 / CSP 고객 기업 / classification: `cloud_npuaaS_lead` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`


## 버전 2 — B2B + B2G 우선 검토 요약

- 삼성SDS / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- KT클라우드 / CSP 운영 기업 / classification: `priority_outreach` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- NH농협은행 / 온프레미스 기업 / classification: `structure_check` / fit: `MID` / outreach: `MID` / 매출시점: `중기`
- 한글과컴퓨터 / CSP 고객 기업 / classification: `structure_check` / fit: `MID` / outreach: `MID` / 매출시점: `중기` / B2G 근거: `기사/RSS 기반` / 나라장터 확인: `미수행`
- 건강보험심사평가원 / 온프레미스 기업 / classification: `structure_check` / fit: `MID` / outreach: `MID` / 매출시점: `장기` / B2G 근거: `기사/RSS 기반` / 나라장터 확인: `미수행`
- 엘리스그룹 / CSP 운영 기업 / classification: `cloud_npuaaS_lead` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`
- 우리은행 / CSP 고객 기업 / classification: `cloud_npuaaS_lead` / fit: `MID` / outreach: `HIGH` / 매출시점: `단기`


## 상세 후보 평가

### 1. 삼성SDS

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `CSP 운영 기업`
- 분류: `priority_outreach`
- 확인된 프로젝트/시그널: 동탄 및 구미 데이터센터 인프라 확장 및 우리은행 AI 에이전트 구축 사업 수주
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 모델 적합성은 미확인 상태이나, 동탄 데이터센터 20MW 전력 확보 및 구미에 4273억원 규모의 60MW 데이터센터를 투자하는 초대형 인프라 사업자입니다. 또한 우리은행 등 대형 금융권 사업을 수주하여 NPUaaS 및 SCP 클라우드 기반의 대규모 추론 인프라 증설 수요가 매우 높으므로 최우선 전략 채널로 분류합니다.
- hook_type: `CLOUD`
- 핵심 buying signal: 동탄 및 구미 지역의 신규 AI 데이터센터 설립과 전력 확보를 지속하고 있으며, 우리은행의 생성형 AI 에이전트 사업 우선협상대상자로 선정되어 금융권 AX 시장을 주도하고 있습니다.
- 인프라 signal: 동탄 데이터센터 서관 가동을 위한 20MW급 전력 확보 및 경북 구미에 4273억원을 투자하여 60MW 규모의 AI 데이터센터를 구축할 계획입니다.
- timing reason: 최근 우리은행 사업 수주 및 대규모 데이터센터 전력 확보 소식이 전해진 시점으로, 인프라 효율화와 추론 비용 절감을 위한 하드웨어 파트너십 논의의 적기입니다.
- 고객 win: 삼성SDS는 초대형 AI 데이터센터 운영에 따른 전력과 냉각 부담을 완화할 수 있습니다. 특히 SCP 클라우드 기반 NPUaaS 인프라에 RNGD를 도입함으로써 전력 효율을 높이고 고객사 대상 AI 추론 단가를 경쟁력 있게 제공할 수 있습니다.
- FuriosaAI win: FuriosaAI는 삼성SDS의 SCP 클라우드 및 NPUaaS 인프라에 RNGD를 대규모로 공급할 수 있는 기회를 확보합니다. 이를 통해 공공 및 금융권 CSP 고객사 수요를 간접적으로 선점하는 강력한 유통 채널을 구축하게 됩니다.
- 직접 판매 가능성: `MID`
- CSP 경유 판매 가능성: `HIGH`
- NPUaaS 유도 가능성: `HIGH`
- CSP capacity 증설 가능성: `HIGH`
- 수치 근거: 경기 동탄 데이터센터 서관 가동을 위해 20MW급 전력 확보 (S003) — 근거: 삼성SDS가 경기 동탄 데이터센터 서관 가동을 위해 20MW급 전력을 확보한 사례 | 경북 구미 AI 데이터센터에 4273억원 투자 및 60MW 규모 구축 계획 (S010) — 근거: 삼성SDS는 경북 구미에 4273억원을 투자해 60MW 규모 AI 데이터센터를 짓기로 했다.
- 컨택 명분: 삼성SDS의 동탄 및 구미 데이터센터 대규모 증설 계획과 금융권 초거대 AI 사업 수주에 맞춰, 저전력 고효율 AI 가속기 도입을 통한 인프라 비용 절감 방안을 제안합니다.
- 실제 컨택 시 사용할 말: 최근 동탄 및 구미 지역의 대규모 AI 데이터센터 구축 소식과 우리은행 사업 수주 성과를 보고 연락드렸습니다. 현재 가속화되는 인프라 확장 단계에서 고효율 가속기 도입을 통한 전력 비용 및 추론 단가 최적화 방안을 함께 논의하고자 합니다.
- 매출 가능 시점: `단기`
- 담당자 후보 힌트: 삼성SDS 클라우드서비스사업부장, AI서비스센터장, 인프라 기획 부서장 또는 구매 담당 책임자
- 공개 프로필 URL: https://www.linkedin.com/company/samsung-sds
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: SCP 인프라 내 RNGD 평가 및 호환성 테스트 여부 | 구미 데이터센터 착공 일정 및 인프라 발주 시기
- source_ids: S001, S003, S010, S012, S026, S028, S031, S038, S039
- source_urls: https://www.mt.co.kr/tech/2026/05/20/2026051922000848265 | https://www.e-science.co.kr/news/articleView.html?idxno=130004 | https://www.mt.co.kr/tech/2026/05/23/2026052210211399740 | https://www.thepowernews.co.kr/view.php?ud=202605221116568858de3f0aa1be_7 | https://www.sedaily.com/article/20046605?ref=naver | https://www.sedaily.com/article/20046505?ref=naver | https://www.ddaily.co.kr/page/view/2026052216371975959 | https://www.pinpointnews.co.kr/news/articleView.html?idxno=454902 | https://www.sedaily.com/article/20047365?ref=naver

### 2. KT클라우드

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `CSP 운영 기업`
- 분류: `priority_outreach`
- 확인된 프로젝트/시그널: AI DC 가동 및 GPUaaS 매출 증가, 해남 솔라시도 국가AI컴퓨팅센터 컨소시엄 참여
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 모델 적합성은 미확인이나, 1분기 매출이 2501억원에 달하고 AI DC 사업 확대와 대규모 국가 컴퓨팅 인프라 컨소시엄에 참여 중인 초대형 CSP 사업자입니다. 저전력 국산 가속기를 자사 AI 클라우드에 탑재하여 전력 수급난을 완화할 명분이 확실하므로 우선순위를 HIGH로 지정합니다.
- hook_type: `POWER`
- 핵심 buying signal: 서울 가산 및 판교 데이터센터 가동률 상승과 GPUaaS 부문 매출 성장을 바탕으로 AI 인프라 사업을 가속화하고 있습니다.
- 인프라 signal: 전남 해남 솔라시도 지역에 삼성SDS 등과 함께 국가AI컴퓨팅센터 구축 컨소시엄에 참여하여 대형 인프라 확충을 지속하고 있습니다.
- timing reason: 데이터센터 전력 공급 부족과 비용 상승에 대응해야 하는 시기로, 저전력 특성이 극대화된 국산 대체 하드웨어 도입 논의가 활발한 시점입니다.
- 고객 win: KT클라우드는 수도권 데이터센터의 심각한 전력난 속에서 저전력 가속기를 도입하여 랙 밀도를 높이고 상면당 전력 소모를 제어할 수 있습니다. 대규모 추론 서비스용 단가를 낮춰 시장 경쟁력을 확보합니다.
- FuriosaAI win: FuriosaAI는 국내 주요 CSP인 KT클라우드에 RNGD를 탑재함으로써 자사 가속기 기반의 상용 인프라 생태계를 단번에 확장하고 대규모 하드웨어 납품 성과를 창출할 수 있습니다.
- 직접 판매 가능성: `HIGH`
- CSP 경유 판매 가능성: `LOW`
- NPUaaS 유도 가능성: `HIGH`
- CSP capacity 증설 가능성: `HIGH`
- 수치 근거: KT클라우드 1분기 매출 2501억원 달성 (S008) — 근거: KT클라우드의 1분기 매출은 2501억원으로
- 컨택 명분: 급증하는 AI DC 인프라 수요와 전력 공급 한계를 극복하기 위해, KT클라우드 인프라 내에 저전력 고효율 가속기 도입을 제안합니다.
- 실제 컨택 시 사용할 말: 최근 귀사의 분기 매출 성장 성과와 해남 솔라시도 국가AI컴퓨팅센터 참여 등 대규모 클라우드 증설 소식을 인상 깊게 보았습니다. 급격한 인프라 확장 속에서 전력 제약과 랙 공간 한계를 해결할 수 있는 당사의 초저전력 가속기 결합 방안을 기획하고자 연락드렸습니다.
- 매출 가능 시점: `단기`
- 담당자 후보 힌트: 대표이사, AI DC 사업 본부장, 인프라 기획 부서장
- 공개 프로필 URL: 확인 필요
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 현재 KT클라우드 내 타 국산 NPU 가속기 도입 비율 | 국가AI컴퓨팅센터 내 가속기 규격 요건
- source_ids: S001, S005, S008, S010
- source_urls: https://www.mt.co.kr/tech/2026/05/20/2026051922000848265 | https://www.ddaily.co.kr/page/view/2026052017342600376 | https://www.m-i.kr/news/articleView.html?idxno=1375542 | https://www.mt.co.kr/tech/2026/05/23/2026052210211399740

### 3. NH농협은행

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `온프레미스 기업`
- 분류: `structure_check`
- 확인된 프로젝트/시그널: LG CNS 전용 생성형 AI 구축 사업 및 검색증강생성(RAG) 플랫폼 고도화
- 확인된 모델명: `EXAONE-3.5`
- 모델 매칭 상태: `family_only`
- 모델 fit_score: `MID`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `MID`
- RNGD fit_score: `MID`
- outreach priority: `MID`
- fit vs priority 설명: 엑사원 모델 계열을 활용하고 있어 모델 아키텍처 정합성은 양호하지만, 엑사원 전용 파인튜닝 버전의 호환성 검증이 추가로 필요합니다. LG CNS가 주도하는 농협은행 전용 생성형 AI의 인프라 전환 명분과 세부 사양 구조를 검증해야 하므로 structure_check 단계로 설정합니다.
- hook_type: `SOVEREIGN`
- 핵심 buying signal: 농협은행 전용 생성형 AI 플랫폼 구축을 통해 내부 업무 규정, 상품 정보 검색 및 리테일 영업 지원 등의 용도로 RAG를 본격 확대하고 있습니다.
- 인프라 signal: 금융권 자체의 내부 전용 프라이빗 AI 플랫폼 구축 흐름을 따르고 있어 온프레미스 또는 프라이빗 클라우드 폐쇄망 환경이 예상됩니다.
- timing reason: 시스템 구축 사업이 본격화되어 실무 비즈니스 영역에 적용되는 시점으로, 운영 효율성과 비용 절감을 논의하기 적절한 접촉 명분이 제공됩니다.
- 고객 win: 농협은행은 내부 중요 정보의 외부 유출 걱정 없이 프라이빗 환경에서 대규모 실시간 질의를 지연 시간 없이 안정적으로 처리할 수 있습니다. 고가의 연산 자원 비용 부담을 크게 낮출 수 있습니다.
- FuriosaAI win: FuriosaAI는 금융권 핵심 프라이빗 AI 도입 계정을 확보하고, 국산 대표 오픈형 모델인 엑사원 엔진 위에서 고효율 서빙 인프라의 강점을 성공적으로 증명할 수 있습니다.
- 직접 판매 가능성: `LOW`
- CSP 경유 판매 가능성: `MID`
- NPUaaS 유도 가능성: `MID`
- CSP capacity 증설 가능성: `LOW`
- 수치 근거: 없음
- 컨택 명분: LG CNS와 구축하는 전용 엑사원 AI RAG 인프라의 비용 최적화를 위해 저전력 가속기 결합 방안 검토를 제안합니다.
- 실제 컨택 시 사용할 말: 최근 LG CNS와 함께 귀행 전용 초거대 AI 플랫폼 및 RAG 기반 업무 서비스를 추진하신다는 소식을 인상 깊게 보았습니다. 안정적인 프라이빗 시스템 운영을 위해 전력 소모가 적으면서도 대규모 실시간 질의 처리에 탁월한 국산 고성능 가속기 활용 방안을 제안드리고자 합니다.
- 매출 가능 시점: `중기`
- 담당자 후보 힌트: IT부문 부행장, 디지털전략부서장, 플랫폼 인프라 실무 파트장
- 공개 프로필 URL: https://www.sanctionlab.com/?p=46854
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 구축 파트너사인 LG CNS의 하드웨어 변경 권한 여부 | 엑사원 튜닝 모델의 구체적인 크기 및 호환 성능
- source_ids: S020
- source_urls: https://www.news2day.co.kr/article/20260522500024

### 4. 한글과컴퓨터

- 국가: `KR`
- 시장: `B2G`
- 타깃 유형: `CSP 고객 기업`
- 분류: `structure_check`
- 확인된 프로젝트/시그널: LG AI연구원과 AI 문서 에이전트 및 챗엑사원 공공 시장 공동 공략
- 확인된 모델명: `EXAONE`
- 모델 매칭 상태: `family_only`
- 모델 fit_score: `MID`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `MID`
- RNGD fit_score: `MID`
- outreach priority: `MID`
- fit vs priority 설명: 모델은 공공 시장을 타깃으로 하는 엑사원 계열로 당사 지원 라인업과 호환 가능성이 높지만, 구체적인 모델 크기 및 공공 클라우드 배포 스택과의 하드웨어 호환성 검증이 필요합니다. 공공 AX 동맹의 일원으로서 솔루션 공급 구조를 파악해야 하므로 structure_check로 분류합니다.
- hook_type: `PROCUREMENT`
- 핵심 buying signal: LG AI연구원과 손잡고 한컴의 AI 에이전트 기술과 엑사원 모델을 결합하여 공공기관 및 지자체 대상 영업과 솔루션 수주를 본격적으로 가속화하고 있습니다.
- 인프라 signal: 정부부처 및 지자체 대상이므로 프라이빗 온프레미스 구축 및 행정안전부 등 공공 전용 클라우드 배포 규격을 따를 예정입니다.
- timing reason: 양사가 공공 AI 동맹을 결성하고 시장 수주에 본격 나서는 단계이므로, 조달 단가 경쟁력을 극대화할 국산 가속기 제안이 시의적절합니다.
- 고객 win: 한글과컴퓨터는 공공 부문 솔루션 공급 시 하드웨어 인프라 비용 부담을 줄여 제안 단가 경쟁력을 높일 수 있습니다. 특히 공공 보안 규제와 프라이빗 온프레미스 설치 요구에 고효율 저전력 인프라로 유연하게 맞출 수 있습니다.
- FuriosaAI win: FuriosaAI는 국산 사무형 AI 및 문서 저작 도구의 사실상 표준인 한컴 솔루션과 당사 가속기 엔진을 결합하여, 공공 B2G 시장 전체로 RNGD 수요를 동시 확산시킬 수 있습니다.
- 직접 판매 가능성: `MID`
- CSP 경유 판매 가능성: `MID`
- NPUaaS 유도 가능성: `MID`
- CSP capacity 증설 가능성: `MID`
- 수치 근거: 없음
- 컨택 명분: 공공 AX 시장을 겨냥해 공동 개발하는 엑사원 기반 한컴 AI 에이전트 인프라의 원가 경쟁력 강화를 위한 하드웨어 협력을 제안합니다.
- 실제 컨택 시 사용할 말: 최근 LG AI연구원과 손잡고 공공 AX 시장 수주를 위한 공동 동맹을 결성하신 소식을 뜻깊게 보았습니다. 귀사의 초거대 AI 문서 에이전트 솔루션이 공공 인프라에 안착할 때, 제안 경쟁력을 높이고 상면 비용을 획기적으로 낮춰줄 고효율 국산 가속기 협력 모델을 제안드립니다.
- 매출 가능 시점: `중기`
- 담당자 후보 힌트: AI사업본부장, 공공사업부문장, 연동 솔루션 아키텍트 총괄
- 공개 프로필 URL: 확인 필요
- 기존 접점: `확인 필요`
- B2G 근거 유형: `기사/RSS 기반`
- 나라장터 직접 확인: `미수행`
- 조달상 다음 액션: 나라장터/RFP 직접 확인 필요
- 확인 필요: 한컴 에이전트가 배포될 주요 공공 클라우드 가상 환경 규격 | 엑사원 탑재 형태가 온프레미스형인지 MaaS형인지 여부
- source_ids: S021, S022, S023, S024, S025
- source_urls: http://www.newslock.co.kr/news/articleView.html?idxno=130504 | https://www.mt.co.kr/tech/2026/05/22/2026052215283358675 | https://www.mk.co.kr/article/12055579 | https://www.getnews.co.kr/news/articleView.html?idxno=870707 | https://www.newsis.com/view/NISX20260522_0003640664

### 5. 건강보험심사평가원

- 국가: `KR`
- 시장: `B2G`
- 타깃 유형: `온프레미스 기업`
- 분류: `structure_check`
- 확인된 프로젝트/시그널: AI 통합플랫폼 구축 및 GPU 서버 기반 인프라 도입 계획 수립
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `MID`
- RNGD fit_score: `MID`
- outreach priority: `MID`
- fit vs priority 설명: 모델 적합성은 미확인 상태이나, GPU 서버 기반의 자체 AI 통합 플랫폼과 전용 데이터 인프라를 직접 기획 및 구축하는 강력한 공공 수요처입니다. 실제 장비 규격과 국산 가속기 가상화 솔루션의 적용 가능성을 확인해야 하므로 structure_check로 분류합니다.
- hook_type: `PROCUREMENT`
- 핵심 buying signal: 디지털전략실 및 디지털클라우드센터를 중심으로 자체 인프라를 활용하여 AI 개발과 운영을 일원화하는 AI 통합플랫폼 구축에 총력을 기울이고 있습니다.
- 인프라 signal: 심평원 자체 GPU 서버 기반의 온프레미스 인프라를 설계하며, 원스톱 서비스 제공을 위한 플랫폼 인프라를 구축할 계획입니다.
- timing reason: 기관의 디지털클라우드센터 전략 수립과 하드웨어 인프라 발주 기획 단계에 있어, 공공 조달을 목표로 사전 규격을 검토하기에 이상적인 접촉 시기입니다.
- 고객 win: 건강보험심사평가원은 방대한 공공 의료 데이터를 안전하게 다루는 내부 인프라에서 전력과 상면 효율을 고려한 안정적인 GPU 대체 인프라를 구성할 수 있습니다. 조달 예산 범위 내에서 대용량 연산 풀을 유연하게 확보합니다.
- FuriosaAI win: FuriosaAI는 국가 중추 의료 공공기관의 온프레미스 AI 인프라 표준 규격에 진입하는 중요한 레퍼런스를 구축하고, 다른 공공 산하 기관으로의 확장 교두보를 마련할 수 있습니다.
- 직접 판매 가능성: `MID`
- CSP 경유 판매 가능성: `MID`
- NPUaaS 유도 가능성: `LOW`
- CSP capacity 증설 가능성: `LOW`
- 수치 근거: 없음
- 컨택 명분: 심평원이 계획 중인 GPU 기반 AI 통합플랫폼의 조달 효율성과 가상화 운영 효율 증대를 위한 국산 가속기 제안을 검토합니다.
- 실제 컨택 시 사용할 말: 최근 귀원의 AI 통합플랫폼 구축 및 GPU 인프라 도입 드라이브 계획을 확인하였습니다. 의료 공공 데이터의 프라이빗 보안 환경에 최적화되고, 조달 단가와 전력 소비율을 대폭 향상시켜 줄 국산 고성능 가속기 기반의 효율적인 플랫폼 구축 방안을 공유해 드리고자 합니다.
- 매출 가능 시점: `장기`
- 담당자 후보 힌트: 디지털전략실장 겸 디지털클라우드센터장, AI융합추진단장, 인프라 기획 담당 사무관
- 공개 프로필 URL: 확인 필요
- 기존 접점: `확인 필요`
- B2G 근거 유형: `기사/RSS 기반`
- 나라장터 직접 확인: `미수행`
- 조달상 다음 액션: 나라장터/RFP 직접 확인 필요
- 확인 필요: 플랫폼 내 탑재 예정인 오픈소스 기반 LLM 및 추론 서비스 아키텍처 | 공공 인프라 조달 예산 수립 규모와 정식 입찰 공고 예정 일정
- source_ids: S035
- source_urls: https://www.etnews.com/20260522000181

### 6. 엘리스그룹

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `CSP 운영 기업`
- 분류: `cloud_npuaaS_lead`
- 확인된 프로젝트/시그널: 코스닥 상장 추진 및 GPUaaS, AI 클라우드 인프라 사업 확장
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `HIGH`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 모델 적합성은 미확인이지만 상장 추진에 맞춰 GPUaaS 및 이동식 모듈형 데이터센터 등 자체 AI 인프라 사업을 빠르게 확장하고 있습니다. 국산 NPUaaS 라인업 다양화와 비용 효율화를 위해 적극적인 파트너십 구축이 가능하므로 outreach priority를 HIGH로 설정합니다.
- hook_type: `PARTNER`
- 핵심 buying signal: 코스닥 상장예비심사를 청구하며 자체 인프라인 ECI 및 GPUaaS 사업 선점 고도화를 공표하였습니다.
- 인프라 signal: 대규모 인프라 자원을 효율적으로 배치하는 기술과 이동식 모듈형 데이터센터를 보유하고 있어 독립적인 추론 팜 구축 역량이 높습니다.
- timing reason: 상장 청구 직후 성장을 가속화하는 시점으로, 대규모 인프라 도입 및 하드웨어 다각화를 위한 전략적 제휴를 논의하기에 최적입니다.
- 고객 win: 엘리스그룹은 고비용인 GPU 의존도를 낮추고 고효율 NPU 인프라를 추가 확보하여 마진율을 개선할 수 있습니다. 상장에 앞서 원가 경쟁력을 입증하고 독자적인 풀스택 AI 솔루션을 완성하는 데 기여합니다.
- FuriosaAI win: FuriosaAI는 국산 AI 클라우드 강자인 엘리스그룹의 인프라 파트너로 참여하여 대규모 실제 납품 레퍼런스를 확보하고 지속적인 가속기 판매 경로를 마련할 수 있습니다.
- 직접 판매 가능성: `HIGH`
- CSP 경유 판매 가능성: `MID`
- NPUaaS 유도 가능성: `HIGH`
- CSP capacity 증설 가능성: `MID`
- 수치 근거: 없음
- 컨택 명분: 엘리스그룹의 코스닥 상장 예비심사 청구와 GPUaaS 사업 고도화 기조에 발맞춰 국산 가속기 도입을 통한 원가 절감 방안을 제시합니다.
- 실제 컨택 시 사용할 말: 최근 코스닥 상장예비심사 청구 및 자체 인프라 고도화 소식을 기쁘게 접하였습니다. 귀사가 보유한 독보적인 풀스택 인프라 역량에 당사의 고효율 가속기를 결합하여, 서비스 원가를 혁신적으로 절감하고 시장을 선점할 방안을 제안드리고자 합니다.
- 매출 가능 시점: `단기`
- 담당자 후보 힌트: 대표이사, 인프라 사업 본부장, 플랫폼 개발 실장
- 공개 프로필 URL: https://www.venturesquare.net/950953/
- 기존 접점: `엘리스 ✅`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 기존 진행 중인 NDA 또는 PoC 내역 업데이트 | 상장 전 신규 하드웨어 도입 예산 확보 여부
- source_ids: S013, S014, S015, S016, S017, S018
- source_urls: http://www.hansbiz.co.kr/news/articleView.html?idxno=839792 | http://www.joseilbo.com/news/news_read.php?uid=568639&class=53&grp= | https://www.fetv.co.kr/news/articleView.html?idxno=302765 | https://www.the-stock.kr/news/articleView.html?idxno=32570 | https://www.newspim.com/news/view/20260520000146 | https://www.cstimes.com/news/articleView.html?idxno=706484

### 7. 우리은행

- 국가: `KR`
- 시장: `B2B`
- 타깃 유형: `CSP 고객 기업`
- 분류: `cloud_npuaaS_lead`
- 확인된 프로젝트/시그널: 우선협상대상자 삼성SDS와 생성형 AI 에이전트 구축 사업 추진
- 확인된 모델명: `미확인`
- 모델 매칭 상태: `unknown`
- 모델 fit_score: `UNKNOWN`
- 배포/인프라 fit_score: `MID`
- 채널/CSP fit_score: `HIGH`
- RNGD fit_score: `MID`
- outreach priority: `HIGH`
- fit vs priority 설명: 모델 적합성은 미확인 상태이나, 삼성SDS를 우선협상대상자로 선정하여 대규모 생성형 AI 시스템을 구축하는 초대형 금융권 엔터프라이즈 수요처입니다. 삼성SDS의 클라우드 인프라를 활용하므로, CSP 경유 및 NPUaaS 유도를 위한 핵심 수요 창출 고객으로 적합하여 우선순위를 HIGH로 설정합니다.
- hook_type: `CLOUD`
- 핵심 buying signal: 생성형 AI 에이전트 구축 사업의 우선협상대상자로 삼성SDS를 선정하여 본격적인 금융 업무 지능화를 추진하고 있습니다.
- 인프라 signal: 금융권의 엄격한 보안 규제와 데이터 관리를 고려하여 망분리 우회 또는 합리화 흐름에 맞춘 인프라를 설계할 가능성이 높습니다.
- timing reason: 사업 우선협상대상자 선정 후 시스템 설계가 구체화되는 시점으로, 인프라 비용을 대폭 줄일 수 있는 국산 가속기 옵션을 제안할 수 있는 적기입니다.
- 고객 win: 우리은행은 대규모 고객 상담 및 자산 분석 시 발생하는 클라우드 추론 비용을 혁신적으로 절감할 수 있습니다. 국산 가속기를 통해 안정적이고 비용 효율적인 상시 서비스 운영 체계를 확립하게 됩니다.
- FuriosaAI win: FuriosaAI는 대형 시중은행의 상용 생성형 AI 서비스에 가속기를 공급하는 상징적인 금융 레퍼런스를 확보하며, 삼성SDS 인프라의 가속기 증설을 유도할 수 있습니다.
- 직접 판매 가능성: `LOW`
- CSP 경유 판매 가능성: `HIGH`
- NPUaaS 유도 가능성: `HIGH`
- CSP capacity 증설 가능성: `HIGH`
- 수치 근거: 없음
- 컨택 명분: 삼성SDS와 함께 추진하는 AI 에이전트 사업의 추론 인프라 비용 효율화를 위해 가속기 도입 검토를 제안합니다.
- 실제 컨택 시 사용할 말: 최근 귀행의 생성형 AI 에이전트 구축 사업 우선협상대상자 선정 소식을 접하였습니다. 구축을 담당할 파트너사와 연계하여 클라우드 및 온프레미스 환경에서 인프라 비용을 최적화할 수 있는 고성능 국산 가속기 도입 방안을 논의하고자 합니다.
- 매출 가능 시점: `단기`
- 담당자 후보 힌트: 디지털그룹장, 정보보호최고책임자, AI 에이전트 구축 프로젝트 PM, 정보기획부장
- 공개 프로필 URL: 확인 필요
- 기존 접점: `확인 필요`
- B2G 근거 유형: `해당 없음`
- 나라장터 직접 확인: `해당 없음`
- 조달상 다음 액션: 해당 없음
- 확인 필요: 삼성SDS 제안서 내 인프라 하드웨어 구성 사양 | 금융권 자체 인프라 내 가속기 직접 도입 허용 여부
- source_ids: S026, S028
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

6. **[선택 2026 강원] 골목골목 현장서 찾는 답 "해야 할 일 보일수록 설렌다...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T00:05:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.kado.net/news/articleView.html?idxno=2052090
   - summary_snippet: 우 후보는 "강릉과 동해 사이 AI 데이터센터 설립을 확정했다"며 "최대 70조원이 투자되는 국가 프로젝트다. 동해 예산이 7000억원 정도인데 70조 중 일부만 풀려도 동해는 대박나는 거 아니겠느냐"고 말했다. 현장 반응은...

7. **춘천시장 1번 공약 입맞춰 “산업·경제”⋯육동한 “첨단 융합 클러스...**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T00:05:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: https://www.kwnews.co.kr/page/view/2026052550122300000
   - summary_snippet: 육동한 후보는 선거관리위원회에 5대 공약을 제출하며 ‘바이오·AI·양자·데이터를 결합한 첨단 산업 융합... 정 후보는 수열에너지 클러스터와 연계한 데이터 센터 유치, 강원권 반도체 공동 연구소와 특화 인력 양성센터...

8. **통합특별시 성패, 결국 ‘기업 유치’에 달렸다**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T00:04:00+09:00`
   - matched_query_or_feed: `AI 데이터센터`
   - url: http://www.kwangju.co.kr/article.php?aid=1779721200799342131
   - summary_snippet: 막대한 전력이 소요되는 반도체, AI, 데이터센터에는 전남의 재생에너지를 공급할 수 있다. 미래모빌리티는 광주가 갖고 있는 자동차 산업 기반과 결합된다. KENTECH와 GIST 는 첨단 기업의 연구개발(R&D) 파트너가 된다....

9. **금융委 “망분리 규제 합리화 속도 낼 것” [2026 한국금융미래포럼]**
   - source: `naver_news_api`
   - published_at_kst: `2026-05-26T00:02:00+09:00`
   - matched_query_or_feed: `생성형 AI 도입 기업`
   - url: http://www.fntimes.com/html/view.php?ud=202605250721116305dd55077bc2_18
   - summary_snippet: 그동안 국내 금융회사들은 내부 업무망과 외부 인터넷망이 분리된 환경 탓에 생성형 AI와 클라우드 기반... 특히 금융회사들이 AI 도입 과정에서 가장 어려워하는 요인으로 거버넌스 부족을 꼽았다. AI 개발과 활용 전반을...

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
