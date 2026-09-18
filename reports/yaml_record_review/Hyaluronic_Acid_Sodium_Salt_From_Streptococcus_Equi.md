# `data/ingredients/mapped/Hyaluronic_Acid_Sodium_Salt_From_Streptococcus_Equi.yaml`

## Verdict

Needs curation. The CAS-primary record intentionally keeps a narrow relation to
the active ChEBI parent `Hyaluronic acid sodium`, but provenance/state text and
a parent-term synonym are curated as exact synonyms and leak into the published
SSSOM `other` column.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Hyaluronic_Acid_Sodium_Salt_From_Streptococcus_Equi.yaml`.
- Identifier and grounding: `identifier: cas:9067-32-7` with
  `ontology_mapping.ontology_id: CHEBI:201433`, label
  `Hyaluronic acid sodium`, source `CHEBI`,
  `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `9067-32-7`, formula `C28H44N2NaO23+`,
  PubChem CID `3084049`, and populated InChI/SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Hortesin.yaml data/ingredients/mapped/Hunters_Trace_Stock_Solution.yaml data/ingredients/mapped/Huperzine_A.yaml data/ingredients/mapped/Hyaluronic_Acid_Sodium_Salt_From_Streptococcus_Equi.yaml data/ingredients/mapped/Hydantoin.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Hyaluronic_Acid_Sodium_Salt_From_Streptococcus_Equi.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1448`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1448`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:201433` as the active ChEBI class
  `Hyaluronic acid sodium` and lists only the long
  `sodium;(2S,3S,4R,5R,6R)-...` text as an exact synonym.
- The stored PubChem CID `3084049` resolves and still matches the saved
  formula, SMILES, and InChI; PubChem no longer resolves CAS RN `9067-32-7` by
  name.
- The final SSSOM publishes the expected `skos:narrowMatch` row from
  `MIM:Hyaluronic_Acid_Sodium_Salt_From_Streptococcus_Equi` to
  `CHEBI:201433`, plus exact CAS and local `kgmicrobe.compound` registry rows.
- Major: `not filter sterilized` is a supplied-state note, not an exact synonym
  for hyaluronic acid sodium salt from `Streptococcus equi`, but it is stored as
  `EXACT_SYNONYM` and exported in the CHEBI parent row's final `other` column.
- Major: the long ChEBI synonym is an exact synonym on the broader parent
  `CHEBI:201433`; exporting it on a narrow parent-mapping row collapses the
  source-specific boundary unless it is separately curated as a synonym of the
  CAS-primary MIM subject.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, three final SSSOM rows, docs projections, and row-review
  manifest entries for the CHEBI parent, CAS registry, and local companion
  registry rows.

## Completeness

- The active ChEBI parent, CAS registry row, local exact registry row,
  structure fields, aggregate copy, and final SSSOM registry rows are present
  and structurally consistent.
- The record is incomplete until non-synonym source/state text and parent-only
  synonyms are removed from the subject's exported exact-synonym surface.

## Recommended Edits

- Major: change `not filter sterilized` to non-exported provenance or delete it
  if the raw CultureBotHT source no longer needs preservation, then regenerate
  the SSSOM.
- Major: remove the broader `CHEBI:201433` systematic synonym from this
  source-specific CAS-primary record unless curated evidence shows it is a true
  synonym of the exact MIM subject, then rerun strict, term, round-trip,
  id-label, component, and SSSOM validation.
