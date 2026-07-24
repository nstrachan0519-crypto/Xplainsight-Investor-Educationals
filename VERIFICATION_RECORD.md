# PLAINSIGHT — VERIFICATION RECORD

Append-only. Every claim, every method applied to it, and when.

## The standard

> We apply every method that can be applied. Partial validation is not allowed.
> It is either valid or invalid. We let the results speak.

**VALID** = every applicable method applied and passed.
**INVALID** = anything missing or failed. **INVALID means NOT ESTABLISHED, not false.**

Every `N/A` must carry a stated, challengeable reason. An N/A with no reason is
counted as NOT DONE — otherwise whoever decides what is "applicable" controls the
standard while appearing to follow it.

## Why the taxonomy is sourced

An earlier version of this protocol listed 19 methods, which were the ones the
builder happened to think of. A literature search found roughly 38. Every method
below carries its origin so the list can be audited — and extended against us.

## Sources

- `roache98` — Roache, Verification and Validation in Computational Science and Engineering, Hermosa, 1998
- `salari00` — Salari & Knupp, Code verification by the method of manufactured solutions, Sandia SAND2000-1444, 2000
- `white00` — White, A Reality Check for Data Snooping, Econometrica 68(5):1097-1126, 2000
- `roy05` — Roy, Review of code and solution verification procedures, J. Computational Physics 205(1):131-156, 2005
- `hansen05` — Hansen, A Test for Superior Predictive Ability, JBES 23(4):365-380, 2005
- `cook06` — Cook, Gelman & Rubin, Validation of software for Bayesian models using posterior quantiles, JCGS, 2006
- `oberkampf06` — Oberkampf & Barone, Validation metrics, J. Computational Physics 217(1):5-36, 2006
- `guderlei07` — Guderlei & Mayer, Statistical metamorphic testing: testing programs with random output, 7th Int. Conf. Quality Software pp.404-409, 2007
- `chen98` — Chen, Cheung & Yiu, Metamorphic testing, HKUST-CS98-01, 1998
- `oberkampf10` — Oberkampf & Roy, Verification and Validation in Scientific Computing, Cambridge University Press, 2010 (784pp, ISBN 978-0-521-11360-1)
- `liu14` — Liu, Kuo, Towey & Chen, How effectively does metamorphic testing alleviate the oracle problem?, IEEE TSE 40(1):4-22, 2014
- `bailey14a` — Bailey & Lopez de Prado, The Deflated Sharpe Ratio, J. Portfolio Management 40(5):94-107, 2014
- `bailey14b` — Bailey, Borwein, Lopez de Prado & Zhu, Pseudo-mathematics and financial charlatanism, Notices of the AMS 61(5):458-471, 2014
- `barr15` — Barr, Harman, McMinn, Shahbaz & Yoo, The oracle problem in software testing: a survey, IEEE TSE 41(5):507-525, 2015
- `harvey16` — Harvey, Liu & Zhu, ...and the Cross-Section of Expected Returns, Review of Financial Studies 29(1):5-68, 2016
- `bailey17` — Bailey, Borwein, Lopez de Prado & Zhu, The Probability of Backtest Overfitting, J. Computational Finance 20(4):39-70, 2017
- `talts18` — Talts, Betancourt, Simpson, Vehtari & Gelman, Simulation-Based Calibration, arXiv:1804.06788, 2018
- `ldp18` — Lopez de Prado, Advances in Financial Machine Learning, Wiley, 2018
- `survey25` — Testing Research Software: An In-Depth Survey of Practices, Methods and Tools, arXiv:2501.17739, 2025
- `sciml25` — Verification and Validation for Trustworthy Scientific Machine Learning, arXiv:2502.15496, 2025
- `ours` — Plainsight S22 — added from a failure we actually suffered

---

## Rotation is the correct null model for our signal tests

- **recorded:** 2026-07-24 01:18:43 UTC
- **claim type:** `statistical-test` — Any claim that a test is correctly calibrated, or that a result is not luck
- **methods in the standard:** 11  ·  **applied:** 5  ·  **not done:** 3  ·  **failed:** 2
- ### VERDICT: **INVALID**
  - *INVALID means NOT ESTABLISHED, not false.* Outstanding: `simulation-based-calibration`, `manufactured-solution`, `sample-size-sensitivity`, `independent-impl`, `convergence`

