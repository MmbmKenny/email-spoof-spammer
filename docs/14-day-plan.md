# 14-Day Client Acquisition Plan

Zero capital. Direct outreach. The goal of these two weeks is **your first
paying client**, with the system in place to keep getting more.

Daily prospect target: **10–20 highly relevant, well-researched prospects** —
not 500 spam messages. Quality of fit and personalization beats volume.

## Week 1 — Build proof, then start reaching out

### Day 1 — Foundation (mostly done in this repo)
- [ ] Review the demos in `demos/` — they are your portfolio proof.
- [ ] Fill in your real contact details in `landing/index.html` and templates
      (WhatsApp number, email). Search for `[YOUR_` placeholders.
- [ ] Deploy `landing/` and `demos/` to free hosting (GitHub Pages / Netlify).
- [ ] Read `docs/outreach/` templates and make them sound like *you*.

### Day 2 — First research batch
- [ ] Research 10–15 local businesses (`prospect-research-workflow.md`).
- [ ] Add each to the CRM: `python3 sales/crm.py add ...`
- [ ] For each, record the ONE concrete, observable problem you'd fix.

### Day 3 — First outreach
- [ ] Generate a personalized message per prospect (based on real observations).
- [ ] **You approve each message before it's sent.**
- [ ] Send manually via the best channel. Mark CONTACTED with the date.
- [ ] Set Day-3-later and Day-7 follow-up reminders.

### Day 4 — Research + respond
- [ ] Research 10–15 more prospects.
- [ ] Reply promptly to anyone who responded. Move REPLIED → INTERESTED as fit.

### Day 5 — Outreach batch 2
- [ ] Personalized outreach to Day-4 prospects (approved first).
- [ ] Send Day-3 follow-ups to Day-2 batch who didn't reply.

### Day 6 — Demos & discovery
- [ ] For anyone INTERESTED, share the most relevant demo link.
- [ ] Book a short discovery chat. Use `docs/outreach/discovery-questions.md`.

### Day 7 — Review week 1
- [ ] Run `python3 sales/dashboard.py` and read the real numbers.
- [ ] Note which industry/offer/message got replies. Adjust. Send Day-7 follow-ups.

## Week 2 — Convert

### Day 8 — Research + proposals
- [ ] Research 10–15 more. Send proposals to anyone at DEMO/QUOTE stage.
- [ ] Quote honestly against the real scope. Take a deposit before building.

### Day 9 — Outreach + objections
- [ ] New outreach batch. Handle objections with `docs/outreach/objections.md`.

### Day 10 — Deliver first build
- [ ] Once a deposit lands, build with Claude Code against the offer checklist.
- [ ] Keep the client updated. Under-promise, over-deliver on timeline.

### Day 11 — Research + follow-ups
- [ ] Keep the top of the funnel full. Chase warm leads, not cold ghosts.

### Day 12 — Deliver + deploy
- [ ] Deliver the first project. Deploy. Walk the client through it.
- [ ] Mark PAID → DELIVERING → COMPLETED in the CRM as it progresses.

### Day 13 — Referral + retainer
- [ ] Ask your first happy client for one introduction.
- [ ] Offer a small monthly care/retainer where it genuinely helps them.

### Day 14 — Review & systematize
- [ ] Full dashboard review. What closed? What stalled? Why?
- [ ] Update templates and offers based on **real** feedback (never invented).
- [ ] Set week-3 targets.

## Weekly learning loop (every Sunday)
- Which industries respond? Which offer gets attention? Which message gets replies?
- Which objections recur? Which service closes? Which takes too long to deliver?
- Feed answers back into offers, templates, and targeting. Only real data.

## Reality checks
- Some weeks the first client takes longer than 14 days. That's normal — keep
  the funnel full and the follow-ups consistent.
- Never harass. Three touches (Day 1 / 3 / 7), then stop unless they re-engage.
- Stop immediately if someone asks not to be contacted.
