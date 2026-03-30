# FightForge Setup Guide

Complete setup from zero to running. Estimated time: 2–3 hours.

---

## Prerequisites

| Requirement | Version | Check |
|---|---|---|
| Node.js | 20+ | `node --version` |
| pnpm | 9+ | `pnpm --version` |
| Git | Any | `git --version` |
| Anthropic API key | — | console.anthropic.com |
| DataForSEO account | — | dataforseo.com |
| Airtable account | — | airtable.com |
| Tailscale (optional) | — | tailscale.com (for mobile access) |

---

## Step 1: Clone and Install

```bash
git clone https://github.com/KoshoDJ/fightforge.git
cd fightforge
pnpm install
```

---

## Step 2: Configure Environment

```bash
cp .env.example .env
```

Open `.env` and add at minimum:
- `ANTHROPIC_API_KEY` — required for all agents
- `DATAFORSEO_USERNAME` + `DATAFORSEO_PASSWORD` — required for SearchScope and CitationScope
- `AIRTABLE_API_KEY` — required for data layer

---

## Step 3: First Launch

```bash
pnpm fightforgeai run
```

This auto-onboards, runs health checks, and starts the server.
Open `http://localhost:3100` in your browser.

---

## Step 4: Create Your Companies

In the FightForge dashboard:

### Company 1: Karate Loco (Agency)
- Name: `Karate Loco`
- Paste mission from `company-templates/karate-loco/company.json`
- Type: Agency

### Company 2: JMAA (Internal Client)
- Name: `James Martial Arts Academy`
- Mission: "Be the #1 martial arts school in East County San Diego"
- Type: Client

---

## Step 5: Hire Your Agents

For each company, hire agents in this exact order:

**Karate Loco (all 10):**
1. CEO — heartbeat 24h, budget $60
2. CMO — heartbeat 12h, budget $40
3. COO — heartbeat 12h, budget $30
4. SEO Analyst — heartbeat 8h, budget $50
5. Content Writer — heartbeat 8h, budget $40
6. Core 30 / Audit — on ticket, budget $35
7. Schema & Tech — on ticket, budget $35
8. UX/UI — on ticket, budget $40
9. Citation — heartbeat monthly, budget $30
10. AEO/GEO — heartbeat weekly, budget $40

**JMAA (6 specialists only):**
SEO Analyst, Content Writer, Schema & Tech, UX/UI, Citation, AEO/GEO

When hiring each agent, paste the contents of the corresponding
`.agents/skills/[agent-name]/SKILL.md` as the agent's system prompt.

---

## Step 6: Configure Integrations

Follow the setup guides in order:

1. `integrations/searchscope/setup.md` — per client, one Airtable base each
2. `integrations/citationscope/setup.md` — per client, one Airtable base each
3. `integrations/ghl/snapshot-guide.md` — per client, one GHL subaccount each
4. `integrations/dataforseo/setup.md` — shared credentials across all clients

---

## Step 7: Mobile Access (Optional but Recommended)

Run from the mat. Approve deliverables between classes.

```bash
# Install Tailscale on your Mac: https://tailscale.com/download
# Install Tailscale on your iPhone: App Store

# Start FightForge with Tailscale auth
pnpm dev --tailscale-auth

# Allow your phone
pnpm fightforgeai allowed-hostname your-iphone-name
```

Access FightForge from your phone at `http://[tailscale-ip]:3100`

---

## Step 8: Your First Client Run

With JMAA configured:

1. Create a ticket for the **Core 30 / Audit Agent**: "Run initial GBP audit for JMAA"
2. After audit completes, create a ticket for **UX/UI Agent**: "Generate design system brief for JMAA"
3. Run SearchScope for JMAA: open Claude Code in SearchScope dir, `/brand https://jamesmartialartsacademy.com`, then `/run kajukenbo el cajon`
4. Run CitationScope for JMAA baseline: open Claude Code in CitationScope dir, `/brand`, then `/run`
5. Review all outputs as board — approve or redirect

---

## Keeping FightForge Updated

FightForge is a fork of `fightforgeai/fightforge`. To pull upstream engine updates:

```bash
git remote add upstream https://github.com/fightforgeai/fightforge.git
git fetch upstream
git merge upstream/master
# Resolve any conflicts in apps/, packages/, cli/
# Your files in agents/, claude_skills/, company-templates/, integrations/ are never touched
git push origin master
```

Your FightForge-specific files will never conflict with upstream engine changes.

---

## Troubleshooting

**Server won't start:**
```bash
pnpm fightforgeai doctor    # Runs health checks with auto-repair
```

**Database issues:**
```bash
# Reset to clean state (WARNING: deletes all data)
FIGHTFORGE_HOME=~/.fightforge pnpm fightforgeai db:reset
```

**Agent not responding:**
Check that the agent's system prompt contains the full SKILL.md content.
In the FightForge dashboard: Agent → Edit → System Prompt.

**Costs running high:**
Check the Run records in each client's Airtable base.
Flag any run over $25 to the board before the next cycle.
