# LLM Evaluation Notes

## LLM metadata

- provider: `gemini`
- model: `gemini-3.1-flash-lite`
- llm_sources_count: `40`
- max_llm_sources: `40`
- max_source_chars: `800`
- max_output_candidates: `12`
- evaluated_at_kst: `2026-05-26T16:13:07.389913+09:00`

## Run summary

- overall_assessment: NHN클라우드와 삼성SDS 등 주요 국내 CSP들이 엑사스케일 규모의 AI 데이터센터와 GPUaaS/NPUaaS 인프라를 본격 가동하며 국산 NPU 도입을 위한 기반을 마련함. 금융권 망분리 규제 완화에 따른 AI 보안 솔루션 수요가 단기 급증 예상.
- top_priority_names: NHN클라우드, 삼성SDS, KB금융그룹
- noise_ratio_comment: 공공/금융 망분리 이슈와 NHN클라우드 신규 인프라 발표 위주의 유의미한 소스 위주로 구성되어 noise는 매우 낮음.
- model_compatibility_caution: NHN클라우드 및 삼성SDS 등이 국산 NPU를 이미 혼합 운영 중임을 명시했으나, 구체적인 Furiosa RNGD 채택 여부는 확인되지 않음. 모델 호환성보다는 인프라/데이터센터 용량 중심의 전략적 접근이 필요함.

## Eval notes

- 금융권 망분리 완화 정책이 RNGD의 폐쇄망 타겟 시장에 강력한 구매 신호로 작용함.
- NHN클라우드의 팩토리X는 추후 Furiosa의 인프라 파트너십 혹은 NPUaaS 연동의 핵심 테스트베드가 될 가능성이 높음.
- competitor_signals 중 유의미한 GTM 관련 항목은 1건임.

## Raw LLM response

