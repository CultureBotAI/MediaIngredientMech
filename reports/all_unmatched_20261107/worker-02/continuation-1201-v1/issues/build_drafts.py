"""Build issue-planning artifacts only; no maintained data or remote writes."""
from pathlib import Path
import hashlib
import json
from datetime import datetime, timezone

R = Path('reports/all_unmatched_20261107/worker-02')
S = R / 'continuation-1201-v1'
OUT = S / 'issues'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
load = lambda p: json.loads(Path(p).read_text())
props = {x['proposal_id']: x for x in load(S/'proposals.json')['proposals']}
evidence = {x['evidence_id']: x for x in load(S/'evidence.json')['evidence']}
decisions = load(S/'decisions.json')['decisions']
issues = load(S/'context/issue-dedup-prepublication.json')
read_inputs = set()
def bind(p):
    p = Path(p)
    read_inputs.add(str(p))
    return f'`{p}` (SHA256 `{sha(p)}`)'
def proposal(pid):
    p = props[pid]
    owner = Path(p['owner_path'])
    after = R/p['after_capture']['path']
    assert sha(owner) == p['before_sha256']
    assert sha(after) == p['after_capture']['sha256']
    return f"- Proposal `{pid}`. Current campaign-baseline owner: {bind(owner)}.\n- Exact proposed payload: {bind(after)}.\n"
def ev(eid):
    e = evidence[eid]
    p = R/e['capture']['path']
    assert sha(p) == e['capture']['sha256']
    return f"- `{eid}`: [{e['url']}]({e['url']}); accessed `{e['accessed_at']}`; {bind(p)}.\n"
def peer(path, pids):
    p = S/path
    x = load(p)
    byid = {q['proposal_id']:q for q in x.get('proposal_reviews', [])}
    for pid in pids:
        assert byid[pid]['status'] == 'approve'
        assert byid[pid]['after_capture'] == props[pid]['after_capture']
    return f"Independent reviewer `{x['reviewer']}` approved these exact bounded payloads in {bind(p)}. This is not a whole-owner, merge or publication approval.\n"
def cases(pids):
    selected = [d for d in decisions if set(d.get('proposal_ids',[])) & set(pids)]
    return '\n'.join(f"- `{d['case_id']}`; source `{d['source']['source_case_id']}`; raw source label `{d['source']['raw_source_label']}`." for d in selected)+'\n'

prefix = """Worker-02 continuation of #1201. These are isolated review proposals against the campaign's unchanged maintained owner bytes, not applied data changes. All artifact paths are repository relative. The published predecessor at `58f885fef05f8ff6e8b9b56fcb2479fef23b55c8` remains unchanged.

"""
limits = """Before applying any accepted delta, compare the then-current owner bytes and reconcile concurrent proposals. Preserve every raw label, original source reference, existing REJECTED_LABEL, WITHHOLD, source-quantity and downstream hold. Use guarded curation with history and the required maintained-surface/SSSOM synchronization and native validation. This draft requests no merge, downstream rebuild, automatic owner release or closure of broader issues.
"""
plan = []
def save(key,title,action,number,body,pids,eids,queries,related,reason):
    findings = [hashlib.sha256((props[p]['owner_path']+'\n'+p).encode()).hexdigest() for p in pids]
    footer = f'\n<!-- mim-review-round: worker02-continuation1201-v1 -->\n<!-- mim-review-bundle: {key} -->\n<!-- mim-fingerprints: {",".join(findings)} -->\n'
    path = OUT/(key+'.md')
    path.write_text(body.rstrip()+'\n'+footer)
    hits = {q:[{'number':i['number'],'state':i['state'],'title':i['title']} for i in issues if q.casefold() in (i['title']+' '+i['body']).casefold()] for q in queries}
    plan.append({'bundle_id':key,'title':title,'action':action,'issue_number':number,'body_path':str(path),'body_sha256':sha(path),'proposal_ids':pids,'evidence_ids':eids,'case_ids':[d['case_id'] for d in decisions if set(d.get('proposal_ids',[]))&set(pids)],'issue_queries_and_hits':hits,'related_issues':related,'deduplication_reason':reason,'finding_fingerprints':findings,'status':'draft_only_root_review_required'})

