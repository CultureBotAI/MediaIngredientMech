"""Immutable report-only successor; no maintained or original artifact edits."""
from pathlib import Path
import json,hashlib,datetime,copy,csv
R=Path.cwd();C=R.parents[2];A=R/'.temp/w03-oxoid-successor-publication-v1';OLD=R/'.temp/w03-oxoid-successor-v1';P=R/'reports/all_unmatched_20261107/worker-03';O=P/'successors/issue1224-v1';F=O/'publication-v1';W=C/'workers/w01/worktree/.temp/nine-scope-candidates-independent-v1';CID='CM_NAME:2be5d4f231ea346e62be345a8e8b35adbc735ccdced2de73963ce5265c48fd66';PID='w03-oxoid-cm0149-product-1224-v1'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,v):
 p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('x') as f:json.dump(v,f,indent=2,ensure_ascii=False);f.write('\n')
def capture(src,dest):
 dest.parent.mkdir(parents=True,exist_ok=True)
 with dest.open('xb') as f:f.write(src.read_bytes())
 assert sha(src)==sha(dest)
 return {'root':'artifact','path':str(dest.relative_to(P)),'sha256':sha(dest)}
assert sha(W/'HANDOFF.json')=='1c320b85dc7ff0f35e5015968e9f290179bc4226b349225ea3b4b4c6f82e6c49';assert sha(W/'MANIFEST.json')=='6da888b709d8d304a072af5c74af3323de8caae9c7bac829d87dd96ef3e7ebdd'
for entry in json.loads((W/'MANIFEST.json').read_text())['files']:
 rel=Path(entry['path']);assert not rel.is_absolute() and '..' not in rel.parts
 assert sha(W/rel)==entry['sha256'];capture(W/rel,F/'context/w01-review'/rel)
capture(W/'MANIFEST.json',F/'context/w01-review/MANIFEST.json')
# Exact sealed W03 preflight: its manifest explicitly omits transient public-cookie metadata.
for line in (OLD/'SHA256SUMS').read_text().splitlines():
 h,n=line.split(None,1);assert sha(OLD/n)==h;capture(OLD/n,F/'context/w03-preflight'/n)
capture(OLD/'SHA256SUMS',F/'context/w03-preflight/SHA256SUMS')
comment=capture(A/'context/issue1224-comment-6718812904.json',F/'context/issue1224-comment-6718812904.json')
verification=capture(A/'context/w01-input-verification.json',F/'context/w01-input-verification.json')
D=O/'draft-v2';d=json.loads((D/'decisions.json').read_text());p=json.loads((D/'proposals.json').read_text());e=json.loads((D/'evidence.json').read_text());case=next(x for x in d['decisions'] if x['case_id']==CID);proposal=next(x for x in p['proposals'] if x['proposal_id']==PID)
new=[]
for eid,path,kind,locator,support in [
 ('w03-oxoid-w01-final-review',F/'context/w01-review/HANDOFF.json','independent_review','matrix[NEW-OXOID-CM0149], complete exact whole-nine review and author/peer scopes','W01 supports only the exact Oxoid named-product correction for this case with no exact finding. Historical version/catalog limits and whole-owner/role/export holds remain. The unrelated Soy1226 finding is retained without transferring it to Oxoid.'),
 ('w03-oxoid-w01-final-skeptic',F/'context/w01-review/skeptical/final-nine-review-v1.json','independent_review','candidate_matrix[NEW-OXOID-CM0149], final separate skeptical assessment','Independent skeptical review of exact1ec7554d full product, real new-origin lineage and NBRC902 source boundary; no owner/export acceptance.'),
 ('w03-oxoid-w03-preflight-skeptic',F/'context/w03-preflight/review/HANDOFF.json','independent_review','Complete exact draft-v2 full-candidate/source-case/retirement/accounting receipt','Separate /root/oxoid_successor_review assessment of unchanged payload and same scientific case conclusion; records exact draft-v2 hashes and its then-pending W01 condition. No retroactive relabeling: final complete publication receives an additional exact review receipt in HANDOFF.'),
 ('w03-oxoid-w03-preflight-native',F/'context/w03-preflight/review/review.yaml','independent_review','Complete validated native private review of exact draft-v2','Author-independent full new-product and one-case scientific review plus187/73/852 unchanged proof, with no scientific reapproval of unrelated worker03 source work. Original review and its historic pending condition remain immutable.'),
 ('w03-oxoid-w01-prerequisite-comment',F/'context/issue1224-comment-6718812904.json','source_snapshot','Issue1224 comment6718812904, complete actual coordinator communication','Supplies the explicit bounded scientific prerequisite for source-origin publication; ordinary commit/nonforcepush remains subject to final exact successor review/checks. No maintained owner/role/release approval.')]:
 new.append({'evidence_id':eid,'capture':{'root':'artifact','path':str(path.relative_to(P)),'sha256':sha(path)},'kind':kind,'locator':locator,'supports_or_contradicts':support,'url':None,'case_ids':[CID]})
