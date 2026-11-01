# Current generation evidence for follow-up issues 684–686

This append-only supplement is the current generation observation for Claw
[`9294730aeb19d269899177678db87406f4251555`](https://github.com/CultureBotAI/culturebotai-claw/commit/9294730aeb19d269899177678db87406f4251555),
in [Claw PR 683](https://github.com/CultureBotAI/culturebotai-claw/pull/683).
It accompanies [MIM PR 1001](https://github.com/CultureBotAI/MediaIngredientMech/pull/1001).
The prior report and both saved reviews remain byte-for-byte historical evidence.
No canonical mapping, ingredient record, aggregate, unified mapping, release
review or workflow/cycle artifact changed. The new candidate is diagnostic and
has not been promoted or scientifically approved.

The native generator ran from the committed head under verified
`RepositorySettings` and an owned `LockManager` lease, writing a new file at
`output/sssom-followup-684-686/ingredient_mappings.sssom.tsv`. It contains **2,980
rows**, SHA-256 `9fff31e31008a4aba70de846febe9f7de07770d84e86e4e7730c9acc69fffe31`.
Generator source SHA-256 was
`cc9c38c1d4922e6b167958daa2ce0bd2618e4c122e2de12c8af4ad13505c6c0e`
before and after invocation. [Generation receipt](generation-result.json)
records the exact command, timestamps, roots, code head and output hash.

The maintained canonical mapping remains **2,987 rows**, SHA-256
`89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9`.
Compared with the previous repaired 2,980-row candidate, **2,979 rows are
identical**. One generated B1 alias for `MIM:Sodium_Nitrate_070_M_Stock` changes
from `kgmicrobe.compound:sodium_nitrate_070_m_stock` to
`kgmicrobe.ingredient:sodium_nitrate_070_m_stock`, preserving the curated
identifier's namespace. Its `object_source` and explanatory `comment` follow
that change. Its old `none|UNKNOWN_TERM|2026-07-07` stamp is not copied to the new
triple; `validation_method` is blank. The curated primary identity and CHEBI
parent relation remain unchanged. No row dates, headers, predicates or synonym
payloads change relative to that previous candidate.

See [exact delta](previous-candidate-changes.json) and
[separate comparisons](candidate-comparison.json). The broader difference from
canonical is recorded separately: 2,365 changed shared pairs, 10 removed pairs,
three added pairs and 612 identical rows. These source/provenance differences
are not approval to replace canonical. The original failed generation's **41
diagnostics** remain explicitly reconciled in
[the retained selector ledger](original-41-remediation.json): 28 B5, eleven K
and two G diagnostics. All eleven corresponding historical K release holds
remain [WITHHOLD](historical-rule-k-holds.json).

## Follow-up behavior and validation

- [Issue 684](https://github.com/CultureBotAI/culturebotai-claw/issues/684):
  synthesized subject-slug aliases use the curated local identifier namespace,
  including when the maintained identifier has a different slug.
- [Issue 685](https://github.com/CultureBotAI/culturebotai-claw/issues/685):
  the exact B1 skip check is retained. When a mixed-case curated identifier
  requires a lowercase subject-slug alias, the builder emits that alias in
  the same curated namespace. Both native B1 and casefolding B5 pass. This
  was latent in the current corpus; regression and adversarial fixtures cover it.
- [Issue 686](https://github.com/CultureBotAI/culturebotai-claw/issues/686):
  valid ASCII calendar dates determine the maximum history date. Mixed
  dateless records retain empty cells for native Rule F curator rejection.
  An all-dateless set, or malformed nonempty emitted dates, is reported before
  replacing output. No clock/mtime fallback is introduced.
  [The explicit contract decision](date-contract.json) and
  [native integration proof](rule-f-integration/receipt.json) show that two
  dateless synthetic records both reach Rule F while one valid record supplies
  the header date. Actual corpus dates did not change.

MIM `just qc` passes on the maintained surfaces. The candidate separately passes
native invariants with zero rejects, SSSOM JSON Schema/prefix/CURIE checks,
configured label validation and native drift reconciliation (all five drift
categories zero). Candidate label counts: 2,216 canonical, four synonym, four
configured exception pairs, 3,736 no-adapter skips. Full baseline product
validation retains 101 nonblocking warnings and 5,314 no-adapter skips. The
native subject check retains 18 non-gating warnings. Actual-path native B4
finds no violations; BTO/MICRO transforms and absent IDs remain uncovered under
the native rule. No substitute labels, transforms or adapters were fabricated.

The committed code passes 84 focused tests, detected mutation checks, native
Ruff and mypy. Its full CI-style suite passes **6,025 tests**, with 377 skipped
and 87.83% coverage (70% gate). Safety-module coverage is 76% (60% gate).
[Independent adversarial review](adversarial-review-code.md)
of the exact final head reports no new findings. The log directory retains
actual command/exit/hash receipts, including expected red mutation runs and
setup failures. The comparison helper initially omitted the legitimate stamp
loss and an intermediate summary reused a loop variable; the final comparison
explicitly verifies the correct alias and blank stamp. Native validators were
unaffected. Exact suite receipts and the native successor review retain the
commands, exit codes and scope limits.

## Inputs, reproduction and preservation

[Input manifest](validation-inputs.json) records 2,985 exact hashes and repository
heads. CultureMech `a74dd489720c9df96cc073ffd11568d407d3c06c` outputs and
kg-microbe `d6baf5b90003a2032747559d94c00f86a7a4c615` Mediadive nodes remain
comparison inputs. The raw builder consumes maintained MIM mapped records,
the preserved copied residual classifications, the actual KG unified mapping
and ontology labels. CultureMech is not bulk imported. Source ontology DBs and
available KG transform hashes are recorded; OLS lookups were free and no paid
provider calls occurred.

The original run layout is recorded in every receipt. `recipes/run.py` retains
the environment wrapper; `locked_generation.py` retains the guarded native
invocation and refuses to overwrite its output. To repeat, choose a new output
path and a unique log name, resolve the verified repository roots, then run
the native builder with `--prior-stamps-from` the unchanged canonical mapping.
Use the recorded versions and input hashes. Run the native invariant validator
with an explicit fresh `--reject-tsv`, `sssom validate -V JsonSchema -V
PrefixMapCompleteness -V StrictCurieFormat`, `validate_published_curies.py` and
the captured candidate-only label configuration. The latter retains every
native policy, adapter, exception and field selection; only its target glob is
redirected. `compare_candidates.py` invokes native `find_drift` and checks the
exact previous-candidate delta; `check_b4_actual.py` invokes unchanged native B4
using the real read-only transform directory. Recipes retain original absolute
layout assumptions and must be given an equivalent isolated layout for replay.

[Post-validation preservation](post-validation-preservation.json) records zero
unexpected changes across 9,242 hash comparisons, unchanged original repository
states, all 87 prior evidence files preserved and no path overlap with live
PR 914 or Intel PRs 999/1000. Existing scientific issues, review holds and
historical validation stamps are not cleared by mechanical validation. The
previous supported/withheld partition remains tied to canonical, not this
candidate. No merge, ready transition, branch deletion or cycle advancement is
part of this supplement.
