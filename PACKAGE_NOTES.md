# PACKAGE NOTES — read before publishing

Assembled 2026-07-24. This file is for the builder, not for readers of the app.

---

## ✅ RESOLVED — licence now matches the constitution

**Was:** `COPYRIGHT.txt` read *"All rights reserved. No license is granted. No part of this
work may be copied, modified, redistributed, or used to create derivative works."* That
directly contradicted the vow stated four times in CORE — *free, open-source, free and
forkable, public and forkable, no hidden logic* — and would have made forking legally
impossible in a public repository.

**Provenance:** none. The file was referenced from `README.md` but **no decision creating
it appears anywhere in CORE or LOG.** It entered the project unlogged, which is precisely
what the grounding rule exists to prevent.

**Now:** replaced with `LICENSE`, containing the MIT licence **verbatim from the Open
Source Initiative** (opensource.org/license/mit). Verified programmatically as a
byte-for-byte match after whitespace normalisation. Only the year and holder name were
filled in — the OSI is explicit that the wording must remain unchanged to be enforceable.

Also updated so nothing still claims the old terms:
- `index.html` footer now reads "MIT licence — free to use, copy, modify and share"
- `README.md` licence section rewritten, including why the old file was replaced
- `COPYRIGHT.txt` deleted
- Verified: no shipping file contains "All rights reserved"

**One open question, not decided here.** MIT is a *software* licence and refers throughout
to "the Software". This project also contains substantial written educational content. If
you want the prose explicitly covered, the usual companion is **CC-BY-4.0 for content
alongside MIT for code**. Many projects do exactly this. *Not legal advice — a licence
choice with real consequences is worth a lawyer's eye.*

## Excluded deliberately

- **`_uslc_d.csv`** (S&P 500 daily prices, 3,409 rows). Used during testing. **Not
  included**: its provenance and redistribution terms were never verified, and Method
  Rule 10 forbids wiring in or redistributing a source whose terms are unchecked. No
  page in the app references it. If you want it in the repo, verify the source's terms
  first and record that verification.
- **`plainsight-3bB-board-v7-1.html`** — superseded, unlinked, and it still contained
  the biased shuffle fixed in v16. A dead file carrying a known bug is a hazard in a
  forkable repository, so it has been removed rather than shipped.

## Replaced in place (so existing links keep working)

| shipped as | contains |
|---|---|
| `plainsight-signal-test-1.html` | the S22 engine: rotation test, adaptive replicate counts, era-check luck rate shown, OHLC validation |
| `plainsight-citations-1.html` | citations [1]–[50], including the methodology sources |
| `plainsight-3bB-board-v16-1.html` | the fair (Fisher-Yates) wallet sampler |

## New, and NOT linked from any page — awaiting your decision

- **`plainsight-hourly-lab-1.html`** — flagged in-file as a lab build. Needs your
  four-gate review (READ, UNDERSTOOD, VERIFIED, APPROVED) before it joins the nav.
- **`plainsight-verification-register-1.html`** — every tool, test and claim, including
  the eight claims we withdrew. Link it from the nav if you want it public.
- **`plainsight-test-methods-1.html`** — is linked from the citations page but not from
  `index.html`. Add it to the nav if you want it on the main path.

⚠️ **The verification register is already stale** on the daily-engine numbers, which were
corrected after it was written. Update before publishing.

---

## Verification tooling (`/verification`)

Runnable with Node, no dependencies:

```
node verification/plainsight-calibration-lab.js        # 8 market generators, 4 null models, invariants
node verification/plainsight-mutation-test.js          # breaks the engine on purpose; current score 7/8
node verification/plainsight-numerical-sweep.js        # 67 adversarial-input checks
node verification/plainsight-executing-protocol.js     # runs every check, writes a timestamped record
```

The executing protocol appends to `docs/VERIFICATION_RECORD.md`. **A method may only be
marked DONE by running and producing evidence — self-report is not an accepted input.**

## Known-open, carried forward honestly

- **No out-of-sample holdout exists anywhere.** By CORE §2.8 the signal test is therefore
  **Gate 3 — "measured, not predictive."** Do not describe it as predictive.
- **Six of eight strategy-evidence methods have never been applied.** That is the claim
  the whole app rests on, and it is the least validated thing in it.
- **One mutation-test fault still escapes** (M5). Cause identified as an effect below
  measurement resolution, but not formally excluded as an equivalent mutant.
- **The candle test** carries the overlap/clustering code pattern harmlessly at its
  one-bar outcome window; measured 17.67% false positives at a five-bar window. One
  parameter change from breaking.
- **The 150-year series has never been tested** — only 13 years of one market — so the
  daily engine's era-stability check is unverified.
- **`Math.random` is unseeded** in the research desk and board. The picks are fair
  (uniform), but results are not reproducible between page loads. Disclosure issue.

---

## What was restored, and what was deliberately left out

**Restored** after checking whether each carried information preserved nowhere else:

- **`docs/PLAINSIGHT_BANKS.md`** — NOT history. It is the active operating-rules file, with
  a session-start ritual: *"The assistant reads this at the start of every session."*
  It must be in the repository, and it should be read first.
- **`docs/PLAINSIGHT_S19_SAVE-1.md`** and **`docs/PLAINSIGHT_S20_SAVE-2.md`** — verified to
  contain 16 and 15 headings respectively that appear **nowhere** in LOG-6, including the
  room manifest, the rename decisions and their reasoning, and the save-numbering
  correction. LOG-6 supersedes LOG-5 but not these; they were separate files.

**Left out**, each verified rather than assumed:

| file | why |
|---|---|
| `PLAINSIGHT_LOG-5.md` | **Measured:** all 24 of its headings appear in LOG-6, none missing. True superset. |
| `PLAINSIGHT_CORE-1.md` | **Measured:** CORE-2 is CORE-1 plus Rule 0B, 0 lines removed. |
| `PLAINSIGHT_CORE.md` | The S15 version, superseded twice. |
| `PLAINSIGHT_MASTER-14_UPDATE.md` | Pre-split single-file master, superseded by the CORE/LOG structure. |
| `plainsight-3bB-board-v7-1.html` | Dead, unlinked, and still carrying the biased shuffle fixed in v16. A hazard in a forkable repository. |
| `_uslc_d.csv` | B13 / Rule 10 — redistribution terms never verified. |

Nothing is destroyed: every excluded file remains in the working project. This is a
judgement about what belongs in a public repository, and it is reversible.