e['evidence'].extend(new);refs=[x['evidence_id'] for x in new]
case['evidence_ids'].extend(refs);proposal['evidence_ids'].extend(refs)
case['reasoning']='NBRC902 explicitly names Oxoid CM0149 at 38 g, with 1 L water and optional 15 g agar in the receiving recipe. A separately qualified named-product identity is supported under issue1224. The current IFU0539 identifies CM0149B/T but its 13 g/L yeast formulation cannot be backdated to the historical occurrence. Bind the byte-exact coordinator-authored v4 candidate without component assertions or package/lot inference. The completed W01 review and earlier independent full-candidate/source-binding review are archived with their exact scopes; the final handoff separately binds the exact complete successor review. Retire the original mixed-owner form annotation from active application while preserving its full provenance.'
case['missing_requirement']='Historical Oxoid CM0149 formula revision and purchased package/lot remain unknown. Do not infer B/T, unconditional modern components, or generic/mixed-supplier membership. Coordinator source partition/admission, retained native/source/role/export holds and guarded maintained integration remain required. Catalog identity does not require inventing these missing facts. No W05 Difco, whole-owner or supported-export approval follows.'
case['independent_review']={'status':'complete','evidence_ids':['w03-oxoid-w01-final-review','w03-oxoid-w01-final-skeptic','w03-oxoid-w03-preflight-skeptic','w03-oxoid-w03-preflight-native'],'reviewer':'OpenAI Codex worker01 independent review team and /root/oxoid_successor_review','primary_author':'/root (worker03 successor source-binding author)','candidate_payload_author':'/root/next23_context','reviewed_after_sha256':proposal['after_capture']['sha256'],'scope_note':'These exact receipts review the unchanged product and same scientific source conclusion; the W03 receipt binds earlier draft-v2 metadata, preserved as such. The final HANDOFF separately supplies an additional independent receipt binding all exact final core bytes, without a self-referential review hash cycle. Original /root/materials review applies only to retired edit.'}
case['issue_refs'].append('https://github.com/CultureBotAI/MediaIngredientMech/issues/1224#issuecomment-6718812904')
proposal['independent_review']={'status':'complete','evidence_ids':case['independent_review']['evidence_ids'],'reviewer':'OpenAI Codex worker01 independent review team and /root/oxoid_successor_review','reviewed_after_sha256':proposal['after_capture']['sha256'],'scope_note':'Exact full product payload and bounded source conclusion reviewed; additional final complete-core review is detached in final HANDOFF. No whole-owner/role/export approval.'}
proposal['limitations']=case['missing_requirement']
for n,j in [('decisions.json',d),('proposals.json',p),('evidence.json',e)]:dump(F/n,j)
with (F/'proposal-inventory.tsv').open('x') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['proposal_id','kind','owner_path','before_sha256','after_sha256','case_ids'])
 for x in p['proposals']:w.writerow([x['proposal_id'],x['kind'],x['owner_path'],x['before_sha256'],x['after_capture']['sha256'],'|'.join(x['case_ids'])])
original_case=next(x for x in json.loads((D/'decisions.json').read_text())['decisions'] if x['case_id']==CID);original_proposal=next(x for x in json.loads((D/'proposals.json').read_text())['proposals'] if x['proposal_id']==PID)
dump(F/'publication-transition.json',{'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'prerequisite_received':True,'coordinator_comment':comment,'verified_w01_receipt':verification,'old_draft_core':{n:sha(D/n) for n in ['decisions.json','proposals.json','evidence.json']},'final_core':{n:sha(F/n) for n in ['decisions.json','proposals.json','evidence.json']},'changed_case_fields_from_draft':[k for k in case if case.get(k)!=original_case.get(k)],'changed_new_proposal_fields_from_draft':[k for k in proposal if proposal.get(k)!=original_proposal.get(k)],'additional_evidence_ids':refs,'candidate_bytes_changed':False,'candidate_sha256':proposal['after_capture']['sha256'],'candidate_author':'/root/next23_context','case_author':'/root','old_origin_consumed':False,'retired_origin':'b-proposal-cm0149-form','retirement_sha256':sha(O/'retirement.json'),'scope':'Actual review prerequisites and final source-binding metadata only. No new science, history event, maintained edit, supported export or owner merge. Final exact independent review required before commit.'})
print(json.dumps({'final_root':str(F),'cases':len(d['decisions']),'proposals':len(p['proposals']),'evidence':len(e['evidence']),'core_sha256':{n:sha(F/n) for n in ['decisions.json','proposals.json','evidence.json']}},indent=2))
