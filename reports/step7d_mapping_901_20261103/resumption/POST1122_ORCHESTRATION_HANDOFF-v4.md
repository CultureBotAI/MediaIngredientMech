# Post-1122 native refresh orchestration v4

Prepared externally only after issue [1126](https://github.com/CultureBotAI/MediaIngredientMech/issues/1126) was filed. No maintained refresh, source edit, test edit, or full native preflight has been executed by this author. The independent reviewer owns the fresh actual preflight.

## Correction and preserved guards

V4 differs from immutable v3 by exactly one assignment: baseline tracked inventory now uses `git ls-tree --name-only -z` and a NUL split with empty-item filtering. Current inventory already uses `git ls-files -z`. The exact set-equality guard remains unchanged. No scope, threshold, protected path or assertion is loosened. Git newline output had quoted exactly five Greek/ß filenames, falsely rejecting identical inventories. The failed v3 receipt and log remain unchanged.

All v3 behavior is retained, including the #1125 full graph path `output/mim-kgx-710-full` and final native manifest-binding assertion; all receipts1–24 and old Step7d reports remain frozen; only existing unpublished batch25 is used. The assembler endpoint replacement and paired companion-selector replacement remain exact guarded transactions. No source or snapshot regeneration occurs.

## Evidence

Nine external checks passed: exact one-expression diff; all remaining AST unchanged; real temporary Git fixture reproduces v3 failure; v4 accepts five Unicode names plus a space/newline path; missing Unicode member is rejected; added tracked member is rejected; quotePath=false also passes; actual protected membership is exactly3582=3582; original failed v3 receipt and log hashes remain intact. The temporary fixture was external to the maintained worktree. These controls are distinct from the pending independent full native preflight.

Frozen artifacts:

- `refresh_post1122_v4.py`: `76bb1e6a9dd8828a45c3033cfaa8c60651bf3a943c62998597e0562e898e98c7`
- `check_post1122_v4_membership.py`: `5fb7d8705dfb374b70eba1a742c3d252114449e89a4ec9b0082e56f0d18b550d`
- `post1122-orchestration-plan-v4.json`: `ea2d1aee4df6fe933446057c5a3687067e520164a9b7f4b11f1b3d9ce246f841`
- `post1122-orchestration-readonly-checks-v4.json`: `0f6ed8de4054e857c331267224688109daae6fed0a0c1378e75f5ec699f7e0c6`
- `post1122-orchestration-v4.diff`: `b8a9cfff53a81417854290efc407ca888b96a17baa11c9c3232f33802f5b5370`

## Root execution order

1. Keep the committed #1122 correction (canonical SHA `d3030e6385a2659a0dbd2c64ad5581568eecd9c10023f4a58de667e8050f20ef`, receipt25 SHA `45af9515590918e3420327668d4b89f564457cf97eea9404a34c4da7d17f0e4b`). HEAD may descend from durable baseline `7d35035f6c521c69fad94f73381c6a6eb7251fff`.
2. Obtain independent review and a passing actual v4 preflight.
3. Root runs v4 before any separately authorized #1123/#1124 test edits, preserving the frozen protected-input guard.
4. Only after native refresh completes may those separate issue-named test commits proceed. Root runs full QC and suite afterward.

```sh
python3 "$RUN/run_step7d_mim.py" step7d step7d-post1122-orchestrator-v1 -- python -B "$D/refresh_post1122_v4.py" --execute
```

The unused orchestration result/log names retain their v1 suffix. Each output must be absent; first failure stops and preserves outputs, receipts and journals without automatic retry, cleanup or rollback. V1, v2, v3 and their original evidence are preserved. No generalized allowance for test changes has been added.