pid='c2-proposal-mucin-type-iii-material'
body=prefix+"""The Type III porcine-stomach mucin owner is classified `SINGLE_INGREDIENT` because an automatic rule treated a CAS primary as a defined chemical. Its own curation history records that rule. The primary material evidence supports a partially purified biological preparation, so the isolated proposal changes `ingredient_type` to `UNDEFINED_MIXTURE` and appends the evidence/history.

DSMZ 1580 specifies 2 g of Type III porcine-stomach mucin. Sigma's M1778 documentation independently describes this named type as partially purified powder with a range of bound sialic acid. This supports the material classification without establishing that the DSMZ recipe purchased Sigma M1778. The supplier, complete composition, Type II/Type III shared-CAS relationship and grade identity remain unasserted or held. The CAS, preferred name, original aliases and occurrence statistics are preserved.

"""+proposal(pid)+'\n'+cases([pid])+'\n'+ev('c2-dsmz-1580')+ev('c-sigma-mucin')+'\n'+peer('a/review-c/independent-review.json',[pid])+"""
The inherited full-row hold about the bound-sialic-acid source text in the synonym channel is retained. Classification repair alone does not approve that alias or the owner for export. #478 is the broader ingredient-type schema-axis discussion; this is a concrete material misclassification that can be corrected within the current schema, without claiming that the schema discussion is resolved.

"""+limits
save('new-mucin-type-iii','Classify Type III porcine mucin as a biological mixture rather than a single compound','create',None,body,[pid],['c2-dsmz-1580','c-sigma-mucin'],['mucin','Mucin_From_Porcine','84082-64-4'],[478,1201],'No mucin-specific finding in the captured 674 issue titles/bodies; #478 is a schema-design umbrella, not this owner correction.')

pid='c2-proposal-netropsin-congocidin-alias'
body=prefix+"""`mapped/Congocidin.yaml` remains a `kgmicrobe.compound:congocidin` PLACEHOLDER owner, while `mapped/Netropsin.yaml` is already mapped to `mesh:D009429`. Primary nomenclature evidence now supports the bare antibiotic name Congocidin/Congocidine as Netropsin. Publishing the proposed aliases without reconciling the existing Congocidin owner would create competing name ownership.

NLM MeSH places term T028107, Congocidine, inside the preferred Netropsin concept M0014675. The salt concepts are separately represented; this conclusion does not assign hydrochloride or dihydrochloride to the frozen source. PubChem CID4461 corroborates the Congocidin spelling; its mixed salt synonym list is not used to infer supplied salt. The metatraits case has the graph label `congocidin`, a blank raw source-label field and no supplied-form observation. The isolated proposal adds the two supported bare aliases to Netropsin, with the competing-owner/export dependency explicitly held.

"""+proposal(pid)+'- Competing maintained placeholder: '+bind('data/ingredients/mapped/Congocidin.yaml')+'.\n\n'+cases([pid])+'\n'+ev('c2-mesh-netropsin-concept')+ev('c2-mesh-congocidine-term')+ev('c-pubchem-synonyms-4461')+ev('c-root-congocidine-pubmed')+'\n'+peer('a/review-c/independent-review.json',[pid])+"""
Follow-up must review both actual owners, their source observations, current mapping scopes and owned-name/export dependencies. Decide the appropriate duplicate reconciliation through the repository procedure, preserving history and source identities. No survivor, deletion, tombstone, role union, count sum or SSSOM merge is authorized by this alias proposal. The existing Congocidin WITHHOLD remains; the descriptor's wider salt scope is not approved by inspecting its preferred concept alone.

The captured issue index has no Netropsin/Congocidin-specific ticket. #226 concerns a different enumerated set of duplicate-identifier groups and does not cover this pair.

"""+limits
save('new-netropsin-congocidin','Reconcile Congocidin and Netropsin owner scopes before publishing duplicate name ownership','create',None,body,[pid],['c2-mesh-netropsin-concept','c2-mesh-congocidine-term','c-pubchem-synonyms-4461','c-root-congocidine-pubmed'],['netropsin','congocidin','congocidine'],[226,1201],'No direct name or owner finding in all 674 captured issue titles/bodies; #226 lists different duplicate groups.')

