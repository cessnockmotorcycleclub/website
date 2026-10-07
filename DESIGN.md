---
name: Cessnock Motor Cycle Club
description: Visual system capturing the club's public website (colors, type, components)
colors:
  bg: "#26211b"
  panel: "#fffdf7"
  page: "#f6f1e7"
  text: "#2b2620"
  brand: "#a61b1b"
  brand-dark: "#7f1d1d"
typography:
  display:
    fontFamily: "Bitter, Georgia, 'Times New Roman', serif"
    fontSize: "clamp(2.2rem, 6vw, 4rem)"
    fontWeight: 700
    lineHeight: 1.08
  body:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.6
rounded:
  md: "8px"
components:
  button-primary:
    backgroundColor: "{colors.brand}"
    textColor: "{colors.panel}"
    rounded: "{rounded.md}"
    padding: "0.75rem 1rem"
---

# Design System: Cessnock Motor Cycle Club

## 0. Adopted direction — "Since 1923" (heritage)

Three layout prototypes were put to the club in September 2026. The club chose the
**heritage** direction: a cream-paper palette, slab-serif headings, ruled borders
instead of shadows, and a homepage led by a **timeline** of the club's century
rather than by a calendar or a marketing hero.

This reframes the whole site. Cessnock Motor Cycle Club is the **oldest active
motorcycle club in Australia** and today a **social riding club** — not the "leading
enduro club" the legacy site claimed. It still hosts the Australian Postie Bike GP,
but as a signature once-a-year public event, not its primary purpose. Copy throughout
should reflect that.

On dates: **1923 is formal incorporation, not founding.** The club was riding for an
unknown number of years before that, so copy says "more than a century" and "since
before 1923" rather than a precise age. Don't reintroduce a hard number like
"103 years" — it understates the club and implies a founding date we don't have.

The sections below describe the adopted system. The earlier dark-hero/white-card
scheme is retired.

## 1. Overview

Creative North Star: **"The Community Noticeboard, with a century behind it"** — a
friendly, legible public presence that prioritises clear information over flashy
presentation, and lets the club's age do the talking. The site preserves legacy
assets and should feel welcoming to members and families while staying easy for
committee editors to update.

Key Characteristics:
- Content-first: event and membership information are prominent and scannable.
- Photographic: authentic club photos carry tone and trust.
- Historical: the club's age is the lead asset, surfaced via the timeline.
- Low-friction: simple components and clear affordances for non-technical editors.

## 2. Colors

A warm, printed-paper palette: cream surfaces, dark brown-black ink, one red accent.

### Primary
- **Club Red** (#a61b1b): primary buttons, call-to-action links, timeline markers,
  and subtle emphasis. Slightly deeper than the previous #b91c1c to sit correctly
  on cream rather than white.

### Neutrals
- **Page** (#f6f1e7): the cream page ground.
- **Panel** (#fffdf7): card and content surface — a shade lighter than the page.
- **Background** (#26211b): dark brown-black for the footer and hero scrim.
- **Text** (#2b2620): default body text, warm near-black for legibility on cream.

Named Rule: The brand accent is used sparingly — reserve it for primary actions,
timeline markers, and key emphasis. Borders do the structural work instead.

## 3. Typography

Display Font: **Bitter** (slab serif), falling back to Georgia then Times New Roman.
Used for `h1`–`h3` only.
Body Font: system UI stack, for legibility in content and nav.

Character: archival and sturdy without being fussy — the serif headings signal age,
the system body keeps long-form content fast and familiar.

Hierarchy:
- Display (H1): Bitter 700, clamp(2.2rem, 6vw, 4rem) — hero and major headings.
- Body: 400, 1rem, line-height 1.6 — paragraphs and long-form content. Aim for a
  65–75ch measure in prose containers.

**Font delivery note.** Bitter currently loads from Google Fonts via an `@import` at
the top of `assets/styles.css`. This is the one external dependency on an otherwise
dependency-free site, and it costs a third-party request plus a render-blocking
import. Self-hosting the two woff2 files under `assets/` would be better, but note
that `build.py`'s fingerprinting only rewrites `assets/...` references in **HTML**,
not inside CSS — so self-hosting needs the font files exempted from fingerprinting,
or the rewrite extended to stylesheets. Until then the fallback to Georgia is the
safety net and must stay in the stack.

## 4. Elevation

Flat. The heritage theme sets `--shadow: none` and uses **1px ruled borders**
(#e4dcc9) plus tonal contrast between `--panel` and the cream page ground to separate
surfaces. Cards do not lift or transform on hover.

Named Rule: Structure comes from rules and tone, not shadow. Do not reintroduce
drop shadows.

## 5. Components

Buttons — character: confident, clear primary actions.
- Shape: rounded corners 8px.
- Primary: background `{colors.brand}`, text `{colors.panel}`, padding 0.75rem 1rem.
- Secondary: dark background for secondary affordance (see `.button-secondary`).

Cards / Containers — character: printed, content-first.
- Corner Style: 8px radius.
- Background: `{colors.panel}` with a 1px #e4dcc9 rule. No shadow.
- Accent variant (`.card-accent`): #fbf3e4 ground with a #ecd9b8 rule, for pricing
  and call-to-action asides.
- Internal Padding: 1.5rem typical; reduce on small screens.

Navigation — character: cream header on a 3px red bottom rule. Nav links use
pill-like hit targets and clear active states. Collapses to a hamburger on mobile.

Hero — character: photographic, with a cream panel (`.hero-panel`) over a darkened
photo. The panel carries a 5px red left border and holds the eyebrow, H1, and intro.

**Timeline** (`.timeline`) — the signature homepage component. A vertical red rule
with ringed markers; each entry is a bold red year followed by one short sentence.
Keep entries to a single line of meaning — it is a skimmable spine, not prose.

**GP banner** (`.gp-banner`) — a two-column image-plus-text band for the Postie Bike
GP, collapsing to one column under 820px.

## 6. Do's and Don'ts

Do:
- Do prioritise clear, scannable event and membership information over decorative layouts.
- Do use real club photos and preserve legacy media to convey trust and history.
- Do lead with the club's age and social-riding focus.
- Do ensure WCAG AA contrast and clear focus states for keyboard users.
- Do respect `prefers-reduced-motion`.

Don't:
- Don't use gradient text or background-clip:text treatments.
- Don't reintroduce drop shadows or hover lift — the theme is deliberately flat.
- Don't describe the club as an enduro or racing club, or imply it runs competitive events.
- Don't use large colored side-stripe borders as the primary affordance (the hero
  panel's red left border is the one sanctioned exception).
- Don't adopt glassmorphism, neon-on-black, or SaaS hero-metric templates that
  conflict with the club's approachable tone.
