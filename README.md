# Cessnock Motor Cycle Club static rebuild

This repository contains a dependency-free static rebuild of the public-facing Cessnock Motor Cycle Club website.

Instead of relying on a CMS, the site is generated with a small Python build script and deployed as plain static files. That keeps it easy to manage in git and cheap to host as static files on Cloudflare Pages.

The current rebuild carries over the main public images as project-local files under `assets/media/`, preserves a broader sweep of legacy public files under `assets/legacy-sweep/`, and includes a locally generated `assets/docs/club-constitution.pdf` based on the full legacy constitution page. The embedded homepage video still uses YouTube.

## Project structure

- `site_data.py` stores page content and site metadata.
- `build.py` generates the static site into `dist/`.
- `.pages.yml` configures Pages CMS collections and media folders.
- `content/news/` stores editable news articles.
- `content/events/` stores editable events.
- `assets/` contains the shared stylesheet.
- `assets/media/` contains exported images copied from the legacy site
- `assets/legacy-sweep/` contains additional preserved public legacy images
- `assets/docs/` contains preserved and generated downloadable documents
- `404.html` and `robots.txt` are copied to the site root by the build

## Local development

Build the site:

```bash
python3 build.py
```

Preview the generated site locally:

```bash
python3 -m http.server 8000 -d dist
```

Then open `http://localhost:8000`.

## Hosting — Cloudflare Pages

The site is hosted on **Cloudflare Pages**, built by Cloudflare directly from this
GitHub repository. There is no GitHub Actions workflow: pushing to `main` triggers a
Cloudflare build, and that is the whole deploy.

Cloudflare Pages project settings:

| Setting | Value |
|---|---|
| Build command | `python3 build.py` |
| Build output directory | `dist` |
| Python version | `3.12` (set `PYTHON_VERSION=3.12` as a build environment variable) |
| Install command | *(leave empty — stdlib only, nothing to install)* |

Custom domain: **new.cessnockmotorcycleclub.com.au**. The live club site
(`www.cessnockmotorcycleclub.com.au`) is a separate, later cutover.

Because Cloudflare publishes `dist/` exactly as the build leaves it, anything that
must appear at the site root has to be emitted by `build.py` — see `ROOT_FILES` in
that script, which currently copies `robots.txt`. (The retired GitHub Actions
workflow used to do this by hand, along with a `CNAME` file. Cloudflare has no use
for `CNAME`; custom domains are configured in the dashboard, so that file is gone.)

## Pages CMS setup

This project is now structured for [Pages CMS](https://pagescms.org/).

After the repository is on GitHub:

- open the repository in Pages CMS
- keep `.pages.yml` at the repository root
- use the `News` and `Events` collections to create and edit entries
- upload reusable images into `assets/media/`

The static build will automatically generate:

- `/news/` and individual news article pages
- `/events/` and individual event pages
- homepage summary sections for the latest news and events

## Content review before launch

This conversion is based on the public content available on the legacy site. Before pointing the real domain at the new build, review these details carefully:

- **first Australian Four Day Enduro (1978)** and **first Postie Bike GP (2014)**
- **membership pricing** ($30 single / $50 family, up to 6 members)
- committee names and roles
- meeting schedule and venue
- sponsorship references
- any historical pages you may no longer want publicly listed
- whether you want additional legacy galleries or documents copied into this repo as well

Confirmed by the club on 2026-10-07 and now stated on the site: 1923 is the club's
**formal incorporation** (its origins run an unknown number of years earlier), the club
is the **oldest active motorcycle club in Australia**, and it ran the **Australian Four
Day Enduro in 2018** — its most recent competitive event. The "oldest active" claim is
prominent on the homepage, About, and membership pages; it is the club's own assertion.

The events calendar is **empty of upcoming events** — it lists only the two archived
historical events. Real ride and meeting dates need to come from the committee before
launch; see "Adding events" below.

## Legacy document note

The old site did not expose a directly linked constitution PDF during migration. `assets/docs/club-constitution.pdf` was generated locally from the full public constitution HTML so the new site can offer a downloadable copy.

## Adding events

Create a markdown file in `content/events/` with YAML frontmatter — `title`, `slug`,
`start_date` (`YYYY-MM-DD`), optional `end_date`, `location`, `featured_image`,
`summary`, and `published: true`. Committee members can do this through Pages CMS
instead of editing files. Entries with `published: false` are skipped by the build.

Note the markdown support is deliberately minimal: `#`/`##`/`###`, flat `-` lists,
paragraphs, `[links]()`, `**bold**`, `*italic*`. Nothing else is parsed.

## Legacy site archive

The legacy ColdFusion site was archived in full on 2026-10-07 before cutover —
browsable mirror plus a WARC record. It lives outside this repo at
`../cmcc-legacy-archive/`; see the README there.

## Suggested next improvements

- self-host the Bitter heading font instead of loading it from Google Fonts
  (see the font delivery note in `DESIGN.md` — needs a fingerprinting change)
- add a small editor guide for committee members using Pages CMS
- add a contact form using Cloudflare Forms, Workers, or a third-party form service
