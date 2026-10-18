# `data/ingredients/mapped/Fusidic_Acid_Sodium_Salt.yaml`

## Verdict

Needs curation, with major synonym and unsupported-role issues. The CAS-backed
sodium-salt identity, local registry rows, and narrow parent mapping to fusidic
acid are internally coherent, but the record keeps acid-form exact synonyms on
the salt subject and exports one of them in final SSSOM `other`; its
`SELECTIVE_AGENT` role is also only a provisional computational prediction.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Fusidic_Acid_Sodium_Salt.yaml`.
- Identifier and grounding: `identifier: cas:751-94-0` with
  `ontology_mapping.ontology_id: CHEBI:29013`, canonical label `fusidic acid`,
  source `CHEBI`, `mapping_quality: NARROW_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- PubChem lookup by CAS RN `751-94-0` resolved to CID 23672955 for `Sodium
  fusidate` / `FUSIDIC ACID SODIUM SALT`, formula `C31H47NaO6`, and the same
  InChI recorded under `chemical_properties`.
- OLS4 resolved `CHEBI:29013` as the active fusidic acid parent term with
  formula `C31H48O6`, matching the record's intentionally broader ChEBI
  target rather than the sodium-salt registry subject.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Furazolidone.yaml data/ingredients/mapped/Furfuryl_Alcohol.yaml data/ingredients/mapped/Fusaric_Acid.yaml data/ingredients/mapped/Fusidate.yaml data/ingredients/mapped/Fusidic_Acid_Sodium_Salt.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Furazolidone.yaml data/ingredients/mapped/Furfuryl_Alcohol.yaml data/ingredients/mapped/Fusaric_Acid.yaml data/ingredients/mapped/Fusidate.yaml data/ingredients/mapped/Fusidic_Acid_Sodium_Salt.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five records.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same CAS
  identifier, narrow ChEBI parent, CAS RN, structure fields, source, inferred
  `SELECTIVE_AGENT` role, and ingredient type as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` output has the expected
  Rule B1 shape for the non-exact ontology mapping: `skos:narrowMatch` to
  `CHEBI:29013`, an exact CAS registry row, and an exact
  `kgmicrobe.compound:fusidic_acid_sodium_salt` registry row.
- `mappings/ingredient_mappings_row_review_manifest.tsv` marks the CAS row and
  local kg-microbe row as expected registry identifiers, and
  `mappings/ingredient_mappings_unknown_term_triage.tsv` records that neither
  row needs OAK/OLS repair.
- Major: both active synonyms erase the salt boundary. `Fusidic acid` is the
  acid parent, and the long IUPAC synonym imported from `CHEBI:29013` is also
  the neutral acid form; the final SSSOM parent row exports that acid-form
  IUPAC in `other`, even though every published `other` token must name the
  sodium-salt MIM subject.
- Major: `physicochemical_roles.SELECTIVE_AGENT` is supported only by
  `COMPUTATIONAL_PREDICTION` from a curated name-pattern rule with a
  provisional curator note; no inspected source in the record supports the
  salt as a medium selective agent.
- PubChem's CID 23672955 synonym list resolves `CAS:751-94-0` to the sodium
  salt and includes several salt-specific aliases, but the attempted live OLS
  search for a newly added sodium-fusidate ChEBI term failed twice with DNS
  resolution errors.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports` found the active YAML, aggregate copy, final SSSOM
  rows, row-review decisions, synonym-enrichment decision, and expected
  unknown-term triage rows.

## Completeness

- The sodium-salt identity, CAS registry row, local exact registry row, broader
  fusidic-acid parent row, and PubChem structure fields are populated.
- The record still lacks reviewed salt-specific synonyms; the active acid
  synonyms should not stand in for the sodium-salt surface.
- Exact ChEBI availability remains a bounded recheck because the live OLS search
  endpoint was unavailable for that query during this review.

## Recommended Edits

- Major: in `data/ingredients/mapped/Fusidic_Acid_Sodium_Salt.yaml`, remove or
  retag acid-form synonyms so `Fusidic acid` and the acid-form IUPAC from
  `CHEBI:29013` no longer publish as exact synonyms for the sodium salt; sync
  `data/curated/mapped_ingredients.yaml`, regenerate final SSSOM, and rerun
  SSSOM invariants to prove the parent row no longer exports broader acid
  aliases.
- Major: replace the provisional `SELECTIVE_AGENT` role with source-backed
  evidence or remove it, then rerun strict validation.
- Minor: when OLS search is available, recheck `sodium fusidate` / `Fusidic
  acid sodium salt` and promote to an exact external term if ChEBI has added
  one since the CAS-fallback row was created.
