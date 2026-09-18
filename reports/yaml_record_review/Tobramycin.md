# `data/ingredients/mapped/Tobramycin.yaml`

## Verdict

Pass. The exact CHEBI identity, MicrobeDecoder occurrence accounting,
aggregate row, and final SSSOM row for tobramycin are synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Tobramycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:28864` with matching
  `ontology_mapping.ontology_id`, label `tobramycin`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Synonyms: none.
- Occurrences: 80 MicrobeDecoder hits across BacDive antibiotic resistance,
  antibiotic sensitivity, and metabolite production columns.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Titanium_chloride` through `Tomatidine_Hydrochloride`: exited 0 and wrote
  zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 search for `tobramycin` returns `CHEBI:28864` with label
  `tobramycin`; the sulfate and charged-species ChEBI terms are separate,
  non-identical neighbors.
- The PubChem-backed formula, SMILES, InChI, and molecular weight encode the
  neutral tobramycin base.
- The final SSSOM row has `MIM:Tobramycin skos:exactMatch CHEBI:28864`, uses
  `obo:chebi.owl`, carries the expected MicrobeDecoder and reviewed curator
  sources, and leaves `other` empty.

## Completeness

- The CHEBI identity, structure fields, MicrobeDecoder source count, aggregate
  copy, and final SSSOM row agree.
- No CAS RN, components, media roles, environmental contexts, or final
  synonym/export tokens require curation.

## Recommended Edits

- None.
