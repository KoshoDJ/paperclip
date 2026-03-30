# ⚔️ FightForge

**AI-powered operating system for combat sports businesses.**

FightForge is a domain-specialized fork of [FightForge](https://github.com/fightforgeai/fightforge) — the open-source AI agent orchestration platform. It is purpose-built for martial arts academies, MMA gyms, boxing clubs, and self-defense studios.

Built by **Darryl James** — Sigung, 6th-Degree Black Belt in Kajukenbo, founder of [James Martial Arts Academy](https://jamesmartialartsacademy.com) and [Karate Loco](https://karateloco.com) martial arts marketing agency.

---

## What FightForge Does

FightForge runs a 10-agent AI workforce that handles the full marketing and operations lifecycle of a combat sports school:

```
Student finds school (SEO + AI search)
    → Books trial class (conversion engine)
        → Enrolls (CRM automation)
            → Stays and advances (retention system)
                → Refers others (referral engine)
```

All of this runs autonomously, with the school owner operating as the board — approving strategy, reviewing deliverables, and teaching.

---

## The 10-Agent Workforce

| Agent | Role | Heartbeat |
|---|---|---|
| **CEO** | Strategy, delegation, board reporting | Every 24h |
| **CMO** | Agency pipeline, outreach, case studies | Every 12h |
| **COO** | Client delivery, project routing | Every 12h |
| **SEO Analyst** | SearchScope output → rank reports | Every 8h |
| **Content Writer** | HTML copy, blog posts, GBP content | Every 8h |
| **Core 30 / Audit** | GBP-to-website mapping audit | On ticket |
| **Schema & Tech** | JSON-LD @graph, GTM injection | On ticket |
| **UX/UI** | Design system, build briefs, QA | On ticket |
| **Citation** | NAP consistency, directory audits | Monthly |
| **AEO/GEO** | CitationScope AI visibility runs | Weekly |

---

## Tech Stack

| Layer | Tools |
|---|---|
| **Agent orchestration** | FightForge (this repo) |
| **CRM + automations** | GoHighLevel |
| **Websites** | Hand-coded HTML/CSS on AWS S3 + CloudFront |
| **Search intelligence** | SearchScope (StackEngine / Wayne Ergle) |
| **AI visibility** | CitationScope (StackEngine / Wayne Ergle) |
| **SEO data** | DataForSEO MCP |
| **Data layer** | Airtable |
| **AI models** | Claude Sonnet (Anthropic) |

---

## Strategic Frameworks

Every deliverable in FightForge applies four expert frameworks:

1. **Semantic Triple** (Bradley Benner / Semantic Mastery) — Entity authority architecture
2. **ThrillX CRO** (Arsh Sanwarwala) — Conversion page architecture
3. **Core 30** (Caleb Ulku) — GBP-to-website URL mapping
4. **StoryBrand** (Donald Miller) — Marketing copy narrative

---

## Supported Combat Sports

Karate · Kajukenbo · Kosho-Ryu · BJJ · MMA · Muay Thai · Boxing · Kickboxing · Wrestling · Judo · Kung Fu · Taekwondo · Self-Defense

---

## Quick Start

```bash
# Prerequisites: Node.js 20+, pnpm 9+, Anthropic API key

git clone https://github.com/KoshoDJ/fightforge.git
cd fightforge
cp .env.example .env        # Add your ANTHROPIC_API_KEY
pnpm install
pnpm fightforgeai run        # Launches at http://localhost:3100
```

See [doc/SETUP.md](doc/SETUP.md) for full setup guide including Tailscale mobile access.

---

## Repository Structure

```
fightforge/
├── agents/skills/          ← SKILL.md files for all 10 agents
├── claude_skills/          ← Mirrored skills for Claude Code sessions
├── company-templates/      ← Pre-built company configs (Karate Loco, JMAA, _template)
├── integrations/           ← SearchScope, CitationScope, GHL, DataForSEO setup guides
├── doc/                    ← Setup, deployment, and SOP documentation
└── [FightForge engine]      ← apps/, packages/, cli/ — inherited from upstream
```

---

## Company Templates

FightForge ships with two ready-to-use company configs:

- **`karate-loco/`** — Karate Loco agency (all 10 agents, full mission)
- **`jmaa/`** — James Martial Arts Academy (internal reference client)
- **`_template/`** — Blank template for new combat sports school clients

---

## Upstream

FightForge is a fork of [fightforgeai/fightforge](https://github.com/fightforgeai/fightforge) (MIT License).
The FightForge engine (apps/, packages/, cli/, docker/) is unchanged from upstream.
All FightForge additions live in `agents/skills/`, `claude_skills/`, `company-templates/`, `integrations/`, and `doc/`.

---

## License

FightForge additions: MIT  
FightForge engine: MIT (see upstream license)

---

*Built on the mat. Deployed from the cloud.*  
*Karate Loco · El Cajon, CA · 2026*
