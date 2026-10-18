# `data/ingredients/mapped/H2seo3.yaml`

## Verdict

Pass. The exact selenous-acid ChEBI identity, CAS RN, chemical structure,
CultureMech mineral role, occurrence count, exported synonyms, and final SSSOM
row are internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/H2seo3.yaml`.
- Identifier and grounding: `identifier: CHEBI:26642` with
  `ontology_mapping.ontology_id: CHEBI:26642`, label `selenous acid`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `7783-00-8`, formula `H2O3Se`, InChI
  `InChI=1S/H2O3Se/c1-4(2)3/h(H2,1,2,3)`, and SMILES `O=[Se](O)O`.
- Occurrence statistics: `total_occurrences: 24` and `media_count: 24`.
- Role facet: `TRACE_ELEMENT` with `DATABASE_ENTRY` evidence preserving the
  CultureMech original role text `Mineral`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/H2_CO2.yaml data/ingredients/mapped/H2dimethylsulfide.yaml data/ingredients/mapped/H2methanol.yaml data/ingredients/mapped/H2seo3.yaml data/ingredients/mapped/H2so4.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `linkml-term-validator` passed for `CHEBI:26642` and the CAS registry CURIE.
- The matching aggregate `data/curated/mapped_ingredients.yaml` entry is
  identical to the split per-record YAML.

## Evidence

- OLS4 resolves `CHEBI:26642` as active `selenous acid` with CAS `7783-00-8`,
  formula `H2O3Se`, the same InChI, and the same SMILES.
- The final SSSOM synonym tokens `[SeO(OH)2]`,
  `dihydroxidooxidoselenium`, `selenige Saeure`, and `selenious acid` all occur
  as ChEBI synonyms for `CHEBI:26642`; the final `CAS:7783-00-8` token matches
  `chemical_properties.cas_rn`.
- The raw CultureMech `Role:`/`Properties:` synonym is correctly filtered from
  final SSSOM.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:H2seo3` to
  `CHEBI:26642`.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, occurrence
  statistics, CultureMech role facet, and final SSSOM row are present and
  consistent.

## Recommended Edits

- None.
