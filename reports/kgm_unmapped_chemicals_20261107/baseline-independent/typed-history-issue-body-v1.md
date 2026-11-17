The three older typed companion-refresh paths reject the current canonical policy history before they can inspect a successor update. At MIM `0dac278466699129a083343a921c2e0ca18a9ab4`, `mappings/ingredient_mappings.sssom.tsv.manifest.json` legitimately contains `owned_name_suppression_updates` from the completed deferred-alias publication. `_verify_policy_projection` in `src/mediaingredientmech/ingredient_bundle_refresh.py` admits only the form, registry-correction and stock-CAS update keys. Its strict shape check therefore raises `Form projection: unknown manifest shape` for the actual current manifest in all three contexts.

This is a fail-closed successor compatibility defect, not a failure of the current release: the current native reviewed SSSOM export and replay both pass. It matters when a later authorized correction needs an explicit typed manifest successor. Removing the owned-name history or bypassing the verifier would lose provenance and is not an acceptable remedy.

Verified source pins:

- Shared verifier SHA256: `cd85ce90c88bb69b05d618492af6bdc7d27adfa12ca1a5c753bb223207ff4f32`.
- Current manifest SHA256: `6b6fe48246bd43dd70499e82f508a7b7ea0fcd121bccafafa0217aae84a17778`.
- Independent private probe: `.temp/kgm-unmapped-20261107/reviewer/probe_typed_history_v1.py` and `typed-history-proof-v1.json`.

The probe calls each native verifier with the exact current manifest and records the shape refusal. As a diagnostic control only, removing that one key in an in-memory copy reaches the later append-only guard instead. It changes no maintained file and does not claim that an incomplete synthetic successor should pass.

Acceptance requires preserving the existing owned-name history byte-for-byte as an immutable unrelated history for these typed successors, retaining each context's existing narrow scientific/receipt contract, and regression tests that reject omitted, altered or reordered retained history. A true alias-addition successor requires its own bounded contract; it must not masquerade as the existing `hydrate_parent_predicate` form transition. No owner merge, scientific approval, gate weakening or broader scope is authorized by this issue.
