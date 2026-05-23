# Schema gap analysis — 2026-05-23

**Tool**: `linkml-validate` (linkml 1.9.x, pinned by `pyproject.toml`).
**Trigger**: pre-republish guard after a batch of cleanups
(env-context migration, ontology-label backfill, chemical-properties
enrichment, OLS encoding fix).

## Summary

| Axis | Findings |
|------|---------:|
| Schema | **0 errors / 0 warnings** |
| Instances (collections) | **0 errors / 0 warnings** |
| Instances (per-record corpus, 2268 files) | **0 errors / 0 warnings** |
| Generator drift (naive datetimes, metadata-stripping dumps, direct writes) | **clean** |

Same end-state as 2026-05-16; nothing regressed.

## What was done in this pass

1. **Canonical schema migration of issue #1 (env-context)**:
   `mediaingredientmech.yaml::IngredientRecord` now carries
   `environmental_context` (multivalued, optional, range
   `EnvironmentContext`). New class `EnvironmentContext` and enum
   `EnvironmentRelevanceEnum` mirror the legacy
   `mapped_ingredients_schema.yaml` definitions verbatim, with a
   schema-level cross-consistency test (`TestCanonicalSchemaEnvironmentalContext`)
   pinning the two in sync.
2. **`ontology_label: ''` sweep**:
   312 CHEBI-mapped records (all in `data/curated/mapped_ingredients.yaml`)
   had empty-string labels — passing `required: true` trivially because
   LinkML treats `''` as present. Backfilled via OLS4 ChEBI lookups
   (`scripts/backfill_ontology_labels.py`). 312/312 filled, 0 unresolved.
3. **Chemical-properties enrichment**:
   `scripts/enrich_chemical_properties.py` was re-run against all
   CHEBI-mapped records. Initial pass: 41 candidates, 9 enriched.
   After the source-mismatch cleanup (see step 5) the candidate count
   dropped to 26 — all genuinely unenrichable: abstract CHEBI classes
   (aromatic compound, bile salts, hydrocarbon, siderophore), polymers
   (DNA, glycogen, xylan, maltodextrin), proteins (catalase, elastin,
   LL-37), or obsolete CHEBI terms (CHEBI:1, CHEBI:8150). CHEBI has no
   formula/SMILES/mass annotations for any of these — they are
   parent classes or biopolymers without a single structural formula.
4. **OLS4 URL encoding fix** in
   `src/mediaingredientmech/utils/chemical_properties_client.py`: the
   ChEBI lookup was single-URL-encoding the IRI, which OLS4 rejects
   with 400. Switched to double encoding (matches OLS4 contract; see
   `scripts/backfill_ontology_labels.py` for the same pattern).
5. **Source-mismatch fix**: 10 records had
   `ontology_mapping.ontology_id` with one prefix but
   `ontology_mapping.ontology_source` declaring a different ontology
   (6 NCIT-ids tagged `CHEBI`, 4 FOODON/ENVO/UBERON-ids tagged
   `registry`). All corrected to match the prefix, with
   `curation_history` action `CORRECTED` for audit. See per-record
   list below.
6. **Backfill regression caught**: The first backfill pass overwrote
   2 records (CHEBI:1, CHEBI:8150 — both obsolete) with junk labels
   like `CHEBI_1` because OLS4 returns the IRI fragment as `label`
   for obsolete terms with no real label. Hardened
   `scripts/backfill_ontology_labels.py` to reject IRI-fragment
   labels and skip `is_obsolete: true` terms. The 2 records were
   reverted to empty-string labels (their pre-pass state).

## Source-mismatch fix detail (step 5)

| ontology_id | old source | new source | preferred_term |
|---|---|---|---|
| NCIT:C221830 | CHEBI | NCIT | Adenomycin |
| NCIT:C169798 | CHEBI | NCIT | Avoparcin |
| NCIT:C98044  | CHEBI | NCIT | Cetocycline |
| NCIT:C1928   | CHEBI | NCIT | Dynemicin |
| NCIT:C90684  | CHEBI | NCIT | Lydimycin |
| NCIT:C152426 | CHEBI | NCIT | Steffimycin |
| FOODON:03315772 | registry | FOODON | Egg yolk |
| FOODON:03301484 | registry | FOODON | Skimmed milk |
| ENVO:06105101   | registry | ENVO   | Plastic |
| UBERON:0001977  | registry | UBERON | Serum |

## Carryover findings (not addressed in this pass)

- **2 records mapped to obsolete CHEBI terms**: `CHEBI:1` (also has
  `preferred_term: CHEBI:1` — itself a placeholder) and `CHEBI:8150`
  (Bacto Soytone). Both retain `ontology_label: ''` since OLS4 has no
  canonical label and the term is obsolete. Worth a manual re-mapping
  pass (Bacto Soytone is a Difco trademark and may not have a CHEBI
  successor; could re-map to a generic peptone/soy hydrolysate term
  or mark as needs-expert).

## Re-running the skill

The /schema-gap-analysis skill commands in
`.claude/skills/schema-gap-analysis/skill.md` are still accurate
and copy-paste runnable. No skill edits needed.
