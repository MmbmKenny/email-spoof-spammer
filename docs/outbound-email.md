# Outbound Email, Brevo (free) for authenticated outreach

_Last researched: 2026-09-19. Confirm Brevo's current limits and include strings
in the Brevo console before relying on them._

## Architecture

```
   Conversations & replies            Personalized outreach (approved)
   ┌───────────────────────┐          ┌───────────────────────────────┐
   │  Zoho mailbox         │          │  Brevo (free plan)            │
   │  hello@DOMAIN         │◀── reply │  sends FROM hello@DOMAIN      │
   │  (receiving + replies)│          │  via authenticated DOMAIN     │
   └───────────────────────┘          └───────────────────────────────┘
              ▲                                     ▲
              └──────────  DOMAIN authenticated with  ──────────┘
                          SPF + DKIM + DMARC (one set)
```

- **Mailbox (Zoho):** where humans read and reply. Low volume.
- **Brevo:** where *approved, personalized* outreach and follow-ups are sent, so
  you don't burn the mailbox's tiny quota or its reputation.
- Both authenticate the **same DOMAIN**, so replies land in the Zoho inbox and
  sends pass authentication.

> **Reality check:** authenticating DOMAIN makes you *deliverable-eligible*. It
> does **not guarantee inbox placement.** On Brevo's free plan you send from a
> **shared IP** and every free email carries a **"Sent with Brevo"** footer.
> Placement depends on your sending behaviour and reputation (below).

## Brevo free plan (verify current)
- **300 emails/day**, up to **100,000 contacts**. Unused daily sends don't roll over.
- **Shared IP** (dedicated IP is Professional/Enterprise only).
- **"Sent with Brevo" branding** on every email (removable only on paid).
- Requires **domain authentication** (SPF + DKIM) to send from `@DOMAIN`.

## Domain authentication in Brevo
1. Brevo → **Senders, Domains & Dedicated IPs → Domains → Add a domain** → `DOMAIN`.
2. Brevo shows records to add to DOMAIN's DNS:
   - A **DKIM** record (Brevo's `brevo._domainkey` / `mail._domainkey` selector, use the exact host/value Brevo gives).
   - An SPF **include**, add `include:spf.brevo.com` to your **existing single**
     SPF record (see `email-setup.md`): `v=spf1 include:zoho.com include:spf.brevo.com ~all`.
   - A **Brevo verification** record (`brevo-code` TXT) if requested.
3. Add a **DMARC** record if not already present (shared with Zoho, one record):
   `v=DMARC1; p=none; rua=mailto:hello@DOMAIN; ...` (tighten to quarantine/reject later).
4. Click **Authenticate/Verify** in Brevo and wait for all records to go green.
5. Add and **verify the sender** `hello@DOMAIN` in Brevo.

## Deliverability discipline (this is what actually gets you into inboxes)

- **SPF / DKIM / DMARC** all passing, necessary baseline, not sufficient.
- **Sender reputation** builds slowly on a new domain. **Warm up gradually**:
  start ~10–20 emails/day, increase only if opens are healthy and bounces/
  complaints are near zero. Do **not** blast 300 on day one.
- **Bounce rate:** keep well under ~2–3%. Verify addresses before sending;
  remove hard bounces immediately.
- **Spam complaints:** keep under ~0.1%. One easy way to get complaints is
  emailing people who never asked, so target only genuinely relevant businesses
  with a real, personalized reason (see the CRM + research workflow).
- **Unsubscribe handling:** every campaign email must include a working
  unsubscribe link (Brevo adds one; keep it). Honor opt-outs immediately and set
  `do_not_contact=1` in the CRM (`python3 sales/crm.py stopcontact <id>`).
- **Personalization:** one real observation per message (never "Dear sir/madam").
  Generic bulk copy is both less effective and more likely to be marked spam.

## Compliance considerations
- Send only to businesses with a **legitimate reason** to hear from you; keep it
  B2B and relevant. Identify yourself honestly and give a real physical/contact
  detail and an unsubscribe option (aligns with anti-spam norms such as
  CAN-SPAM / GDPR-style consent expectations).
- Never scrape-and-blast, never hide who you are, never email someone who opted
  out. Re-confirm your obligations under Nigerian/EU rules for the audiences you
  actually contact.

## HARD RULE, human approval before sending
This project **must not** auto-send unsolicited email at volume. The workflow is:
1. Agent **researches** prospects and logs them in the CRM.
2. Agent **drafts** a personalized email + follow-ups (as Gmail/Brevo **drafts**).
3. **A human reviews and approves each message.**
4. A human (or an explicitly approved, throttled step) sends it.
5. Responses and opt-outs are recorded in the CRM.

Drafting, researching, and CRM updates are automated. **Bulk automatic sending
is not.**

## Verification checklist (once DOMAIN + Brevo exist)
- [ ] DOMAIN shows **Authenticated** in Brevo (SPF + DKIM green).
- [ ] `dig TXT DOMAIN` shows ONE SPF record containing both includes.
- [ ] Brevo DKIM host resolves (`dig` the selector Brevo gave).
- [ ] `dig TXT _dmarc.DOMAIN` present.
- [ ] Send ONE real test to a Gmail you own → "Show original" shows SPF=pass,
      DKIM=pass, DMARC=pass, and From is `hello@DOMAIN`.
- [ ] Unsubscribe link present and working.

Record results in `STATUS.md`. Configuration existing ≠ working.

## Sources
- Brevo free plan limits: https://help.brevo.com/hc/en-us/articles/208580669
- Brevo pricing: https://www.brevo.com/pricing/
- Brevo plans overview: https://help.brevo.com/hc/en-us/articles/208589409
