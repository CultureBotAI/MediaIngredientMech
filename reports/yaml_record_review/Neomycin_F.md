# `data/ingredients/mapped/Neomycin_F.yaml`

## Verdict

Pass. The manual `CHEBI:81287` Paromomycin II grounding is active, `Neomycin
F` is a ChEBI synonym for that term, the structure agrees with ChEBI and
PubChem, and the final exact SSSOM row emits no unsafe `other` text.

## Identity

- Reviewed record: `data/ingredients/mapped/Neomycin_F.yaml`.
- Identifier and grounding: `identifier: CHEBI:81287` with
  `ontology_mapping.ontology_id: CHEBI:81287`, label `Paromomycin II`, source
  `CHEBI`, `mapping_quality: SYNONYM_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 0 CultureMech recipe occurrences and 1 MicrobeDecoder source
  occurrence.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Neomycin_F` through `Netilmycin`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:81287` as active `Paromomycin II`,
  lists `Neomycin F` as a synonym, and reports formula `C23H45N5O14`, CAS
  `51795-47-2`, and the same InChI and SMILES as the record.
- A fresh PubChem CAS lookup for `51795-47-2` resolves to a compound with the
  same formula and InChI, confirming the chemical block.
- `mapping_quality: SYNONYM_MATCH` accurately records that the record label
  resolves through a ChEBI synonym rather than the canonical label; the final
  `skos:exactMatch` predicate is still correct under Rule D.
- The final SSSOM row maps `MIM:Neomycin_F` exactly to `CHEBI:81287` and emits
  no `other` synonym noise.

## Completeness

- The active ChEBI term, synonym evidence, formula, structure,
  MicrobeDecoder occurrence, empty CultureMech occurrence count, and final
  exact row agree.
- No role, component, or environment assertions are present; those optional
  slots are appropriately empty for the imported trait record.

## Recommended Edits

- None.
