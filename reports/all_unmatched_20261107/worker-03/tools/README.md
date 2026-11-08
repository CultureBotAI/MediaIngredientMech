These helpers operate only on the worker03 evidence lane. They do not integrate proposals, regenerate maintained exports, refresh an ontology or run a downstream build.

The recorded environment uses Python 3.13.2 and the unchanged frozen uv.lock. `audit_worker_outcomes_v1.py` is an exact copy of the campaign auditor; its original path and hash are in `provenance.json`. Use explicit shard, artifact, source and MIM roots and a new output receipt for each audit run.

Assembly order is `assemble.py`, `attach_reviews.py`, then `attach_bergey_supplement.py`. Original author bundles and separately authored review captures are immutable inputs. The last helper adds the independently assessed final two-case publisher followup without changing an outcome or proposal. Reassembly overwrites root campaign files, so it is unnecessary for review and should not be run casually on this frozen handoff.

`validate_proposals.py` performs read-only closed-schema, before-hash, appended-history, biological-role-preservation, full-catalog component and new active-identifier-collision checks. `test_validate_proposals.py` supplies six synthetic failure controls. `verify_final_surfaces.py` compares the exact baseline hashes and actual owner-file membership. `check_local_terms_final.py` inspects existing local ontology tables only; MICRO and NCIT supplemental coverage is recorded in `validation/final-id-label-coverage.json`.

`prepare_native_review.py` compiles only actual maintained owners through native inspect after final scientific and structural checks; its result must pass native validate/save. It records an honest self-reviewed compilation with separately attributed independent captures and verdict needs_curation. Source-only cases are excluded from that native owner profile. `write_handoff.py` derives inventories and handoff counts from final artifacts. The final non-author branch reviewer separately checks all root artifacts and staged paths.

Native source inspection binds the root core files and agent scopes. Changing those files after saving the native review requires a new native inspection/review; do not rewrite the historical saved pair.
