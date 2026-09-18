# `data/ingredients/mapped/Vitamin_B12.yaml`

## Verdict

Needs curation. The broad `CHEBI:176843` vitamin B12 vitamer identity and
source-backed vitamin role pass, but final SSSOM exports cyanocobalamin-specific
child labels plus malformed kg-microbe artifacts as `other` synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Vitamin_B12.yaml`.
- Identifier and grounding: `identifier: CHEBI:176843` with matching
  `ontology_mapping.ontology_id`, label `vitamin B12`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `68-19-9`.
- Synonyms: four raw CultureMech role/property strings plus 19 exact synonyms
  retained from the kg-microbe sweep, duplicate MIM records, and unmapped
  duplicate reviews.
- Occurrences: 2,408 CultureMech recipe occurrences across 2,406 media.
- Role: `VITAMIN_SOURCE` imported from CultureMech original role text.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Virginiamycin` through `Vitamin_K`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on this 5-file CHEBI
  batch exited 0.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:176843` returns active label `vitamin B12` and
  defines the term as a group of cobalamin vitamers with vitamin B12 activity,
  not specifically as the cyanocobalamin molecule.
- The active `Cyanocobalamin` record is mapped separately to `CHEBI:17439`; its
  review already flagged the reverse leakage of generic Vitamin B12 labels onto
  that specific cyanocobalamin row.
- The four raw `Role:`/`Properties:` CultureMech strings are filtered from final
  SSSOM `other`, as intended.
- The `VITAMIN_SOURCE` role is backed by `DATABASE_ENTRY` evidence carrying the
  original CultureMech role text `Vitamin Source`.

## Issues

- Major: the final SSSOM row
  `MIM:Vitamin_B12 skos:exactMatch CHEBI:176843` exports
  cyanocobalamin-specific strings, including `CN-Cbl`, `CO-CYANOCOBALAMIN`,
  `Cyanocob(III)alamin`, `Cyanocobalamin`, `Cyanocobalamine`, and
  `Dicopac`, as exact `other` labels for the broader vitamer class.
- Major: the same final SSSOM row still exports malformed kg-microbe artifacts
  that contain source fragments, non-breaking spaces, or list numbers rather
  than clean synonyms: the `Cyanocobalamin in` fragment and the numbered
  Vitamin B12 labels.
- Minor: the `LITERATURE` evidence item for PMID `37093107` is explicitly an
  auto-proposed placeholder whose snippet discusses circulating vitamin B12
  during pregnancy, not MIM-to-CHEBI identity. A hidden/ignored-inclusive search
  across `data`, `reports`, `.claude`, `mappings`, and `scripts` found this as
  part of a repeated auto-proposed-evidence pattern rather than a hand-curated
  source.

## Completeness

- The broad CHEBI mapping, occurrence count, source-backed vitamin role,
  aggregate copy, and exact SSSOM row agree.
- The final SSSOM synonym set needs to be restricted to labels for the broad
  vitamin B12 vitamer class; cyanocobalamin-specific names belong on the
  `Cyanocobalamin` record only where they are clean labels for `CHEBI:17439`.

## Recommended Edits

- Remove cyanocobalamin-specific, OCR-fragment, and numbered source-artifact
  labels from `data/ingredients/mapped/Vitamin_B12.yaml` so final SSSOM no
  longer publishes them on `CHEBI:176843`.
- Remove the auto-proposed PMID `37093107` `LITERATURE` evidence item from this
  record or replace it with a checked source only if literature evidence is
  genuinely needed beside the CultureMech database match.
- Rebuild SSSOM and rerun strict validation, LinkML term validation, SSSOM
  invariant validation, and the cross-record `other` synonym audit.
