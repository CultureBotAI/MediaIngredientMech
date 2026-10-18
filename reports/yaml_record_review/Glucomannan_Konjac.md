# `data/ingredients/mapped/Glucomannan_Konjac.yaml`

## Verdict

Needs curation, with major structure, synonym, and unsupported-role issues. The
CAS/local identity and broad `CHEBI:17020` glucomannan parent pass, but the
record stores a finite PubChem oligomer for a konjac glucomannan polymer,
final SSSOM exports an autoclaving phrase as a synonym, and `CARBON_SOURCE` is
still only a provisional name-pattern prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Glucomannan_Konjac.yaml`.
- Identifier and grounding: `identifier: cas:11078-31-2` with parent
  `ontology_mapping.ontology_id: CHEBI:17020`, canonical parent label
  `glucomannan`, source `CHEBI`, `mapping_quality: NARROW_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- OLS4 resolved `CHEBI:17020` as active glucomannan and confirmed it is a broad
  heteroglycan polymer class. The CAS record for konjac glucomannan remains a
  narrower registry/local identity rather than an exact ChEBI primary.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ginkgolide_A.yaml data/ingredients/mapped/Ginkgotoxin.yaml data/ingredients/mapped/Glebomycin.yaml data/ingredients/mapped/Glucomannan_Konjac.yaml data/ingredients/mapped/Gluconate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `Glucomannan_Konjac.yaml` was skipped for LinkML Engine A label validation
  because its primary identifier is the registry CURIE `cas:11078-31-2`;
  Engine B validates the record without asking OAK for a CAS ontology adapter.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry carries
  the same CAS primary, ChEBI narrow parent, PubChem CID, structure fields,
  raw autoclaved text, and provisional carbon-source role as the per-record
  YAML.
- The final SSSOM export correctly emits three rows: a `skos:narrowMatch` to
  `CHEBI:17020`, an exact CAS registry identity row, and an exact local
  kg-microbe registry row for the narrow-match subject.
- Major: `chemical_properties.pubchem_cid: 24892726`, formula `C24H42O21`,
  SMILES, and InChI describe a finite four-sugar oligosaccharide, while konjac
  glucomannan CAS `11078-31-2` is a polymeric glucomannan material and the only
  ontology mapping is a broad polymer parent.
- Major: final SSSOM exports `autoclaved, Glucomannan (konjac)` in `other` on
  the `CHEBI:17020` parent row. That is process-qualified recipe text, not a
  clean synonym of the broad glucomannan parent or the narrower konjac CAS
  record.
- Major: `nutritional_roles.CARBON_SOURCE` is supported only by a
  `COMPUTATIONAL_PREDICTION` whose reference text is an inferred curated
  media-role name pattern and whose curator note says the role is provisional.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports` found the active YAML, aggregate copies, final SSSOM
  rows, row-review rows, the MIM CURIE alias for the parenthetical local key,
  generated indexes, old batch validation reports, and ignored aggregate
  backups.

## Completeness

- The local CAS identity, broad ChEBI parent, and registry rows are populated.
- The finite structure fields, autoclaved synonym export, and carbon-source
  role need curator review.

## Recommended Edits

- Major: remove or replace the PubChem finite-oligomer structure fields unless
  evidence shows they describe CAS `11078-31-2` rather than just a representative
  small glucomannan fragment.
- Major: remove or retag `autoclaved, Glucomannan (konjac)` so final SSSOM no
  longer exports process-qualified recipe text as a synonym, then regenerate
  final SSSOM and rerun SSSOM invariants.
- Major: replace `CARBON_SOURCE` with source-backed evidence or remove the role,
  then rerun strict validation.
