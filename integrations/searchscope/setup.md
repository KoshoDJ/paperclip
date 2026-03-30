# SearchScope Integration Setup
## FightForge × StackEngine

SearchScope is a Claude Code agent by Wayne Ergle / StackEngine that analyzes
the full search landscape for any topic — Google organic, AI Overviews, and AI
platforms — and delivers scored, reasoned keyword cluster recommendations to Airtable.

In FightForge, the SEO Analyst Agent reads SearchScope output from Airtable
to build monthly rank reports and content recommendations.

---

## Prerequisites

- SearchScope files from the StackEngine Circle community (Wayne Ergle)
- DataForSEO account with API credentials
- Airtable account

---

## Per-Client Setup (One Time)

### Step 1: Copy the StackEngine Master Airtable Base
1. Open the StackEngine master SearchScope base (link provided by Wayne)
2. Click **Copy base** in Airtable
3. Name it: `SearchScope — [Client School Name]`
4. Note the base ID from the URL: `https://airtable.com/app[BASE_ID]/...`

### Step 2: Configure searchscope.json
In the SearchScope project directory:

```json
{
  "airtable_base_id": "app[YOUR_BASE_ID]",
  "location": "United States",
  "language_code": "en",
  "keyword_limit_per_endpoint": 100,
  "serp_sample_size": 5,
  "llm_response_sample_size": 3
}
```

### Step 3: Configure MCP Servers
Add to your Claude Code MCP config:

```json
{
  "mcpServers": {
    "airtable": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-airtable"],
      "env": { "AIRTABLE_API_KEY": "pat..." }
    },
    "dfs-mcp": {
      "command": "npx",
      "args": ["-y", "@dataforseo/mcp-server"],
      "env": {
        "DATAFORSEO_USERNAME": "your@email.com",
        "DATAFORSEO_PASSWORD": "your-password"
      }
    }
  }
}
```

### Step 4: Run Brand Analysis
Start a Claude Code session in the SearchScope directory:
```
/brand [client-website-url]
```

SearchScope will analyze the school's website and build a brand profile.
Review and confirm the profile before proceeding.

### Step 5: Run Initial Topic Analysis
```
/run [primary style + city]
```
Example: `/run karate el cajon`

SearchScope will:
- Expand 100–300 keywords
- Analyze SERP landscape for representative keywords
- Check LLM responses for primary clusters
- Score and categorize all clusters
- Write everything to Airtable

### Step 6: Connect to FightForge SEO Analyst Agent
Add the client's SearchScope Airtable base ID to their `client-config.json`:
```json
"searchscope_airtable_base": "app[BASE_ID]"
```

The SEO Analyst Agent reads this base on its 8h heartbeat.

---

## Monthly Cadence

SearchScope runs on the 1st of each month per client.
The SEO Analyst Agent triggers the run and reads the output.
Content tickets are created from high-scoring clusters with content gaps.

---

## Estimated Cost Per Run

| Client Size | Topics | Est. DataForSEO Cost |
|---|---|---|
| Single location school | 3–5 topics | $3–8/month |
| Multi-program school | 5–8 topics | $5–12/month |
| Full agency run (10 clients) | varies | $30–80/month |

Costs are tracked in the Assessments table in Airtable per run.
