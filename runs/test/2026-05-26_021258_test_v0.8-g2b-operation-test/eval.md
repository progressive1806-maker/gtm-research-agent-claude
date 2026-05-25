# LLM Evaluation Notes

## LLM metadata

- provider: `gemini`
- model: `gemini-3.5-flash`
- llm_sources_count: `40`
- max_llm_sources: `40`
- max_source_chars: `800`
- max_output_candidates: `12`
- evaluated_at_kst: `2026-05-26T02:21:42.416604+09:00`

## Run summary

- overall_assessment: 최근 7일간의 국내 GTM 신호 조사 결과, 삼성SDS의 대규모 AI 데이터센터 투자 및 전력 확보 계획과 엘리스그룹의 코스닥 상장예비심사 청구에 따른 GPUaaS 인프라 확장 등 고유한 인프라 기회가 포착되었습니다. 또한 LG AI연구원의 EXAONE-4.0 모델 공식 precompiled 정합성을 바탕으로 한글과컴퓨터와의 공공 AX 에이전트 연합, 전남소방본부의 Solar LLM 기반 재난 안전 플랫폼 등 즉각적인 POC 및 수주 대응이 가능한 단기 매출 기회들이 식별되어 정밀한 BD 우선 접촉이 요구됩니다.
- top_priority_names: 삼성SDS, 엘리스그룹, 한글과컴퓨터, 에코아이티
- noise_ratio_comment: 공개 기사 분석 중 망분리 완화에 대한 일반론적인 금융 정책 뉴스 및 자국 가속기를 탑재한 해외 알리바바 동향 등 직접적인 타겟 가치가 부재한 노이즈 기사들이 일부 혼재되어 분류 과정에서 정리하였습니다.
- model_compatibility_caution: EXAONE 계열의 경우 4.0 버전은 공식 precompiled 호환 대상이지만, 농협은행 사례에서 언급되는 EXAONE 3.5 모델 등은 family_only에 해당하므로 정밀한 아키텍처 호환성 검증 단계가 필수적입니다.

## Eval notes

- 삼성SDS 및 NHN클라우드 등 주요 국산 CSP들의 동탄/구미 데이터센터 가속기 전력 및 요금 우려 신호는 RNGD의 저전력 소버린 소구력과 정확히 일치하여 고유한 마켓 타이밍을 보여줍니다.
- 한컴 및 LG AI연구원의 엑사원 4.0 연동 행정망 공략과 전남소방본부의 Solar RAG 프로젝트 등 precompiled 모델 정합성을 완비한 B2G 단기 레퍼런스를 개척해 신속한 매출 창출로 연결하는 전방위BD 활동이 강력히 요구됩니다.

## Raw LLM response