```json
{
  "run_summary": {
    "overall_assessment": "NHN클라우드와 삼성SDS 등 주요 국내 CSP들이 엑사스케일 규모의 AI 데이터센터와 GPUaaS/NPUaaS 인프라를 본격 가동하며 국산 NPU 도입을 위한 기반을 마련함. 금융권 망분리 규제 완화에 따른 AI 보안 솔루션 수요가 단기 급증 예상.",
    "top_priority_names": [
      "NHN클라우드",
      "삼성SDS",
      "KB금융그룹"
    ],
    "noise_ratio_comment": "공공/금융 망분리 이슈와 NHN클라우드 신규 인프라 발표 위주의 유의미한 소스 위주로 구성되어 noise는 매우 낮음.",
    "model_compatibility_caution": "NHN클라우드 및 삼성SDS 등이 국산 NPU를 이미 혼합 운영 중임을 명시했으나, 구체적인 Furiosa RNGD 채택 여부는 확인되지 않음. 모델 호환성보다는 인프라/데이터센터 용량 중심의 전략적 접근이 필요함."
  },
  "candidates": [
    {
      "name": "NHN클라우드",
      "country": "KR",
      "market": "B2B",
      "target_type": "CSP 운영 기업",
      "classification": "cloud_npuaaS_lead",
      "confirmed_project_or_signal": "AI 풀스택 브랜드 '팩토리X' 공개 및 27.4EF 규모 엑사스케일 AI 인프라 구축",
      "confirmed_model_name": "미확인",
      "model_match_status": "unknown",
      "model_fit_score": "UNKNOWN",
      "deployment_fit_score": "HIGH",
      "channel_fit_score": "HIGH",
      "rngd_fit_score": "MID",
      "outreach_priority": "HIGH",
      "fit_vs_priority_explanation": "모델 적합성은 미확인이지만, NHN이 팩토리X를 통해 대규모 GPU/NPU 혼합 운영 환경을 구축 중이며 인프라 확충이 필수적인 CSP 운영사이므로 우선순위가 높음.",
      "hook_type": "CLOUD",
      "buying_signal": "27.4EF 규모의 엑사스케일 AI 인프라를 위한 가속기 다변화 필요성",
      "infrastructure_signal": "엔비디아 B200 7,656장 기반 팩토리X 서울 데이터센터 운영",
      "timing_reason": "팩토리X 브랜드 런칭 시점에 맞춰 국산 NPUaaS 연계 전략 논의 가능",
      "customer_win": "외산 GPU 의존도를 낮추고 국산 NPU 기반의 효율적 추론 인프라를 구축하여 운영 효율성 제고 가능.",
      "furiosa_win": "국내 최대 규모 GPU 클러스터 사업자에 Furiosa RNGD 솔루션을 PoC/도입할 수 있는 전략적 요충지 확보.",
      "numeric_claims": [
        {
          "claim": "B200 GPU 7,656장 규모 데이터센터",
          "source_id": "S005",
          "source_url": "https://www.lcnews.co.kr/news/articleView.html?idxno=202630",
          "evidence_text": "B200 7656장으로 구성한 27.4EF(엑사플롭스) 규모의 국내 최초 엑사스케일 AI"
        }
      ],
      "direct_sales_possibility": "MID",
      "csp_routed_sales_possibility": "HIGH",
      "npuaas_adoption_possibility": "HIGH",
      "csp_capacity_expansion_possibility": "HIGH",
      "contact_reason": "국내 엑사스케일 AI 인프라 확장에 따른 추론용 NPUaaS 협력 논의",
      "outreach_talk_track": "NHN클라우드의 팩토리X 런칭을 축하드립니다. 대규모 엑사스케일 인프라에서 추론 비용 효율을 극대화하기 위한 Furiosa RNGD의 Kubernetes 기반 Cloud Native Toolkit 활용 방안을 논의하고 싶습니다.",
      "revenue_timing": "중기",
      "decision_maker_hint": "Head of AI Infrastructure, Head of Cloud, NPUaaS Product Lead",
      "existing_touchpoint": "확인 필요",
      "verification_needed": [
        "기존 국산 NPU 운영 구체 사양 확인"
      ],
      "source_ids": [
        "S005",
        "S027",
        "S039",
        "S040"
      ],
      "source_urls": [
        "https://www.lcnews.co.kr/news/articleView.html?idxno=202630",
        "https://www.metroseoul.co.kr/article/20260526500320",
        "https://www.getnews.co.kr/news/articleView.html?idxno=870933",
        "http://www.inews24.com/view/1971407"
      ]
    },
    {
      "name": "삼성SDS",
      "country": "KR",
      "market": "B2B",
      "target_type": "CSP 운영 기업",
      "classification": "priority_outreach",
      "confirmed_project_or_signal": "구미 데이터센터 60MW급 AI 전력 확보 및 SCP 고도화",
      "confirmed_model_name": "미확인",
      "model_match_status": "unknown",
      "model_fit_score": "UNKNOWN",
      "deployment_fit_score": "HIGH",
      "channel_fit_score": "HIGH",
      "rngd_fit_score": "MID",
      "outreach_priority": "HIGH",
      "fit_vs_priority_explanation": "CSP 운영 및 대규모 데이터센터 확장 기조가 명확하며 SCP/NPUaaS 경로로의 파급력이 매우 큼.",
      "hook_type": "POWER",
      "buying_signal": "구미 데이터센터 60MW급 AI 인프라 증설",
      "infrastructure_signal": "데이터센터 가동을 위한 대규모 전력 확보 단계",
      "timing_reason": "전력 효율이 핵심인 신규 데이터센터 구축 단계에서 고효율 NPU 도입 명분 강화",
      "customer_win": "전력 효율이 우수한 국산 RNGD 도입을 통해 데이터센터 운영 안정성 및 비용 절감 가능.",
      "furiosa_win": "삼성SDS CSP/SCP 생태계 내 주요 NPU 벤더로 진입하여 대규모 공공/금융 고객 확보 기회.",
      "numeric_claims": [
        {
          "claim": "60MW급 AI 데이터센터 증설",
          "source_id": "S037",
          "source_url": "https://www.mt.co.kr/tech/2026/05/23/2026052210211399740",
          "evidence_text": "삼성SDS는 경북 구미에 4273억원을 투자해 60MW 규모 AI 데이터센터를 짓기로 했다."
        }
      ],
      "direct_sales_possibility": "MID",
      "csp_routed_sales_possibility": "HIGH",
      "npuaas_adoption_possibility": "HIGH",
      "csp_capacity_expansion_possibility": "HIGH",
      "contact_reason": "구미 데이터센터 신규 구축에 따른 추론 인프라 다변화 논의",
      "outreach_talk_track": "삼성SDS의 구미 데이터센터 구축을 통한 AI 인프라 확장을 확인했습니다. 전력 제약이 심화되는 데이터센터 환경에서 RNGD의 전력 효율을 기반으로 한 NPUaaS 운영 최적화 방안을 검토 요청드립니다.",
      "revenue_timing": "중기",
      "decision_maker_hint": "Head of Data Center, Head of Cloud Infrastructure",
      "existing_touchpoint": "확인 필요",
      "verification_needed": [
        "구미 데이터센터 내 AI 가속기 선정 일정"
      ],
      "source_ids": [
        "S026",
        "S031",
        "S036",
        "S037"
      ],
      "source_urls": [
        "https://www.e-science.co.kr/news/articleView.html?idxno=130004",
        "https://www.ddaily.co.kr/page/view/2026052017342600376",
        "https://www.ddaily.co.kr/page/view/2026052509101133595",
        "https://www.mt.co.kr/tech/2026/05/23/2026052210211399740"
      ]
    },
    {
      "name": "KB금융그룹",
      "country": "KR",
      "market": "B2B",
      "target_type": "온프레미스 기업",
      "classification": "priority_outreach",
      "confirmed_project_or_signal": "망분리 규제 예외에 따른 AI 보안 에이전트 도입 및 사이버보안 체계 고도화",
      "confirmed_model_name": "미확인",
      "model_match_status": "none",
      "model_fit_score": "LOW",
      "deployment_fit_score": "HIGH",
      "channel_fit_score": "MID",
      "rngd_fit_score": "LOW",
      "outreach_priority": "HIGH",
      "fit_vs_priority_explanation": "금융권 망분리 규제 완화로 인해 온프레미스 AI 수요가 즉각적으로 발생할 수 있는 가장 강력한 B2B 타겟임.",
      "hook_type": "SOVEREIGN",
      "buying_signal": "금융위 망분리 규제 1년 한시적 면제에 따른 보안용 AI 솔루션 도입 필요",
      "infrastructure_signal": "금융권 폐쇄망 내 AI 에이전트 구축 수요",
      "timing_reason": "규제 완화 발표 직후 보안 에이전트 도입 추진 시점",
      "customer_win": "외부망 접속 없이 폐쇄망 내에서 동작하는 RNGD 기반의 온프레미스 보안 에이전트로 데이터 유출 우려 원천 차단.",
      "furiosa_win": "가장 규제가 까다로운 금융권 폐쇄망 내 레퍼런스 확보를 통해 여타 금융사 및 공공기관으로 확산 가능.",
      "numeric_claims": [],
      "direct_sales_possibility": "HIGH",
      "csp_routed_sales_possibility": "MID",
      "npuaas_adoption_possibility": "LOW",
      "csp_capacity_expansion_possibility": "LOW",
      "contact_reason": "금융권 망분리 예외 적용에 따른 프라이빗 보안 에이전트 인프라 도입 논의",
      "outreach_talk_track": "금융권 망분리 규제 완화에 발맞춘 보안 에이전트 도입 소식을 접했습니다. 데이터 주권이 중요한 환경에서 RNGD의 폐쇄망/온프레미스 특화 성능을 활용해 안전한 AI 인프라를 구축하는 방안을 함께 확인하고 싶습니다.",
      "revenue_timing": "단기",
      "decision_maker_hint": "CISO, Head of Digital Transformation, Head of AI Lab",
      "existing_touchpoint": "확인 필요",
      "verification_needed": [
        "보안 에이전트 구체 구축 인프라 사양"
      ],
      "source_ids": [
        "S007",
        "S010",
        "S012",
        "S013"
      ],
      "source_urls": [
        "https://www.todayeconomic.com/news/article.html?no=30719",
        "http://www.thevaluenews.co.kr/news/view.php?idx=198982",
        "https://www.ekn.kr/web/view.php?key=20260526029567819",
        "https://www.factin.co.kr/news/articleView.html?idxno=6365"
      ]
    }
  ],
  "competitor_signals": [
    {
      "competitor": "기타",
      "signal_type": "public_sector_win",
      "summary": "모빌린트가 조달청 혁신제품으로 등록되어 공공기관 AI 인프라 시장 공략을 본격화함.",
      "source_id": "S017",
      "source_url": "https://www.mt.co.kr/future/2026/05/26/2026052214135044338",
      "evidence_excerpt": "모빌린트 'NPU 솔루션' 조달청 혁신제품 등록…\"공공시장 공략\""
    }
  ],
  "noise_examples": [],
  "eval_notes": [
    "금융권 망분리 완화 정책이 RNGD의 폐쇄망 타겟 시장에 강력한 구매 신호로 작용함.",
    "NHN클라우드의 팩토리X는 추후 Furiosa의 인프라 파트너십 혹은 NPUaaS 연동의 핵심 테스트베드가 될 가능성이 높음.",
    "competitor_signals 중 유의미한 GTM 관련 항목은 1건임."
  ]
}
```