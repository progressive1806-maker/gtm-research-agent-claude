# LLM Evaluation Notes

## LLM metadata

- provider: `gemini`
- model: `gemini-3.1-flash-lite`
- llm_sources_count: `40`
- max_llm_sources: `40`
- max_source_chars: `800`
- max_output_candidates: `12`
- evaluated_at_kst: `2026-05-26T17:49:53.140097+09:00`

## Run summary

- overall_assessment: NHN클라우드의 'FactoryX' 출시와 국내 CSP들의 AI 데이터센터 경쟁이 본격화됨에 따라 NPUaaS 및 CSP capacity expansion 타깃이 구체화됨. 공공/금융 망분리 완화와 연계된 폐쇄망 온프레미스 기회 또한 중요한 GTM 포인트.
- top_priority_names: NHN클라우드, KB금융, 삼성SDS
- noise_ratio_comment: 수집된 40건 중 대부분이 데이터센터 인프라 및 금융 보안 관련 전략 보도로 GTM 관련성이 매우 높음.
- model_compatibility_caution: NHN클라우드 등이 국산 NPU를 이미 도입 중이나, FuriosaAI 모델 호환은 버전별 확인이 필수.

## Eval notes

- 구미 AI 데이터센터 관련 삼성SDS와 지자체 협력 정황은 향후 주요 타깃으로 포함 가능성이 높음.
- B2G 조달 부문에서는 나라장터 입점 전략을 가진 경쟁사 움직임이 포착됨.

## Raw LLM response

