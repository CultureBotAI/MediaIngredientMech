# Reviewed source IDs in the unified export

`mappings/unified_mapping_rejections.tsv` records source identifiers that curation
has explicitly rejected for a MIM identity or an exact source label. It is consumed by claw's
`scripts/build_unified_ingredient_mapping.py` during `just rebuild-unified`.

The columns are exactly `ingredient_name`, `rejected_id`, `mim_id`, and `reason`.
All four cells must be present. Only `mim_id` may be explicitly empty; a missing
cell is malformed. The reason must cite the curation evidence. The two scopes
follow the [merged Claw contract](https://github.com/CultureBotAI/culturebotai-claw/blob/0cc221bd0f4eb460030eb2e5d14b91a311ed2965/docs/guides/UNIFIED_MAPPING_REJECTIONS.md):

- With a nonempty `mim_id`, the ingredient name must resolve to that current MIM
  identity. Rejections apply to all source labels resolving to that identity.
- With an explicitly empty `mim_id`, the rejection applies only to the
  `ingredient_name` / `rejected_id` pair. Label comparison uses Unicode NFC,
  surrounding-whitespace trimming, and case folding. It preserves internal
  whitespace, concentrations, hydrates, stereochemistry, and parenthetical
  qualifiers. A hold cannot reject an independently resolved owner's own ID.

Neither scope globally bans the rejected identifier. A genuine
dodecylphosphocholine record may still use `CHEBI:78018`. Different source labels
may hold the same ID, and one label may hold several reviewed IDs.

For a reviewed rejection, the producer ignores the rejected source ID during
record lookup and when populating `chebi_id` and `culturemech_term_id`. It retains
the independently resolved MIM identity, when one exists. A source hold with no
independent owner prevents source-ID fallback from borrowing another record's
identity, synonyms, or metadata. It does not mint an identity or change YAML,
SSSOM, or the policy for unreviewed candidate alternatives. Source occurrence
counts and example media remain available. The original source identifier remains in this ledger
and in the CultureMech source recipes as provenance, outside the export's active
identity columns. The TSV schema is unchanged. Other cross-ontology disagreements
retain the existing publication policy until reviewed.

After changing the ledger, rebuild with an updated claw checkout, run
`just check-unified-rejections`, and commit the generated TSV and provenance
sidecar together. A malformed ledger or disagreement with the current MIM record
fails generation. MIM CI also checks the published artifact independently of claw
so an older producer cannot stamp a known-bad mapping and pass merely because it
is fresh. The checker enforces both scopes across `chebi_id`,
`culturemech_term_id`, `mim_id`, `kg_microbe_node_id`, and `cas_rn`, while retaining
the identity-preservation check for nonempty `mim_id` rows. An empty `mim_id`
does not match every unmapped export row. `just rebuild-unified` runs this check
before stamping.

The bounded source-hold cohort reviewed in [MIM #1025](https://github.com/CultureBotAI/MediaIngredientMech/issues/1025)
contains 33 label/ID pairs with no independent MIM owner. Its regression checks
require those labels to retain source counts and examples while publishing no
borrowed identity or synonym fields. The existing identity-scoped ledger entries
remain unchanged.
