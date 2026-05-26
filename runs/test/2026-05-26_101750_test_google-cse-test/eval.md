# LLM Evaluation Notes

## LLM metadata

- provider: `gemini`
- model: `gemini-3.5-flash`
- llm_sources_count: `40`
- max_llm_sources: `40`
- max_source_chars: `800`
- max_output_candidates: `12`
- evaluated_at_kst: `2026-05-26T10:23:25.870174+09:00`

## Run summary

- overall_assessment: 금융권 망분리 규제 완화에 따른 프라이빗 AI 보안 시스템 구축 수요와 국내 주요 CSP 및 AI 클라우드 제공사들의 인프라 증설 움직임이 포착됩니다. 특히 삼성SDS의 대규모 데이터센터 투자 및 전력 확보, 엘리스그룹의 코스닥 상장 추진 및 GPUaaS 확장 등은 NPUaaS 연계 및 대형 채널 확보 관점에서 매우 강력한 GTM 기회를 제공합니다.
- top_priority_names: 삼성SDS, 엘리스그룹, KB금융그룹
- noise_ratio_comment: 수집된 40건의 소스 중 단순 제약계 동향, 이커머스 민원 관련 소식, 전기공사 실적 관련 기사 등 3건을 노이즈로 분류하였습니다. 전반적으로 망분리 완화와 데이터센터 인프라 전력 수급 이슈 등 유효한 GTM 신호의 비중이 높습니다.
- model_compatibility_caution: 본 보고서에 포함된 유효 후보군 중 현재 명확한 타깃 서비스 모델명이 기사 상으로 확인된 사례는 없습니다. 따라서 호환 모델 매칭 점수는 UNKNOWN으로 보수적으로 평가하였으며, 추후 vLLM 연동 및 Triton Server 환경을 통한 드롭인 대체 가능성을 기반으로 한 아키텍처 레벨의 검증 영업이 필요합니다.

## Eval notes

- 이번 주 소스에서는 대규모 금융권 망분리 규제 완화(보안 분야 선도입) 신호가 매우 강력하게 부각되었습니다.
- 이러한 보안 인프라 완화와 대형 병원들의 온프레미스 구축 실증 성공은 보안 주권을 무기로 하는 RNGD 솔루션에 매우 적합한 타이밍을 선사합니다.
- 다만 타깃 기업들이 구체적인 실무 지원 모델 명칭을 외부 기사에 밝히지 않고 있으므로, 세부 아키텍처 파악을 위한 실무 엔지니어 접촉이 전제되어야 합니다.
- 삼성SDS 및 엘리스그룹과 같은 하이브리드 파트너/CSP 운영 후보군들은 자체적으로 거대 투자를 가시화하고 있으므로 NPUaaS 조기 입점을 위한 최우선 컨택을 강력히 제안합니다.

## Raw LLM response