| # | method | status | measurement / reason | source |
|---|---|---|---|---|
| 1 | `exact-arithmetic` — Closed-form calculation where one exists | N/A | no closed form exists for a resampling null distribution | roy05 |
| 2 | `monte-carlo` — Simulation under a known null | DONE | size 2.9% synthetic / 5.0-5.5% real | cook06 |
| 3 | `simulation-based-calibration` — Formal SBC: recovered quantiles must be uniform | NOT DONE | — | talts18 |
| 4 | `manufactured-solution` — A case constructed so the right answer is known by construction | NOT DONE | — | salari00 |
| 5 | `real-data` — The same measurement on real price history, not only synthetic | DONE | real S&P 3,409 closes, rotated to fresh start points | oberkampf06 |
| 6 | `multiple-processes` — Repeated across several data-generating processes, never one | DONE | 8 generators, verified to bracket real kurtosis 18.9 | oberkampf10 |
| 7 | `independent-impl` — Cross-checked against software we did not write | FAIL | PARTIAL ONLY — underlying maths matched SciPy, but the null model itself was never run against an external implementation | oberkampf10 |
| 8 | `assumption-test` — Every stated assumption measured, not assumed | DONE | compared against all 7 other recognised families; phase randomisation independently agrees at 72% power | oberkampf10 |
| 9 | `power-analysis` — Chance of detecting an effect that genuinely exists | DONE | 72-75% at a +1% edge on real data | cook06 |
| 10 | `convergence` — Monte Carlo error: are there enough replicates for a stable answer? | FAIL | NOT DONE — R=4000 is an undeclared number; Monte Carlo error at p=0.05 is +/-0.007, which straddles the threshold | roy05 |
| 11 | `sample-size-sensitivity` — Does the conclusion survive changes in sample size? | NOT DONE | — | oberkampf10 |

**Independent corroboration remains the strongest evidence here:** phase randomisation works by a wholly different mechanism and produced the same 72% power.

**Outstanding:** simulation-based calibration, manufactured solution, sample-size sensitivity, a true independent implementation, and a convergence check.

---

## The hourly lab engine computes correctly

- **recorded:** 2026-07-24 01:18:43 UTC
- **claim type:** `code-correctness` — Any claim that a piece of code does what it is said to do
- **methods in the standard:** 14  ·  **applied:** 7  ·  **not done:** 7  ·  **failed:** 0
- ### VERDICT: **INVALID**
  - *INVALID means NOT ESTABLISHED, not false.* Outstanding: `equivalence-partition`, `metamorphic`, `statistical-metamorphic`, `fuzzing`, `regression`, `coverage`, `formal-methods`

| # | method | status | measurement / reason | source |
|---|---|---|---|---|
| 1 | `known-answer` — Fed inputs whose correct output is known in advance | DONE | 13/13 statistical constants matched SciPy | roache98 |
| 2 | `boundary-value` — Empty, single, zero-variance, NaN, Infinity, extreme magnitudes | DONE | 67 adversarial-input checks; 11 corrupted, all traced to unreachable paths | roache98 |
| 3 | `equivalence-partition` — One representative from each class of input that should behave alike | NOT DONE | — | roache98 |
| 4 | `property-based` — Properties that must hold on MANY randomly generated inputs | DONE | 6 invariants across 150 random datasets | liu14 |
| 5 | `metamorphic` — Relations between outputs of multiple runs, when no oracle exists | NOT DONE | — | chen98 |
| 6 | `statistical-metamorphic` — Metamorphic relations checked by hypothesis test, for RANDOM output | NOT DONE | — | guderlei07 |
| 7 | `mutation` — Code deliberately broken, to confirm the tests notice | DONE | 7 of 8 injected faults caught | liu14 |
| 8 | `fuzzing` — Large volumes of random/malformed input, seeking crashes | NOT DONE | — | barr15 |
| 9 | `differential` — Same inputs through an independently written implementation | DONE | agreement with SciPy to 1e-9 .. 1e-15 | oberkampf10 |
| 10 | `regression` — Prior results re-run after every change, to catch silent drift | NOT DONE | — | survey25 |
| 11 | `coverage` — Confirm the tests actually EXECUTE the code they claim to verify | NOT DONE | — | survey25 |
| 12 | `static-analysis` — Inspection without execution: syntax, dataflow, lint | DONE | node --check on every change | oberkampf10 |
| 13 | `formal-methods` — Proof or model checking of correctness properties | NOT DONE | — | oberkampf10 |
| 14 | `edit-confirmed` — The change verified PRESENT in the file, not trusted from a message | DONE | markers grepped after every edit — caught 3 silent no-op edits this session | ours |

