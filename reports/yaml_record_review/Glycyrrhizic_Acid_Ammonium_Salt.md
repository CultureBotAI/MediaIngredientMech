# `data/ingredients/mapped/Glycyrrhizic_Acid_Ammonium_Salt.yaml`

## Verdict

Pass. The CAS-primary ammonium glycyrrhizate identity, PubChem-backed ammonium
salt structure, narrow parent mapping to `CHEBI:15939`, registry identity rows,
rejected parent-derived synonym, and final SSSOM payload all agree.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Glycyrrhizic_Acid_Ammonium_Salt.yaml`.
- Identifier and grounding: `identifier: cas:53956-04-0` for the exact
  ammonium salt with `ontology_mapping.ontology_id: CHEBI:15939`, canonical
  label `glycyrrhizinic acid`, source `CHEBI`,
  `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: PubChem CID `62074`, CAS-RN `53956-04-0`, formula
  `C42H65NO16`, the PubChem ammonium glycyrrhizate InChI, and the PubChem
  SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Glycylglycine.yaml data/ingredients/mapped/Glycylglycylglycine.yaml data/ingredients/mapped/Glycyrrhizic_Acid_Ammonium_Salt.yaml data/ingredients/mapped/Glyoxylate.yaml data/ingredients/mapped/Gold_Iii_Chloride_Hydrate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Glycyrrhizic_Acid_Ammonium_Salt.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry is
  identical to the split per-record YAML.
- PubChem resolves CAS `53956-04-0` to CID `62074` and lists that CID with
  synonyms including `AMMONIUM GLYCYRRHIZINATE`,
  `Glycyrrhizic acid, ammonium salt`, and `53956-04-0`, formula
  `C42H65NO16`, and the same InChI and SMILES as the record.
- OLS4 resolves `CHEBI:15939` as `glycyrrhizinic acid`, CAS `1405-86-3`, and
  formula `C42H62O16`, confirming that the CHEBI target is the acid parent and
  not the ammonium salt.
- The current `CURATOR_JUDGMENT` evidence documents the 2026-09-12 repair from
  the acid's CAS to `cas:53956-04-0` and intentionally keeps `CHEBI:15939` as a
  narrow parent.
- The ChEBI IUPAC label inherited from the acid is retained as
  `REJECTED_LABEL`, and the three final `mappings/ingredient_mappings.sssom.tsv`
  rows contain only the parent `skos:narrowMatch`, the exact CAS registry row,
  and the exact `kgmicrobe.compound:glycyrrhizic_acid_ammonium_salt` row.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, `conf`, `docs`, and `.claude` found the active YAML, the
  counterion repair script, matching aggregate copies, generated products,
  final SSSOM rows, row-review TSVs, and ignored aggregate backups.

## Completeness

- The local CAS identity, PubChem CID, CAS RN, formula, InChI, SMILES, ChEBI
  parent, parent/registry SSSOM rows, rejected parent-specific synonym, and
  counterion curation history are populated.
- No role facet is asserted, which is acceptable for this record.

## Recommended Edits

- None.
