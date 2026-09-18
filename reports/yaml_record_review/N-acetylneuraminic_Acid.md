# `data/ingredients/mapped/N-acetylneuraminic_Acid.yaml`

## Verdict

Pass. The exact `CHEBI:17012` N-acetylneuraminic acid identity, CultureBotHT CAS
provenance, MicrobeDecoder raw-label merge, ChEBI synonym, structure, and final
exact row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/N-acetylneuraminic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:17012` with
  `ontology_mapping.ontology_id: CHEBI:17012`, label
  `N-acetylneuraminic acid`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no direct CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `N-acetylneuraminate` through `N-decanoyl-DL-Homoserine_Lactone`: exited 0
  and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:17012` as active
  `N-acetylneuraminic acid`, with `cas:131-48-6`, formula `C11H19NO9`, the
  stored InChI/SMILES, and the curated IUPAC synonym.
- `mappings/edison_residual_merges.tsv` records
  `N-acetyl-neuraminic Acid` as a hyphenation variant of this same ChEBI term.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:N-acetylneuraminic_Acid` to `CHEBI:17012` with the IUPAC synonym, the
  merged raw hyphenation variant, and `CAS:131-48-6` in `other`.

## Completeness

- The active ChEBI target, CAS RN, structure, duplicate raw label, accepted
  synonym, and final row agree.
- The record does not assert components, roles, or non-synonym final `other`
  text.

## Recommended Edits

- None.
