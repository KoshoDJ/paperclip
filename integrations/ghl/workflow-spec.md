# FightForge GHL Snapshot — Complete Workflow Specification
## Version 1.0 | Karate Loco Agency

This document specifies all 10 GoHighLevel automation workflows
included in the FightForge GHL Snapshot. Use this to build the
snapshot from scratch in GHL, or to verify an installed snapshot
is correctly configured per client.

GHL is used for: CRM, calendar embeds, automations ONLY.
GHL never hosts client websites.

---

## Custom Fields (Create These First)

Before building workflows, create these custom contact fields in GHL:

| Field Name | Type | Values |
|---|---|---|
| Program Interest | Dropdown | Preschool, Kids, Preteen, Teen, Adult, Women's Self-Defense, General |
| Child Name | Text | — |
| Child Age | Number | — |
| How Did You Hear | Dropdown | Google, Facebook, Instagram, Referral, Drive By, Other |
| Trial Class Date | Date | — |
| Belt Rank | Dropdown | White, Yellow, Orange, Green, Blue, Purple, Brown, Red, Black |
| Enrollment Date | Date | — |
| Membership Type | Dropdown | Monthly, Annual, Family, Trial |

---

## Custom Values (School-Specific — Set Per Client)

| Key | Example Value |
|---|---|
| school.name | James Martial Arts Academy |
| school.instructor | Sigung James |
| school.phone | (833) 894-0191 |
| school.address | 2356 Fletcher Pkwy, El Cajon, CA 92020 |
| school.website | https://jamesmartialartsacademy.com |
| school.review_link | [Direct GBP review URL] |
| school.trial_offer | Free Trial Class |

---

## Tags Used Across All Workflows

Create these tags before building workflows:

`New Lead` · `Trial Booked` · `Trial Attended` · `Trial No-Show`
`Enrolled` · `Active Member` · `Annual Member` · `Family Plan`
`Dormant Lead` · `Cold Lead Post Trial` · `No-Show Unresponsive`
`Belt Test Eligible` · `Referral Requested` · `Review Requested`
`At Risk` · `Win Back`

---

## WORKFLOW 1: Speed-to-Lead
**Trigger:** Contact created (any source — form, calendar, inbound call, social DM)
**Goal:** First contact within 60 seconds, 24/7

```
TRIGGER: Contact Created

ACTION 1: Add Tag → "New Lead"

ACTION 2: Wait — 0 minutes (immediate)
SEND SMS:
  "Hi {{contact.first_name}}! This is {{school.instructor}} at
  {{school.name}} — thanks for reaching out about our
  {{contact.program_interest}} program! We'd love to set up a FREE
  trial class for {{contact.child_name | default: 'you'}}. Are you
  available [Day Option 1] or [Day Option 2] this week? Just reply
  and I'll get you set up! 🥋"

IF: Contact does not reply within 2 hours →

ACTION 3: Wait — 2 hours
SEND SMS:
  "Hey {{contact.first_name}} — just making sure you got my message!
  We have a few spots open this week for a free trial. No commitment,
  just come see if it's a good fit. Reply YES and I'll hold a spot!"

IF: Contact does not book within 24 hours →

ACTION 4: Wait — 24 hours from trigger
SEND EMAIL:
  Subject: "Your free {{school.trial_offer}} is waiting — {{school.name}}"
  Body: [Program overview email — include photos, instructor bio,
         testimonials, and booking link for relevant program calendar]

IF: Contact does not book within 48 hours →

ACTION 5: Wait — 48 hours from trigger
SEND SMS:
  "Hi {{contact.first_name}} — I know life gets busy! We're holding
  a spot for {{contact.child_name | default: 'you'}}. Most families
  tell us this was the best decision they made. Our link to book your
  free trial: {{school.website}}/contact"

ACTION 6: Wait — 5 days from trigger (no booking)
CREATE TASK:
  "Personal call to {{contact.first_name}} {{contact.last_name}}
  — inquired about {{contact.program_interest}}. Call today."
  Assigned to: [School Owner]
  Due: Today

IF: No booking after 7 days →
ACTION 7: Add Tag → "Dormant Lead"
  Remove from active follow-up
  Enter 30-day monthly nurture (see Workflow 10)

BOOKING DETECTED (any point):
  → Remove from this workflow
  → Enters Workflow 2: Trial Booked Confirmation
```

