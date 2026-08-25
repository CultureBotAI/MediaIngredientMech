# Next Tasks — MediaIngredientMech backlog

Deferred work, each entry with enough context to pick up cold. **Maintenance:**
update this file as work is started/finished — move done items out, add new
deferrals here. Keep the cross-Mech items in sync with the sibling repos'
`NEXT_TASKS.md` (CultureMech / CommunityMech / TraitMech). The hub,
culturebotai-claw, now keeps one too, for items no single Mech owns.

Last reconciled: 2026-08-21 (measured the `publish-sssom` blocker; item 14 is new and is the top of the queue).
**#160** was filed on 2026-07-30 for the `trigger_paths` gap described in the
vendored-sync section below.

> **Reconcile note (2026-08-21).** Scope of this pass was the question "what
> stands between us and a fresh published MIM SSSOM?", so it measured the
> blocker rather than re-reading the issue that describes it. **#416's diagnosis
> is incomplete, and the incomplete half is the larger half** — see the new
> **item 14**. #416 frames the entire 155/102 row difference as a registry-CURIE
> *policy* question. Rebuilt from both mains on 2026-08-21: 82 published subjects
> are absent from the rebuild and 82 new ones appear, and they are **the same 82
> records under a different spelling** — 65 case variants, 17 paren-escape
> variants, plus a few genuine relabels. Checked against the repo's own
> `mim_curie_for_stem`, **all 2,512 rebuilt subjects resolve to a real record
> file and 82 published subjects do not**, and 11 published subjects violate
> `curie.py`'s own `_CURIE_RE`. The rebuild is the correct side and the guard is
> refusing to promote a correction. Only ~73 rows are a genuine policy call.
>
> Found on the way: **`just curie-validate` does not read the SSSOM.** Its
> justfile comment claims to assert the published file satisfies the CURIE
> standard; the body runs `pytest tests/test_curie_normalizer.py` and opens no
> artifact. It is green today against a file with 11 violating subjects — the
> #178/#179/#180/#188/#189 "guard that is not guarding" class, again.
>
> 13 PRs merged since 2026-08-13 (#397–#430). Predicate flips are **0** on shared
> keys, confirming #409/#415 fixed that half for real. Gates at this pass:
> `check-instruction-refs` OK (33 files, 68 recipes); `check-chebi-currency`
> unchanged — local **252** vs ChEBI **253**, still upstream lag a refresh cannot
> fix.
>
> ⚠ The working tree of the primary checkout was 2 commits behind `origin/main`
> at this pass, with locally-modified `pyproject.toml`/`uv.lock` and five
> untracked files that partly duplicate merged #412 content. This reconcile was
> therefore done in a clean worktree off `origin/main`. Sort that checkout out
> before curating from it.

> **Reconcile note (2026-08-04, second pass).** After PR #190's reconcile earlier
> today, an entire thread shipped and went unlogged: the **microbedecoder
> unmapped-labels onboarding + residual grounding** (#193/#194/#195/#202/#205/#211,
> and closed #201) — now captured as **item 12** below. Eleven open issues belong
> to it (#196, #197, #203, #204, #206, #207, #208, #209, #210, #212, #213), none of
> which appeared here before. Gate/currency status at this pass: `check-instruction-refs`
> OK (32 files, 58 recipes); `check-chebi-currency` local build **252** vs ChEBI
> **253** — behind by 1, **upstream lag a refresh cannot fix** (bears on the 6
> deferred antibiotics). A second session is concurrently working
> `fix/microbedecoder-residual-merges-blends`; this pass did not touch it.

> **Reconcile note (2026-08-13).** The file had drifted badly again: **40 PRs
> merged since 2026-08-04**, and an entire thread went unlogged — the **two-lane
> deep-research validation of every ingredient record** (#309) and the whole
> curation arc it produced (#314 → #356), now captured as **item 13**. Item 12's
> microbedecoder issues are almost all closed (#196, #203, #204, #207, #208,
> #212, #213); only #206 and #209 remain. #114 is closed, which retires item 7.
>
> **The most important finding of this pass is item 0, which was not in the file
> at all**: `UNIFIED_INGREDIENT_MAPPING.tsv` was last rebuilt **2026-07-20** and
> still carries superseded identifiers. kg-microbe re-syncs that artifact on
> every consolidation run, so three weeks of curation is not reaching the
> consumer.
>
> Gates at this pass: `check-instruction-refs` OK (32 files, 62 recipes);
> `check-chebi-currency` local **252** vs ChEBI **253**, and the check now
> reports explicitly that **a refresh would not help** — the published semsql
> build is byte-identical to the local one, so this is upstream lag. Treat any
> missing-id verdict on a high accession as unproven and check OLS4 first.

**Shipped 2026-08-03/04 — the "guards that were not guarding" thread.**
Five PRs, all closing the same class of defect: a check that reports OK while
checking nothing.

| PR | closes | what was wrong |
|---|---|---|
| #178 | #171 | The role applier wrote role slots per-record only, so the next `just export-individual` reverted them — the #148 mechanism, in the tool the role-research lane runs. |
| #179 | #169, #176 | `aggregate_records.py` and `verify_roundtrip.py` defaulted to `data/collections/`, which nothing reads; the round-trip verifier paired records on a key that was not asserted unique. |
| #180 | #164 | The curation-history advisory's `data/custom/*.yaml` matched zero tracked files (that directory holds a `.tsv`). #164 as filed did not reproduce; the adjacent surface was genuinely broken. |
| #188 | #185 | Skills/commands/prompts naming recipes and paths that no longer exist — including `merge-ingredients` telling agents to validate every merge with a script that was never there. |
| #189 | #181 | The curation-history advisory **counts** matches and never asserts, so a dead pathspec reads exactly like "no records changed". |

New local gates, both in `just qc` and blocking in CI:
`just check-instruction-refs` · `just check-curation-targets`.

Two follow-ups filed rather than guessed, because both need judgment rather than
a path fix: **#186** (`just enrich-with-hierarchy` is cited as CultureMech's but
exists in no repo — and it is the documented hand-off for the role-research lane
in item 5) and **#187** (`data/curation/flagged_duplicates.yaml` never existed,
and the 61 duplicate identifier PKs in item 2 will produce exactly those flags).

> **Reconcile note (2026-07-30).** The previous reconcile was 2026-06-15 and the
> file had drifted badly: PRs #114–#157 shipped in the interim, including two
> entire threads it never mentioned (the **role-facet migration + role-research
> pipeline**, and the **vendored-sync drift check that retired the sha256 pins**),
> and **none of the 7 open GitHub issues** appeared anywhere in it. Section 2's
> description of a 3-line sha256 pin manifest was actively wrong — that mechanism
> was retired in #156/#157. Everything below is verified against the tree at
> `675d771f`. Gates on `main` are green: `qc-sssom` Rules A/B1/B2/B3 pass,
> `validate-products` reports OK_CANONICAL 5034 / OK_ID_ONLY 1667 /
> OK_EXCEPTION 16 / **IMPLAUSIBLE_LABEL 0**.

---

# Pending & actionable

## 0. Rebuild and publish `UNIFIED_INGREDIENT_MAPPING.tsv` — DONE (2026-08-13, PR #358)

Rebuilt and published: **131 rows changed `mim_id`**, coverage MAPPED 1905 →
1965, matched-to-MIM 30% → 53%. Verified reproducible — the committed artifact
is byte-identical to what the builder now produces.

The rebuild found a builder bug first (**culturebotai-claw#67**): `chebi_index`
and `ontology_index` were last-writer-wins, and MIM's merge pattern deliberately
gives the REJECTED loser the WINNER's identifier, so tombstones shadowed live
records. `Glucose` — 2,120 CultureMech occurrences — was being published as
`REJECTED`. Fixed before publishing; REJECTED 50 → 20.

Two follow-ups filed: **#359** (nothing gates this artifact — the reason it
drifted; the regenerate-and-diff pattern used elsewhere cannot work because the
builder and CultureMech live outside this repo) and **#360** (a tombstone keeps
an `ontology_id` it no longer asserts, mis-routing `D-Glucose`; affects ~31
tombstones).

**Still open from this item: the `Cobalamine` conflict below is unresolved.**
The published file carries `CHEBI:30411` per PR #350. If #138's view prevails,
the record moves first and the TSV is rebuilt after.

### original entry

`UNIFIED_INGREDIENT_MAPPING.tsv` was last written on **2026-07-20**
(`38a66b67`, PR #140). `data/curated/mapped_ingredients.yaml` has changed on
**2026-08-13** and in ~40 PRs between. kg-microbe's loader re-syncs this file on
every consolidation run and picks the primary CURIE with
`best_primary([chebi_id, culturemech_term_id, mim_id, kg_microbe_node_id, cas_rn])`,
so **every stale row is actively re-asserted downstream**.

Spot-checked 2026-08-13 — the file still carries identifiers that curation has
since superseded:

| ingredient | still in the TSV | corrected to | where |
|---|---|---|---|
| `Cobalamine` | `CHEBI:28911` cob(III)alamin | `CHEBI:30411` cobalamin | PR #350 |
| `EDTA` | `CHEBI:64755` EDTA(2-) | `CHEBI:4735` the free acid | PR #351 |
| `m-Inositol` | `CHEBI:10642` scyllo-inositol | merged into `myo-Inositol` | PR #347 |

Plus every merge from #341/#347/#351/#353/#355, which retire whole records the
TSV still lists.

**Do this before any further curation.** The `build-unified-mapping` skill owns
it. Two things to settle during the rebuild rather than after:

1. **Item 6 / #138 is the same surface** — the stale-precedence-column bug. A
   rebuild fixes those three rows only if the builder writes all precedence
   columns from the current grounding rather than preserving old ones. Verify,
   do not assume.
2. **#138 and PR #350 disagree about `Cobalamine`.** #138 records the *intended*
   grounding as `CHEBI:28911` and calls `CHEBI:30411` stale; #350 moved the
   record to `CHEBI:30411` on the evidence that ChEBI defines `CHEBI:28911` as
   "oxidation state of **+3**" while the label states none, and that the
   record's own CAS points at cob(**I**)alamin — a third state. **One of the two
   is wrong and the rebuild will publish whichever wins**, so decide it
   deliberately.

## 1. `sanitize_filename` casing corruption (#147) — DONE (2026-07-30, PR #159)

`scripts/export_individual_records.py:155` ends with
`name = "_".join(part.capitalize() … )`. Python's `str.capitalize()` **lowercases
everything after the first character**, so `just export-individual` rewrites
per-record filenames to a casing the committed corpus does not use
(`14-B-D-Galactobiose` → `14-b-d-galactobiose`). Simulated over the tracked
corpus on 2026-07-30: **387 of 2,252 tracked records would get a different filename**
(the issue estimated 359). On macOS's case-insensitive filesystem `git status`
stays empty, so it is invisible — two files have *already* drifted on disk
(`data/ingredients/mapped/Α1-acid_Glycoprotein_From_Bovine_Plasma.yaml`,
`data/ingredients/unmapped/Α-d-glucose_Monohydrate.yaml`; git tracks
`…Α1-Acid_…` / `…Α-D-Glucose_…`). Committed from a case-sensitive filesystem it
would rename 387 files and desync their SSSOM `MIM:` subjects.

**Why it is first:** it blocks #2 and #3 below (any corpus-wide re-export today
would bake in the 387 renames) and it closes #149 outright.

**⚠ The issue's proposed fix does not work — measured 2026-07-30.** Option 1
("drop the `.capitalize()` lowercasing so the function matches the committed
corpus") rests on the assumption that the corpus follows one case-preserving
rule. It does not: **the corpus is a historical mix of two rules**, so no single
naming function reproduces it. Simulated over all 2,252 tracked per-record files,
comparing each candidate against the filename **git tracks** (not the drifted
on-disk name):

| rule | exact | + `_N` collision suffix | mismatch |
|---|---|---|---|
| current — `part.capitalize()` per part | 1859 | 6 | **387** |
| uppercase first char of each part, preserve rest | 1854 | 3 | **395** |
| uppercase first char only (the docstring's rule) | 1124 | 3 | 1125 |
| no case transformation at all | 1079 | 0 | 1173 |

The two leading rules fail on **disjoint** sets. Today's rule mismatches files
that preserve inner capitals (`1-Kestose`, `14-B-D-Galactobiose`); the
case-preserving rule mismatches files that were *created by* today's rule and
carry a lowercased tail (`112-trichloroethane`, `2-mercaptoethanol`). Switching
to case-preserving would rename **more** files (395) than leaving the bug in
place (387). Note the function's own docstring is already inconsistent with its
code — it promises `"NaCl (99%)" -> "NaCl_99"` and `"sodium chloride" ->
"Sodium_chloride"`, neither of which `capitalize()` produces.

**The fix that actually works: make the exporter filename-stable.**
`export_collection_to_individual_files` deletes every `*.yaml` in the output
directory and rewrites from the collection, so the filename is re-derived from
`preferred_term` on every run — that re-derivation is the whole bug. The file
already solves this exact class of problem for `discussions` via
`PreservedFields`, which indexes by identifier *and* by preferred_term because
neither key survives every move. Apply the same pattern to filenames: capture
each record's existing filename before the clear, reuse it on rewrite, and fall
back to `sanitize_filename` only for genuinely new records. That renames nothing,
keeps every published `MIM:` subject valid, and removes the silent-corruption
mode outright.

Second, smaller change: `capitalize()` also corrupts chemical casing on *new*
records — `TAPSO` → `Tapso`, `KI` → `Ki`, `MnCl2` → `Mncl2`, and the corpus
carries the scars (`Feso43_X_N_H2o`, `Na2moo7_X_2_H2o`, `K2hpo4`). With stability
in place this only affects newly-added records, so the rule can safely be
corrected to the documented first-character-only behaviour without touching
anything already committed.

`src/mediaingredientmech/curie.py::mim_curie_for_stem` carries a stated "must
stay identical" contract with culturebotai-claw's
`build_mim_ingredient_sssom._mim_curie`. **The stability fix does not touch it** —
stems stop changing, so the contract is honoured rather than renegotiated.

**Shipped 2026-07-30 (PR #159).** `FilenameIndex` + `collect_existing_filenames`
mirror the `PreservedFields` pattern the same file already uses for
`discussions`, indexing by identifier *and* preferred_term and dropping ambiguous
keys rather than guessing. `sanitize_filename` was corrected to the documented
first-character-only rule for new records. The two already-drifted working-tree
filenames were restored, which is what made `tests/test_curie_normalizer.py` fail
locally while passing in CI. Verified: `just export-individual` rewrites all
2,260 records with **zero renames**; 490 tests pass; `just curie-validate` green.
9 new tests in `tests/test_export_filename_stability.py` pin the behaviour,
including idempotency across repeated runs.

**#149 (non-ASCII α escaping) was a duplicate of this, with a wrong diagnosis —
closed 2026-07-30.** The diagnosis is kept here because the two Greek-alpha
records are a *symptom* of #147 and stay broken until the casing is restored.
Verified 2026-07-30: `mim_curie_for_stem("Α1-Acid_Glycoprotein_From_Bovine_Plasma")`
returns `MIM:~3911-Acid_Glycoprotein_From_Bovine_Plasma`, exactly the published
SSSOM subject — the escaping round-trips fine. The character is U+0391 *capital*
Greek Alpha (`CE 91` → `~391`), not the lowercase α the issue body claims, and
`format(945, '02X')` = `'3B1'` (the `02` is a minimum width, nothing truncates).
The single unresolvable subject is just the working-tree file having been
lowercased by #147, and it disappears when the casing is restored. Note that
#149 only ever mentioned one of the two Greek-alpha records; fixing #147 covers
both.

## 2. Duplicate identifier families — SUPERSEDED BY REVIEWED BASELINE

**Historical snapshot (2026-07-30).** This item predates the reviewed duplicate-family
contract and must not be read as a current uniqueness requirement. `identifier` is a
semantic identity slot, not a guaranteed unique document address; distinct supplied
forms may share a CURIE when `MAPPING_SEMANTICS.md` permits it. Current duplicate
families and their reviewed dispositions are governed by
`mappings/duplicate_identifier_baseline.tsv`. At the time of this snapshot,
`data/ingredients/mapped/` held 1,879 files carrying 1,793 distinct identifiers:

```
grep -h '^identifier:' data/ingredients/mapped/*.yaml | sort | uniq -d
```

The collisions split into two dispositions, and telling them apart is the work:

- **True duplicates → merge** (`merge-ingredients`): `Glycyl-glycine` /
  `Glycylglycine` (CHEBI:17201), `Glycerol_2` / `Glycerol` (CHEBI:17754),
  `Glutathione` / `L-Glutathione` (CHEBI:16856),
  `Deoxyribonucleic_Acid_From_Herring_Sperm` / `Fish-sperm_Dna` (CHEBI:16991).
- **Distinct compounds sharing an imprecise identifier → re-identify**
  (`manage-identifiers`), *not* merge:
  `Rhamnogalacturonan_From_Soy_Bean_Pectic_Fibre` / `Rhamnogalacturonan_I_From_Potato_Pectic_Fiber`
  (both `cas:39280-21-2`), `Mucin_From_Porcine_Stomach_Type_III` /
  `Mucin_From_Porcine_StomachType_II` (both `cas:84082-64-4`),
  `B-Mannan_Borohydrate_Reduced_Carob_Seed` / `Mannan_From_Saccharomyces_Cerevisiae`
  (both `cas:9036-88-8`).
- **Judgement call:** `K2hpo4_X_3_H2o` / `K2hpo4` both on `CHEBI:131527` — the
  trihydrate is arguably a `skos:narrowMatch` on a `cas:`-primary record (the
  pattern used for `Mg(NO3)2 x 6 H2O`, see the ledger below), not a merge.

Do not add a repo-wide uniqueness invariant. New or changed families must instead
be checked against `mappings/duplicate_identifier_baseline.tsv` and assigned the
appropriate reviewed disposition; true duplicate records remain merge candidates.

## 3. Collection ↔ per-record drift (#148) — DONE (2026-08-02, PR #167)

Counts on 2026-07-30: mapped 1,879 per-record files vs 1,879 collection entries;
unmapped **378 per-record files vs 381 collection entries**.

**The drift runs collection-stale / per-record-current — the opposite direction
from the issue's "Suggested fix", which would re-demote three correct groundings.
Rewrite that section of #148 before anyone acts on it.** The 3-entry surplus is
exactly:

| collection entry (stale) | per-record file (current) |
|---|---|
| `UNMAPPED_0488` Phytone | `mapped/Phytone.yaml` → `FOODON:03315720` |
| `UNMAPPED_0531` Soya pepton | `mapped/Soya_Pepton.yaml` → `FOODON:03315720` |
| `UNMAPPED_0558` Tryptone peptone | `mapped/Tryptone_Peptone.yaml` → `MICRO:0000182` |

All three are already in `data/curated/mapped_ingredients.yaml`; only their
pre-promotion `UNMAPPED_*` entries were never deleted from
`data/curated/unmapped_ingredients.yaml` (lines 8330, 9677, 10713). Note Phytone
and Soya pepton share `FOODON:03315720` — they are also one of the 61 collisions
in item 2.

Also in scope, found during this reconcile:

- **A bare, non-conforming identifier:** `identifier: TAPSO` in
  `data/curated/unmapped_ingredients.yaml` and `data/ingredients/unmapped/Tapso.yaml`.
  Every other unmapped record uses an `UNMAPPED_NNNN` placeholder. Mint one
  (`manage-identifiers`) — TAPSO is a real buffer and a mapping candidate.
- ~~**"Self-inconsistent" collection headers**~~ — **the original header was
  right; the reconcile briefly made it wrong.** `total_count: 1879` against
  `mapped_count: 1877` + `unmapped_count: 0` does not sum, but that is accurate,
  not inconsistent: 2 records are `mapping_status: REJECTED`, and
  `IngredientCollection` is closed with no slot for other statuses. PR #167
  recomputed `unmapped_count` as `total − mapped`, which relabelled those 2 as
  UNMAPPED — asserting something false. Corrected in the #172 fix, which counts
  each status explicitly and prints a note when they legitimately do not sum. The
  2 records (`Bacto_Soytone.yaml`, `Sodium_L-lactate.yaml`) are filed as #170.
- **Stale derived indexes:** `data/curated/mapped_ingredients_index.csv` (line 410)
  and `…_index.json` still carry `CHEBI:48601` for Carnitine Hydrochloride, whose
  identifier was corrected to `kgmicrobe.compound:carnitine_hydrochloride` (the
  collection YAML is right; only the indexes lag). Regenerate them.
- ~~**`data/collections/` is a dead March-2026 pair**~~ — **DONE (#169, PR #179).**
  Retired: the directory is deleted, `just aggregate-collections` is removed, and
  `--output-dir` / `--aggregated-dir` are now **required** rather than defaulted.
  Defaulting them to `data/curated/` instead was rejected — that turns a stray
  command into a data change.

**The issue's item 1 is now CONFIRMED and is worse than "stale files" — it is a
data-destroying landmine. Measured 2026-07-30, once PR #159 made a full export
safe to run.** A `just export-individual` on current `main` reverts **67 files**
(197 insertions, 472 deletions). The losses are not cosmetic:

| curation action silently reverted | count | curator |
|---|---|---|
| `RECLASSIFY_INGREDIENT_TYPE` (`UNDEFINED_MIXTURE` → `DEFINED_MEDIUM`) | 53 | `cbclaw_media_modeling_114` |
| `FLAGGED_NON_INGREDIENT` | 2 | `cbclaw_followups_114` |

These are exactly PR #116's 53 media reclassifications. They were written to the
per-record files and **never aggregated back into `data/curated/`**, so the
collection still says `UNDEFINED_MIXTURE` and the export — which treats the
collection as the source — undoes all 55 curation events and drops their history
entries. `promote_resolved_unmapped.py` calls `just export-individual`, so **any
routine promotion would have silently reverted them.**

**Root cause (found 2026-08-02): the reverse half of the round trip never fed
back.** `aggregate_records.py` defaults `--output-dir` to `data/collections/`,
but *every* one of the ~20 consumers in the repo reads `data/curated/`. Nothing
reads `data/collections/`: the only references are the aggregator's own default,
`verify_roundtrip.py`'s, and two `notes/` docs that documented the stale
comparison as the way to do it (docs fixed in PR #167; the defaults themselves
retired in PR #179 — both options are required now, so no code path silently
writes to or reads from a directory nothing consumes).
So a per-record edit had no path back into the export
source, and `verify_roundtrip.py` — which would have caught this and already
exits 1 on mismatch — was comparing against an artifact last regenerated in
March 2026. It was never wired into CI. `just aggregate-collections` was
therefore *not* the fix: on its own it writes to the dead end.

**FIXED 2026-08-02 (PR #167).** Two halves:

1. **Data reconciled.** Applied surgically (record and key order preserved, only
   drifted fields touched) so the diff stayed reviewable: 55 unmapped records
   gained `ingredient_type`/`curation_history`/`notes`; the 3 orphans were
   dropped. Headers were also recomputed, and **that part was a mistake** — see
   the header bullet above; `unmapped_count` was set to 2 when the 2 records are
   `REJECTED`, not UNMAPPED. Reverted to 0 in the #172 fix, which counts each
   status explicitly. `discussions` deliberately stays out of the
   collection. 12 per-record files were also normalised — line wrapping and
   scalar quoting only, verified semantically identical by parsing both sides and
   stable across three consecutive exports. **`just export-individual` is now a
   true no-op.**
2. **Guard added so it cannot recur.** `just qc-roundtrip` (now part of `just
   qc`) and `.github/workflows/qc-roundtrip.yaml` aggregate into a *temp* dir —
   never a committed artifact — and verify against `data/curated`; CI also
   asserts that `export-individual` produces no diff. `verify_roundtrip.py`
   gained `--ignore-fields` (default `discussions`) and no longer stops after the
   first mismatch per file. Verified the gate **fails** as well as passes:
   reverting `data/curated` exits 1, and a single-field change with counts left
   unchanged is caught and pinpointed.

**The 53 reclassifications were validated before being made canonical.** All are
named standard culture media. `Oatmeal agar` appears **verbatim** in the schema's
own `DEFINED_MEDIUM` examples, and `Marine broth 2216` is the broth counterpart
of its `Marine agar 2216` example (same DSMZ 2216 formulation, solidified or
not) — a near-match, not a verbatim one. MediaDive REST confirms
the 8 contested "Base" products carry no formula/CAS/ChEBI (formulations, not
chemicals). Three independent Edison/PaperQA3 runs on the hardest cases — Blood
Agar Base (incomplete base), Soil+Seawater Medium (natural-substrate, genuinely
variable components), Leptospira Medium Base EMJH (supplement-dependent base) —
**each independently confirmed `DEFINED_MEDIUM`**. Reports under
`research/ingredients/` (gitignored).

⚠ **All three runs independently flagged the same schema hazard** — see the new
item 10 below.

## 4. Flip `plausibility_severity: warn` → `error` — DONE (2026-07-30, PR #159)

`conf/id_label_targets.yaml:60` ships `plausibility_severity: warn` with the
comment "Flip to `error` once the backlog clears -- the same report-then-enforce
rollout the base gate used." The gate (enabled in #155 on the `mapped_csv` target
via `label_waiver_mode: plausible`) is currently report-only: the validator
discards `IMPLAUSIBLE_LABEL` from `error_verdicts` when severity is `warn`
(`scripts/validate_id_label_correspondence.py:745-748`).

**The backlog it was waiting on was already empty**, so the flip cost nothing.
`conf/id_label_targets.yaml` now carries `plausibility_severity: error`, and
`just validate-products` still exits 0 (OK_CANONICAL 5034 / OK_ID_ONLY 1667 /
OK_EXCEPTION 16 / SKIPPED_NO_ADAPTER 3357, no implausible pairs). An implausible
id↔label pair is now build-breaking rather than merely reported. Only the
per-repo config changed — `scripts/validate_id_label_correspondence.py` is
vendored and drift-checked, so its `severity != "error"` logic was left alone.

## 5. Run the ingredient-role research pipeline — all tooling merged, never run

The role thread was absent from this file entirely. The schema migration is
**complete** (#120 rename → #129 three facet enums → #130 assignment classes,
slots, writers → #133/#134/#135/#143 polish → #139/#141 retirement of the flat
`IngredientRoleEnum`/`RoleAssignment`/`media_roles`, migrating 987 assignments
across 906 records). The research lane is **built but has never been executed**:

- MIM #146 — role research template + Edison shim + `template_vars()`.
- MIM #153 — `scripts/apply_role_research_results.py`.
- MIM #178 (2026-08-04) — the applier now writes its edits back into
  `data/curated/` and re-exports, so a run leaves the two surfaces consistent.
  Before this, every applied role would have been reverted by the next
  `just export-individual` (#171) — the lane was not safely runnable.
- CultureMech #105/#106/#107 — cross-repo prioritizer, Edison extractor,
  `apply_ingredient_roles.py` + the `research-ingredient-roles` skill.

Evidence it has not run, re-verified 2026-08-04: `research/ingredients/roles/`
(the shim's fixed output dir) does not exist; there is no
`reports/edison_role_extraction.json`; and **0** records carry
`edison-deep-research` provenance.

Current coverage over 2,257 records: **898 (39.8%) carry ≥1 ingredient-facet
role**, all of them mapped records (47.8% of the 1,879); **0 of 378 unmapped**.
Per slot — `nutritional_roles` 622 records / 716 assignments,
`physicochemical_roles` 268 / 269, **`cellular_metabolic_roles` 9 / 9**. All 994
assignments are `COMPUTATIONAL_PREDICTION` (698) or `DATABASE_ENTRY` (283):
**no literature-cited evidence exists yet**, which is precisely what this lane
was built to supply, and `cellular_metabolic_roles` is the facet it should fill.

Order of operations (per the CultureMech skill's documented merge order):

**Both lanes are driven from CultureMech, not from here** (confirmed 2026-07-30:
`scripts/backfill_ingredient_roles.py` and `scripts/audit_missing_roles.py` are
CultureMech files, added by its #95 and present on its `origin/main`; MIM only
supplies the Edison shim, the research template, and the applier). Schedule the
run there. Note the local CultureMech checkout is on `validate-media-recipes`,
61 commits ahead of its origin, and those two scripts are missing from its
working tree despite being at `HEAD` — sort that checkout out before running
anything.

1. **Mechanistic lane first** — CultureMech's `backfill_ingredient_roles.py`
   (#95) derives facets from CHEBI `has_role` via OAK. It is dry-run-only and its
   output was never applied. Cheap, deterministic, no Edison spend. Its
   2026-07-20 audit baseline: 143,651 ingredient descriptors MIM-mapped but
   missing all three facets.
2. **Then the literature lane** — CultureMech prioritizer → MIM
   `just research-ingredient-roles-edison-batch` → CultureMech
   `extract_roles_from_edison.py` → MIM `just apply-role-research-results` +
   CultureMech `apply_ingredient_roles`. Needs an Edison budget decision.

**Carry CultureMech's #107 lesson across before the first live run:** its applier
wrote a `fields_changed` key that is not a slot on `CurationEvent`, and because
`validate-strict` runs linkml-validate with `closed=True` the first live apply
would have failed CI on every record it touched — latent because the PR shipped
no data. MIM's `apply_role_research_results.py` should get the same treatment:
at least one test that validates its emitted YAML against the schema. Also
inherited: enum validation of role tokens lives only in the *extractor*, so a
batch produced with `--no-validate` or hand-edited can carry invalid tokens all
the way to `validate-strict`.

`community_organism_roles` being 0 is **not** a gap — it is an organism-level
slot, explicitly handled as such in `scripts/validate_roles.py:97`. No action.

## 6. Stale precedence columns in `UNIFIED_INGREDIENT_MAPPING.tsv` (#138)

kg-microbe's loader picks the primary CURIE with
`best_primary([chebi_id, culturemech_term_id, mim_id, kg_microbe_node_id, cas_rn])`,
and within one prefix the *first* candidate wins. Three rows had a correction
written to `kg_microbe_node_id`/`mim_id` while the superseded id stayed in the
higher-precedence columns, so the consumer re-asserts the stale grounding on
every run. Verified unchanged on 2026-07-30:

| ingredient | `chebi_id` | intended (`kg_microbe_node_id`/`mim_id`) | `culturemech_term_id` |
|---|---|---|---|
| 4-Aminobenzoic acid (line 167) | `CHEBI:194474` stale | `CHEBI:30753` | `CHEBI:194474` stale |
| Cobalamine | `CHEBI:30411` stale | `CHEBI:28911` | `CHEBI:30411` stale |
| Infusion from Potatoes (line 3908) | — | `UNMAPPED_0251` | `FOODON:03316428` "Peptone" — a mis-annotation |

The PABA variant rows (`p-Amino Benzoic Acid` line 1040, `p-amino benzoic acid`
line 3346) have partly moved on since the issue was filed — they now carry
`CHEBI:30753` and status `MAPPED` — but still hold `CHEBI:194474` in both stale
columns.

**Do not hand-edit the TSV.** It is a generated artifact; `build-unified-mapping`
copies `workspace/unified_ingredient_mapping.tsv` over it, so an edit regresses
on the next refresh. The fix has to land in the CultureMech source record or in
the builder's column precedence. Worth saying so in the issue. Not blocking —
kg-microbe already runs a retraction pass, so the published graph is clean.

## 7. PubChem-derived `cas_rn` false-positive audit — DONE (2026-08-06, PR #289; #114 closed)

PR #289 ran the CAS audit alongside the non-chemical disposition and the 61 stock
solutions, and #114 is now closed. #287/#290 additionally tightened the `cas_rn`
pattern so EC/EINECS numbers can no longer be written at all. Retained below for
the record.

### original entry

#114 is a 75%-done tracker that still reads as fully open. Three of its four
follow-ups have landed (peptone→MICRO grounding, the Carnitine Hydrochloride
`CHEBI:48601` → `CHEBI:17126` correction, and the non-chemical disposition,
re-scoped and half-shipped in #116 as 53 `UNDEFINED_MIXTURE` → `DEFINED_MEDIUM`
reclassifications). **The one genuinely open item has no PR and no tooling:**

`fetch_cas_rn_from_pubchem` mis-assigned CAS `103-47-9` to Beef extract — that
CAS is CHES (`CHEBI:44302`), a name-lookup false positive. Cross-check
`chemical_properties.cas_rn` corpus-wide against CHEBI / expected formula, most
valuable on `UNDEFINED_MIXTURE` and other complex records. Medium size; needs
PubChem/CHEBI network lookups, no upstream dependency.

Recommend closing #114 and opening a narrow issue for just this audit. Note that
residual `CHEBI:48601` strings survive in three review scratch files
(`mappings/ingredient_mappings_oak_ols_review.tsv:485`,
`…_synonym_enrich_review.tsv:116`, `…_row_review_manifest.tsv:484`) — harmless,
but they will trip a naive grep audit.

## 8. Web design review residue (#110) — cosmetic, 2 of 3 actionable here

Nine items shipped in #108/#109/#111; three remain, all confirmed present:

1. **Meaningless axes on the force-directed graph** —
   `docs/ingredient_graph.html:552-575` draws `d3.axisBottom`/`axisLeft` labelled
   "Dimension 1"/"Dimension 2". Force-simulation coordinates have no scale, so the
   axes are decorative and actively misleading. Small: delete the two axis groups,
   keep zoom/pan.
2. **Theme-toggle repaint lag** — `docs/theme-toggle.js` flips `data-theme` and
   persists it but emits no repaint signal. The viz pages only re-read CSS custom
   properties inside their `resize` handler (`ingredient_graph.html:486`, :704),
   with no `MutationObserver` on `data-theme`, so JS-drawn colors stay stale until
   the window is resized. Small: observe the attribute, call the existing redraw.
3. **Token-system divergence** — `docs/index.html:8-15` uses a pastel token set
   (`--pastel-a`, `--accent`, `--ink`, …); `docs/ingredient_umap.html:8-19` and
   `ingredient_graph.html:8` use a disjoint slate set (`--primary`, `--surface`,
   `--text`, …). Only `#7E5BC4` is shared, under two different names. Every dark
   rule is also duplicated per page (`:root:not([data-theme="light"])` +
   `:root[data-theme="dark"]`, ~55 lines each, e.g. `browser.html:294-348`).
   **Cross-Mech** — `theme-toggle.js` is vendored byte-identical across all Mech
   sites, so unifying tokens unilaterally would desync MIM. Coordinate in claw.

## 9. Small cleanups

- **`enrich_edison_response.py` non-recursive glob** (deferred in #146): the
  default `DEFAULT_RESEARCH_DIR` pattern `*-edison-*-meta.yaml` is non-recursive,
  so it will not see `research/ingredients/roles/` unless `--research-dir` is
  passed. Verified still non-recursive on 2026-08-04
  (`scripts/enrich_edison_response.py:270` uses `.glob()`, not `.rglob()`).
  More urgent since #178: the applier now syncs correctly, so the lane is
  genuinely runnable and this is the next thing in its path.
- **`.claude/skills/ingredient-roles/SKILL.md` is pre-facet** — it documents the
  retired flat lowercase role names (`carbon_source`, `buffer`) with no mention of
  the three facets or the Step 7b lane. The facet-aware skill exists only in
  CultureMech (`.claude/skills/research-ingredient-roles/SKILL.md`). Modernize or
  point at it.
- **`docs/ROLE_CURATION_WORKFLOW.md`** carries a 2026-03-15 stats snapshot
  (446 ingredients / 996 mapped). It is honestly labelled "before the #128 facet
  migration" and points at `scripts/validate_roles.py` for current numbers, so
  this is cosmetic; the "Future Enhancements (Phase 5)" section (lines 399-420)
  describes a manual DOI-review workflow that Step 7b supersedes.
- **`chemical_properties` residual is the ceiling, not a task.** The enricher was
  repaired in 2026-06 (OLS4 renamed its annotation keys: `formula` →
  `generalized_empirical_formula`, SMILES/InChI → `*_string`). The remaining ~83
  missing-formula records are abstract CHEBI classes, polymers, proteins,
  complexes and minerals that legitimately have no single empirical formula.
  Re-run any time with `python scripts/enrich_chemical_properties.py`
  (idempotent), then `just export-individual`. Gotcha still live: OLS4 needs
  **double** URL-encoding of ChEBI IRIs.
- ~~**`dashboard/` was last generated 2026-07-19**~~ — stale claim; it was
  regenerated 2026-07-31. Still worth a `just gen-qc-dashboard` after item 5,
  since role coverage is what it charts.

## 10. `DEFINED_MEDIUM` reads as "chemically defined" — schema hazard — DONE (2026-08-04, PR #216, closes #168)

**Shipped 2026-08-04 (PR #216).** Took Option 1 (description-only): the
`IngredientTypeEnum.DEFINED_MEDIUM` description now states explicitly that
"DEFINED" denotes RECORD GRANULARITY (a complete *named* medium, not a single
ingredient), is NOT the microbiology term of art "chemically defined medium", and
that complex undefined components are expected; the compositional distinction is
carried by `UNDEFINED_MIXTURE`. The compact inline restatement and the 3 affected
LinkML docs were updated too. Enum **values unchanged** → no data migration, no
effect on the 53 records or kg-microbe. `validate-schema` clean. **The rename (the
honest fix) is deferred cross-Mech as #222** — CultureMech imports these enums, so
it needs coordination + a migration.

Original finding, kept for context:

Surfaced independently by **all three** Edison/PaperQA3 runs during the #148
validation (2026-08-02), each unprompted and each phrasing it as a warning:

- Blood Agar Base — "`DEFINED_MEDIUM` should be understood as the project's
  named-medium record type, **not a claim that every molecular constituent and
  concentration is chemically specified**."
- Soil+Seawater Medium — "may be retained if it means 'complete named medium,'
  but **it must not be interpreted as 'chemically defined medium'**."
- Leptospira Medium Base EMJH — "'defined' **should not be interpreted as
  chemically defined**."

In microbiology "defined medium" is a term of art meaning *chemically* defined
(every constituent known and quantified) — the opposite of the complex digests
and extracts these records contain. MIM's enum means "complete named medium
formulation", which the schema *description* supports ("Complete medium
formulation or recipe with multiple ingredients … Should cross-reference to
CultureMech for full recipe") but the enum *name* actively contradicts. 53
records now carry this value, and kg-microbe consumes it.

Low-risk fix: sharpen the `DEFINED_MEDIUM` description to say explicitly that it
denotes record granularity (a complete named medium), not chemical definedness,
and that complex undefined components are expected. A rename is the honest fix
but is cross-repo (CultureMech imports MIM's enums) and would need coordination —
weigh against the description-only change. Note `UNDEFINED_MIXTURE` sits in the
same enum and *does* carry the compositional meaning, which is what makes the
pair misleading.

## 11. Follow-ups filed during the guard work (2026-08-03/04)

Five issues opened while closing #148/#164/#169/#171/#176/#181/#185. Each was
filed rather than guessed because the fix needs a decision, not a keystroke.

- **#186 — `just enrich-with-hierarchy` exists in no repo.**
  `.claude/skills/ingredient-roles/SKILL.md` names it as the CultureMech hand-off
  for propagating MIM role changes into the ingredient hierarchy. It is not in
  CultureMech's `justfile` or `project.justfile` (closest: `enrich-with-chebi`).
  **Blocks item 5's tail** — this is the step that follows a role-research batch.
  Suppressed in `conf/instruction_refs.yaml` with a pointer; remove that entry as
  part of the fix.
- **#187 — `data/curation/flagged_duplicates.yaml` never existed.**
  The merge-ingredients skill tells curators to record flagged duplicates there.
  **Blocks item 2** — the 61 duplicate PKs will produce exactly those
  flagged-not-merged cases. Candidate homes now exist that did not when the skill
  was written: a `Discussion(kind=OPEN_QUESTION)` on the surviving record, or a
  `history/` record. That is a curation-workflow call.
- **#177 — "CI blocking" is aspirational.** `main` has no branch protection, so
  no check is actually required; several gates describe themselves as blocking.
  Needs a policy decision *and* repo-admin action, and note that several
  workflows carry `paths:` filters, so a required check that never runs blocks a
  PR forever.
- **#182 — `just export-individual` relies on implicit default directories.** Not
  a bug (the defaults are correct) but the same shape as the pattern #169
  retired. Either pass them explicitly or comment that they are load-bearing.
- **#183 — `just sync-individual` has no caller**, and its trailing
  `qc-roundtrip` can only ever pass, because the first step makes the two
  surfaces agree by discarding one of them. Delete it, or rename it to say the
  collection wins.

## 12. microbedecoder unmapped-labels onboarding + residual grounding — LARGELY DONE

Closed since the last pass: #196 (PR #286), #203 (#269), #204, #207 (#282), #208
(#274), #212, #213 (#275/#277/#280/#281/#283/#284), plus #249/#263/#273/#279.
**Still open: #206** (check-chebi-currency infers 'a refresh would help' from byte
size, not release — note the check now prints the correct verdict, so this may be
fixed in place; verify) and **#209** (is microbedecoder 'sodium(+)' a media
ingredient, and relabel `Sodium().yaml`). Original entry follows.

### original entry

An entire thread that was absent from this file. kg-microbe's `microbedecoder`
transform emits `unmapped_labels.tsv` — 5,224 free-text labels it could not
ontology-map. Staged into MIM at `data/custom/microbedecoder/` and onboarded.
Only ~1,023 rows are chemical/ingredient candidates; the other ~4,200 are numeric
phenotype measurements, isolation-category environment/host/food context, enzyme
names, and metabolic pathways — **out of ingredient scope by design**. Assessment:
`notes/microbedecoder_source_assessment_2026-08-03.md`.

**Shipped (all 2026-08-04):**

| PR | what |
|---|---|
| #193 | Onboard the labels; hold 386 auto-groundings at PENDING_REVIEW |
| #194 | Track the review manifest (`reports/` gitignored) |
| #195 | Promote the 386 reviewed auto-groundings to MAPPED |
| #205 | Restore 11 antibiotic records demoted on the accession-ceiling false positive (closes issue #198; the other 6 stay upstream-blocked) |
| #202 | Deep-research the deferred residual: **3 net-new applied** (Diacetyl→CHEBI:16583, Ferric Iron→CHEBI:29034, Sodium(+)→CHEBI:29101); 7 reclassified as already-mapped synonym-merges; blends + antibiotics deferred. Report + ledger + 43-label decomposition table under `mappings/microbedecoder_residual_research_*` |
| #211 | Recover **22 free** exact/synonym groundings orphaned when PR #201 was closed unmerged (sugars, amino-acid/peptide substrates, nitrophenyl enzyme substrates, acids/ions/polymers, 2 dropped-locant chloroalkanes) |

**PR #201 was CLOSED unmerged** (it was stacked on `review/microbedecoder-pending-groundings`,
not `main`). Its content reached `main` piecemeal — 386→#195, antibiotics→#205,
20+2 free groundings→#211, deferred-NCIT→#202 — but the source branch
`feat/microbedecoder-residual-grounding` (worktree `MediaIngredientMech-residual`,
tip `80d9b010`) still holds a few unmerged bits:
`scripts/promote_microbedecoder_residual.py`, the blends/deferred-NCIT triage
TSVs, and 4 duplicate-synonym merges + NEEDS_EXPERT flags. **Do not delete that
branch** — it feeds the active work below.

**Active parallel work (a second session, 2026-08-04):** branch
`fix/microbedecoder-residual-merges-blends` (worktree `MediaIngredientMech-merges`),
running Edison literature searches on the blends. **Stay off that branch/worktree.**

**Remaining — tracked, ~583 `UNMAPPED_*` placeholder records still unmapped;
consolidated in #213:**

- **#212 — follow-up on #211 (verified accurate).** 4 records need a synonym-**merge**
  (`merge-ingredients`), not a promote, because their CHEBI targets are already
  mapped via *other* records so `promote_resolved_unmapped.py` correctly skipped
  them: `2-dichloropropane`→CHEBI:142468, `2-trichloroethane`→CHEBI:36018,
  `1% Sodium Chloride`→CHEBI:26710, `1% Sodium Lactate`→CHEBI:75228. #211's body
  called them "already present" — the *targets* are; the source placeholders are
  not. These are exactly the merges #201's `80d9b010` had staged.
- **#208** — 7 already-mapped labels need synonym-merges onto the canonical record
  (alpha-/beta-hydroxybutyrate=2-/3-hydroxybutyrate, Achromycin=Tetracycline,
  neomycin E=Paromomycin, (+)-D-glycogen=Glycogen, (+)-L-lyxitol=Arabitol); the
  **RNA→CHEBI:33697 case needs a split** (generic RNA vs the Torula-yeast product
  record already on that id).
- **~43 multi-component blends / co-substrate pairs** — decomposition strategy
  researched in #202 (`mappings/microbedecoder_residual_research_decomposition.tsv`);
  the active second session is working these. Gaps flagged: rumen fluid (#204,
  verify `MICRO:0000520`), corn steep liquor (no FOODON/CHEBI term), the TYGVS VFA
  mixture.
- **6 out-of-coverage antibiotics** — **5 of 6 RESOLVED** (verified 2026-08-07,
  re-grounded during the microbedecoder residual work, not by a build refresh).
  All six are MAPPED with ids that resolve against the local builds, labels
  canonical, none deprecated: carbomycin → `NCIT:C166659`, colistin sulfate →
  `NCIT:C386`, lysostaphin → `NCIT:C166895`, polymyxin B → `NCIT:C61894`,
  netilmicin → `CHEBI:7528` (the duplicate record was merged in; the surviving
  file is `Netilmycin.yaml`). The published SSSOM and `docs/data/` carry those
  ids and **zero** occurrences of the six dead accessions — they survive only in
  `curation_history` prose (correct: that is the audit trail) and in the
  microbedecoder working manifests under `mappings/`.
  **#207 CLOSED by curator ruling (2026-08-07): NCIT is correct.** These five
  are FINAL groundings, not stopgaps waiting on a build refresh — a term MIM can
  resolve and label-check is the better published mapping, and that judgement
  does not expire when the build catches up. Gentamicin's earlier "should move
  back to `CHEBI:759884` once the build carries it" intent is **superseded**:
  `CHEBI:17833` resolves, so the ordinary source preference
  (`curie.py::PREFIX_RANK`, CHEBI above NCIT) already selects it — the four NCIT
  groundings are that same rule working, not an exception to it.
  This mattered because all six displaced accessions **do** exist in kg-microbe's
  own ChEBI 253, so a future sync against the consumer's ontology would have read
  as an invitation to "restore" them. Each of the five now carries a
  `CURATOR_RULING` curation event saying not to, applied by
  `scripts/apply_ncit_grounding_ruling.py` (idempotent; refuses if a record has
  moved off the grounding being ruled on). The general rule — *a term you cannot
  resolve is not a candidate; ground to the next ontology that has one and treat
  it as final* — is written up under **Ontology Selection Guide** in
  `.claude/skills/map-media-ingredients/SKILL.md`.
  The upstream lag itself is unchanged and still true (build **252** vs ChEBI
  **253**, refresh is a no-op because the published semsql artifact is
  byte-identical) — it is simply no longer blocking anything here.
- **#209** — is `sodium(+)` a media ingredient (vs a phenotype), and relabel
  `mapped/Sodium().yaml` → `sodium(1+)`.
- **#196** — microbedecoder records carry `total_occurrences: 0`; the source
  occurrence signal (present in `unmapped_labels.tsv`) is dropped on import.
- The bulk remainder plus the ~347 **isolation-category** environment/host/food
  rows should route to **ENVO/FOODON**, not the ingredient pipeline; keratin →
  Protein Ontology (no CHEBI term).

**Related infra issues (accession ceiling / currency):** #210 **CLOSED** — the
CHEBI ceiling was 300000 while ChEBI reaches 747618, so valid recent terms were
reported as foreign ids; raised to `1000000` in PR #302, matching
`curie.py::MAX_ACCESSION`, with the two tables now pinned in sync by test. Still
open: #303 (the vendored validator still states the conclusion in comments and
attaches no `detail` to the verdict — needs a CultureMech-first change, tracked
there as CultureMech#247), #304 (the ceiling can now only fire on 8-digit ids, so
`ID_OUT_OF_RANGE` is narrower than its name suggests), #206
(`check-chebi-currency` infers "a refresh would help" from byte size, not
release), #203 (`promote_microbedecoder_reviewed.py` approval check is
tautological — re-runs the lookup that created the mapping).
**#249 CLOSED** (2026-08-07) — it reported six UNMAPPED records whose primary key
was a nonexistent CHEBI id. None of the six ids is any record's identifier today;
all six records are MAPPED to ids that resolve. Re-verified rather than assumed,
because #249 was itself filed as an off-by-six correction to #248. **#207 CLOSED**
(2026-08-07) by curator ruling — NCIT is correct and these groundings are final;
see the antibiotics item above.

---

## 13. Two-lane deep-research validation + the curation arc it produced (NEW — 2026-08-13)

**What**: every ingredient record was validated against two independent research
lanes — Edison/PaperQA3 (literature; cannot open ontology pages) and a Claude
lane resolving CURIEs directly against OLS4/ChEBI/PubChem (PR #309). The
disagreements it surfaced became issues #315–#334, and working those produced
~20 further PRs. **54% of Edison flags were false alarms**, measured over 243
adjudicated records — do not treat a flag as a defect.

**Closed by this thread**: #319 (protonation policy), #320 (84 CAS-vs-CURIE
conflicts), #322, #326(a), #342, #346, #352.

**The reusable findings**, each of which cost real time to establish:

* **Ancestry beats heuristics for CAS-vs-CURIE conflicts.** Asking whether the
  CAS's ChEBI term is a *descendant* of the record's term reclassified 49 of 84
  #320 flags as benign registry granularity (`Arginine` → `arginine`, CAS →
  `L-arginine`). Structurelessness — the heuristic tried first — cuts across all
  three ancestry classes and can never discriminate.
* **ChEBI does not subsume hydrates, salts, racemates or conjugate bases.** It
  files hydrates under `CHEBI:35505 hydrate`, never under the anhydrous form.
  That is why those relations surface as "unrelated" in any ancestry test, and
  it is what #342 decided (74 records → `skos:closeMatch`).
* **Duplicate shadowing is the root cause behind #315/#334/#320.** A notation
  variant the merge pass does not recognise (`·` vs ` x `, `Na2-EDTA` vs
  `Na2EDTA`, one letter of case) escapes dedup and is then grounded to the
  nearest lexical match — usually the anhydrous parent or a false friend.
* **A derived CAS is not independent evidence.** `KF` → `Lys-Phe` and `D` →
  aspartate both survived CAS-vs-CURIE checking because the CAS was fetched
  *from* the wrong CHEBI term. Check `curation_history` for "via CHEBI:…" before
  treating agreement between the two fields as corroboration.
* **Count hydrate water by element totals, not string matching** (#349). The
  string test was wrong four separate ways, the worst being that
  `InChI=1S/Cu.H2O4S/…` contains `.H2O` as part of the *sulfate* fragment, which
  silently skipped every sulfate hydrate. `scripts/check_hydrate_water.py --check`
  now gates it.

**Still open from this thread:**

* **#344** — 9 labels state a hydration number with no known hydrate. Source
  found: MediaDive's REST API carries all 9 **verbatim**, so the earlier
  "sulfate→chloride slip" hypothesis is **disproven**. MediaDive gives all 9 the
  *anhydrous* formula/mass/CAS and `MgCl2 x 7 H2O` has no CAS at all. Needs a
  decision on whether MIM keeps the constructed hydrate formula, reverts to
  anhydrous, or clears the field. Publishes into `docs/data/`.
* **#356** — record `X`, **101 occurrences**, mapped to `NCIT:C189218`, defined
  as "The 24th letter of the English alphabet". Needs the source media (history
  says `samples: Wolf…`), not chemistry. The mapping should not stand regardless
  of what `X` turns out to be.
* **#321 residual** — 44 hydrate records whose labels state no stoichiometry.
  Verified unresolvable from the label, ChEBI, **and** PubChem's entry for each
  record's own CAS; MediaDive has none of them. Needs a supplier catalogue or the
  original recipe text. `missing` is 0; these are `unknown`, not defects.
* **#336** — 55 SSSOM rows whose predicate contradicts the record's
  `mapping_quality`. Untouched by this thread.
* **Edison lane is blocked** at 1,145/2,841 records on HTTP 402 (account out of
  credit). `scripts/run_research_shard.sh` exits 3 on account-level refusals and
  will not retry, so a top-up resumes it cleanly.

## 14. Unblock `just publish-sssom` — the row-count guard is firing on a subject-spelling defect, not a policy gap (#416) (NEW — 2026-08-21)

**This is the top of the queue**: `mappings/ingredient_mappings.sssom.tsv` is the
artifact kg-microbe re-syncs, and nothing curated since 2026-08-20 can reach it
while promotion is refused. Reproduce in `culturebotai-claw`:

```
just build-sssom          # -> workspace/reports/mim_ingredient_mappings.sssom.tsv
just publish-sssom-dry    # -> Refusing to promote: row count would drop from 2938 -> 2885
```

Measured 2026-08-21 against MIM `62af3ebf` / claw `d70988a`:

| | |
|---|---|
| published rows | 2,938 |
| rebuilt rows | 2,885 |
| published-only `(subject, object)` | 155 |
| rebuilt-only `(subject, object)` | 102 |
| **predicate flips on shared keys** | **0** — #409/#415 fixed this half |
| rows sharing key+predicate but differing elsewhere | **~1,900** — see note |
| published subjects / rebuilt subjects | 2,512 / 2,512 |
| subjects present in one side only | **82 lost / 82 gained** |

Coverage is *not* the problem. Both sides carry all 2,512 `MAPPED` records; the
54 records the builder reports as "skipped, no supported `ontology_id` prefix"
are exactly the 54 `REJECTED` tombstones, which is correct.

> **A `(subject, object, predicate)` diff does not mean "identical row".** Of the
> 2,783 rows that survive with the same key and predicate, roughly 1,900 differ
> in some other column: `source` 1886, `mapping_date` 1626, `other` 682,
> `mapping_justification` 203 (179 `LexicalMatching` → `ManualMappingCuration`),
> `confidence` 154, `object_label` 1. Most is legitimate rebuild output, but the
> guard was blind to all of it — a rebuild could rewrite every `object_label` and
> still report "unchanged". Fixed in culturebotai-claw#115; the one
> `object_label` regression it surfaced is #441.

### The finding #416 does not have: the rebuild is right and the published file is stale

`82 lost / 82 gained` is not a coincidence — they are the same 82 records under
two different spellings. **The rebuild carries the correct one.** Measured
against `src/mediaingredientmech/curie.py::mim_curie_for_stem`, the repo's own
canonical subject function, over the 2,566 files in `data/ingredients/mapped/`:

| | subjects NOT derivable from any real mapped/ stem |
|---|---|
| rebuilt | **0** of 2,512 |
| published | **82** of 2,512 |

So every subject the builder emits resolves to a file that exists, and 82
published subjects point at filenames that were renamed out from under them.
Two shapes, and in both the published spelling is the older one:

**65 casing** — the published file predates renames the corpus has already made:

| published subject | actual file on disk today |
|---|---|
| `MIM:ATCC_Wolfes_mineral_mix` | `ATCC_Wolfes_Mineral_Mix.yaml` |
| `MIM:EDTA_Stock` | `Edta_Stock.yaml` |
| `MIM:DAS_Vitamin_Cocktail` | `Das_Vitamin_Cocktail.yaml` |
| `MIM:BG-11_Trace_Metals_Solution` | `Bg-11_Trace_Metals_Solution.yaml` |

Note the *stems themselves* are scarred by item 1's `capitalize()` bug —
`Edta_Stock`, `Das_Vitamin_Cocktail`, `Bg-11_…` are exactly the corruption item 1
catalogues. PR #159 froze the filenames in place rather than repairing them, so
the SSSOM is now correctly reflecting a corpus whose filenames are wrong. **The
subjects are consistent; the underlying names still want fixing** — but that is
item 1's residue, not a reason to hold the SSSOM.

**17 paren escaping** — and here the published file is not merely stale, it is
**invalid**. `mim_curie_for_stem` escapes any character outside
`[A-Za-z0-9_.\-]` as `~HEX`, and `_CURIE_RE` (`curie.py:67`) rejects anything
else:

| published (violates `_CURIE_RE`) | rebuilt (conforms) |
|---|---|
| `MIM:(R)-lactate` | `MIM:~28R~29-lactate` |
| `MIM:Calcium(2)` | `MIM:Calcium~282~29` |
| `MIM:(-)-anisomycin` | `MIM:~28-~29-anisomycin` |

**11 published subjects fail the repo's own CURIE regex right now**, and the
rebuild fails 0.

### `just curie-validate` is a guard that is not guarding

The justfile comment reads *"Assert the published SSSOM satisfies the CURIE
standard"* (`justfile:603`). The recipe body is:

```
uv run python -m pytest tests/test_curie_normalizer.py -q --no-cov
```

It never opens `mappings/ingredient_mappings.sssom.tsv`. It exercises the
normalizer on fixtures, passes 19/19, and reports green while the published
artifact it claims to assert on carries 11 subjects that violate the very regex
those tests cover. This is the same defect class as the #178/#179/#180/#188/#189
thread — **file it, and make the recipe read the file.** It is also why #300
("no gate catches a published `MIM:` subject leaving the mapping set") stayed
open long enough for 82 subjects to drift.

### What is actually left to decide

Normalising subject spelling collapses the difference from 155/102 to **73
published-only / 20 rebuilt-only**, and *that* residue is the real #416:

* **67 of the 73** are `kgmicrobe.compound:<slug>` registry rows on records whose
  own identifier is a `cas:` CURIE — `MIM:3-Fucosyllactose →
  kgmicrobe.compound:3-fucosyllactose`, `MIM:Ammonium_Molybdate_Tetrahydrate →
  kgmicrobe.compound:ammonium_molybdate_tetrahydrate`, and 65 more of one shape.
  #416's question 1: *does a `cas:`-primary record also get a minted registry
  row?* The published file says yes; the builder emits only the `cas:` row. This
  is a genuine policy call worth 67 rows, and it is the **only** part of the
  blocker that needs a curator rather than a code fix.
* **5 published-only / 5 rebuilt-only `CHEBI:` rows**, plus 14 rebuilt-only
  `kgmicrobe.compound:` and 1 `cas:` — adjudicate individually.

### Order of work

1. **Make the guard set-based — #416's question 2 is well-founded and is now the
   critical path.** `publish_sssom.py` compares row *counts*, which is blind to
   155 out and 102 in; it should diff row *sets* on `(subject_id, object_id)` and
   report added / removed / re-spelled. Had it done so, this whole diagnosis
   would have been the guard's own output.
2. Settle the `cas:` + minted-registry-row question — 67 rows.
3. Adjudicate the ~10 residual `CHEBI:` rows.
4. Record the genuine relabels (e.g. `MIM:2-phenylethylamine` →
   `MIM:Phenethylamine_Hydrochloride`, #236) in
   `mappings/mim_curie_aliases.tsv` so a consumer holding the old subject can
   still resolve it. **This is required, not optional** — 82 published subjects
   are about to change and kg-microbe re-syncs the file.
5. Promote, bumping `mapping_set_version` / `mapping_date` (**#301** — both still
   read `2026-08-18` and nothing moves them).
6. Then fix `curie-validate` to read the artifact, and land #300's
   subject-survival gate, so the next drift is caught by CI rather than by a
   reconcile.

**Do not "fix" the builder to reproduce the published spellings.** It is already
honouring `mim_curie_for_stem`; the published file is the stale side.

> **Correction (2026-08-21, after this item was first written).** The paragraph
> above is right but was written without noticing that **#299 had already
> litigated the case cohort and decided the other way**, pinning all 64 spellings
> in `tests/test_published_mim_subject_case.py` as a deliberately literal table.
> Promoting the rebuild fails all 64. That test defers to **#236** — "are `MIM:`
> slugs paths or opaque identifiers?" — which was the real gate, not the registry
> policy question.
>
> #299's *stated* objection turned out to be narrower than its remedy: the
> renames "produced no alias trail … which would have left all 64 dangling",
> and `CURIE_STANDARD.md` §1 documents the filename-derived rule as the standard.
> **#236 was settled on 2026-08-21 in favour of filename-derived**, the alias
> trail was supplied (`mappings/mim_curie_alias_seeds.tsv`, 82 seeds), the 64-row
> test was rewritten to pin *no published CURIE dangles* across all 2,512
> subjects, and the rebuild was promoted. **PR #436.**
>
> Lesson worth keeping: a backlog item that says "X is simply correct" should be
> checked against the test suite for a guard that says otherwise. The guard was
> there, named after the issue, and green.

**Related open issues this item subsumes or unblocks:** #416 (row-count
difference — its diagnosis needs correcting), #300 (no subject-survival gate),
#301 (version/date go stale), #236 / #293 / #307 (subject recomputed from
`preferred_term` rather than the stem — the MIM-side scripts still do this, and
they are what *creates* the drift the builder then faithfully reports).


# Upstream-blocked — do not schedule

## MICRO ids with malformed upstream IRIs (#137)

MicrO mints ~1,472 of its 3,450 classes under
`http://purl.obolibrary.org/obo/MicrO.owl/MICRO_nnnnnnn` instead of
`.../obo/MICRO_nnnnnnn`, so the CURIE does not round-trip and OLS4 reports
`is_defining_ontology: false`. Three are published in
`mappings/ingredient_mappings.sssom.tsv` (verified live on 2026-07-30, all
`skos:exactMatch`): `MICRO:0002250` V-8 juice (line 2168), `MICRO:0002392`
rabbit serum (1799), `MICRO:0002393` Proteose Peptone No. 2 (1760). The other 53
of 56 MICRO rows verify clean.

The quarantine is in place and self-policing: `KNOWN_BAD_MICRO` in
`tests/test_curie_normalizer.py:147`, applied at :160, with a companion assertion
at :171-172 that **fails once the ids start passing** — so the workaround cannot
silently outlive the defect. Detector: `just curie-verify-micro`
(`scripts/verify_micro_ids.py`).

Blocked on the MicrO build. The actionable-here alternative is re-grounding the 3
subjects to well-formed terms or dropping them to UNMAPPED — not obviously
better than waiting. **Triage warning: do not use PURL status to judge these.**
Term-level PURLs 404 for *all* of MicrO, well-formed or not; use
`is_defining_ontology` and the IRI shape.

## mesh.db — keep the 4 SCR exceptions (verified 2026-06-17)

`conf/id_label_targets.yaml` carries 4 `exceptions` for valid MeSH
supplementary-concept records absent from the cached `sqlite:obo:mesh`:
`mesh:C000709627` avocatin B, `mesh:C000655964` cholinium lysinate,
`mesh:C000730144` sodium glutarate, `mesh:C000633628` plicacetin.

A forced clean re-download (394 MB, byte-identical to the prior cache) confirmed
the 4 are **still absent** while older SCRs (e.g. C016600) are present — the
upstream semsql MeSH build excludes these recent (2020/2024) records. **Keep the
exceptions.** Revisit only if that build starts shipping C-prefix SCRs from 2020+;
then drop the matching entries and re-run `just validate-products` to confirm
OK_CANONICAL.

Related structural exception with no removal condition: `MICRO` sits in
`ignored_prefixes` rather than `adapters` because `sqlite:obo:micro` is a 0-byte
stub. Move it back once a real `micro.db` exists.

## DRC provider shim for role research (deferred in #146)

`scripts/research_ingredient_roles.py` (the deep-research-client counterpart to
the Edison shim) was deferred, blocked on an upstream refactor of the DRC runner's
hardcoded output path. The file does not exist. Edison covers the lane meanwhile.

---

# Reference ledgers — resolved, do not re-investigate

## Hard unmapped residual (378 records) — automated matching is exhausted

Verified 2026-06-14: only ~1 clean exact match across the whole residual.
It is specialized cobamides, flavonoids, natural products, element placeholders,
commercial media/broths/agars, trace-element and vitamin solutions, sera,
extracts, grains, buffers, and metal-NTA chelates. **Current count is 378
per-record files / 381 collection entries** (this file previously said 383 —
wrong in both directions; see item 3 for the 3-entry discrepancy).

> **Superseded as a total-unmapped count (2026-08-04).** This 378 ledger predates
> the microbedecoder onboarding (item 12), which added hundreds of `UNMAPPED_*`
> placeholder records. Total unmapped is now ~612 (~605 placeholders). This ledger
> still stands as the analysis of the *original, pre-microbedecoder* hard residual;
> for the current unmapped picture use item 12 and #213.

Use `deep-research-ingredient` (Edison/PaperQA3; `EDISON_PLATFORM_API_KEY` is
configured) or `mediaingredientmech-agentic-curation` (FutureHouse Falcon) for
source-backed identity and grounding, per record. 23 ingredients have been
Edison-researched so far; bundles live under `research/ingredients/` (gitignored).

**Migration recipe.** `scripts/promote_resolved_unmapped.py` automates the whole
multi-surface move (collection move + canonical-label lookup + SSSOM row inserted
in sort order + regen + verify), with a **PK-collision guard** that refuses to
create a duplicate CHEBI primary — redirect those to a merge. `--dry-run` by
default:

```
python scripts/promote_resolved_unmapped.py --identifier UNMAPPED_NNNN \
  --to CHEBI:NNN --quality EXACT_MATCH --evidence-source "…" --note "…" --apply
```

It handles exact/close only; narrow and broad matches need registry SSSOM rows
and must be hand-curated (see `Mg(NO3)2 x 6 H2O` below for the worked pattern).
The manual sequence it replaces, for reference: move + transform the record in
the collections → `just export-individual` → **hand-add the SSSOM row**
(`reconcile_sssom` reports the GAP but will not synthesize new-row provenance;
insert in the file's sort order by *decoded* subject label) → `just export-lists`.

**Outcome of five research batches.** Confirmed-unmapped-and-enriched is the
correct, defensible outcome for most of this residual — the compounds genuinely
lack clean ontology grounding.

- **Mapped:** `1-Naphtylacetic Acid` → CHEBI:32918 (a "naphtyl" misspelling
  string-matching missed) · `KNO2` → CHEBI:232610 · `Thioglycollic acid` →
  CHEBI:30065 · `Pyromelitic acid` → CHEBI:45165 · `NH42CO3` → CHEBI:229630
  (MediaDive CAS 10361-29-2, anhydrous).
- **Merged as typo-duplicates** (absorbed as RAW_TEXT synonyms +
  `MERGED_FROM_UNMAPPED_DUPLICATE`; a merge asserts no new SSSOM row, which
  honours Edison's "don't exactMatch a malformed label" caution):
  `alpha-ketoglutamate` → CHEBI:30915 · `KJ` (= Kaliumjodid) → CHEBI:8346
  potassium iodide · `Na2Mo4`/`Na2MoO7`/`Na2MoO7O4 x 2 H2O` → CHEBI:75213 ·
  `Na2WO2 x 2 H2O` → CHEBI:63939 · `Na2Se2O3` → CHEBI:48843 · `Na2S2SO3` →
  CHEBI:132112 · `MnCl4 x 4 H2O` → CHEBI:86368.
- **narrowMatch, hand-curated:** `Mg(NO3)2 x 6 H2O` as a **cas-primary**
  `cas:13446-18-9` "magnesium nitrate hexahydrate" with `skos:narrowMatch` →
  CHEBI:64736 (anhydrous parent) plus the two Rule-B1 registry rows. This is the
  pattern to copy when the helper refuses a narrow match.
- **Confirmed UNMAPPED, enriched in place — do not re-map:** the whole cobamide
  cluster (2-methyladeninyl / adeninyl / benzimidazolyl / 5-methyl- and
  5-methoxy-benzimidazolyl — Factor A, Factor IIIm, pseudocobalamin; upper-ligand
  ambiguity, **must not** map to cobalamin/B12) · `6-methylnicotinate` (carboxylate
  vs methyl ester ambiguity) · `Amphotericin` (spans A/B + formulations; do not
  exact-map to amphotericin B CHEBI:2682) · `7,2'-Dimethoxyflavone` and
  `7,4'-Dimethoxyisoflavone` (positional isomers; a closeMatch to a flavone parent
  would lose isomer specificity) · `2',2'-Bisepigallocatechin Digallate` ·
  `Fe(SO4)3 x n H2O` (candidate CHEBI:131387, but the label is malformed and `n`
  is unspecified; Fe sulfate hydrates are distinct CAS substances) ·
  `MnCl4 x 6 H2O` (non-standard hydrate, no CHEBI term) · `Se-acid` (MediaDive
  CAS 7783-08-6 = selen**ous** acid CHEBI:26642 but its `formula` field `H2O4Se`
  = selen**ic** acid — the conflict blocks a confident call).
- **Deferred, source-CAS-confirmed but CHEBI lacks the salt** (genuinely
  unmappable): cerium(III) nitrate hexahydrate (10294-41-4), chromium potassium
  sulfate dodecahydrate (7788-99-0), potassium phosphite `KH2PO3`
  (13977-65-6 — phosph**ite**, not phosphate), lanthanum nitrate hexahydrate
  (10277-43-7), sodium β-glycerophosphate pentahydrate (13408-09-8), sodium
  metasilicate nonahydrate (13517-24-3), neodymium chloride hexahydrate
  (13477-89-9), praseodymium chloride hydrate (19423-77-9).

**Method note that made batches 4–5 work:** these records carry
`source_id=mediadive.ingredient:NNNN`, so the **MediaDive REST API**
(`/rest/ingredient/{id}`) is authoritative — its `name`/`formula`/`CAS-RN` confirm
or refuse the intended compound even though MediaDive's own `ChEBI` field is null
for all of them. **Recipe context beats the ingredient record** when they
disagree: `KJ` was resolved because it sits among trace halide salts next to
KBr/NaBr in MediaDive media 1155 and 1727, while MediaDive *ingredient* 1042 is
corrupt (CAS 77-10-1 / "Phencyclidine") and an earlier review had wrongly flagged
it as a kilojoule unit.

## Cross-repo vendored-file sync — the sha256 pins are retired

**This replaces the old "validator pin guard" section, which described a
mechanism that no longer exists.** The self-generated sha256 pin compared a copy
against a hash from the *same* repo, so all four Mechs could pass while diverged.
It was retired in #156 (validator) and #157 (schema), and no `*.sha256` or
manifest files remain — only explanatory comments in the justfile and workflow.

Drift is now caught by `scripts/check_vendored_sync.sh` (dependency-free: bash +
curl + diff, byte-exact `cmp`), run by the **`vendored-sync`** job in
`.github/workflows/label-correspondence.yaml`. It covers **6 files** against
`CultureBotAI/CultureMech@<scripts/.vendored_canon_ref>` — currently
`6be694f3` — with public `CultureMech` as the hub by explicit governance choice,
not because of a visibility constraint:

`scripts/validate_id_label_correspondence.py` · `scripts/chem_formula.py` ·
`tests/test_id_label_empty_adapter.py` · `tests/test_id_label_unknown_prefix.py` ·
`tests/test_id_label_plausibility.py` · `src/*/schema/mech_shared.yaml`
(path-mapped to the hub's `src/culturemech/schema/mech_shared.yaml`).

**To propagate a change:** PR into the hub → merge → copy the changed files
byte-exact into this repo → bump `scripts/.vendored_canon_ref` to the new hub
commit **in the same PR**. The ref bump is the deliberate propagation act. The
hub's nightly `vendored-fleet-audit.yml` is the backstop.

**Settled topology — do not re-propose moving the canon into claw.** CultureMech
is the hub by design, not as a fallback for claw: claw's
`shared/idlabel/` is a passive *mirror* of it (claw #19). Making claw canonical
was tried and abandoned — claw #21 enforced it (merged 2026-07-22) and claw #22
reverted it (2026-07-25) as off-model for claw-as-mirror. Claw is public, but
that does not revive the abandoned plan. The single fleet audit in claw now
checks spokes and claw's mirrors against CultureMech; it replaced the two
overlapping audit jobs described in the original incident chronology.

**Known gap, now tracked as #160** (filed 2026-07-30): `scripts/chem_formula.py`,
`scripts/check_vendored_sync.sh`, `scripts/.vendored_canon_ref` and the
`tests/test_id_label_*.py` files are **not** in the workflow's `trigger_paths`,
so a PR touching only those does not fire the drift job. `conf/id_label_targets.yaml`
stays unpinned **by design** — it is intentionally per-repo (different adapters,
targets, exceptions), not a drift risk.

MIM is in better shape here than TraitMech: the `src/mediaingredientmech/schema/**`
glob does cover `mech_shared.yaml`, where TraitMech has no `src/**` path at all
(TraitMech#184). The four unlisted files are common to all three spokes —
CommunityMech#280 is the same defect — so fix it as one cross-Mech sweep
(`cross-mech-sync`), not three PRs. The suggested shape is to derive
`trigger_paths` from the same list `check_vendored_sync.sh` reads, so the filter
and the check cannot drift apart, which is exactly the failure this is an instance
of.

Severity is bounded: CultureMech's nightly `vendored-fleet-audit.yml` still catches
divergence within a day, so this is a PR-time hole rather than an unguarded one.
Do not confuse it with CommunityMech#278, which is about *what* is compared (the
checker has no canonical copy in the hub) rather than *when* the comparison runs.

Cross-repo companion status for #157 (CultureMech #112 plus the CommunityMech and
TraitMech spokes), confirmed from the hub on 2026-07-30: all three spokes — MIM,
CommunityMech, TraitMech — pin the same `scripts/.vendored_canon_ref`
(`6be694f3d6308ac0f4c2e0dcf196e2ff73f6468f`) against `CultureBotAI/CultureMech`;
CultureMech itself carries no ref because it *is* the hub. CultureMech's
`vendored-fleet-audit` has run green nightly through 2026-07-30.

## Adopt DisMech knowledge-gaps + datasets + QC dashboard (claw#7) — LANDED

Previously listed as pending; it has shipped. `src/mediaingredientmech/schema/mech_shared.yaml`
is vendored and drift-checked (see above) and defines `Discussion`,
`DiscussionKindEnum`, `DiscussionStatusEnum`, `Dataset`, `DatasetTypeEnum`,
`DatasetRepositoryEnum`. `mediaingredientmech.yaml` imports it (line 30) and
attaches `discussions` (line 244) and `datasets` (line 253) to `IngredientRecord`.
Recipes exist for all three slices: `just knowledge-gap-scan` (justfile:196, over
the shared `kg_microbe_kgscan`), `just gen-discussions-data` (:330), and
`just gen-qc-dashboard` (:189, rendering `dashboard/index.html` + `coverage.png`).
Supporting surface: `tests/test_export_preserves_discussions.py`,
`conf/discussions_config.yaml`, `conf/kgscan_config.yaml`, `app/discussions/`,
and generated docs.

**8 mapped records carry `discussions`** — these are exactly the population #144
and #151 were protecting (#144 fixed `export_individual_records.py` silently
wiping them on every export; #151 fixed the follow-on where indexing by
`identifier` dropped them on promotion/demotion/remap, since in MIM the identifier
*is* the CURIE). **0 records carry `datasets`**, which matches the original
assessment that MIM models none today. TraitMech marked its equivalent adoption
done by 2026-07-22; CultureMech's section is still open.

---

# Recently shipped (2026-07-05 → 2026-07-22) — recorded here for the first time

- **Role-facet migration** — #120 (rename `CellularRoleEnum` →
  `CommunityOrganismRoleEnum`), #129 (three facet enums), #130 (assignment
  classes, slots, writer methods), #133/#134/#135/#143 (docs regen, schema polish,
  SchemaView guard, `iter_role_assignments`), #139 (+#141) retired the flat
  `IngredientRoleEnum`/`RoleAssignment`/`media_roles`, migrating 987 assignments
  across 906 records.
- **Role research tooling** — #146 (template + Edison shim + `template_vars()`),
  #153 (`apply_role_research_results.py`). Never executed; see item 5.
- **Vendored-sync + pin retirement** — #150 (sync `chem_formula.py` from
  TraitMech), #154 (shared-reference drift check replaces the self-referential
  sha256 pin; resynced `test_id_label_plausibility.py`), #155 (enable the
  plausibility gate report-only, sync a hub validator fix, bump the canon ref),
  #156 (retire the id-label pin), #157 (fold in `mech_shared.yaml`, retire the
  schema pin).
- **CURIE standard** — #140, `docs/CURIE_STANDARD.md`, with
  `mappings/mim_curie_aliases.tsv` resolving the 205 renames that have retired
  `MIM:<name>` CURIEs. `MIM:<name>` is **not** rename-stable; always resolve
  through the alias map before concluding a CURIE is missing.
- **Curation** — #117 (SSSOM rebuilt to current filenames + CHEBI revalidated via
  OAK and OLS), #118 (`UNIFIED_INGREDIENT_MAPPING.tsv` refresh), #145 (2
  SIMPLE_CHEMICAL residual records grounded), #152 (duplicate
  anthraquinone-2,6-disulfonate merged into AQDS), #144 (id-label cache fix,
  discussions export fix, `next-tasks` skill), #151 (preserve discussions across
  identifier-changing moves).
- **Published artifacts** — `mappings/ingredient_mappings.sssom.tsv` 2,201 data
  rows, last rebuilt 2026-07-21 (#152); `UNIFIED_INGREDIENT_MAPPING.tsv` 3,915
  data rows, last rebuilt 2026-07-20 (#140). kg-microbe re-syncs both on every
  consolidation run, so an item is only done once these are rebuilt *and*
  published.
