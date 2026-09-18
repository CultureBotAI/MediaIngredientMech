# `data/ingredients/mapped/Ethylenediamine_N_N_Prime_Disuccinic_Acid.yaml`

## Verdict

Needs curation, with a major duplicate-identity issue. The historical OLS
candidate rejection was sound for the unrelated CHEBI candidates, but the
kg-microbe placeholder label appears to be the same EDDS identity already
represented by the CAS-backed record.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Ethylenediamine_N_N_Prime_Disuccinic_Acid.yaml`.
- Identifier and grounding: `identifier:
  kgmicrobe.compound:ethylenediamine_n_n_prime_disuccinic_acid` with matching
  `ontology_mapping.ontology_id`, source `kgmicrobe.compound`,
  `mapping_quality: PLACEHOLDER`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- The May 2026 manual-candidate review correctly rejected unrelated
  ethylenediamine lexical hits, and a fresh exact CHEBI/NCIT query for
  `Ethylenediamine N N Prime Disuccinic Acid` returned 0 documents.
- This label encodes the same N,N-prime EDDS wording as the active
  `cas:20846-91-7` record and the MicrobeDecoder comma-split EDDS repair, so
  keeping a separate kg-microbe placeholder gives the final graph a third EDDS
  identity.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ethylenediamine-NN-disuccinic_acid_EDDS.yaml data/ingredients/mapped/Ethylenediamine_N_N_Prime_Disuccinic_Acid.yaml data/ingredients/mapped/Ethylmalonic_Acid.yaml data/ingredients/mapped/Eudesmic_Acid.yaml data/ingredients/mapped/Eugenol.yaml --out /tmp/mim_edds_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- Engine A term validation was skipped for this record because the ontology ID
  uses the local `kgmicrobe.compound` prefix rather than an OBO prefix.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  placeholder identifier, kg-microbe provenance, candidate-rejection note, and
  ingredient type as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Ethylenediamine_N_N_Prime_Disuccinic_Acid` to
  `kgmicrobe.compound:ethylenediamine_n_n_prime_disuccinic_acid` with
  `skos:exactMatch` and an empty `other` column.
- `mappings/ingredient_mappings_unknown_term_manual_candidate_review.tsv`
  records that the proposed CHEBI candidates were related but not EDDS identity
  terms.
- Major: the active mapped corpus already contains the CAS-backed EDDS row and
  the MicrobeDecoder EDDS repair row. This kg-microbe placeholder does not
  represent a distinct substance from those records.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, and `reports/yaml_record_review` for
  `Ethylenediamine N N Prime`, `ethylenediamine_n_n`,
  `Ethylenediamine-N,N`, and `EDDS` found this active placeholder, the
  CAS-backed EDDS row, the MicrobeDecoder EDDS row, final SSSOM rows for all
  three active mapped records, the UNKNOWN_TERM review row, the rejected split
  fragment, and ignored aggregate backups.

## Completeness

- The candidate-rejection provenance and final kgmicrobe row are populated.
- No roles, components, source occurrences, environmental contexts, or final
  SSSOM synonyms are asserted.

## Recommended Edits

- Major: merge or redirect this placeholder to the CAS-backed EDDS
  representative in
  `data/ingredients/mapped/Ethylenediamine-NN-disuccinic_Acid.yaml`, preserve
  the kg-microbe review provenance, sync `data/curated/mapped_ingredients.yaml`,
  regenerate `mappings/ingredient_mappings.sssom.tsv`, and rerun strict
  validation plus the final SSSOM invariant gates.
