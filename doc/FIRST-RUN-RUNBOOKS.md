# FightForge First-Run Runbooks
## Tasks 6, 7, 8 — Requires Your Credentials

These three tasks require your DataForSEO credentials and Wayne's
StackEngine Circle access. Each is a 15–30 minute session once you
have the prerequisites ready.

---

## TASK 6: First JMAA SearchScope Run
**Time required:** ~30 minutes
**Prerequisites:** DataForSEO account + SearchScope files from Wayne

### Step 1: Confirm Prerequisites
- [ ] SearchScope files downloaded from Wayne's Circle community
- [ ] DataForSEO username and password ready
- [ ] Airtable account ready (free tier works)

### Step 2: Copy Airtable Base
1. Get the StackEngine SearchScope master base link from Wayne
2. In Airtable: click **Copy base**
3. Name it: `SearchScope — James Martial Arts Academy`
4. Go to the base URL and copy the base ID: `airtable.com/app[BASE_ID]/...`

### Step 3: Configure SearchScope
Open `searchscope-se-community-v1-030626/dev/config/searchscope.json`:
```json
{
  "airtable_base_id": "app[YOUR_BASE_ID_HERE]",
  "location": "United States",
  "language_code": "en",
  "keyword_limit_per_endpoint": 100,
  "serp_sample_size": 5,
  "llm_response_sample_size": 3
}
```

### Step 4: Configure MCP Servers
In Claude Desktop settings (or `.claude/settings.local.json`):
```json
{
  "mcpServers": {
    "airtable": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-airtable"],
      "env": { "AIRTABLE_API_KEY": "pat_YOUR_KEY" }
    },
    "dfs-mcp": {
      "command": "npx",
      "args": ["-y", "dataforseo-mcp"],
      "env": {
        "DATAFORSEO_USERNAME": "your@email.com",
        "DATAFORSEO_PASSWORD": "your-password"
      }
    }
  }
}
```

### Step 5: Open Claude Code in SearchScope Directory
```bash
cd searchscope-se-community-v1-030626/dev
claude
```

### Step 6: Run Brand Analysis
```
/brand https://jamesmartialartsacademy.com
```
SearchScope will analyze the JMAA website and present a brand profile.
Review it carefully — confirm or correct before proceeding.
Expected output:
- Summary: Kajukenbo and Kosho-Ryu martial arts school in El Cajon
- Audience: Families with children ages 3–17, adults
- Key Themes: Discipline, confidence, self-defense, belt progression
- Positioning: Traditional martial arts, 36+ years experience, Hall of Fame

### Step 7: Run Initial Keyword Analysis
```
/run kajukenbo el cajon
```
This will take 10–20 minutes and cost approximately $5–10 in DataForSEO.
SearchScope will cluster all keywords and write scored recommendations to Airtable.

### Step 8: Review Output
Open your Airtable base → Assessments table → read the latest record.
Share the Airtable base ID with FightForge by adding to JMAA client-config.json:
```json
"searchscope_airtable_base": "app[BASE_ID]"
```

### Expected Results
- 5–10 keyword clusters identified
- Each cluster scored 1–10 with written reasoning
- Top opportunities: "karate el cajon" cluster, "kajukenbo classes" cluster,
  "kids martial arts el cajon" cluster
- Content calendar ready to hand to SEO Analyst Agent

---

## TASK 7: First JMAA CitationScope Baseline Run
**Time required:** ~30 minutes
**Prerequisites:** DataForSEO (same as Task 6) + CitationScope Dev.zip from Wayne

### Step 1: Extract CitationScope
```bash
unzip CitationScope.zip
unzip CitationScope/Dev.zip -d citationscope-dev
cd citationscope-dev/Dev
```

### Step 2: Copy Airtable Base
1. Get the StackEngine CitationScope master base from Wayne
2. Copy base → name: `CitationScope — James Martial Arts Academy`
3. Note the base ID

### Step 3: Configure citationscope.json
```json
{
  "airtable_base_id": "app[YOUR_BASE_ID_HERE]",
  "location": "United States",
  "language_code": "en",
  "prompts_per_topic": 8,
  "platforms": ["chat_gpt", "perplexity", "claude", "gemini"],
  "batch_size": 5,
  "cost_per_query": 0.05,
  "scheduled_run_day": "monday"
}
```

