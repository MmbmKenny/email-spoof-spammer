# Professional Email Setup — Zoho Mail (free custom-domain mailboxes)

_Last researched: 2026-09-19. Zoho's free tier has changed repeatedly — confirm
every limit against Zoho's own docs before relying on it._

`DOMAIN` = the domain you will own (e.g. `brightfront.ng`). **You cannot create
`hello@DOMAIN` until you own DOMAIN.** Everything here is the plan + exact records
to add once you do. Nothing here requires a purchase to read/prepare.

## Why Zoho (free)
Zoho Mail's **Forever Free** plan currently offers custom-domain mailboxes at
₦0: up to **5 users**, **5 GB each**, **1 custom domain**, ad-free, with the DNS
records (MX/SPF/DKIM) guided in their console.

### Known free-plan restrictions (verify current)
- **Webmail/mobile-app access only** — IMAP/POP/Active Sync are typically blocked
  on the free plan (no Outlook/Apple Mail desktop sync).
- **1 custom domain**, **5 users** max.
- **Low daily send caps** (reported ~200/day, rolling hourly). Fine for personal
  replies — **bulk outreach must go through Brevo**, not the mailbox (see
  `outbound-email.md`).
- Data-region is chosen at signup and is hard to change later.

## Mailboxes to create
Start with what you'll actually use (each address = 1 "user" on free, so be
economical):

- `hello@DOMAIN` — primary, public-facing (put this on the website).
- `contact@DOMAIN` and `info@DOMAIN` — set up as **aliases of `hello@`** (aliases
  don't consume a user slot) unless you want separate inboxes.
- `sales@DOMAIN` — optional, when you want to separate sales threads.

## Setup steps (in order)
1. **Sign up** at Zoho Mail → choose the free plan → "Add existing domain",
   enter `DOMAIN`.
2. **Verify domain ownership** — add the **TXT** (or CNAME) verification record
   Zoho shows to DOMAIN's DNS. Wait for verification.
3. **Create your first mailbox**: `hello@DOMAIN`.
4. **MX records** — point mail to Zoho (values Zoho displays; typical):
   | Type | Host | Value | Priority |
   |------|------|-------|----------|
   | MX | @ | `mx.zoho.com` | 10 |
   | MX | @ | `mx2.zoho.com` | 20 |
   | MX | @ | `mx3.zoho.com` | 50 |
   Remove any old/registrar-default MX records so mail routes only to Zoho.
5. **SPF** — add ONE TXT record at `@`. If Zoho is your only sender:
   ```
   v=spf1 include:zoho.com ~all
   ```
   You will **merge Brevo into this same record** later (see below) — never
   create two SPF records.
6. **DKIM** — in Zoho console generate a DKIM key (selector, e.g. `zoho`), then
   add the CNAME/TXT it gives at `zoho._domainkey.DOMAIN`, and **enable** it in
   the console after publishing.
7. **DMARC** — add a TXT at `_dmarc.DOMAIN`. Start in monitor mode:
   ```
   v=DMARC1; p=none; rua=mailto:hello@DOMAIN; fo=1; adkim=s; aspf=s
   ```
   Move to `p=quarantine` then `p=reject` only after SPF+DKIM pass cleanly for a
   couple of weeks (check the `rua` reports).

## Combined SPF once Brevo is added
When you also send via Brevo, use a **single** SPF record combining both includes:
```
v=spf1 include:zoho.com include:spf.brevo.com ~all
```
(Confirm Brevo's exact include string in its console — see `outbound-email.md`.)

## Sending / receiving limits (free — verify current)
- **Receiving:** generous (normal mailbox use).
- **Sending (mailbox):** low daily cap (~200/day reported), rolling hourly; up to
  ~100 recipients per message (may drop to 50 under a custom policy). Treat the
  mailbox as for **conversations and replies**, not campaigns.

## Verification checklist (do these once DOMAIN + records exist)
- [ ] Domain shows **Verified** in Zoho.
- [ ] `dig MX DOMAIN` returns the Zoho MX hosts.
- [ ] `dig TXT DOMAIN` shows the SPF record (exactly one).
- [ ] `dig CNAME zoho._domainkey.DOMAIN` (or TXT) resolves; DKIM **enabled** in console.
- [ ] `dig TXT _dmarc.DOMAIN` shows the DMARC record.
- [ ] Send a test **to** `hello@DOMAIN` from Gmail → it arrives (receiving works).
- [ ] Reply from `hello@DOMAIN` → Gmail shows SPF=pass, DKIM=pass (open "Show original").

Record results in `STATUS.md`. **Do not mark anything working until the test
above actually passes.**

## Sources
- Zoho Mail rates & limits: https://www.zoho.com/mail/help/adminconsole/rates-and-limits.html
- Zoho Mail setup help: https://www.zoho.com/mail/help/
- Zoho free-plan overview (independent): https://truehost.com/zoho-mail-forever-free-plan/
