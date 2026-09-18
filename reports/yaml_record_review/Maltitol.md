# `data/ingredients/mapped/Maltitol.yaml`

## Verdict

Needs curation. The exact ChEBI identity, CAS number, ChEBI structure, exact
IUPAC synonym, and final SSSOM row pass, but `CARBON_SOURCE` is still
supported only by provisional ChEBI-ancestry evidence.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Maltitol.yaml`.
- Identifier and grounding: `identifier: CHEBI:68428` with
  `ontology_mapping.ontology_id: CHEBI:68428`, label `maltitol`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: zero CultureMech recipe occurrences.
- Chemical identity: `cas_rn: 585-88-6`, formula `C12H24O11`, InChI and
  SMILES copied from ChEBI.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Malt_Extract_Broth` through `Maltose`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for this
  CHEBI-primary record.

## Evidence

- EBI OLS4 resolves `CHEBI:68428` as active `maltitol` with CAS `585-88-6`,
  formula `C12H24O11`, and the same InChI and SMILES carried in the YAML.
- ChEBI carries `alpha-D-glucopyranosyl-(1->4)-D-glucitol` as an exact IUPAC
  synonym.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Maltitol` to
  `CHEBI:68428` with `alpha-D-glucopyranosyl-(1->4)-D-glucitol` and
  `CAS:585-88-6` in `other`.

## Completeness

- The identity, chemistry, exact synonym, and final SSSOM predicate are
  consistent.
- `CARBON_SOURCE` is backed only by `COMPUTATIONAL_PREDICTION` evidence from
  ChEBI carbohydrate ancestry with a provisional curator note.

## Recommended Edits

- Remove `CARBON_SOURCE` unless source-backed evidence for maltitol as a media
  carbon source can be attached.
