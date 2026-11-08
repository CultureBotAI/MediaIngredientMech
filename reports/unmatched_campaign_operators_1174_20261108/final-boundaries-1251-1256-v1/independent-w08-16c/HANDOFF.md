# Independent exact16c code review

Verdict: **needs_curation**. Complete review of PR1205 head `16c39b63bc95d3e7978ddccc6280b0d57954f4a5` retains two major findings:

- Existing `REJECTION-CODE-001` / #1255: quoted Git path parsing rejects legitimate Unicode/control-character owner changes after mutation.
- New `W08-16C-CODE-002`: live application does not retain the accepted HEAD/clean baseline after prepare. A later unrelated committed change can be hidden by comparing against moving HEAD and still produce a complete receipt.

The explicit demotion implementation and publisher removal paths are supported within tested scope, but the combined head is not accepted. The file-ready new finding was disclosed before any fix. No code was corrected here.

337 distinct focused cases passed across two runs: 197 source +131 publication initially, then all9 real integration cases with zero skips. The initial9 native lock failures remain. Native private workspace configuration fixed only that harness context. Additional independent controls comprise19 source,31 publisher-stage and5 root baseline scenarios. Actual27-receipt preservation and held431→436→435 lineage were checked.

The native structured review binds27 committed16c inputs,23 private evidence inputs and5 targets. Exact prior W04 finding pairs and all historical severities remain. See `native-validation.json` for the bounded native reader context and exact pair hashes.

Entry PRhead was16c; exit PRhead was `7a990e36b0e08d1deff943fe58bdc40d24d3834f`. The successor was not reviewed. I stayed16c, J stayedeac, CLAW stayed76c and W08 stayedae1. Exact Git tar and all14,723 original extracted files remain unchanged;29 added private bytecode caches are retained and inventoried. Prior sealed design/source/review packets were preserved.

Root owns deduplication, issue filing, corrections and successor acceptance. No maintained application, source-science, whole-owner, mapping, role or export approval. Ready for collection.
