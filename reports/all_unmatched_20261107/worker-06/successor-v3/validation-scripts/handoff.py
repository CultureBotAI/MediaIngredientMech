from pathlib import Path
import collections,datetime,hashlib,json,shutil
R=Path('reports/all_unmatched_20261107/worker-06');S=R/'successor-v3';O=R/'successor-v2/final';N=Path('reviews/structured/20261108T064951Z-w06-successor-v3-reconciliation')
def rd(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,x):
 assert not p.exists(),p
 p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
assert rd(S/'native/check-command.json')['exit_code']==0
D=rd(S/'decisions.json')['decisions'];P=rd(S/'proposals.json')['proposals'];E=rd(S/'evidence.json')['evidence'];delta=rd(S/'delta.json');f=rd(S/'finding-dispositions.json')['findings']
oldnew={name:{'original_d5':sha(R/name),'previous_v2':sha(O/name),'current_v3':sha(S/name)} for name in ['decisions.json','proposals.json','evidence.json','source-holds.json']}
out={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'complete proposed successor, final publication review and ordinary commit/push pending','branch':'review/all-unmatched-w06-source-review-20261107','parent_published_head':'1b3641853c7105b9091f81b5a9b19c99e8ed351e','authoritative_intake':{'selection':{'path':str(S/'selection.json'),'sha256':sha(S/'selection.json')},'core':{name:{'path':str(S/name),'sha256':sha(S/name)} for name in oldnew}},'historical_and_current_core_hashes':oldnew,'counts':{'cases':len(D),'CM_occurrence_ids':sum(len(d['occurrence_ids']) for d in D),'original_downstream_holds':88,'proposals':len(P),'proposal_kinds':dict(collections.Counter(p['kind'] for p in P)),'evidence':len(E),'changed_payloads':sum(p['payload_changed'] for p in delta['proposal_deltas']),'changed_proposal_metadata':len(delta['proposal_deltas']),'changed_case_outcomes_or_review_metadata':len(delta['case_deltas'])},'independent_review_receipts':[{'path':str(S/p),'sha256':sha(S/p)} for p in ['research-a/review-b/final-scientific-review.json','research-a/review-v2/final-scientific-review.json','research-b/review-a/final-scientific-review.json','research-root/review-c/final-review-v2.json','research-a/central-binding-addendum.json','research-b/review-a/final-binding-addendum.json','research-root/review-c/central-binding-addendum.json','research-c/final-assembly-review/review-final.json']],'native_pair':{str(p):sha(p) for p in [N/'review.yaml',N/'review.md']},'native_check':{'path':str(S/'native/check-command.json'),'sha256':sha(S/'native/check-command.json'),'exit_code':0},'all_original_bytes_preserved':True,'coordinator_source_case_acceptance':'pending independent re-review','whole_owner_role_export_approval':False,'maintained_application':False}
dump(S/'completion-receipt.json',out)
text='''# Worker06 successor-v3 handoff

Use [selection.json](selection.json) as the **single authoritative complete proposed intake**. All earlier selections and author fragments are historical. This successor is based on published `1b3641853c7105b9091f81b5a9b19c99e8ed351e`; the commit containing this handoff is the publication revision, reported separately after ordinary push.

All 188 assigned cases, 310 frozen CultureMech occurrence IDs and 88 downstream holds are retained. The selection contains 103 proposals (78 new-owner proposals and 25 edits of existing owners) and 1,091 evidence entries. Relative to v2, 23 payloads are new or changed, 26 proposal metadata objects change, and 48 case outcomes or review bindings change. These are isolated proposals; no maintained owner, source selector, SSSOM, canonical export or downstream rebuild was applied.

Final source-case acceptance remains pending independent coordinator re-review. Passing gates and this handoff confer no whole-owner, role or export approval.

## Authoritative hashes

'''
text+='Selector SHA256: `'+sha(S/'selection.json')+'`.\n\n'
text+='| Ledger | Previous v2 SHA256 | Final v3 SHA256 |\n|---|---|---|\n'
for name,hashes in oldnew.items():text+=f"| [{name}]({name}) | `{hashes['previous_v2']}` | `{hashes['current_v3']}` |\n"
text+='\n[Completion receipt](completion-receipt.json) also records original d5 hashes, exact native pair hashes and all independent receipt hashes. [Delta ledger](delta.json) gives every exact old/new proposal payload hash and changed case-object hash.\n\n'
text+='''## Finding dispositions

The full sealed worker03 findings and assessment are preserved unchanged in `review-provenance/`; the original review is not rewritten. [Detailed dispositions](finding-dispositions.json) bind exact affected cases, payloads, independent receipts and residual limits.

| Finding | Proposed correction and retained boundary |
|---|---|
| 001 / issue1207 | One NBRC1308/1356 stock with both source/author lineages; complete named inputs, unquantified NaOH, water input rather than final volume. Final pH7 does not imply another titrant. |
| 002 | Eleven alias payloads corrected: 23 contextual labels become nonresolving, four preferred labels qualified. Identifying named stocks and tablet-qualified product labels remain resolving. |
| 003 | Exact v2 Merck canonical D-glucose child label retained and independently re-reviewed; old failed checks retained. |
| 004 | Remove untranscribed JCM977 stock Water and aqueous claim; retain literal20%w/v glucose. |
| 005 | Remove inferred Water from six other stocks; preserve literal membership and independently unknown solvent/form/percent/gas/closure facts. |
| 006 | JCM381→379 is positive primary evidence; original body and retrieval time retained. |
| 007 | Complete bounded EBIOS tablet, RM trace-metals, source-specific Oxoid BHI supplement and Sheffield TypeB proposals; unknown SKU/doses/forms/excipients remain unknown. |
| 008 | Four failed receiving pages are failed evidence. Separate MediaDive737/876/955 chains support only their exact contexts; J887 remains an explicit access/applicability hold. |
| 009 | TSY frozen amount correctly described as1000ML_PER_L; unknown formula remains unresolved. |
| 010 | Unsupported ingredient1886→JCM187 bridge removed; KG152 unresolved, genuine JCM187 CM106 link retained. |
| 011 | J240 YNB actual1g distinguished from6.7g in1682/1837; no SKU/formulation inferred from dose. |
| 012 | Seven source-qualified Sheffield TypeA contexts attach to unchanged TypeA proposal; four unqualified DSMZ contexts remain excluded. |

Issue1217 groups002–012 have bounded proposed corrections. Issue1207 group001 has a newly reviewed membership correction. Neither issue is closed by this handoff. The additional EBIOS cross-worker identity overlap was filed **before** its proposal as [issue1221](https://github.com/CultureBotAI/MediaIngredientMech/issues/1221); competing worker01/02/06 uninstalled choices require coordinator reconciliation. No other worker was edited and no maintained owners were merged.

## Independent review and checks

[Review coverage](review-coverage.json) records actual authors, distinct scientific reviewers and exact final case/payload hashes. A authored alias corrections, reviewed by B; B authored product preparations, reviewed by A; C authored membership/source corrections, reviewed by root; root authored the stock membership correction, reviewed by A. Existing author lineages are disclosed. [Sealed-review reading scopes](sealed-review-read-coverage.json) cover all188 original case and100 payload assessments; this is not a claim that this turn repeated fresh primary research for every unchanged case.

Final independent integration review: [C metadata/diff receipt](research-c/final-assembly-review/review-final.json). Scientific reviews and final central binding addenda are hash-listed in the completion receipt. Final publication metadata/native/handoff review is recorded in `research-c/final-assembly-review/publication-review.json` before publication.

Passed gates:

- Complete188-case/evidence/owner binding audit and1,091 capture hashes.
- Strict closed-schema validation of all103 selected payloads.
- Native partonomy on all2,956 baseline records and the isolated3,034-record successor overlay:152 decompositions,1,037 components, zero violations.
- Forty-seven focused positive/negative control pairs for alias identity, source-success classification, literal membership, unsupported bridges and exact context subsets.
- Native review inspect, validate, save and full retained-review check. The exact command exits and full logs are in [native/](native/) and [logs/full-final-v2/](logs/full-final-v2/).
- All1,758 original d5 manifest members and115 v2 members remain byte-identical, including failed checks and native pairs. No existing tracked file changes.

Native batch review: [YAML](../../../../reviews/structured/20261108T064951Z-w06-successor-v3-reconciliation/review.yaml) and [rendered Markdown](../../../../reviews/structured/20261108T064951Z-w06-successor-v3-reconciliation/review.md). Its74 targets are the26 changed proposal entries and48 affected case outcomes, with claims limited as stated. It does not fabricate terminal native predecessor lineage from the private worker03 fixture.

Initial authored candidates, the first central evidence-kind failure, and the independent metadata reviewer's corrected checker assumption remain saved as historical evidence. `assembly-attempt-1/`, B `author-attempt-1/`, original review receipts and old negative-control bindings are not current intake. Final gates use the current selector hashes. The initial `progress.json` is preserved; completion-receipt.json and this handoff describe completion.

## Remaining holds

[Source holds](source-holds.json) are exactly unchanged. [Remaining limits](remaining-holds.json) enumerates every explicit case limitation and all frozen downstream holds;29 cases retain unresolved dispositions. In particular, retain J887 receiving-source verification, ingredient1886 source continuity, unqualified Sheffield contexts, EBIOS cross-worker selection, historical product/lot/SKU distinctions, unspecified solvents/forms/doses/percent bases/gas content and final-volume uncertainty. Full formula uncertainty does not invalidate the bounded product preparations already supplied.

All original captures and retrieval dates remain unchanged. The shared immutable cache supplied no automatic source-case, owner or export approval. The maintained catalogue and all-source duplicate checks are scoped to the actual frozen/current worker inputs and recorded candidates, not an assertion about uninspected remote main.

Coordinator owns final acceptance, guarded integration and export. Worker06 publishes by ordinary commit/push on its assigned branch and then idles; no standalone PR, merge or branch deletion.
'''
assert not (S/'HANDOFF.md').exists();(S/'HANDOFF.md').write_text(text)
shutil.copyfile(Path(__file__),S/'validation-scripts/handoff.py')
print('Prepared final handoff and completion receipt')
