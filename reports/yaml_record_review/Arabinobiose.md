# `data/ingredients/mapped/Arabinobiose.yaml`

## Verdict

Needs curation. The CAS fallback identity, stored PubChem CID, MeSH parent,
formula, structure, SSSOM registry rows, and aggregate copy pass, but the
`CARBON_SOURCE` role is still only a provisional name-pattern inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Arabinobiose.yaml`.
- Active local identity: `identifier: cas:78088-21-8`, preferred term
  `Arabinobiose`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- `ontology_mapping` targets `mesh:C434937` with label `arabinobiose`, source
  `MESH`, and `mapping_quality: NARROW_MATCH`.
- EBI OLS resolves `mesh:C434937` to non-obsolete MeSH `arabinobiose`.
- PubChem resolves stored `pubchem_cid: 165359509` to formula `C10H18O9`, the
  stored SMILES and InChI, and InChIKey `BKTHPEZTBMTHCL-IJQGAOOBSA-N`;
  PubChem's CAS-RN xref for `78088-21-8` also includes CID `165359509`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Apramycin.yaml data/ingredients/mapped/Apramycin_Sulfate_Salt.yaml data/ingredients/mapped/Arabinan_From_Sugar_Beet.yaml data/ingredients/mapped/Arabinitol.yaml data/ingredients/mapped/Arabinobiose.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Arabinobiose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i ols:mesh term-metadata mesh:C434937`: unavailable;
  the adapter raised `NotImplementedError`, so the term was checked with a
  direct OLS request instead.
- `curl -L https://www.ebi.ac.uk/ols4/api/ontologies/mesh/terms/http%253A%252F%252Fid.nlm.nih.gov%252Fmesh%252FC434937`:
  resolved `mesh:C434937` to non-obsolete `arabinobiose`.
- `curl -L https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/165359509/property/MolecularFormula,CanonicalSMILES,InChI,InChIKey/JSON`:
  returned the stored formula, SMILES, and InChI for CID `165359509`.
- `curl -L https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/xref/RN/78088-21-8/cids/JSON`:
  returned CID `165359509` among the CAS-RN xrefs.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` records
  `mesh:C434937` as `RESOLVED_EXACT_CURIE` with OLS label `arabinobiose`,
  matching the active direct OLS check.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` classifies the old
  `mesh:C434937` UNKNOWN_TERM row as a missing prefix-validator coverage issue,
  not as a bad mapping; the CAS and kg-microbe exact rows are classified as
  expected registry identifiers.
- `mappings/ingredient_mappings.sssom.tsv` rows 457-459 publish a
  `skos:narrowMatch` to `mesh:C434937`, an exact CAS registry row for
  `78088-21-8`, and an exact kg-microbe registry row.
- The only `nutritional_roles` evidence cites `Inferred from curated media-role
  name pattern` and explicitly marks the carbon-source role as provisional, so
  the current role is not supported by claim-level source evidence.
- A hidden, ignored-inclusive search across the full checkout, excluding the
  old `data/curated/backups` snapshots and noncanonical batch-review output,
  found the active YAML, aggregate copy, SSSOM rows, row-review rows, and
  generated docs.

## Completeness

- CAS, PubChem CID, formula, SMILES, InChI, MeSH grounding, curation history,
  `ingredient_type`, SSSOM registry rows, and the aggregate copy are populated.
- Source occurrence counts are intentionally zero because this is a CultureBotHT
  CAS fallback rather than a media recipe ingredient.
- No component, environmental context, discussion, or dataset entry is needed.
- The unsupported carbon-source role is the only consequential gap.

## Recommended Edits

- In `data/ingredients/mapped/Arabinobiose.yaml`, remove
  `nutritional_roles.CARBON_SOURCE` unless direct source evidence for
  Arabinobiose as a carbon source is attached to that role.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`,
  `uv run linkml-term-validator validate-data data/ingredients/mapped/Arabinobiose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
