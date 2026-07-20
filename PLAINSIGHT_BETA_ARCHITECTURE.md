# PLAINSIGHT — BETA APP ARCHITECTURE (S18)

## The shape of the app
One folder of self-contained HTML files on any static host. No build step, no server, no database, no dependencies — the folder IS the app. `plainsight-home-1.html` is the front door and the ONLY file that knows other files' version numbers; when any page ships a new version, update its one link there. The user's phone is the runtime; public APIs are the backend; the identity rule is the login system (there isn't one, on purpose).

## File manifest (current versions — the beta set, 14 files)
| Role | File | Status |
|---|---|---|
| Front door + feedback |  plainsight-home-2.html (market-organized) | new (S18) |
| Wallet board | plainsight-3bB-board-v16-1.html | LIVE-VERIFIED (HL pipes proven on phone) |
| Markets pack (COT gauges) | plainsight-markets-pack-3.html | DOC-EXPECTED |
| Company reading + EDGAR checker | plainsight-company-reading-7.html | education live; checker DOC-EXPECTED |
| Bonds & metals | plainsight-bonds-metals-2.html | education |
| Remaining markets compendium | plainsight-remaining-markets-2.html | education |
| Wealth bookshelf | plainsight-wealth-bookshelf-4.html | education |
| Case for active | plainsight-case-for-active-2.html | education |
| Museum of losses | plainsight-museum-of-losses-4.html | education |
| Prediction graveyard | plainsight-prediction-graveyard-3.html | education |
| Flight simulator | plainsight-flight-simulator-3.html | crypto pipe verified-pattern; 4 Stooq modules DOC-EXPECTED |
| Graduation | plainsight-graduation-2.html | education |
| Needle widget | plainsight-needle-widget-2.html | tool (self-contained) |
| Buy-and-hold deep dive | (S15 build, project archive) | education — add current filename to home on deploy |

## Data pipes (the whole backend)
| Pipe | Used by | Status |
|---|---|---|
| Hyperliquid /info (keyless POST) | board: accounts, fills, sampler | LIVE-VERIFIED on phone |
| CoinGecko market_chart | simulator crypto module | pattern LIVE-VERIFIED (prior sessions) |
| CFTC Socrata (publicreporting.cftc.gov) | markets pack ×4 gauges | DOC-EXPECTED |
| SEC ticker map + data.sec.gov submissions | insider checker | DOC-EXPECTED |
| Stooq CSV (stooq.com/q/d/l) | simulator ×4 modules | DOC-EXPECTED |
| FRED (DFII10) | macro gauge (board family) | CORS-blocked → shim pattern (known) |

ONE phone session tests every DOC-EXPECTED pipe. Each failure is a finding (→ shim list), not a blocker: dark-on-failure means the app degrades honestly.

## Feedback mechanism (vow-clean v1)
No server → feedback rides channels the user owns: structured copy-paste template + mailto link on the home page. Before launch: replace the `SET-FEEDBACK-ADDRESS` placeholder (search string) with a real address. When the open-repo decision lands, the repo's issues page becomes the permanent public feedback record and the home page gets its link — feedback then satisfies the "public and forkable" vow too (bugs and their fixes become part of the public history, like F1–F10 already are in LOG).

## What "beta" means here (printed on the front door)
Pipes may go dark and say why; sample warnings are load-bearing; users are named as test pilots; the flight recorder is the feedback box. Honesty is the beta program.

## Remaining checklist to launch
1. LIVE-TEST SESSION: one phone pass over CFTC, EDGAR, Stooq ×4 → upgrade or shim each; log results.
2. Set the feedback address (home page placeholder).
3. Add buy-and-hold deep dive's filename to home (it predates this manifest).
4. Repo decision → issues-page feedback link + widget/graveyard ambitions unblock.
5. FIVE-STAGE LAUNCH REVIEW: The builder personally clears READ → UNDERSTOOD → VERIFIED → APPROVED per page — the gate that exists precisely because an AI helped build a skeptic's tool. Nothing ships around it.

## S18 UPDATES
- HOME v2: landing reorganized BY MARKET (crypto/stocks/bonds-rates/metals/currencies/everything-else/every-market); pages listed under every market they serve; simulator in all groups (it contains all markets); quick-start row on top.
- CONNECTIVE TISSUE: every page now carries a "Keep going" footer of related links whose labels state the cross-page correlations (e.g., sequence-of-returns ↔ cohort catastrophe named as "the same lesson at two zoom levels").
- ESMA 74–89% added to the compendium's options evidence (was markets-pack-only).
- plainsight-validate.py added: the whole check suite (tags/JS/glossary/prescription-sweep/dead links) as one shippable command — ships with the repo so users can check us.
- PLAINSIGHT_CLAIM_REGISTRY.md added: canonical list of every shared empirical claim + carrying pages; corrections grep the registry, not the site.
- ⚠ DEPLOY RULE: ship ONLY manifest files. The working folder holds 19+ frozen old versions (with pre-correction figures) — they are archives, not deployables.
