# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Dependency-free static rebuild of the Cessnock Motor Cycle Club public website. A small Python (stdlib-only) build script generates plain HTML into `dist/`, hosted on **Cloudflare Pages** at `new.cessnockmotorcycleclub.com.au`.

Cloudflare builds straight from this repo on push to `main` (build command `python3 build.py`, output dir `dist`, `PYTHON_VERSION=3.12`). **There is no CI workflow** — `.github/workflows/deploy.yml` and the `CNAME` file were removed when the site moved off GitHub Pages (2026-10-07). Consequence: anything that must land at the site root has to be emitted by `build.py` itself — see `ROOT_FILES` (currently `robots.txt`), which the old workflow used to `cp` by hand.

Cutting over the real domain (`www.cessnockmotorcycleclub.com.au`) off the legacy ColdFusion site is a separate, still-pending step.

## Commands

```bash
python3 build.py                       # build the site into dist/ (wipes dist/ first)
npm run dev                            # browser-sync live-reload server on :8001; rebuilds on changes to assets/, content/, build.py, site_data.py
python3 -m http.server 8000 -d dist    # plain static preview (no rebuild)
```

There are no tests and no linter. Python is stdlib-only — do not add pip dependencies; the CI build is just `python build.py` on Python 3.12.

## Architecture

Content comes from two sources, both rendered by `build.py`:

1. **`site_data.py`** — static pages as a `PAGES` list of dicts (`slug`, `title`, `eyebrow`, `intro`, `content` as raw HTML, optional `hero_image`/`body_class`), plus `NAV_ITEMS` and `FOOTER_LINKS`. Editing a fixed page means editing HTML strings here.
2. **`content/news/*.md`** and **`content/events/*.md`** — YAML-frontmatter markdown collections, editable by committee members through Pages CMS (schema in `.pages.yml`). `build.py` generates `/news/`, `/events/`, per-entry detail pages, and the homepage "Latest news / Events" section from these. Entries with `published: false` are skipped.

Key facts about `build.py`:

- **Hand-rolled parsers, deliberately minimal.** The frontmatter parser handles flat `key: value` scalars only (no nesting), and the markdown converter supports only `#`/`##`/`###`, flat `-` lists, paragraphs, `[links]()`, `**bold**`, `*italic*`. Don't write markdown features beyond that in content files, and don't swap in a library.
- **Asset fingerprinting.** Every file under `assets/` is copied to `dist/assets/` renamed to `name-<sha256[:8]>.ext` (flattened — subdirectory structure like `assets/media/` is NOT preserved in dist). All `assets/...` references in rendered HTML (and `404.html`) are rewritten via regex to the fingerprinted names. Reference assets by their source paths (e.g. `/assets/media/foo.jpg`) and let the build rewrite them; note the regex only matches `[\w-]` path characters, so no spaces/dots in asset filenames apart from the extension.
- **URLs are `slug/index.html`** with relative hrefs computed from page depth (`relative_prefix`). Internal links in `content` HTML should be written relative to the page (e.g. `membership/` from home, or use `/`-prefixed asset paths).
- **Hero images:** a page's `hero_image` (bare filename resolves to `assets/media/`) becomes a CSS background on the hero section; without one, the first `/assets/...` image in the page content is used.
- **`ROOT_FILES`** is copied verbatim into `dist/` at the end of `main()`. Add to it rather than relying on CI, which no longer exists.

Client-side JS is just `assets/site.js` (hamburger menu). Styles are one file, `assets/styles.css`.

## Design guardrails

`DESIGN.md` and `PRODUCT.md` define the visual system. The club picked the **"Since 1923" heritage direction** in September 2026, so the system is now: cream paper ground `#f6f1e7` with `#fffdf7` panels, club red `#a61b1b` used sparingly, **Bitter slab serif for `h1`–`h3`** over a system body stack, **8px** radii, and genuinely **flat** — `--shadow: none`, structure comes from 1px `#e4dcc9` rules, no hover lift. The homepage is led by the `.timeline` component.

Explicit don'ts: no gradient text, no reintroducing shadows, no glassmorphism/neon/SaaS-style heroes, keep WCAG AA contrast and reduced-motion support. **And don't describe the club as an enduro/racing club** — see below.

Bitter loads from Google Fonts via an `@import` in `assets/styles.css` — the site's one external dependency. Self-hosting is the wanted improvement but is blocked on fingerprinting: the asset-rewrite regex only touches `assets/...` references in HTML, not inside CSS.

## Content positioning

The club is the **oldest active motorcycle club in Australia**, and today a **social riding club**. It hosts the Australian Postie Bike GP, but as a signature once-a-year public event, not its primary purpose. The legacy site's "Hunter Valley's leading enduro club" framing was inherited by the first rebuild and has been removed — don't reintroduce it.

**Dates: 1923 is formal incorporation, not founding.** The club predates its paperwork by an unknown number of years. Copy therefore says "more than a century" / "since before 1923" and never a precise age — the old "103 years" phrasing was removed for exactly this reason, so don't reintroduce it. The club's most recent competitive event was the **Australian Four Day Enduro in 2018** (archive page `archive/a4de-2018` exists), which is what "it has been some years since" refers to.

## Content caveats

Migrated legacy content (committee names, membership pricing, meeting details) is pending owner review before launch — don't treat it as verified. Still unconfirmed and currently stated as fact on the live pages: first A4DE **1978**, first Postie GP **2014**, pricing **$30 single / $50 family**.

Confirmed by the owner (2026-10-07): **1923 = formal incorporation**, origins earlier but unknown; **oldest active motorcycle club in Australia**; **A4DE run by the club in 2018**. The "oldest active" line is a strong public claim that now appears on the homepage, About, membership and in the site description — it is owner-asserted, not independently checked.

The **events calendar has no upcoming entries** — only the two archived historical events. Three sample events existed in the design prototypes but were deliberately not shipped: publishing invented ride dates on a live club site risks people turning up to nothing.

`assets/docs/club-constitution.pdf` was generated locally from the legacy constitution HTML page, not an original club document. `assets/legacy-sweep/` holds preserved legacy files; leave them alone.

## Legacy site archive

The legacy ColdFusion site (Member Jungle CMS) was archived in full on **2026-10-07**, before cutover: browsable mirror + WARC record + fetch log, at **`../cmcc-legacy-archive/`** (outside this repo). See its README for coverage and known gaps.
