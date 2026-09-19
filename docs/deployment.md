# Deployment — Cloudflare Pages (free)

_Last researched: 2026-09-19. Free-tier details change — re-check the linked
official docs before relying on any number._

Throughout, `DOMAIN` is a placeholder for the domain you will eventually own
(e.g. `brightfront.ng`). **Do not purchase anything to follow this doc** — every
step up to "custom domain" works on the free `*.pages.dev` subdomain.

## 0. Project compatibility (verified locally)

This project is a **pure static site** — no framework, no build dependencies.
Confirmed: no `package.json`, `requirements.txt`, `wrangler.toml`, or any bundler
config. The Python files in `sales/` are the **internal CRM tools and are NOT
part of the deployed website.**

Because docs, the CRM, and `.claude/` must never be served publicly, deployment
uses a tiny build step (`build.sh`) that assembles only the public site into
`public/`:

- `public/index.html` ← the landing page (`landing/index.html`, demo paths rewritten)
- `public/demos/…` ← the five demos

Run it locally any time to preview the exact deployed output:

```bash
bash build.sh
# then open public/index.html
```

## 1. Cloudflare Pages — settings

Create a free Cloudflare account, then **Workers & Pages → Create → Pages →
Connect to Git**, authorize GitHub, and pick this repository.

Build configuration:

| Field | Value |
|-------|-------|
| Production branch | `main` (merge the feature branch first) |
| Framework preset | **None** |
| Build command | `bash build.sh` |
| Build output directory | `public` |
| Root directory | `/` (leave default) |

Save and deploy. Cloudflare runs `build.sh`, publishes `public/`, and gives you a
live `https://<project>.pages.dev` URL with **automatic HTTPS** and a global CDN.

## 2. Automatic deployment from `main`

Once connected, **every push to `main` auto-deploys** to production. No action
needed after the first setup. Free plan allows up to **500 builds/month**.

## 3. Preview deployments

Every **pull request / non-production branch gets its own preview URL**
automatically (unlimited previews on free). Use this to review changes before
merging to `main`. Our working branch `claude/agency-client-acquisition-w7cwcm`
will produce a preview build once the repo is connected.

## 4. Custom domain + HTTPS

_(Only when you own `DOMAIN`. You do not need this to go live on `*.pages.dev`.)_

1. Cloudflare dashboard → your Pages project → **Custom domains → Set up a domain**.
2. Enter `DOMAIN` (and/or `www.DOMAIN`).
3. **If DOMAIN's DNS is on Cloudflare** (recommended — free): activation is
   near-instant; Cloudflare adds the record and provisions the SSL certificate
   automatically.
4. **If DOMAIN stays at another registrar**: add the `CNAME` record Cloudflare
   shows (typically `DOMAIN → <project>.pages.dev`) at your registrar's DNS.
5. Wait for the certificate to issue (usually minutes). HTTPS is then automatic
   and free; HTTP redirects to HTTPS.

> Free plan allows **1 custom domain per project**. Point the apex `DOMAIN` at
> the site and use `www` as a redirect, or vice-versa.

## 5. Environment variables & secrets

Pages settings → **Settings → Environment variables**. Set per environment
(Production vs Preview).

- This static site needs **no secrets to run**.
- **Never** put mailbox passwords, Brevo API keys, or DKIM private keys in the
  repo or in plain env vars. If a future feature needs a key, use Cloudflare's
  **encrypted secrets**, not plaintext variables, and never commit it.

## 6. Rollback

Pages → **Deployments** → open the three-dot menu on any previous successful
deployment → **Rollback to this deployment**. Instant (all versions are kept on
the edge). This is your undo button if a deploy breaks the site.

## 7. Free-plan limits to know

| Limit | Free plan |
|-------|-----------|
| Bandwidth | Unlimited |
| Builds | 500 / month |
| Files per site | 20,000 |
| Max single asset size | 25 MiB |
| Build timeout | 20 minutes |
| Custom domains / project | 1 |
| Preview deployments | Unlimited |

Our site is tiny (well under every limit).

## Alternative (also free): GitHub Pages

If you prefer to skip Cloudflare initially: repo **Settings → Pages**, deploy
from a GitHub Action that runs `build.sh` and publishes `public/`. Gives a free
`https://<user>.github.io/<repo>/` URL with HTTPS. Requires a **public repo** on
the free plan. Cloudflare Pages is recommended (custom domain + previews +
instant rollback are smoother).

## Sources
- Cloudflare Pages limits: https://developers.cloudflare.com/pages/platform/limits/
- Preview deployments: https://developers.cloudflare.com/pages/configuration/preview-deployments/
- Pages overview: https://developers.cloudflare.com/pages/
