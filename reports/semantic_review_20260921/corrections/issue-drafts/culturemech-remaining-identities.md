Destination: https://github.com/CultureBotAI/CultureMech/issues
Title: Regenerate remaining peptone and trypticase ingredient assignments after MIM corrections

A read-only audit of the current local normalized-recipe snapshot on 2026-09-21 found 109 active ingredient assignments still using rejected identities:

- 105 Trypticase and one Bacto-tryptone assignment use CHEBI:78018, dodecylphosphocholine.
- Three Peptone assignments use FOODON:03302071, green kidney bean.

The MIM review artifact `reports/semantic_review_20260921/corrections/downstream-remaining-identifiers.json` records every recipe ID, JSON pointer, source path, and SHA256. These are current-snapshot counts; the original 96/358 cohorts have not been reconstructed.

Regenerate the affected recipes and downstream occurrence/graph exports using the reviewed MIM identities, then verify that these assignments no longer use the rejected IDs. A corrected unified mapping alone does not establish recipe regeneration.
