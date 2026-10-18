# `data/ingredients/mapped/8-azaguanine.yaml`

## Verdict

Pass, none. The microbedecoder exact ChEBI identity, source occurrence, ChEBI
and PubChem chemistry, SSSOM row, and aggregate copy pass.

## Identity

- Reviewed record: `data/ingredients/mapped/8-azaguanine.yaml`.
- Identifier and grounding: `identifier: CHEBI:63486` with
  `ontology_mapping.ontology_id: CHEBI:63486`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- The official ChEBI page resolves `CHEBI:63486` to `8-azaguanine` with formula
  `C4H4N6O`, SMILES `Nc1nc(=O)c2nnnc2n1`, and InChIKey
  `LPXQRXLUHJKZIE-UHFFFAOYSA-N`.
- Local OAK metadata carries the same formula, structure strings, average mass,
  monoisotopic mass, CAS `134-58-7`, exact synonym
  `5-amino-3,6-dihydro-7H-[1,2,3]triazolo[4,5-d]pyrimidin-7-one`, and
  alternative ID `CHEBI:40862`.
- PubChem's InChIKey lookup resolves records with the same formula and same
  InChIKey as the ChEBI-backed local chemistry.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/6-methoxy-2_3h-benzoxazolone.yaml data/ingredients/mapped/7-Hydro-8-methylpteroylglutamylglutamic_Acid.yaml data/ingredients/mapped/7-hydroxyflavone.yaml data/ingredients/mapped/72-Dihydroxyflavone.yaml data/ingredients/mapped/8-azaguanine.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/8-azaguanine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:173101 CHEBI:2268 CHEBI:94071 CHEBI:63486`:
  returned the expected ChEBI label and exact synonym for `CHEBI:63486`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:173101 CHEBI:2268 CHEBI:94071 CHEBI:63486`:
  returned the expected formula, structure strings, CAS xref, and mass for
  `CHEBI:63486`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The active ChEBI term supports the exact `8-azaguanine` identity promoted from
  the microbedecoder exact-label import.
- PubChem resolves the ChEBI InChIKey to entries with the same `C4H4N6O`
  formula and `LPXQRXLUHJKZIE-UHFFFAOYSA-N` InChIKey.
- The source occurrence block preserves two `BacDive_Metabolite_production`
  microbedecoder occurrences from
  `data/custom/microbedecoder/unmapped_labels.tsv`.
- The SSSOM row maps `MIM:8-azaguanine` to `CHEBI:63486` with
  `skos:exactMatch` and the expected microbedecoder review provenance.
- The hidden/ignored-inclusive search over `data`, `mappings`, `src`, `tests`,
  and `scripts` found the active YAML, aggregate copy, SSSOM row,
  microbedecoder source rows, microbedecoder review row, and ignored aggregate
  backups.

## Completeness

- Formula, InChI, SMILES, ChEBI/PubChem chemistry, source occurrence counts,
  and `ingredient_type` are populated.
- No CAS field, synonyms, roles, components, environmental context, or
  discussion entries need review.

## Recommended Edits

No YAML edit is required for this record.
