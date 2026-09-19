---
name: premium-web
description: >
  Build premium, high-trust, motion-rich web pages (landing pages, client
  sites, marketing sections) that do NOT look AI-generated. Use whenever
  creating or rebuilding any Brightfront or client-facing web page. Covers the
  house design system (dark glass + mesh), the GSAP+Lenis motion recipe, and
  the anti-generic + honesty rules.
---

# Premium Web — Brightfront House Style

Goal: pages that feel luxurious and trustworthy even on a zero budget. Motion is
purposeful, never gimmicky. **Trust comes from showing real working product, not
stock photos or fake reviews.**

## 1. Design system (tokens)

Dark-first, deliberately single-world (paint every color explicitly). Neutrals
carry a slight blue-green bias.

```
--bg:#080b0f  --bg2:#0c1117  --panel:#0f151c
--glass:rgba(255,255,255,.045)  --glass-2:rgba(255,255,255,.07)
--stroke:rgba(255,255,255,.10)  --stroke-2:rgba(255,255,255,.16)
--ink:#eef4f1  --muted:#9aa9b2  --faint:#6d7a83
--mint:#35e3a1  --teal:#18c6d6  --gold:#f1c65e  --violet:#8b7bf7  --coral:#ff7a59
```

- **Type:** display = `Fraunces` (characterful serif, use italic for the accent
  phrase in headlines); body/UI = `Manrope`. Load from Google Fonts with real
  fallback stacks. This pairing is the identity — do not swap to Inter/Space
  Grotesk (AI defaults).
- **Glass:** `background:var(--glass)` + `backdrop-filter:blur(16px) saturate(140%)`
  + 1px `--stroke` border. Premium glass = subtle blur + hairline border +
  soft shadow, never heavy frost.
- **Accent gradient:** `linear-gradient(135deg,var(--mint),var(--teal))`. Spend
  boldness in ONE place per section; keep surroundings quiet.
- **Ambient:** one fixed blurred mesh-gradient layer + faint grain. Subtle.

## 2. Motion recipe (GSAP + Lenis)

Libraries via allowed CDNs only:
- GSAP core + ScrollTrigger: `cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/...`
- Lenis smooth scroll: `cdn.jsdelivr.net/npm/lenis@1.1.14/dist/lenis.min.js`

Rules:
- **No-JS / reduced-motion safe.** Content is visible by default. Only add a
  `.js` class (which sets reveal start states) after confirming GSAP loaded and
  `prefers-reduced-motion` is not set. First viewport must be readable at rest.
- **Hero:** one orchestrated load timeline — staggered word reveal + card rise.
  Split headline into `<span class="word">` in the HTML (readable + no SplitText).
- **Below-fold:** `.reveal` (fade+rise, `once:true`) and `.reveal-c` (stagger
  children). Start at `top 85–86%`.
- **Smooth scroll:** Lenis driven by `gsap.ticker`; route `a[href^="#"]` through
  `lenis.scrollTo`.
- **One scrubbed moment:** e.g. the process progress line (`scrub`).
- **Count-up** honest stats on enter.
- **Desktop only** (`hover:hover and pointer:fine`): soft custom cursor,
  magnetic primary CTAs, subtle 3D card tilt. Skip on touch.
- Always honor `prefers-reduced-motion:reduce` (kill animations, show at rest).

## 3. Trust without fakery (non-negotiable)

- **Centerpiece = real demos running in-frame.** Put the actual live demo pages
  in a phone mockup via `<iframe>` (scaled, `pointer-events:none`) with an
  "Open full demo" link. Seeing the real product working beats any claim.
- No fake testimonials, client logos, reviews, or invented metrics.
- "Stats" must be true facts (price floor, service count, delivery window,
  deposit %). Never fabricate counts of clients/results.
- Label demo/sample businesses as demos.

## 4. Anti-generic checklist (before shipping)

- [ ] Not centered-everything; not one radius+shadow on every block.
- [ ] No emoji as section markers in headings (icons inside cards are fine).
- [ ] Numbered markers only where order is real (e.g. process steps).
- [ ] Distinctive type pairing (Fraunces + Manrope), real hierarchy.
- [ ] Boldness spent in one place per section; quiet elsewhere.
- [ ] Works at 400px; 16px side gutter; no horizontal scroll.
- [ ] Focus states visible; every non-void tag closed.

## 5. Files & deployment

- Author the canonical page as a full HTML doc for the repo (`landing/…`).
- CDN links work on GitHub Pages / Netlify — no build step, ₦0 hosting.
- For an in-chat preview, publish via the Artifact tool (strip the outer
  doctype/head/body wrapper; the artifact skeleton provides it) and bundle the
  demo files so the iframes and navigation work.

## Reference implementation

`landing/index.html` is the reference build of this system. Reuse its structure
and CSS when building new pages or client sites.
