# `data/ingredients/mapped/Arsenate.yaml`

## Verdict

Needs curation; severity major. The CHEBI grounding and structure identify
`arsenate(3-)`, but the synonym list and published SSSOM `other` payload also
carry arsenite and pathway labels that are not aliases of arsenate.

## Identity

- Reviewed record: `data/ingredients/mapped/Arsenate.yaml`.
- Identifier and grounding: `identifier: CHEBI:29125` with
  `ontology_mapping.ontology_id: CHEBI:29125`, `ontology_source: CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, and `mapping_status: MAPPED`.
- OLS resolves `CHEBI:29125` to non-obsolete ChEBI `arsenate(3-)`; the term has
  CAS xref `15584-04-0`, formula `AsO4`, InChI
  `InChI=1S/AsH3O4/c2-1(3,4)5/h(H3,2,3,4,5)/p-3`, and SMILES
  `O=[As]([O-])([O-])[O-]`, all matching the record.
- PubChem resolves CAS `15584-04-0` to CID `27401` with the same InChI and the
  equivalent arsenate SMILES `[O-][As](=O)([O-])[O-]`.
- `ingredient_type: SINGLE_INGREDIENT` fits the fixed arsenate ion identity.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Arsenate.yaml data/ingredients/mapped/Artepaulin.yaml data/ingredients/mapped/Artificial_Sea_Salt.yaml data/ingredients/mapped/Artificial_seawater.yaml data/ingredients/mapped/Ascomycin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Arsenate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `runoak -i ols:chebi info CHEBI:29125 CHEBI:29582` and
  `runoak -i ols:chebi aliases CHEBI:29125 CHEBI:29582`: unavailable because
  `runoak` is not on PATH in this shell; direct OLS and PubChem `curl` checks
  were used instead.
- OLS4 term lookup for `CHEBI:29125`: resolved the current ChEBI label, CAS
  xref, formula, InChI, SMILES, and exact/related synonyms.
- Quoted OLS4 searches for `arsenite` and `dihydrogen arsenite`: resolved the
  arsenite strings carried by this record to the separate ChEBI arsenite branch,
  including `CHEBI:29242` `arsenite(1-)`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id/label pairs corresponded and 104 non-blocking plausibility
  warnings were reported.
- `uv run --frozen python scripts/check_flat_export_coverage.py`: passed; docs
  data were fresh and every curated label was resolvable.

## Evidence

- Supported: `Arsenate`, `Arsenate ion`, `arsorate`,
  `tetraoxidoarsenate(3-)`, `tetraoxoarsenate(3-)`, and
  `tetraoxoarsenate(V)` are present on `CHEBI:29125` in OLS.
- Unsupported and wrong-scope: `dihydrogen arsenite`, `H2AsO3(-)`,
  `[AsO(OH)2](-)`, `arsenite`, `arsenite(1-)`, and
  `dihydroxidooxidoarsenate(1-)` denote `arsenite(1-)` or other arsenite ions,
  not arsenate. They are present in the YAML and in
  `mappings/ingredient_mappings.sssom.tsv` row 479.
- Unsupported and wrong-scope: `reduction: arsenate detoxification` is a
  pathway label from the kg-microbe import, not a chemical synonym.
- Unsupported as a synonym: `(after autoclaving)` is only an instruction
  fragment from a CultureMech surface form. A hidden, ignored-inclusive search
  across the checkout, excluding stale `data/curated/backups` and review output,
  did not find a maintained source occurrence that would make the fragment a
  valid synonym.

## Completeness

- The exact ChEBI identity, formula, structure, CAS xref, occurrence counts,
  SSSOM row, and aggregate copy are present.
- No component decomposition, ingredient role, environment entry, dataset, or
  discussion is needed for this single arsenate ion record.
- The consequential gap is not missing coverage; it is over-coverage of the
  synonym and SSSOM `other` surfaces by arsenite/pathway strings.

## Recommended Edits

- In `data/ingredients/mapped/Arsenate.yaml`, remove the arsenite labels,
  `reduction: arsenate detoxification`, and `(after autoclaving)` from
  `synonyms`.
- Run the supported per-record sync so
  `data/curated/mapped_ingredients.yaml`,
  `mappings/ingredient_mappings.sssom.tsv`, and generated docs/data label
  products drop the same invalid `other` labels.
- Rerun the focused strict and term validators, `validate_sssom_invariants.py`,
  `check_flat_export_coverage.py`, and the label-index/product checks to prove
  the arsenite aliases no longer resolve through `MIM:Arsenate`.
