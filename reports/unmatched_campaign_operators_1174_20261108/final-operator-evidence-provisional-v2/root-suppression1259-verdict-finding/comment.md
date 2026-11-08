#1259 private implementation finding: a completed but nonpassing transition review is consumed as supporting the append.

The exact unfrozen consumer snapshot is `ea142b624f90d0ac9282fc2bdeca1d6b5001fb2cc8ca711a8207cb70871e34fb`. The preserved focused fixture is `02e88ed6141d4bb9bec538ffa139f6619952f9544d4b2305b0d1a96cec53caa4`. Neither changed during the reproduction.

The independent probe runs the actual native review schema/rendering, all119 original W07 input byte checks, and the current four-event/owner/credit/source-field joins. Its transition review and source/generation proof declarations are explicitly synthetic unit-fixture inputs. It does not call source `prepare`, source apply, publisher `prepare`, or publication.

The positive `pass_with_limitations` review returns the expected38-row sidecar. Two negative native-valid reviews also return38 rows: verdict `blocked` and verdict `needs_curation`, each with a required check explicitly `failed`. All four target assessments still include a supported transport assessment, isolating the missing overall verdict/check gate. Result SHA: `4537397067f4b91b600ed7a5a75f934c549ec20203dfd261a92f27679a4f3ef2`.

The native validator correctly permits a structured review to record failure when its verdict is nonpassing. The consumer checks completion/independence, target positives and absence of open/deferred target findings, but does not itself require a passing review or reject the failed required check. Schema validity is therefore being mistaken for admissible review disposition at this consumer boundary.

Bounded correction: require an admissible passing native review verdict and reject failed required transition checks, while retaining explicit pass-with-limitations and all original conditional WITHHOLD scopes. Keep target/evidence/input/independence checks, all original pins, the native schema, and root's separate acceptance unchanged. Preserve both negatives, the ordinary positive, and a qualified positive regression. This is not a report of maintained-data mutation or a full source/publication bypass.

Tracked here as the concrete review-consumption defect in this still-private capability implementation; this does not describe a defect in the currently pushed version1 publisher. Independent finding packet has23portable evidence members; root rehashed all of them before this comment. Portable manifest SHA256 `b3fabb3721b42aab734cf03d6e1ce4daea3c5301b5a868c93803e5748a64fadf`. The author is holding the affected repair until this finding is recorded.
