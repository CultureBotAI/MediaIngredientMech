# `data/ingredients/mapped/P-aminobenzoic_Acid.yaml`

## Verdict

Needs curation; major. The `CHEBI:30753` 4-aminobenzoic-acid identity, CAS-RN,
and CultureMech vitamin role pass, but the final SSSOM still exports a
concentration-qualified surface form and zwitterion labels as `other` tokens.

## Identity

- Reviewed record: `data/ingredients/mapped/P-aminobenzoic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:30753` with
  `ontology_mapping.ontology_id: CHEBI:30753`, label
  `4-aminobenzoic acid`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `kg_microbe_node_id: CHEBI:30753`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 2,270 CultureMech occurrences across 2,269 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data --labels` exited 0 across this
  five-record CHEBI batch.
- The final SSSOM row was inspected directly and maps
  `MIM:P-aminobenzoic_Acid` exactly to `CHEBI:30753`.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:30753` as active
  `4-aminobenzoic acid` and reports CAS `150-13-0`, formula `C7H7NO2`, the
  InChI, and the SMILES stored in the YAML.
- The kg-microbe synonyms that describe the neutral 4-aminobenzoic-acid
  compound, including `PABA`, `gamma-Aminobenzoic acid`, and
  `Para-aminobenzoic acid`, match live ChEBI synonyms for `CHEBI:30753`.
- The `VITAMIN_SOURCE` role is supported by the CultureMech database's
  original `Vitamin` role across many imported occurrences; unlike a
  name-pattern role, this is source-backed database evidence.
- The raw `Role: Vitamin; Properties: ...` strings are correctly filtered out
  of the final SSSOM.
- The final SSSOM wrongly keeps a microgram-per-microliter concentration label
  as a synonym. That token is a one-off recipe surface, not a canonical or
  same-substance synonym for the neutral compound.
- Fresh exact OLS4 searches for `4-ammoniobenzoate` and
  `4-aminobenzoic acid zwitterion` both resolve to separate `CHEBI:194474`,
  not to neutral `CHEBI:30753`. The YAML backfilled
  `4-ammoniobenzoate`, `4-azaniumylbenzoate`, and
  `4-aminobenzoic acid zwitterion` should not be exported in `other` for this
  record.

## Completeness

- The active ChEBI term, CAS-RN, neutral formula and structure, CultureMech
  occurrence count, and exact final SSSOM object agree.
- The duplicate-merge history explains why several equivalent spelling and
  capitalization variants are retained; those variants are not the problem.
- The auto-proposed PubMed mapping evidence is weak, because it only mentions
  the compound in a ketoconazole cocrystal context. The CultureMech and
  ChEBI-backed identity evidence are sufficient without relying on that PMID.

## Recommended Edits

- Major: in `data/ingredients/mapped/P-aminobenzoic_Acid.yaml`, remove the
  microgram-per-microliter concentration surface from active `synonyms`, or
  preserve it only as non-exported occurrence provenance, then rebuild the
  final SSSOM and rerun `scripts/validate_sssom_invariants.py` plus the
  id-label product check to prove it no longer appears in `other`.
- Major: move `4-ammoniobenzoate`, `4-azaniumylbenzoate`, and
  `4-aminobenzoic acid zwitterion` out of active `synonyms`, preserve them
  only as rejected or historical provenance if useful, and rebuild the final
  SSSOM so `MIM:P-aminobenzoic_Acid` no longer publishes zwitterion labels as
  neutral-acid synonyms.
- Minor: remove or rephrase the auto-proposed PMID `31986050` ontology
  evidence so a p-aminobenzoic-acid cocrystal paper is not presented as
  support for the CultureMech mapping decision.
