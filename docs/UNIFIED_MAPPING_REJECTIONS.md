# Reviewed source IDs in the unified export

`mappings/unified_mapping_rejections.tsv` records source identifiers that curation
has explicitly rejected for a MIM identity. It is consumed by claw's
`scripts/build_unified_ingredient_mapping.py` during `just rebuild-unified`.

The columns are `ingredient_name`, `rejected_id`, `mim_id`, and `reason`.
The ingredient name must resolve to the stated current MIM identity. The reason
must cite the curation evidence. Rejections apply to all source labels resolving
to that identity; they do not globally ban the rejected identifier. A genuine
dodecylphosphocholine record may still use `CHEBI:78018`.

For a reviewed rejection, the producer ignores the rejected source ID during
record lookup and when populating `chebi_id` and `culturemech_term_id`. It retains
the corrected MIM identity. The original source identifier remains in this ledger
and in the CultureMech source recipes as provenance, outside the export's active
identity columns. The TSV schema is unchanged. Other cross-ontology disagreements
retain the existing publication policy until reviewed.

After changing the ledger, rebuild with an updated claw checkout, run
`just check-unified-rejections`, and commit the generated TSV and provenance
sidecar together. A malformed ledger or disagreement with the current MIM record
fails generation. MIM CI also checks the published artifact independently of claw
so an older producer cannot stamp a known-bad mapping and pass merely because it
is fresh. `just rebuild-unified` runs this check before stamping.
