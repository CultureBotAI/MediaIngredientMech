# `data/ingredients/mapped/Glutamic_Acid.yaml`

## Verdict

Needs curation. The stereounspecific `CHEBI:18237` glutamic-acid identity, the
CultureMech nitrogen-source role, and the raw role-text filtering in the final
SSSOM pass, but the record carries the L-glutamic-acid CAS RN `56-86-0` and the
final SSSOM exports that stereospecific CAS plus DL-prefixed surfaces in
`other` on the generic ChEBI row.

## Identity

- Reviewed record: `data/ingredients/mapped/Glutamic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:18237` with matching
  `ontology_mapping.ontology_id`, canonical label `glutamic acid`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties model stereounspecific glutamic acid by formula
  `C5H9NO4` and an InChI with no stereochemical layer.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Glutamate.yaml data/ingredients/mapped/Glutamic_Acid.yaml data/ingredients/mapped/Glutamyl-glutamic_Acid.yaml data/ingredients/mapped/Glutaraldehyde.yaml data/ingredients/mapped/Glutarate.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Glutamate.yaml data/ingredients/mapped/Glutamic_Acid.yaml data/ingredients/mapped/Glutamyl-glutamic_Acid.yaml data/ingredients/mapped/Glutaraldehyde.yaml data/ingredients/mapped/Glutarate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five ChEBI-primary records in the batch.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry carries
  the same ChEBI exact match, CultureMech occurrence count, raw role-text
  synonyms, exact synonyms, nitrogen-source role, L-glutamic-acid CAS value, and
  chemical structure as the per-record YAML.
- OLS4 resolves `CHEBI:18237` as `glutamic acid`, matching the YAML
  `ontology_mapping`.
- The CultureMech role facet is source-backed: the `NITROGEN_SOURCE` role keeps
  `reference_type: DATABASE_ENTRY` and cites the imported original role text.
- Major: `chemical_properties.cas_rn: 56-86-0` belongs to an isomeric PubChem
  record with IUPAC name `(2S)-2-aminopentanedioic acid` and InChI layer
  `/t3-/m0/s1`; that CAS denotes L-glutamic acid, not the stereounspecific
  `CHEBI:18237` record.
- Major: the final `mappings/ingredient_mappings.sssom.tsv` row exports
  `CAS:56-86-0`, `DL-Glutamic acid`, and `DL-Glutaminic acid` in `other`.
  Those surfaces describe a stereospecific L-CAS and DL/racemate labels rather
  than confirmed synonyms for the generic MIM subject.
- The raw `Role: ...; Properties: ...` CultureMech strings are still present in
  YAML for provenance, but the final SSSOM correctly omits them from `other`.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `reports`, and `.claude` found the active YAML, aggregate copies, final SSSOM
  row, the synonym-enrichment review row, related L/D/glutamate salt records,
  generated indexes, old batch validation reports, and ignored aggregate
  backups.

## Completeness

- The generic ChEBI identity, CultureMech occurrences, source-backed
  nitrogen-source role, formula, InChI, SMILES, and final SSSOM row are
  populated.
- The CAS RN and exported stereochemical synonyms need curation before the
  record's registry and synonym payload are form-safe.

## Recommended Edits

- Major: remove `chemical_properties.cas_rn: 56-86-0` from
  `data/ingredients/mapped/Glutamic_Acid.yaml` unless the record is re-grounded
  to L-glutamic acid; the existing `CHEBI:18237` identity should not retain an
  L-specific CAS.
- Major: demote or remove `DL-Glutamic acid` and `DL-Glutaminic acid` from the
  active exact-synonym set so the final SSSOM no longer publishes those
  racemate labels as synonyms for the generic record.
- Major: rebuild the final SSSOM from the curated YAML so
  `CAS:56-86-0` and the DL-prefixed labels disappear from the `other` field.
