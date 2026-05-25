# LLM Evaluation Notes

## LLM metadata

- provider: `gemini`
- model: `gemini-3.5-flash`
- llm_sources_count: `40`
- max_llm_sources: `40`
- max_source_chars: `800`
- max_output_candidates: `12`
- evaluated_at_kst: `2026-05-26T00:54:16.235678+09:00`

## Run summary

- overall_assessment: 최근 7일 국내 GTM 환경은 민간 및 공공 대형 데이터센터의 전력 공급난 심화와 국내 CSP들의 합작 대응 기조가 돋보입니다. 특히 삼성SDS의 지속적인 자체 데이터센터 확장과 대형 금융사 AI 에이전트 사업 수주, 엘리스그룹의 코스닥 상장 청구에 따른 독자 인프라 고도화 움직임은 고성능 저전력 국산 NPU에 매우 강력한 기회 요인입니다. 또한 금융권 망분리 규제 합리화 흐름과 의료 공공기관의 자체 AI 통합 플랫폼 구축 드라이브가 가속화되고 있어, 비용 효율적이고 보안성이 높은 프라이빗 온프레미스 인프라 수요 역시 강력하게 포착되고 있습니다.
- top_priority_names: 삼성SDS, 엘리스그룹, KT클라우드
- noise_ratio_comment: 수집된 데이터 중 중국 시장 중심의 알리바바 및 텐센트 등의 인프라 동향이나 실질적 한국 및 일본 GTM 접점이 없는 머스크의 xAI 대규모 컴퓨터 확장 뉴스는 전략적 노이즈로 분류하고 제외하였습니다.
- model_compatibility_caution: NH농협은행 및 한글과컴퓨터 사례의 경우 엑사원 계열 모델 도입 정황이 명확히 포착되었으나, 구체적인 모델 아키텍처 버전과 커스텀 파인튜닝 수준이 당사 지원 목록과 일치하는지에 대한 검증이 필요합니다. 엑사원 계열의 경우 버전 간 연산 특성 차이가 존재하므로 제품 제안 전 세부 호환 성능 체크를 선행 조치해야 합니다.

## Eval notes

- 삼성SDS와 같이 대규모 인프라 투자 및 공공/금융권 대형 프로젝트를 연이어 수주하는 클라우드 운영 기업은 당사의 우선협상대상이자 전략적 영업 파트너 채널로서 outreach_priority를 HIGH로 최상향 고수하였습니다.
- 모델명이 확실하게 밝혀지지 않은 경우 model_fit_score는 엄격하게 UNKNOWN으로 처리하였으며, 그에 따른 판단 이유를 fit_vs_priority_explanation 영역에 구체적으로 명시하였습니다.
- 한글과컴퓨터 및 NH농협은행 등 K-EXAONE 패밀리 혹은 엑사원 탑재 제품을 활용하고 있는 사례에 대해서는 exact_supported가 아닌 family_only를 적용하여 보수적인 정합성 검토를 가이드하였습니다.
- 모든 서술 항목에서 인위적인 가상적 수치나 불필요하게 단정적인 성능 주장을 배제하고, 소스 본문에 명기된 수치만 완벽히 매핑하여 일관성을 엄격히 관리하였습니다.

## Raw LLM response

