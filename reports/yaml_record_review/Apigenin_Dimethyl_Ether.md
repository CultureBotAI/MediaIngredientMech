# `data/ingredients/mapped/Apigenin_Dimethyl_Ether.yaml`

## Verdict

Needs curation. The record conflates three different chemical identities: the
label says Apigenin Dimethyl Ether, the ChEBI parent is the small molecule
dimethyl ether / methoxymethane, and the active CAS/PubChem chemistry denotes
`4-(2-cyanophenyl)benzoic Acid`. That wrong-parent/wrong-structure mixture
makes the active SSSOM export denote the wrong thing.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Apigenin_Dimethyl_Ether.yaml`.
- Active local identity: `identifier: cas:5728-44-9`, preferred term
  `Apigenin Dimethyl Ether`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- `ontology_mapping` targets `CHEBI:28887` with label `dimethyl ether`,
  source `CHEBI`, and `mapping_quality: NARROW_MATCH`.
- Local OAK and EBI OLS resolve `CHEBI:28887` to methoxymethane with formula
  `C2H6O`, SMILES `COC`, exact synonym `Methoxymethane`, and CAS `115-10-6`.
- PubChem resolves the record CAS `5728-44-9` and the stored
  `pubchem_cid: 10727789` to `4-(2-cyanophenyl)benzoic Acid`, formula
  `C14H9NO2`.
- PubChem's name lookup for `Apigenin Dimethyl Ether` resolves to
  `5-Hydroxy-7,4'-dimethoxyflavone`, CID `5281601`, and formula `C17H14O5`,
  not the active CAS/CID structure.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Apidaecin_IB.yaml data/ingredients/mapped/Apigenin.yaml data/ingredients/mapped/Apigenin_Dimethyl_Ether.yaml data/ingredients/mapped/Apiole.yaml data/ingredients/mapped/Apple_Juice.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Apigenin_Dimethyl_Ether.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:18388 CHEBI:28887 CHEBI:70353`:
  returned formula `C2H6O`, SMILES `COC`, InChI, InChIKey, and CAS
  `115-10-6` for `CHEBI:28887`.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:18388 CHEBI:28887 CHEBI:70353`:
  returned `Methoxymethane` as an exact ChEBI synonym of `CHEBI:28887`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/ingredient_mappings_oak_ols_review.tsv` already showed the active
  ChEBI row was only a `SYNONYM_ENRICH` row against `CHEBI:28887` `dimethyl
  ether`, not evidence that apigenin dimethyl ether is chemically near
  methoxymethane.
- `mappings/ingredient_mappings.sssom.tsv` rows 444-446 publish the bad
  `skos:narrowMatch` to `CHEBI:28887`, an exact CAS registry row for
  `5728-44-9`, an exact kg-microbe registry row, and exact other-surface
  `Methoxymethane`.
- `mappings/ingredient_mappings_row_review_manifest.tsv` classified the
  Methoxymethane synonym-enrichment row as `ALREADY_REPRESENTED`, but that only
  explains why the synonym is present; it does not make Methoxymethane a synonym
  of Apigenin Dimethyl Ether.
- A hidden, ignored-inclusive search across `data`, `src`, `tests`,
  `mappings`, `scripts`, and non-review `reports` found the active YAML,
  aggregate copy, SSSOM rows, row-review rows, and no active
  apigenin-dimethyl-ether record grounded to a flavone-shaped identifier.

## Completeness

- The aggregate copy matches the per-record YAML, including the bad
  methoxymethane parent, `Methoxymethane` exact synonym, and unrelated
  `C14H9NO2` PubChem structure.
- Source occurrence counts are intentionally zero because this is a CultureBotHT
  CAS fallback rather than a media recipe ingredient.
- No role, environmental context, discussion, or dataset entry is needed until
  the chemical identity is corrected.

## Recommended Edits

- In `data/ingredients/mapped/Apigenin_Dimethyl_Ether.yaml`, remove the
  `CHEBI:28887` parent, the `Methoxymethane` synonym, and the CID `10727789`
  chemistry. Decide whether CAS `5728-44-9` was a source error; if the surface
  label is authoritative, ground it to a flavone-shaped Apigenin Dimethyl Ether
  identity such as PubChem CID `5281601` or a new exact local CAS fallback.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`,
  `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Apigenin_Dimethyl_Ether.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