```json
{
  "run_summary": {
    "overall_assessment": "최근 7일간의 국내 GTM 신호 조사 결과, 삼성SDS의 대규모 AI 데이터센터 투자 및 전력 확보 계획과 엘리스그룹의 코스닥 상장예비심사 청구에 따른 GPUaaS 인프라 확장 등 고유한 인프라 기회가 포착되었습니다. 또한 LG AI연구원의 EXAONE-4.0 모델 공식 precompiled 정합성을 바탕으로 한글과컴퓨터와의 공공 AX 에이전트 연합, 전남소방본부의 Solar LLM 기반 재난 안전 플랫폼 등 즉각적인 POC 및 수주 대응이 가능한 단기 매출 기회들이 식별되어 정밀한 BD 우선 접촉이 요구됩니다.",
    "top_priority_names": [
      "삼성SDS",
      "엘리스그룹",
      "한글과컴퓨터",
      "에코아이티"
    ],
    "noise_ratio_comment": "공개 기사 분석 중 망분리 완화에 대한 일반론적인 금융 정책 뉴스 및 자국 가속기를 탑재한 해외 알리바바 동향 등 직접적인 타겟 가치가 부재한 노이즈 기사들이 일부 혼재되어 분류 과정에서 정리하였습니다.",
    "model_compatibility_caution": "EXAONE 계열의 경우 4.0 버전은 공식 precompiled 호환 대상이지만, 농협은행 사례에서 언급되는 EXAONE 3.5 모델 등은 family_only에 해당하므로 정밀한 아키텍처 호환성 검증 단계가 필수적입니다."
  },
  "candidates": [
    {
      "name": "삼성SDS",
      "country": "KR",
      "market": "B2B",
      "target_type": "CSP 운영 기업",
      "classification": "priority_outreach",
      "confirmed_project_or_signal": "경북 구미 및 경기 동탄 데이터센터 인프라 확충에 따른 고전력 부담 극복 및 SCP 클라우드 AI 비즈니스 확대",
      "confirmed_model_name": "미확인",
      "model_match_status": "unknown",
      "model_fit_score": "UNKNOWN",
      "deployment_fit_score": "HIGH",
      "channel_fit_score": "HIGH",
      "rngd_fit_score": "MID",
      "outreach_priority": "HIGH",
      "fit_vs_priority_explanation": "구체적인 지원 모델 정보는 불명확하여 모델 정합성은 UNKNOWN으로 분류되나, 구미 60MW 및 동탄 20MW 전력 인프라 확대와 국내 핵심 CSP 파트너십 가치를 종합 고려해 삼성SDS 맞춤형 가속기 운영 기회로 평가하여 최고의 우선순위로 책정함.",
      "hook_type": "POWER",
      "buying_signal": "경북 구미 AI 데이터센터 대규모 투자를 확정하고 동탄 데이터센터의 전력 확보를 마쳐 가속 인프라 기획을 강화하고 있음.",
      "infrastructure_signal": "구미 데이터센터에 4273억원을 투자하여 60MW 규모의 전력을 기획 중이며, 동탄 데이터센터 서관 운영을 위해서도 20MW급 전력을 확보하는 등 고전력 부담이 커지는 환경임.",
      "timing_reason": "대규모 인프라 투자 발표와 연계하여 저전력 추론 최적화 가속기 제안을 본격화할 수 있는 적절한 도입 설계 단계임.",
      "customer_win": "데이터센터 전력 및 에너지 비용 급등 상황에서 전력 대 성능비가 우수한 RNGD를 동사 인프라에 도입함으로써 고가 GPU 위주 구성의 마진 압박을 개선하고 원가 경쟁력을 다질 수 있음.",
      "furiosa_win": "국내 최고 수준의 대형 CSP 파트너 채널을 공고히 선점하여 동사 클라우드를 통해 대형 그룹사 및 금융권으로 RNGD 기반의 간접 수요와 추가 서버 공급 계약을 대량 창출함.",
      "numeric_claims": [
        {
          "claim": "경북 구미 4273억원 투자, 60MW 규모 AI 데이터센터",
          "source_id": "S010",
          "source_url": "https://www.mt.co.kr/tech/2026/05/23/2026052210211399740",
          "evidence_text": "삼성SDS는 경북 구미에 4273억원을 투자해 60MW 규모 AI 데이터센터를 짓기로 했다."
        },
        {
          "claim": "동탄 데이터센터 20MW급 전력 확보",
          "source_id": "S003",
          "source_url": "https://www.e-science.co.kr/news/articleView.html?idxno=130004",
          "evidence_text": "삼성SDS가 경기 동탄 데이터센터 서관 가동을 위해 20MW급 전력을 확보한 사례도 이런 상황을 보여준다."
        }
      ],
      "direct_sales_possibility": "MID",
      "csp_routed_sales_possibility": "HIGH",
      "npuaas_adoption_possibility": "HIGH",
      "csp_capacity_expansion_possibility": "HIGH",
      "contact_reason": "전력 확보 부담 완화 및 고전력 가속기 대체 포트폴리오 기획에 맞추어 저전력 추론 하드웨어 제안",
      "outreach_talk_track": "최근 경북 구미 60MW 규모 신규 데이터센터 투자 및 동탄 전력 확보 발표 소식을 접하고 연락드렸습니다. 데이터센터 전력 수급과 에너지 원가 부담이 심화되는 시점에서, 동사 클라우드 인프라의 TCO를 극적으로 절감할 수 있는 저전력 가속기 RNGD 적용 방안을 보고드리고자 합니다.",
      "revenue_timing": "단기",
      "decision_maker_hint": "CTO, Head of Cloud, Head of Infrastructure, Head of Data Center",
      "existing_touchpoint": "확인 필요",
      "verification_needed": [
        "경북 구미 및 동탄 데이터센터 내 RNGD 가상화 규격 검토 가능 여부"
      ],
      "source_ids": ["S003", "S010", "S039"],
      "source_urls": [
        "https://www.e-science.co.kr/news/articleView.html?idxno=130004",
        "https://www.mt.co.kr/tech/2026/05/23/2026052210211399740",
        "https://www.sedaily.com/article/20047365?ref=naver"
      ]
    },
    {
      "name": "엘리스그룹",
      "country": "KR",
      "market": "B2B",
      "target_type": "CSP 운영 기업",
      "classification": "priority_outreach",
      "confirmed_project_or_signal": "코스닥 시장 상장을 통한 자금 확보 및 자체 모듈형 데이터센터(PMDC) 중심의 GPUaaS 사업 전면 확장",
      "confirmed_model_name": "미확인",
      "model_match_status": "unknown",
      "model_fit_score": "UNKNOWN",
      "deployment_fit_score": "HIGH",
      "channel_fit_score": "HIGH",
      "rngd_fit_score": "MID",
      "outreach_priority": "HIGH",
      "fit_vs_priority_explanation": "특정 도입 모델명이 확인되지 않아 모델 적합도는 UNKNOWN이나, 코스닥 상장과 맞물려 자체 이동식 모듈형 데이터센터 인프라 포트폴리오를 빠르게 확장하는 선도적인 AI 인프라 파트너이므로 최우선 영업 접촉이 권장됨.",
      "hook_type": "CLOUD",
      "buying_signal": "한국거래소에 상장예비심사청구서를 제출하며 본격적인 AI 클라우드 인프라 인프라스트럭처 선점과 고도화 의지를 피력함.",
      "infrastructure_signal": "자체 이동식 모듈형 데이터센터(AI PMDC) 인프라 및 대규모 GPUaaS 관리 시스템을 독자 구축하여 구동하고 있음.",
      "timing_reason": "기업공개(IPO) 추진으로 시장 입지 제고와 추가 투자가 예정된 최적의 인프라 전환 도입 제휴 시점임.",
      "customer_win": "동사가 강점으로 삼는 소형 모듈형 데이터센터의 제한된 공간 및 전력 환경에서, 에너지 절감형 RNGD 가속기를 채택하여 동일 상면당 추론 가용량을 높이고 원가를 낮출 수 있음.",
      "furiosa_win": "상장 준비 단계의 파격적이고 유연한 성장 파트너를 확보하여, 동사가 운영하는 GPUaaS 생태계 전반에 RNGD를 선탑재 공급하는 성과를 도출함.",
      "numeric_claims": [],
      "direct_sales_possibility": "HIGH",
      "csp_routed_sales_possibility": "MID",
      "npuaas_adoption_possibility": "HIGH",
      "csp_capacity_expansion_possibility": "HIGH",
      "contact_reason": "이동식 데이터센터 및 GPUaaS 인프라 확장을 겨냥한 저전력 고가성비 국산 추론 가속기 라인업 추가 제안",
      "outreach_talk_track": "최근 코스닥 상장예비심사 신청과 함께 풀스택 AI 인프라 사업 강화를 선언하신 소식을 기쁘게 접했습니다. 동사의 주력 제품군인 이동식 모듈형 데이터센터 내의 전력 효율을 개선하고 가속기 가격 압박을 타개할 수 있는 대안으로 RNGD 하드웨어 테스트 기회를 상호 논의해 보고자 합니다.",
      "revenue_timing": "단기",
      "decision_maker_hint": "김재원 대표이사, CTO, Head of AI Cloud Unit",
      "existing_touchpoint": "확인 필요",
      "verification_needed": [
        "엘리스 모듈형 데이터센터 인프라 내부의 전력 밀도 및 하드웨어 폼팩터 실질 규격"
      ],
      "source_ids": ["S013", "S014", "S015", "S017"],
      "source_urls": [
        "http://www.hansbiz.co.kr/news/articleView.html?idxno=839792",
        "http://www.joseilbo.com/news/news_read.php?uid=568639&class=53&grp=",
        "https://www.fetv.co.kr/news/articleView.html?idxno=302765",
        "https://www.newspim.com/news/view/20260520000146"
      ]
    },
    {
      "name": "한글과컴퓨터",
      "country": "KR",
      "market": "B2B",
      "target_type": "온프레미스 기업",
      "classification": "priority_outreach",
      "confirmed_project_or_signal": "LG AI연구원과의 동맹을 기반으로 한 챗엑사원 결합 AI 문서 에이전트 출시 및 공공 AX 조달 시장 수주전 본격 진입",
      "confirmed_model_name": "EXAONE",
      "model_match_status": "family_only",
      "model_fit_score": "MID",
      "deployment_fit_score": "HIGH",
      "channel_fit_score": "HIGH",
      "rngd_fit_score": "MID",
      "outreach_priority": "HIGH",
      "fit_vs_priority_explanation": "EXAONE-4.0 모델은 FuriosaAI에 공식 지원 및 프리컴파일 가속이 가능하나, 구체적인 연동 버전은 아키텍처에 따라 조율이 필요한 패밀리군에 머물러 MID로 평가함. 단, 공공기관 및 부처 중심의 폐쇄망 영업력이 매우 탄탄하여 상업적 우선순위는 HIGH로 상향함.",
      "hook_type": "SOVEREIGN",
      "buying_signal": "LG AI연구원과의 동맹 협약을 통해 자사 문서 에이전트와 초거대 모델 '챗엑사원'을 밀접하게 결합하여 정부부처 및 공공기관에 수주를 대응하겠다고 명확히 밝혔음.",
      "infrastructure_signal": "주요 타겟이 망분리 및 정보 주권이 강하게 걸린 공기업과 지자체이며, 프라이빗 온프레미스 혹은 온디바이스형 AI 어플라이언스 수주를 지향함.",
      "timing_reason": "협력 발표 이후 각 공공부처의 예산 심사 및 실행형 조달 프로젝트 발주가 본격화되어, 연계 솔루션 아키텍처를 사전에 구성해야 하는 시기임.",
      "customer_win": "엄격한 공공기관의 폐쇄망 규제를 충족하며, LG AI연구원 모델 가속이 기 검증된 고효율 국산 가속기를 자사 패키지에 통합 구성함으로써 공공 납품 예산 경쟁력에서 절대적 우위를 점할 수 있음.",
      "furiosa_win": "동사의 강력한 공공 AX 수주 전선에 가속 엔진 파트너로 협력 연동함으로써, 대규모 공공 행정 문서 AI 서빙 시스템에 RNGD를 일괄 침투시키는 성과를 획득함.",
      "numeric_claims": [],
      "direct_sales_possibility": "MID",
      "csp_routed_sales_possibility": "MID",
      "npuaas_adoption_possibility": "LOW",
      "csp_capacity_expansion_possibility": "LOW",
      "contact_reason": "공공 행정망 전용 문서 AI 어플라이언스 구성 및 최적화 연계를 위한 RNGD 공동 가속 하드웨어 제휴 제안",
      "outreach_talk_track": "한컴의 문서 에이전트와 LG AI연구원 챗엑사원 결합 솔루션의 공공 공략 발표를 관심 있게 모니터링해왔습니다. 공공부처 온프레미스 구축 시 인프라 예산 문턱을 획기적으로 개선하며, 이미 엑사원-4.0 서빙이 최적화 완료된 RNGD를 활용하여 공공 AX 수주 승률을 높이는 협력 방안을 제안드리고자 합니다.",
      "revenue_timing": "단기",
      "decision_maker_hint": "CTO, Head of Public Sector Sales, Head of AI Platform",
      "existing_touchpoint": "확인 필요",
      "verification_needed": [
        "챗엑사원 패키지 서빙 엔진의 vLLM 호환성 상태 검증"
      ],
      "source_ids": ["S021", "S022", "S023", "S025"],
      "source_urls": [
        "http://www.newslock.co.kr/news/articleView.html?idxno=130504",
        "https://www.mt.co.kr/tech/2026/05/22/2026052215283358675",
        "https://www.mk.co.kr/article/12055579",
        "https://www.newsis.com/view/NISX20260522_0003640664"
      ]
    },
    {
      "name": "에코아이티",
      "country": "KR",
      "market": "B2G",
      "target_type": "온프레미스 기업",
      "classification": "priority_outreach",
      "confirmed_project_or_signal": "전남소방본부 AI 기반 재난 대응 플랫폼 구축 사업 본격 수주에 따른 Solar LLM 기반 시스템 전개",
      "confirmed_model_name": "Solar 1.0",
      "model_match_status": "exact_supported",
      "model_fit_score": "HIGH",
      "deployment_fit_score": "HIGH",
      "channel_fit_score": "MID",
      "rngd_fit_score": "HIGH",
      "outreach_priority": "HIGH",
      "fit_vs_priority_explanation": "도입에 나서는 Solar LLM(SOLAR-10.7B 등) 모델 계열은 FuriosaAI 공개 문서상 공식 지원 및 precompiled 검증이 완비된 exact_supported 유형이며, 소방 인프라의 실시간 반응에 초저지연 하드웨어 최적화 정합성이 완벽하여 최우선 순위로 조준함.",
      "hook_type": "PROCUREMENT",
      "buying_signal": "전남소방본부 전용의 RAG 기반 소방 행정 및 재난 대응 플랫폼 구축 사업자로 최종 수주되어 본격 착수를 예고함.",
      "infrastructure_signal": "쿠버네티스(K8s) 기반의 클라우드 구조와 업스테이지의 Solar 엔진을 적용하여 대량의 구조 문서를 정밀 처리하는 실 구축 인프라임.",
      "timing_reason": "전남소방본부의 실 구축 인프라 서버 및 클라우드 플랫폼 아키텍처 구성을 최종 조율하는 초기 구축 국면임.",
      "customer_win": "긴박한 재난 분석 현장에서 소방대원에게 지연 없이 가동되는 초고속 추론 환경을 제공하며, 쿠버네티스 환경에 드롭인 연동되어 도입 후 신속한 서빙 스택 배포가 완벽히 보장됨.",
      "furiosa_win": "소방 및 안전 재난 관리 시스템의 국가 인프라 구축 핵심 트랙에 RNGD를 공식 채택시켜 중장기 다른 지자체 소방본부 확장의 결정적 선례를 선점함.",
      "numeric_claims": [],
      "direct_sales_possibility": "HIGH",
      "csp_routed_sales_possibility": "LOW",
      "npuaas_adoption_possibility": "LOW",
      "csp_capacity_expansion_possibility": "LOW",
      "contact_reason": "쿠버네티스 구조 및 Solar LLM 구동을 지원하는 최첨단 국산 가속기 RNGD 적용 논의",
      "outreach_talk_track": "최근 전남소방본부의 지능형 재난 대응 플랫폼 구축 사업 수주 성공을 지심으로 축하드립니다. 본 사업에 도입되는 Solar LLM은 당사의 RNGD에서 완벽히 구동이 지원되며, 네이티브 쿠버네티스 및 최적화 서빙 솔루션을 통해 재난 안전 플랫폼의 실시간 연산 성능과 시스템 가용 비용을 대폭 개선할 수 있습니다.",
      "revenue_timing": "단기",
      "decision_maker_hint": "CTO, Project Manager, Platform Infrastructure Lead",
      "existing_touchpoint": "확인 필요",
      "verification_needed": [
        "전남소방본부 소유 온프레미스 인프라 구동용 하드웨어 단독 발주 방식 확인"
      ],
      "source_ids": ["S029"],
      "source_urls": [
        "https://magazine.hankyung.com/business/article/202605196285b"
      ]
    },
    {
      "name": "우리은행",
      "country": "KR",
      "market": "B2B",
      "target_type": "CSP 고객 기업",
      "classification": "cloud_npuaaS_lead",
      "confirmed_project_or_signal": "AI 에이전트 구축 사업 우선협상대상자로 삼성SDS를 선정하여 금융 AX 시스템 확대 추진",
      "confirmed_model_name": "미확인",
      "model_match_status": "unknown",
      "model_fit_score": "UNKNOWN",
      "deployment_fit_score": "HIGH",
      "channel_fit_score": "HIGH",
      "rngd_fit_score": "MID",
      "outreach_priority": "HIGH",
      "fit_vs_priority_explanation": "특정 AI 모델은 미공개로 UNKNOWN 상태이나, 삼성SDS를 핵심 파트너이자 주사업자로 선정하여 금융권 최초의 AX 플랫폼 가동을 추진하고 있으므로, 삼성SDS 채널 연동을 통한 가속 인프라 유도가 매우 강력하게 성립되어 최우선으로 분석함.",
      "hook_type": "PARTNER",
      "buying_signal": "자산관리 보고서 생성 및 고객 가치 중심의 CRM 혁신을 주도할 AI 에이전트 프로젝트 우선협상자로 삼성SDS를 조기 지정함.",
      "infrastructure_signal": "삼성SDS의 전문 금융 전용 클라우드나 고도의 프라이빗 전용 가상 서버 아키텍처를 연동할 개연성이 짙음.",
      "timing_reason": "구축 사업자 낙찰 발표 직후 시스템 개발과 서버 구성의 초기 설계가 확정되기 이전 최상의 타이밍임.",
      "customer_win": "삼성SDS 가상화 솔루션 기반 인프라에서 가동되어, 과다한 GPU 수급 비용 한계를 극복하고 제1금융권의 규제 준수 하에 합리적 예산으로 전행 상담 AI 플랫폼을 가치 높게 구현함.",
      "furiosa_win": "삼성SDS를 경유한 제1금융권 영업 협력 트랙을 최초 성공시켜, 국내 대규모 금융 엔터프라이즈 내에 당사 NPU 기반의 대화형 서비스를 실 서비스 연동함.",
      "numeric_claims": [],
      "direct_sales_possibility": "LOW",
      "csp_routed_sales_possibility": "HIGH",
      "npuaas_adoption_possibility": "HIGH",
      "csp_capacity_expansion_possibility": "MID",
      "contact_reason": "우리은행 에이전트 서빙 트래픽 처리를 위한 삼성SDS 연계 고가성비 가속 하드웨어 제안",
      "outreach_talk_track": "귀행의 AI 에이전트 사업 진행 및 삼성SDS 파트너십 소식을 관심 깊게 지켜보고 있습니다. 금융 인프라의 안정성을 검증하면서도 대량의 검색RAG 질의를 가성비 높게 처리할 수 있도록, 삼성SDS 플랫폼에 맞춤 정합된 국산 가속기 RNGD 적용 이점을 상세히 제안드리고자 합니다.",
      "revenue_timing": "단기",
      "decision_maker_hint": "CIO, Head of AI Business, Head of CRM Transformation",
      "existing_touchpoint": "확인 필요",
      "verification_needed": [
        "우리은행 내부 프라이빗 AI 에이전트에 적용할 미세조정 예정 LLM 종류"
      ],
      "source_ids": ["S026", "S028"],
      "source_urls": [
        "https://www.sedaily.com/article/20046605?ref=naver",
        "https://www.sedaily.com/article/20046505?ref=naver"
      ]
    },
    {
      "name": "건강보험심사평가원",
      "country": "KR",
      "market": "B2G",
      "target_type": "온프레미스 기업",
      "classification": "structure_check",
      "confirmed_project_or_signal": "디지털클라우드센터 기반 독자 AI 통합 플랫폼 구축 추진 및 원스톱 서비스 체계 기획",
      "confirmed_model_name": "미확인",
      "model_match_status": "unknown",
      "model_fit_score": "UNKNOWN",
      "deployment_fit_score": "HIGH",
      "channel_fit_score": "MID",
      "rngd_fit_score": "MID",
      "outreach_priority": "HIGH",
      "fit_vs_priority_explanation": "사용 모델 사양은 명확히 드러나지 않아 UNKNOWN이나, 공공 핵심 의료기관으로서 자체 디지털클라우드센터 내 GPU 기반 독자적인 서버 및 원스톱 개발 AI 플랫폼 가동을 선언했으므로 인프라 및 바이어 신호가 매우 강력해 HIGH로 평가함.",
      "hook_type": "PROCUREMENT",
      "buying_signal": "디지털전략실장이 지휘하는 'AI·클라우드 동시 드라이브' 계획을 발표하며, 기관 내부 GPU 서버 기반의 독자 AI 서비스 구축 계획을 천명함.",
      "infrastructure_signal": "대국민 의료기관 탐색 등을 위한 자체 디지털클라우드센터 기반의 연산 인프라 기획 수립 상태임.",
      "timing_reason": "전략적 평가기관 전환이라는 공공 목표 기정 사실화에 따라 대규모 서버 장비의 조달 계획 수립이 예정된 타이밍임.",
      "customer_win": "민감한 공공 보건 의료 데이터를 온프레미스로 철저히 보호하는 동시에, 국산 가속기를 통해 정부 저전력 및 에너지 절감 정책에 완벽히 상응하는 의료 정보 행정 플랫폼을 소유함.",
      "furiosa_win": "B2G 헬스케어 최고 핵심 기관에 주도적으로 입찰 참여 혹은 파트너 협업하여 국가 공공 부문 독보적인 NPU 시스템 입지를 성취함.",
      "numeric_claims": [],
      "direct_sales_possibility": "HIGH",
      "csp_routed_sales_possibility": "MID",
      "npuaas_adoption_possibility": "LOW",
      "csp_capacity_expansion_possibility": "LOW",
      "contact_reason": "심평원 독자 디지털클라우드센터 내부 전용 가속 서버로 저전력 고효율 RNGD 기술 입찰 연계 협의",
      "outreach_talk_track": "귀원 디지털전략실 주도의 AI·클라우드 동시 가동 추진 발표를 무척 뜻깊게 살펴보았습니다. 귀원에서 독자 구축을 기획하고 계시는 자체 GPU 서버 기반 AI 통합 플랫폼의 예산 효율과 유지 보수 이점을 높일 수 있도록, 국가 보급형 국산 고성능 NPU RNGD의 가용 방안을 논의드리고자 합니다.",
      "revenue_timing": "단기",
      "decision_maker_hint": "김무성 디지털전략실장, Head of Digital Cloud Center",
      "existing_touchpoint": "확인 필요",
      "verification_needed": [
        "건강보험심사평가원 AI 통합 플랫폼 내부 가속 하드웨어 정형 RFP 개시 일정"
      ],
      "source_ids": ["S035"],
      "source_urls": [
        "https://www.etnews.com/20260522000181"
      ]
    },
    {
      "name": "NHN클라우드",
      "country": "KR",
      "market": "B2B",
      "target_type": "CSP 운영 기업",
      "classification": "priority_outreach",
      "confirmed_project_or_signal": "초거대 GPU 클러스터 및 AI 가속 클라우드 비즈니스 추진 및 인프라 고도화",
      "confirmed_model_name": "미확인",
      "model_match_status": "unknown",
      "model_fit_score": "UNKNOWN",
      "deployment_fit_score": "HIGH",
      "channel_fit_score": "HIGH",
      "rngd_fit_score": "MID",
      "outreach_priority": "HIGH",
      "fit_vs_priority_explanation": "구체적인 추론 타겟 모델 사양은 불확실해 UNKNOWN이나, 국내 CSP 얼라이언스 중추 멤버이며 초거대 규모의 가속 클러스터를 전략적으로 확장하고 있어 가속기 탑재 가능성이 극도로 커 HIGH로 분석함.",
      "hook_type": "CLOUD",
      "buying_signal": "동종 CSP와의 에너지 절감 및 GPU난 해결 공동 연대 선언과 함께 이노그리드 인수를 토대로 한 독자 AI 클라우드 확장 공세를 시작함.",
      "infrastructure_signal": "광주 등에 가속 전용 초대형 데이터센터 인프라를 확장해 가동 중이며 전력 비용 부담을 최소화할 하드웨어가 필요함.",
      "timing_reason": "인수합병 마무리 및 신년 기자간담회 전개에 이어 인프라 공급 다각화 결정이 구체화되는 최상의 접촉 적기임.",
      "customer_win": "데이터센터 에너지 요금 급등 압박 하에서, 전력 밀도 및 냉각 효율이 검증된 RNGD를 활용하여 가속 서비스 운용 비용을 크게 아끼고 고객 가성비 NPUaaS 라인업을 활성화할 수 있음.",
      "furiosa_win": "국내 주요 대형 CSP 파트너와 공동 연대를 구축하고, 동사 클라우드를 채택하려는 많은 엔터프라이즈에 RNGD 가속기를 대폭 전파하는 매출 교두보 확보함.",
      "numeric_claims": [],
      "direct_sales_possibility": "MID",
      "csp_routed_sales_possibility": "HIGH",
      "npuaas_adoption_possibility": "HIGH",
      "csp_capacity_expansion_possibility": "HIGH",
      "contact_reason": "대규모 인프라 전력 최적화 및 신규 저전력 NPUaaS 상품 출시를 위한 비즈니스 모델 파트너십 구축",
      "outreach_talk_track": "최근 NHN클라우드의 독자적인 이노그리드 통합 및 초거대 가속기 클러스터 사업 다각화 계획을 기쁘게 들었습니다. 폭발적인 클라우드 가속기 수요 대응 과정에서, GPU 대안으로 전력 효율이 매우 뛰어난 국산 RNGD를 동사 NPUaaS 서비스에 정식 포함시키는 방안을 공동 논의해 보고자 합니다.",
      "revenue_timing": "단기",
      "decision_maker_hint": "CTO, Head of Infrastructure Division, Head of AI Business",
      "existing_touchpoint": "확인 필요",
      "verification_needed": [
        "NHN클라우드 통합 인프라 내 RNGD 가상화 솔루션 지원 상태 검토"
      ],
      "source_ids": ["S005", "S031"],
      "source_urls": [
        "https://www.ddaily.co.kr/page/view/2026052017342600376",
        "https://www.ddaily.co.kr/page/view/2026052216371975959"
      ]
    },
    {
      "name": "LG AI연구원",
      "country": "KR",
      "market": "B2B",
      "target_type": "CSP 운영 기업",
      "classification": "priority_outreach",
      "confirmed_project_or_signal": "EXAONE-4.0 모델 기반 휴머노이드 파운데이션 모델 고도화 및 공공 AX 동맹 강화",
      "confirmed_model_name": "EXAONE-4.0",
      "model_match_status": "exact_supported",
      "model_fit_score": "HIGH",
      "deployment_fit_score": "HIGH",
      "channel_fit_score": "HIGH",
      "rngd_fit_score": "HIGH",
      "outreach_priority": "HIGH",
      "fit_vs_priority_explanation": "EXAONE-4.0-32B가 FuriosaAI에 precompiled 및 공식 지원 대상으로 안착되어 기술 정합도상 HIGH 등급을 보장하며, 실제 GTM 협력과 다수의 기업 고객을 이미 공유하는 고부가가치 타겟이므로 최고의 영업 관리를 유지함.",
      "hook_type": "VLLM",
      "buying_signal": "국책 과제 주도로 엑사원 탑재 K-휴머노이드 모델 확장을 예고하고, 자사 초거대 '챗엑사원'의 공공기관 납품 제휴를 다각화하기 시작함.",
      "infrastructure_signal": "K-휴머노이드 연구단의 대용량 행동 가속 및 챗엑사원 전술망 서빙 아키텍처 인프라를 자체 수급하고 설계하는 중임.",
      "timing_reason": "국책 국방/로보틱스 사업 3차년도 이행 시점과 공공 AX 부처 공동 낙찰 협력이 동시다발적으로 개시된 골든 타임임.",
      "customer_win": "자체 연구한 거대 아키텍처를 추론 최적화 하드웨어에 다이렉트 연동시켜 연산 반응성과 전력 밀도를 극대화하고 전반적인 GPU 보유 비용을 대폭 개선함.",
      "furiosa_win": "강력한 파운데이션 모델 개발 연합을 완성하고, EXAONE 구동의 표준 레퍼런스 가속기로 동반 안착해 생태계적 영향력을 압도적으로 장악함.",
      "numeric_claims": [
        {
          "claim": "K-휴머노이드 국책 사업 3차년도에 비디오캡처 기반 인터페이스 도입",
          "source_id": "S027",
          "source_url": "https://www.ddaily.co.kr/page/view/2026052016512856045",
          "evidence_text": "3차년도에는 비디오캡처 기반 인터페이스를 도입해 착용 장비 없이도 다수 사용자가 데이터 수집에 참여할..."
        }
      ],
      "direct_sales_possibility": "HIGH",
      "csp_routed_sales_possibility": "MID",
      "npuaas_adoption_possibility": "LOW",
      "csp_capacity_expansion_possibility": "LOW",
      "contact_reason": "엑사원 4.0 모델의 연산 성능 극대화 및 차세대 로보틱스 전용 서버 인프라에 RNGD 탑재 논의",
      "outreach_talk_track": "귀원의 국책 K-휴머노이드 착수와 공공 챗엑사원 서비스 확장 성과를 매우 기쁘게 지켜보고 있습니다. 당사의 RNGD 가속기는 EXAONE-4.0 연동 성능이 이미 검증되었으므로, 실시간 대화형 서비스 및 연구 단말용 초고속 저지연 추론 인프라 최적화 방안을 함께 실현해 가고자 합니다.",
      "revenue_timing": "단기",
      "decision_maker_hint": "CTO, Head of AI Research, Project Lead",
      "existing_touchpoint": "확인 필요",
      "verification_needed": [
        "휴머노이드 데이터 수집 및 실시간 제어에 들어가는 구체적 하드웨어 폼팩터 형태"
      ],
      "source_ids": ["S021", "S027", "S039"],
      "source_urls": [
        "http://www.newslock.co.kr/news/articleView.html?idxno=130504",
        "https://www.ddaily.co.kr/page/view/2026052016512856045",
        "https://www.sedaily.com/article/20047365?ref=naver"
      ]
    },
    {
      "name": "NH농협은행",
      "country": "KR",
      "market": "B2B",
      "target_type": "온프레미스 기업",
      "classification": "structure_check",
      "confirmed_project_or_signal": "내부규정 및 금융 영업 지정을 타겟팅한 전용 생성형 AI 플랫폼 구축 및 엑사원 적용 가동",
      "confirmed_model_name": "EXAONE",
      "model_match_status": "family_only",
      "model_fit_score": "MID",
      "deployment_fit_score": "HIGH",
      "channel_fit_score": "MID",
      "rngd_fit_score": "MID",
      "outreach_priority": "MID",
      "fit_vs_priority_explanation": "사용 모델인 엑사원 3.5는 아키텍처적 조율이 다소 필요한 family_only 대상이며, 구축사 LG CNS와의 추가 하드웨어 정합 검증이 수반되어야 하므로 MID 수준의 영업 단계로 평가함.",
      "hook_type": "SOVEREIGN",
      "buying_signal": "전행 전용 초거대 AI 기반의 플랫폼 구축을 완수하여 내부 업무 리테일 지원 및 RAG 검색을 연동 운영하기 시작함.",
      "infrastructure_signal": "망분리 및 내부 업무 처리를 위한 전용의 온프레미스 프라이빗 데이터 서버 환경을 조성함.",
      "timing_reason": "초기 구축 시스템의 실질 전행 전파 및 추가 트래픽 처리를 겨냥해 추론 속도 고도화 투자를 타진할 수 있는 국면임.",
      "customer_win": "엄격한 망분리 규제를 완벽하게 준수하면서도, 전용 EXAONE 구동에 뛰어난 저전력 가속기로 인프라를 교체하여 서버 유지 관리 비용과 상면 공간 부담을 경감할 수 있음.",
      "furiosa_win": "제1금융권의 성공적인 프라이빗 엑사원 구축 사례를 선제 장악해 실증 레퍼런스로 전환시킴으로써 동종 업계 확산의 강력한 지렛대로 활용함.",
      "numeric_claims": [],
      "direct_sales_possibility": "MID",
      "csp_routed_sales_possibility": "MID",
      "npuaas_adoption_possibility": "LOW",
      "csp_capacity_expansion_possibility": "LOW",
      "contact_reason": "농협은행 프라이빗 엑사원 RAG 검색 속도 향상과 서버 자원 절감을 위한 고성능 국산 NPU 기술 검토 제안",
      "outreach_talk_track": "귀원의 선도적인 엑사원 기반 전용 생성형 AI 플랫폼 구축 및 실무 가동 성과를 무척 인상 깊게 전해 들었습니다. 엑사원 모델 추론 속도 지연을 최소화하고 장기적인 프라이빗 인프라 TCO를 대폭 아낄 수 있는 국산 RNGD 실증 검토 기회를 조심스럽게 건네드리고자 합니다.",
      "revenue_timing": "중기",
      "decision_maker_hint": "CIO, Head of AI Lab, Head of Digital Transformation",
      "existing_touchpoint": "확인 필요",
      "verification_needed": [
        "기존 시스템 구축 주체인 LG CNS와의 하드웨어 교차 적용 허용 범위 검토"
      ],
      "source_ids": ["S020"],
      "source_urls": [
        "https://www.news2day.co.kr/article/20260522500024"
      ]
    }
  ],
  "noise_examples": [
    {
      "source_id": "S004",
      "title": "[금쪽상식] '토스·네이버페이'는 은행일까···핀테크 쉽게 풀어보기",
      "reason": "핀테크와 인공지능 자산관리에 대한 단순 개념 설명을 기술한 일반 상식 수준의 기사로, 실질적인 인프라 구축이나 하드웨어 도입과는 무관하여 필터링함."
    },
    {
      "source_id": "S033",
      "title": "AI·금융 공들이고, 건설교통 공약 ‘쑥’… 재원조달은 ‘어물쩍’ [심...",
      "reason": "정치권의 일반적인 선거 공약 및 국가 예산 구조 분석 기사로, 구체적인 영업 기회 또는 접촉 명분을 식별할 수 없어 배제함."
    },
    {
      "source_id": "S034",
      "title": "머스크, AI 슈퍼컴퓨터 '콜로서스' 확장 승부수…xAI, 초대형 GPU 전쟁 본...",
      "reason": "해외 xAI의 가속 클러스터 도입 뉴스로, 한국 및 일본 GTM 시장 범위에 해당하지 않아 영업 후보에서 제외함."
    }
  ],
  "eval_notes": [
    "삼성SDS 및 NHN클라우드 등 주요 국산 CSP들의 동탄/구미 데이터센터 가속기 전력 및 요금 우려 신호는 RNGD의 저전력 소버린 소구력과 정확히 일치하여 고유한 마켓 타이밍을 보여줍니다.",
    "한컴 및 LG AI연구원의 엑사원 4.0 연동 행정망 공략과 전남소방본부의 Solar RAG 프로젝트 등 precompiled 모델 정합성을 완비한 B2G 단기 레퍼런스를 개척해 신속한 매출 창출로 연결하는 전방위BD 활동이 강력히 요구됩니다."
  ]
}
```