pids=['w02-v2-mohr-hexahydrate-composed','c2-proposal-pyruvate-stock-alias','c2-proposal-vanadyl-stock-and-bare-aliases','a2-proposal-methanol-source-filtration-provenance']
body=prefix+"""Four current pure-substance owners accept concentration-qualified or hydration-erasing strings as resolving aliases. The proposed corrections preserve each exact token and original source as `REJECTED_LABEL`; they do not invent stock recipes or change the established solute identities.

| Owner | Tokens made non-resolving | Bounded reason |
| --- | --- | --- |
| `Fe_Nh42_So42_X_6_H2o.yaml` | `Fe(NH4)2(SO4)2 x 6 H2O (0.01% w/v)`, `Fe(NH4)2(SO4)2 x 6 H2O (0.1% w/v)`, `Fe(NH4)2(SO4)2 x 6 H2O (2% v/v)` | Concentration-qualified preparation labels do not unconditionally identify neat Mohr hexahydrate. |
| `Na-pyruvate.yaml` | `1 M Sodium pyruvate*` | The explicit 1 M preparation is not the neat sodium-pyruvate substance. |
| `Voso4_X_5_H2o.yaml` | `VOSO4 x 5 H2O (0.01% w/v)`, `VOSO4` | One is preparation-qualified; the other omits the five waters required by the exact hydrate. |
| `Methanol.yaml` | `Methanol (10%)` | The original stock-strength versus receiving-medium-dose interpretation is unestablished. Either interpretation is unsuitable as an unrestricted molecular-identity alias. |

ChEBI 76181, 50144 and 132758 establish the compared solute scopes. They are not evidence for an unstated solvent or a complete formulation. The vanadyl source's CAS12439-96-2 and owner's CAS14708-82-8 differ as annotations; the inspected ChEBI132758 response lists both, so their difference alone is not a chemical contradiction. Preserve both facts rather than silently replacing either.

ATCC2883 separately specifies filter-sterilized methanol, 3 mL added after autoclaving. The exact methanol proposal records that source-qualified treatment in notes and supplied_form on the existing molecular owner. It does not create a new mixture from filtration alone or infer assay, dilution, solvent or filter pore size.

"""
for p in pids: body+='\n'+proposal(p)
body+='\n'+cases(pids)+'\n'
for eid in ['c-chebi-76181','c-chebi-50144','c-chebi-132758','c-chebi-87020','a-primary-atcc-2883']: body+=ev(eid)
body+='\n'+peer('d/independent-review-mohr-v2.json',[pids[0]])+peer('a/review-c/independent-review.json',pids[1:3])+peer('b/independent-review-a-binder-v1.json',[pids[3]])
overlap=load(S/'validation/cross-shard-overlaps-v1.json')['same_owner_path']['data/ingredients/mapped/Voso4_X_5_H2o.yaml']
w10=next(x for x in overlap if x['worker']==10)
body+=f"""
The Mohr receipt binds the final composed successor, including all six preserved earlier source aliases and the three new rejections. Approval of C's isolated fragment alone was not treated as approval of that composition. Bare-formula, generic-hydrate, role-like and other full-owner obligations remain held.

Vanadyl requires cross-shard reconciliation: the captured coordinator observation records worker10 `{w10['proposal_id']}` at head `{w10['head_at_observation']}`, payload `reports/all_unmatched_20261107/worker-10/chemicals/proposed/Voso4_X_5_H2o.yaml`, SHA256 `{w10['payload_sha256']}`, against the same baseline owner. It proposes a source formula-ordering alias from TOGO M2262. That is a distinct delta from worker02's two rejections. Preserve both proposal histories and require independent review of the exact combined bytes before integration; this observation does not attest worker10's scientific review, choose a winner or approve worker10's source cases. Observation: {bind(S/'validation/cross-shard-overlaps-v1.json')}.

Existing #1189 covers glyoxylate, vanadate, AQDS and carbonate, not these four owners. #1203 concerns magnesium-sulfate stock occurrences. #702 mentions Na-pyruvate for a historical CAS-to-ChEBI import defect, and #752 mentions methanol within hydrogen-gas aliases; neither covers these exact tokens. This is a bounded related bundle, not a closure of those issues or #718's release umbrella. Keep the recorded Mohr, sodium-pyruvate and vanadyl WITHHOLD reasons and all other source/owner/release obligations until separately assessed.

"""+limits
save('new-pure-owner-qualified-aliases','Preserve stock and supplied-form boundaries in Mohr, pyruvate, vanadyl and methanol aliases','create',None,body,pids,['c-chebi-76181','c-chebi-50144','c-chebi-132758','c-chebi-87020','a-primary-atcc-2883'],['Fe_Nh42','Fe(NH4)2(SO4)2','1 M Sodium pyruvate','Na-pyruvate','VOSO4','vanadyl','Methanol (10%)','methanol'],[1189,1203,702,752,718,1201],'No exact four-owner or token finding in the captured issue index; inspected related issues address different substances or different defects.')