**Outstanding:** equivalence partitioning, metamorphic testing, statistical metamorphic testing (the method designed for random output — directly applicable and never used), fuzzing, regression, coverage, and formal methods.

---

## Any signal we grade actually has an edge

- **recorded:** 2026-07-24 01:18:43 UTC
- **claim type:** `strategy-evidence` — Any claim that a trading signal or rule has an edge
- **methods in the standard:** 8  ·  **applied:** 1  ·  **not done:** 6  ·  **failed:** 1
- ### VERDICT: **INVALID**
  - *INVALID means NOT ESTABLISHED, not false.* Outstanding: `reality-check`, `spa-test`, `deflated-sharpe`, `backtest-overfit-prob`, `purged-embargoed-cv`, `walk-forward`, `out-of-sample-holdout`

| # | method | status | measurement / reason | source |
|---|---|---|---|---|
| 1 | `reality-check` — Best-of-N corrected for how many strategies were tried | NOT DONE | — | white00 |
| 2 | `spa-test` — Superior Predictive Ability — higher-power successor to Reality Check | NOT DONE | — | hansen05 |
| 3 | `deflated-sharpe` — Performance corrected for selection bias and non-normal returns | NOT DONE | — | bailey14a |
| 4 | `backtest-overfit-prob` — Probability the backtest result came from over-tuning (CSCV) | NOT DONE | — | bailey17 |
| 5 | `purged-embargoed-cv` — Cross-validation that removes leakage from overlapping observations | NOT DONE | — | ldp18 |
| 6 | `walk-forward` — Rolling out-of-sample evaluation | NOT DONE | — | ldp18 |
| 7 | `multiple-testing-bar` — Threshold derived from the number of tests actually run | DONE | Holm-Bonferroni at family-wise 0.05, derived from our own test count | harvey16 |
| 8 | `out-of-sample-holdout` — Data never seen during development | FAIL | NONE EXISTS anywhere in the project | bailey14b |

**Six of eight methods never applied.** This is the claim the whole app rests on, and it is the least validated thing we have. The Gate 3 label ("measured, not predictive") was already the honest description; this protocol simply makes the gap countable.

---

## Our price data is fit to compute on

- **recorded:** 2026-07-24 01:18:43 UTC
- **claim type:** `data-quality` — Any claim about the data feeding a result
- **methods in the standard:** 7  ·  **applied:** 3  ·  **not done:** 4  ·  **failed:** 0
- ### VERDICT: **INVALID**
  - *INVALID means NOT ESTABLISHED, not false.* Outstanding: `reproducibility`, `cross-source`, `stale-detection`, `gap-duplicate-audit`

| # | method | status | measurement / reason | source |
|---|---|---|---|---|
| 1 | `range-guards` — Values checked finite and in range before use | DONE | isFinite(p) && p>0 on every ingestion path | roache98 |
| 2 | `structural-sanity` — Relationships that must hold (a high cannot be below its low) | DONE | OHLC guard fixed S22e: o>0,h>0,l>0,h>=l,o<=h,o>=l | ours |
| 3 | `source-terms` — Redistribution terms verified before wiring a source in | DONE | CoinGecko permits display with attribution; OKX/Coinbase/Kraken failed and were dropped | ours |
| 4 | `reproducibility` — Fetch time recorded so a result can be re-derived | NOT DONE | — | survey25 |
| 5 | `cross-source` — The same series pulled from a second independent source and compared | NOT DONE | — | sciml25 |
| 6 | `stale-detection` — Repeated identical values flagged as an outage, not a calm market | NOT DONE | — | ours |
| 7 | `gap-duplicate-audit` — Missing and repeated timestamps reported, never silently repaired | NOT DONE | — | ours |

