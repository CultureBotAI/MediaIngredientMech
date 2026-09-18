# `data/ingredients/mapped/3-phenylpropionate.yaml`

## Verdict

Pass with minor issues, minor. The exact anion mapping to `CHEBI:51057`,
microbedecoder occurrence count, ChEBI/PubChem chemistry, SSSOM row, and
aggregate row pass; only stale advisory rows and optional synonym enrichment
remain.

## Identity

- Reviewed record: `data/ingredients/mapped/3-phenylpropionate.yaml`.
- Identifier and grounding: `identifier: CHEBI:51057` with
  `ontology_mapping.ontology_id: CHEBI:51057`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: `CHEBI:51057` resolves to the 3-phenylpropionate
  monocarboxylic-acid anion, formula `C9H9O2`, net charge `-1`, InChI
  `InChI=1S/C9H10O2/c10-9(11)7-6-8-4-2-1-3-5-8/h1-5H,6-7H2,(H,10,11)/p-1`,
  and SMILES `O=C([O-])CCc1ccccc1`; the record matches.
- The direct microbedecoder `BacDive_Metabolite_production` count of 1 is
  preserved under `source_occurrences`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/3-methyl-3-butenol.yaml data/ingredients/mapped/3-nitropropanoate.yaml data/ingredients/mapped/3-octanone.yaml data/ingredients/mapped/3-phenylpropionate.yaml data/ingredients/mapped/3-sialyllactose_Sodium_Salt.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/3-methyl-3-butenol.yaml data/ingredients/mapped/3-nitropropanoate.yaml data/ingredients/mapped/3-octanone.yaml data/ingredients/mapped/3-phenylpropionate.yaml data/ingredients/mapped/3-sialyllactose_Sodium_Salt.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- The active aggregate and `mappings/ingredient_mappings.sssom.tsv` contain the
  same exact `MIM:3-phenylpropionate` to `CHEBI:51057` row.

## Evidence

- The active ChEBI page confirms that `CHEBI:51057` is the anion, not the
  neutral 3-phenylpropionic acid.
- The older `microbedecoder_auto_mapped_review.tsv` row explicitly warned that
  its approval did not check for homonyms or wrong-sense matches. The direct
  ChEBI verification performed here closes that gap for this record.
- Stale: `mappings/record_research_validation.tsv` still reports
  `ingredient_type` as missing and asks whether the source meant the neutral
  acid. The active microbedecoder label is the exact anion label, and the
  `ingredient_type` field is populated.
- Optional: ChEBI lists `3-phenylpropanoate`; this exact synonym could be added
  but its absence does not corrupt identity, SSSOM, or generated docs.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `scripts`, `conf`, `src`, `tests`, `.github`, and `.claude` found the
  active YAML, aggregate copy, SSSOM row, microbedecoder review row, generated
  docs, source import rows, stale advisory rows, and ignored aggregate backups.

## Completeness

- Formula, molecular weight, InChI, and SMILES are populated from ChEBI/PubChem.
- The direct microbedecoder occurrence is traceable.
- Empty `synonyms: []` is acceptable; neutral-acid names should not be added to
  this exact anion.

## Recommended Edits

No YAML edit is required for this record. The stale advisory rows can be ignored
or refreshed when `mappings/record_research_validation.tsv` is rebuilt.
