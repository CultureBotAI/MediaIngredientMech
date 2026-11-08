`data/ingredients/mapped/Nh42so4.yaml` carries `(NH4)2S4` as an active EXACT_SYNONYM of ammonium sulfate. This oxygen-free formula does not establish sulfate identity. The current `main` owner retrieved on 2026-11-08 has SHA256 `1806053b7d0adc25bd2d1a84f0aeae92185a69f84d2db46abe816c75c21db48d`, identical to the frozen campaign file.

[MediaDive ingredient 1902](https://mediadive.dsmz.de/ingredients/1902) leads to [JCM medium 826](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=826), whose original first row also prints `(NH4)2S4`, 1.3 g. Therefore checking the original recipe does not supply the missing oxygen or justify silently interpreting the source as `(NH4)2SO4`. The captured JCM response SHA256 is `63aa07eb253c6d8c98dd77996ece5ed908071ece832096f8a374f31f7b382795`.

Follow-up: retain the literal source text as provenance and quarantine this alias as REJECTED_LABEL on the sulfate owner. Keep the sulfate identity itself unchanged. The source case remains unresolved until provider clarification or reagent evidence distinguishes a source error from a different intended sulfur compound. Do not mint an exact sulfate association from lexical similarity or medium plausibility.

Worker03 has prepared a bounded isolated alias proposal, with primary follow-up and separate skeptical review, under `reports/all_unmatched_20261107/worker-03/chemicals/`. No maintained owner or export was edited. Guarded integration, fresh complete changed-owner review and the inherited native holds remain required.

Deduplication: the all-state indexed search for `(NH4)2S4`, `Nh42so4` and JCM826 found only closed #607, which removed `Original amount: ...` note labels. Its body and comments were checked; it does not address this formula alias.
