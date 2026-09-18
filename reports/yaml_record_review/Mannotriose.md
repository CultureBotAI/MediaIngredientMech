# `data/ingredients/mapped/Mannotriose.yaml`

## Verdict

Needs curation. The exact generic ChEBI identity passes, but the final SSSOM
exports a CAS number for a more specific beta-D-mannotriose structure and
`CARBON_SOURCE` is only a provisional ChEBI-ancestry inference.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Mannotriose.yaml`.
- Identifier and grounding: `identifier: CHEBI:146181` with
  `ontology_mapping.ontology_id: CHEBI:146181`, label `mannotriose`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: zero CultureMech recipe occurrences.
- Chemical identifier: `cas_rn: 28173-52-6`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mannobiose` through `Marine_Broth_2216`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for this
  CHEBI-primary record.

## Evidence

- EBI OLS4 resolves `CHEBI:146181` as active generic `mannotriose`, defined as
  any trisaccharide composed of three mannose moieties, with no CAS xref or
  structure attached to the ChEBI term.
- PubChem resolves `28173-52-6` to CID 3082284 with formula `C18H32O16`,
  structural SMILES, and beta-D-mannotriose synonyms.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Mannotriose` to
  `CHEBI:146181` and exports `CAS:28173-52-6` in `other`.

## Completeness

- `CARBON_SOURCE` is only backed by a `COMPUTATIONAL_PREDICTION` inferred from
  `CHEBI:16646` carbohydrate ancestry. No source attached to the role verifies
  that mannotriose was deliberately supplied as a carbon source in a medium.
- CAS `28173-52-6` denotes a structured beta-D-mannotriose in PubChem, while
  `CHEBI:146181` deliberately remains generic across trisaccharides of three
  mannose moieties. Publishing that CAS on the generic MIM subject makes the
  final SSSOM row too specific.

## Recommended Edits

- Remove `chemical_properties.cas_rn: 28173-52-6` from `Mannotriose`, or split
  the CAS-backed beta-D-mannotriose into a narrower local registry record and
  keep `Mannotriose` generic.
- Curate recipe or literature evidence for `CARBON_SOURCE`, or remove the
  provisional nutritional role.
