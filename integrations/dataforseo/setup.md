# DataForSEO Setup Guide
## FightForge Integration

DataForSEO provides the raw search intelligence that powers both SearchScope
(keyword research) and CitationScope (AI platform responses). It is the data
backbone of the FightForge SEO layer.

---

## Account Setup

1. Create account at https://dataforseo.com
2. Navigate to API Dashboard → API Access
3. Copy your **Login (email)** and **Password**
4. Add both to `.env`:
   ```
   DATAFORSEO_USERNAME=your@email.com
   DATAFORSEO_PASSWORD=your-api-password
   ```

---

## Endpoints Used by FightForge

### SearchScope (Monthly per client)
| Endpoint | Purpose | Est. Cost per Run |
|---|---|---|
| `dataforseo_labs_google_keyword_suggestions` | Primary keyword expansion | ~$0.075 |
| `dataforseo_labs_google_related_keywords` | Related keyword discovery | ~$0.075 |
| `dataforseo_labs_google_keyword_ideas` | Category-based discovery | ~$0.075 |
| `dataforseo_labs_search_intent` | Batch intent classification | ~$0.01/1000 kw |
| `ai_optimization_keyword_data_search_volume` | AI search volume proxy | ~$0.075 |
| `serp_organic_live_advanced` | SERP landscape sampling | ~$0.002/query |
| `ai_optimization_llm_response` | LLM platform responses | ~$0.02+/query |

### CitationScope (Weekly per client)
| Endpoint | Purpose | Est. Cost per Run |
|---|---|---|
| `ai_optimization_llm_response` | ChatGPT/Gemini/Perplexity/Claude queries | ~$0.05/query |
| `dataforseo_labs_google_keyword_overview` | Topic search volume enrichment | ~$0.01 |
| `dataforseo_labs_google_keyword_suggestions` | Related keyword context | ~$0.01 |
| `serp_organic_live_advanced` | Google AI Overview sampling | ~$0.002/query |
| `on_page_content_parsing` | Brand website analysis | ~$0.002/page |

---

## Monthly Cost Estimates (Per Active Client)

| Activity | Frequency | Est. Monthly Cost |
|---|---|---|
| SearchScope full run | 1×/month | $5–15 |
| CitationScope full run (10 topics) | 4×/month | $64 |
| SEO Analyst rank tracking | 8h heartbeat | $2–5 |
| **Total per client** | | **~$71–84/month** |

**At 10 clients:** ~$710–840/month DataForSEO
**At 20 clients:** ~$1,420–1,680/month DataForSEO

Budget these costs into client pricing. DataForSEO at this scale
is still 5–10x cheaper than equivalent SaaS subscriptions.

---

## API Response Optimization

Both SearchScope and CitationScope use the `.ai` response format
where available. Append `.ai` to endpoint URLs for LLM-optimized
responses — strips empty fields, reduces metadata, cuts token consumption.

This is handled automatically by both tools. No configuration needed.

---

## Rate Limits

DataForSEO enforces rate limits per account tier.
If rate limits are hit, both SearchScope and CitationScope
back off automatically and report the issue.

Recommended: Use separate DataForSEO API sub-users per client
for enterprise-scale deployments (10+ clients).