---

## WORKFLOW 2: Trial Booked Confirmation
**Trigger:** Appointment booked in any program calendar
**Goal:** 70–85% show rate through strategic reminders

```
TRIGGER: Appointment Status = Booked

ACTION 1: Add Tag → "Trial Booked"

ACTION 2: Wait — 0 minutes (immediate)
SEND SMS:
  "You're confirmed! 🥋 Trial class for
  {{contact.child_name | default: 'you'}} on
  {{appointment.start_time | date: '%A, %B %d at %I:%M %p'}}.
  {{school.name}} is at {{school.address}}.
  Wear comfortable clothes — we'll handle everything else.
  Questions? Just reply!"

ACTION 3: Wait — until 24 hours before appointment
SEND SMS:
  "Reminder: {{contact.child_name | default: 'Your'}}'s trial class
  is tomorrow at {{appointment.start_time | date: '%I:%M %p'}}!
  We're looking forward to meeting
  {{contact.child_name | default: 'you'}}.
  See you then — {{school.instructor}}"

ACTION 4: Wait — until 2 hours before appointment
SEND SMS:
  "Heading out soon! {{school.name}} is at {{school.address}}.
  Parking is [parking note]. 
  {{contact.child_name | default: 'You'}} is going to love it today 🥋"

ACTION 5: Wait — 1 hour after appointment start time
CHECK: Has "Trial Attended" tag been applied?

IF YES: Remove from workflow (attended — enters Workflow 3)

IF NO: → Enters Workflow 5: No-Show Recovery
  Add Tag → "Trial No-Show"
```

---

## WORKFLOW 3: Trial Attended — Enrollment Push
**Trigger:** Tag "Trial Attended" applied
**Goal:** 55–75% trial-to-enrollment conversion

```
TRIGGER: Tag Added = "Trial Attended"
  Remove tag: "Trial Booked", "Trial No-Show"

ACTION 1: Wait — 30 minutes
SEND SMS:
  "It was so great having
  {{contact.child_name | default: 'you'}} in class today —
  {{school.instructor}} was really impressed!
  We'd love to talk about getting
  {{contact.child_name | default: 'you'}} started.
  Can we schedule a quick 10-minute chat this week?"

ACTION 2: Wait — 24 hours
SEND EMAIL:
  Subject: "{{contact.child_name | default: contact.first_name}}'s
  next step at {{school.name}}"
  Body: [Full program overview email with:]
  - What they experienced in the trial class
  - Program schedule and belt progression
  - Pricing and membership options
  - 2–3 parent testimonials for their age group
  - Clear CTA: "Reserve {{contact.child_name | default: 'Your'}}'s Spot"
  - Link to booking calendar

ACTION 3: Wait — 48 hours
SEND SMS:
  "Hi {{contact.first_name}} — wanted to check in after
  {{contact.child_name | default: 'your'}}'s class!
  {{school.instructor}} thinks
  {{contact.child_name | default: 'you'}} would really excel.
  Do you have 10 minutes to chat today or tomorrow?"

ACTION 4: Wait — 72 hours
SEND SMS:
  "Hey {{contact.first_name}} — I want to make sure
  {{contact.child_name | default: 'you'}} gets the spot while
  we still have availability in our
  {{contact.program_interest}} class.
  Want me to hold a space? Just reply YES."

ACTION 5: Wait — 7 days
SEND EMAIL:
  Subject: "Still thinking about it? Here's what other parents told us..."
  Body: [Objection-crusher email addressing:]
  - "It's too expensive" → cost per class breakdown, ROI framing
  - "We're too busy" → flexible schedule, 2x/week commitment
  - "I'm not sure it's right for us" → free trial + no-contract option
  [Include 2 long-form testimonials from similar families]

ACTION 6: Wait — 14 days (still not enrolled)
  Add Tag → "Cold Lead Post Trial"
  Remove from this workflow
  → Enter monthly reactivation sequence (Workflow 10)
```

