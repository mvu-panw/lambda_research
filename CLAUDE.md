# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

Internal PANW account research for **Lambda AI** (GPU cloud), used by a sales engineer for technical enablement and firewall positioning.

**Deployed publicly:** pushed to the public repo `github.com/mvu-panw/lambda_research` (branch `main`). `.github/workflows/pages.yml` publishes only `site/` to GitHub Pages on every push to `main`. The repo itself (including `corpus/` and `CLAUDE.md`) is public too, so the user chose to publish knowing the positioning is visible to anyone. One-time manual step: Settings → Pages → Source = "GitHub Actions".

`Palo Alto Networks Resources/` (1.4 GB of public PANW PDFs) is gitignored as local reference only. Adding it would need Git LFS, because some files are close to GitHub's 100 MB limit.

`fortinet resources/` (FortiOS 7.6.8 Admin Guide, Fortinet product matrix, `fortibleed.pdf`) is also gitignored and kept as local competitive reference for the FortiGate incumbent. The admin guide is 148 MB, which is over GitHub's limit, so never commit it. Use `pdftotext` or the `pages` parameter instead of reading it whole.

## Layout

| Path | What |
|---|---|
| `.github/workflows/pages.yml` | GitHub Pages deploy (copies `site/` → `_site`) |
| `site/` | Static 6-page front end: `index`, `architecture`, `nvidia-gear`, `positioning`, `identity`, `resources` |
| `corpus/research/*.md` | Hand-collected evidence the crawler can't get (DNS, Ashby job posts, SafeBase trust-portal control text), dated in the filename |
| `corpus/{docs,blog,site}/*.md` | Plain-text crawl of docs.lambda.ai and lambda.ai (from sitemaps). Grep this before searching the web. |
| `corpus/github/<org>.json` | Repo listings for `lambdal` and `LambdaLabsML` (stars, description, last push) |
| `corpus/sources.csv` | url, title, local file, fetched_at for every crawled page |
| `tools/crawl.py` | Stdlib-only crawler (robots.txt respected, 1 req/s) |
| `Lambda *.pdf` | Mike's own topology diagrams. Copies and PNG renders live in `site/assets/diagrams/`. |

## Commands

```bash
python3 -m http.server 8080 --directory site    # preview the site
python3 -I tools/crawl.py --github              # refresh corpus (skips files that already exist; delete a file to refetch it)
pdftoppm -png -r 150 "Lambda 1-Click Clusters.pdf" site/assets/diagrams/1cc   # re-render a diagram after editing the PDF
```

To crawl a new source, add its sitemap to `SITEMAPS` or an org to `GITHUB_ORGS` at the top of `tools/crawl.py`.

`crawl.py` fetches with `curl` via subprocess on purpose: the python.org Python on this Mac has no CA bundle, so `urllib` fails TLS verification. Don't "fix" this by disabling verification.

## Site conventions

- **The UI is copied from `~/ai_sec_by_design`** (Prisma AIRS look: cyan/purple gradient, Inter font). `site/assets/css/styles.css` is that file unchanged, plus a block at the end marked "Lambda account site additions" (`.tag-*` confidence pills, `.prose`, `.two-col`, `.link-grid`/`.link-card`, `.table-wrap`, mobile nav wrap). Tables reuse the template's `.scoreboard-table`.
- **No templating:** nav and footer are copy-pasted into all 6 pages. Each page's `.nav-links` lists the *other* pages (Home appears on every page except `index.html`). Edit all 6 files when changing nav.
- Stylesheet is linked as `styles.css?v=1`. Bump it on every page together after CSS edits.
- **Every factual claim carries a source link and a confidence tag**: `tag-confirmed` (Lambda-owned page), `tag-reported` (third-party or secondhand), `tag-inferred` (our reasoning). PANW performance numbers come from reseller-hosted datasheet mirrors and are flagged as needing confirmation against official datasheets.

## Key account facts (verified in corpus, Oct 2026)

- Private Cloud perimeter/VPN is **Fortinet FortiGate** with FortiClient SSL-VPN (`corpus/docs/docs.lambda.ai__private-cloud__accessing-private-cloud.md`).
- 1CC: 16–512 H100/B200, Quantum-2 400G IB (3,200 Gb/s per node), 2×100G Ethernet per node, shared DIA (`docs.lambda.ai__public-cloud__1-click-clusters.md`).
- Lambda Cloud's own firewall is L3/L4 port/CIDR only, 100 global rules per workspace (`docs.lambda.ai__public-cloud__firewalls.md`).
- Vera Rubin NVL72 (H2 2026) ships with BlueField-4, Spectrum-6, ConnectX-9 (`corpus/site/lambda.ai__vr-200.md`).
- Lambda runs BlueField DPUs in zero-trust mode and owns them; its provisioning runs on the DPU (`corpus/blog/lambda.ai__blog__lambda-bare-metal-instances.md`). Any AIRS-on-DPU pitch is a platform sale to Lambda.
- Private Cloud product page now redirects to `lambda.ai/superclusters`; Lambda also sells air-gapped Superclusters to DoD (`lambda.ai/government`).
- Positioning logic: firewalls go north-south only (DIA edge, mgmt, OOB) and never in the IB/RoCE GPU fabric. Prisma AIRS on BlueField-3 is designed for ~1–5 Gbps, so position it for inference and head nodes, not training.
- Identity (`site/identity.html`, evidence in `corpus/research/identity-2026-11.md`): Google Workspace is confirmed (MX/SPF). The workforce IdP is **likely Okta but unconfirmed**: `lambda.okta.com` and `lambdal.okta.com` tenants exist, but ownership isn't verified, so keep it tagged `tag-inferred`. Trust-portal SOC 2 text confirms MFA on the IAM platform, HR-driven provisioning, and only *annual* access reviews. The Enterprise Security job post (Sep 2026) lists contractor/BYOD access, AI-agent data controls, and privileged access as the roadmap.
- Lambda Cloud API keys have full access to all API operations. Console SSO (SAML/OIDC) is 1CC-only, by invitation, with JIT provisioning and no documented SCIM.
- `cloud.lambda.ai` and `trust.lambda.ai` now redirect to `lambda.com`. The trust portal is SafeBase; its Auth0/Drata strings belong to SafeBase, not Lambda.

## Research tooling

Lambda's job board is readable without JS at `https://api.ashbyhq.com/posting-api/job-board/lambda` (`descriptionPlain` per job). Okta tenant existence: `https://<name>.okta.com/.well-known/okta-organization` returns JSON only for real tenants.

For larger or JS-heavy crawls, use Firecrawl or crawl4ai. `gh` is not installed, so use the GitHub REST API (`api.github.com/orgs/<org>/repos`). Use WebSearch/WebFetch for press, funding, and PANW datasheets.