### Step 4: Open Claude Code in CitationScope Directory
```bash
claude
```

### Step 5: Brand Analysis
```
/brand https://jamesmartialartsacademy.com
```
Confirm the brand profile. CitationScope will then suggest topics.

### Step 6: Confirm the 10 Standard JMAA Topics
Accept or adjust these suggested topics:
1. karate school el cajon
2. best karate classes el cajon
3. karate for kids el cajon
4. adult karate classes el cajon
5. kajukenbo school el cajon
6. self-defense classes el cajon
7. martial arts for kids el cajon
8. james martial arts academy
9. martial arts instructor el cajon
10. martial arts school el cajon

### Step 7: Run Baseline
```
/run
```
**Estimated cost:** ~$16 (10 topics × 8 prompts × 4 platforms × $0.05)
**Estimated time:** 20–30 minutes

This establishes JMAA's baseline AI visibility score.
The baseline is the starting point — all future weekly runs are measured against it.

### Step 8: Record Baseline Scores
After run completes, open Airtable → Topics table.
Record these numbers — this is your Week 0 benchmark:

| Topic | Visibility Score | ChatGPT | Gemini | Perplexity | Claude |
|---|---|---|---|---|---|
| karate school el cajon | | | | | |
| kajukenbo school el cajon | | | | | |
| [etc.] | | | | | |

Most schools start at 0–15% visibility on primary topics.
Target: 40%+ within 6 months of running FightForge.

### Step 9: Connect to FightForge
Add to JMAA client-config.json:
```json
"citationscope_airtable_base": "app[BASE_ID]"
```

---

## TASK 8: Airtable Master Base Setup
**Time required:** ~20 minutes
**Prerequisites:** Airtable account + access to Wayne's StackEngine Circle

### What You Need from Wayne

From the StackEngine Circle community, you need:
1. **SearchScope master base** — link to copy the base
2. **CitationScope master base** — link to copy the base

Both should be in the Circle community resources. If you can't find them,
message Wayne directly: wayne@wergle.com

### Per-Client Setup (Repeat for Every New Client)

For each new school you onboard, create two Airtable bases:

**Base 1: SearchScope**
- Copy the StackEngine SearchScope master base
- Name: `SearchScope — [Client School Name]`
- Share with: Your DataForSEO MCP connection

**Base 2: CitationScope**
- Copy the StackEngine CitationScope master base
- Name: `CitationScope — [Client School Name]`
- Share with: Your DataForSEO MCP connection

**Base 3: FightForge Operations** (one base total — not per client)
Create manually with these tables:

| Table | Purpose |
|---|---|
| Clients | Client registry — name, config, status, agent assignments |
| Content Calendar | All content tickets across all clients |
| Agent Task Queue | Open tasks per agent per client |
| KPI Dashboard | Weekly metrics for all clients |
| Deployment Tracker | 48-hour deployment checklist per client |

This is the master Karate Loco operations base that the CEO, CMO, and COO
agents read from on every heartbeat.

### Airtable Workspace Structure

```
Karate Loco Airtable Workspace
├── FightForge Operations (master ops base)
├── SearchScope — JMAA
├── CitationScope — JMAA
├── SearchScope — [Client 1]
├── CitationScope — [Client 1]
└── [repeat per client]
```

### API Key Setup

1. Go to airtable.com → Account → Developer Hub → Personal Access Tokens
2. Create token with scopes: `data.records:read`, `data.records:write`,
   `schema.bases:read`
3. Add to your FightForge `.env`:
   ```
   AIRTABLE_API_KEY=pat_YOUR_TOKEN_HERE
   ```
4. Add to SearchScope and CitationScope MCP configs (see Task 6 setup)

### Verification

After setup, confirm the FightForge SEO Analyst Agent can read from
the SearchScope base by running:
```
airtable list tables app[BASE_ID]
```
You should see: Brand Profiles, Topics, Keywords, Clusters, Assessments

If the Citation Agent and AEO/GEO Agent can both access their respective
bases, your Airtable layer is fully operational.