---

## WORKFLOW 4: Program Selection to Calendar Routing
**Trigger:** Form submission with "Program Interest" field populated
**Goal:** Route every lead to the exact right program calendar

```
TRIGGER: Form Submitted (any lead capture form)

BRANCH on "Program Interest" field:

IF "Preschool" OR child_age ≤ 5:
  SEND SMS with Preschool Martial Arts calendar booking link
  "For little ones ages 3–5, here's the link to schedule
  {{contact.child_name}}'s free trial:
  [Preschool Calendar Link]"

IF "Kids" OR child_age 6–9:
  SEND SMS with Kids Martial Arts calendar link

IF "Preteen" OR child_age 10–12:
  SEND SMS with Preteen Martial Arts calendar link

IF "Teen" OR child_age 13–17:
  SEND SMS with Teen Martial Arts calendar link

IF "Adult" OR adult=true AND interest ≠ self-defense:
  SEND SMS with Adult Martial Arts calendar link

IF "Women's Self-Defense" OR gender=female AND adult=true:
  SEND SMS with Women's Self-Defense calendar link

IF program_interest is empty OR "General":
  SEND SMS:
    "Quick question — how old is your child
    (or is this class for yourself)?
    Just reply with an age and I'll send you the right link!"
  → Wait for reply → Re-run routing logic on reply
```

---

## WORKFLOW 5: No-Show Recovery
**Trigger:** Tag "Trial No-Show" applied (from Workflow 2, Step 5)
**Goal:** Recover 25–40% of no-shows to rebook

```
TRIGGER: Tag Added = "Trial No-Show"

ACTION 1: Wait — 0 minutes (immediate)
SEND SMS:
  "Hi {{contact.first_name}} — we missed you and
  {{contact.child_name | default: 'you'}} today!
  Everything okay? We completely understand if something came up.
  We'd love to reschedule your free trial:
  {{school.website}}/contact"

ACTION 2: Wait — 24 hours
SEND EMAIL:
  Subject: "We saved a spot for you — reschedule your trial"
  Body: [Light-touch email with easy reschedule link + social proof]

ACTION 3: Wait — 48 hours
SEND SMS:
  "Hey {{contact.first_name}} — one more try before I release the spot.
  Reschedule your free trial here: {{school.website}}/contact
  No worries if timing isn't right — I'll reach back out next month."

ACTION 4: Wait — 5 days (no reschedule)
  Add Tag → "No-Show Unresponsive"
  Remove tag: "Trial No-Show"
  → Enter 30-day monthly reactivation (Workflow 10)
```

---

## WORKFLOW 6: Review Generation System
**Trigger:** Multiple trigger points (see branches)
**Goal:** 4+ new Google reviews per month, 4.9+ stars

