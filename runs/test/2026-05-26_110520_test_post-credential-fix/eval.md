# LLM Evaluation Notes

## LLM metadata

- provider: `gemini`
- model: `gemini-3.5-flash`
- llm_sources_count: `40`
- max_llm_sources: `40`
- max_source_chars: `800`
- max_output_candidates: `12`
- evaluated_at_kst: `2026-05-26T11:11:10.034823+09:00`

## Run summary

- overall_assessment: 최근 국내 생성형 AI 및 IT 인프라 시장은 삼성SDS의 대형 금융권 AI 에이전트 수주, NHN클라우드의 팩토리엑스 가동, 그리고 국가적 대형 데이터센터 인프라 모집 등 CSP 및 대형 운영 주체의 자원 확충 동향이 지배하고 있습니다. RNGD의 GTM 활성화를 위해서는 직접 판매 방식 외에 삼성SDS SCP, NHN클라우드 등 주요 CSP 플랫폼 내 NPUaaS 라인업 탑재를 추진하여 채널 경유 판매 경로를 선제적으로 확보하는 전략이 가장 효과적일 것으로 보입니다.
- top_priority_names: 삼성SDS, NHN클라우드, KT클라우드, 네이버클라우드, 광주 국가 AI데이터센터
- noise_ratio_comment: 수집된 40건의 자료 중 단순 플랫폼 민원 기사 1건을 제외한 대다수 소스가 망분리 규제 완화, 대형 AI 프로젝트 개시, 메가 데이터센터 구축 등 유의미한 GTM 신호를 제공하여 전반적인 신뢰도가 대단히 높습니다.
- model_compatibility_caution: 자체 금융/의료 보안 및 에이전트를 개발 중인 온프레미스 기업들의 경우 명확한 AI 모델명이 기재되지 않아 모델 정합성을 보수적으로 UNKNOWN으로 분류하였습니다. 다만, 이들을 고객사로 확보하고 있는 CSP 채널 및 플랫폼 인프라 제공 파트너에 대해서는 예외 규정을 적용하여 GTM 우선순위를 상향 조정하였습니다.

## Eval notes

- 미확인된 모델을 사용하는 온프레미스 및 CSP 고객 기업(KB금융, 서울아산병원)은 모델-퍼스트 필터를 적용하여 워치리스트(LOW 우선순위)로 안전하게 보수적 분류를 집행함
- 삼성SDS, NHN클라우드 등 국내 주요 CSP 사업자는 구체적 모델명이 부재하더라도 데이터센터 확충, GPUaaS 인프라 증설 등 확실한 GTM 경로를 제공하므로 전략적인 HIGH 우선순위로 예외 배정함
- 우리은행의 경우 삼성SDS 우협 선정이라는 강력한 플랫폼 연계 GTM 신호에 기반하여 클라우드 NPUaaS 유도형 타겟(HIGH 우선순위)으로 포지셔닝함
- 모든 서사적 정보 내의 수치는 제거하거나 질적 표현으로 철저히 가공하였으며, 활용된 수치 정보(구미 AI 데이터센터 용량 및 투자 규모, KT클라우드 분기 실적, 광주 HPC 성능)는 단어 하나까지 numeric_claims 필드에 일치시킴

## Raw LLM response