```json
{
  "run_summary": {
    "overall_assessment": "NHN클라우드의 'FactoryX' 출시와 국내 CSP들의 AI 데이터센터 경쟁이 본격화됨에 따라 NPUaaS 및 CSP capacity expansion 타깃이 구체화됨. 공공/금융 망분리 완화와 연계된 폐쇄망 온프레미스 기회 또한 중요한 GTM 포인트.",
    "top_priority_names": ["NHN클라우드", "KB금융", "삼성SDS"],
    "noise_ratio_comment": "수집된 40건 중 대부분이 데이터센터 인프라 및 금융 보안 관련 전략 보도로 GTM 관련성이 매우 높음.",
    "model_compatibility_caution": "NHN클라우드 등이 국산 NPU를 이미 도입 중이나, FuriosaAI 모델 호환은 버전별 확인이 필수."
  },
  "candidates": [
    {
      "name": "NHN클라우드",
      "country": "KR",
      "market": "B2B",
      "target_type": "CSP 운영 기업",
      "classification": "cloud_npuaaS_lead",
      "confirmed_project_or_signal": "AI 풀스택 브랜드 'FactoryX' 출시 및 광주/서울 AI 데이터센터 운영",
      "confirmed_model_name": "미확인",
      "model_match_status": "unknown",
      "model_fit_score": "UNKNOWN",
      "deployment_fit_score": "HIGH",
      "channel_fit_score": "HIGH",
      "rngd_fit_score": "MID",
      "outreach_priority": "HIGH",
      "fit_vs_priority_explanation": "모델 호환성은 미확인이지만, NHN클라우드의 팩토리X와 광주 AI 데이터센터에서 국산 NPU 통합 운영 의지를 밝혀 CSP capacity expansion 및 NPUaaS 연계 가능성이 매우 높음.",
      "hook_type": "CLOUD",
      "buying_signal": "GPU 수급난 대응 및 AI 추론 효율 극대화를 위한 국산 NPU 도입 가속화",
      "infrastructure_signal": "서울/광주 AI 전용 데이터센터 내 엔비디아 GPU 및 국산 NPU 하이브리드 운영",
      "timing_reason": "FactoryX 브랜드 공식 출범 및 팩토리X 서울 데이터센터 구축 시점",
      "customer_win": "엔비디아 의존도를 낮추고 국산 NPU를 통한 추론 최적화 및 비용 효율화",
      "furiosa_win": "국내 주요 AI CSP 파트너 확보 및 대규모 추론 인프라 레퍼런스 구축",
      "numeric_claims": [
        {
          "claim": "B200 GPU 7656장 투입",
          "source_id": "S038",
          "source_url": "https://www.hankyung.com/article/2026052699161",
          "evidence_text": "엔비디아 B200 GPU 7656장을 기반으로 총 27..."
        }
      ],
      "direct_sales_possibility": "MID",
      "csp_routed_sales_possibility": "HIGH",
      "npuaas_adoption_possibility": "HIGH",
      "csp_capacity_expansion_possibility": "HIGH",
      "contact_reason": "FactoryX 내 국산 NPU 생태계 구축 관련 FuriosaAI의 최적화 스택 연동 논의",
      "outreach_talk_track": "최근 팩토리X 출시 소식을 확인했습니다. 당사의 RNGD 인프라가 NHN클라우드의 AI 추론 풀스택 환경에서 효율적으로 구동될 수 있도록 기술적 협력을 검토하고 싶습니다.",
      "revenue_timing": "중기",
      "decision_maker_hint": "김태형 CTO / AI 인프라 사업 총괄 임원",
      "existing_touchpoint": "확인 필요",
      "verification_needed": ["NPU 통합 운영 구체적 사양", "팩토리X 내 FuriosaAI 솔루션 탑재 로드맵"],
      "source_ids": ["S006", "S026", "S033", "S035", "S038", "S039", "S040"],
      "source_urls": ["http://www.biztribune.co.kr/news/articleView.html?idxno=354147", "https://www.megaeconomy.co.kr/news/newsview.php?ncode=1065579909469061", "https://www.mhj21.com/news/articleView.html?idxno=252348", "https://biz.chosun.com/it-science/ict/2026/05/26/K73CFXG73NGZLDYOLJYKKMARGM/?utm_source=naver&utm_medium=original&utm_campaign=biz", "https://www.hankyung.com/article/2026052699161", "https://www.sedaily.com/article/20048370?ref=naver", "https://news.mtn.co.kr/news-detail/2026052616115639487"]
    },
    {
      "name": "KB금융",
      "country": "KR",
      "market": "B2B",
      "target_type": "온프레미스 기업",
      "classification": "priority_outreach",
      "confirmed_project_or_signal": "제로트러스트 및 망분리 완화에 따른 AI 보안 고도화",
      "confirmed_model_name": "미확인",
      "model_match_status": "unknown",
      "model_fit_score": "UNKNOWN",
      "deployment_fit_score": "HIGH",
      "channel_fit_score": "MID",
      "rngd_fit_score": "MID",
      "outreach_priority": "HIGH",
      "fit_vs_priority_explanation": "금융권 망분리 완화로 인해 폐쇄망 환경 내 고성능 추론 수요가 급증함. 모델명은 확인되지 않았으나 규제 대응형 폐쇄망 구축 신호가 매우 강함.",
      "hook_type": "SOVEREIGN",
      "buying_signal": "망분리 완화 정책에 따른 AI 에이전트 및 폐쇄망 내부 플랫폼 구축",
      "infrastructure_signal": "제로트러스트 기반의 사내 구축형 보안 시스템 및 망분리 환경 유지",
      "timing_reason": "금융위 망분리 완화 정책 시행 및 그룹 차원의 AI 보안 체계 고도화 시점",
      "customer_win": "보안 규제를 준수하면서도 최신 AI 에이전트를 폐쇄망 내부에서 운영하여 데이터 보안성 확보",
      "furiosa_win": "금융권 레퍼런스 확보 및 망분리 환경에서 요구되는 온프레미스 AI 인프라 최적화 기회",
      "numeric_claims": [],
      "direct_sales_possibility": "HIGH",
      "csp_routed_sales_possibility": "MID",
      "npuaas_adoption_possibility": "LOW",
      "csp_capacity_expansion_possibility": "LOW",
      "contact_reason": "금융권 제로트러스트 보안 체계에 적합한 온프레미스 인프라 제공 논의",
      "outreach_talk_track": "금융권 망분리 완화와 AI 에이전트 도입 전략에 대해 깊은 관심을 가지고 있습니다. 당사의 온프레미스 최적화 인프라가 KB금융의 보안 신뢰성을 강화하며 AI 성능을 높이는 데 기여할 수 있는지 검토하고 싶습니다.",
      "revenue_timing": "단기",
      "decision_maker_hint": "CIO / CISO / Head of AI, KB금융 디지털/AI 전략 부문",
      "existing_touchpoint": "확인 필요",
      "verification_needed": ["금융 데이터센터 내 인프라 증설 계획", "폐쇄망용 LLM 도입 로드맵"],
      "source_ids": ["S001", "S005", "S012", "S015", "S016"],
      "source_urls": ["http://www.dailypop.kr/news/articleView.html?idxno=99156", "https://news.bizwatch.co.kr/article/finance/2026/05/22/0043", "https://www.socialvalue.kr/news/view/1065600234596663", "http://www.thefirstmedia.net/news/articleView.html?idxno=199980", "https://www.todayeconomic.com/news/article.html?no=30719"]
    }
  ],
  "competitor_signals": [
    {
      "competitor": "모빌린트",
      "signal_type": "public_sector_win",
      "summary": "조달청 혁신제품으로 등록되어 공공기관 인프라 시장 공략 본격화",
      "source_id": "S017",
      "source_url": "https://www.mt.co.kr/future/2026/05/26/2026052214135044338",
      "evidence_excerpt": "모빌린트의 AI 가속기... 조달청 혁신제품에 등록되면 중앙부처와 지방자치단체, 공공기관은 나라장터를 통해..."
    }
  ],
  "noise_examples": [
    {
      "source_id": "S024",
      "title": "중고거래 플랫폼 민원",
      "reason": "단순 소비자 민원 및 플랫폼 운영 관련 기사로 AI 인프라 사업과는 관련성이 낮음"
    }
  ],
  "eval_notes": [
    "구미 AI 데이터센터 관련 삼성SDS와 지자체 협력 정황은 향후 주요 타깃으로 포함 가능성이 높음.",
    "B2G 조달 부문에서는 나라장터 입점 전략을 가진 경쟁사 움직임이 포착됨."
  ]
}
```