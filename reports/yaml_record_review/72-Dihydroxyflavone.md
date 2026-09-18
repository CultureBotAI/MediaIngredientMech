# `data/ingredients/mapped/72-Dihydroxyflavone.yaml`

## Verdict

Pass, none. The CAS primary identity, exact same-structure ChEBI identity row,
PubChem chemistry, SSSOM rows, and aggregate copy pass.

## Identity

- Reviewed record: `data/ingredients/mapped/72-Dihydroxyflavone.yaml`.
- Identifier and grounding: `identifier: cas:77298-66-9` with
  `ontology_mapping.ontology_id: CHEBI:94071`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, and `mapping_status: MAPPED`.
- PubChem maps CAS `77298-66-9` to CID `5391149`, whose formula `C15H10O4` and
  InChIKey `NUGPQONICGTVNA-UHFFFAOYSA-N` match the stored chemistry.
- The official ChEBI page resolves `CHEBI:94071` to
  `7-hydroxy-2-(2-hydroxyphenyl)-1-benzopyran-4-one` with the same formula,
  InChI, and InChIKey.
- Local OAK metadata carries the same formula, structure strings, average mass,
  monoisotopic mass, and ChEBI label.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/6-methoxy-2_3h-benzoxazolone.yaml data/ingredients/mapped/7-Hydro-8-methylpteroylglutamylglutamic_Acid.yaml data/ingredients/mapped/7-hydroxyflavone.yaml data/ingredients/mapped/72-Dihydroxyflavone.yaml data/ingredients/mapped/8-azaguanine.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/72-Dihydroxyflavone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:173101 CHEBI:2268 CHEBI:94071 CHEBI:63486`:
  returned the expected ChEBI label for `CHEBI:94071`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:173101 CHEBI:2268 CHEBI:94071 CHEBI:63486`:
  returned the expected formula, structure strings, and mass for
  `CHEBI:94071`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- PubChem and ChEBI agree on formula, InChI, and InChIKey for the
  7,2'-Dihydroxyflavone identity; this supports the #326 regrade from
  `NARROW_MATCH` parent mapping to same-substance `SYNONYM_MATCH`.
- The initial CultureBotHT evidence row and `CREATED_FROM_CAS_FALLBACK` history
  record accurately preserve that the record started as a CAS fallback before
  the PubChem-mediated ChEBI xref was added.
- The SSSOM export has the expected exact identity row to `CHEBI:94071` and
  registry row to `cas:77298-66-9`.
- The hidden/ignored-inclusive search over `data`, `mappings`, `src`, `tests`,
  and `scripts` found the active YAML, aggregate copy, SSSOM rows, row-review
  rows for the ChEBI/CAS surfaces, the #326 regrade script allowlist, and
  ignored aggregate backups.

## Completeness

- CAS, formula, InChI, SMILES, PubChem CID, the same-structure ChEBI mapping,
  and `ingredient_type` are populated.
- No synonyms, roles, components, source occurrences, environmental context, or
  discussion entries need review.

## Recommended Edits

No YAML edit is required for this record.