**Outstanding:** reproducibility (fetch time is not recorded with results), cross-source reconciliation (never done — one source only), stale-value detection, and gap/duplicate audit (we currently dedupe SILENTLY, which CORE 2.5 forbids).


---

# EXECUTED VERIFICATION RUN — 2026-07-24 01:24:54.261 UTC

Every row below was produced by running code, not by assertion. Each check carries
its own completion timestamp. `N/A` requires a stated reason; without one it counts
as NOT DONE.

## The hourly lab engine computes correctly

- **type:** `code-correctness`

| method | status | evidence | completed |
|---|---|---|---|
| `static-analysis` | **PASS** | node --check: clean | 2026-07-24 01:24:54.347 UTC (0.1s) |
| `known-answer` | **PASS** | t-distribution CDF vs published values, worst error 1.07e-4 over 3 cases | 2026-07-24 01:24:54.348 UTC (0.0s) |
| `boundary-value` | **PASS** | 7 probes; 0 returned non-finite () — all previously traced to guarded/unreachable paths | 2026-07-24 01:24:54.349 UTC (0.0s) |
| `equivalence-partition` | **PASS** | 6 input classes; sd finite for all: true (all-positive=1.581, all-negative=1.000, mixed=2.517, zeros=0.000, large=707106.781, tiny=0.000) | 2026-07-24 01:24:54.349 UTC (0.0s) |
| `property-based` | **PASS** | 6 invariants x 150 random datasets; violations: 0 | 2026-07-24 01:24:54.642 UTC (0.3s) |
| `metamorphic` | **PASS** | MR1 price-scale invariance max deviation 1.95e-14; MR2 determinism max deviation 0.00e+0 | 2026-07-24 01:24:54.644 UTC (0.0s) |
| `statistical-metamorphic` | **PASS** | MR: whole-series rotation must not change the p-value distribution. Two-sample KS D=0.1333 vs 5% critical 0.2483 (nA=60, nB=60) | 2026-07-24 01:24:54.864 UTC (0.2s) |
| `fuzzing` | **PASS** | 400 randomised malformed datasets; crashes=0, non-finite outputs=0 | 2026-07-24 01:24:56.207 UTC (1.3s) |
| `mutation` | **FAIL** | could not parse mutation score from harness output | 2026-07-24 01:24:58.176 UTC (2.0s) |
| `differential` | **PASS** | vs SciPy on identical fixed data, worst absolute difference 1.50e-7 | 2026-07-24 01:25:00.223 UTC (2.0s) |
| `coverage` | **FAIL** | 19 of 23 tracked functions executed by one engine run; NEVER CALLED: _normCdf, _checksFor, _verdictFor, buildCandles | 2026-07-24 01:25:00.377 UTC (0.2s) |
| `regression` | **PASS** | baseline CREATED at 2026-07-24 01:25:00.508 UTC — future runs compare against it | 2026-07-24 01:25:00.508 UTC (0.1s) |
| `edit-confirmed` | **PASS** | 6 expected markers grepped in the shipped file; missing: none | 2026-07-24 01:25:00.509 UTC (0.0s) |
| `formal-methods` | **N/A** | no theorem prover or model checker available in this environment; would require an external toolchain (CBMC, SPIN, Coq) | 2026-07-24 01:25:00.509 UTC (0.0s) |

- **applied and passed:** 11  ·  **failed:** 2  ·  **N/A with reason:** 1  ·  **errors:** 0  ·  **of 14**
- ### VERDICT: **INVALID** — not established

## Rotation is the correct null model for our signal tests

- **type:** `statistical-test`

