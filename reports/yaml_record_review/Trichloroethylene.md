# `data/ingredients/mapped/Trichloroethylene.yaml`

## Verdict

Needs curation, major. The exact CHEBI identity, CAS RN, PubChem structure,
real synonyms, occurrence count, aggregate row, and final SSSOM row pass, but a
concentration-qualified methanol-stock label leaks into final SSSOM `other`.

## Identity

- Reviewed record: `data/ingredients/mapped/Trichloroethylene.yaml`.
- Identifier and grounding: `identifier: CHEBI:16602` with matching
  `ontology_mapping.ontology_id`, label `trichloroethene`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `79-01-6`.
- Synonyms: fifteen exact kg-microbe synonyms plus raw CultureMech stock label
  `Trichloroethylene (10 mg/ml in methanol)`.
- Occurrences: 2 CultureMech recipe occurrences in 2 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tribenuron-methyl` through `Tricine`: exited 0 and wrote zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh exact OLS4 search for `trichloroethene` returns `CHEBI:16602` with
  label `trichloroethene`.
- Fresh PubChem lookup for CAS `79-01-6` returns formula `C2HCl3` and the same
  InChI as the YAML.
- The final SSSOM row has
  `MIM:Trichloroethylene skos:exactMatch CHEBI:16602` and exports the
  concentration-qualified `Trichloroethylene (10 mg/ml in methanol)` surface in
  `other` alongside true synonyms and the CAS token.

## Issues

### Major: final `other` exports a methanol-stock label

`Trichloroethylene (10 mg/ml in methanol)` denotes a prepared stock or recipe
input, not the pure trichloroethene molecule. Concentration- and
solvent-qualified labels must stay out of final SSSOM synonyms.

## Completeness

- The CHEBI identity, CAS RN, structure fields, occurrence count, aggregate
  copy, and real ChEBI/kg-microbe synonyms agree.
- The only issue is the raw concentration-qualified alias leaking into final
  `other`.

## Recommended Edits

- Mark `Trichloroethylene (10 mg/ml in methanol)` as non-exportable raw source
  text so the final SSSOM row keeps only true synonyms.