```
BRANCH A — TRIGGER: Tag "Trial Attended" applied
  Wait — 7 days
  SEND SMS:
    "Hi {{contact.first_name}}! {{contact.child_name | default: 'You'}}
    has been doing great in class. If you've had a positive experience,
    would you mind leaving us a quick Google review?
    It helps other local families find us — takes under 2 minutes:
    {{school.review_link}}
    Thank you! — {{school.instructor}}"
  Add Tag → "Review Requested"

BRANCH B — TRIGGER: Tag "Enrolled" applied
  Wait — 30 days
  SEND EMAIL:
    Subject: "30 days in — how's everything going?"
    Body: [Check-in + review request with direct GBP link]

BRANCH C — TRIGGER: Tag "Belt Test Eligible" applied
  Wait — 24 hours after belt promotion
  SEND SMS:
    "Congratulations again on
    {{contact.child_name | default: 'your'}} new belt! 🎉
    We're so proud of
    {{contact.child_name | default: 'your'}} progress.
    If you have a moment, a quick Google review means so much:
    {{school.review_link}}"

BRANCH D — TRIGGER: Monthly on "Active Member" contacts
  Filter: Tag = "Active Member" AND Tag ≠ "Review Requested" (last 90 days)
  CREATE TASK:
    "Send personal review request to {{contact.first_name}}
    {{contact.last_name}} — they have been an engaged member.
    Call or text personally."
  Assigned to: [School Owner]
  Due: This week
```

---

## WORKFLOW 7: Active Member Retention — Milestone System
**Trigger:** Class count milestones (requires class attendance tracking)
**Goal:** < 8% monthly churn through emotional engagement

```
TRIGGER: Custom Field "Class Count" updated

BRANCH: Class Count = 10
  SEND SMS:
    "🎉 {{contact.child_name | default: contact.first_name}} just
    completed their 10th class at {{school.name}}! That's a real
    milestone — {{school.instructor}} noticed the improvement.
    Keep it up!"

BRANCH: Class Count = 25
  SEND SMS:
    "25 classes! 🥋 {{contact.child_name | default: contact.first_name}}
    is building something real. The dedication shows every time
    {{contact.child_name | default: 'you'}} steps on the mat."

BRANCH: Class Count = 50
  SEND SMS:
    "50 classes — that's incredible. {{contact.child_name | default:
    contact.first_name}} is in rare company. {{school.instructor}} has
    something special for {{contact.child_name | default: 'you'}}
    next class. 🏆"
  CREATE TASK: "Prepare 50-class recognition gift for
    {{contact.first_name}}'s next class"

TRIGGER: Membership anniversary (Enrollment Date = today's date, prior year)
  SEND SMS:
    "{{contact.first_name}} — it's been one year since
    {{contact.child_name | default: 'you'}} joined
    {{school.name}}. We are genuinely grateful.
    — {{school.instructor}}"
```

---

## WORKFLOW 8: At-Risk Member Win-Back
**Trigger:** 3 consecutive missed classes (requires attendance tracking)
**Goal:** Recover 30–40% of at-risk members before cancellation

```
TRIGGER: Custom Field "Consecutive Missed Classes" = 3

ACTION 1: Add Tag → "At Risk"

ACTION 2: CREATE TASK (immediate):
  "URGENT: {{contact.first_name}} {{contact.last_name}} has missed
  3 consecutive classes. Personal call required within 24 hours.
  Their program: {{contact.program_interest}}.
  Enrolled: {{contact.enrollment_date}}"
  Assigned to: [School Owner]
  Due: Today
  Priority: High

ACTION 3: Wait — 5 days (if no "At Risk" resolution)
SEND SMS:
  "Hi {{contact.first_name}} — we miss
  {{contact.child_name | default: 'you'}} on the mat!
  Is everything okay? {{school.instructor}} was asking about
  {{contact.child_name | default: 'you'}} this week.
  Is there anything we can help with?"

ACTION 4: Wait — 10 days total
SEND EMAIL:
  Subject: "We want to make sure everything's okay"
  Body: [Personal, warm check-in from instructor. Offer to:
  - Temporarily pause membership
  - Switch class time
  - Schedule a one-on-one catch-up class]

ACTION 5: Wait — 21 days (still at-risk)
  Add Tag → "Win Back"
  CREATE TASK: "Final win-back call for {{contact.first_name}}.
    Offer 1 free make-up class + special re-enrollment rate."
```

---