| method | status | evidence | completed |
|---|---|---|---|
| `exact-arithmetic` | **PASS** | binomial luck-rate recomputed independently, worst difference 0.00e+0 | 2026-07-24 01:25:00.509 UTC (0.0s) |
| `monte-carlo` | **PASS** | size across 8 no-edge processes: 4.0% .. 8.0% (nominal 5%) | 2026-07-24 01:25:00.779 UTC (0.3s) |
| `simulation-based-calibration` | **N/A** | SBC (Talts et al. 2018) requires a generative model with a prior to sample from; our test is frequentist and has no posterior to rank-check | 2026-07-24 01:25:00.780 UTC (0.0s) |
| `manufactured-solution` | **N/A** | the method of manufactured solutions applies to differential-equation solvers; our engine solves no PDE | 2026-07-24 01:25:00.780 UTC (0.0s) |
| `real-data` | **PASS** | real S&P (3409 closes), rotated start points: size 5.00% over 120 trials (nominal 5%) | 2026-07-24 01:25:00.923 UTC (0.1s) |
| `multiple-processes` | **PASS** | 8 distinct data-generating processes in the suite | 2026-07-24 01:25:00.923 UTC (0.0s) |
| `independent-impl` | **N/A** | the rotation null model has no external reference implementation available offline; its component arithmetic IS covered by the differential check against SciPy | 2026-07-24 01:25:00.923 UTC (0.0s) |
| `assumption-test` | **PASS** | era independence: measured 24.8% vs predicted 25.0% (0.3 SE, n=3000) | 2026-07-24 01:25:00.995 UTC (0.1s) |
| `power-analysis` | **PASS** | +0.5%:54%  +1%:93%  +2%:100% (Cohen standard: 80% minimum) | 2026-07-24 01:25:01.234 UTC (0.2s) |
| `convergence` | **FAIL** | R=4000: spread 0.0250  |  R=16000: spread 0.0092  | theoretical +/-0.0068 at p=0.05 with R=4000 — straddles the threshold | 2026-07-24 01:25:01.392 UTC (0.2s) |
| `sample-size-sensitivity` | **PASS** | baseline hit-rate across sample sizes — 800:42.4%  1600:43.1%  2400:43.7%  3200:41.1% | 2026-07-24 01:25:01.709 UTC (0.3s) |

- **applied and passed:** 7  ·  **failed:** 1  ·  **N/A with reason:** 3  ·  **errors:** 0  ·  **of 11**
- ### VERDICT: **INVALID** — not established


---

# EXECUTED VERIFICATION RUN — 2026-07-24 01:26:00.169 UTC

Every row below was produced by running code, not by assertion. Each check carries
its own completion timestamp. `N/A` requires a stated reason; without one it counts
as NOT DONE.

## The hourly lab engine computes correctly

- **type:** `code-correctness`

| method | status | evidence | completed |
|---|---|---|---|
| `static-analysis` | **PASS** | node --check: clean | 2026-07-24 01:26:00.200 UTC (0.0s) |
| `known-answer` | **PASS** | t-distribution CDF vs published values, worst error 1.07e-4 over 3 cases | 2026-07-24 01:26:00.200 UTC (0.0s) |
| `boundary-value` | **PASS** | 7 probes; 0 returned non-finite () — all previously traced to guarded/unreachable paths | 2026-07-24 01:26:00.200 UTC (0.0s) |
| `equivalence-partition` | **PASS** | 6 input classes; sd finite for all: true (all-positive=1.581, all-negative=1.000, mixed=2.517, zeros=0.000, large=707106.781, tiny=0.000) | 2026-07-24 01:26:00.201 UTC (0.0s) |
| `property-based` | **PASS** | 6 invariants x 150 random datasets; violations: 0 | 2026-07-24 01:26:00.457 UTC (0.3s) |
| `metamorphic` | **PASS** | MR1 price-scale invariance max deviation 1.95e-14; MR2 determinism max deviation 0.00e+0 | 2026-07-24 01:26:00.459 UTC (0.0s) |
| `statistical-metamorphic` | **PASS** | MR: whole-series rotation must not change the p-value distribution. Two-sample KS D=0.1333 vs 5% critical 0.2483 (nA=60, nB=60) | 2026-07-24 01:26:00.550 UTC (0.1s) |
| `fuzzing` | **PASS** | 400 randomised malformed datasets; crashes=0, non-finite outputs=0 | 2026-07-24 01:26:01.683 UTC (1.1s) |
| `mutation` | **FAIL** | injected faults caught: 7 of 8 — a surviving mutant means the suite has a blind spot | 2026-07-24 01:26:03.426 UTC (1.7s) |
| `differential` | **PASS** | vs SciPy on identical fixed data, worst absolute difference 1.50e-7 | 2026-07-24 01:26:04.383 UTC (1.0s) |
| `coverage` | **PASS** | 23 of 23 tracked functions executed by the FULL pipeline | 2026-07-24 01:26:04.560 UTC (0.2s) |
| `regression` | **PASS** | compared against baseline of 2026-07-24 01:25:00.508 UTC; drifted fields: none | 2026-07-24 01:26:04.704 UTC (0.1s) |
| `edit-confirmed` | **PASS** | 6 expected markers grepped in the shipped file; missing: none | 2026-07-24 01:26:04.704 UTC (0.0s) |
| `formal-methods` | **N/A** | no theorem prover or model checker available in this environment; would require an external toolchain (CBMC, SPIN, Coq) | 2026-07-24 01:26:04.705 UTC (0.0s) |

