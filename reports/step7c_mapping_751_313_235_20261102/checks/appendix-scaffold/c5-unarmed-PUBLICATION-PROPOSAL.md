# One-use final appendix publication proposal

This is an unarmed invocation outside the maintained repository. It calls the
unchanged `scripts/step7a_guarded_publication.publish` under the repository's
native lock. No maintained publisher, workflow, source, generated product or
cleanup helper is changed or called. No W publication has occurred.

The draft expects the exact C5 head `9a8414ad88bbbb01c2a43995e3f0decb2e7f2a7e`.
Tracked work must still match C5. Only the separately saved, hash-bound native
review pair and the literal `reports/step7c_final_review_20261102/diagnostics.json`
may be untracked before publication. All three must be copied from the official
save without relocation or rewriting. Twenty-five explicit C5 inputs
are pinned in `protected-c5-inputs.json`: the six source owners, aggregate,
canonical and receipt24, the final #1114 test, native review/evidence and semantic report, active
companion, preserved policy/unified assets and committed primary evidence
packet. The one replaced README must still match its exact C5 preimage.

The selected input inventory must become `final_completed_local_validation`,
with the actual completed final suite and native review-check receipt/log pairs.
It may explicitly leave remote closure and the final documentation-delta review
pending. That qualification is mandatory: the native source review captured the
old README, and this publication is not a review of the final docs commit.

Only inventory files under `checks/` and `independent/`, the inventory bytes as
`final-validation.json`, and the replacement `README.md` can be published under
`reports/step7c_mapping_751_313_235_20261102/`. All evidence destinations must be
absent. The native pair and diagnostic are inputs, not outputs of this invocation. Each input,
output, original README, helper/runtime module and completed command/log binding
is checked. Native recovery retains an external README backup and journal.

Before execution, the coordinator must supply `publication-freeze.json` with:

- `head`, `scientific_approval_added: false`, `supervisor_binding: null`, and
  `documentation_delta_requires_final_head_review: true`;
- `inventory_path`, `inventory_sha256` for the exact completed final inventory;
- `readme_path`, `readme_sha256` for the final placeholder-free replacement;
- `native_review_pair`: the exact two relative paths and SHA-256 hashes already
  copied from the independent reviewer's official save;
- `native_review_diagnostic_sha256`: the hash of the separately copied literal
  `reports/step7c_final_review_20261102/diagnostics.json`; no alternative path is accepted;
- `required_command_pairs`: `full_suite` and `native_review_check`, each naming
  the exact selected relative `receipt` and `log` entries.

Pin that config's SHA-256 in `CONFIG_SHA256` only after all actual files exist.
The current `None` deliberately refuses even a dry run. Then freeze the script,
config and inventory together for review. Run a real dry run against W and a
private-copy probe using the same frozen actual inputs before the root applies.
Synthetic private fixtures are test data, not substitutes for those final steps.

Invocation after the reviewed final freeze (omit `--apply` for the actual dry run):

```
python3 RUN/run_step7c_mim.py step7c UNIQUE-TAG -- python -B \
  RUN/step7c-final-validation-appendix/invoke_final_appendix.py \
  --log RUN/step7c-final-validation-appendix/UNIQUE-RECEIPT.json [--apply]
```

Use absolute `RUN` paths in the command; the runtime changes its working
 directory. Existing logs, backups, journals or evidence files must be preserved.

The prior C4 scaffold/inventory is preserved under `c4-unarmed-before-1114/`.
`inventory-proposal-c5-v1.json` retains the earlier failed/interrupted history
and adds `extra-completed-c4-history.json` with the failed full-suite-v2 receipt
and log. These are historical failures, never final successful validation.
Full-suite-v3, final C5 QC, and a fresh native final review remain pending.
