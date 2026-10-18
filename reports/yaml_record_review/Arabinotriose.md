# `data/ingredients/mapped/Arabinotriose.yaml`

## Verdict

Needs curation. The CAS-backed PubChem and ChEBI structures, synonym-match
grounding, exact ChEBI synonym, CAS registry row, SSSOM, and aggregate copy pass,
but the `CARBON_SOURCE` role is still only a provisional name-pattern
inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Arabinotriose.yaml`.
- Active local identity: `identifier: cas:89315-59-3`, preferred term
  `Arabinotriose`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- `ontology_mapping` targets `CHEBI:62799` with label
  `alpha-L-Araf-(1->5)-alpha-L-Araf-(1->5)-alpha-L-Araf`, source `CHEBI`, and
  `mapping_quality: SYNONYM_MATCH`.
- Local OAK resolves `CHEBI:62799` to the same formula `C15H26O13`, InChI,
  and InChIKey `OUGBMVAQMSBUQH-BGHOBRCPSA-N` stored in the record, and returns
  the stored exact ChEBI synonym.
- PubChem resolves stored `pubchem_cid: 53356682` to the stored formula,
  SMILES, InChI, and InChIKey; PubChem's CAS-RN xref for `89315-59-3` also
  includes CID `53356682`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Arabinogalactan.yaml data/ingredients/mapped/Arabinose.yaml data/ingredients/mapped/Arabinotriose.yaml data/ingredients/mapped/Arabinoxylan_Rye_Flour.yaml data/ingredients/mapped/Arabitol.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Arabinotriose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:27569 CHEBI:22599 CHEBI:62799 CHEBI:18403`:
  returned formula, SMILES, InChI, and InChIKey metadata for `CHEBI:62799`.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:27569 CHEBI:22599 CHEBI:62799 CHEBI:18403`:
  returned the canonical `alpha-L-Araf-(1->5)-alpha-L-Araf-(1->5)-alpha-L-Araf`
  label and the stored exact ChEBI synonym for `CHEBI:62799`.
- `curl -L https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/53356682/property/MolecularFormula,CanonicalSMILES,InChI,InChIKey/JSON`:
  returned the stored formula, SMILES, and InChI for CID `53356682`.
- `curl -L https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/xref/RN/89315-59-3/cids/JSON`:
  returned CID `53356682` among the CAS-RN xrefs.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The #326 repair regraded the old identical-formula parent from `NARROW_MATCH`
  to `SYNONYM_MATCH`; the record formula and PubChem InChIKey still match
  `CHEBI:62799`.
- `mappings/ingredient_mappings.sssom.tsv` rows 462-463 publish the exact ChEBI
  row and the exact CAS registry row for `89315-59-3`.
- `mappings/ingredient_mappings_row_review_manifest.tsv` classifies the
  ChEBI synonym-enrichment row as already represented and the CAS row as an
  expected registry identifier.
- The only `nutritional_roles` evidence cites `Inferred from curated media-role
  name pattern` and explicitly marks the carbon-source role as provisional, so
  the current role is not supported by claim-level source evidence.
- A hidden, ignored-inclusive search across the full checkout, excluding the
  old `data/curated/backups` snapshots and noncanonical batch-review output,
  found the active YAML, aggregate copy, generated docs, SSSOM rows, and
  row-review rows.

## Completeness

- CAS, PubChem CID, formula, SMILES, InChI, exact ChEBI synonym, curation
  history, `ingredient_type`, SSSOM registry row, and the aggregate copy are
  populated.
- Source occurrence counts are intentionally zero because this is a CultureBotHT
  CAS fallback rather than a media recipe ingredient.
- No component, environmental context, discussion, or dataset entry is needed.
- The unsupported carbon-source role is the only consequential gap.

## Recommended Edits

- In `data/ingredients/mapped/Arabinotriose.yaml`, remove
  `nutritional_roles.CARBON_SOURCE` unless direct source evidence for
  Arabinotriose as a carbon source is attached to that role.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`,
  `uv run linkml-term-validator validate-data data/ingredients/mapped/Arabinotriose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
