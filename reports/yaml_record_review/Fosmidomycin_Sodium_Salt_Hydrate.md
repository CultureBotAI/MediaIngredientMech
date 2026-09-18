# `data/ingredients/mapped/Fosmidomycin_Sodium_Salt_Hydrate.yaml`

## Verdict

Needs curation, with major SSSOM synonym and unsupported-role issues. The
CAS-backed identity row and close match to the anhydrous ChEBI sodium-salt
parent are intentional, but the parent row exports an anhydrous ChEBI synonym
as if it were a synonym of the hydrate subject, and `SELECTIVE_AGENT` is still
only a provisional name-pattern prediction.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Fosmidomycin_Sodium_Salt_Hydrate.yaml`.
- Identifier and grounding: `identifier: cas:66508-37-0` with
  `ontology_mapping.ontology_id: CHEBI:201600`, label
  `Fosmidomycin sodium salt`, source `CHEBI`,
  `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- The close match is appropriate: the record represents a hydrate/CAS registry
  identity and `CHEBI:201600` is the anhydrous `Fosmidomycin sodium salt`
  parent. The August 2026 #342 event correctly changed the ChEBI predicate from
  `skos:narrowMatch` to `skos:closeMatch`.
- PubChem lookup by CAS RN `66508-37-0` resolved to CID 5141362 titled
  `Fosmidomycin Sodium` with formula `C4H9NNaO5P` and the same InChI recorded
  under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Formatetrimethylamine.yaml data/ingredients/mapped/Formic_Acid.yaml data/ingredients/mapped/Fortimicin_B.yaml data/ingredients/mapped/Fosfomycin.yaml data/ingredients/mapped/Fosmidomycin_Sodium_Salt_Hydrate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- LinkML term validation passed for the three CHEBI-primary records in this
  batch and was intentionally skipped for this CAS-primary close-match record
  because the Engine A/OBO primary-ID check does not cover CAS registry CURIEs.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:201600`:
  returned the active ChEBI label, formula, InChI, SMILES, mass, and exact
  synonym for the anhydrous sodium-salt parent.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  CAS identifier, close ChEBI parent mapping, structure fields, CAS RN,
  ingredient type, provisional selective-agent role, and anhydrous-parent
  synonym as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` output has the expected
  two-row shape: `MIM:Fosmidomycin_Sodium_Salt_Hydrate skos:closeMatch
  CHEBI:201600` plus a `skos:exactMatch` CAS registry row for
  `cas:66508-37-0`.
- Major: the close-match row exports
  `sodium;3-[ormyl(hydroxy)amino]propyl-hydroxyphosphinate` in `other`. That
  token comes from the anhydrous `CHEBI:201600` parent and is not a true
  synonym for the hydrate subject; it also reproduces ChEBI's misspelled parent
  synonym.
- Major: `physicochemical_roles.SELECTIVE_AGENT` has only
  `COMPUTATIONAL_PREDICTION` evidence from the curated media-role name pattern
  and the evidence note explicitly says the role is provisional.
- `mappings/hydrate_review.tsv` accepts `cas:66508-37-0` as the current target
  but leaves an action of `NEEDS_SOURCE`: the source label says only `hydrate`,
  so the original recipe or supplier is still needed to resolve any concrete
  water stoichiometry.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` correctly triages the
  CAS identity row as an expected registry identifier rather than a missing OBO
  term.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports`, excluding prior per-record review reports and
  historical aggregate backups, found the active YAML, aggregate copy, two
  final SSSOM rows, hydrate-review rows, row-review entries, unknown-term
  triage rows, and generated batch findings.

## Completeness

- The CAS registry identity, close anhydrous ChEBI parent, PubChem structure,
  and registry exact SSSOM row are populated.
- Hydrate stoichiometry remains intentionally unresolved until source or
  supplier inspection narrows the bare hydrate label to a specific form.

## Recommended Edits

- Major: prevent anhydrous-parent synonyms from exporting as `other` on the
  `CHEBI:201600` close-match row for
  `data/ingredients/mapped/Fosmidomycin_Sodium_Salt_Hydrate.yaml`; sync
  `data/curated/mapped_ingredients.yaml`, regenerate
  `mappings/ingredient_mappings.sssom.tsv`, and rerun the SSSOM invariant
  gates.
- Major: either replace `physicochemical_roles.SELECTIVE_AGENT` with inspected
  source-backed evidence for fosmidomycin sodium salt hydrate, or remove the
  unsupported role.
- Minor: inspect the original supplier or recipe source for
  `Fosmidomycin sodium salt hydrate` and record the hydrate stoichiometry if it
  can be resolved.
