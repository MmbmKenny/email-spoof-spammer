# Service Architecture

How we turn a prospect into a delivered, paid project — and how the pieces in
this repo fit together.

## The seven productized offers

| # | Offer | Best for | Intro price (₦) | Typical delivery |
|---|-------|----------|-----------------|------------------|
| 1 | Business Website | Any business with no/weak site | 30,000+ | 3–5 days |
| 2 | Online Product Catalog | Sellers of physical products | 20,000–50,000+ | 3–5 days |
| 3 | WhatsApp Ordering System | Instagram/TikTok sellers taking DMs | 30,000–75,000+ | 4–7 days |
| 4 | Digital Receipt / Invoice System | Hotels, salons, shops, services | 20,000–50,000+ | 2–4 days |
| 5 | Social Media Content Package | Businesses with weak/inconsistent posting | 15,000–30,000+ | 2–3 days |
| 6 | Product Ad Creative | Ecommerce sellers running/wanting ads | 10,000–25,000+ | 1–2 days |
| 7 | Business Automation | Businesses with obvious repetitive manual work | Quote by complexity | Varies |

Full one-pagers for each are in `docs/offers/`.

## Production engine

We use Claude Code internally to compress production time. The client buys an
**outcome** (more customers, more orders, less manual work, a professional
presence), not a toolchain. We never over-promise a fixed price when scope is
genuinely unclear — we quote honestly.

## Repository map

```
docs/
  service-architecture.md   <- this file
  tool-stack.md             <- what we use and what it costs
  14-day-plan.md            <- the launch playbook
  sales-funnel.md           <- stage definitions
  prospect-research-workflow.md
  offers/                   <- one client-facing page per offer
  outreach/                 <- message templates + objection handling
sales/
  crm.py                    <- CRM CLI (SQLite-backed, real data only)
  dashboard.py              <- renders sales-dashboard.html from real data
  leads/
    schema.md               <- lead record fields
    leads.csv               <- CSV mirror (header only until real leads added)
    crm.db                  <- SQLite database (created on first use)
demos/
  index.html                <- demo gallery (all clearly labelled DEMO)
  restaurant/  hotel/  catalog/  invoice-generator/  whatsapp-ordering/
landing/
  index.html                <- the agency landing page
```

## Delivery pipeline (per client)

1. **Research** — confirm the genuine problem (`prospect-research-workflow.md`).
2. **Outreach** — personalized message, human-approved before sending.
3. **Discovery** — short call/chat, gather requirements.
4. **Proposal + quote** — scoped to the real work.
5. **Deposit** — take a deposit before building (protects both sides).
6. **Build** — Claude Code-assisted production against a checklist.
7. **Review** — client feedback, one revision round included by default.
8. **Deliver + deploy** — hand over, deploy to free hosting.
9. **Record** — mark PAID/COMPLETED in the CRM, capture what worked.
10. **Referral / retAiner** — ask for an introduction; offer ongoing care.

## Honesty guardrails (non-negotiable)

- No fake leads, testimonials, reviews, case studies, results, or stats.
- Demos are labelled DEMO and use fictional businesses — never presented as real clients.
- Outreach is never marked "sent" unless it actually was.
- An integration is "working" only after a real, verified use.
- No guaranteed-ROI or guaranteed-sales claims.
