# `data/ingredients/mapped/Maltose.yaml`

## Verdict

Needs curation. The anomer-agnostic ChEBI identity, CAS number, structure,
CultureMech-backed carbon-source role, and rejected `Maltose x H2O` synonym
pass, but final SSSOM still exports a hydrate label and alpha-anomer-specific
labels as `other` synonyms, and `ENERGY_SOURCE` remains provisional.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Maltose.yaml`.
- Identifier and grounding: `identifier: CHEBI:17306` with
  `ontology_mapping.ontology_id: CHEBI:17306`, label `maltose`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 189 total occurrences in 188 CultureMech recipes.
- Chemical identity: `cas_rn: 69-79-4`, formula `C12H22O11`, InChI and SMILES
  copied from ChEBI.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Malt_Extract_Broth` through `Maltose`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for this
  CHEBI-primary record.

## Evidence

- EBI OLS4 resolves `CHEBI:17306` as active `maltose` with CAS `69-79-4`,
  formula `C12H22O11`, and the same InChI and SMILES carried in the YAML.
- The 2026-09-12 hydrate cleanup rejected `Maltose x H2O` on this anhydrous
  maltose record so hydrate labels no longer resolve to the anhydrous parent.
- The 2026-08-13 duplicate merge absorbed the lower-case `maltose` record that
  was grounded to `CHEBI:18167` `alpha-maltose` because the winner is the
  anomer-agnostic term.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Maltose` to
  `CHEBI:17306`.

## Completeness

- The primary identity, CAS, structure, exact predicate, and CultureMech
  `CARBON_SOURCE` evidence are consistent.
- Final SSSOM still exports `Maltose Hydrate` as an `other` value for
  anhydrous `MIM:Maltose`.
- Final SSSOM also exports alpha-anomer-specific labels, including
  `Alpha-maltose`,
  `alpha-D-glucopyranosyl-(1->4)-alpha-D-glucopyranose`, and
  `4-O-alpha-D-glucopyranosyl-alpha-D-glucopyranose`, on the generic maltose
  row.
- `ENERGY_SOURCE` is backed only by a `COMPUTATIONAL_PREDICTION` evidence
  block with a provisional curator note.

## Recommended Edits

- Reject or relocate the hydrate and alpha-anomer surface forms so final SSSOM
  only emits exact synonyms of anomer-agnostic maltose.
- Remove `ENERGY_SOURCE` unless source-backed evidence can be attached.
