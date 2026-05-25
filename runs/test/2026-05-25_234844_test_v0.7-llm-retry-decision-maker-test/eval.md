# LLM Evaluation Notes

## LLM metadata

- provider: `gemini`
- model: `gemini-3.5-flash`
- llm_sources_count: `40`
- max_llm_sources: `40`
- max_source_chars: `800`
- max_output_candidates: `12`
- evaluated_at_kst: `2026-05-25T23:54:40.294778+09:00`

## Run summary

- overall_assessment: 최근 국내 대형 CSP 및 공공 부문을 중심으로 생성형 AI 서비스 인프라 확장과 민간·공공 전용 AI 플랫폼 구축 수요가 강하게 확인됩니다. 특히 삼성SDS의 동탄 및 구미 데이터센터 인프라 확장, 우리은행 AI 에이전트 사업 수주 등은 대규모 추론 인프라 공급의 핵심 기회입니다. 또한 한글과컴퓨터와 LG AI연구원의 공공 AI 에이전트 동맹, 건강보험심사평가원의 GPU 기반 플랫폼 구축 등 B2G 영역의 실행형 사업이 구체화되고 있어 맞춤형 GTM 전개가 요구됩니다.
- top_priority_names: 삼성SDS, 엘리스그룹, 우리은행, 건강보험심사평가원
- noise_ratio_comment: 수집된 40개 소스 중 선거 공약, 글로벌 거대 기술기업 동향, 전력 인프라 주식 동향 등 직접적인 GTM 신호가 없는 3개 소스를 제외한 대부분의 소스가 국내 CSP 인프라 확장 및 생성형 AI 플랫폼 구축 프로젝트와 관련된 유의미한 비즈니스 신호를 포함하고 있습니다.
- model_compatibility_caution: 본 평가에서는 제공된 FuriosaAI 개발자 문서 기준을 엄격히 적용하여 정확한 모델 및 버전 매칭을 수행했습니다. 농협은행의 EXAONE 3.5 도입 사례와 한글과컴퓨터의 챗엑사원 결합 사례는 EXAONE 모델 제품군에 해당하나 구체적인 지원 버전 검증이 필요하므로 family_only로 분류하여 보수적으로 평가했습니다. 또한 큐엔 모델군 및 업스테이지 솔라 모델의 경우 구체적인 버전 일치 여부를 파트너십 과정에서 추가 확인해야 합니다.

## Eval notes

- 경쟁사인 알리바바가 코딩 및 에이전트 작업용 모델 Qwen 3.7-Max 출시와 함께 독자 AI 가속기 '전우 M890'을 신규 공개(S006, S029)하며 자사 전용 인프라 및 금융 영역 고객 유치를 활발히 전개하는 흐름입니다. 국산 AI 가속기의 지배력 수호를 위해 국내 금융·공공 GTM 공략 시 기술적 경쟁 장치를 신속하게 선점해야 합니다.
- 삼성SDS는 경기 동탄 데이터센터에 20MW급 전력을 추가 조달하고, 경북 구미에 60MW AI 데이터센터 구축을 본격 투입하는 등 데이터센터 전력 자립 노력을 가속화하고 있습니다(S003, S009). 이는 당사 RNGD가 지닌 최대 차별적 이점인 저전력 설계 및 전력 효율 향상 성능(Rack density 최적화)을 파트너사 기술 설계단에 침투시킬 우수한 진입 명분으로 작용합니다.
- B2G 시장에 맞추어 한글과컴퓨터와 LG AI연구원이 공공 행정 AI 수주 연합 전선을 결성함에 따라(S020) 해당 챗엑사원 플랫폼에 대한 국산 NPU 탑재 추진 가능성이 매우 긍정적입니다. 즉각적인 하드웨어 조달 파트너십 제안이 긴요하며 차기 주력 사업인 K-EXAONE 로드맵 지원 사양과 접목을 면밀하게 선행 추진할 필요가 있습니다.

## Raw LLM response

