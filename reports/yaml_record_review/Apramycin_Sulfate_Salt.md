# `data/ingredients/mapped/Apramycin_Sulfate_Salt.yaml`

## Verdict

Needs curation. The CAS, PubChem CID, ChEBI sulfate structure, formula, exact
ChEBI synonym, exact CAS and kg-microbe registry rows, SSSOM invariants, and
aggregate copy pass, but the ChEBI sulfate relation is undergraded as a
`NARROW_MATCH` and the `SELECTIVE_AGENT` role is still only a provisional
name-pattern inference.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Apramycin_Sulfate_Salt.yaml`.
- Active local identity: `identifier: cas:65710-07-8`, preferred term
  `Apramycin sulfate salt`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- `ontology_mapping` targets `CHEBI:190734` with label `Apramycin sulfate`,
  source `CHEBI`, and `mapping_quality: NARROW_MATCH`.
- Local OAK resolves `CHEBI:190734` to non-obsolete ChEBI `Apramycin sulfate`
  with formula `C21H41N5O11.H2O4S`, a zero charge, the stored exact synonym,
  and SMILES/InChI for apramycin plus sulfuric acid.
- PubChem resolves stored `pubchem_cid: 3081544` to formula `C21H43N5O15S`,
  the stored SMILES and InChI, and InChIKey `WGLYHYWDYPSNPF-RQFIXDHTSA-N`;
  PubChem's CAS-RN xref for `65710-07-8` also includes CID `3081544`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Apramycin.yaml data/ingredients/mapped/Apramycin_Sulfate_Salt.yaml data/ingredients/mapped/Arabinan_From_Sugar_Beet.yaml data/ingredients/mapped/Arabinitol.yaml data/ingredients/mapped/Arabinobiose.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Apramycin_Sulfate_Salt.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:2790 CHEBI:190734 CHEBI:22605`:
  returned formula, SMILES, InChI, and InChIKey metadata for `CHEBI:190734`.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:2790 CHEBI:190734 CHEBI:22605`:
  returned the canonical `Apramycin sulfate` label and the stored exact
  structural synonym for `CHEBI:190734`.
- `curl -L https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/3081544/property/MolecularFormula,CanonicalSMILES,InChI,InChIKey/JSON`:
  returned the stored formula, SMILES, and InChI for CID `3081544`.
- `curl -L https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/xref/RN/65710-07-8/cids/JSON`:
  returned CID `3081544` among the CAS-RN xrefs.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The exact structural synonym is an exact ChEBI synonym for `CHEBI:190734`;
  its `suluric acid` typo is source-inherited rather than introduced locally.
- `mappings/ingredient_mappings.sssom.tsv` rows 450-452 publish a
  `skos:narrowMatch` to `CHEBI:190734`, an exact CAS registry row for
  `65710-07-8`, and an exact kg-microbe registry row.
- `mappings/ingredient_mappings_row_review_manifest.tsv` already classified
  the CAS and kg-microbe rows as expected registry identifiers and the ChEBI
  synonym-enrichment row as already represented.
- The CAS-backed ChEBI sulfate target is the same formula and structure as the
  PubChem record, so the current `NARROW_MATCH`/`skos:narrowMatch` understates
  the relation to `CHEBI:190734`.
- The only `physicochemical_roles` evidence cites `Inferred from curated
  media-role name pattern` and explicitly marks the selective-agent role as
  provisional, so the current role is not supported by claim-level source
  evidence.
- A hidden, ignored-inclusive search across the full checkout, excluding the
  old `data/curated/backups` snapshots and noncanonical batch-review output,
  found the active YAML, aggregate copy, SSSOM rows, row-review rows, generated
  docs, and no hidden CultureBotHT raw row for `65710-07-8`.

## Completeness

- CAS, PubChem CID, formula, SMILES, InChI, exact ChEBI synonym, curation
  history, `ingredient_type`, SSSOM registry rows, and the aggregate copy are
  populated.
- Source occurrence counts are intentionally zero because this is a CultureBotHT
  CAS fallback rather than a media recipe ingredient.
- No component, environmental context, discussion, or dataset entry is needed.
- The undergraded ChEBI sulfate relation and unsupported selective-agent role
  are the only consequential gaps.

## Recommended Edits

- In `data/ingredients/mapped/Apramycin_Sulfate_Salt.yaml`, promote the
  `CHEBI:190734` mapping from `NARROW_MATCH` to exact identity, or document a
  concrete chemical distinction that makes apramycin sulfate salt narrower than
  ChEBI `Apramycin sulfate`.
- In the same maintained record, remove `physicochemical_roles.SELECTIVE_AGENT`
  unless direct source evidence for Apramycin sulfate salt as a selective agent
  is attached to that role.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`,
  `uv run linkml-term-validator validate-data data/ingredients/mapped/Apramycin_Sulfate_Salt.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