## WORKFLOW 9: Ascension — Annual Membership Upsell
**Trigger:** 6 months of active membership
**Goal:** Convert monthly → annual at 15% savings

```
TRIGGER: Enrollment Date = 6 months ago (monthly check)
  Filter: Membership Type = "Monthly" AND Tag = "Active Member"

ACTION 1: Wait — 0 (send on trigger date)
SEND EMAIL:
  Subject: "{{contact.first_name}} — a special offer for loyal members"
  Body:
    "You've been training with us for 6 months — and the progress
    {{contact.child_name | default: 'you'}} has made is real.

    As a thank-you, we'd like to offer you our Annual Membership:
    • Save 15% vs. monthly (that's $[X] back in your pocket)
    • Lock in your current rate for 12 months
    • Priority belt test scheduling

    Offer is good through [date 2 weeks out].
    Reply YES or call us at {{school.phone}} to lock it in."

ACTION 2: Wait — 7 days (no response)
SEND SMS:
  "Hi {{contact.first_name}} — did you get the email about our
  Annual Membership? Saves you $[X] over the year.
  Offer ends [date]. Want me to set it up?"

ACTION 3: Wait — 14 days (no response)
  Add Tag → "Annual Upsell Attempted"
  Remove from this workflow
  → Retry at 12-month anniversary
```

---

## WORKFLOW 10: Long-Term Nurture (Dormant + Post-Trial)
**Trigger:** Tag "Dormant Lead" or "Cold Lead Post Trial" or "No-Show Unresponsive"
**Goal:** Keep Karate Loco top-of-mind for 6 months — reactivate when timing is right

```
TRIGGER: Any of the above tags applied

MONTH 1 (30 days after tag):
  SEND SMS:
    "Hi {{contact.first_name}} — {{school.instructor}} here from
    {{school.name}}. Just checking in — is {{contact.child_name |
    default: 'the timing'}} better for getting started this month?
    We'd love to have you."

MONTH 2 (60 days):
  SEND EMAIL:
    Subject: "What's new at {{school.name}}"
    Body: [School update — recent belt promotions, upcoming events,
           a student success story. Soft CTA to book trial.]

MONTH 3 (90 days):
  SEND SMS:
    "{{contact.first_name}} — we have a new class time opening up
    that might work better for your schedule. Still interested in
    {{contact.program_interest}}?
    Here's our updated schedule: {{school.website}}/contact"

MONTH 4 (120 days):
  SEND EMAIL:
    Subject: "A message from {{school.instructor}}"
    Body: [Personal note from instructor — transformation story,
           community update, no hard sell]

MONTH 5 (150 days):
  SEND SMS:
    "Last check-in from us, {{contact.first_name}} — we're always
    here when the timing is right. Our door is always open.
    — {{school.instructor}}"

MONTH 6 (180 days):
  Add Tag → "Long-Term Dormant"
  Remove from active automation
  [Lead stays in database — can be reactivated by future campaign]
```

---

## Snapshot Export Checklist

Before exporting the snapshot for new client installs:

- [ ] All 10 workflows are active and tested
- [ ] All 6 program calendars are configured
- [ ] All Custom Fields are created
- [ ] All Custom Values are templated (not hardcoded to JMAA)
- [ ] All SMS/email copy uses `{{custom_values.*}}` variables
- [ ] Review link uses `{{school.review_link}}` variable
- [ ] All workflows tested in GHL test mode (no real SMS sent)
- [ ] Snapshot exported and named: "FightForge — Combat Sports v1.0"

---

## Post-Install Per-Client Configuration

After installing snapshot on a new client subaccount:

1. Update all Custom Values with client-specific data
2. Set calendar availability for all 6 programs
3. Get iFrame embed codes for all 6 calendars
4. Pass embed codes to UX/UI Agent for site installation
5. Connect GHL → Google for direct review link integration
6. Test Workflow 1 with a test contact
7. Confirm COO Agent webhook integration
