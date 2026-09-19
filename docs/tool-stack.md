# Tool Stack & Costs

_Last reviewed: 2026-09-19_

The rule: **nothing paid gets added without your approval.** This file is the
single source of truth for what we use and what it costs. If a cost changes or
a free tier runs out, update this file the same day.

## Currently in use (₦0 / free tier)

| Tool | Purpose | Cost | Notes |
|------|---------|------|-------|
| Claude Code | Internal production (websites, catalogs, tools, copy) | Free tier / your existing plan | Our production engine. Customers never need to know. |
| Git + GitHub | Version control, code hosting | Free | Private repos free. |
| GitHub Pages | Free static hosting for demos & simple sites | Free | Custom domain supported. Good for websites/catalogs/landing pages. |
| Netlify / Cloudflare Pages | Alt free static hosting + forms | Free tier | Netlify free tier includes form submissions (100/mo). |
| SQLite | Lead database / CRM storage | Free | Single file, no server. Lives in `sales/leads/`. |
| Gmail | Outreach email + client comms | Free | Approval-first drafts (see outreach docs). |
| Google Maps / Search | Prospect research | Free | Find businesses, check if they have a site. |
| Instagram / Facebook / TikTok (web) | Prospect research + DM outreach | Free | Manual, respectful outreach only. |
| WhatsApp | Outreach + ordering-system deliverable | Free | wa.me links, click-to-chat. |
| Spreadsheet (Google Sheets / LibreOffice) | Backup lead tracking, quick views | Free | CSV import/export from CRM. |

## Available in this environment (verify before promising to a client)

These MCP integrations are connected to this workspace. **They are internal
production tools — do not tell a client "we have X integration" unless we have
actually used it for their project and verified it works.**

| Integration | Potential use | Verified working? |
|-------------|---------------|-------------------|
| Gmail | Draft/send outreach & client email | Connected — needs a real send test before relying on it |
| Canva | Social content, ad creative, brand assets | Connected — not yet used |
| Gamma | Proposal decks, service one-pagers | Connected — not yet used |
| Shopify | Ecommerce client stores, product catalogs | Connected — not yet used |
| GitHub | Hosting, code delivery | Connected & in use |
| Claude Docs | Shared proposals/notes | Connected — not yet used |

> Honesty rule: the "Verified working?" column must reflect reality. Never move
> a row to "verified" until we've actually completed a real task with it.

## Considered but NOT adopted (would cost money)

| Tool | Why we'd want it | Cost | Decision |
|------|------------------|------|----------|
| Custom domain (agency) | Professional email + landing page URL | ~₦10,000–15,000/yr (.com.ng / .com) | Optional. Not required to get first clients — use a free subdomain first. |
| Paid email sender (SendGrid/Brevo) | Bulk transactional email | Free tier exists; paid above limits | NOT needed. We do manual, personalized outreach, not bulk sends. |
| Paid hosting (VPS) | Dynamic apps / databases | ~₦5,000+/mo | Only if a client project needs a backend. Quote it into that project. |

## Cost summary

**Current monthly cost to run the agency: ₦0.**

First revenue does not require spending anything. A custom domain is the first
optional upgrade, and only once cash flow supports it.

## Deployment & email infrastructure (added 2026-09-19)

All free tier. See `docs/deployment.md`, `docs/email-setup.md`,
`docs/outbound-email.md`, and `STATUS.md`.

| Tool | Purpose | Cost | Notes |
|------|---------|------|-------|
| Cloudflare Pages | Live website hosting, HTTPS, custom domain, previews, rollback | Free | Build: `bash build.sh` → `public/`. 1 custom domain/project. |
| Zoho Mail (Forever Free) | Professional mailboxes `hello@DOMAIN` (receiving + replies) | Free | 5 users, 5GB each, 1 domain, webmail-only, ~200 sends/day. |
| Brevo (Free) | Authenticated outbound outreach (approved, throttled) | Free | 300 emails/day, shared IP, "Sent with Brevo" footer. |
| Domain name | Custom domain for site + email | ~₦10,000–15,000/yr | **Optional**, only when funds allow. Everything works on free subdomains first. |

**Still ₦0/month** until you choose to buy a domain. A domain is the single
optional purchase, and only when cash flow supports it.
