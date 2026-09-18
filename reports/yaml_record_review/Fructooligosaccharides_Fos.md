# `data/ingredients/mapped/Fructooligosaccharides_Fos.yaml`

## Verdict

Needs curation, with major identity and final-SSSOM defects. The record's
subject is `Fructooligosaccharides (FOS)`, but its CAS RN, PubChem structure
fields, ChEBI parent, and exported `FRUCTOSE` synonym all collapse the oligomer
surface onto the beta-D-fructose monomer.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Fructooligosaccharides_Fos.yaml`.
- Identifier and grounding: `identifier: cas:308066-66-2` with
  `ontology_mapping.ontology_id: CHEBI:28645`, label
  `beta-D-fructofuranose`, source `CHEBI`, `mapping_quality: NARROW_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- PubChem lookup by CAS RN `308066-66-2` resolved to CID 439709 titled
  `beta-D-fructose` with formula `C6H12O6` and the same InChI recorded under
  `chemical_properties`; that is a fructose monomer, not the
  `Fructooligosaccharides (FOS)` oligomer surface.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Fradicin.yaml data/ingredients/mapped/Framycetin.yaml data/ingredients/mapped/Fraxetin.yaml data/ingredients/mapped/Fructooligosaccharides_Fos.yaml data/ingredients/mapped/Fructose-6-phosphate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- LinkML term validation passed for the four OBO/external-prefix records in
  this batch and was intentionally skipped for this CAS-primary record because
  the Engine A/OBO primary-ID check does not cover CAS registry CURIEs.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:28645 CHEBI:15946 CHEBI:7508 CHEBI:5169`:
  returned beta-D-fructofuranose metadata showing that `CHEBI:28645` has
  formula `C6H12O6`, CAS xref `53188-23-1`, and exact synonym `FRUCTOSE`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  CAS identifier, beta-D-fructofuranose parent mapping, monomeric structure
  fields, computational carbon-source role, ingredient type, and parent synonym
  as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` output has three rows for
  the subject: `skos:narrowMatch` to `CHEBI:28645`, an exact CAS registry row,
  and a local exact `kgmicrobe.compound:fructooligosaccharides_fos` registry
  row.
- Major: `cas:308066-66-2` and the populated `chemical_properties` describe
  beta-D-fructose rather than the FOS oligomer identity in `preferred_term`.
- Major: the `CHEBI:28645` parent mapping is wrong for FOS. A fructose oligomer
  has fructose-like monomeric parts but is not a narrower term under the
  single-molecule beta-D-fructofuranose identity.
- Major: final SSSOM exports `FRUCTOSE` in `other` on the `CHEBI:28645`
  narrow-match row. That is a synonym of the parent monomer, not a true synonym
  of `Fructooligosaccharides (FOS)`.
- Major: `nutritional_roles.CARBON_SOURCE` has only
  `COMPUTATIONAL_PREDICTION` evidence from the curated media-role name pattern
  and the evidence note explicitly says the role is provisional.
- The hidden/ignored-inclusive search found the separate
  `Fructooligosaccharides from chicory` unmapped record, but its exact-label
  audit also found no OLS hit and it does not resolve this CAS/FOS mapping.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports`, excluding prior per-record review reports and
  historical aggregate backups, found the active YAML, aggregate copy, three
  final SSSOM rows, unknown-term triage rows, row-review entries, the
  cross-record `FRUCTOSE` baseline, label-index precedence regression tests,
  and the unmapped chicory FOS record.

## Completeness

- The current exact CAS row, structure fields, ChEBI parent row, and
  carbon-source role do not reliably describe the FOS subject.
- Empty component and supplied-form slots leave the FOS oligomer composition
  underspecified; a future record likely needs a local identity plus component
  or polymer/oligomer semantics instead of a fructose monomer parent.

## Recommended Edits

- Major: replace `cas:308066-66-2` and the beta-D-fructose
  `chemical_properties` in
  `data/ingredients/mapped/Fructooligosaccharides_Fos.yaml` with a
  source-backed FOS identity; if no external exact term exists, mint or keep a
  local identity for the oligomer surface instead.
- Major: remove the `CHEBI:28645` `NARROW_MATCH` parent mapping unless a
  correct OBO parent for fructooligosaccharides is identified; regenerate final
  SSSOM so `FRUCTOSE` no longer appears in `other`.
- Major: remove the computational `CARBON_SOURCE` role or replace it with
  inspected claim-level evidence for FOS as a carbon source in media.