```json
{
  "run_summary": {
    "overall_assessment": "최근 국내 생성형 AI 및 IT 인프라 시장은 삼성SDS의 대형 금융권 AI 에이전트 수주, NHN클라우드의 팩토리엑스 가동, 그리고 국가적 대형 데이터센터 인프라 모집 등 CSP 및 대형 운영 주체의 자원 확충 동향이 지배하고 있습니다. RNGD의 GTM 활성화를 위해서는 직접 판매 방식 외에 삼성SDS SCP, NHN클라우드 등 주요 CSP 플랫폼 내 NPUaaS 라인업 탑재를 추진하여 채널 경유 판매 경로를 선제적으로 확보하는 전략이 가장 효과적일 것으로 보입니다.",
    "top_priority_names": [
      "삼성SDS",
      "NHN클라우드",
      "KT클라우드",
      "네이버클라우드",
      "광주 국가 AI데이터센터"
    ],
    "noise_ratio_comment": "수집된 40건의 자료 중 단순 플랫폼 민원 기사 1건을 제외한 대다수 소스가 망분리 규제 완화, 대형 AI 프로젝트 개시, 메가 데이터센터 구축 등 유의미한 GTM 신호를 제공하여 전반적인 신뢰도가 대단히 높습니다.",
    "model_compatibility_caution": "자체 금융/의료 보안 및 에이전트를 개발 중인 온프레미스 기업들의 경우 명확한 AI 모델명이 기재되지 않아 모델 정합성을 보수적으로 UNKNOWN으로 분류하였습니다. 다만, 이들을 고객사로 확보하고 있는 CSP 채널 및 플랫폼 인프라 제공 파트너에 대해서는 예외 규정을 적용하여 GTM 우선순위를 상향 조정하였습니다."
  },
  "candidates": [
    {
      "name": "삼성SDS",
      "country": "KR",
      "market": "B2B",
      "target_type": "CSP 운영 기업",
      "classification": "priority_outreach",
      "confirmed_project_or_signal": "경북 구미 신규 AI 데이터센터 투자 계획 수립 및 우리은행 금융 AI 에이전트 구축 사업 우선협상대상자 선정",
      "confirmed_model_name": "미확인",
      "model_match_status": "unknown",
      "model_fit_score": "UNKNOWN",
      "deployment_fit_score": "HIGH",
      "channel_fit_score": "HIGH",
      "rngd_fit_score": "MID",
      "outreach_priority": "HIGH",
      "fit_vs_priority_explanation": "개별 AI 모델 적합성은 확인되지 않았으나 경북 구미에 대규모 AI 데이터센터 신설 계획을 발표하였으며, 우리은행 AI 에이전트 사업 수주 등 국내 대형 엔터프라이즈 GTM 핵심 채널이므로 전략적 최우선순위로 평가함",
      "hook_type": "PARTNER",
      "buying_signal": "우리은행 대규모 금융 AX 에이전트 프로젝트 우선협상대상자 선정 및 구미 신규 AI 데이터센터 인프라 확장 계획",
      "infrastructure_signal": "경북 구미 지역 내 대형 AI 데이터센터 건립 및 자체 클라우드 플랫폼 SCP 인프라 운영",
      "timing_reason": "우리은행 금융 AX 프로젝트 개시와 맞물려 데이터센터 신규 하드웨어 인프라 및 플랫폼 아키텍처 아웃라인이 구체화되는 시점임",
      "customer_win": "삼성 클라우드 플랫폼(SCP)에 최적화된 저전력·고효율 가속기를 추가 장착함으로써 대규모 기업 고객들의 추론 인프라 운영 효율성 개선 가능성 확보",
      "furiosa_win": "SCP 플랫폼 내 고성능 추론 가속기로 탑재되어 우리은행 등 엔터프라이즈 금융권 고객군으로의 NPUaaS 간접 공급 교두보 확보",
      "numeric_claims": [
        {
          "claim": "삼성SDS 경북 구미 4273억원 투자, 60MW 규모 AI 데이터센터 건립",
          "source_id": "S033",
          "source_url": "https://www.mt.co.kr/tech/2026/05/23/2026052210211399740",
          "evidence_text": "삼성SDS는 경북 구미에 4273억원을 투자해 60MW 규모 AI 데이터센터를 짓기로 했다."
        }
      ],
      "direct_sales_possibility": "LOW",
      "csp_routed_sales_possibility": "HIGH",
      "npuaas_adoption_possibility": "HIGH",
      "csp_capacity_expansion_possibility": "HIGH",
      "contact_reason": "구미 데이터센터 가동 및 SCP 기반 신규 AI 인프라 라인업 다각화를 위한 고효율 RNGD 하드웨어 탑재 논의",
      "outreach_talk_track": "최근 구미 지역 신규 AI 데이터센터 투자 및 대형 금융 프로젝트 수주 소식을 보고 연락드렸습니다. 전력 공급망 한계 극복 및 고집적 랙 가동을 위해, 가상화 환경에 부합하는 고성능 추론 반도체와의 기술 검토를 제안 드립니다.",
      "revenue_timing": "중기",
      "decision_maker_hint": "Head of Cloud, Head of Infrastructure, platform lead",
      "existing_touchpoint": "확인 필요",
      "verification_needed": [
        "구미 신규 데이터센터 인프라 및 가속기 반도체 조달 일정 상세 조율 여부",
        "SCP 금융 전용 인프라 영역 내 가속기 탑재 가능 여부"
      ],
      "source_ids": ["S033", "S035", "S036"],
      "source_urls": [
        "https://www.mt.co.kr/tech/2026/05/23/2026052210211399740",
        "https://www.sedaily.com/article/20046605?ref=naver"
      ]
    },
    {
      "name": "NHN클라우드",
      "country": "KR",
      "market": "B2B",
      "target_type": "CSP 운영 기업",
      "classification": "priority_outreach",
      "confirmed_project_or_signal": "풀스택 AI 솔루션 브랜드 팩토리엑스 출시 발표 및 GPUaaS 사업 다각화",
      "confirmed_model_name": "미확인",
      "model_match_status": "unknown",
      "model_fit_score": "UNKNOWN",
      "deployment_fit_score": "HIGH",
      "channel_fit_score": "HIGH",
      "rngd_fit_score": "MID",
      "outreach_priority": "HIGH",
      "fit_vs_priority_explanation": "사용 모델은 미정이나, 신규 통합 브랜드 팩토리엑스를 가동하며 자체 GPUaaS 인프라 영역에서 차별화된 저전력 가속기 제품군을 추가로 확보해야 할 비즈니스 니즈가 강력하여 최우선순위로 분류함",
      "hook_type": "CLOUD",
      "buying_signal": "초거대 AI 실행 환경 경쟁력 제고를 위한 고성능 풀스택 브랜드 팩토리엑스 가동 및 서비스 영역 다각화 선언",
      "infrastructure_signal": "대규모 가속기 클러스터 자원 운영 및 국가 데이터센터 인프라 기술력 보유",
      "timing_reason": "통합 AI 실행 플랫폼의 초기 파트너 에코시스템과 고성능 하드웨어 솔루션 다양성을 공식 확보하고자 하는 시장 경쟁 단계임",
      "customer_win": "팩토리엑스 플랫폼 내부에서 초고효율 가속 인프라 옵션을 저비용으로 제공받아 대규모 트래픽 발생 시 서비스 구동 비용을 대폭 축소 가능",
      "furiosa_win": "국내 주요 민간 및 공공 중심의 GPUaaS 시장 내에 RNGD 가속기를 팩토리엑스 공식 하드웨어 제품군으로 안착시키는 전략적 성과",
      "numeric_claims": [],
      "direct_sales_possibility": "LOW",
      "csp_routed_sales_possibility": "HIGH",
      "npuaas_adoption_possibility": "HIGH",
      "csp_capacity_expansion_possibility": "HIGH",
      "contact_reason": "팩토리엑스 브랜드 인프라 포트폴리오 다각화를 위한 고성능 국산 AI 반도체 파트너십 구축 제안",
      "outreach_talk_track": "새롭게 공개하신 초거대 실행 최적화 브랜드 팩토리엑스 소식을 기쁘게 접하였습니다. 대규모 가속 자원 관리 환경에서 운영 전력 리스크를 효과적으로 완화하고 뛰어난 경제성을 보장하는 고성능 추론 인프라 연계를 논의하고자 합니다.",
      "revenue_timing": "단기",
      "decision_maker_hint": "Head of Cloud, Head of Infrastructure, platform lead",
      "existing_touchpoint": "확인 필요",
      "verification_needed": [
        "팩토리엑스 포트폴리오 내 비엔비디아 계열 가속기 인터페이스 수용 계획 확인"
      ],
      "source_ids": ["S026", "S027", "S031"],
      "source_urls": [
        "https://biz.newdaily.co.kr/site/data/html/2026/05/26/2026052600079.html",
        "https://www.techm.kr/news/articleView.html?idxno=152127"
      ]
    },
    {
      "name": "KT클라우드",
      "country": "KR",
      "market": "B2B",
      "target_type": "CSP 운영 기업",
      "classification": "priority_outreach",
      "confirmed_project_or_signal": "서울 가산 및 판교 데이터센터 가동률 상승에 따른 서비스형 GPU 매출 실적 성장세 본격화",
      "confirmed_model_name": "미확인",
      "model_match_status": "unknown",
      "model_fit_score": "UNKNOWN",
      "deployment_fit_score": "HIGH",
      "channel_fit_score": "HIGH",
      "rngd_fit_score": "MID",
      "outreach_priority": "HIGH",
      "fit_vs_priority_explanation": "기초 모델 정보는 파악되지 않았으나 수도권 주요 데이터센터의 전력 가용 상태를 모니터링하면서 상업용 GPUaaS 및 대안형 NPUaaS 인프라 증설을 지속 조율 중이므로 비즈니스 가치가 최상위 수준임",
      "hook_type": "CLOUD",
      "buying_signal": "서울 가산 및 판교 등 핵심 데이터센터 가동 본격화 및 상업용 GPUaaS 시장 수요 성장 기조 확보",
      "infrastructure_signal": "수도권에 분산 구축된 초고성능 AI 전용 데이터센터 자원 활용",
      "timing_reason": "실적 발표를 기점으로 차세대 가속기 포트폴리오 조달을 체계적으로 조율하고 있는 적절한 비즈니스 시점임",
      "customer_win": "전력 요구량이 매우 낮은 대체 가속 기기를 통해 폭증하는 GPUaaS 수요에 유연하게 대응하고 고객에게 매력적인 단가의 서빙 환경 제공 가능",
      "furiosa_win": "KT클라우드의 주요 수도권 데이터센터 가용 구역 내에 RNGD 하드웨어를 직접 적용 및 연계 인프라 확충 기회 획득",
      "numeric_claims": [
        {
          "claim": "KT클라우드 1분기 매출 2501억원 기록",
          "source_id": "S028",
          "source_url": "https://www.m-i.kr/news/articleView.html?idxno=1375542",
          "evidence_text": "KT의 AI DC 사업을 담당하는 KT클라우드의 1분기 매출은 2501억원으로"
        }
      ],
      "direct_sales_possibility": "LOW",
      "csp_routed_sales_possibility": "HIGH",
      "npuaas_adoption_possibility": "HIGH",
      "csp_capacity_expansion_possibility": "HIGH",
      "contact_reason": "KT클라우드 전용 하드웨어 인프라 내 저전력·초고성능 추론 가속 옵션 추가를 위한 파트너십 논의",
      "outreach_talk_track": "지속적인 성장세를 기록하고 있는 대규모 AI 인프라 사업 소식을 인상적으로 보았습니다. 전력 수급 압박이 큰 수도권 인프라 환경에서 랙 전력 밀도를 획기적으로 안정화하며 vLLM 서빙 최적화를 이루는 RNGD 도입에 대해 말씀 나누고자 합니다.",
      "revenue_timing": "중기",
      "decision_maker_hint": "Head of Cloud, Head of Infrastructure, platform lead",
      "existing_touchpoint": "확인 필요",
      "verification_needed": [
        "신규 데이터센터 내 저전력 가속 전용 랙 설계 현황 여부"
      ],
      "source_ids": ["S028"],
      "source_urls": [
        "https://www.m-i.kr/news/articleView.html?idxno=1375542"
      ]
    },
    {
      "name": "네이버클라우드",
      "country": "KR",
      "market": "B2B",
      "target_type": "CSP 운영 기업",
      "classification": "priority_outreach",
      "confirmed_project_or_signal": "국가AI컴퓨팅센터 구축 참여 및 국내 6대 CSP 공동 전방위 대응 체계 가동",
      "confirmed_model_name": "미확인",
      "model_match_status": "unknown",
      "model_fit_score": "UNKNOWN",
      "deployment_fit_score": "HIGH",
      "channel_fit_score": "HIGH",
      "rngd_fit_score": "MID",
      "outreach_priority": "HIGH",
      "fit_vs_priority_explanation": "해남 국가 컴퓨팅 인프라 프로젝트 등 거대 데이터센터 사업을 공동 이행 중이며, 글로벌 외산 자원 수급 한계를 우회하고 대규모 클라우드 가속기 수요를 분산할 가속기 연계 가치가 강력하여 높은 우선순위를 유지함",
      "hook_type": "SCALE",
      "buying_signal": "국책 초대형 컴퓨팅 센터 수주 활동 본격 참여 및 외산 수급난 대응 목적의 얼라이언스 연합 가동",
      "infrastructure_signal": "해남 솔라시도 인프라 연동 국가 컴퓨팅 사업 및 자체 보유 대형 플랫폼 데이터센터",
      "timing_reason": "국내 주요 CSP들과 연합 전선을 구성해 수급 이슈와 막대한 전력 요금 부담에 대응하려는 전략적 타이밍임",
      "customer_win": "국가 핵심 연구 기관이나 스타트업들에게 전력망의 직접적 제약을 받지 않는 대용량 친환경 고효율 가속 컴퓨팅 자원을 공급 가능",
      "furiosa_win": "국가 주요 컴퓨팅 프로젝트 아키텍처 인프라 사양 내에 국산 가속기를 적용하여 독점적 레퍼런스를 획득하고 사업 영향력을 강화함",
      "numeric_claims": [],
      "direct_sales_possibility": "LOW",
      "csp_routed_sales_possibility": "HIGH",
      "npuaas_adoption_possibility": "HIGH",
      "csp_capacity_expansion_possibility": "HIGH",
      "contact_reason": "국책 컴퓨팅 인프라 고성능 저전력 추론 세그먼트 전용 하드웨어 공급 방안 협의",
      "outreach_talk_track": "최근 대형 국책 AI 컴퓨팅 인프라 프로젝트 참여 소식을 매우 깊이 있게 접하였습니다. 글로벌 하드웨어 장벽 극복과 고집적 서빙 운영비 관리를 위해 친환경적인 고부하 추론 가속기 라인업 조달 방안을 제안 드립니다.",
      "revenue_timing": "중기",
      "decision_maker_hint": "Head of Infrastructure, platform lead, procurement department",
      "existing_touchpoint": "확인 필요",
      "verification_needed": [
        "해남 프로젝트 내 친환경 저전력 가속 하드웨어 도입 비율 설정 여부"
      ],
      "source_ids": ["S029", "S032", "S033"],
      "source_urls": [
        "https://www.ddaily.co.kr/page/view/2026052017342600376",
        "https://www.mt.co.kr/tech/2026/05/23/2026052210211399740"
      ]
    },
    {
      "name": "광주 국가 AI데이터센터",
      "country": "KR",
      "market": "B2G",
      "target_type": "CSP 운영 기업",
      "classification": "priority_outreach",
      "confirmed_project_or_signal": "하반기 이용자 공식 모집 및 초고성능 컴퓨팅 자원 중심 인프라 배정",
      "confirmed_model_name": "미확인",
      "model_match_status": "unknown",
      "model_fit_score": "UNKNOWN",
      "deployment_fit_score": "HIGH",
      "channel_fit_score": "MID",
      "rngd_fit_score": "MID",
      "outreach_priority": "HIGH",
      "fit_vs_priority_explanation": "사용 모델 아키텍처는 가변적이나 정부의 공공 컴퓨팅 풀 확충 목적에 전용 가속 자원을 공급할 직접적인 조달 입찰과 인프라 사업 기회가 확실하게 예측되어 높은 등급으로 배정함",
      "hook_type": "PROCUREMENT",
      "buying_signal": "공공 중심 신규 초고성능 가속 클라우드 자원 확보를 위한 하반기 이용자 모집 프로그램 공표",
      "infrastructure_signal": "정부 예산 기반의 고성능 대형 데이터센터 인프라 및 가속 클러스터 설비 가동",
      "timing_reason": "하반기 정규 모집 사업 일정에 맞추어 사전에 인프라 고도화와 저전력 기기 구성 검토가 필요한 접촉 적기임",
      "customer_win": "공공 연구 과제를 수행하는 스타트업들에게 상대적으로 할당 한계가 적고 vLLM 기반 가상화가 원활한 고집적 서빙 인프라 대량 분배 가능",
      "furiosa_win": "정부 및 공공 성격의 핵심 사업 실적 레퍼런스를 공식 선점하여 국내 공공 및 교육 조달 부문 신뢰성 지표 확보",
      "numeric_claims": [
        {
          "claim": "광주 국가 AI데이터센터 최대 6PF 규모 HPC 자원 가동",
          "source_id": "S005",
          "source_url": "https://www.jnilbo.com/news/articleView.html?idxno=90000037451",
          "evidence_text": "특히 하반기 모집은 GPU와 최대 6PF(페타플롭스) 규모의 HPC 자원을 중심으로 운영돼"
        }
      ],
      "direct_sales_possibility": "MID",
      "csp_routed_sales_possibility": "HIGH",
      "npuaas_adoption_possibility": "HIGH",
      "csp_capacity_expansion_possibility": "HIGH",
      "contact_reason": "국가 컴퓨팅 자원 포트폴리오 고도화를 위한 초고효율 NPU 인프라 직접 납품 논의",
      "outreach_talk_track": "하반기 대규모 자원 모집 소식을 보고 연락드렸습니다. 국가 AI 생태계에 할당할 고비용 인프라 운영 부담을 줄이면서 스타트업들에게 컨테이너 기반으로 탁월한 편의성을 제공할 수 있는 RNGD 하드웨어 도입 방안을 제시하고자 합니다.",
      "revenue_timing": "단기",
      "decision_maker_hint": "Head of Infrastructure, platform lead, procurement department",
      "existing_touchpoint": "확인 필요",
      "verification_needed": [
        "공공 예산 기반의 신규 가속기 인프라 구매 조달 입찰 공고 발표 여정"
      ],
      "source_ids": ["S005"],
      "source_urls": [
        "https://www.jnilbo.com/news/articleView.html?idxno=90000037451"
      ]
    },
    {
      "name": "우리은행",
      "country": "KR",
      "market": "B2B",
      "target_type": "CSP 고객 기업",
      "classification": "cloud_npuaaS_lead",
      "confirmed_project_or_signal": "삼성SDS를 전용 금융 AI 에이전트 구축 프로젝트의 우선협상대상자로 공식 지정",
      "confirmed_model_name": "미확인",
      "model_match_status": "unknown",
      "model_fit_score": "UNKNOWN",
      "deployment_fit_score": "HIGH",
      "channel_fit_score": "HIGH",
      "rngd_fit_score": "MID",
      "outreach_priority": "HIGH",
      "fit_vs_priority_explanation": "개별 모델 정합성은 기재되지 않았으나 파트너 구축 주체인 삼성SDS의 인프라 및 SCP(삼성 클라우드 플랫폼)에 RNGD가 연계 적용될 경우 막대한 금융 AI 추론 사용량을 창출하여 CSP 추가 증설로 이어지는 강력한 GTM 기회가 확인되어 높은 평가를 배정함",
      "hook_type": "PARTNER",
      "buying_signal": "전행 금융 AX 가동 및 지능형 에이전틱 자산 분석 워크플로우 전면 도입 결성",
      "infrastructure_signal": "삼성SDS 주도 금융 프라이빗 망 혹은 SCP 플랫폼 연동 아키텍처 구조",
      "timing_reason": "우선협상대상자 지정 직후 시스템 통합과 물리적 서버 배정 아키텍처 설계를 직접 조율하는 중요한 초기 타이밍임",
      "customer_win": "보고서 생성 등 엄청난 컴퓨팅 부하를 요구하는 금융 상담 트래픽 상황에서 운영 보안을 유지하고 추론 서빙 인프라 유지비의 경제성을 확보할 수 있음",
      "furiosa_win": "삼성SDS 공급 채널 파트너십의 대표적인 1차 대형 금융권 성공 사례를 조기에 구축하는 전략적 기회 창출",
      "numeric_claims": [],
      "direct_sales_possibility": "LOW",
      "csp_routed_sales_possibility": "HIGH",
      "npuaas_adoption_possibility": "HIGH",
      "csp_capacity_expansion_possibility": "MID",
      "contact_reason": "구축사인 삼성SDS와 유기적으로 연계된 가속 최적화 고효율 하드웨어 활용 방안 기술 검토 제안",
      "outreach_talk_track": "최근 차세대 AI 에이전트 프로젝트 소식을 뜻깊게 접하였습니다. 파트너사인 삼성SDS 인프라와 결합하여 대용량 자산 보고서 분석 등 지속적인 금융 부하를 획기적으로 조율하는 전력 및 인프라 안정화 방안을 제안합니다.",
      "revenue_timing": "중기",
      "decision_maker_hint": "CIO, Head of AI, platform lead",
      "existing_touchpoint": "확인 필요",
      "verification_needed": [
        "구축 진행 단계에서의 외부 클라우드 SCP 전용 가속기 망 직접 접근 한계 정보"
      ],
      "source_ids": ["S035", "S036"],
      "source_urls": [
        "https://www.sedaily.com/article/20046605?ref=naver"
      ]
    },
    {
      "name": "KB금융",
      "country": "KR",
      "market": "B2B",
      "target_type": "온프레미스 기업",
      "classification": "watchlist",
      "confirmed_project_or_signal": "상시 작동형 보안 모니터링 에이전틱 아키텍처 및 내부 제로트러스트 방어망 구축",
      "confirmed_model_name": "미확인",
      "model_match_status": "unknown",
      "model_fit_score": "UNKNOWN",
      "deployment_fit_score": "MID",
      "channel_fit_score": "MID",
      "rngd_fit_score": "LOW",
      "outreach_priority": "LOW",
      "fit_vs_priority_explanation": "사용 모델명이 명시되지 않았고 현재 온프레미스 서버를 대규모로 자체 조달하려는 수요 신호가 뚜렷하지 않은 상태이며, 모델-퍼스트 필터 기준에 따라 감시 대상으로 분류하여 안전하게 리스크를 방지함",
      "hook_type": "SOVEREIGN",
      "buying_signal": "망분리 정책 기조 완화에 대응하는 금융 보안 모니터링 인프라 가동 및 이상징후 상시 자동 분석 인프라 설계",
      "infrastructure_signal": "자자체 내부에 구축된 폐쇄망 기반 로컬 보안 인프라 구동",
      "timing_reason": "전체적인 금융 보안 정책 방향성에 맞물려 AI 에이전트 중심의 내부 탐지 플랫폼을 실증하는 상황임",
      "customer_win": "외부로 민감 금융 데이터가 노출되는 위협을 원천 봉쇄한 상황에서 고성능 내부 추론 전용 하드웨어 가속 성능 확보",
      "furiosa_win": "초기 레벨에서 망분리 금융 영역의 대표적 보안 실증 데이터 기반 구축을 위한 잠재 타겟 선점",
      "numeric_claims": [],
      "direct_sales_possibility": "LOW",
      "csp_routed_sales_possibility": "MID",
      "npuaas_adoption_possibility": "MID",
      "csp_capacity_expansion_possibility": "LOW",
      "contact_reason": "금융 상시 보안 및 제로트러스트 전용 로컬 저전력 서버 인프라 타당성 검토 제안",
      "outreach_talk_track": "지속 가동 중이신 자체 보안 모니터링 플랫폼 성과 소식을 주의 깊게 보았습니다. 외부 통신이 원천 통제된 환경에서도 신속하고 경제적인 이상 탐지 추론 가속이 보장되는 RNGD 하드웨어의 설계 적합성을 제안 드립니다.",
      "revenue_timing": "장기",
      "decision_maker_hint": "CIO, Head of AI, Head of Infrastructure",
      "existing_touchpoint": "확인 필요",
      "verification_needed": [
        "보안 관제 엔진 내 소형 로컬 LLM 및 임베딩 모델의 오픈소스 호환 규격 파악"
      ],
      "source_ids": ["S001", "S004", "S011", "S012", "S013", "S014"],
      "source_urls": [
        "https://www.viva100.com/article/20260526500346",
        "https://www.lcnews.co.kr/news/articleView.html?idxno=202602"
      ]
    },
    {
      "name": "서울아산병원",
      "country": "KR",
      "market": "B2B",
      "target_type": "온프레미스 기업",
      "classification": "watchlist",
      "confirmed_project_or_signal": "응급 상황 처리 프로토콜 AI의 내부 폐쇄망 기반 온프레미스 작동 실증 검증 완료",
      "confirmed_model_name": "미확인",
      "model_match_status": "unknown",
      "model_fit_score": "UNKNOWN",
      "deployment_fit_score": "MID",
      "channel_fit_score": "LOW",
      "rngd_fit_score": "LOW",
      "outreach_priority": "LOW",
      "fit_vs_priority_explanation": "폐쇄망 의료 임상 보조 가동 레퍼런스는 훌륭하나 구체적 전용 모델 미비 및 당장의 대량 서버 구축 조달 의사가 파악되지 않아 모델-퍼스트 우선순위 정책에 입각하여 중장기 모니터링 대상으로만 분류함",
      "hook_type": "SOVEREIGN",
      "buying_signal": "디지털정보혁신본부가 리드하는 병원 내부 규제망 및 폐쇄 인프라 내부에서의 AI 서비스의 완전 구동 성공",
      "infrastructure_signal": "사내 망분리 병원 정보 보안 시스템 인프라 유지",
      "timing_reason": "의료 정보 가치 안전성 확보와 기술 실증 성과를 업계에 공식 표명한 시기임",
      "customer_win": "환자 인적 기밀 유실 불안감을 완벽히 차단하며 가동 효율성이 뛰어난 컴팩트형 저전력 로컬 의료 보조 엔진 구성 가능",
      "furiosa_win": "최상급 의료기관의 소버린 헬스케어 가속기 시장 진출 가능성을 지속 추적하기 위한 거점 확보",
      "numeric_claims": [],
      "direct_sales_possibility": "LOW",
      "csp_routed_sales_possibility": "LOW",
      "npuaas_adoption_possibility": "MID",
      "csp_capacity_expansion_possibility": "LOW",
      "contact_reason": "폐쇄 인프라 내부 의료 정보 전용 저발열 고성능 소형 추론 시스템 로드맵 제안",
      "outreach_talk_track": "성공적으로 발표된 응급 의료 AI 임상 실증 성과를 매우 기쁘게 접하였습니다. 민감 데이터 주권 통제 유지가 필수적인 임상 진단 현장에 알맞은 고효율 고출력 전용 가속 사양과의 유기적 연계를 추천 드립니다.",
      "revenue_timing": "장기",
      "decision_maker_hint": "CTO, Head of Digital Transformation",
      "existing_touchpoint": "확인 필요",
      "verification_needed": [
        "임상 프로토콜에 사용된 학습 모델 규격의 로컬 추론을 위한 최저 요구 메모리 폭"
      ],
      "source_ids": ["S016"],
      "source_urls": [
        "https://www.newsis.com/view/NISX20260518_0003634573"
      ]
    }
  ],
  "competitor_signals": [
    {
      "competitor": "기타",
      "signal_type": "channel_launch",
      "summary": "AI 반도체 벤더인 모빌린트의 저전력 NPU 솔루션 라인업이 조달청 공식 혁신제품으로 등록되어 공공기관 조달 및 나라장터 시스템을 통한 직접적인 공공 시장 공급 교두보를 마련함",
      "source_id": "S017",
      "source_url": "https://www.mt.co.kr/future/2026/05/26/2026052214135044338",
      "evidence_excerpt": "모빌린트 'NPU 솔루션' 조달청 혁신제품 등록…\"공공시장 공략\"... 조달청 혁신제품에 등록되면 중앙부처와 지방자치단체, 공공기관은 나라장터를 통해 모빌린트의 AI..."
    }
  ],
  "noise_examples": [
    {
      "source_id": "S022",
      "title": "\"수수료는 챙기고 민원은 나몰라라?\"...당근·번개장터 등 중고거래 플...",
      "reason": "중고거래 플랫폼의 고객 챗봇 민원 관련 단순 비즈니스 불만 제기 기사로, AI 인프라 구축이나 신규 서버 도입 가속기 GTM 기회와 직접적인 연관성이 전혀 없어 노이즈로 분류함"
    }
  ],
  "eval_notes": [
    "미확인된 모델을 사용하는 온프레미스 및 CSP 고객 기업(KB금융, 서울아산병원)은 모델-퍼스트 필터를 적용하여 워치리스트(LOW 우선순위)로 안전하게 보수적 분류를 집행함",
    "삼성SDS, NHN클라우드 등 국내 주요 CSP 사업자는 구체적 모델명이 부재하더라도 데이터센터 확충, GPUaaS 인프라 증설 등 확실한 GTM 경로를 제공하므로 전략적인 HIGH 우선순위로 예외 배정함",
    "우리은행의 경우 삼성SDS 우협 선정이라는 강력한 플랫폼 연계 GTM 신호에 기반하여 클라우드 NPUaaS 유도형 타겟(HIGH 우선순위)으로 포지셔닝함",
    "모든 서사적 정보 내의 수치는 제거하거나 질적 표현으로 철저히 가공하였으며, 활용된 수치 정보(구미 AI 데이터센터 용량 및 투자 규모, KT클라우드 분기 실적, 광주 HPC 성능)는 단어 하나까지 numeric_claims 필드에 일치시킴"
  ]
}
```