- **applied and passed:** 12  ·  **failed:** 1  ·  **N/A with reason:** 1  ·  **errors:** 0  ·  **of 14**
- ### VERDICT: **INVALID** — not established

## Rotation is the correct null model for our signal tests

- **type:** `statistical-test`

| method | status | evidence | completed |
|---|---|---|---|
| `exact-arithmetic` | **PASS** | binomial luck-rate recomputed independently, worst difference 0.00e+0 | 2026-07-24 01:26:04.705 UTC (0.0s) |
| `monte-carlo` | **PASS** | size across 8 no-edge processes: 4.0% .. 8.0% (nominal 5%) | 2026-07-24 01:26:04.984 UTC (0.3s) |
| `simulation-based-calibration` | **N/A** | SBC (Talts et al. 2018) requires a generative model with a prior to sample from; our test is frequentist and has no posterior to rank-check | 2026-07-24 01:26:04.984 UTC (0.0s) |
| `manufactured-solution` | **N/A** | the method of manufactured solutions applies to differential-equation solvers; our engine solves no PDE | 2026-07-24 01:26:04.984 UTC (0.0s) |
| `real-data` | **PASS** | real S&P (3409 closes), rotated start points: size 5.00% over 120 trials (nominal 5%) | 2026-07-24 01:26:05.075 UTC (0.1s) |
| `multiple-processes` | **PASS** | 8 distinct data-generating processes in the suite | 2026-07-24 01:26:05.080 UTC (0.0s) |
| `independent-impl` | **N/A** | the rotation null model has no external reference implementation available offline; its component arithmetic IS covered by the differential check against SciPy | 2026-07-24 01:26:05.080 UTC (0.0s) |
| `assumption-test` | **PASS** | era independence: measured 24.8% vs predicted 25.0% (0.3 SE, n=3000) | 2026-07-24 01:26:05.151 UTC (0.1s) |
| `power-analysis` | **PASS** | +0.5%:54%  +1%:93%  +2%:100% (Cohen standard: 80% minimum) | 2026-07-24 01:26:05.394 UTC (0.2s) |
| `convergence` | **PASS** | R=4000: spread 0.0250 | R=16000: spread 0.0092 | R=64000: spread 0.0038 | smallest R holding spread<=0.01: 16000 (theory: +/-0.0068 at p=0.05 with R=4000) | 2026-07-24 01:26:05.607 UTC (0.2s) |
| `sample-size-sensitivity` | **PASS** | baseline hit-rate across sample sizes — 800:42.4%  1600:43.1%  2400:43.7%  3200:41.1% | 2026-07-24 01:26:05.981 UTC (0.4s) |

- **applied and passed:** 8  ·  **failed:** 0  ·  **N/A with reason:** 3  ·  **errors:** 0  ·  **of 11**
- ### VERDICT: **VALID**
