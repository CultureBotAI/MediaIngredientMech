# Unified table refresh for SSSOM finalization

The 39-record synonym correction in PR #731 takes the shared unified table beyond
its allowed drift budget. Regenerate it from current MIM records and the local
CultureMech recipe snapshot before stamping freshness.

This uses the previously reviewed
[`corrections/rebuild_unified.py`](../corrections/rebuild_unified.py) workflow:
stage only direct ingredient records, exclude rejected records whose names remain
on their representatives, apply the explicit rejected-ID ledger, and verify that
all input bytes remain unchanged during the build. The new wrapper differs only
in its description and output evidence location. Historical build evidence is
preserved.

Inputs:

- CultureBotAI/culturebotai-claw commit
  `a566cf8a26ab14c1a94301a29d0eba130b0629a6`,
  `scripts/build_unified_ingredient_mapping.py`.
- CultureMech commit `866b335301a53838c2868515e68ec96a11528f17`, read only.
- Current MIM records and `mappings/unified_mapping_rejections.tsv`.

The rebuilt table retains all 3,870 rows. Exactly 43 rows lose rejected activity
phrases from their synonym fields; identifiers, occurrence counts and all other
columns are unchanged. Reviewed rejected-ID checks and freshness checks pass.

`unified-build.json` records the exact producer, wrapper, recipe, record and output
hashes. Run the wrapper with `--builder`, `--culturemech` and `--output` paths,
then `scripts/check_unified_rejections.py` and the freshness stamp/check. This
refresh does not establish that downstream media have been regenerated and does
not make the unified table a scientifically approved SSSOM mapping set.
