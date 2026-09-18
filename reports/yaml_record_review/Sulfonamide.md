# `data/ingredients/mapped/Sulfonamide.yaml`

## Verdict

Needs curation - major. Active `CHEBI:35358` resolves and exact-matches the
record label, but it is the structural sulfonamide functional-group class; this
MicrobeDecoder record came from an antibiotic-resistance trait, was already held
as wrong-sense for that reason, and was later promoted back to `MAPPED` by the
comma-split repair.

## Identity

- Reviewed record: `data/ingredients/mapped/Sulfonamide.yaml`.
- Identifier and grounding: `identifier: CHEBI:35358` with
  `ontology_mapping.ontology_id: CHEBI:35358`, label `sulfonamide`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `NO2SR3`, ChEBI/PubChem InChI, ChEBI/PubChem
  SMILES, and molecular weight `78.071`.
- Occurrences: zero CultureMech recipe occurrences and 3 MicrobeDecoder
  antibiotic-resistance or antibiotic-sensitivity rows.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sulfite` through `Sulfur`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:35358` with label `sulfonamide`, a
  generic amide-of-sulfonic-acid meaning, and generic `NO2SR3` formula; that is
  consistent with the current CHEBI fields but too broad for an
  antibiotic-trait source row.
- The record history explicitly held this import for wrong-sense grounding
  because `CHEBI:35358` is the broad structural functional-group class while
  the provenance is `kgmicrobe.trait:sulfonamide`; the likely intended class is
  `CHEBI:87228` `sulfonamide antibiotic`.
- Major: `repair_comma_split_labels` promoted the same record back to `MAPPED`
  by rechecking the exact label against `CHEBI:35358`; that reproduced the
  lexical false positive already described by the prior review history.
- Major: the final SSSOM row exact-matches `CHEBI:35358`, so the final product
  still publishes the broad functional group for the MicrobeDecoder antibiotic
  trait.

## Completeness

- The aggregate row agrees with the per-record YAML, so this is not local YAML
  or SSSOM drift; the wrong-sense exact match is present in the source of
  truth.
- An ignored/hidden search of local curated, mapping, generated, report,
  source, and documentation paths found the expected MicrobeDecoder,
  aggregate, generated index, final SSSOM, wrong-sense hold, and comma-split
  repair rows; the evidence trail is sufficient to identify the re-promotion
  as a regression.

## Recommended Edits

- Major: review `data/ingredients/mapped/Sulfonamide.yaml` as a MicrobeDecoder
  antibiotic-trait record and either ground it to `CHEBI:87228` or hold it for
  expert review instead of publishing `CHEBI:35358`.
- Major: add a guard or reject-list entry to the comma-split repair path so a
  label that has already been held for wrong-sense review is not restored only
  because it is an exact lexical match.
- Major: regenerate `mappings/ingredient_mappings.sssom.tsv` after the YAML
  repair so the final SSSOM no longer exact-matches the broad sulfonamide
  functional group.
