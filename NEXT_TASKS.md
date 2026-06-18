# Next Tasks — MediaIngredientMech backlog

Deferred work, each entry with enough context to pick up cold. **Maintenance:**
update this file as work is started/finished — move done items out, add new
deferrals here. Keep the cross-Mech items in sync with the sibling repos'
`NEXT_TASKS.md` (CultureMech / CommunityMech / TraitMech).

Last reconciled: 2026-06-15.

## 1. Chemical-properties enrichment — enricher repaired, residual is the ceiling

**Done (2026-06-15, `feat/enrich-chemical-properties`)** — the enricher had silently
broken: OLS4 renamed its annotation keys (`formula` → `generalized_empirical_formula`;
SMILES/InChI → `*_string`), so every fetch returned None. Fixed
`chemical_properties_client.py` to read the current keys (legacy fallback kept),
broadened the enricher to target records *missing `molecular_formula`* (not just
those with no `chemical_properties` block) with a gap-filling **merge** (never
clobbers `cas_rn`), and made the `Enriched` counter report net changes. Re-ran:
**3 records gained formula/SMILES** (diaminopimelic acid, sodium L-lactate,
isobutyramide+mass).

The remaining ~83 missing-formula records are the **genuine ceiling** — abstract
CHEBI classes (aromatic compound, bile salt, hydrocarbon), polymers (glycogen,
carboxymethylcellulose, chondroitin sulfate, DNA), proteins (elastin, LL-37),
complexes (kanamycin), and minerals (ferrihydrite) — which legitimately have no
single empirical formula in ChEBI. Not failures; leave them.

- Run again any time with `python scripts/enrich_chemical_properties.py` (idempotent);
  regenerate per-record files with `just export-individual` after.
- Gotcha still live: OLS4 needs **double** URL-encoding of ChEBI IRIs (handled).
- Find remaining: `grep -rL molecular_formula data/ingredients/mapped/*.yaml | xargs grep -l 'ontology_source: CHEBI'`

## 2. Cross-Mech validator pin guard — DONE (4-repo invariant)