```json
{
  "run_summary": {
    "overall_assessment": "금융권 망분리 규제 완화에 따른 프라이빗 AI 보안 시스템 구축 수요와 국내 주요 CSP 및 AI 클라우드 제공사들의 인프라 증설 움직임이 포착됩니다. 특히 삼성SDS의 대규모 데이터센터 투자 및 전력 확보, 엘리스그룹의 코스닥 상장 추진 및 GPUaaS 확장 등은 NPUaaS 연계 및 대형 채널 확보 관점에서 매우 강력한 GTM 기회를 제공합니다.",
    "top_priority_names": [
      "삼성SDS",
      "엘리스그룹",
      "KB금융그룹"
    ],
    "noise_ratio_comment": "수집된 40건의 소스 중 단순 제약계 동향, 이커머스 민원 관련 소식, 전기공사 실적 관련 기사 등 3건을 노이즈로 분류하였습니다. 전반적으로 망분리 완화와 데이터센터 인프라 전력 수급 이슈 등 유효한 GTM 신호의 비중이 높습니다.",
    "model_compatibility_caution": "본 보고서에 포함된 유효 후보군 중 현재 명확한 타깃 서비스 모델명이 기사 상으로 확인된 사례는 없습니다. 따라서 호환 모델 매칭 점수는 UNKNOWN으로 보수적으로 평가하였으며, 추후 vLLM 연동 및 Triton Server 환경을 통한 드롭인 대체 가능성을 기반으로 한 아키텍처 레벨의 검증 영업이 필요합니다."
  },
  "candidates": [
    {
      "name": "삼성SDS",
      "country": "KR",
      "market": "B2B",
      "target_type": "CSP 운영 기업",
      "classification": "priority_outreach",
      "confirmed_project_or_signal": "경북 구미 AI 데이터센터 투자 및 경기 동탄 데이터센터 서관 가동 가속화",
      "confirmed_model_name": "미확인",
      "model_match_status": "unknown",
      "model_fit_score": "UNKNOWN",
      "deployment_fit_score": "HIGH",
      "channel_fit_score": "HIGH",
      "rngd_fit_score": "MID",
      "outreach_priority": "HIGH",
      "fit_vs_priority_explanation": "모델 정보는 미확인이지만 경북 구미에 대규모 AI 데이터센터를 짓고 전력을 확보하는 등 클라우드 인프라 확장 속도가 빠르며, SCP 및 NPUaaS 서비스 다각화 측면에서 채널 파트너로서의 우선순위가 매우 높습니다.",
      "hook_type": "CLOUD",
      "buying_signal": "경북 구미에 인프라를 구축하며 데이터센터 투자를 본격화하고 있으며 동탄 데이터센터 전력 확보와 함께 자체 AI 클라우드인 SCP의 추론 처리량 대응을 위한 국산 NPU 수용 가능성이 증대되고 있습니다.",
      "infrastructure_signal": "경기 동탄 데이터센터 서관 가동을 위한 전력 확보 및 경북 구미 데이터센터 신설을 통한 AI 연산 자원 및 전력 용량 대폭 확장 흐름이 확인됩니다.",
      "timing_reason": "국내 주요 CSP들과 함께 공동 전선을 구축하여 글로벌 CSP의 진입 및 GPU 공급난에 대응하는 시점으로, 비용 효율성이 높은 RNGD 기반 NPUaaS 라인업 확보가 요구되는 적기입니다.",
      "customer_win": "삼성SDS의 AI 클라우드(SCP) 고객사들에게 GPU 대비 우수한 비용 효율과 낮은 전력 소모를 보장하는 추론 인프라 옵션을 제공할 수 있습니다. 전력 포화 상태인 수도권 외 지역 데이터센터 운영 시 전력 사용량 저감에 기여합니다.",
      "furiosa_win": "삼성SDS SCP 플랫폼에 RNGD가 핵심 NPUaaS 라인업으로 정식 채택될 경우 엔터프라이즈 및 공공 수요를 아우르는 대규모 CSP 경유 매출과 지속적인 인프라 증설 기회를 확보할 수 있습니다.",
      "numeric_claims": [
        {
          "claim": "삼성SDS 경기 동탄 데이터센터 서관 가동을 위해 20MW급 전력 확보",
          "source_id": "S026",
          "source_url": "https://www.e-science.co.kr/news/articleView.html?idxno=130004",
          "evidence_text": "삼성SDS가 경기 동탄 데이터센터 서관 가동을 위해 20MW급 전력을 확보한 사례"
        },
        {
          "claim": "삼성SDS 경북 구미 AI 데이터센터에 4273억원 투자 및 60MW 규모 구축 계획",
          "source_id": "S032",
          "source_url": "https://www.mt.co.kr/tech/2026/05/23/2026052210211399740",
          "evidence_text": "삼성SDS는 경북 구미에 4273억원을 투자해 60MW 규모 AI 데이터센터를 짓기로 했다."
        }
      ],
      "direct_sales_possibility": "LOW",
      "csp_routed_sales_possibility": "HIGH",
      "npuaas_adoption_possibility": "HIGH",
      "csp_capacity_expansion_possibility": "HIGH",
      "contact_reason": "구미와 동탄의 대규모 AI 인프라 구축 및 국내 CSP의 고효율 자원 다각화 추진 시점에 맞추어 SCP 내 NPUaaS 라인업 구성을 제안하고자 합니다.",
      "outreach_talk_track": "최근 구미 데이터센터 투자와 동탄 데이터센터 전력 확보 소식을 접하고 연락드렸습니다. 전력 및 상면 제약이 커지는 시점에 초고효율 아키텍처인 RNGD를 활용하여 SCP 내에 차세대 고성능 NPUaaS를 신속히 도입하고 공급망 리스크를 해소하는 방안을 논의하고 싶습니다.",
      "revenue_timing": "단기",
      "decision_maker_hint": "클라우드서비스사업부장, SCP 플랫폼 개발본부장, 인프라아키텍처팀장, AI 인프라 기획 부서장",
      "existing_touchpoint": "확인 필요",
      "verification_needed": [
        "삼성SDS 자체 개발 플랫폼 혹은 SCP 고객사 중 Llama-3.1 계열 또는 Qwen2.5 계열의 오픈소스 모델을 활용하는 비중 파악 필요",
        "SCP NPUaaS 플랫폼의 하이퍼바이저 및 가상화 솔루션 호환 여부 검증"
      ],
      "source_ids": [
        "S026",
        "S028",
        "S031",
        "S032",
        "S033"
      ],
      "source_urls": [
        "https://www.e-science.co.kr/news/articleView.html?idxno=130004",
        "https://www.ddaily.co.kr/page/view/2026052017342600376",
        "https://www.ddaily.co.kr/page/view/2026052509101133595",
        "https://www.mt.co.kr/tech/2026/05/23/2026052210211399740",
        "https://www.thepowernews.co.kr/view.php?ud=202605221116568858de3f0aa1be_7"
      ]
    },
    {
      "name": "엘리스그룹",
      "country": "KR",
      "market": "B2B",
      "target_type": "CSP 운영 기업",
      "classification": "priority_outreach",
      "confirmed_project_or_signal": "코스닥 상장예비심사 청구 및 이동식 모듈형 데이터 센터(AI PMDC) 자원 확장",
      "confirmed_model_name": "미확인",
      "model_match_status": "unknown",
      "model_fit_score": "UNKNOWN",
      "deployment_fit_score": "HIGH",
      "channel_fit_score": "HIGH",
      "rngd_fit_score": "MID",
      "outreach_priority": "HIGH",
      "fit_vs_priority_explanation": "자체 AI 인프라 솔루션인 PMDC 및 인프라 서비스 ECI를 직접 제조/운영하고 있으며 상장 예심 청구를 기점으로 대규모 인프라 다각화를 꾀하는 만큼, 모델 정보 미확인 상태에서도 높은 인프라 채널 시너지를 기대할 수 있습니다.",
      "hook_type": "CLOUD",
      "buying_signal": "상장예비심사 청구를 시작으로 국내 및 글로벌 시장 선점을 고도화하고 있으며, 자체적인 이동식 모듈형 데이터센터(AI PMDC) 인프라 비용 절감과 전력 효율 확보가 필요한 시점입니다.",
      "infrastructure_signal": "이동식 모듈형 데이터 센터(AI PMDC) 및 컨테이너 가상화 인프라인 ECI 환경을 구축하고 있으며 대규모 GPUaaS 자원을 관리하고 있습니다.",
      "timing_reason": "코스닥 상장 절차 착수에 따른 자금 유입과 국내외 비즈니스 영토 확장 타이밍이 맞물려 있어, 차별화된 고성능 저비용 NPU 인프라 라인업을 파트너 포트폴리오로 조기 편입시키기에 적절한 시기입니다.",
      "customer_win": "엘리스그룹의 ECI 및 PMDC 인프라 솔루션 내부의 운영 전력량과 비용 부담을 대폭 경감시킬 수 있으며, 자사 GPUaaS 고객들에게 경쟁력 있는 요금제의 추론 전용 옵션을 신규 제공할 수 있습니다.",
      "furiosa_win": "국내 교육 및 엔터프라이즈 AI 클라우드 영역에서 급성장하는 파트너의 인프라 내에 하드웨어 레벨로 내장되어 고정 매출을 확보하고 글로벌 동반 진출 교두보를 마련할 수 있습니다.",
      "numeric_claims": [],
      "direct_sales_possibility": "MID",
      "csp_routed_sales_possibility": "HIGH",
      "npuaas_adoption_possibility": "HIGH",
      "csp_capacity_expansion_possibility": "MID",
      "contact_reason": "모듈형 데이터센터 및 ECI 인프라 고도화와 GPUaaS 요금 경쟁력 제고를 위한 하이브리드 NPU 연동 방안 제안 목적입니다.",
      "outreach_talk_track": "최근 IPO 예비심사 청구와 AI 클라우드 부문 확장 소식을 기쁘게 접하였습니다. 엘리스의 AI PMDC 및 ECI 플랫폼 아키텍처에 컨테이너 환경 호환성이 검증된 RNGD를 통합 적용하여 인프라 전력 사용량을 개선하고 비용을 최적화하는 방안을 제안드리고 싶습니다.",
      "revenue_timing": "단기",
      "decision_maker_hint": "CTO, 클라우드인프라본부장, 인프라개발팀장, 하드웨어 플랫폼 아키텍트",
      "existing_touchpoint": "확인 필요",
      "verification_needed": [
        "엘리스 PMDC에 사용되는 서버 하우징 규격 및 PCIe 슬롯 가용성 조사",
        "ECI 내 컨테이너 오케스트레이션 환경에서 Furiosa Kubernetes Toolkit 적용 여부 확인"
      ],
      "source_ids": [
        "S034",
        "S035",
        "S036",
        "S037"
      ],
      "source_urls": [
        "http://www.joseilbo.com/news/news_read.php?uid=568639&class=53&grp=",
        "https://www.fetv.co.kr/news/articleView.html?idxno=302765",
        "https://www.the-stock.kr/news/articleView.html?idxno=32570",
        "https://www.newspim.com/news/view/20260520000146"
      ]
    },
    {
      "name": "KB금융그룹",
      "country": "KR",
      "market": "B2B",
      "target_type": "온프레미스 기업",
      "classification": "structure_check",
      "confirmed_project_or_signal": "예방형 사이버보안 체계 구축 및 정보보호 실태 점검 내 AI 에이전트 도입 추진",
      "confirmed_model_name": "미확인",
      "model_match_status": "unknown",
      "model_fit_score": "UNKNOWN",
      "deployment_fit_score": "HIGH",
      "channel_fit_score": "MID",
      "rngd_fit_score": "MID",
      "outreach_priority": "MID",
      "fit_vs_priority_explanation": "사용 모델은 미확인이지만 망분리 완화 가이드라인에 부합하는 사내 보안용 온프레미스/프라이빗 AI 시스템 구축 니즈가 명확하여, 하드웨어 보안 주권 관점에서의 접촉 명분이 충분합니다.",
      "hook_type": "SOVEREIGN",
      "buying_signal": "금융위의 금융권 망분리 완화 가이드라인에 맞추어 보안 강화를 목적으로 한 내부 AI 에이전트 및 악성메일 대응 피싱 시나리오 자동화 시스템 도입을 본격 가속화하고 있습니다.",
      "infrastructure_signal": "망분리 및 MFA 다중인증, 접근통제 체계를 유지하는 폐쇄망 중심의 사내 인프라 환경을 가동 중입니다.",
      "timing_reason": "보안용 목적에 한해 망분리 규제가 선제 완화되면서 연내 정보보호 시스템에 AI 기술을 우선 도입하는 로드맵이 설정되어 즉각적인 아키텍처 제안 기회가 존재합니다.",
      "customer_win": "사내 내부망의 극도로 안전한 폐쇄형 온프레미스 환경 하에서 외부 통신 없이도 보안성 높고 지연 시간이 짧은 생성형 AI 에이전트를 저전력으로 구동할 수 있습니다.",
      "furiosa_win": "금융권 망분리 규제 완화의 첫 상징적 레퍼런스로서 타 제1금융권 및 대형 증권사로의 온프레미스 프라이빗 패키지 수평 확장을 도모할 수 있습니다.",
      "numeric_claims": [],
      "direct_sales_possibility": "MID",
      "csp_routed_sales_possibility": "HIGH",
      "npuaas_adoption_possibility": "LOW",
      "csp_capacity_expansion_possibility": "LOW",
      "contact_reason": "망분리 규제 완화에 따른 내부 정보보안 시스템 내 온프레미스 추론 서버 인프라 제안 목적입니다.",
      "outreach_talk_track": "최근 망분리 완화 가이드를 반영한 KB금융그룹의 AI 기반 사이버 보안 체계 구축 발표를 인상 깊게 보았습니다. 외부 인터넷 접속이 제한된 사내 보안망 안에서도 vLLM 컴패티블 환경을 통해 대형 모델을 보안 유출 없이 저비용 고성능으로 서비스할 수 있는 온프레미스 최적 가속기 RNGD에 대해 검토를 제안드립니다.",
      "revenue_timing": "중기",
      "decision_maker_hint": "CISO, 그룹정보보호부장, IT기획부장, 보안AI 아키텍처 실무 파트장",
      "existing_touchpoint": "확인 필요",
      "verification_needed": [
        "보안 에이전트 서비스 및 악성메일 피싱 생성 솔루션 내 탑재 예정인 경량 LLM(SMM) 규격 파악",
        "자체 구축 예정인지 혹은 SI 파트너(예: 삼성SDS, KB데이타시스템 등)를 경유하는지 구조 파악 필요"
      ],
      "source_ids": [
        "S001",
        "S006",
        "S008",
        "S009",
        "S010"
      ],
      "source_urls": [
        "https://www.gosiweek.com/article/1065608272873992",
        "https://biz.heraldcorp.com/article/10755783?ref=naver",
        "https://www.straightnews.co.kr/news/articleView.html?idxno=303329",
        "https://www.seoultimes.news/news/article.html?no=2000095985",
        "https://www.ziksir.com/news/articleView.html?idxno=134842"
      ]
    },
    {
      "name": "서울아산병원",
      "country": "KR",
      "market": "B2B",
      "target_type": "온프레미스 기업",
      "classification": "watchlist",
      "confirmed_project_or_signal": "응급환자 프로토콜 지원 폐쇄망 내부 온프레미스 AI 시스템 성공적 실증",
      "confirmed_model_name": "미확인",
      "model_match_status": "unknown",
      "model_fit_score": "UNKNOWN",
      "deployment_fit_score": "HIGH",
      "channel_fit_score": "LOW",
      "rngd_fit_score": "MID",
      "outreach_priority": "MID",
      "fit_vs_priority_explanation": "사용 모델 정보는 미확인이지만 환자 정보 보안을 극대화하기 위해 폐쇄망 하드웨어 인프라를 지향하는 확실한 도메인 신호가 존재하여 향후 하드웨어 수급 제안 대상군으로 적합합니다.",
      "hook_type": "SOVEREIGN",
      "buying_signal": "디지털정보혁신본부의 주도 하에 환자 민감 정보 보호를 위해 외부 클라우드가 차단된 온프레미스 폐쇄망 환경에서 정상 작동하는 응급 프로토콜 AI 시스템을 성공적으로 실증 완료했습니다.",
      "infrastructure_signal": "원내에 폐쇄형 GPU 인프라 혹은 보안 온프레미스 서버 인프라를 직접 구동 중입니다.",
      "timing_reason": "원내 응급실 등 실전 배치와 의료 데이터 활용 인프라 고도화 계획이 구체화되는 현 시점에 적격 제안 타이밍입니다.",
      "customer_win": "외부 클라우드로의 의료 데이터 유출 리스크를 원천 차단하면서, 온프레미스 랙 내에서 환자 생명과 연관된 의료 대용량 임상 매뉴얼 데이터 추론 속도를 높이고 서버실 전력 비용을 줄일 수 있습니다.",
      "furiosa_win": "보수적인 대형 병원 도메인에서 폐쇄형 온프레미스 의료 AI 구동용 인프라 표준 레퍼런스를 확보하여 타 주요 대학병원으로 확산할 기반을 마련합니다.",
      "numeric_claims": [],
      "direct_sales_possibility": "MID",
      "csp_routed_sales_possibility": "LOW",
      "npuaas_adoption_possibility": "LOW",
      "csp_capacity_expansion_possibility": "LOW",
      "contact_reason": "보안망 내 고성능 저지연 응급 의료 LLM 실무 운영을 위한 온프레미스 가속기 공급 제안 목적입니다.",
      "outreach_talk_track": "최근 폐쇄망 환경에서 응급환자 프로토콜 AI 시스템을 완벽히 구축해내신 행보를 전해 들었습니다. 민감 정보 처리를 위한 내부 서버실의 전력 부담과 랙 상면 문제를 획기적으로 낮추면서도 의료진의 다중 동시 추론 질의를 지연 없이 처리해내는 국산 추론 칩 RNGD 도입 방안을 제안드리고자 합니다.",
      "revenue_timing": "장기",
      "decision_maker_hint": "디지털정보혁신본부장, 의료정보센터 파트장, 전산정보팀 인프라 담당 임원",
      "existing_touchpoint": "확인 필요",
      "verification_needed": [
        "병원 원내 전산실 서버 랙 전력 한계치 및 추가 확장 한계 검증",
        "응급환자 프로토콜 솔루션 자체에 적용된 소형 특화 모델 아키텍처 정보 확인 필요"
      ],
      "source_ids": [
        "S012"
      ],
      "source_urls": [
        "https://www.newsis.com/view/NISX20260518_0003634573"
      ]
    },
    {
      "name": "시스트란",
      "country": "KR",
      "market": "B2B",
      "target_type": "온프레미스 기업",
      "classification": "structure_check",
      "confirmed_project_or_signal": "'AI EXPO Korea 2026'서 폐쇄망 맞춤형 온프레미스 AI 솔루션 4종 공개",
      "confirmed_model_name": "미확인",
      "model_match_status": "unknown",
      "model_fit_score": "UNKNOWN",
      "deployment_fit_score": "HIGH",
      "channel_fit_score": "MID",
      "rngd_fit_score": "MID",
      "outreach_priority": "MID",
      "fit_vs_priority_explanation": "사용하는 구체적인 프라이빗 모델은 미공개 상태이나, 기업 내부 독립 온프레미스 폐쇄망 공급을 위해 자사 패키지에 특화 가속기를 탑재/번들링할 수 있는 잠재적 파트너 파이프라인으로 적합합니다.",
      "hook_type": "PARTNER",
      "buying_signal": "사내 정보 유출 우려를 해소하는 폐쇄망 독립형 AI 솔루션에 특화하여 AI 엑스포 등지에서 온프레미스 맞춤 포트폴리오를 대대적으로 홍보하고 있습니다.",
      "infrastructure_signal": "외부 클라우드 연결이 완벽히 차단된 순수 내부 온프레미스 환경에 단독 배포 가능한 소프트웨어 패키징 방식을 지원합니다.",
      "timing_reason": "최근 온프레미스 폐쇄망 기반 4종 맞춤형 솔루션을 정식 출시 및 마케팅하는 타이밍으로 하드웨어 번들 협의를 전개하기에 우호적인 여건입니다.",
      "customer_win": "고객사 구축 시 GPU 서버 공급 단가 상승으로 인한 제안 경쟁력 저하 문제를 가성비와 전력비 우위의 RNGD 연동을 통해 해결할 수 있습니다.",
      "furiosa_win": "폐쇄망 엔터프라이즈 AI 번역 및 문서 처리 시장의 선도적 패키지 소프트웨어사와의 연동을 기반으로 다수의 소규모 프라이빗 AI 수주 레퍼런스를 확보할 수 있습니다.",
      "numeric_claims": [],
      "direct_sales_possibility": "LOW",
      "csp_routed_sales_possibility": "LOW",
      "npuaas_adoption_possibility": "LOW",
      "csp_capacity_expansion_possibility": "LOW",
      "contact_reason": "프라이빗 폐쇄망 AI 솔루션의 고성능 저비용 제안을 위한 하드웨어 연동 및 파트너십 구축 목적입니다.",
      "outreach_talk_track": "최근 AI 엑스포에서 공개하신 폐쇄망 맞춤형 온프레미스 AI 제품군을 매우 인상 깊게 보았습니다. 기업 보안을 확보하면서 연산 효율을 높여야 하는 시스트란의 고객사들에게 뛰어난 전력 효율의 RNGD가 탑재된 온프레미스 서버 패키지를 공동 제안하여 윈윈 구조를 만들고 싶습니다.",
      "revenue_timing": "중기",
      "decision_maker_hint": "CTO, 솔루션연구소장, 비즈니스개발(BD) 부서장",
      "existing_touchpoint": "확인 필요",
      "verification_needed": [
        "시스트란 온프레미스 시스템의 주요 기반 LLM 아키텍처(Llama 기반 여부 등) 기술 규격 확인",
        "번들 판매를 위한 가속기 탑재 전용 어플라이언스 기획 가능성 검토"
      ],
      "source_ids": [
        "S002"
      ],
      "source_urls": [
        "https://www.etnews.com/20260522000276"
      ]
    },
    {
      "name": "오픈네트웍시스템",
      "country": "KR",
      "market": "B2B",
      "target_type": "CSP 고객 기업",
      "classification": "structure_check",
      "confirmed_project_or_signal": "Dify 운영사 랭지니어스 국내 독점 공식 계약 체결 및 에이전트 플랫폼 구축 상담 확대",
      "confirmed_model_name": "미확인",
      "model_match_status": "unknown",
      "model_fit_score": "UNKNOWN",
      "deployment_fit_score": "MID",
      "channel_fit_score": "MID",
      "rngd_fit_score": "MID",
      "outreach_priority": "MID",
      "fit_vs_priority_explanation": "자체 생성 모델보다는 LLM 게이트웨이 및 에이전틱 프레임워크인 Dify의 연동에 특화되어 있어 특정 단일 모델 적합도는 UNKNOWN이지만, 고성능 멀티 모델 서빙 허브 인프라 구축 수요를 견인하는 역할로 유효합니다.",
      "hook_type": "VLLM",
      "buying_signal": "Dify 기반 AI 에이전트 서비스, 스마트 브로슈어 OCR 및 자연어 기반 SQL 데이터 조회 등 다채로운 상담 사례를 구축하며 엔터프라이즈 에이전트 엔진 수요를 확대하고 있습니다.",
      "infrastructure_signal": "다중 LLM 서빙 환경 및 멀티모델 추론 백엔드 오케스트레이션 설계를 다루고 있습니다.",
      "timing_reason": "AI 엑스포 참가 후 다수 기업 고객들을 상대로 구체적인 에이전틱 플랫폼 구축 및 클라우드/온프레미스 인프라 하이브리드 제안 영업을 구체화하는 국면입니다.",
      "customer_win": "고객사들이 Dify 인프라를 백엔드에서 지탱하는 추론 비용을 극적으로 줄이면서 대량의 API 호출 및 토큰 처리를 원활히 관리하도록 도움을 줍니다.",
      "furiosa_win": "Dify 프레임워크와 vLLM/RNGD 백엔드 통합 레퍼런스를 개척하여, 에이전트 플랫폼 단위로 NPU 인프라가 표준 통합되는 대형 GTM 고리를 확보할 수 있습니다.",
      "numeric_claims": [],
      "direct_sales_possibility": "LOW",
      "csp_routed_sales_possibility": "MID",
      "npuaas_adoption_possibility": "HIGH",
      "csp_capacity_expansion_possibility": "LOW",
      "contact_reason": "Dify 프라이빗 에이전틱 플랫폼의 온프레미스/클라우드 추론 백엔드 고효율 최적화 공동 영업 제의 목적입니다.",
      "outreach_talk_track": "Dify 운영사인 랭지니어스와의 공식 파트너십 및 에이전틱 워크플로우 기술 지원 사례를 높이 평가합니다. Dify 기반의 기업용 프라이빗 서비스 시 추론 백엔드의 리소스를 대폭 경감하고 API 처리량을 늘려주는 RNGD-vLLM 통합 서빙 플랫폼 구성에 대해 논의를 희망합니다.",
      "revenue_timing": "중기",
      "decision_maker_hint": "솔루션개발본부장, 기술영업총괄, AI 비즈니스본부장",
      "existing_touchpoint": "확인 필요",
      "verification_needed": [
        "Dify 백엔드 오케스트레이션 엔진 내 vLLM / OpenAI API 규격 완벽 대응 여부 확인",
        "실무 PoC 고객군 중 특정 CSP 클라우드를 가호스팅 영역으로 사용하는지 조사"
      ],
      "source_ids": [
        "S020",
        "S021",
        "S023"
      ],
      "source_urls": [
        "https://www.joongang.co.kr/article/25430014",
        "https://www.gokorea.kr/news/articleView.html?idxno=866999",
        "https://www.sentv.co.kr/article/view/sentv202605190084"
      ]
    }
  ],
  "competitor_signals": [
    {
      "competitor": "리벨리온",
      "signal_type": "public_sector_win",
      "summary": "가비아가 과학기술정보통신부의 ‘2026년 고성능 컴퓨팅 지원사업’ 공급기업으로 선정되며 수혜 중소벤처기업 및 연구자들에게 리벨리온의 NPU 인프라를 가상 클라우드 형태로 공급하게 되었습니다.",
      "source_id": "S038",
      "source_url": "https://www.ajunews.com/view/20260526082847223",
      "evidence_excerpt": "가비아가 정부의 ‘2026년 고성능 컴퓨팅 지원사업’ 공급기업으로 선정… 리벨리온 NPU 제공"
    }
  ],
  "noise_examples": [
    {
      "source_id": "S007",
      "title": "[제약업계 소식] 5월 26일",
      "reason": "제약 분야 강연 소식이 주로 다루어져 있으며 AI 부문은 타사 에이전트 출시의 1줄짜리 단순 언급에 그치고 있어 GTM 유효 타깃으로 분류하기에 부적합합니다."
    },
    {
      "source_id": "S019",
      "title": "산업수도 울산 찾은 이형주 회장...\"회원 보호·업역 확대\" 강조",
      "description": "나라장터 단가 현실화 언급이 있으나 이는 전기공사업계 실적증명 및 실질 단가에 국한된 논의로 AI 시스템 도입과는 무관한 소스입니다."
    },
    {
      "source_id": "S022",
      "title": "\"수수료는 챙기고 민원은 나몰라라?\"...당근·번개장터 등 중고거래 플...",
      "reason": "중고 거래 중개 서비스에서의 수수료 및 단순 챗봇 고객 불만을 다룬 소식으로, 고성능 인프라 수요나 AI 추론 하드웨어 GTM 신호와는 연관성이 없습니다."
    }
  ],
  "eval_notes": [
    "이번 주 소스에서는 대규모 금융권 망분리 규제 완화(보안 분야 선도입) 신호가 매우 강력하게 부각되었습니다.",
    "이러한 보안 인프라 완화와 대형 병원들의 온프레미스 구축 실증 성공은 보안 주권을 무기로 하는 RNGD 솔루션에 매우 적합한 타이밍을 선사합니다.",
    "다만 타깃 기업들이 구체적인 실무 지원 모델 명칭을 외부 기사에 밝히지 않고 있으므로, 세부 아키텍처 파악을 위한 실무 엔지니어 접촉이 전제되어야 합니다.",
    "삼성SDS 및 엘리스그룹과 같은 하이브리드 파트너/CSP 운영 후보군들은 자체적으로 거대 투자를 가시화하고 있으므로 NPUaaS 조기 입점을 위한 최우선 컨택을 강력히 제안합니다."
  ]
}
```