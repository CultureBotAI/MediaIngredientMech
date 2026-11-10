# Current reviews and the immutable migration proof

Issue [#1325](https://github.com/CultureBotAI/MediaIngredientMech/issues/1325)
separates two required checks. The historical administrative ID migration keeps
its complete original proof and science. An ordinary current mapping/companion
review covers the actual endpoint, including every current external row and its
exact owner and evidence. Neither check confers new scientific approval.

The default `just qc-reviewed-sssom` and CI route remain `projected`; their
selectors and all original native projection assertions are unchanged. The new
entry point is `mediaingredientmech.validation.reviewed_export_route`. It only
reads and checks inputs. It does not prepare checkouts, export products, rewrite
reviews, promote data or alter the source identity product.

After authentic ordinary mapping and companion reviews have been saved, and the
external products exported through their existing native producer, run:

```bash
just qc-current-reviewed-sssom \
  path/to/current-mapping-review.json path/to/current-companion-review.json \
  /absolute/path/to/pinned-historical-root FULL_REVIEWED_HISTORICAL_COMMIT \
  output/current-reviewed-sssom
```

These are required future bindings, not supplied campaign approvals. The
historical root must be a distinct, disjoint, genuine Git checkout at that exact
full commit. Prepare it explicitly using ordinary Git clone/checkout in owned
persistent storage, retaining complete history for the original proof. Do not
fabricate a `.git`, relabel another working tree, use `--last`, copy dirty inputs,
or derive authority from an unreviewed manifest. Review the revision/root pin
independently. The gate creates no clone, alters no branch and performs no fetch.

The gate checks all tracked historical bytes and modes against actual Git blobs,
including literal symlink targets without following them; untracked historical
ingredient additions remain subject to the native complete-inventory proof.
It then invokes the unchanged native `identity_projection --root ... --check`,
and rechecks the pinned checkout after current review validation. An index,
HEAD, byte, mode, alias or proof discrepancy is a refusal, never a new baseline.
The original native checker still refuses changed science or fabricated mint
inventory even if someone commits those changes and supplies the new SHA.

The ordinary route requires an explicit paired companion review, the complete
current canonical SSSOM, native full-row evidence, current owner hashes and the
existing native companion claims. A projected header cannot use this route.
Removing only that header cannot turn its inherited decision proof into new
ordinary science. Historical context may remain evidence context, but a selected
decision that declares projection still needs the projection route. Rehashing
payloads or choosing `ordinary` is not scientific approval.

The ordinary companion producer/validator and external SSSOM schema validator
remain unchanged. Export and validate companion products separately through
`mediaingredientmech.export.ingredient_bundle`; the routing check itself emits
no product. No future current review exists in this code change, so CI retains
its existing projected selectors. A real data PR must supply its genuine
ordinary reviews, reviewed historical checkout preparation/pin and paired
workflow/test selectors before selecting the ordinary route. Other required QC,
graph, freshness, source identity and consumer gates still apply.

## Native review currentness

Native `record_review.save_review` requires an unsaved working-tree review's
recorded HEAD and exact inputs before publication. Do not silently restamp a
worker's report after a code commit. Save it at its genuine original bound root,
or have its authors explicitly inspect/reassess and bind the successor.

Already-saved review pairs preserve their original provenance. The adoption and
source-identity native admission code separately verifies every declared current
input, required context/payload/policy digest, exact target and disposition.
A code-only successor does not by itself erase unchanged science; a changed
declared code/policy/context input does invalidate that currentness condition.
Computational producer manifests have their own revision/runtime bindings and
must be rebuilt natively when stale. This routing gate neither changes those
rules nor transfers scientific approval to changed bytes.

KG-Microbe's stable/source candidate adapter remains a separate prerequisite.
An older consumer's capability refusal is expected safety behavior, not proof of
compatibility. No KG rebuild or production promotion is authorized here.