pid='c2-proposal-silicate-related-aliases'
body=prefix+"""Additional bounded sodium-silicate owner finding; the MediaDive2160 pentahydrate/21.2 g/L stock hold in this issue remains unchanged.

The current Na-silicate owner types five source terms as EXACT_SYNONYM: `(5)  Sodium metasilicate`, `Sodium polysilicate`, `Sodium sesquisilicate`, `Sodium silicate glass`, and `Sodium siliconate`. In the inspected official ChEBI60720 response, each underlying term is explicitly `hasRelatedSynonym`. Flattening the ontology's synonym list lost that scope. The proposed v2 payload retains all five exact source strings and their kg_microbe provenance as REJECTED_LABEL. `disodium oxosilanediolate` also has an independent `hasExactSynonym` IUPAC assertion; it is not rejected merely because it additionally occurs with a related assertion.

"""+proposal(pid)+'\n'+cases([pid])+'\n'+ev('c-chebi-60720')+ev('c2-ols-sodium-silicate')+'\n'+peer('a/review-c/independent-review.json',[pid])+"""
The two worker02 source entries remain source-bound: MediaDive1596/DSMZ1753 and MediaDive524/DSMZ511 do not establish modulus, hydration, vendor or an exact formulation. This correction therefore does not assign either generic source to a fixed unstated silicate form. It also does not resolve MediaDive2160, resurrect the rejected pentahydrate alias or approve worker03's separate hydrate/stock proposal. Preserve the existing numbered-source-artifact and full-owner release holds. No other row in #1157 is assessed or closed by this comment.

"""+limits
save('comment-1157-silicate-related','Additional Na-silicate related-synonym scope correction','append_to_existing',1157,body,[pid],['c-chebi-60720','c2-ols-sodium-silicate'],['silicate','Na-silicate','Sodium polysilicate','Sodium siliconate'],[1157,226,1201],'Append to the existing bounded Na-silicate source/form ticket; the five related-term predicate losses are additional to its retained pentahydrate/stock hold.')

pid='w02-v2-ferric-variable-composed'
body=prefix+"""A bounded correction is proposed on the mapped Fe2(SO4)3 variable-hydrate owner. It does not resolve the separate UNMAPPED_0385 owner or the competing-label problem reported here.

The mapped owner's inherited `Fe(SO4)3 x n H2O` synonym omits the Fe coefficient required by the balanced ferric-sulfate formula. The exact composed successor changes that one token from RAW_TEXT to REJECTED_LABEL, retaining the original source. It also preserves the two published B source aliases and adds the two independently supported A variable-hydrate spellings. The local primary identity and NARROW_MATCH to the anhydrous parent CHEBI53438 remain; no fixed water number, monohydrate identity or anhydrous exact equivalence is asserted.

"""+proposal(pid)+'- Separate owner still requiring reconciliation: '+bind('data/ingredients/unmapped/FeSO43_X_N_H2O.yaml')+'. It remains UNMAPPED_0385 and still contains the competing RAW_TEXT alias `Fe2(SO4)3 x n H2O`.\n\n'+cases([pid])+'\n'+ev('a-primary-primary-4ac0f41bc31f358e')+ev('a-primary-primary-84d6ae660e2442ec')+ev('a-primary-togo-M1344')+'\n'+peer('c/independent-review-ferric-composition-v2.json',[pid])+"""
Primary source support is bound in that review: NBRC830 and JCM1327 explicitly retain balanced variable-hydrate formulas. JCM1250-derived evidence is the frozen source plus TOGO M1344; the current JCM1250 page returns Nothing found and is not positive recipe evidence. The exact composition evidence and original proposal fragments remain preserved under `continuation-1201-v1/integration/`; correcting the mapped-owner typo cannot establish source identity or select a survivor for the separate placeholder.

The existing owner/name collision and any row-order-sensitive downstream routing in #873 therefore remain open. No new runtime rerun is claimed by this comment. Reconcile both current owners and their provenance before considering a merge or label-ownership change, and reassess exact downstream routing separately. Do not close #873 because the mapped owner's different malformed alias has been corrected in a proposal.

"""+limits
save('comment-873-ferric-alias','Mapped ferric-hydrate alias correction does not close the separate competing-owner issue','append_to_existing',873,body,[pid],props[pid]['evidence_ids'],['Fe2_So43','FeSO43','Fe(SO4)3'],[873,871,1201],'Existing #873 is the precise competing-owner ticket; append the bounded mapped-owner delta while explicitly retaining its separate-owner and downstream-routing obligations.')

