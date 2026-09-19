# Infrastructure Status

_Last updated: 2026-09-19._

**Honesty rule:** a line is only `✅ VERIFIED` if it was actually tested and
passed. Configuration existing, or a doc describing it, is **not** verification.
Anything not truly tested is `❌ NOT VERIFIED`.

Most live checks below cannot be verified yet because **no domain has been
purchased and no Cloudflare / Zoho / Brevo accounts exist** (per instructions:
do not purchase). They become verifiable once you own a domain and create the
free accounts, then run the checklists in the linked docs.

## Website / deployment

| # | Item | Status | Notes |
|---|------|--------|-------|
| 1 | Framework compatibility (static, deployable) | ✅ VERIFIED | No build framework present; confirmed pure static. |
| 2 | `build.sh` produces clean `public/` | ✅ VERIFIED | Ran locally: outputs `index.html` + `demos/`; internal docs/CRM excluded; no broken `../` links. |
| 3 | Live public website (Cloudflare Pages) | ❌ NOT VERIFIED | Requires connecting the repo in a Cloudflare account. Steps in `docs/deployment.md`. |
| 4 | Automatic deploy from `main` | ❌ NOT VERIFIED | Configured only after step 3. |
| 5 | Preview deployments | ❌ NOT VERIFIED | Available after step 3. |
| 6 | HTTPS / SSL | ❌ NOT VERIFIED | Automatic on Pages once deployed; not yet live. |
| 7 | Custom domain | ❌ NOT VERIFIED | No domain owned. |
| 8 | Rollback capability | ❌ NOT VERIFIED | Native to Pages; untested until deployed. |

## Email (Zoho — receiving + replies)

| # | Item | Status | Notes |
|---|------|--------|-------|
| 9  | Domain ownership verified in Zoho | ❌ NOT VERIFIED | No domain / account. |
| 10 | MX records | ❌ NOT VERIFIED | Values documented in `docs/email-setup.md`. |
| 11 | SPF | ❌ NOT VERIFIED | Single record planned (Zoho + Brevo combined). |
| 12 | DKIM | ❌ NOT VERIFIED | Generated & enabled in Zoho console (pending). |
| 13 | DMARC | ❌ NOT VERIFIED | Start `p=none`, tighten later. |
| 14 | Mailbox receiving (`hello@DOMAIN`) | ❌ NOT VERIFIED | Test: send from Gmail, confirm arrival. |
| 15 | Reply passes SPF+DKIM | ❌ NOT VERIFIED | Check "Show original" in Gmail. |

## Outbound (Brevo — approved outreach)

| # | Item | Status | Notes |
|---|------|--------|-------|
| 16 | Brevo account + free plan | ❌ NOT VERIFIED | No account yet. |
| 17 | Sending domain authenticated (SPF+DKIM) | ❌ NOT VERIFIED | Add Brevo include + DKIM; verify in console. |
| 18 | DMARC alignment for Brevo sends | ❌ NOT VERIFIED | Confirm via test to Gmail. |
| 19 | Legitimate outbound send (1 real test) | ❌ NOT VERIFIED | Send one test; confirm SPF/DKIM/DMARC=pass. |
| 20 | Unsubscribe link works | ❌ NOT VERIFIED | Verify on first campaign. |
| 21 | Human-approval workflow enforced | ✅ VERIFIED (by design) | No auto-bulk-send exists in this project; outreach is draft → human approve → send. |

## Documented limitations (known now)

- **Zoho free:** webmail-only (no IMAP/POP), 5 users, 1 domain, ~200/day send cap.
- **Brevo free:** 300 emails/day, shared IP, "Sent with Brevo" footer, no dedicated IP.
- **Cloudflare Pages free:** 1 custom domain/project, 500 builds/month, 20k files.
- **Deliverability:** authentication ≠ guaranteed inbox placement; reputation must
  be warmed up gradually.
- **No domain purchased**, so items 3–20 are pending by design, not failing.

## How to move items to VERIFIED
1. Register a domain (cheapest available `.com.ng`/`.com` when funds allow) and
   put its DNS on Cloudflare (free).
2. Deploy per `docs/deployment.md` → verifies items 3–8.
3. Set up Zoho per `docs/email-setup.md` → verifies items 9–15.
4. Set up Brevo per `docs/outbound-email.md` → verifies items 16–20.
5. Update this file with the actual test result and date for each line.
