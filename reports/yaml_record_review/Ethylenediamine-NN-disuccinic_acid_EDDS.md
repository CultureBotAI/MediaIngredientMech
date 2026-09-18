# `data/ingredients/mapped/Ethylenediamine-NN-disuccinic_acid_EDDS.yaml`

## Verdict

Needs curation, with major duplicate-identity and final-SSSOM synonym issues.
The comma-split MicrobeDecoder label was correctly rejoined as an EDDS label,
but the record now overlaps the CAS-backed EDDS record and still exports the
two raw split fragments as published synonyms.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Ethylenediamine-NN-disuccinic_acid_EDDS.yaml`.
- Identifier and grounding: `identifier:
  kgmicrobe.compound:ethylenediamine_n_n_disuccinic_acid` with matching
  `ontology_mapping.ontology_id`, source `kgmicrobe.compound`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and one
  MicrobeDecoder BacDive metabolite-production occurrence.
- The current preferred term, `Ethylenediamine-N,N'-disuccinic acid (EDDS)`, is
  an EDDS surface form, but `data/ingredients/mapped/Ethylenediamine-NN-disuccinic_Acid.yaml`
  already represents the same EDDS identity with CAS RN `20846-91-7` and a
  PubChem-backed structure.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ethylenediamine-NN-disuccinic_acid_EDDS.yaml data/ingredients/mapped/Ethylenediamine_N_N_Prime_Disuccinic_Acid.yaml data/ingredients/mapped/Ethylmalonic_Acid.yaml data/ingredients/mapped/Eudesmic_Acid.yaml data/ingredients/mapped/Eugenol.yaml --out /tmp/mim_edds_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- Engine A term validation was skipped for this record because the ontology ID
  uses the local `kgmicrobe.compound` prefix rather than an OBO prefix.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  local identifier, MicrobeDecoder occurrence, raw split-fragment synonyms,
  moved-to-mapped history, and fallback registry row as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Ethylenediamine-NN-disuccinic_acid_EDDS` to
  `kgmicrobe.compound:ethylenediamine_n_n_disuccinic_acid` with
  `skos:exactMatch`.
- Major: the final SSSOM `other` column publishes `Ethylenediamine-N` and
  `N'-disuccinic Acid (EDDS)`. Those are parser fragments from a comma-split
  source label, not synonyms of EDDS.
- Major: the active mapped corpus now has this local EDDS row plus the
  CAS-backed `cas:20846-91-7` EDDS row. The hidden/ignored-inclusive search
  also found the rejected `N'-disuccinic Acid (EDDS)` half in
  `data/ingredients/unmapped`, which confirms that the fragment was already
  retired into this local representative.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, and `reports/yaml_record_review` for
  `Ethylenediamine-N,N`, `ethylenediamine_n_n`, `EDDS`,
  `cas:20846-91-7`, and related labels found the active local EDDS row, the
  CAS-backed EDDS row, the kg-microbe placeholder EDDS-like row, the rejected
  split-fragment row, final SSSOM rows for the active mapped records, and
  ignored aggregate backups.

## Completeness

- The MicrobeDecoder source occurrence and comma-split repair history are
  traceable.
- The record is missing `ingredient_type`, and its top-level import `notes`
  still say "Curator review needed" even though the record has been moved to
  the mapped collection. Both should be cleaned up as part of the same merge or
  representative repair.

## Recommended Edits

- Major: merge or re-point this record to the CAS-backed
  `data/ingredients/mapped/Ethylenediamine-NN-disuccinic_Acid.yaml`
  representative, preserve the MicrobeDecoder occurrence and comma-split
  provenance there, remove the raw split-fragment active synonyms, sync
  `data/curated/mapped_ingredients.yaml`, regenerate
  `mappings/ingredient_mappings.sssom.tsv`, and rerun strict validation plus
  the final SSSOM invariant gates.
