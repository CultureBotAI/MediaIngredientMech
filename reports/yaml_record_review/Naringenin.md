# `data/ingredients/mapped/Naringenin.yaml`

## Verdict

Needs curation - major. The generic `CHEBI:50202` naringenin identity and final
exact row otherwise pass, but the stored CAS RN and published CAS alias resolve
to a stereospecific PubChem record while the stored ChEBI structure is
non-stereochemical.

## Identity

- Reviewed record: `data/ingredients/mapped/Naringenin.yaml`.
- Identifier and grounding: `identifier: CHEBI:50202` with
  `ontology_mapping.ontology_id: CHEBI:50202`, label `naringenin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 0 CultureMech recipe occurrences across 0 media; the record was
  created from CultureBotHT CAS input.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Naphthalene_Sulfonic_Acid` through `Natamycin`: exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:50202` as active generic
  `naringenin` with formula `C15H12O5` and the same non-stereochemical InChI
  and SMILES as the record.
- A fresh OLS4 search for `Naringenin` also exposes distinct child terms for
  `(S)-naringenin` and `(R)-naringenin`, so the generic/enantiospecific
  boundary is represented in ChEBI.
- Major: the stored `chemical_properties.cas_rn: 480-41-1` resolves in a fresh
  PubChem CAS lookup to a stereospecific naringenin structure, not to the
  non-stereochemical InChI stored from generic `CHEBI:50202`; the final SSSOM
  row also publishes `CAS:480-41-1` for the generic ChEBI subject.

## Completeness

- The active generic ChEBI term, formula, structure, IUPAC synonym, and final
  exact row agree apart from the CAS stereochemistry conflict.
- The remaining consequential gap is deciding whether the CultureBotHT input
  should denote generic naringenin or the stereospecific CAS-resolved form.

## Recommended Edits

- Major: verify the CultureBotHT source row for CAS `480-41-1`; either remove
  the CAS from this generic `CHEBI:50202` record or re-ground the record to the
  appropriate stereospecific ChEBI term before rebuilding final SSSOM.
