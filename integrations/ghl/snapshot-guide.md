# GoHighLevel Snapshot Installation
## FightForge Client Onboarding SOP-002

GHL is used exclusively for: CRM, calendar embeds, and automations.
GHL never hosts client websites. All websites are HTML/CSS on AWS S3 + CloudFront.

---

## What the FightForge GHL Snapshot Contains

The Karate Loco GHL snapshot includes:

**Pipelines:**
- Student Acquisition Pipeline
  (Inquiry → Trial Booked → Trial Attended → Offer Made → Enrolled → Active Member → Renewal → Lapsed)

**Calendars (6 — one per program):**
- Preschool Martial Arts (ages 3–5)
- Kids Martial Arts (ages 6–9)
- Preteen Martial Arts (ages 10–12)
- Teen Martial Arts (ages 13–17)
- Adult Martial Arts (ages 17+)
- Women's Self-Defense (ages 17+)

**Workflows (10):**
1. Speed-to-Lead (new lead → 60-second SMS)
2. Trial Booked Confirmation (confirmation + reminders)
3. Trial Attended → Enrollment Push
4. Program Selection → Calendar Routing
5. No-Show Recovery
6. Review Generation
7. Active Member Retention (milestone touchpoints)
8. At-Risk Member Win-Back
9. Annual Membership Upsell
10. Referral Request (90-day and 6-month triggers)

**Custom Fields:**
- Program Interest, Child Age, Child Name, How Did You Hear

**Tags:**
- New Lead, Trial Booked, Trial Attended, Enrolled, Active Member,
  Dormant Lead, Cold Lead Post Trial, No-Show Unresponsive

---

## Installation Steps

### Step 1: Access the Client's GHL Account
- Either create a new GHL subaccount under the Karate Loco agency account
- Or get manager access to the client's existing GHL account

### Step 2: Install the Snapshot
1. In GHL Agency Dashboard → Snapshots
2. Find "FightForge — Combat Sports School v1.0"
3. Click **Load Snapshot** → select client subaccount
4. Wait for install (2–5 minutes)

### Step 3: Customize Per-Client Variables
Update these in GHL after snapshot install:

| Field | Location | Value |
|---|---|---|
| Business Name | Settings → Business Profile | {{SCHOOL_NAME}} |
| Phone | Settings → Business Profile | {{PHONE}} |
| Address | Settings → Business Profile | {{ADDRESS_FULL}} |
| Time zone | Settings → Business Profile | America/Los_Angeles |
| Instructor name | Custom Values | {{INSTRUCTOR_FIRST}} |
| Trial class offer | Custom Values | "Free Trial Class" or client's offer |

### Step 4: Configure Calendar Availability
For each of the 6 program calendars:
- Set correct class days and times (from onboarding questionnaire)
- Set buffer time between appointments (15 min recommended)
- Set maximum advance booking window (30 days)
- Connect to school owner's calendar for conflict blocking

### Step 5: Get iFrame Embed Codes
For each calendar, go to Calendar → Settings → Get Embed Code.
Pass the 6 embed codes to the UX/UI Agent for installation on:
- Corresponding program page (primary placement)
- Contact page (all programs listed)

### Step 6: Test All Workflows
Use GHL's workflow testing mode to verify:
- [ ] New form fill → Speed-to-Lead SMS fires within 60 seconds
- [ ] Calendar booking → Confirmation SMS fires immediately
- [ ] "Trial Attended" tag → Enrollment push SMS fires correctly
- [ ] No-Show trigger → Recovery SMS fires 1 hour after appointment time

### Step 7: Connect Review Request Webhook to GBP
In GHL → Settings → Integrations → Google → Connect
This enables direct GBP review link in automated SMS/email messages.

---

## Calendar iFrame Placement Rules

| Page | Calendar(s) Embedded |
|---|---|
| `/programs/preschool-martial-arts/` | Preschool calendar only |
| `/programs/kids-martial-arts/` | Kids calendar only |
| `/programs/preteen-martial-arts/` | Preteen calendar only |
| `/programs/teen-martial-arts/` | Teen calendar only |
| `/programs/adult-martial-arts/` | Adult calendar only |
| `/programs/womens-self-defense/` | Women's Self-Defense calendar only |
| `/contact/` | All 6 calendars (tabbed by program) |
| Homepage | Single "Book a Free Trial" CTA → routes to contact page |

**Never embed GHL calendar on:** city guide pages, blog posts, About page.

---

## Snapshot Version History

| Version | Date | Changes |
|---|---|---|
| v1.0 | March 2026 | Initial FightForge release — 10 workflows, 6 calendars |
