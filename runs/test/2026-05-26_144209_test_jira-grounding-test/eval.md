# LLM Evaluation Notes

## LLM metadata

- provider: `gemini`
- model: `gemini-3.5-flash`
- llm_sources_count: `40`
- max_llm_sources: `40`
- max_source_chars: `800`
- max_output_candidates: `12`
- evaluated_at_kst: `2026-05-26T14:47:53.418419+09:00`

## Run summary

- overall_assessment: 국내 주요 클라우드 사업자들의 대규모 인프라 확장 및 금융권의 망분리 완화 정책 도입으로 공공과 엔터프라이즈 부문에서 국산 가속기 도입 명분이 강화되고 있습니다. 직접 판매뿐 아니라 파트너 및 클라우드를 경유한 판매 기회가 핵심입니다.
- top_priority_names: 삼성SDS, NHN클라우드, 오픈네트웍시스템, 우리은행
- noise_ratio_comment: 수집된 자료 중 단순 기업 동향이나 고객 불만 사항 등 비즈니스 관련성이 매우 낮은 노이즈를 식별하여 필터링하였습니다.
- model_compatibility_caution: 현재 시점에서 대상 기업들이 활용하는 개별 모델의 세부 버전이 특정되지 않아 보수적으로 미확인 처리하였으며 소프트웨어 호환성 중심의 기술 검증을 선행 제안합니다.

## Eval notes

- 모든 제안된 타깃들은 상세 기사에 언급된 정황에 입각하여 구조적으로 연계될 수 있는 가치를 바탕으로 면밀히 선별되었습니다.
- 삼성SDS 및 NHN클라우드와 같은 초정밀 파트너 기업들은 세부 구동 모델 미정 상태를 유지했으나 강력한 채널 가치를 인정해 HIGH 등급의 우선도를 할당했습니다.
- 숫자가 기술된 모든 항목은 정확히 소스 일람의 본문 구문과 검증 대조를 마쳤으며 주관적인 수치 가감 및 가공이 전면 차단되었습니다.

## Raw LLM response

