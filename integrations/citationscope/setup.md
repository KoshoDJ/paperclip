# CitationScope Integration Setup
## FightForge × StackEngine

CitationScope is a Claude Code agent by Wayne Ergle / StackEngine that maps
where a brand sits in AI search across ChatGPT, Perplexity, Claude, and Gemini.
It generates prompt variations for each tracked topic, queries all four platforms,
classifies sentiment, and produces Citation Gap Briefs — content recommendations
that close AI visibility gaps.

In FightForge, the AEO/GEO Visibility Agent operates CitationScope weekly
for every active client.

---

## Prerequisites

- CitationScope files from the StackEngine Circle community (Dev.zip)
- DataForSEO account (same credentials as SearchScope)
- Airtable account

---

## Per-Client Setup (One Time)

### Step 1: Copy the CitationScope Airtable Base
1. Get the StackEngine master CitationScope base from Wayne's Circle community
2. Click **Copy base** in Airtable
3. Name it: `CitationScope — [Client School Name]`
4. Note the base ID from the URL

### Step 2: Configure citationscope.json
In the CitationScope Dev directory:

```json
{
  "airtable_base_id": "app[YOUR_BASE_ID]",
  "location": "United States",
  "language_code": "en",
  "prompts_per_topic": 8,
  "platforms": ["chat_gpt", "perplexity", "claude", "gemini"],
  "batch_size": 5,
  "cost_per_query": 0.05,
  "scheduled_run_day": "monday"
}
```

### Step 3: MCP Server Config
Same DataForSEO and Airtable MCP servers as SearchScope (see searchscope/setup.md).

### Step 4: Initial Brand Analysis and Topic Setup
Start Claude Code in the CitationScope Dev directory:

```
/brand [client-website-url]
```

CitationScope will analyze the site and suggest 10 topics.
Review and confirm. Standard FightForge starting topics:

1. `[style] school [city]`
2. `best [style] classes [city]`
3. `[style] for kids [city]`
4. `adult [style] classes [city]`
5. `[style] near me`
6. `self-defense classes [city]`
7. `[style] for beginners [city]`
8. `[school name]`
9. `[style] instructor [city]`
10. `martial arts school [city]`

### Step 5: Run Initial Baseline
```
/run
```

This establishes the baseline visibility score for all topics.
Record the baseline in the client's FightForge KPI dashboard.
All future runs are measured against this baseline.

### Step 6: Connect to FightForge AEO/GEO Agent
Add the client's CitationScope Airtable base ID to client-config.json:
```json
"citationscope_airtable_base": "app[BASE_ID]"
```

---

## Weekly Cadence

CitationScope runs every Monday morning per client.
The AEO/GEO Agent triggers `/scheduled-run` (non-interactive).
Results are read from Airtable and content tickets are created for zero-visibility topics.

---

## Estimated Cost

| Run Type | Prompts | Platforms | Est. Cost |
|---|---|---|---|
| Full run (10 topics × 8 prompts × 4 platforms) | 320 | 4 | ~$16 |
| Subset (1 topic × 8 prompts × 4 platforms) | 32 | 4 | ~$1.60 |
| Monthly total (4 weekly runs) | 1,280 | 4 | ~$64/client/month |

DataForSEO topic enrichment adds ~$0.20/run. Negligible.

**Budget rule:** Flag any run estimate over $25 to COO before executing.

---

## Known Issues (March 2026)

- **Perplexity 500 errors:** Known intermittent issue via DataForSEO API.
  When Perplexity fails, CitationScope continues with ChatGPT, Claude, and Gemini.
  Mark run as "Partial" in the Run record and note in weekly report.

---

## Citation Gap Brief → Content Ticket Flow

After every run, CitationScope generates Citation Gap Briefs in Airtable
(Content Recommendations table). The AEO/GEO Agent reads these and creates
content tickets for the Content Writer Agent via COO.

See `.agents/skills/aeo-geo/SKILL.md` for the full ticket template.
