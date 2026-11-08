The #1174 infrastructure changes pass this independent review at source `4fb9bf0339d4621e56ee4278ae1b68eeadd371d6a7991a4c99ec7ee832670dca` and publisher `9e1aa0767f1501a89dffb78402d89b96b66ecbe18b9a08b9daa0b9b8ca2fd832`. No new finding remains in the reviewed scope. Findings #1194, #1195 (including cached dependencies), #1197, #1198 (including receipt destinations), and #1200 were reproduced against their fixes and are resolved in these bytes.

The original successful controls still complete. The final publisher rejects disconnected owner history and global owned-name collisions before writing, including prior-only aliases absent from diagnostic output. The private loader executes captured code without replacing public cached modules.

Independent checks included the original adversarial programs, four receipt-path refusals, eleven focused final tests, and an offline native reconstruction of 3,007 diagnostic rows and exact suppression bytes. The latter preserved all 2,956 owners and used 2,699 captured inputs plus one absent input. Author88/106-test and static evidence was verified, not relabelled as independent reruns.

Two first publisher reruns used obsolete synthetic proof snapshots and were refused by the new guard before their intended test. Those outcomes remain recorded; compatible successor probes reached and verified the target checks.

This accepts the code scope for infrastructure review. It grants no scientific, whole-campaign, owner, alias, role, mapping or release approval. Actual accepted manifests, source application, current generation, scientific review, complete QC and PR CI remain separate.
