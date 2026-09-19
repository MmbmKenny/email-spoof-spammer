# Digital Services Agency — Client Acquisition System

A practical, zero-capital system for landing the first paying clients of a small
digital-services business (websites, catalogs, WhatsApp ordering, receipts,
content, automation).

Built to be **honest by design**: no fake leads, testimonials, reviews, case
studies, or stats; no spam; no unsolicited mass messaging; and **human approval
before any outreach is sent**.

## What's here

| Path | What it is |
|------|------------|
| `landing/index.html` | The agency landing page (fill in your contact details) |
| `demos/` | Live demo builds — your portfolio proof (all labelled DEMO) |
| `sales/crm.py` | SQLite-backed CRM CLI — track prospects with real data only |
| `sales/dashboard.py` | Generates a sales dashboard from real CRM data |
| `docs/offers/` | Client-facing one-pager per service |
| `docs/outreach/` | Personalized message templates + objection handling |
| `docs/14-day-plan.md` | The launch playbook |
| `docs/prospect-research-workflow.md` | How to find & qualify 10–20 prospects/day |
| `docs/sales-funnel.md` | CRM stage definitions |
| `docs/tool-stack.md` | Every tool we use and what it costs (currently ₦0/mo) |
| `docs/service-architecture.md` | How the pieces fit together |

## Quick start

```bash
# 1. Look at your demos (open in a browser)
open demos/index.html          # or just double-click the file

# 2. Fill in your real contact details on the landing page
#    (search landing/index.html for [YOUR_ )

# 3. Add your first researched prospect
python3 sales/crm.py add --name "Business Name" --industry restaurant \
  --location "Lagos" --website none --social "@handle" --contact whatsapp \
  --problem "Customers DM to ask prices" --offer "WhatsApp Ordering System" \
  --pitch "I noticed customers have to DM to see prices..." --channel instagram

# 4. See your pipeline and generate the dashboard
python3 sales/crm.py stats
python3 sales/dashboard.py     # writes sales/sales-dashboard.html

# 5. Follow the plan
open docs/14-day-plan.md
```

Deploy `landing/` and `demos/` free on GitHub Pages or Netlify.

## The rules (non-negotiable)

- Real data only. Nothing is marked "sent" or "paid" unless it truly happened.
- Outreach is personalized from a **real observation** and **you approve every
  message** before it goes out.
- Three touches max (Day 1 / 3 / 7), then stop. Stop immediately if asked.
- Honest quotes. We don't underquote complex work just to close.
- No guaranteed-ROI or guaranteed-sales claims.

## Note on this repository's history

This repo was previously an "email spoof spammer". That has nothing to do with —
and directly contradicts — this legitimate, consent-based business. The old
`main.py` spam script should be removed. See the launch notes / ask your
operator before deleting if you want to keep the git history reference.