for p in [S/'proposals.json',S/'evidence.json',S/'decisions.json',S/'context/issue-dedup-final.json',S/'context/issue-dedup-final-receipt.json',S/'context/issue-dedup-prepublication.json',S/'context/issue-dedup-prepublication-receipt.json',OUT/'build_drafts.py']:
    read_inputs.add(str(p))
for n in [1157,873,1189,1203,478,702]: read_inputs.add(str(S/f'context/issue-{n}-current.json'))
for p in OUT.glob('*.md'):
    p.write_text(p.read_text().replace('674 issue',str(len(issues))+' issue'))
for x in plan:
    x['body_sha256']=sha(x['body_path'])
    x['deduplication_reason']=x['deduplication_reason'].replace('674 captured',str(len(issues))+' captured').replace('674 issue',str(len(issues))+' issue')
OUT.joinpath('issue-plan.json').write_text(json.dumps({'schema_version':'worker02-issue-draft-plan-v1','draft_only':True,'bundles':plan},indent=2,ensure_ascii=False)+'\n')
receipt={'drafted_at':datetime.now(timezone.utc).isoformat(),'drafter':'/root/research_b','status':'draft_only_root_review_required','scope':'Issue bodies/comments only; no data, after payload, review or remote changes.','source_issue_count':len(issues),'source_issue_snapshot':str(S/'context/issue-dedup-final.json'),'source_issue_snapshot_sha256':sha(S/'context/issue-dedup-final.json'),'dedup_scope':'All titles and bodies in the coordinator-captured all-state 674-issue snapshot, plus full comments from the six bound current issue captures. No claim to have searched all comment threads. No new network fetch. Local actual owner searches used pathlib.rglob and included ignored files.','new_issue_drafts':3,'existing_issue_comment_drafts':2,'remote_mutations':[],'fingerprint_method':'SHA256(owner_path + newline + proposal_id); issue-planning fingerprints, not invented native review finding IDs.','review_scope':'Exact proposal approvals and limitations verified from current independent receipts; composed Mohr v2 approval became available and is cited. No cross-shard scientific approval inferred from observation.','input_hash_manifest':[{'path':p,'sha256':sha(p)} for p in sorted(read_inputs)],'outputs':[{'path':x['body_path'],'sha256':x['body_sha256']} for x in plan]+[{'path':str(OUT/'issue-plan.json'),'sha256':sha(OUT/'issue-plan.json')}],'remaining_actions':['Root inspect and refresh dedup if later issue state changes before posting.','Root decide and submit exact reviewed bodies or comments; no automatic submission.','Preserve cross-shard vanadyl reconciliation and all owner/source/row/release holds.']}
receipt['source_issue_snapshot']=str(S/'context/issue-dedup-prepublication.json')
receipt['source_issue_snapshot_sha256']=sha(S/'context/issue-dedup-prepublication.json')
receipt['dedup_scope']=receipt['dedup_scope'].replace('674-issue',str(len(issues))+'-issue')
OUT.joinpath('drafting-dedup-receipt.json').write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'created_drafts':len(plan),'input_bindings':len(read_inputs),'receipt_sha256':sha(OUT/'drafting-dedup-receipt.json')},indent=2))