```json
{
  "run_summary": {
    "overall_assessment": "최근 국내 대형 CSP 및 공공 부문을 중심으로 생성형 AI 서비스 인프라 확장과 민간·공공 전용 AI 플랫폼 구축 수요가 강하게 확인됩니다. 특히 삼성SDS의 동탄 및 구미 데이터센터 인프라 확장, 우리은행 AI 에이전트 사업 수주 등은 대규모 추론 인프라 공급의 핵심 기회입니다. 또한 한글과컴퓨터와 LG AI연구원의 공공 AI 에이전트 동맹, 건강보험심사평가원의 GPU 기반 플랫폼 구축 등 B2G 영역의 실행형 사업이 구체화되고 있어 맞춤형 GTM 전개가 요구됩니다.",
    "top_priority_names": [
      "삼성SDS",
      "엘리스그룹",
      "우리은행",
      "건강보험심사평가원"
    ],
    "noise_ratio_comment": "수집된 40개 소스 중 선거 공약, 글로벌 거대 기술기업 동향, 전력 인프라 주식 동향 등 직접적인 GTM 신호가 없는 3개 소스를 제외한 대부분의 소스가 국내 CSP 인프라 확장 및 생성형 AI 플랫폼 구축 프로젝트와 관련된 유의미한 비즈니스 신호를 포함하고 있습니다.",
    "model_compatibility_caution": "본 평가에서는 제공된 FuriosaAI 개발자 문서 기준을 엄격히 적용하여 정확한 모델 및 버전 매칭을 수행했습니다. 농협은행의 EXAONE 3.5 도입 사례와 한글과컴퓨터의 챗엑사원 결합 사례는 EXAONE 모델 제품군에 해당하나 구체적인 지원 버전 검증이 필요하므로 family_only로 분류하여 보수적으로 평가했습니다. 또한 큐엔 모델군 및 업스테이지 솔라 모델의 경우 구체적인 버전 일치 여부를 파트너십 과정에서 추가 확인해야 합니다."
  },
  "candidates": [
    {
      "name": "삼성SDS",
      "country": "KR",
      "market": "B2B",
      "target_type": "CSP 운영 기업",
      "classification": "priority_outreach",
      "confirmed_project_or_signal": "동탄 데이터센터 및 경북 구미 AI 데이터센터 투자 및 우리은행 AI 에이전트 구축 사업 우선협상대상자 선정",
      "confirmed_model_name": "미확인",
      "model_match_status": "unknown",
      "model_fit_score": "UNKNOWN",
      "deployment_fit_score": "HIGH",
      "channel_fit_score": "HIGH",
      "rngd_fit_score": "MID",
      "outreach_priority": "HIGH",
      "fit_vs_priority_explanation": "도입 모델이 구체적으로 확인되지 않아 모델 적합성은 UNKNOWN으로 분류되었으나, 동탄 데이터센터 전력 확보 및 구미 데이터센터 대규모 투자를 통한 인프라 확장 계획과 우리은행 AI 에이전트 사업 수주 등 강력한 비즈니스 신호가 존재합니다. 따라서 인프라 파트너십 및 대규모 CSP 용량 증설 경로를 고려하여 outreach_priority를 HIGH로 책정하였습니다.",
      "hook_type": "CLOUD",
      "buying_signal": "경기 동탄 데이터센터에 20MW급 전력을 확보하고, 경북 구미에 4273억원을 투자해 60MW 규모의 AI 데이터센터를 구축하기로 결정함",
      "infrastructure_signal": "동탄 및 구미 지역에 대규모 데이터센터를 확보하여 GPUaaS 인프라 공급 능력을 확장하고 있음",
      "timing_reason": "대규모 인프라 확장 및 전력 확보 시점에 맞추어 하드웨어 효율성 및 운영 비용 개선을 위한 가속기 도입 제안이 가능한 시점임",
      "customer_win": "대규모 AI 추론 서비스 운영 시 발생하는 전력 및 냉각 비용을 절감하고, 가속기 도입 효율성을 높여 인프라 구축 및 운영 부담을 최소화할 수 있음",
      "furiosa_win": "대규모 AI 인프라를 보유한 핵심 CSP 파트너를 확보함으로써 국산 NPU 기반의 NPUaaS 비즈니스 협력 및 추가적인 가속기 대량 공급 기회를 선점할 수 있음",
      "numeric_claims": [
        {
          "claim": "경북 구미에 4273억원을 투자해 60MW 규모 AI 데이터센터를 구축하기로 결정",
          "source_id": "S009",
          "source_url": "https://www.mt.co.kr/tech/2026/05/23/2026052210211399740",
          "evidence_text": "삼성SDS는 경북 구미에 4273억원을 투자해 60MW 규모 AI 데이터센터를 짓기로 했다."
        },
        {
          "claim": "경기 동탄 데이터센터 서관 가동을 위해 20MW급 전력 확보",
          "source_id": "S003",
          "source_url": "https://www.e-science.co.kr/news/articleView.html?idxno=130004",
          "evidence_text": "삼성SDS가 경기 동탄 데이터센터 서관 가동을 위해 20MW급 전력을 확보한 사례"
        }
      ],
      "direct_sales_possibility": "MID",
      "csp_routed_sales_possibility": "HIGH",
      "npuaas_adoption_possibility": "HIGH",
      "csp_capacity_expansion_possibility": "HIGH",
      "contact_reason": "동탄 및 구미 데이터센터 인프라 확장 계획과 금융권 AI 수주 성과에 맞추어 고성능 저전력 가속기 기반의 추론 비용 절감 방안 제안 필요",
      "outreach_talk_track": "최근 동탄 및 구미 데이터센터 인프라 투자 소식을 보고 연락드렸습니다. 대규모 GPUaaS 인프라 및 금융권 AI 서비스 운영 시 전력과 냉각 효율을 대폭 개선할 수 있는 가속기 도입 협력 방안을 제안드리고자 합니다.",
      "revenue_timing": "단기",
      "decision_maker_hint": "클라우드 서비스 및 인프라 부문 CIO, CTO, Head of Cloud, 플랫폼 및 데이터센터 구축 담당 부서장",
      "existing_touchpoint": "확인 필요",
      "verification_needed": [
        "구미 및 동탄 데이터센터 내 국산 NPU 및 가속기 평가/도입 로드맵 확인 필요",
        "우리은행 AI 에이전트 서비스 플랫폼에 RNGD 기술 규격 접목 가능성 타진"
      ],
      "source_ids": [
        "S003",
        "S009",
        "S025",
        "S027"
      ],
      "source_urls": [
        "https://www.e-science.co.kr/news/articleView.html?idxno=130004",
        "https://www.mt.co.kr/tech/2026/05/23/2026052210211399740",
        "https://www.sedaily.com/article/20046605?ref=naver",
        "https://www.sedaily.com/article/20046505?ref=naver"
      ]
    },
    {
      "name": "엘리스그룹",
      "country": "KR",
      "market": "B2B",
      "target_type": "CSP 운영 기업",
      "classification": "priority_outreach",
      "confirmed_project_or_signal": "코스닥 상장 예비심사 청구 및 자체 GPUaaS 및 인프라 비즈니스 본격화",
      "confirmed_model_name": "미확인",
      "model_match_status": "unknown",
      "model_fit_score": "UNKNOWN",
      "deployment_fit_score": "HIGH",
      "channel_fit_score": "HIGH",
      "rngd_fit_score": "MID",
      "outreach_priority": "HIGH",
      "fit_vs_priority_explanation": "도입 모델이 구체화되지 않아 model_fit_score는 UNKNOWN이나, 코스닥 상장 추진을 계기로 자체 AI 클라우드 인프라(ECI, AI PMDC) 및 GPUaaS 서비스를 적극적으로 고도화하고 확장하는 성장 단계에 있어 인프라 파트너십 구축 및 NPUaaS 협력 강화를 위한 접촉 가치가 매우 크므로 outreach_priority를 HIGH로 판정했습니다.",
      "hook_type": "CLOUD",
      "buying_signal": "코스닥 상장 예비심사를 신청하며 AI 클라우드 인프라 솔루션 및 자체 이동식 모듈형 데이터센터 등의 서비스 사업 확대를 공식화함",
      "infrastructure_signal": "자체 클라우드 인프라 및 AI PMDC를 직접 설계·운영하며 대규모 가속기 리소스 확보에 높은 관심을 보이고 있음",
      "timing_reason": "상장 추진을 통해 유입될 투자 재원을 바탕으로 인프라 확장 투자가 예정되어 있어, 저비용·고효율 NPU 하드웨어 솔루션 제안의 최적기임",
      "customer_win": "효율적인 하드웨어 설계를 바탕으로 인프라 투자 비용을 절감하고 가성비 높은 NPUaaS 라인업을 구성하여 서비스 경쟁력을 제고할 수 있음",
      "furiosa_win": "성장세가 가파른 신흥 AI 클라우드 전문 플랫폼을 확보하여 국산 NPU 레퍼런스를 다각화하고 중장기적인 가속기 공급 파이프라인을 구축할 수 있음",
      "numeric_claims": [],
      "direct_sales_possibility": "MID",
      "csp_routed_sales_possibility": "HIGH",
      "npuaas_adoption_possibility": "HIGH",
      "csp_capacity_expansion_possibility": "HIGH",
      "contact_reason": "AI 클라우드 인프라 확장 및 고도화 시점에 발맞춘 저전력 가속기 솔루션 기반 NPUaaS 파트너십 제안",
      "outreach_talk_track": "최근 코스닥 상장 추진 및 AI 클라우드 서비스 고도화 소식을 보고 연락드렸습니다. 엘리스그룹의 모듈형 데이터센터 및 클라우드 인프라에 당사의 RNGD를 연계하여 비용 효율적인 차세대 NPUaaS 라인업을 공동 구축하는 방안을 논의하고자 합니다.",
      "revenue_timing": "단기",
      "decision_maker_hint": "대표이사(CEO), CTO, AI 클라우드 인프라 본부장, 인프라 아키텍처 및 하드웨어 조달 담당 부서장",
      "existing_touchpoint": "확인 필요",
      "verification_needed": [
        "엘리스그룹이 현재 기획 중인 신규 가속기 라인업 내 국산 NPU 채택 가능 여부 검토",
        "RNGD 기반의 AI 가상화 및 Kubernetes 스택 정합성 검증 일정 조율"
      ],
      "source_ids": [
        "S012",
        "S013",
        "S014",
        "S015",
        "S016",
        "S017"
      ],
      "source_urls": [
        "http://www.hansbiz.co.kr/news/articleView.html?idxno=839792",
        "http://www.joseilbo.com/news/news_read.php?uid=568639&class=53&grp=",
        "https://www.fetv.co.kr/news/articleView.html?idxno=302765",
        "https://www.the-stock.kr/news/articleView.html?idxno=32570",
        "https://www.newspim.com/news/view/20260520000146",
        "https://www.cstimes.com/news/articleView.html?idxno=706484"
      ]
    },
    {
      "name": "우리은행",
      "country": "KR",
      "market": "B2B",
      "target_type": "CSP 고객 기업",
      "classification": "cloud_npuaaS_lead",
      "confirmed_project_or_signal": "AI 에이전트 구축 사업 우선협상대상자로 삼성SDS 선정",
      "confirmed_model_name": "미확인",
      "model_match_status": "unknown",
      "model_fit_score": "UNKNOWN",
      "deployment_fit_score": "HIGH",
      "channel_fit_score": "HIGH",
      "rngd_fit_score": "MID",
      "outreach_priority": "HIGH",
      "fit_vs_priority_explanation": "사용 모델명이 명시되지 않아 model_fit_score는 UNKNOWN으로 평가했으나, 금융권 AI 플랫폼 고도화를 위해 삼성SDS의 클라우드 기반 및 전용 인프라를 활용하여 사업을 대규모로 전개할 예정입니다. 삼성SDS와의 파트너십 채널을 활용한 CSP 경유 도입 또는 NPUaaS 도입 시나리오의 가치가 매우 높기 때문에 outreach_priority를 HIGH로 결정했습니다.",
      "hook_type": "PARTNER",
      "buying_signal": "자산관리 분석 보고서 작성 및 기업 분석 등의 기능을 수행하기 위해 대규모 AI 에이전트 구축 사업을 진행하며 우선협상대상자로 삼성SDS를 최종 선정함",
      "infrastructure_signal": "삼성SDS의 금융 AI 플랫폼 인프라를 연계 사용하거나 보안 요건을 충족하기 위한 전용 인프라 아키텍처 환경 구축을 검토 중임",
      "timing_reason": "우선협상대상자 선정 직후 구체적인 인프라 아키텍처 및 가속기 규격을 검토하고 확정하는 단계로, 파트너사인 삼성SDS와 공동으로 최적의 비용 효율을 제공하는 NPU 규격을 제안할 적절한 타이밍임",
      "customer_win": "보안 제약을 해소하며 금융권 전용 AI 에이전트 서빙 환경을 대규모로 운영할 때 발생하는 연산 비용 및 인프라 구축 단가를 크게 낮출 수 있음",
      "furiosa_win": "국내 대형 금융권 고객의 핵심 서비스 플랫폼에 삼성SDS 협력 채널을 경유하여 RNGD 추론 서버를 성공적으로 도입하고 주요 금융권 모범 사례를 확보할 수 있음",
      "numeric_claims": [],
      "direct_sales_possibility": "LOW",
      "csp_routed_sales_possibility": "HIGH",
      "npuaas_adoption_possibility": "HIGH",
      "csp_capacity_expansion_possibility": "MID",
      "contact_reason": "삼성SDS 우선협상대상자 선정에 따라 대규모 추론 서비스용 저전력 고효율 NPU 도입 방안 제안",
      "outreach_talk_track": "최근 생성형 AI 기반 금융 비즈니스 고도화 사업의 우선협상대상자로 삼성SDS가 선정된 것을 보고 연락드렸습니다. 삼성SDS 인프라와 결합하여 대규모 금융 데이터 분석 및 문서 요약 서비스를 한층 경제적이고 안정적으로 구동할 수 있는 NPU 솔루션을 소개드리고자 합니다.",
      "revenue_timing": "단기",
      "decision_maker_hint": "디지털그룹 임원, AI 플랫폼 센터장, CDO, IT 인프라 기획 부서장 및 조달 담당 부서",
      "existing_touchpoint": "확인 필요",
      "verification_needed": [
        "금융위의 망분리 규제 완화 기조 속에서 클라우드 및 전용 온프레미스 인프라 비중 확인 필요",
        "삼성SDS의 해당 구축 본부와의 연계 파트너십 가능 여부 점검"
      ],
      "source_ids": [
        "S025",
        "S027"
      ],
      "source_urls": [
        "https://www.sedaily.com/article/20046605?ref=naver",
        "https://www.sedaily.com/article/20046505?ref=naver"
      ]
    },
    {
      "name": "한글과컴퓨터",
      "country": "KR",
      "market": "B2G",
      "target_type": "CSP 고객 기업",
      "classification": "structure_check",
      "confirmed_project_or_signal": "LG AI연구원과 AI 문서 에이전트 및 공공 AX 시장 공동 진출 협력",
      "confirmed_model_name": "EXAONE",
      "model_match_status": "family_only",
      "model_fit_score": "MID",
      "deployment_fit_score": "HIGH",
      "channel_fit_score": "MID",
      "rngd_fit_score": "MID",
      "outreach_priority": "HIGH",
      "fit_vs_priority_explanation": "LG AI연구원의 EXAONE 모델군을 기반으로 사업을 전개하므로 model_match_status는 family_only로 분류하여 model_fit_score와 rngd_fit_score는 MID로 책정했습니다. 다만 공공 AX 시장 수주를 목표로 정부부처 및 공기업에 대규모 납품을 추진하는 파트너십 구축이 활발하므로, 공공망 및 규제 환경을 위한 국산 하드웨어 최적화 가치를 평가하여 outreach_priority를 HIGH로 판정했습니다.",
      "hook_type": "PROCUREMENT",
      "buying_signal": "정부부처, 공공기관, 공기업을 대상으로 문서 AI 역량과 LG의 '챗엑사원'을 결합한 통합 에이전트 솔루션 공급을 확대하고 있음",
      "infrastructure_signal": "공공기관의 특수 보안 요건을 준수하기 위해 온프레미스 구축 및 행안부 보안 기준을 만족하는 프라이빗 클라우드 인프라 배포를 고려 중임",
      "timing_reason": "공공 AX 공동 수주 및 정부 주도의 AI 플랫폼 인프라 도입 사업이 연달아 구체화되는 단계로, 하드웨어 주권 확보 차원의 국산 NPU 도입 제안을 추진하기에 최적의 시기임",
      "customer_win": "공공 전용 AI 문서 에이전트 서비스 전개 시 엄격한 데이터 보안 요구사항을 충족하고 전력 소비와 도입 비용을 한층 합리적으로 제어할 수 있음",
      "furiosa_win": "대표적인 한글 문서 기반 AI 서비스에 가속기 최적화를 실현하여 공공 부문 비즈니스 영역에서 지배적인 국산 가속기 레퍼런스를 확보할 수 있음",
      "numeric_claims": [],
      "direct_sales_possibility": "MID",
      "csp_routed_sales_possibility": "MID",
      "npuaas_adoption_possibility": "MID",
      "csp_capacity_expansion_possibility": "MID",
      "contact_reason": "공공 부문 AX 연합 진출에 따른 저전력 국산 NPU 기반 AI 문서 솔루션 최적화 논의 제안",
      "outreach_talk_track": "최근 LG AI연구원과의 '챗엑사원' 및 AI 문서 에이전트 공공 시장 동맹 강화 소식을 확인하고 연락드렸습니다. 공공 및 정부부처의 보안 규제를 완벽히 준수하며 대규모 문서 요약 및 생성 인프라를 합리적으로 제어할 수 있는 국산 RNGD 가속기 도입 방안을 논의하고자 합니다.",
      "revenue_timing": "단기",
      "decision_maker_hint": "공공사업본부장, CTO, AI 연구소장, AI 플랫폼 개발 팀장 또는 솔루션 설계 부서장",
      "existing_touchpoint": "확인 필요",
      "verification_needed": [
        "공공부문 사업 추진 시 가속기에 대한 기술적 요구 사양(K8s 연동성 등) 충족 여부 확인",
        "EXAONE 4.0 계열 등 최신 모델 버전 적용을 위한 가속기 컴파일 최적화 정합성 평가"
      ],
      "source_ids": [
        "S020",
        "S021",
        "S022",
        "S023",
        "S024"
      ],
      "source_urls": [
        "http://www.newslock.co.kr/news/articleView.html?idxno=130504",
        "https://www.mt.co.kr/tech/2026/05/22/2026052215283358675",
        "https://www.mk.co.kr/article/12055579",
        "https://www.getnews.co.kr/news/articleView.html?idxno=870707",
        "https://www.newsis.com/view/NISX20260522_0003640664"
      ]
    },
    {
      "name": "NH농협은행",
      "country": "KR",
      "market": "B2B",
      "target_type": "온프레미스 기업",
      "classification": "structure_check",
      "confirmed_project_or_signal": "LG CNS와 협력하여 전용 생성형 AI 플랫폼 구축 및 RAG 소방/금융 업무 적용",
      "confirmed_model_name": "EXAONE",
      "model_match_status": "family_only",
      "model_fit_score": "MID",
      "deployment_fit_score": "HIGH",
      "channel_fit_score": "MID",
      "rngd_fit_score": "MID",
      "outreach_priority": "MID",
      "fit_vs_priority_explanation": "LG CNS를 통해 커스텀 튜닝된 EXAONE 3.5 기반 전용 AI 플랫폼을 구축하였으며, 이는 당사 지원 모델군인 EXAONE 패밀리에 속하지만 구체적인 버전에 관한 컴파일 유효성 검토가 요구되므로 model_fit_score를 MID로 배정했습니다. 보안 중심의 금융 폐쇄망 및 전용 온프레미스 인프라 성격이 뚜렷하여 구조 검토 목적의 우선순위 MID로 책정했습니다.",
      "hook_type": "SOVEREIGN",
      "buying_signal": "내부 규정 및 상품 정보 검색, 리테일 영업 지원을 수행하기 위해 전용 생성형 AI 및 RAG 기반 고도화 플랫폼을 실제 가동하며 업무 범위를 점진적으로 확대하고 있음",
      "infrastructure_signal": "보안 및 규정을 준수하기 위해 대외 망과 분리된 금융사 전용의 폐쇄형/프라이빗 인프라 환경을 가동하고 있음",
      "timing_reason": "전용 생성형 AI의 실무 도입이 완료된 상태로, 업무용 트래픽 증가 및 검색 모델 다각화에 대응하여 가속기 효율성을 정밀 검토할 적기임",
      "customer_win": "엄격한 보안 기준을 우수하게 만족시키면서, 금융 전용 온프레미스 가속 서버의 소모 전력을 최소화하고 내부 생성형 인프라 유지 관리 부담을 대폭 경감할 수 있음",
      "furiosa_win": "금융권 자체 생성형 AI 및 RAG 서버 구축 분야에서 최적의 파트너십 레퍼런스를 개척하고, 특수 도메인 프라이빗 하드웨어 공급을 본격 다각화할 수 있음",
      "numeric_claims": [],
      "direct_sales_possibility": "MID",
      "csp_routed_sales_possibility": "MID",
      "npuaas_adoption_possibility": "LOW",
      "csp_capacity_expansion_possibility": "LOW",
      "contact_reason": "금융사 전용 프라이빗 AI 모델 서빙의 비용 및 운영 전력 절감을 위한 NPU 최적화 검토 제안",
      "outreach_talk_track": "최근 LG CNS와 구축하신 전용 생성형 AI 플랫폼 및 RAG 기반 금융 업무 혁신 성과를 보고 연락드렸습니다. 금융 폐쇄망 환경의 고유 요구사항을 충족하면서도 가속 장치의 전력과 상면 효율을 극대화할 수 있는 당사 RNGD 기반의 최적화 방안을 함께 제안드립니다.",
      "revenue_timing": "중기",
      "decision_maker_hint": "디지털금융부문장, IT보안기획실장, AI 개발총괄 임원, 시스템운영 플랫폼 부서장",
      "existing_touchpoint": "확인 필요",
      "verification_needed": [
        "기 도입된 EXAONE 3.5 모델에 대응하여 RNGD 컴파일러 환경 연동 가능성 조율",
        "자체 IDC 내에 하드웨어 가속기 추가 설치 가능성 및 전력 예산 여유 확인"
      ],
      "source_ids": [
        "S019"
      ],
      "source_urls": [
        "https://www.news2day.co.kr/article/20260522500024"
      ]
    },
    {
      "name": "건강보험심사평가원",
      "country": "KR",
      "market": "B2G",
      "target_type": "온프레미스 기업",
      "classification": "priority_outreach",
      "confirmed_project_or_signal": "GPU 서버 기반의 원스톱 AI 통합 플랫폼 및 클라우드 구축 드라이브",
      "confirmed_model_name": "미확인",
      "model_match_status": "unknown",
      "model_fit_score": "UNKNOWN",
      "deployment_fit_score": "HIGH",
      "channel_fit_score": "HIGH",
      "rngd_fit_score": "MID",
      "outreach_priority": "HIGH",
      "fit_vs_priority_explanation": "도입 예정 모델이 알려지지 않아 model_fit_score는 UNKNOWN으로 설정했으나, GPU 서버에 기반을 둔 자체적인 AI 통합 플랫폼을 신규 설계하고 클라우드 드라이브를 공동 추진하는 강한 인프라 도입 조달 신호가 존재합니다. 공공 성격의 의료 공공기관의 강한 B2G 도입 구조를 보유하므로 outreach_priority를 HIGH로 결정했습니다.",
      "hook_type": "PROCUREMENT",
      "buying_signal": "김무성 디지털전략실장을 중심으로 GPU 서버 기반의 AI 통합플랫폼 구축 및 클라우드 동시 드라이브 계획을 대외적으로 선언함",
      "infrastructure_signal": "자체 클라우드 센터를 중심으로 가상화 기반의 GPU 서버 및 추론 처리 시스템을 대규모로 가동하고자 함",
      "timing_reason": "평가기관 전환 총력 및 클라우드/AI 통합 플랫폼 로드맵 수립 발표 직후 시점으로, 하드웨어 사양 및 예산 편성 전 단계에서의 규격 협의가 절실한 타이밍임",
      "customer_win": "대규모 진료 정보 및 의료 관련 검색 서비스를 처리할 때 급증할 수 있는 공공 데이터 인프라의 운영 비용을 절감하고, 전력 및 상면 부담을 대폭 해소할 수 있음",
      "furiosa_win": "국내 주요 의료 공공기관의 핵심 추론 인프라 영역에 성공적으로 공급하여 의료 공공 도메인의 강력한 국산 NPU 모범 구축 사례를 획득함",
      "numeric_claims": [],
      "direct_sales_possibility": "HIGH",
      "csp_routed_sales_possibility": "MID",
      "npuaas_adoption_possibility": "LOW",
      "csp_capacity_expansion_possibility": "LOW",
      "contact_reason": "심평원 자체 GPU 기반 AI 플랫폼 계획에 맞춤화된 고효율 NPU 하드웨어 아키텍처 제안 기회 포착",
      "outreach_talk_track": "최근 발표하신 AI·클라우드 드라이브 및 GPU 기반 통합 플랫폼 구축 전략을 보고 연락드렸습니다. 심평원의 AI 공공 서비스 활성화를 위한 고성능·저전력 기반의 하드웨어 운영 효율성 달성에 국산 RNGD 솔루션이 제공할 기여 요소를 소개해 드리고자 합니다.",
      "revenue_timing": "단기",
      "decision_maker_hint": "디지털전략실장(디지털클라우드센터장 겸 AI융합추진단장), 정보화실 총괄책임, 공공 플랫폼 조달 담당자",
      "existing_touchpoint": "확인 필요",
      "verification_needed": [
        "신규 AI 시스템 구축 관련 공공 입찰/나라장터 RFP 조달 규격 확인 필요",
        "의료 영상 및 문서 처리를 위해 검토 예정인 내부 백엔드 모델과의 호환성 조율"
      ],
      "source_ids": [
        "S036"
      ],
      "source_urls": [
        "https://www.etnews.com/20260522000181"
      ]
    },
    {
      "name": "전남소방본부",
      "country": "KR",
      "market": "B2G",
      "target_type": "온프레미스 기업",
      "classification": "structure_check",
      "confirmed_project_or_signal": "에코아이티와 협력하여 Solar LLM 기반 재난 대응 플랫폼 구축 본격화",
      "confirmed_model_name": "Solar LLM",
      "model_match_status": "family_only",
      "model_fit_score": "MID",
      "deployment_fit_score": "HIGH",
      "channel_fit_score": "MID",
      "rngd_fit_score": "MID",
      "outreach_priority": "MID",
      "fit_vs_priority_explanation": "도입 모델이 Upstage Solar LLM 계열로 당사 지원 제품군에 부합하지만 정확한 버전 최적화 검증이 사전에 필요하므로 family_only로 판단하여 model_fit_score와 rngd_fit_score는 MID로 책정했습니다. 소방 업무의 폐쇄망 성격과 K8s 클라우드 기반 구축 사업을 직접 전개하고 있으므로 구조 확인 목적의 MID 우선순위로 매칭했습니다.",
      "hook_type": "PROCUREMENT",
      "buying_signal": "에코아이티를 개발 주체로 선정하여 Solar LLM 및 RAG 기술을 적용하는 지능형 소방행정 지원 및 문서 생성 플랫폼 사업에 착수함",
      "infrastructure_signal": "안정성과 복구 능력을 확보하기 위해 쿠버네티스(K8s) 기반의 독립 클라우드 인프라 아키텍처 환경에 추론 서버 배포를 기획함",
      "timing_reason": "본격적인 플랫폼 구축 및 학습데이터 연계 적용 초기 단계로, 서빙 인프라 단에서의 GPU 부족 해결을 위한 가속 장치 성능 시험을 연계 검토하기 적합함",
      "customer_win": "재난 관리 현장 및 대민 지원 영역에서 빠른 응답성과 고가용성을 지닌 LLM 인프라를 가혹한 환경 하에서도 비용 효율적으로 확보 및 운영할 수 있음",
      "furiosa_win": "안전행정 및 공공 재난 대응이라는 고신뢰성 특수 조달 분야에서 대표적인 국산 추론 가속기 배포 레퍼런스를 다지는 기회가 됨",
      "numeric_claims": [],
      "direct_sales_possibility": "MID",
      "csp_routed_sales_possibility": "MID",
      "npuaas_adoption_possibility": "LOW",
      "csp_capacity_expansion_possibility": "LOW",
      "contact_reason": "Solar LLM 기반 공공 솔루션 전개 시 K8s 가상화 연동 규격 및 저전력 고효율 가속 인프라 제시",
      "outreach_talk_track": "최근 전남소방본부와 에코아이티가 추진하는 Solar LLM 기반 재난 대응 플랫폼 구축 사업을 확인하고 연락드렸습니다. 당사의 RNGD는 쿠버네티스 환경에 유연하게 작동하는 만큼 지능형 소방행정 인프라의 완성도를 저비용으로 개선하는 데 많은 기여를 도울 수 있습니다.",
      "revenue_timing": "중기",
      "decision_maker_hint": "전남소방본부 소방정보화팀장, 에코아이티 프로젝트 수행 PM, 소방 인프라 조달 부서장",
      "existing_touchpoint": "확인 필요",
      "verification_needed": [
        "도입 추진 예정인 Solar LLM의 구체적 파라미터 규격 및 RNGD 상에서의 동작 테스트 일정 확인",
        "소방본부 자체 전산센터 내 물리적 전력 한도 정보 확인"
      ],
      "source_ids": [
        "S028"
      ],
      "source_urls": [
        "https://magazine.hankyung.com/business/article/202605196285b"
      ]
    }
  ],
  "noise_examples": [
    {
      "source_id": "S033",
      "title": "AI·금융 공들이고, 건설교통 공약 ‘쑥’… 재원조달은 ‘어물쩍’",
      "reason": "정당 공약 및 재정 조달 계획 중심의 포괄적인 선거 보도로, 구체적인 엔터프라이즈 AI 플랫폼 도입 및 개별 조달 하드웨어 사업 정보를 내포하지 않아 GTM 비즈니스 리서치 분석 관점에서는 노이즈로 분류됩니다."
    },
    {
      "source_id": "S034",
      "title": "머스크, AI 슈퍼컴퓨터 '콜로서스' 확장 승부수…xAI, 초대형 GPU 전쟁 본...",
      "reason": "글로벌 xAI의 미국 인프라 확장과 관련된 외신 동향 기사로, 한국이나 일본 내 FuriosaAI 영업에 직접적으로 연결 가능한 로컬 GTM 영업 대상 및 인프라 파트너십 구축 신호로 활용하기는 어렵습니다."
    },
    {
      "source_id": "S035",
      "title": "LS일렉트릭·HD현대일렉트릭 주목 배경…AI 시대 전력망 전쟁 본격화 예...",
      "reason": "전력 기자재 및 데이터센터 수요 증가에 따른 일반적인 금융 시장 및 산업 주식 분석용 뉴스로, 실제 가속기를 구매하고 배포를 구체적으로 확정한 주체 식별이 모호해 세일즈 타깃 발굴 기회에서 배제하였습니다."
    }
  ],
  "eval_notes": [
    "경쟁사인 알리바바가 코딩 및 에이전트 작업용 모델 Qwen 3.7-Max 출시와 함께 독자 AI 가속기 '전우 M890'을 신규 공개(S006, S029)하며 자사 전용 인프라 및 금융 영역 고객 유치를 활발히 전개하는 흐름입니다. 국산 AI 가속기의 지배력 수호를 위해 국내 금융·공공 GTM 공략 시 기술적 경쟁 장치를 신속하게 선점해야 합니다.",
    "삼성SDS는 경기 동탄 데이터센터에 20MW급 전력을 추가 조달하고, 경북 구미에 60MW AI 데이터센터 구축을 본격 투입하는 등 데이터센터 전력 자립 노력을 가속화하고 있습니다(S003, S009). 이는 당사 RNGD가 지닌 최대 차별적 이점인 저전력 설계 및 전력 효율 향상 성능(Rack density 최적화)을 파트너사 기술 설계단에 침투시킬 우수한 진입 명분으로 작용합니다.",
    "B2G 시장에 맞추어 한글과컴퓨터와 LG AI연구원이 공공 행정 AI 수주 연합 전선을 결성함에 따라(S020) 해당 챗엑사원 플랫폼에 대한 국산 NPU 탑재 추진 가능성이 매우 긍정적입니다. 즉각적인 하드웨어 조달 파트너십 제안이 긴요하며 차기 주력 사업인 K-EXAONE 로드맵 지원 사양과 접목을 면밀하게 선행 추진할 필요가 있습니다."
  ]
}
```