```json
{
  "run_summary": {
    "overall_assessment": "최근 7일 국내 GTM 환경은 민간 및 공공 대형 데이터센터의 전력 공급난 심화와 국내 CSP들의 합작 대응 기조가 돋보입니다. 특히 삼성SDS의 지속적인 자체 데이터센터 확장과 대형 금융사 AI 에이전트 사업 수주, 엘리스그룹의 코스닥 상장 청구에 따른 독자 인프라 고도화 움직임은 고성능 저전력 국산 NPU에 매우 강력한 기회 요인입니다. 또한 금융권 망분리 규제 합리화 흐름과 의료 공공기관의 자체 AI 통합 플랫폼 구축 드라이브가 가속화되고 있어, 비용 효율적이고 보안성이 높은 프라이빗 온프레미스 인프라 수요 역시 강력하게 포착되고 있습니다.",
    "top_priority_names": [
      "삼성SDS",
      "엘리스그룹",
      "KT클라우드"
    ],
    "noise_ratio_comment": "수집된 데이터 중 중국 시장 중심의 알리바바 및 텐센트 등의 인프라 동향이나 실질적 한국 및 일본 GTM 접점이 없는 머스크의 xAI 대규모 컴퓨터 확장 뉴스는 전략적 노이즈로 분류하고 제외하였습니다.",
    "model_compatibility_caution": "NH농협은행 및 한글과컴퓨터 사례의 경우 엑사원 계열 모델 도입 정황이 명확히 포착되었으나, 구체적인 모델 아키텍처 버전과 커스텀 파인튜닝 수준이 당사 지원 목록과 일치하는지에 대한 검증이 필요합니다. 엑사원 계열의 경우 버전 간 연산 특성 차이가 존재하므로 제품 제안 전 세부 호환 성능 체크를 선행 조치해야 합니다."
  },
  "candidates": [
    {
      "name": "삼성SDS",
      "country": "KR",
      "market": "B2B",
      "target_type": "CSP 운영 기업",
      "classification": "priority_outreach",
      "confirmed_project_or_signal": "동탄 및 구미 데이터센터 인프라 확장 및 우리은행 AI 에이전트 구축 사업 수주",
      "confirmed_model_name": "미확인",
      "model_match_status": "unknown",
      "model_fit_score": "UNKNOWN",
      "deployment_fit_score": "HIGH",
      "channel_fit_score": "HIGH",
      "rngd_fit_score": "MID",
      "outreach_priority": "HIGH",
      "fit_vs_priority_explanation": "모델 적합성은 미확인 상태이나, 동탄 데이터센터 20MW 전력 확보 및 구미에 4273억원 규모의 60MW 데이터센터를 투자하는 초대형 인프라 사업자입니다. 또한 우리은행 등 대형 금융권 사업을 수주하여 NPUaaS 및 SCP 클라우드 기반의 대규모 추론 인프라 증설 수요가 매우 높으므로 최우선 전략 채널로 분류합니다.",
      "hook_type": "CLOUD",
      "buying_signal": "동탄 및 구미 지역의 신규 AI 데이터센터 설립과 전력 확보를 지속하고 있으며, 우리은행의 생성형 AI 에이전트 사업 우선협상대상자로 선정되어 금융권 AX 시장을 주도하고 있습니다.",
      "infrastructure_signal": "동탄 데이터센터 서관 가동을 위한 20MW급 전력 확보 및 경북 구미에 4273억원을 투자하여 60MW 규모의 AI 데이터센터를 구축할 계획입니다.",
      "timing_reason": "최근 우리은행 사업 수주 및 대규모 데이터센터 전력 확보 소식이 전해진 시점으로, 인프라 효율화와 추론 비용 절감을 위한 하드웨어 파트너십 논의의 적기입니다.",
      "customer_win": "삼성SDS는 초대형 AI 데이터센터 운영에 따른 전력과 냉각 부담을 완화할 수 있습니다. 특히 SCP 클라우드 기반 NPUaaS 인프라에 RNGD를 도입함으로써 전력 효율을 높이고 고객사 대상 AI 추론 단가를 경쟁력 있게 제공할 수 있습니다.",
      "furiosa_win": "FuriosaAI는 삼성SDS의 SCP 클라우드 및 NPUaaS 인프라에 RNGD를 대규모로 공급할 수 있는 기회를 확보합니다. 이를 통해 공공 및 금융권 CSP 고객사 수요를 간접적으로 선점하는 강력한 유통 채널을 구축하게 됩니다.",
      "numeric_claims": [
        {
          "claim": "경기 동탄 데이터센터 서관 가동을 위해 20MW급 전력 확보",
          "source_id": "S003",
          "source_url": "https://www.e-science.co.kr/news/articleView.html?idxno=130004",
          "evidence_text": "삼성SDS가 경기 동탄 데이터센터 서관 가동을 위해 20MW급 전력을 확보한 사례"
        },
        {
          "claim": "경북 구미 AI 데이터센터에 4273억원 투자 및 60MW 규모 구축 계획",
          "source_id": "S010",
          "source_url": "https://www.mt.co.kr/tech/2026/05/23/2026052210211399740",
          "evidence_text": "삼성SDS는 경북 구미에 4273억원을 투자해 60MW 규모 AI 데이터센터를 짓기로 했다."
        }
      ],
      "direct_sales_possibility": "MID",
      "csp_routed_sales_possibility": "HIGH",
      "npuaas_adoption_possibility": "HIGH",
      "csp_capacity_expansion_possibility": "HIGH",
      "contact_reason": "삼성SDS의 동탄 및 구미 데이터센터 대규모 증설 계획과 금융권 초거대 AI 사업 수주에 맞춰, 저전력 고효율 AI 가속기 도입을 통한 인프라 비용 절감 방안을 제안합니다.",
      "outreach_talk_track": "최근 동탄 및 구미 지역의 대규모 AI 데이터센터 구축 소식과 우리은행 사업 수주 성과를 보고 연락드렸습니다. 현재 가속화되는 인프라 확장 단계에서 고효율 가속기 도입을 통한 전력 비용 및 추론 단가 최적화 방안을 함께 논의하고자 합니다.",
      "revenue_timing": "단기",
      "decision_maker_hint": "삼성SDS 클라우드서비스사업부장, AI서비스센터장, 인프라 기획 부서장 또는 구매 담당 책임자",
      "existing_touchpoint": "확인 필요",
      "verification_needed": [
        "SCP 인프라 내 RNGD 평가 및 호환성 테스트 여부",
        "구미 데이터센터 착공 일정 및 인프라 발주 시기"
      ],
      "source_ids": ["S001", "S003", "S010", "S012", "S026", "S028", "S031", "S038", "S039"],
      "source_urls": [
        "https://www.mt.co.kr/tech/2026/05/20/2026051922000848265",
        "https://www.e-science.co.kr/news/articleView.html?idxno=130004",
        "https://www.mt.co.kr/tech/2026/05/23/2026052210211399740",
        "https://www.thepowernews.co.kr/view.php?ud=202605221116568858de3f0aa1be_7",
        "https://www.sedaily.com/article/20046605?ref=naver",
        "https://www.sedaily.com/article/20046505?ref=naver",
        "https://www.ddaily.co.kr/page/view/2026052216371975959",
        "https://www.pinpointnews.co.kr/news/articleView.html?idxno=454902",
        "https://www.sedaily.com/article/20047365?ref=naver"
      ]
    },
    {
      "name": "엘리스그룹",
      "country": "KR",
      "market": "B2B",
      "target_type": "CSP 운영 기업",
      "classification": "cloud_npuaaS_lead",
      "confirmed_project_or_signal": "코스닥 상장 추진 및 GPUaaS, AI 클라우드 인프라 사업 확장",
      "confirmed_model_name": "미확인",
      "model_match_status": "unknown",
      "model_fit_score": "UNKNOWN",
      "deployment_fit_score": "HIGH",
      "channel_fit_score": "HIGH",
      "rngd_fit_score": "MID",
      "outreach_priority": "HIGH",
      "fit_vs_priority_explanation": "모델 적합성은 미확인이지만 상장 추진에 맞춰 GPUaaS 및 이동식 모듈형 데이터센터 등 자체 AI 인프라 사업을 빠르게 확장하고 있습니다. 국산 NPUaaS 라인업 다양화와 비용 효율화를 위해 적극적인 파트너십 구축이 가능하므로 outreach priority를 HIGH로 설정합니다.",
      "hook_type": "PARTNER",
      "buying_signal": "코스닥 상장예비심사를 청구하며 자체 인프라인 ECI 및 GPUaaS 사업 선점 고도화를 공표하였습니다.",
      "infrastructure_signal": "대규모 인프라 자원을 효율적으로 배치하는 기술과 이동식 모듈형 데이터센터를 보유하고 있어 독립적인 추론 팜 구축 역량이 높습니다.",
      "timing_reason": "상장 청구 직후 성장을 가속화하는 시점으로, 대규모 인프라 도입 및 하드웨어 다각화를 위한 전략적 제휴를 논의하기에 최적입니다.",
      "customer_win": "엘리스그룹은 고비용인 GPU 의존도를 낮추고 고효율 NPU 인프라를 추가 확보하여 마진율을 개선할 수 있습니다. 상장에 앞서 원가 경쟁력을 입증하고 독자적인 풀스택 AI 솔루션을 완성하는 데 기여합니다.",
      "furiosa_win": "FuriosaAI는 국산 AI 클라우드 강자인 엘리스그룹의 인프라 파트너로 참여하여 대규모 실제 납품 레퍼런스를 확보하고 지속적인 가속기 판매 경로를 마련할 수 있습니다.",
      "numeric_claims": [],
      "direct_sales_possibility": "HIGH",
      "csp_routed_sales_possibility": "MID",
      "npuaas_adoption_possibility": "HIGH",
      "csp_capacity_expansion_possibility": "MID",
      "contact_reason": "엘리스그룹의 코스닥 상장 예비심사 청구와 GPUaaS 사업 고도화 기조에 발맞춰 국산 가속기 도입을 통한 원가 절감 방안을 제시합니다.",
      "outreach_talk_track": "최근 코스닥 상장예비심사 청구 및 자체 인프라 고도화 소식을 기쁘게 접하였습니다. 귀사가 보유한 독보적인 풀스택 인프라 역량에 당사의 고효율 가속기를 결합하여, 서비스 원가를 혁신적으로 절감하고 시장을 선점할 방안을 제안드리고자 합니다.",
      "revenue_timing": "단기",
      "decision_maker_hint": "대표이사, 인프라 사업 본부장, 플랫폼 개발 실장",
      "existing_touchpoint": "엘리스 ✅",
      "verification_needed": [
        "기존 진행 중인 NDA 또는 PoC 내역 업데이트",
        "상장 전 신규 하드웨어 도입 예산 확보 여부"
      ],
      "source_ids": ["S013", "S014", "S015", "S016", "S017", "S018"],
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
      "confirmed_project_or_signal": "우선협상대상자 삼성SDS와 생성형 AI 에이전트 구축 사업 추진",
      "confirmed_model_name": "미확인",
      "model_match_status": "unknown",
      "model_fit_score": "UNKNOWN",
      "deployment_fit_score": "MID",
      "channel_fit_score": "HIGH",
      "rngd_fit_score": "MID",
      "outreach_priority": "HIGH",
      "fit_vs_priority_explanation": "모델 적합성은 미확인 상태이나, 삼성SDS를 우선협상대상자로 선정하여 대규모 생성형 AI 시스템을 구축하는 초대형 금융권 엔터프라이즈 수요처입니다. 삼성SDS의 클라우드 인프라를 활용하므로, CSP 경유 및 NPUaaS 유도를 위한 핵심 수요 창출 고객으로 적합하여 우선순위를 HIGH로 설정합니다.",
      "hook_type": "CLOUD",
      "buying_signal": "생성형 AI 에이전트 구축 사업의 우선협상대상자로 삼성SDS를 선정하여 본격적인 금융 업무 지능화를 추진하고 있습니다.",
      "infrastructure_signal": "금융권의 엄격한 보안 규제와 데이터 관리를 고려하여 망분리 우회 또는 합리화 흐름에 맞춘 인프라를 설계할 가능성이 높습니다.",
      "timing_reason": "사업 우선협상대상자 선정 후 시스템 설계가 구체화되는 시점으로, 인프라 비용을 대폭 줄일 수 있는 국산 가속기 옵션을 제안할 수 있는 적기입니다.",
      "customer_win": "우리은행은 대규모 고객 상담 및 자산 분석 시 발생하는 클라우드 추론 비용을 혁신적으로 절감할 수 있습니다. 국산 가속기를 통해 안정적이고 비용 효율적인 상시 서비스 운영 체계를 확립하게 됩니다.",
      "furiosa_win": "FuriosaAI는 대형 시중은행의 상용 생성형 AI 서비스에 가속기를 공급하는 상징적인 금융 레퍼런스를 확보하며, 삼성SDS 인프라의 가속기 증설을 유도할 수 있습니다.",
      "numeric_claims": [],
      "direct_sales_possibility": "LOW",
      "csp_routed_sales_possibility": "HIGH",
      "npuaas_adoption_possibility": "HIGH",
      "csp_capacity_expansion_possibility": "HIGH",
      "contact_reason": "삼성SDS와 함께 추진하는 AI 에이전트 사업의 추론 인프라 비용 효율화를 위해 가속기 도입 검토를 제안합니다.",
      "outreach_talk_track": "최근 귀행의 생성형 AI 에이전트 구축 사업 우선협상대상자 선정 소식을 접하였습니다. 구축을 담당할 파트너사와 연계하여 클라우드 및 온프레미스 환경에서 인프라 비용을 최적화할 수 있는 고성능 국산 가속기 도입 방안을 논의하고자 합니다.",
      "revenue_timing": "단기",
      "decision_maker_hint": "디지털그룹장, 정보보호최고책임자, AI 에이전트 구축 프로젝트 PM, 정보기획부장",
      "existing_touchpoint": "확인 필요",
      "verification_needed": [
        "삼성SDS 제안서 내 인프라 하드웨어 구성 사양",
        "금융권 자체 인프라 내 가속기 직접 도입 허용 여부"
      ],
      "source_ids": ["S026", "S028"],
      "source_urls": [
        "https://www.sedaily.com/article/20046605?ref=naver",
        "https://www.sedaily.com/article/20046505?ref=naver"
      ]
    },
    {
      "name": "KT클라우드",
      "country": "KR",
      "market": "B2B",
      "target_type": "CSP 운영 기업",
      "classification": "priority_outreach",
      "confirmed_project_or_signal": "AI DC 가동 및 GPUaaS 매출 증가, 해남 솔라시도 국가AI컴퓨팅센터 컨소시엄 참여",
      "confirmed_model_name": "미확인",
      "model_match_status": "unknown",
      "model_fit_score": "UNKNOWN",
      "deployment_fit_score": "HIGH",
      "channel_fit_score": "HIGH",
      "rngd_fit_score": "MID",
      "outreach_priority": "HIGH",
      "fit_vs_priority_explanation": "모델 적합성은 미확인이나, 1분기 매출이 2501억원에 달하고 AI DC 사업 확대와 대규모 국가 컴퓨팅 인프라 컨소시엄에 참여 중인 초대형 CSP 사업자입니다. 저전력 국산 가속기를 자사 AI 클라우드에 탑재하여 전력 수급난을 완화할 명분이 확실하므로 우선순위를 HIGH로 지정합니다.",
      "hook_type": "POWER",
      "buying_signal": "서울 가산 및 판교 데이터센터 가동률 상승과 GPUaaS 부문 매출 성장을 바탕으로 AI 인프라 사업을 가속화하고 있습니다.",
      "infrastructure_signal": "전남 해남 솔라시도 지역에 삼성SDS 등과 함께 국가AI컴퓨팅센터 구축 컨소시엄에 참여하여 대형 인프라 확충을 지속하고 있습니다.",
      "timing_reason": "데이터센터 전력 공급 부족과 비용 상승에 대응해야 하는 시기로, 저전력 특성이 극대화된 국산 대체 하드웨어 도입 논의가 활발한 시점입니다.",
      "customer_win": "KT클라우드는 수도권 데이터센터의 심각한 전력난 속에서 저전력 가속기를 도입하여 랙 밀도를 높이고 상면당 전력 소모를 제어할 수 있습니다. 대규모 추론 서비스용 단가를 낮춰 시장 경쟁력을 확보합니다.",
      "furiosa_win": "FuriosaAI는 국내 주요 CSP인 KT클라우드에 RNGD를 탑재함으로써 자사 가속기 기반의 상용 인프라 생태계를 단번에 확장하고 대규모 하드웨어 납품 성과를 창출할 수 있습니다.",
      "numeric_claims": [
        {
          "claim": "KT클라우드 1분기 매출 2501억원 달성",
          "source_id": "S008",
          "source_url": "https://www.m-i.kr/news/articleView.html?idxno=1375542",
          "evidence_text": "KT클라우드의 1분기 매출은 2501억원으로"
        }
      ],
      "direct_sales_possibility": "HIGH",
      "csp_routed_sales_possibility": "LOW",
      "npuaas_adoption_possibility": "HIGH",
      "csp_capacity_expansion_possibility": "HIGH",
      "contact_reason": "급증하는 AI DC 인프라 수요와 전력 공급 한계를 극복하기 위해, KT클라우드 인프라 내에 저전력 고효율 가속기 도입을 제안합니다.",
      "outreach_talk_track": "최근 귀사의 분기 매출 성장 성과와 해남 솔라시도 국가AI컴퓨팅센터 참여 등 대규모 클라우드 증설 소식을 인상 깊게 보았습니다. 급격한 인프라 확장 속에서 전력 제약과 랙 공간 한계를 해결할 수 있는 당사의 초저전력 가속기 결합 방안을 기획하고자 연락드렸습니다.",
      "revenue_timing": "단기",
      "decision_maker_hint": "대표이사, AI DC 사업 본부장, 인프라 기획 부서장",
      "existing_touchpoint": "확인 필요",
      "verification_needed": [
        "현재 KT클라우드 내 타 국산 NPU 가속기 도입 비율",
        "국가AI컴퓨팅센터 내 가속기 규격 요건"
      ],
      "source_ids": ["S001", "S005", "S008", "S010"],
      "source_urls": [
        "https://www.mt.co.kr/tech/2026/05/20/2026051922000848265",
        "https://www.ddaily.co.kr/page/view/2026052017342600376",
        "https://www.m-i.kr/news/articleView.html?idxno=1375542",
        "https://www.mt.co.kr/tech/2026/05/23/2026052210211399740"
      ]
    },
    {
      "name": "NH농협은행",
      "country": "KR",
      "market": "B2B",
      "target_type": "온프레미스 기업",
      "classification": "structure_check",
      "confirmed_project_or_signal": "LG CNS 전용 생성형 AI 구축 사업 및 검색증강생성(RAG) 플랫폼 고도화",
      "confirmed_model_name": "EXAONE-3.5",
      "model_match_status": "family_only",
      "model_fit_score": "MID",
      "deployment_fit_score": "HIGH",
      "channel_fit_score": "MID",
      "rngd_fit_score": "MID",
      "outreach_priority": "MID",
      "fit_vs_priority_explanation": "엑사원 모델 계열을 활용하고 있어 모델 아키텍처 정합성은 양호하지만, 엑사원 전용 파인튜닝 버전의 호환성 검증이 추가로 필요합니다. LG CNS가 주도하는 농협은행 전용 생성형 AI의 인프라 전환 명분과 세부 사양 구조를 검증해야 하므로 structure_check 단계로 설정합니다.",
      "hook_type": "SOVEREIGN",
      "buying_signal": "농협은행 전용 생성형 AI 플랫폼 구축을 통해 내부 업무 규정, 상품 정보 검색 및 리테일 영업 지원 등의 용도로 RAG를 본격 확대하고 있습니다.",
      "infrastructure_signal": "금융권 자체의 내부 전용 프라이빗 AI 플랫폼 구축 흐름을 따르고 있어 온프레미스 또는 프라이빗 클라우드 폐쇄망 환경이 예상됩니다.",
      "timing_reason": "시스템 구축 사업이 본격화되어 실무 비즈니스 영역에 적용되는 시점으로, 운영 효율성과 비용 절감을 논의하기 적절한 접촉 명분이 제공됩니다.",
      "customer_win": "농협은행은 내부 중요 정보의 외부 유출 걱정 없이 프라이빗 환경에서 대규모 실시간 질의를 지연 시간 없이 안정적으로 처리할 수 있습니다. 고가의 연산 자원 비용 부담을 크게 낮출 수 있습니다.",
      "furiosa_win": "FuriosaAI는 금융권 핵심 프라이빗 AI 도입 계정을 확보하고, 국산 대표 오픈형 모델인 엑사원 엔진 위에서 고효율 서빙 인프라의 강점을 성공적으로 증명할 수 있습니다.",
      "numeric_claims": [],
      "direct_sales_possibility": "LOW",
      "csp_routed_sales_possibility": "MID",
      "npuaas_adoption_possibility": "MID",
      "csp_capacity_expansion_possibility": "LOW",
      "contact_reason": "LG CNS와 구축하는 전용 엑사원 AI RAG 인프라의 비용 최적화를 위해 저전력 가속기 결합 방안 검토를 제안합니다.",
      "outreach_talk_track": "최근 LG CNS와 함께 귀행 전용 초거대 AI 플랫폼 및 RAG 기반 업무 서비스를 추진하신다는 소식을 인상 깊게 보았습니다. 안정적인 프라이빗 시스템 운영을 위해 전력 소모가 적으면서도 대규모 실시간 질의 처리에 탁월한 국산 고성능 가속기 활용 방안을 제안드리고자 합니다.",
      "revenue_timing": "중기",
      "decision_maker_hint": "IT부문 부행장, 디지털전략부서장, 플랫폼 인프라 실무 파트장",
      "existing_touchpoint": "확인 필요",
      "verification_needed": [
        "구축 파트너사인 LG CNS의 하드웨어 변경 권한 여부",
        "엑사원 튜닝 모델의 구체적인 크기 및 호환 성능"
      ],
      "source_ids": ["S020"],
      "source_urls": ["https://www.news2day.co.kr/article/20260522500024"]
    },
    {
      "name": "한글과컴퓨터",
      "country": "KR",
      "market": "B2G",
      "target_type": "CSP 고객 기업",
      "classification": "structure_check",
      "confirmed_project_or_signal": "LG AI연구원과 AI 문서 에이전트 및 챗엑사원 공공 시장 공동 공략",
      "confirmed_model_name": "EXAONE",
      "model_match_status": "family_only",
      "model_fit_score": "MID",
      "deployment_fit_score": "HIGH",
      "channel_fit_score": "MID",
      "rngd_fit_score": "MID",
      "outreach_priority": "MID",
      "fit_vs_priority_explanation": "모델은 공공 시장을 타깃으로 하는 엑사원 계열로 당사 지원 라인업과 호환 가능성이 높지만, 구체적인 모델 크기 및 공공 클라우드 배포 스택과의 하드웨어 호환성 검증이 필요합니다. 공공 AX 동맹의 일원으로서 솔루션 공급 구조를 파악해야 하므로 structure_check로 분류합니다.",
      "hook_type": "PROCUREMENT",
      "buying_signal": "LG AI연구원과 손잡고 한컴의 AI 에이전트 기술과 엑사원 모델을 결합하여 공공기관 및 지자체 대상 영업과 솔루션 수주를 본격적으로 가속화하고 있습니다.",
      "infrastructure_signal": "정부부처 및 지자체 대상이므로 프라이빗 온프레미스 구축 및 행정안전부 등 공공 전용 클라우드 배포 규격을 따를 예정입니다.",
      "timing_reason": "양사가 공공 AI 동맹을 결성하고 시장 수주에 본격 나서는 단계이므로, 조달 단가 경쟁력을 극대화할 국산 가속기 제안이 시의적절합니다.",
      "customer_win": "한글과컴퓨터는 공공 부문 솔루션 공급 시 하드웨어 인프라 비용 부담을 줄여 제안 단가 경쟁력을 높일 수 있습니다. 특히 공공 보안 규제와 프라이빗 온프레미스 설치 요구에 고효율 저전력 인프라로 유연하게 맞출 수 있습니다.",
      "furiosa_win": "FuriosaAI는 국산 사무형 AI 및 문서 저작 도구의 사실상 표준인 한컴 솔루션과 당사 가속기 엔진을 결합하여, 공공 B2G 시장 전체로 RNGD 수요를 동시 확산시킬 수 있습니다.",
      "numeric_claims": [],
      "direct_sales_possibility": "MID",
      "csp_routed_sales_possibility": "MID",
      "npuaas_adoption_possibility": "MID",
      "csp_capacity_expansion_possibility": "MID",
      "contact_reason": "공공 AX 시장을 겨냥해 공동 개발하는 엑사원 기반 한컴 AI 에이전트 인프라의 원가 경쟁력 강화를 위한 하드웨어 협력을 제안합니다.",
      "outreach_talk_track": "최근 LG AI연구원과 손잡고 공공 AX 시장 수주를 위한 공동 동맹을 결성하신 소식을 뜻깊게 보았습니다. 귀사의 초거대 AI 문서 에이전트 솔루션이 공공 인프라에 안착할 때, 제안 경쟁력을 높이고 상면 비용을 획기적으로 낮춰줄 고효율 국산 가속기 협력 모델을 제안드립니다.",
      "revenue_timing": "중기",
      "decision_maker_hint": "AI사업본부장, 공공사업부문장, 연동 솔루션 아키텍트 총괄",
      "existing_touchpoint": "확인 필요",
      "verification_needed": [
        "한컴 에이전트가 배포될 주요 공공 클라우드 가상 환경 규격",
        "엑사원 탑재 형태가 온프레미스형인지 MaaS형인지 여부"
      ],
      "source_ids": ["S021", "S022", "S023", "S024", "S025"],
      "source_urls": [
        "http://www.newslock.co.kr/news/articleView.html?idxno=130504",
        "https://www.mt.co.kr/tech/2026/05/22/2026052215283358675",
        "https://www.mk.co.kr/article/12055579",
        "https://www.getnews.co.kr/news/articleView.html?idxno=870707",
        "https://www.newsis.com/view/NISX20260522_0003640664"
      ]
    },
    {
      "name": "건강보험심사평가원",
      "country": "KR",
      "market": "B2G",
      "target_type": "온프레미스 기업",
      "classification": "structure_check",
      "confirmed_project_or_signal": "AI 통합플랫폼 구축 및 GPU 서버 기반 인프라 도입 계획 수립",
      "confirmed_model_name": "미확인",
      "model_match_status": "unknown",
      "model_fit_score": "UNKNOWN",
      "deployment_fit_score": "HIGH",
      "channel_fit_score": "MID",
      "rngd_fit_score": "MID",
      "outreach_priority": "MID",
      "fit_vs_priority_explanation": "모델 적합성은 미확인 상태이나, GPU 서버 기반의 자체 AI 통합 플랫폼과 전용 데이터 인프라를 직접 기획 및 구축하는 강력한 공공 수요처입니다. 실제 장비 규격과 국산 가속기 가상화 솔루션의 적용 가능성을 확인해야 하므로 structure_check로 분류합니다.",
      "hook_type": "PROCUREMENT",
      "buying_signal": "디지털전략실 및 디지털클라우드센터를 중심으로 자체 인프라를 활용하여 AI 개발과 운영을 일원화하는 AI 통합플랫폼 구축에 총력을 기울이고 있습니다.",
      "infrastructure_signal": "심평원 자체 GPU 서버 기반의 온프레미스 인프라를 설계하며, 원스톱 서비스 제공을 위한 플랫폼 인프라를 구축할 계획입니다.",
      "timing_reason": "기관의 디지털클라우드센터 전략 수립과 하드웨어 인프라 발주 기획 단계에 있어, 공공 조달을 목표로 사전 규격을 검토하기에 이상적인 접촉 시기입니다.",
      "customer_win": "건강보험심사평가원은 방대한 공공 의료 데이터를 안전하게 다루는 내부 인프라에서 전력과 상면 효율을 고려한 안정적인 GPU 대체 인프라를 구성할 수 있습니다. 조달 예산 범위 내에서 대용량 연산 풀을 유연하게 확보합니다.",
      "furiosa_win": "FuriosaAI는 국가 중추 의료 공공기관의 온프레미스 AI 인프라 표준 규격에 진입하는 중요한 레퍼런스를 구축하고, 다른 공공 산하 기관으로의 확장 교두보를 마련할 수 있습니다.",
      "numeric_claims": [],
      "direct_sales_possibility": "MID",
      "csp_routed_sales_possibility": "MID",
      "npuaas_adoption_possibility": "LOW",
      "csp_capacity_expansion_possibility": "LOW",
      "contact_reason": "심평원이 계획 중인 GPU 기반 AI 통합플랫폼의 조달 효율성과 가상화 운영 효율 증대를 위한 국산 가속기 제안을 검토합니다.",
      "outreach_talk_track": "최근 귀원의 AI 통합플랫폼 구축 및 GPU 인프라 도입 드라이브 계획을 확인하였습니다. 의료 공공 데이터의 프라이빗 보안 환경에 최적화되고, 조달 단가와 전력 소비율을 대폭 향상시켜 줄 국산 고성능 가속기 기반의 효율적인 플랫폼 구축 방안을 공유해 드리고자 합니다.",
      "revenue_timing": "장기",
      "decision_maker_hint": "디지털전략실장 겸 디지털클라우드센터장, AI융합추진단장, 인프라 기획 담당 사무관",
      "existing_touchpoint": "확인 필요",
      "verification_needed": [
        "플랫폼 내 탑재 예정인 오픈소스 기반 LLM 및 추론 서비스 아키텍처",
        "공공 인프라 조달 예산 수립 규모와 정식 입찰 공고 예정 일정"
      ],
      "source_ids": ["S035"],
      "source_urls": ["https://www.etnews.com/20260522000181"]
    }
  ],
  "noise_examples": [
    {
      "source_id": "S006",
      "title": "[AI의 종목 이야기] 알리바바, 신형 AI 가속기 '전우 M890' 공개",
      "reason": "해당 기사는 중국 기업 알리바바의 독자적인 신형 하드웨어 출시 및 중국 내 Qwen 모델 업데이트를 다룬 뉴스로서, 한국 및 일본 시장을 타깃으로 하는 FuriosaAI의 실질적인 GTM 성과 창출과는 무관한 노이즈 데이터입니다."
    },
    {
      "source_id": "S034",
      "title": "머스크, AI 슈퍼컴퓨터 '콜로서스' 확장 승부수…xAI, 초대형 GPU 전쟁 본...",
      "reason": "해외 빅테크 기업인 xAI의 글로벌 슈퍼컴퓨터 인프라 확장 및 GPU 수급 상황을 설명하는 글로벌 시장 가십성 뉴스로서, 본사 BD팀이 단기적으로 접촉하거나 영업 구조를 확인할 대상에서 완전히 벗어나 있어 제외합니다."
    }
  ],
  "eval_notes": [
    "삼성SDS와 같이 대규모 인프라 투자 및 공공/금융권 대형 프로젝트를 연이어 수주하는 클라우드 운영 기업은 당사의 우선협상대상이자 전략적 영업 파트너 채널로서 outreach_priority를 HIGH로 최상향 고수하였습니다.",
    "모델명이 확실하게 밝혀지지 않은 경우 model_fit_score는 엄격하게 UNKNOWN으로 처리하였으며, 그에 따른 판단 이유를 fit_vs_priority_explanation 영역에 구체적으로 명시하였습니다.",
    "한글과컴퓨터 및 NH농협은행 등 K-EXAONE 패밀리 혹은 엑사원 탑재 제품을 활용하고 있는 사례에 대해서는 exact_supported가 아닌 family_only를 적용하여 보수적인 정합성 검토를 가이드하였습니다.",
    "모든 서술 항목에서 인위적인 가상적 수치나 불필요하게 단정적인 성능 주장을 배제하고, 소스 본문에 명기된 수치만 완벽히 매핑하여 일관성을 엄격히 관리하였습니다."
  ]
}
```