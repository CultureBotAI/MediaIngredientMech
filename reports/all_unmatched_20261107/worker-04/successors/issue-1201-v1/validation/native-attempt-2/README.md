# Native report shape failure — preserved

The actual native validator rejected a missing required action.finding_ids field before any save. The native schema allows an explicit empty list, which correctly records that this successor action does not invent a new finding or retire prior findings. The corrected content passed an actual native shape precheck. The builder correction is code-bound, so all actual mechanical gates and independent controls are rerun before the final native save. Scientific decisions, proposals, source captures and their timestamps are unchanged.
