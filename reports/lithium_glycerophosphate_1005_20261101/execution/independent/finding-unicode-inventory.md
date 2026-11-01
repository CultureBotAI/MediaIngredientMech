The first actual Step 4 dependency-chain dispatch for #1005 stopped before invoking any native build command because the run-owned inventory guard parsed Git filenames incorrectly.

`native_chain.py` uses `git ls-tree -r --name-only BASE data/ingredients`, splits on newlines, and retains strings ending in `.yaml`. Git quotes and escapes non-ASCII filenames by default, so five existing owners end in a closing quote and are dropped. The actual ignored-inclusive filesystem inventory contains the unchanged 2,955 owners; the parsed baseline contains only 2,950. This falsely reports changed membership.

Affected existing names include `L-α-phosphatidylinositol_From_Glycine_Max_Soybean.yaml`, `Α-lipoic_Acid.yaml`, `Α1-Acid_Glycoprotein_From_Bovine_Plasma.yaml`, `Poly-ß-hydroxybutyric_Acid.yaml`, and `Α-D-Glucose_Monohydrate.yaml`.

Evidence: driver SHA256 `75c29e50c75fd6ee4acfc5c2b8402da634ee286f7ae8054958e656b368a21a13`; base `838d0c2627552b0094545ebb580b5bb9b1a84d57`; failed native dispatch log `output/approved-plan-20261101T031134Z/logs/step4-dispatch-chain-build.log` SHA256 `3d4f1b110a70aaa4d37ee91a6267df49cfcbae1f3976cb23a91c64f32d3c0241`. The separate post-application comparison already verified one changed owner and 2,954 unchanged owners. No native chain output was produced by this failed dispatch.

Severity: low, false refusal in execution guard. Use Git's NUL-delimited filename output and parse exact filename bytes/text without quote interpretation. Add a regression using real Git entries with non-ASCII filenames, and retain rejection of actual added/removed owner paths. Independently re-review before rerunning the chain. This is a run-owned driver defect, not a request to rename ingredient files or weaken ignored-file inventory coverage.