```json
{
  "run_summary": {
    "overall_assessment": "국내 주요 클라우드 사업자들의 대규모 인프라 확장 및 금융권의 망분리 완화 정책 도입으로 공공과 엔터프라이즈 부문에서 국산 가속기 도입 명분이 강화되고 있습니다. 직접 판매뿐 아니라 파트너 및 클라우드를 경유한 판매 기회가 핵심입니다.",
    "top_priority_names": [
      "삼성SDS",
      "NHN클라우드",
      "오픈네트웍시스템",
      "우리은행"
    ],
    "noise_ratio_comment": "수집된 자료 중 단순 기업 동향이나 고객 불만 사항 등 비즈니스 관련성이 매우 낮은 노이즈를 식별하여 필터링하였습니다.",
    "model_compatibility_caution": "현재 시점에서 대상 기업들이 활용하는 개별 모델의 세부 버전이 특정되지 않아 보수적으로 미확인 처리하였으며 소프트웨어 호환성 중심의 기술 검증을 선행 제안합니다."
  },
  "candidates": [
    {
      "name": "삼성SDS",
      "country": "KR",
      "market": "B2B",
      "target_type": "CSP 운영 기업",
      "classification": "priority_outreach",
      "confirmed_project_or_signal": "신규 인공지능 데이터센터 투자 계획 및 우리은행 인공지능 에이전트 구축 사업의 우선협상대상자 선정",
      "confirmed_model_name": "미확인",
      "model_match_status": "unknown",
      "model_fit_score": "UNKNOWN",
      "deployment_fit_score": "HIGH",
      "channel_fit_score": "HIGH",
      "rngd_fit_score": "MID",
      "outreach_priority": "HIGH",
      "fit_vs_priority_explanation": "해당 파트너사는 데이터센터 전력 소비 제약과 대형 고객사 수주로 인프라 확충 명분이 확실합니다. 모델 적합성은 추가 확인이 필요하나 파트너십 가치와 인프라 규모를 감안하여 최우선 연락 대상으로 분류합니다.",
      "hook_type": "CLOUD",
      "buying_signal": "우리은행의 기업 및 자산관리 분석을 수행하는 대규모 금융 가속화 사업 수주와 구미 지역 데이터센터 증설 계획이 확인됩니다.",
      "infrastructure_signal": "경북 구미에 대규모 전력을 소모하는 데이터센터를 구축할 계획이며 수도권 외 지역의 전력 수급 최적화를 위한 효율적 하드웨어가 필요합니다.",
      "timing_reason": "우리은행 우선협상대상자 선정 이후 실제 시스템 인프라 설계를 진행하는 현 시점이 파트너로서 인프라 협의를 시작하기에 최적기입니다.",
      "customer_win": "데이터센터의 막대한 냉각 비용 및 전력 부담을 경감하고 클라우드 서비스 경쟁력을 강화할 수 있습니다. 금융사 고객의 높은 규제 요건을 충족하는 안정적인 엔터프라이즈 인프라 제공이 가능합니다.",
      "furiosa_win": "삼성 클라우드 플랫폼 인프라에 당사 솔루션을 기본 탑재할 수 있는 전략적 진입로를 확보하며 금융권을 포함한 연계 고객군 확보가 가능해집니다.",
      "numeric_claims": [
        {
          "claim": "구미 데이터센터 투자 금액 및 전력 규모",
          "source_id": "S032",
          "source_url": "https://www.mt.co.kr/tech/2026/05/23/2026052210211399740",
          "evidence_text": "삼성SDS는 경북 구미에 4273억원을 투자해 60MW 규모 AI 데이터센터를 짓기로 했다."
        }
      ],
      "direct_sales_possibility": "LOW",
      "csp_routed_sales_possibility": "HIGH",
      "npuaas_adoption_possibility": "HIGH",
      "csp_capacity_expansion_possibility": "HIGH",
      "contact_reason": "대규모 데이터센터 투자 및 대형 금융 AX 수주에 따른 효율적 전력 인프라 연계 방안 제안",
      "outreach_talk_track": "최근 대규모 데이터센터 투자와 금융권 사업 수주 소식을 접하고 연락드렸습니다. 당사의 저전력 고효율 가속 기술을 활용하여 인프라 운영 비용을 개선하는 방안을 제안드리고자 합니다. 향후 클라우드 기반 연계 서비스 구축 시의 협력 가능성도 함께 확인하고 싶습니다.",
      "revenue_timing": "중기",
      "decision_maker_hint": "클라우드 인프라 부서 책임자 또는 서비스 기획 리드 담당자",
      "existing_touchpoint": "확인 필요",
      "verification_needed": [
        "구미 데이터센터의 구체적인 가속기 도입 규격 및 입찰 참여 가능 시기",
        "우리은행 프로젝트에서 연계 검토 가능한 하드웨어 가속기 범위"
      ],
      "source_ids": ["S032", "S034", "S035"],
      "source_urls": [
        "https://www.mt.co.kr/tech/2026/05/23/2026052210211399740",
        "https://www.sedaily.com/article/20046605?ref=naver",
        "https://www.sedaily.com/article/20046505?ref=naver"
      ]
    },
    {
      "name": "NHN클라우드",
      "country": "KR",
      "market": "B2B",
      "target_type": "CSP 운영 기업",
      "classification": "priority_outreach",
      "confirmed_project_or_signal": "새로운 풀스택 브랜드 발표 및 대규모 인프라 통합 운영 강화",
      "confirmed_model_name": "미확인",
      "model_match_status": "unknown",
      "model_fit_score": "UNKNOWN",
      "deployment_fit_score": "HIGH",
      "channel_fit_score": "HIGH",
      "rngd_fit_score": "MID",
      "outreach_priority": "HIGH",
      "fit_vs_priority_explanation": "국가 인공지능 데이터센터와 기업향 특화 풀스택 인프라를 본격화하는 단계입니다. 모델은 미확인 상태이나 국산 가속기 통합 운영 경험이 풍부하고 정부 사업과 연계한 판로 확장의 핵심 거점입니다.",
      "hook_type": "CLOUD",
      "buying_signal": "범용 서비스형 그래픽처리장치 사업부터 프라이빗 영역까지 전방위 맞춤형 브랜드인 팩토리엑스를 신규 발표하였습니다.",
      "infrastructure_signal": "광주에 구축된 국가적 컴퓨팅 인프라와 신규 대규모 클러스터를 직접 통합 관리하는 체계를 구축하고 있습니다.",
      "timing_reason": "신규 브랜드가 출시되고 공공과 민간의 하이브리드 인프라 수요를 공격적으로 수주하는 활성화 시기입니다.",
      "customer_win": "효율적인 전력 제어 기술을 통해 가속기 집적도를 극대화하고 운영 효율을 향상시킬 수 있습니다. 공공 및 기업 고객에게 규제를 준수하는 경제적인 프라이빗 솔루션 라인업을 제공하게 됩니다.",
      "furiosa_win": "대규모 국가 컴퓨팅 망 및 대표 클라우드 풀스택 파트너로서의 상징적 성공 사례를 확보할 수 있습니다.",
      "numeric_claims": [
        {
          "claim": "NHN클라우드의 신규 가속기 클러스터 장비 도입 규모",
          "source_id": "S003",
          "source_url": "https://www.etoday.co.kr/news/view/2587725",
          "evidence_text": "B200 7656장이 구축된 AI 전용 데이터센터 FactoryX 서울"
        }
      ],
      "direct_sales_possibility": "LOW",
      "csp_routed_sales_possibility": "HIGH",
      "npuaas_adoption_possibility": "HIGH",
      "csp_capacity_expansion_possibility": "HIGH",
      "contact_reason": "통합 인프라 브랜드 내 고효율 국산 실리콘 라인업 다양화를 위한 기술 연계 협의",
      "outreach_talk_track": "최근 새로운 풀스택 브랜드 출시를 통해 사업 영역을 대폭 넓혀가시는 행보를 매우 의미 있게 보고 연락드렸습니다. 대규모 데이터센터의 효율적 다중 인프라 운영 경험에 당사의 가속 기술을 접목하여 시너지를 창출하고 싶습니다. 구체적인 가속기 표준 규격에 부합하는 연동 방안을 조율할 수 있기를 기대합니다.",
      "revenue_timing": "단기",
      "decision_maker_hint": "클라우드 서비스 기획 또는 인프라 운영 기술 총괄 부서장",
      "existing_touchpoint": "확인 필요",
      "verification_needed": [
        "신규 브랜드의 하드웨어 다각화 파이프라인 존재 여부",
        "기존 운영 인프라의 전력 한계치 및 가속 가속기 추가 수용 여력"
      ],
      "source_ids": ["S003", "S005", "S026", "S030"],
      "source_urls": [
        "https://www.etoday.co.kr/news/view/2587725",
        "http://www.efnews.co.kr/news/articleView.html?idxno=129944",
        "https://www.mt.co.kr/tech/2026/05/26/2026052609523154709",
        "https://www.thelec.kr/news/articleView.html?idxno=57143"
      ]
    },
    {
      "name": "오픈네트웍시스템",
      "country": "KR",
      "market": "B2B",
      "target_type": "CSP 운영 기업",
      "classification": "priority_outreach",
      "confirmed_project_or_signal": "글로벌 대표 에이전트 개발 도구 파트너십 체결 및 스마트 솔루션 사업 개시",
      "confirmed_model_name": "미확인",
      "model_match_status": "unknown",
      "model_fit_score": "UNKNOWN",
      "deployment_fit_score": "HIGH",
      "channel_fit_score": "HIGH",
      "rngd_fit_score": "MID",
      "outreach_priority": "HIGH",
      "fit_vs_priority_explanation": "해당 파트너는 에이전트 서비스 공급 및 인프라 구축의 핵심 기업입니다. 디파이를 접목한 엔터프라이즈 플랫폼 보급 주체로서 당사의 표준 기술 사양과 높은 사업적 호환성을 가집니다.",
      "hook_type": "VLLM",
      "buying_signal": "에이전트 기술 기반의 전문적 플랫폼 개발 도구인 디파이의 국내 파트너로서 가속 솔루션을 필요로 하는 엔터프라이즈 고객군을 다수 발굴하고 있습니다.",
      "infrastructure_signal": "고객사의 내부 지식 유출을 방지하기 위한 구축형 솔루션 기획과 인프라 통합 기술을 주축으로 개발을 진행하고 있습니다.",
      "timing_reason": "전시회를 통해 구축형 시스템 활용 사례를 다수 공개하고 본격적인 영업 확장을 시작하는 적기입니다.",
      "customer_win": "클라우드 의존도를 탈피하여 대기업 고객이 안심하고 도입 가능한 고속의 폐쇄망 구축형 인프라 패키지를 완성할 수 있습니다.",
      "furiosa_win": "유연한 에이전트 도구 생태계와 당사 가속 기술을 통합한 고성능 하이브리드 서버 패키지를 공동 개발하여 채널 성장을 도모할 수 있습니다.",
      "numeric_claims": [],
      "direct_sales_possibility": "MID",
      "csp_routed_sales_possibility": "HIGH",
      "npuaas_adoption_possibility": "HIGH",
      "csp_capacity_expansion_possibility": "LOW",
      "contact_reason": "구축형 기업 솔루션 고속 구동을 위한 최적화 인프라 파트너십 체결 제안",
      "outreach_talk_track": "인공지능 비즈니스 파트너로서 엔터프라이즈 시장을 주도하시는 활동을 고무적으로 생각하여 연락드렸습니다. 당사의 표준 인터페이스와 연동이 편리한 고속 하드웨어를 고객향 구축 시스템에 결합한다면 매우 경쟁력 있는 비용 절감 효과를 기대할 수 있을 것입니다. 상호 시너지 창출 방안을 점검해 보고 싶습니다.",
      "revenue_timing": "단기",
      "decision_maker_hint": "신규 사업 개발 총괄 실장 또는 인프라 개발 리드",
      "existing_touchpoint": "확인 필요",
      "verification_needed": [
        "도입 추진 중인 구축형 프로젝트의 하드웨어 납품 여부",
        "당사 가속 솔루션과 호환 가능한 표준 인터페이스 지원 여부"
      ],
      "source_ids": ["S021", "S022"],
      "source_urls": [
        "https://www.joongang.co.kr/article/25430014",
        "https://www.gokorea.kr/news/articleView.html?idxno=866999"
      ]
    },
    {
      "name": "우리은행",
      "country": "KR",
      "market": "B2B",
      "target_type": "CSP 고객 기업",
      "classification": "cloud_npuaaS_lead",
      "confirmed_project_or_signal": "대형 인공지능 자산 분석 및 자금 상담용 내부 고도화 프로젝트 추진",
      "confirmed_model_name": "미확인",
      "model_match_status": "unknown",
      "model_fit_score": "UNKNOWN",
      "deployment_fit_score": "HIGH",
      "channel_fit_score": "HIGH",
      "rngd_fit_score": "MID",
      "outreach_priority": "HIGH",
      "fit_vs_priority_explanation": "자체 서버 직접 도입보다는 클라우드 또는 파트너 연계를 통한 비용 통제가 주요 관심사입니다. 파트너사를 경유한 판매 가능성이 높으므로 채널 영업 우수 사례로 관리합니다.",
      "hook_type": "CLOUD",
      "buying_signal": "은행 업무 효율 개선과 고객 관계 유지를 위해 내부 상담 및 대량 문서 분석 처리가 핵심 과제로 부상하고 있습니다.",
      "infrastructure_signal": "보안 규정과 법률 준수 요건으로 인해 대규모 연산을 안전하게 처리할 인프라 환경이 필수적입니다.",
      "timing_reason": "우선협상대상자가 선정되어 솔루션 구체화 작업이 활발히 구상되고 있는 상황입니다.",
      "customer_win": "대량의 자산 포트폴리오 분석 처리에 소모되는 컴퓨팅 인프라 예산을 대폭 통제하고 업무 처리 속도를 개선할 수 있습니다.",
      "furiosa_win": "대표적인 대형 제1금융권의 대용량 실시간 비즈니스 처리 성공 사례를 안정적으로 확보할 수 있습니다.",
      "numeric_claims": [],
      "direct_sales_possibility": "LOW",
      "csp_routed_sales_possibility": "HIGH",
      "npuaas_adoption_possibility": "HIGH",
      "csp_capacity_expansion_possibility": "LOW",
      "contact_reason": "구축 수행 파트너사 연계를 통한 비용 효율적 고성능 추론 하드웨어 도입 방안 탐색",
      "outreach_talk_track": "현재 추진 중이신 첨단 분석 및 관리 서비스의 신속한 전개를 돕고자 연락드렸습니다. 당사의 고속 가속 시스템은 방대한 규모의 금융 문서 처리에 수반되는 장비 전력 비용을 제어하는 최상의 대안이 될 수 있습니다. 구축 예정인 플랫폼에 부합하는 적합성 점검을 유관 부서와 조율하고 싶습니다.",
      "revenue_timing": "중기",
      "decision_maker_hint": "디지털 혁신 추진 부서 리더 또는 정보보호 책임자",
      "existing_touchpoint": "확인 필요",
      "verification_needed": [
        "파트너사가 제안한 인프라 사양 내에 국산 칩 도입 허용 범위",
        "내부 서비스의 실시간 추론 지연 시간 허용 기준 요구치"
      ],
      "source_ids": ["S034", "S035"],
      "source_urls": [
        "https://www.sedaily.com/article/20046605?ref=naver",
        "https://www.sedaily.com/article/20046505?ref=naver"
      ]
    },
    {
      "name": "시스트란",
      "country": "KR",
      "market": "B2B",
      "target_type": "온프레미스 기업",
      "classification": "structure_check",
      "confirmed_project_or_signal": "폐쇄망용 온프레미스 기업 지식 관리 솔루션 라인업 신규 런칭",
      "confirmed_model_name": "미확인",
      "model_match_status": "unknown",
      "model_fit_score": "UNKNOWN",
      "deployment_fit_score": "HIGH",
      "channel_fit_score": "MID",
      "rngd_fit_score": "MID",
      "outreach_priority": "MID",
      "fit_vs_priority_explanation": "보안에 특화된 온프레미스 지식 자산 도구를 공급하는 솔루션 파트너입니다. 기성 클라이언트에게 제공할 하드웨어 어플라이언스 제품군 다양화를 위해 구조 검토가 요구됩니다.",
      "hook_type": "SOVEREIGN",
      "buying_signal": "보안 유출을 우려하는 기업들을 겨냥해 데이터가 차단된 내부 온프레미스에서 완결되는 제품을 지속 확장하고 있습니다.",
      "infrastructure_signal": "인터넷이 철저히 격리된 환경에서 개별 서버 내 처리를 수반하므로 효율적인 단일 머신 성능이 중요합니다.",
      "timing_reason": "전용 폐쇄형 시스템군을 공개하고 솔루션 결합 파트너를 활발히 물색하는 비즈니스 국면입니다.",
      "customer_win": "외부와 전면 격리된 기업의 보안 장비로서, 소형 전력 규범 하에서도 빠르고 매끄러운 문서 처리를 달성할 수 있습니다.",
      "furiosa_win": "독립 실행형 보안 솔루션 하드웨어 패키지 내 탑재를 통해 검증된 산업용 표준 모델을 널리 알릴 수 있습니다.",
      "numeric_claims": [],
      "direct_sales_possibility": "MID",
      "csp_routed_sales_possibility": "MID",
      "npuaas_adoption_possibility": "LOW",
      "csp_capacity_expansion_possibility": "LOW",
      "contact_reason": "보안 격리형 시스템 장비 내 국산 저전력 하드웨어 탑재 협의",
      "outreach_talk_track": "귀사의 최신 격리형 인공지능 패키지 출시 관련 소식을 유익하게 검토하였습니다. 엄격한 정보보호가 생명인 보안 장비 도입 현장에는 저전력 기반 가속 장치의 정합성이 높습니다. 저희 솔루션과 결합 시 달성 가능한 처리 처리량과 경제성에 대해 실무 차원의 테스트를 논의하고 싶습니다.",
      "revenue_timing": "중기",
      "decision_maker_hint": "제품 개발 부문 총괄 엔지니어 또는 기술 제휴 담당 부서장",
      "existing_touchpoint": "확인 필요",
      "verification_needed": [
        "패키지 소프트웨어 자체의 이식 장비 요구 사항 및 호환 여부",
        "보안 타깃 업계에서 요구하는 일일 처리 처리 속도 성능 목표치"
      ],
      "source_ids": ["S001"],
      "source_urls": [
        "https://www.etnews.com/20260522000276"
      ]
    },
    {
      "name": "네이버클라우드",
      "country": "KR",
      "market": "B2B",
      "target_type": "CSP 운영 기업",
      "classification": "priority_outreach",
      "confirmed_project_or_signal": "국가 규모 컴퓨팅 인프라 조성 참여 및 기술 창업 활성화 협력 강화",
      "confirmed_model_name": "미확인",
      "model_match_status": "unknown",
      "model_fit_score": "UNKNOWN",
      "deployment_fit_score": "HIGH",
      "channel_fit_score": "HIGH",
      "rngd_fit_score": "MID",
      "outreach_priority": "HIGH",
      "fit_vs_priority_explanation": "지방에 신설될 거대 국가 컴퓨팅 인프라 프로젝트에 참여 중인 대형 연합의 일원입니다. 공공과 민간의 에너지 한계를 조율해야 하므로 접촉의 시급성이 인정됩니다.",
      "hook_type": "SCALE",
      "buying_signal": "지역 혁신 기업 대상의 생성 서비스 육성 모델 지원을 병행하며 인프라 주권을 공고히 하기 위해 다자 동맹에 동참하고 있습니다.",
      "infrastructure_signal": "수도권 전력 집중을 탈피하여 다양한 남부 전역에 대규모 에너지 활용 구조 설계를 검토하고 있습니다.",
      "timing_reason": "국가 주도 신규 컴퓨팅 전용 센터 구상이 본격 가시화되고 세부 스펙 조율이 추진되는 현 시점입니다.",
      "customer_win": "급격한 클라우드 냉각 비용과 에너지 부하 부담을 극적으로 통제하며 차세대 지역 분산 인프라에 대응할 수 있습니다.",
      "furiosa_win": "국내 최고 공공 및 민간 컴퓨팅 허브에 메이저 벤더로 공식 등록되는 중대한 영업적 디딤돌을 확보합니다.",
      "numeric_claims": [],
      "direct_sales_possibility": "LOW",
      "csp_routed_sales_possibility": "HIGH",
      "npuaas_adoption_possibility": "HIGH",
      "csp_capacity_expansion_possibility": "HIGH",
      "contact_reason": "전력 효율 중심의 차세대 지방형 분산 데이터센터 설계 표준 제안",
      "outreach_talk_track": "국가 차원의 신규 데이터센터 조성 사업 구상과 관련하여 인프라 전력 최적화 방안에 대해 논의를 희망합니다. 당사의 솔루션은 고전력 수급 한계를 극복해야 하는 대규모 설계 현장에 매우 적절한 친환경 가속을 구현합니다. 기술 검증 차원의 구체적인 사양 교환을 기대합니다.",
      "revenue_timing": "장기",
      "decision_maker_hint": "공공 클라우드 사업 부문 전무 또는 데이터센터 인프라 기술 리더",
      "existing_touchpoint": "확인 필요",
      "verification_needed": [
        "남부권 신설 센터의 국산 제품 대상 규범적 최소 할당 지침",
        "자체 소유 모델 외에 이기종 오픈 소스 가속 플랫폼 구성 계획"
      ],
      "source_ids": ["S009", "S028", "S031", "S032"],
      "source_urls": [
        "https://www.mt.co.kr/policy/2026/05/26/2026052612464197902",
        "https://www.ddaily.co.kr/page/view/2026052017342600376",
        "https://www.ddaily.co.kr/page/view/2026052509101133595",
        "https://www.mt.co.kr/tech/2026/05/23/2026052210211399740"
      ]
    },
    {
      "name": "인공지능산업융합사업단",
      "country": "KR",
      "market": "B2G",
      "target_type": "CSP 운영 기업",
      "classification": "cloud_npuaaS_lead",
      "confirmed_project_or_signal": "국가 데이터센터 컴퓨팅 자원 대규모 하반기 이용자 모집 공고",
      "confirmed_model_name": "미확인",
      "model_match_status": "unknown",
      "model_fit_score": "UNKNOWN",
      "deployment_fit_score": "HIGH",
      "channel_fit_score": "HIGH",
      "rngd_fit_score": "MID",
      "outreach_priority": "HIGH",
      "fit_vs_priority_explanation": "조달 및 공공 사업의 주요 발주처로서 클라우드 개발 인프라 보급에 필수적입니다. 국산 부품 채택 권고사항과 국가적 정책 방향이 강력히 일치하는 요충지입니다.",
      "hook_type": "PROCUREMENT",
      "buying_signal": "수많은 학계 및 상업 기업들을 광범위하게 수용하기 위해 컴퓨팅 클러스터 대규모 활성화를 공식 발표하였습니다.",
      "infrastructure_signal": "막대한 한계 연산 능력을 필요로 하는 시스템을 정부 주도로 가동하여 기업들에게 최적의 개발 자원을 임대 중입니다.",
      "timing_reason": "하반기 이용자 접수를 본격화하며 연동 인프라 점검 및 이기종 연산 가속 최적화를 협의하기 적절합니다.",
      "customer_win": "제한된 예산 안에서 더 많은 벤처 기업들에게 대량의 가속 인프라 기회를 폭넓게 보장할 수 있어 인프라 공급률이 제고됩니다.",
      "furiosa_win": "공공 디지털 인프라의 주요 국산화 목표치를 조기 도달하고 대표적 정부 주도 성공 실적을 증명하게 됩니다.",
      "numeric_claims": [
        {
          "claim": "국가 인공지능 데이터센터 초당 연산 한계 성능",
          "source_id": "S006",
          "source_url": "https://www.etnews.com/20260526000308",
          "evidence_text": "최대 초당 6000조 개의 연산을 수행할 수 있는 6PF"
        }
      ],
      "direct_sales_possibility": "LOW",
      "csp_routed_sales_possibility": "HIGH",
      "npuaas_adoption_possibility": "HIGH",
      "csp_capacity_expansion_possibility": "HIGH",
      "contact_reason": "공공 지원 국산 가속 인프라 생태계 강화를 위한 연산 자원 다각화 기술 협력",
      "outreach_talk_track": "하반기 국가 컴퓨팅 자원 분배 정책에 국산 고효율 가속 모듈을 접목하여 더 큰 시너지를 도출하고 싶어 제안을 드립니다. 당사 솔루션 도입 시 공공 예산의 사용 한계를 대폭 넓혀줄 수 있습니다. 기획 중이신 표준 생태계 구조에 맞춘 실무 협력 방안을 타진해 보고 싶습니다.",
      "revenue_timing": "중기",
      "decision_maker_hint": "인프라 자원 분배 기획 팀장 또는 조달 주관 기술 서기관",
      "existing_touchpoint": "확인 필요",
      "verification_needed": [
        "지정 가속 장비 도입 입찰 일람 및 자격 연계 실태",
        "중소 및 신생 벤처들의 국산 가속 기술 이식 지원 전담 예산 할당 유무"
      ],
      "source_ids": ["S006"],
      "source_urls": [
        "https://www.etnews.com/20260526000308"
      ]
    },
    {
      "name": "베슬에이아이",
      "country": "KR",
      "market": "B2B",
      "target_type": "CSP 운영 기업",
      "classification": "structure_check",
      "confirmed_project_or_signal": "클라우드 스케일 확보를 위한 글로벌 탑 파트너 네트워크와의 제휴 강화",
      "confirmed_model_name": "미확인",
      "model_match_status": "unknown",
      "model_fit_score": "UNKNOWN",
      "deployment_fit_score": "HIGH",
      "channel_fit_score": "HIGH",
      "rngd_fit_score": "MID",
      "outreach_priority": "MID",
      "fit_vs_priority_explanation": "분산된 가속 리소스 활용을 정교화하는 전문 소프트웨어 제공사입니다. 당사 기술이 분산 가속에 쉽게 포함되도록 관리 콘솔 수준의 연동 논의가 권장됩니다.",
      "hook_type": "PARTNER",
      "buying_signal": "자체 서버 소유 한계를 해소하기 위해 분산형 데이터 인프라의 글로벌 통합 가동 체계를 구상하고 있습니다.",
      "infrastructure_signal": "개별 연산 자원들의 편차를 줄이고 운영 안정성을 확보하기 위해 표준 오케스트레이션 도구에 상시 최적화를 추진 중입니다.",
      "timing_reason": "대외 제휴 시너지를 앞세워 신진 데이터 거점으로 입지를 강화하는 영업 활동 단계입니다.",
      "customer_win": "고성능 하드웨어를 플랫폼에 결합하여 이기종 클라우드를 통합 관리하는 경쟁 우위를 시장에 증명할 수 있습니다.",
      "furiosa_win": "다양한 글로벌 이종 연산 인프라 제어 플랫폼에 당사의 접근성이 원천 보장되도록 환경을 구축합니다.",
      "numeric_claims": [],
      "direct_sales_possibility": "LOW",
      "csp_routed_sales_possibility": "HIGH",
      "npuaas_adoption_possibility": "HIGH",
      "csp_capacity_expansion_possibility": "LOW",
      "contact_reason": "이기종 분산 관리 효율 개선을 위한 표준 컨트롤 인터페이스 통합 제안",
      "outreach_talk_track": "글로벌 기반의 분산 데이터 관리 최적화 모델에 관해 기술 제휴를 논의하고 싶습니다. 당사의 효율적인 하드웨어 자원을 귀사의 정교한 통합 통제 시스템에 연동한다면 신규 클라우드 고객을 위한 최상의 가격 경쟁력이 구현됩니다. 세부 협력 방향을 조율할 기회를 고대합니다.",
      "revenue_timing": "중기",
      "decision_maker_hint": "플랫폼 개발 아키텍트 최고 임원 또는 비즈니스 제휴 디렉터",
      "existing_touchpoint": "확인 필요",
      "verification_needed": [
        "가상 오케스트레이션 사양 내 국산 표준 칩용 특화 플러그인 연동 규격",
        "자주 도입되는 목표 워크로드의 입출력 특성 상세 분석"
      ],
      "source_ids": ["S004"],
      "source_urls": [
        "https://www.datanet.co.kr/news/articleView.html?idxno=211927"
      ]
    },
    {
      "name": "KB금융그룹",
      "country": "KR",
      "market": "B2B",
      "target_type": "온프레미스 기업",
      "classification": "watchlist",
      "confirmed_project_or_signal": "보안 강화를 위한 제로트러스트 체계 확대 및 실시간 차단용 내부 인공지능 에이전트 가동",
      "confirmed_model_name": "미확인",
      "model_match_status": "unknown",
      "model_fit_score": "UNKNOWN",
      "deployment_fit_score": "HIGH",
      "channel_fit_score": "MID",
      "rngd_fit_score": "MID",
      "outreach_priority": "WATCH",
      "fit_vs_priority_explanation": "망분리 원칙을 강력히 내세우는 정통 온프레미스 보안 수요처입니다. 외부 의존 최소화 구조를 희망하나 직접 하드웨어 구매 성숙도를 진단하기 위해 모니터링합니다.",
      "hook_type": "SOVEREIGN",
      "buying_signal": "정교해지는 사이버 위협에 실시간 대응하고자 사내 훈련용 및 위협 판단 전용 에이전트 인프라 고도화에 자금을 배정 중입니다.",
      "infrastructure_signal": "기존 망분리 구조를 최대한 온전히 고수하며 모든 접근 경로를 내부망에서 자체 감사하는 인프라를 마련하고자 합니다.",
      "timing_reason": "당국이 보안을 목적으로 하는 유연한 망 보안 해제 및 AI 완화 정책 기조를 마련하는 배경 하에 선제 준비에 돌입하는 형국입니다.",
      "customer_win": "엄격한 폐쇄형 금융 보안 가이드라인 아래 외부 통신 없이도 악성 판단 처리를 내부에서 고속 실행할 능력을 획득합니다.",
      "furiosa_win": "최고 수준의 안전성을 자처하는 대한민국 주요 금융지주의 전용 보안망 내부 하드웨어 우수 레퍼런스를 개척하게 됩니다.",
      "numeric_claims": [],
      "direct_sales_possibility": "MID",
      "csp_routed_sales_possibility": "MID",
      "npuaas_adoption_possibility": "LOW",
      "csp_capacity_expansion_possibility": "LOW",
      "contact_reason": "엄격한 오프라인 정보 유출 차단형 사내 금융망 전용 가속 서버 구축 방안 제안",
      "outreach_talk_track": "귀사의 최첨단 통합 보안 인프라 구상과 정부의 최근 지침 완화 행보를 중요하게 보고 있습니다. 당사는 외부 연결 필요성을 원천 차단하면서도 높은 대량 처리를 지원하는 독자 가속 기술을 제공합니다. 금융 컴플라이언스를 온전히 수호하는 독자 인프라 구축 가능성을 편안히 검토해 드리고 싶습니다.",
      "revenue_timing": "장기",
      "decision_maker_hint": "정보보호 최고 책임자 또는 사내 네트워크 관리 센터 부장",
      "existing_touchpoint": "확인 필요",
      "verification_needed": [
        "망 격리 보존 상태에서 탑재 소프트웨어 패치를 분배하는 표준 절차 규정",
        "보안 관련 학습 및 실시간 패턴 대응을 위한 자체 장비 보유 자금 수준"
      ],
      "source_ids": ["S011", "S013", "S014"],
      "source_urls": [
        "http://www.newsdream.kr/news/articleView.html?idxno=112269",
        "https://www.polinews.co.kr/news/articleView.html?idxno=732241",
        "https://www.kbanker.co.kr/news/articleView.html?idxno=225052"
      ]
    },
    {
      "name": "브레인치즈",
      "country": "KR",
      "market": "B2G",
      "target_type": "온프레미스 기업",
      "classification": "watchlist",
      "confirmed_project_or_signal": "나라장터 혁신 입점 성과 확보 및 다양한 관공서 안전 관제 플랫폼 구축 성과 확대",
      "confirmed_model_name": "미확인",
      "model_match_status": "unknown",
      "model_fit_score": "UNKNOWN",
      "deployment_fit_score": "HIGH",
      "channel_fit_score": "MID",
      "rngd_fit_score": "LOW",
      "outreach_priority": "WATCH",
      "fit_vs_priority_explanation": "공공 지능형 영상 분석 분야의 혁신 장비 선두권 솔루션 기업입니다. 비록 당사 지향 LLM보다는 비전 성격이 강하나 지자체 통합 장비 고도화를 대비해 장기 파이프라인으로 지속 추적합니다.",
      "hook_type": "PROCUREMENT",
      "buying_signal": "중앙정부 및 다수 자치단체 안전 감시 인프라 진입을 본격 전개하며 하드웨어 소형 경량화 및 고성능 연산을 요하고 있습니다.",
      "infrastructure_signal": "실시간 다중 채널을 끊김 없이 해독하고 위험 사항을 적시에 수집하는 대규모 관제용 상시 엣지형 데이터 수집 시스템을 가동 중입니다.",
      "timing_reason": "전국 단위 지자체에 통합 인텔리전트 관제망 구축을 위한 공공 제안 제안이 잇따라 개최되는 계절입니다.",
      "customer_win": "서버실 공간과 소비 전력 제약이 심한 일선 행정관청 인프라에 뛰어난 성능 밀도의 소규모 관제 가속기를 납품 가능케 합니다.",
      "furiosa_win": "일선 지자체 생활 안전망을 뒷받침하는 기술적 동반자로서 안정적 소형 하드웨어 수주 동력을 장기 축적할 발판이 됩니다.",
      "numeric_claims": [],
      "direct_sales_possibility": "MID",
      "csp_routed_sales_possibility": "LOW",
      "npuaas_adoption_possibility": "LOW",
      "csp_capacity_expansion_possibility": "LOW",
      "contact_reason": "지자체 소형 상시 관제 연산장비 최적화를 위한 효율적 실시간 영상 해독 기술 제안",
      "outreach_talk_track": "공공의 안전 인프라 지평을 성공적으로 넓히시는 성과 소식을 접하고 연락을 올렸습니다. 당사는 발열 제어와 공간 활용성이 제한된 기성 행정 시스템실에 최적인 저전력 실시간 가속 아키텍처를 지원하고 있습니다. 향후 기종 설계 시 적용 범위를 확대하기 위한 기술 연계 미팅을 제의합니다.",
      "revenue_timing": "장기",
      "decision_maker_hint": "지능형 관제 플랫폼 개발실 이사 또는 공공 비즈니스 팀장",
      "existing_touchpoint": "확인 필요",
      "verification_needed": [
        "기성 영상 해독 프로그램 내 국산 칩셋 구동에 핵심적인 연계 드라이버 호환 상황",
        "지자체 표준 구매 명세서에서 허용하는 전용 가속 보드 수급 가이드라인"
      ],
      "source_ids": ["S019"],
      "source_urls": [
        "https://www.joongboo.com/news/articleView.html?idxno=363726733"
      ]
    }
  ],
  "competitor_signals": [
    {
      "competitor": "NVIDIA",
      "signal_type": "customer_deployment",
      "summary": "NHN클라우드의 초대형 신규 국가 AI 데이터센터 및 팩토리엑스 서울 센터에 엔비디아의 최신 세대 대규모 연산 카드들을 기반으로 대규모 인프라 공급 체계를 수립하고 연동 중인 것으로 파악됩니다.",
      "source_id": "S003",
      "source_url": "https://www.etoday.co.kr/news/view/2587725",
      "evidence_excerpt": "국내 최초 H100 그래픽처리장치(GPU)... B200 7656장이 구축된 AI 전용 데이터센터 FactoryX 서울"
    },
    {
      "competitor": "기타",
      "signal_type": "channel_launch",
      "summary": "엣지형 인공지능 가속 장치 분야 전문 중소 팹리스가 가속기 제품 2종을 조달청 혁신제품으로 입점 완료하여 공공기관 및 부처의 나라장터 조달 기회를 정식 획득하고 본격적인 공공 침투를 준비 중입니다.",
      "source_id": "S017",
      "source_url": "https://www.mt.co.kr/future/2026/05/22/2026052214135044338",
      "evidence_excerpt": "모빌린트 'NPU 솔루션' 조달청 혁신제품 등록… 두 제품이 가격뿐 아니라 전력효율이 높아 공공기관 AI 인프라 환경에서"
    }
  ],
  "noise_examples": [
    {
      "source_id": "S023",
      "title": "\"수수료는 챙기고 민원은 나몰라라?\"...당근·번개장터 등 중고거래 플...",
      "reason": "소비자 상담 및 수수료 정산 지연 관련 언론 지적으로 당사 가속칩 GTM 기회나 인프라 관련 실질 신호와 무관한 단순 고충성 내용입니다."
    },
    {
      "source_id": "S020",
      "title": "산업수도 울산 찾은 이형주 회장...\"회원 보호·업역 확대\" 강조",
      "reason": "공공 자재 가격 현실화와 관련된 정통 전기협회 활동 동향으로 가속 하드웨어 연산 자원 설계나 연계 사업과는 상관없는 일반 협회 동태 정보입니다."
    }
  ],
  "eval_notes": [
    "모든 제안된 타깃들은 상세 기사에 언급된 정황에 입각하여 구조적으로 연계될 수 있는 가치를 바탕으로 면밀히 선별되었습니다.",
    "삼성SDS 및 NHN클라우드와 같은 초정밀 파트너 기업들은 세부 구동 모델 미정 상태를 유지했으나 강력한 채널 가치를 인정해 HIGH 등급의 우선도를 할당했습니다.",
    "숫자가 기술된 모든 항목은 정확히 소스 일람의 본문 구문과 검증 대조를 마쳤으며 주관적인 수치 가감 및 가공이 전면 차단되었습니다."
  ]
}
```