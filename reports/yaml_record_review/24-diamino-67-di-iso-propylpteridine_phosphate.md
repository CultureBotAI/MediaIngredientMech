# `data/ingredients/mapped/24-diamino-67-di-iso-propylpteridine_phosphate.yaml`

## Verdict

Needs curation, minor. The local phosphate-salt identity and narrow parent
mapping to `CHEBI:73908` pass, and the comma-split fragments have been absorbed
as raw text, but the promoted record still has stale pre-resolution notes and no
`ingredient_type` or chemistry.

## Identity

- Reviewed record:
  `data/ingredients/mapped/24-diamino-67-di-iso-propylpteridine_phosphate.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.compound:24-diamino-67-di-iso-propylpteridine_phosphate`
  with `ontology_mapping.ontology_id: CHEBI:73908`, source `CHEBI`,
  `mapping_quality: NARROW_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:73908`
  resolves to the free base `2,4-diamino-6,7-diisopropylpteridine`, lists
  formula `C12H18N6`, and carries the `O/129` synonym.
- The YAML correctly does not assert that the phosphate salt is identical to
  the free base. Its exact identity is the local `kgmicrobe.compound` CURIE, and
  `CHEBI:73908` is only a parent `NARROW_MATCH`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/24-Dinitrophenol.yaml data/ingredients/mapped/24-diamino-67-di-iso-propylpteridine_phosphate.yaml data/ingredients/mapped/25-Dihydroxy-4-Methoxychalcone.yaml data/ingredients/mapped/3-Aminophenol.yaml data/ingredients/mapped/3-Aminopropionitrile_Fumarate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/24-diamino-67-di-iso-propylpteridine_phosphate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected
  `skos:narrowMatch` row to `CHEBI:73908` and the exact registry/identity row
  preserving the local `kgmicrobe.compound` CURIE.

## Evidence

- The active ChEBI page verifies that `CHEBI:73908` denotes the free-base
  vibriostat parent, which is consistent with the current narrow-match
  rationale.
- `0129 (2` and `4-Diamino-6` remain as rejected per-file records, and their
  histories show they were merged into this intact record as comma-split
  fragments. The active mapped YAML retains both as `RAW_TEXT`, which prevents
  the fragments from being treated as exact standalone compounds.
- The `Vibriostat` record separately maps to `CHEBI:73908` as the free-base
  identity, so the phosphate salt and free base are not collapsed.
- Stale: `mappings/record_research_validation.tsv` still contains P1/P2 rows
  arguing against an exact `CHEBI:73908` mapping. Those rows predate, or do not
  account for, the current local exact identity plus parent `NARROW_MATCH`
  pattern.
- The hidden/ignored-inclusive search over `data/custom`, `data/curated`,
  `data/ingredients`, `mappings`, and `reports` found the active YAML, rejected
  fragment files, exact and narrow SSSOM rows, the paired `Vibriostat` record,
  and advisory rows.

## Completeness

- Minor: the top-level `notes` still describe the original unmapped import and
  say "Curator review needed" even though the record has been promoted.
- Minor: `ingredient_type` is absent.
- Minor: the local exact salt identity has no CAS RN, formula, InChI, or SMILES
  captured yet.

## Recommended Edits

1. Replace the stale top-level `notes` with a short summary of the #213/#313
   local salt identity, comma-split-fragment merge, and narrow free-base parent.
2. Set `ingredient_type: SINGLE_INGREDIENT`.
3. Add phosphate-salt chemistry if an inspected authority can support it.
4. Regenerate `data/curated/mapped_ingredients.yaml`,
   `mappings/ingredient_mappings.sssom.tsv`, and docs from the maintained YAML.
5. Re-run the focused strict/LinkML validators, synonym review,
   `just qc-sssom`, and `just qc-flat-coverage` after those edits.
