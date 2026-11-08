# Historical validation schema for issue 1265

The canonical packaged `src/mediaingredientmech/schema/pre_mint_ingredient_snapshot.yaml`
is byte-identical to `mediaingredientmech.yaml` at pre-mint main
`0dac278466699129a083343a921c2e0ca18a9ab4`. This manifest records its source path,
SHA-256 and unchanged `mech_shared.yaml` dependency SHA-256.

Only historical replay modules explicitly opting into `pre_mint_schema` use
this test fixture. Original owner records, review receipts, source hashes and
scientific assertions remain unchanged. Current production record validation
and permanent-ID tests continue to require `mim_id`; the fixture supplies
neither IDs nor scientific approval. The separate production snapshot gate may
use the same frozen schema only for explicitly byte-bound historical snapshots.
