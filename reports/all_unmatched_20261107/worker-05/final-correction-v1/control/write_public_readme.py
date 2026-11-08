from pathlib import Path
import json,collections
W=Path.cwd();P=W/'reports/all_unmatched_20261107/worker-05/final-correction-v1'
D=json.loads((P/'core/decisions.json').read_text())['decisions'];PS=json.loads((P/'core/proposals.json').read_text())['proposals'];E=json.loads((P/'core/evidence.json').read_text())['evidence']
L=json.loads((P/'core/proposal-lineage.json').read_text());F=json.loads((P/'finding-register.json').read_text());A=json.loads((P/'core/assembly-receipt.json').read_text())
native=json.loads((P/'native-review-preparation/review-content.json').read_text());review_id=native['review_id']
facts=[dict(case_id=d['case_id'],source=d['source'],disposition=d['disposition'],occurrence_ids=d['occurrence_ids'],
 missing_requirement=d.get('missing_requirement'),no_change_reason=d.get('no_change_reason'),proposal_ids=d['proposal_ids'],
 primary_evidence_ids=d['evidence_ids'],independent_review=d['independent_review'],
 interpretation='The stated missing fact is retained at its original claim scope. A component/formulation uncertainty does not automatically negate a supported whole supplied-preparation identity.')
 for d in D if d.get('missing_requirement') or not d['proposal_ids']]
q=P/'remaining-source-facts.json';assert not q.exists();q.write_text(json.dumps(dict(cases=facts,scope='Source-specific missing facts and no-change explanations; not a blanket release or whole-identity rejection list.'),indent=2,ensure_ascii=False)+'\n')
counts=dict(collections.Counter(d['disposition'] for d in D));status=dict(collections.Counter(f['native_status'] for f in F['original_findings']))
text=f'''# W05 scientific correction successor

This append-only report supersedes the selected source decisions and proposals at `43f7cf6e8681fa617b5d6d3529d94d537ca01f0d` for the bounded corrections documented here. The original head, every prior report/capture/review and the sealed 22-family comparison packet remain intact. These are isolated candidates; the coordinator owns final acceptance, reconciliation, maintained application and export approval.

The canonical [core](core/) accounts for **{len(D)} frozen cases**, **{len(PS)} candidate payloads**, all **{L['original_count']} original proposal lineages**, and **{len(E)} evidence entries**. The additional {len(PS)-L['original_count']} candidates are individually identified in the lineage register. They include existing-owner follow-ons for the false thiamine-dihydrate CAS, the explicit KI stock alias and the explicit ferric-citrate stock alias. The latter two do not resolve the separate KJ and Eisencitrat source identities. Any additional source-form candidate retains its exact source scope and unassigned molecular facts. Every raw source label, case hash, occurrence membership and substantive source hold is preserved. The campaign boundary remains all 1,879 assigned cases in ten disjoint shards.

[Proposal lineage](core/proposal-lineage.json), [finding register](finding-register.json) and [remaining source facts](remaining-source-facts.json) provide exact before/after and source-scope accountability. All 18 original finding IDs, issue keys and target scopes remain: {status.get('resolved',0)} are resolved only within their bounded isolated/report scopes and {status.get('deferred',0)} retain explicit prerequisites. Additional scientific and report findings have their own immutable before-fix reproductions and separate dispositions; no issue was closed by this worker.

HEPES, both Wolfe comparisons and the 95% ethanol family remain conditional. Source numbers, receiving-medium pH, omitted carrier/hydration and nominal strength establish neither full equivalence nor distinctness. The [conditional matrices](chemicals/conditional-family-matrix-v1.json) preserve each candidate and source route without selecting a winning identifier or authorizing co-installation. Six hydration-unspecified magnesium aliases retain their exact historical objects and unresolved applicability. The Peptone eighteen historical inbound references, current proposed-component coupling and shared-owner unions remain explicit [integration dependencies](materials/integration-dependencies.json).

Primary science was divided among `/root/chemicals_research` (67 cases), `/root/materials_research` (61) and `/root/media_research` (60). Independent whole-case/payload reviews were assigned to `/root/materials_research` for chemicals, `/root/media_research` for materials and `/root/final_skeptical` for media. Their actual delegated scopes, source hashes, authorship limits, findings and rereviews are preserved under [reviews](reviews/). `/root` compiled the canonical outcome and authored the explicitly identified report amendments. The separate final assembly review and its preservation subreview are mechanical/provenance review where stated, not substitutes for chemical assessment.

Selected amendments are explicit: media report v2 corrects unsupported human attribution and the EMJH printed-page locator; media report v3 corrects the LB ingredient caption to1999. Chemical report v1 corrects the JCM628/629 comparison and adds14 required envelope fields by exact observation-text copy; v2 restores the three original native case-disposition values; v3 corrects MKP to DSMZ/MediaDive1895 solution6635. Earlier files remain historical evidence. No primary capture bytes, original retrieval timestamps or historical evidence enums were globally rewritten.

The unchanged native guarded writer and strict closed-schema validator pass for all {len(PS)} selected complete payloads. The complete path-keyed baseline substitution passes component partonomy, filename case and introduced-identifier checks. The unchanged campaign outcome auditor passes all {len(D)} cases. Complete isolated native row projections preserve the corrected Tris/tellurium parent and registry rows and remove only the false thiamine-dihydrate CAS row. [Validation receipts](validation/) retain the failed draft envelopes, exact bounded corrections and successful reruns. No producer, gate, schema, workflow, pin, maintained ingredient, aggregate or generated export changed; no downstream rebuild was run.

The native review is [`{review_id}`](../../../../reviews/structured/{review_id}/review.yaml), with verdict **needs_curation** because the scientific and integration prerequisites above remain. Completed review is not source-case admission, inherited-role approval, whole-owner approval or export approval. The original 22-family private comparison is unchanged and retains its original attribution and frozen-source bindings.

The authoritative final publication handoff is `.temp/w05-final-correction-v1/HANDOFF.json` in the W05 worktree, written after ordinary push so it records the exact published commit and manifest. This directory's manifest seals the published successor; historical lane handoffs describe their own earlier scopes.
'''
q=P/'README.md';assert not q.exists();q.write_text(text)
(P/'final-counts.json').write_text(json.dumps(dict(cases=len(D),candidate_payloads=len(PS),original_proposals=L['original_count'],evidence_entries=len(E),
 dispositions=counts,original_finding_statuses=status,cases_with_proposals=sum(bool(d['proposal_ids']) for d in D),
 cases_without_proposals=sum(not d['proposal_ids'] for d in D),occurrence_memberships=sum(len(d['occurrence_ids']) for d in D),
 evidence_kind_counts=dict(collections.Counter(e['kind'] for e in E)),source_identity_resolution_inferred_from_counts=False),indent=2)+'\n')
print(json.dumps(dict(cases=len(D),proposals=len(PS),evidence=len(E),native_review_id=review_id)))