~~Vendor the id↔label validator into CommunityMech~~ — **DONE** (2026-06-12,
CommunityMech PR #132).

**Done** (2026-06-15): the byte-identical invariant now spans **all four** Mech
repos (CultureMech, MIM, CommunityMech, TraitMech). culturebotai-claw#6 Option 1
extended the pin from the script alone to the full vendored set — the validator
`.py` **plus** the two shared tests — across every repo (CommunityMech's drifted
test copies were resynced + pinned in PR #151); editing a vendored test now fails
CI everywhere. TraitMech joined and enforces too (TraitMech PR #110 Phase 1,
PR #111 Phase 2 blocking gate — 14 wrong CURIEs fixed, gate green). All four pin
the same 3-line manifest (`142bbe1…` / `55a432…` / `f01d22…`).
`conf/id_label_targets.yaml` stays **unpinned by design** — it is intentionally
per-repo (different adapters/targets/exceptions), not a drift risk to fix.

## 3. Hard unmapped residual — dedicated semantic curation (~395 records)

Automated exact/normalized/fuzzy matching is **exhausted** (verified 2026-06-14:
only ~1 clean exact match across all 398). The residual is specialized cobamides,
flavonoids, natural products, element placeholders, and mixtures.

- Use `deep-research-ingredient` (Edison/PaperQA3; `EDISON_PLATFORM_API_KEY` is
  configured) or `mediaingredientmech-agentic-curation` (FutureHouse Falcon) for
  source-backed identity + CHEBI/FOODON grounding, per record.
- **Migration recipe (proven 2026-06-15, NAA promotion):** mapping an unmapped
  record is multi-surface and only partly automated. The working sequence:
  1. In the source collections, move + transform the record:
     `unmapped_ingredients.yaml` (delete record, decrement header counts) →
     `mapped_ingredients.yaml` (add with `ontology_mapping`, `mapping_status: MAPPED`,
     a `PROMOTED_TO_MAPPED` history entry; increment header counts).
  2. `just export-individual` (record file moves unmapped/ → mapped/).
  3. **Hand-add the SSSOM row** — `reconcile_sssom` reports the GAP but won't
     synthesize new-row provenance. One `skos:exactMatch` row to the CHEBI id
     (`obo:chebi.owl`, canonical object_label) suffices for a CHEBI-primary record;
     Rule B1 needs no registry sibling. Insert in the file's sort order (by the
     *decoded* subject label, e.g. between `MIM:1-Kestose` and `MIM:1-Pentanol`).
  4. `just export-lists` (docs). Verify: `reconcile_sssom` GAP 0, SSSOM invariants
     Rules A/B1/B2/B3, `validate-products` (the blocking id↔label gate), validate-strict.
  - **Helper built (2026-06-16): `scripts/promote_resolved_unmapped.py`** automates
    the whole recipe (collection move + canonical-label lookup + SSSOM row inserted in
    sort order + regen + verify), with a **PK-collision guard** that refuses to create
    a duplicate CHEBI primary (redirect those to a merge). `--dry-run` by default.
    Usage: `python scripts/promote_resolved_unmapped.py --identifier UNMAPPED_NNNN
    --to CHEBI:NNN --quality EXACT_MATCH --evidence-source "…" --note "…" --apply`.
    Only handles exact/close (narrow/broad need registry SSSOM rows — hand-curate).
  - Note: the per-record filename sanitiser drifted over time, so a freshly-promoted
    file may get a slightly different slug casing than the old unmapped file — cosmetic.
- **Batch 1 done (2026-06-14, `feat/deep-research-unmapped-batch`)** — 3 records
  deep-researched (Edison/PaperQA3) and **enriched in place** (synonyms / CAS-RN /
  provenance; left UNMAPPED — no risky migration yet):
  - `1-Naphtylacetic Acid` → **MAPPED 2026-06-15** (UNMAPPED_0316 → CHEBI:32918
    "1-naphthaleneacetic acid", EXACT_MATCH) via the migration recipe above. NAA,
    CAS 86-87-3 — a "naphtyl" misspelling string-matching missed. (unmapped 398 → 397)
  - `alpha-ketoglutamate` → **MERGED 2026-06-16** into the existing `CHEBI:30915`
    "alpha-ketoglutaric acid" record (added as a synonym; UNMAPPED_0323 removed).
    `promote_resolved_unmapped.py`'s PK-collision guard caught that CHEBI:30915 (and
    the anion CHEBI:16810) are already mapped — it's a duplicate, not a new mapping.
    (unmapped 397 → 396)
  - `2-methyladeninyl cobamide` (UNMAPPED_0182) → **stays UNMAPPED, confirmed**: a
    specific corrinoid ("Factor A") with no source-backed CHEBI/CAS; do NOT map to
    cobalamin/B12. Validates the prior curator call; enriched with synonyms.
  - Takeaway: deep research resolves identities that string-matching can't, but most
    of the residual is genuinely hard. The 2 "ready to map" records still await the
    multi-surface migration above. Edison reports live under `research/` (gitignored).
- **Batch 2 done (2026-06-16, `feat/deep-research-batch2-enrich`)** — 5 records
  deep-researched (Edison/PaperQA3); **all confirmed UNMAPPED** (0 mappings, 0
  merges) and enriched in place with the findings + provenance:
  - `6-methylnicotinate` — ambiguous (carboxylate/anion vs methyl ester); +synonym
    `6-methylnicotinic acid` (related).
  - `Amphotericin` — spans A/B + formulations; do NOT exact-map to amphotericin B
    (CHEBI:2682); +related synonyms `amphotericin B`/`AmB`.
  - `7,2'-Dimethoxyflavone`, `7,4'-Dimethoxyisoflavone` — specific positional
    isomers, no source-backed CAS/CHEBI; closeMatch to a flavone parent would lose
    isomer specificity.
  - `2',2'-Bisepigallocatechin Digallate` — polyphenol; no CAS/formula/CHEBI;
    naming-variant instability prevents grounding.
  - Confirms the residual is genuinely hard: like the cobamide in batch 1, these
    specialized natural products / ambiguous-form compounds lack clean ontology
    grounding. "Confirmed unmapped + enriched" is the correct, defensible outcome.
  - **Cobamide cluster closed (2026-06-17)** — the remaining 4 (5-methoxy-/
    5-methyl-benzimidazolyl, adeninyl, benzimidazolyl cobamide) deep-researched;
    **all confirmed UNMAPPED** + enriched (Factor IIIm; 5-MeBza-Cba; pseudocobalamin;
    underspecified — no stable CHEBI/CAS, upper-ligand ambiguity, must not map to B12).
- **Batch 3 done (2026-06-16, `feat/mim-map-inorganic-batch3`)** — a different angle:
  not deep research but a **mappability triage** of the 396 residual. Most is
  genuinely unmappable (commercial media/broths/agars, trace-element & vitamin
  solutions, sera, extracts, grains, buffers, metal-NTA chelates). The high-yield
  sliver is single compounds automated matching missed via formula/spelling
  variants. **3 mapped** (EXACT_MATCH) via `promote_resolved_unmapped.py`, each
  CHEBI id↔label verified against local OAK before mapping (so the blocking gate
  stays green):
  - `KNO2` (UNMAPPED_0413) → **CHEBI:232610** "potassium nitrite" (formula).
  - `Thioglycollic acid` (UNMAPPED_0539) → **CHEBI:30065** "thioglycolic acid" (spelling).
  - `Pyromelitic acid` (UNMAPPED_0504) → **CHEBI:45165** "pyromellitic acid" (misspelling).
  (unmapped 396 → 393.)
  - **`KJ` (UNMAPPED_0412) — do NOT merge (2026-06-17 review):** the ledger guess
    "Kaliumjodid = potassium iodide" is *plausible by German-naming domain knowledge*
    but is **not source-confirmed** — MediaDive ingredient 1042 ("KJ") returns garbage
    (auto-matched to **phencyclidine**, C17H25N / CAS 77-10-1), and a prior reviewer
    flagged the **kilojoule** (unit) reading and classified it UNDEFINED_MIXTURE.
    With the only source garbage and a genuine homonym, leave it UNMAPPED — merging
    KI's synonyms onto an unconfirmed "KJ" isn't justified for a gate-enforced dataset.
  - Left alone (ambiguous, no source CAS to disambiguate): garbled salt-hydrate
    formulae (`MnCl4 x n H2O`, `Na2MoO7 x 2 H2O`, `Na2Se2O3`, …), `Na-tetrathionate`,
    `Sodium crotonate`, `α-D-Glucose monohydrate`. Map only with source confirmation.
- **Batch 4 done (2026-06-16, `feat/mim-map-salt-hydrates`)** — the careful
  source-confirmed pass over the ~25 garbled inorganic salt-hydrate formulae. Method:
  each carries `source_id=mediadive.ingredient:NNNN`, so the **MediaDive REST API**
  (`/rest/ingredient/{id}`) is the authoritative source — its `name` / `formula` /
  `CAS-RN` fields confirm (or refuse) the intended compound even though MediaDive's
  own `ChEBI` is null for all of them. Outcome: **1 mapped**, the rest deferred with
  reasons (a fully-resolved ledger — do not re-investigate without new evidence):
  - **Mapped:** `NH42CO3` (UNMAPPED_0480) → **CHEBI:229630** "ammonium carbonate"
    (MediaDive CAS 10361-29-2; anhydrous = EXACT_MATCH). (unmapped 393 → 392.)
  - **Deferred — no clean CHEBI term** (genuinely unmappable, like CommunityMech's
    minting-exceptions; all source-CAS-confirmed but CHEBI lacks the salt): cerium(III)
    nitrate hexahydrate (10294-41-4), chromium potassium sulfate dodecahydrate /
    chrome alum (7788-99-0), potassium phosphite `KH2PO3` (13977-65-6 — NB: phosph**ite**,
    not phosphate), lanthanum nitrate hexahydrate (10277-43-7), sodium β-glycerophosphate
    pentahydrate (13408-09-8), sodium metasilicate nonahydrate (13517-24-3), neodymium
    chloride hexahydrate (13477-89-9), praseodymium chloride hydrate (19423-77-9).
  - **`Mg(NO3)2 x 6 H2O` (UNMAPPED_0444) — DONE 2026-06-17** (`feat/resolve-deferred-salt-ledger`):
    hand-curated the narrowMatch per the corpus convention. Re-confirmed via MediaDive
    REST (1763: magnesium nitrate hexahydrate, CAS 13446-18-9). Now `cas:13446-18-9`
    primary, `skos:narrowMatch` **CHEBI:64736** "magnesium nitrate" (anhydrous parent)
    + 3 SSSOM rows (CHEBI narrowMatch + cas/kgmicrobe exactMatch registry rows for
    Rule B1). reconcile in sync; SSSOM invariants A/B1/B2/B3 pass. (The last actionable
    narrowMatch in the salt-hydrate ledger.)
  - **Deferred — no source confirmation** (MediaDive `CAS-RN`+`formula`+`ChEBI` all
    null; only the garbled name, so unverifiable per this pass's bar even though
    chemically guessable): `Na2Mo4`/`Na2MoO7`/`Na2MoO7O4 x 2 H2O` (sodium molybdate?),
    `Na2WO2 x 2 H2O` (sodium tungstate?), `Na2Se2O3` (sodium selenite?), `Na2S2SO3`
    (sodium thiosulfate?), `MnCl4 x 4/6 H2O` (manganese(II) chloride hydrate?),
    `Fe(SO4)3 x n H2O` (iron(III) sulfate?).
  - **Deferred — ambiguous source:** `Se-acid` (UNMAPPED_0517) — MediaDive CAS
    7783-08-6 = selen**ous** acid (CHEBI:26642) but its `formula` field `H2O4Se` =
    selen**ic** acid; the conflict blocks a confident call.

## 4. mesh.db refresh → keep the 4 SCR exceptions (verified 2026-06-17)

`conf/id_label_targets.yaml` carries 4 `exceptions` for valid MeSH supplementary-
concept records (avocatin B, cholinium lysinate, sodium glutarate, plicacetin)
absent from the cached `sqlite:obo:mesh`.

**Refresh tested 2026-06-17 — does NOT help.** Forced a clean re-download of
`sqlite:obo:mesh` (394 MB, byte-identical to the prior cache): the 4 SCRs are
**still absent** while older SCRs (e.g. C016600) are present — the upstream semsql
MeSH build excludes these recent (2020/2024) supplementary-concept records.
**Keep the exceptions.** Only revisit if the semsql/obo MeSH build starts shipping
C-prefix SCRs from 2020+; then drop the matching entries and re-run
`just validate-products` to confirm OK_CANONICAL.
