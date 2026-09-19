# Prospect Research Workflow

Goal: 10–20 well-fit prospects/day, each with ONE concrete, observable problem
we can genuinely solve. No random spraying.

## Where to find prospects (all free)
- Instagram / TikTok / Facebook: search a niche + location
  (e.g. "Lagos thrift store", "Abuja small chops", "Enugu salon").
- Google Maps: search a category + area, open the listings.
- Google Search: "<business type> <city>" and see who has a bad/no website.
- Local directories, WhatsApp catalogs shared in status/groups.

## Qualify — a prospect needs a REAL reason to buy
Prioritize businesses showing at least one of these observable signs:
1. Active social presence (they care about their business online).
2. No website, or an outdated/broken/slow one.
3. Products/services that would suit a catalog.
4. Orders taken by DM (slow, messy, easy to lose).
5. WhatsApp contact but no easy way to browse/order.
6. Poor presentation (blurry photos, no prices, hard to contact).
7. Obvious repetitive manual work (hand-written receipts, manual follow-ups).

If you can't name a specific problem, it's not a prospect yet. Skip it.

## Capture (one row per prospect in the CRM)
For each, record — using only what you actually observed:
- business name, industry, location
- website (or "none"), social handles
- contact method (WhatsApp / IG DM / email / form)
- the ONE observable problem
- recommended offer (1–7)
- a personalized opening line based on that fact
- best contact channel
- follow-up date

Add with:
```
python3 sales/crm.py add \
  --name "Business Name" --industry restaurant --location "Lagos" \
  --website none --social "@handle" --contact whatsapp \
  --problem "Menu only in IG bio; customers DM to ask prices" \
  --offer "WhatsApp Ordering System" \
  --pitch "I noticed customers have to DM to see prices..." \
  --channel instagram
```

## Personalization engine — the rule
Never send "Hello sir/madam, I offer website services." Lead with ONE thing you
actually saw:

> "I noticed customers have to DM your page to ask which items are in stock. I
> put together a simple mobile catalog where they can browse everything and send
> the order straight to your WhatsApp — want me to show you a quick demo?"

Every personalized line must trace back to a real observation. If you didn't
see it, don't say it.

## Daily rhythm
1. Pick one niche + area for the day.
2. Find 10–20 that qualify.
3. Add each to the CRM with its problem + offer + opening line.
4. Hand the batch to review; approve messages; send manually.
5. Log CONTACTED + set follow-up dates.
