# `data/ingredients/mapped/Aesculetin.yaml`

## Verdict

Needs curation. The exact CAS registry identity is valid, but the record's
`FALLBACK_REGISTRY` mapping and "no CHEBI entry exists" evidence are now stale:
current ChEBI has exact compound `CHEBI:490095` for CAS `305-01-1`.

## Identity

- Reviewed record: `data/ingredients/mapped/Aesculetin.yaml`.
- Identifier and grounding: `identifier: cas:305-01-1` with
  `ontology_mapping.ontology_id: cas:305-01-1`, source `CAS`,
  `mapping_quality: FALLBACK_REGISTRY`, and `mapping_status: MAPPED`.
- PubChem resolves CAS `305-01-1` to CID `5281416`, title `Esculetin`, formula
  `C9H6O4`, SMILES `C1=CC(=O)OC2=CC(=C(C=C21)O)O`, and InChIKey
  `ILEDWLMCKZNDJK-UHFFFAOYSA-N`.
- Local OAK and the official ChEBI page resolve `CHEBI:490095` to `esculetin`
  with the same formula, InChIKey, CAS `305-01-1`, and related synonyms
  `Aesculetin` and `aesculetin`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Adipate.yaml data/ingredients/mapped/Adipic_Acid.yaml data/ingredients/mapped/Aesculetin.yaml data/ingredients/mapped/Agar.yaml data/ingredients/mapped/Agarose.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/Aesculetin.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  exited 1, so `just validate-terms` would skip Engine A for this non-OBO CAS
  fallback.
- `uv run --frozen runoak -i sqlite:obo:chebi search Aesculetin`: returned
  `CHEBI:490095 ! esculetin`.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:17128 CHEBI:30832 CHEBI:2509 CHEBI:2511 CHEBI:490095`:
  returned `Aesculetin` and `aesculetin` as related aliases of `CHEBI:490095`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:17128 CHEBI:30832 CHEBI:2509 CHEBI:2511 CHEBI:490095`:
  returned CAS `305-01-1`, formula, charge, SMILES, InChI, InChIKey, average
  mass, and monoisotopic mass for `CHEBI:490095`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- PubChem and ChEBI now agree that CAS `305-01-1` denotes esculetin /
  aesculetin.
- `mappings/ingredient_mappings.sssom.tsv` row 352 still maps
  `MIM:Aesculetin` to `cas:305-01-1` with `registry:cas` and trailer
  `none|UNKNOWN_TERM|2026-07-07`.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` and
  `mappings/ingredient_mappings_row_review_manifest.tsv` record the old padded
  `cas:0305-01-1` unknown-term review as an expected registry identifier; that
  result was valid only while no ChEBI term was available.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `src`, `tests`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found the
  active YAML, aggregate copy, CAS SSSOM row, stale unknown-term triage rows,
  generated indexes, and ignored aggregate backups.

## Completeness

- CAS and `ingredient_type` are populated, and the stripped CAS value has the
  correct check digit.
- The record is now missing the best ChEBI primary grounding and the
  structure-derived formula, SMILES, and InChI available from `CHEBI:490095`.
- No role, component, environmental context, discussion, occurrence, or dataset
  entry is needed.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- In `data/ingredients/mapped/Aesculetin.yaml`, promote the CAS fallback to
  `CHEBI:490095`, canonical `ontology_label: esculetin`, and a CAS-backed ChEBI
  mapping quality.
- Update the stale `ontology_mapping.evidence` note that says no ChEBI entry
  exists, add `chemical_properties` for `CHEBI:490095`/PubChem CID `5281416`,
  and keep `305-01-1` as a CAS xref rather than the primary mapping.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`, `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Aesculetin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  `uv run --frozen python scripts/validate_component_partonomy.py`, and
  `uv run --frozen python scripts/validate_sssom_invariants.py`.
