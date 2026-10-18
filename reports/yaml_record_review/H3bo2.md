# `data/ingredients/mapped/H3bo2.yaml`

## Verdict

Needs curation. The exact boronic-acid ChEBI identity, CAS RN, structure fields,
occurrence count, exported synonyms, and final SSSOM row pass, but the
`TRACE_ELEMENT` role is only an in-session computational prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/H3bo2.yaml`.
- Identifier and grounding: `identifier: CHEBI:38267` with
  `ontology_mapping.ontology_id: CHEBI:38267`, label `boronic acid`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `13780-71-7`, formula `H3BO2`, InChI
  `InChI=1S/BH3O2/c2-1-3/h1-3H`, and SMILES `[H]OB([H])O[H]`.
- Occurrence statistics: `total_occurrences: 4` and `media_count: 4`.
- Role facet: `TRACE_ELEMENT` with `COMPUTATIONAL_PREDICTION` evidence from
  provisional in-session Claude reasoning.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/H2tetramethylammonium.yaml data/ingredients/mapped/H2trimethylamine.yaml data/ingredients/mapped/H2wo4.yaml data/ingredients/mapped/H3PO4.yaml data/ingredients/mapped/H3bo2.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `linkml-term-validator` passed for `CHEBI:38267` and the CAS registry CURIE.
- The matching aggregate `data/curated/mapped_ingredients.yaml` entry is
  identical to the split per-record YAML.

## Evidence

- OLS4 resolves `CHEBI:38267` as active `boronic acid` with CAS `13780-71-7`,
  formula `H3BO2`, the same InChI, and the same SMILES.
- The final SSSOM synonym tokens `BH(OH)2`, `dihydroxyborane`, and
  `hydridodihydroxidoboron` all occur as ChEBI synonyms for `CHEBI:38267`;
  the final `CAS:13780-71-7` token matches `chemical_properties.cas_rn`.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:H3bo2` to
  `CHEBI:38267`.
- Major: the `TRACE_ELEMENT` facet is supported only by
  `reference_type: COMPUTATIONAL_PREDICTION` from an in-session LLM note.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, occurrence
  statistics, exact synonyms, and final SSSOM row are present and consistent.
- The role facet is incomplete until a curator either supplies external
  evidence for boronic acid as a trace element or removes the provisional role.

## Recommended Edits

- Major: review the `TRACE_ELEMENT` facet and either replace the provisional
  in-session evidence with an external database/literature source or remove the
  unsupported role.
