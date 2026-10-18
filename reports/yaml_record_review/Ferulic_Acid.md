# `data/ingredients/mapped/Ferulic_Acid.yaml`

## Verdict

Needs curation, with a major stereochemistry-specificity issue. The record
maps the CultureBotHT `Ferulic Acid` row to generic `CHEBI:193350` ferulic
acid, but its CAS RN resolves to the trans isomer and a form-specific
`CHEBI:17620` term exists for `trans-ferulic acid`.

## Identity

- Reviewed record: `data/ingredients/mapped/Ferulic_Acid.yaml`.
- Current grounding: `identifier: CHEBI:193350`,
  `ontology_mapping.ontology_id: CHEBI:193350`, canonical label
  `ferulic acid`, source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- PubChem lookup by CAS RN `537-98-4` resolved to CID 445858 with the
  stereospecific InChI `InChI=1S/C10H10O4/.../b5-3+`, while the InChI stored in
  `chemical_properties` omits that trans double-bond layer.
- `uv run runoak -i sqlite:obo:chebi info CHEBI:193350` resolved the current
  target as the generic `ferulic acid` term; the form-specific neutral target
  is `CHEBI:17620` `trans-ferulic acid`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ferrous_Ion.yaml data/ingredients/mapped/Ferrous_ammonium_sulfate.yaml data/ingredients/mapped/Ferroverdin.yaml data/ingredients/mapped/Ferulate.yaml data/ingredients/mapped/Ferulic_Acid.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Ferulic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed against the current generic ChEBI target.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CAS RN, structure fields, and synonyms as the per-record
  YAML.
- The OAK/OLS row-review manifest only confirmed that the
  `trans-4-Hydroxy-3-methoxycinnamic acid` synonym was already represented; it
  did not resolve the CAS-level trans specificity.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Ferulic_Acid` to generic `CHEBI:193350` with `skos:exactMatch` and
  exports `trans-4-Hydroxy-3-methoxycinnamic acid` plus `CAS:537-98-4`, both
  of which point at the trans isomer.
- Major: MIM mapping semantics require stereospecific substances to use the
  specific ontology term when one exists; this record's CAS-backed source
  should be aligned with `CHEBI:17620` after the Ferulate record moves off that
  target to `CHEBI:29749`.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, `scripts`, `src`, `tests`, and `reports` for `Ferulic_Acid` and
  `Ferulic Acid` found the active YAML, aggregate copy, final SSSOM row,
  OAK/OLS synonym-enrichment review row, and ignored aggregate backups.

## Completeness

- The CultureBotHT CAS RN, ingredient type, formula, and final SSSOM row are
  populated.
- The ontology target and structure fields need a stereospecific refresh
  against the trans-ferulic-acid identity.

## Recommended Edits

- Major: after remapping `Ferulate` to `CHEBI:29749`, remap
  `data/ingredients/mapped/Ferulic_Acid.yaml` to `CHEBI:17620`
  `trans-ferulic acid`, refresh the trans InChI/SMILES from PubChem or ChEBI,
  sync `data/curated/mapped_ingredients.yaml`, regenerate
  `mappings/ingredient_mappings.sssom.tsv`, and rerun strict validation plus
  the final SSSOM invariant gates.
