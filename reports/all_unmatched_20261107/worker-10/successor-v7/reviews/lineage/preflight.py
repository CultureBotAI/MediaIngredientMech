from pathlib import Path
import json, hashlib, subprocess, datetime
import yaml

R=Path.cwd(); C=R.parents[2]; A=R/'reports/all_unmatched_20261107/worker-10'
O=R/'.temp/columbia-controls-successor-v1'; P=O/'lineage'
W7=C/'workers/w07/worktree/.temp/columbia-continuity-independent-v1'
CENT=C/'preflight/central24-25-independent-v1'
NOM=C/'preflight/central24-25-nominal-decisions-v1'
SRC=C/'queue/preliminary-v5'
HEAD='c66d6d3665368fe1ae8986fb7c16340a103582c1'
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
reads={}
def sha(b):return hashlib.sha256(b).hexdigest()
def canonical(x):return sha(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode())
def read(p):
 b=p.read_bytes(); reads[str(p)]={'sha256':sha(b),'bytes':len(b)};return b
def js(p):return json.loads(read(p))
def blob(root,head,path):return subprocess.check_output(['git','-C',str(root),'show',f'{head}:{path}'])
def bound(root,head,path):
 p=root/path;b=read(p);assert blob(root,head,path)==b,('git',path);return b
def save(n,x):
 p=P/n;assert not p.exists();p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
assert subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()==HEAD
task=read(O/'inputs/user-task.md')
comments=[js(O/'inputs'/f'issue1237-comment{i}.json') for i in [6720201281,6720201502]]
manifests=[]
for root,key,expected in [(W7,'files',2358),(CENT,'members',50)]:
 m=js(root/'MANIFEST.json');members=m[key];assert len(members)==expected
 for f in members:assert sha((root/f['path']).read_bytes())==f['sha256'],f['path']
 manifests.append({'path':str(root/'MANIFEST.json'),'sha256':reads[str(root/'MANIFEST.json')]['sha256'],'verified_members':len(members)})
pins=js(CENT/'input-pins.json')
for p,h in pins.items():assert sha(Path(p).read_bytes())==h,p
controls=[x for x in js(NOM/'bound-current-origins.json') if x['historical_index'] in [941,955]]
assert len(controls)==2
bindings=js(W7/'inputs/selected-source-bindings.json')
decision=js(W7/'decision/continuity-decision-v3.json')
handoff=js(W7/'HANDOFF.json');originbridge=js(W7/'validation/current-origin-bridges.json')
matrix=js(W7/'review/science/current-source-occurrence-matrix.json')
core={k:json.loads(bound(R,HEAD,str((A/f'successor-v6/final-core/{k}.json').relative_to(R)))) for k in ['decisions','proposals','evidence']}
ds={x['case_id']:x for x in core['decisions']['decisions']};ps={x['proposal_id']:x for x in core['proposals']['proposals']}
es={x['evidence_id']:x for x in core['evidence']['evidence']}
shard=js(SRC/'shards/shard-10.json');cases={x['case_id']:(i,x) for i,x in enumerate(shard['cases'])}
assert len(ds)==len(cases)==188 and ds.keys()==cases.keys()
occurrences=[]
for cid,(i,x) in cases.items():
 d=ds[cid];assert d['case_input_sha256']==canonical(x),(i,'casehash')
 assert d['occurrence_ids']==[o['occurrence_id'] for o in x.get('occurrences',[])]
 for o in x.get('occurrences',[]):
  b=read(SRC/o['full_recipe_snapshot']);assert sha(b)==o['source_file_sha256']
  doc=yaml.safe_load(b);cur=doc
  for part in o['component_path'].split('/'):cur=cur[int(part)] if isinstance(cur,list) else cur[part]
  assert cur==o['raw_component'],o['occurrence_id']
  occurrences.append({'case_id':cid,'source_index':i,'occurrence':o,'recipe_sha256':sha(b)})
assert len(occurrences)==304
payloads=[]
for p in ps.values():
 cap=p['after_capture'];assert cap['root']=='artifact'
 b=bound(R,HEAD,str((A/cap['path']).relative_to(R)));assert sha(b)==cap['sha256']
 payloads.append({'proposal_id':p['proposal_id'],'proposal_sha256':canonical(p),'after_capture':cap,'before_sha256':p.get('before_sha256'),'kind':p['kind'],'case_ids':p['case_ids']})
assert len(payloads)==127
capchecks={}
for e in es.values():
 cap=e['capture'];root={'artifact':A,'source':SRC}[cap['root']];p=root/cap['path']
 if str(p) not in capchecks:capchecks[str(p)]=sha(read(p))
 assert capchecks[str(p)]==cap['sha256'],e['evidence_id']
ownerpath='data/ingredients/unmapped/Columbia_Blood_Agar_Base.yaml'
ownerbytes=bound(R,HEAD,ownerpath);owner=yaml.safe_load(ownerbytes)
assert sha(ownerbytes)=='29ed63a00d3f4f7a1652beee549526d625eef231f29b40691bd128d2f7608324'
assert owner['identifier']=='UNMAPPED_0118' and len(owner['curation_history'])==5
selected=[]
targetpids=['sv1-bio-columbia_blood_agar_oxoid_m2224','sv3-hm-difco-columbia1270','sv1-buffers-tris_hcl_0_2m_ph7_5_dsmz273','sv1-buffers-hepes_2m_ph7_jcm556_1200']
for pid in targetpids:
 p=ps[pid];assert p['before_sha256'] is None and p['kind']=='new_owner'
 selected.append({'worker':'w10','source_head':HEAD,'proposal':p,'payload':yaml.safe_load(read(A/p['after_capture']['path'])),'case_bindings':[{'zero_based_index':cases[cid][0],'complete_original_case':cases[cid][1],'current_decision':ds[cid]} for cid in p['case_ids']]})
for control in controls:
 p=ps[control['current_binding']['proposal_id']]
 assert control['current_original_proposal']==p
 assert yaml.safe_load(read(NOM/control['payload_capture']))==yaml.safe_load(read(A/p['after_capture']['path']))
 assert control['current_binding']['payload_sha256']==p['after_capture']['sha256']
 assert control['source_case_outcomes']==[ds[cid] for cid in p['case_ids']]
w4=next(x for x in bindings if x['proposal']['proposal_id']=='FREV-MEDIA-P-media-followup-oxoid_cm0331_columbia_blood_agar_base')
w4root=C/'workers/w04/worktree';w4head=w4['source_head']
assert subprocess.check_output(['git','-C',str(w4root),'rev-parse','HEAD'],text=True).strip()==w4head
assert sha(bound(w4root,w4head,w4['payload']['git_path']))==w4['payload']['sha256']
w4ps=json.loads(bound(w4root,w4head,w4['source_selector']+'proposals.json'))['proposals']
assert w4['proposal']==next(x for x in w4ps if x['proposal_id']==w4['proposal']['proposal_id'])
w4ds=json.loads(bound(w4root,w4head,w4['source_selector']+'decisions.json'))['decisions']
assert all(d==next(x for x in w4ds if x['case_id']==d['case_id']) for d in w4['decisions'])
w4shard=js(SRC/'shards/shard-04.json');w4case=next(x for x in w4shard['cases'] if x['case_id']==w4['proposal']['case_ids'][0])
assert canonical(w4case)==w4['decisions'][0]['case_input_sha256']
for o in w4case['occurrences']:
 b=read(SRC/o['full_recipe_snapshot']);assert sha(b)==o['source_file_sha256']
 v=yaml.safe_load(b)
 for part in o['component_path'].split('/'):v=v[int(part)] if isinstance(v,list) else v[part]
 assert v==o['raw_component'] and v['concentration']=={'value':'variable','unit':'VARIABLE'}
routes=[]
for row in matrix['rows']:
 cap=row['recipe_capture'];b=read(W7/'review/science'/cap['snapshot']);assert sha(b)==cap['sha256']
 recipe=yaml.safe_load(b);o=row['occurrence'];comp=recipe[o['component_field']][int(o['component_index'])]
 assert comp==json.loads(o['ingredient_json']),row['recipe_id']
 routes.append({'reviewed_row':row,'recipe_sha256':sha(b),'actual_component':comp,'campaign_membership':'external continuity inventory; no new W10 case or occurrence'})
assert len(routes)==7
save('selected-source-lineage.json',{'targets':selected,'external_W04_origin':w4,'external_W04_original_case':w4case,'controls_central_pin_records':controls,'authentic_owner':{'path':ownerpath,'sha256':sha(ownerbytes),'complete_record':owner},'seven_current_source_rows':routes,'scope':'Complete exact objects; current-science dispositions attributed to W07, not renewed by hash verification.'})
save('baseline-fullcore.json',{'head':HEAD,'core_hashes':{k:reads[str(A/f'successor-v6/final-core/{k}.json')]['sha256'] for k in core},'decisions':[{'case_id':x['case_id'],'sha256':canonical(x),'case_input_sha256':x['case_input_sha256'],'occurrence_ids':x['occurrence_ids']} for x in ds.values()],'proposals':payloads,'evidence':[{'evidence_id':x['evidence_id'],'sha256':canonical(x),'capture':x['capture']} for x in es.values()],'occurrences':occurrences})
save('preflight-read-bindings.json',{'read_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'files':reads,'all_central_input_pins_verified':len(pins),'packet_manifests':manifests,'all_current_evidence_captures_verified':len(capchecks)})
save('preflight-review-v1.json',{'reviewer':'worker10:/root/bio_research','scientific_review':False,'review_timing':{'exact_first_read_utc':None,'qualification':'Reading began before this audit script; exact first tool UTC not retained. Audit execution is not represented as full review interval.','audit_execution_started_at':start,'completed_at':datetime.datetime.now(datetime.timezone.utc).isoformat()},'authorship':'I authored W10 biological source proposals including original M2224 Oxoid, later W10 HCl/BD-manual source successors and unrelated ISP4; I independently reviewed original buffers. I did not author original buffers941/955 or original KG Difco owner, but later authored its BD-manual correction. I am independent of root new successor authorship only; this metadata review does not renew independent original science. W04 and W07 source/review authors retain attribution.','head':HEAD,'status':'PASS_ORIGIN_AND_MEMBERSHIP_PREFLIGHT_FINAL_SUCCESSOR_PENDING','counts':{'original_cases':len(ds),'original_occurrences':len(occurrences),'original_proposals':len(ps),'original_evidence':len(es),'target_W10_proposals':4,'external_W04_origin':1,'current_continuity_rows':7,'supported_Difco_dry_rows':3,'held_prepared_Oxoid_rows':4},'recommendation':{'new_dependency':'One genuine edit_existing_owner at the same UNMAPPED_0118 path from exact29ed preimage; retain identity/status/type/stats/generic synonym/history, reject only two vendor resolving aliases with truthful partition notes. Bind new dependency to existing source_index118/178; invent no new case or CM occurrence.','Difco':'Retain current new_owner/null-before and e35684 proposal predecessor; supported exact BD-Difco dry synonym plus exact0118 reviewed after hash. Current7rows are contextual routing outside assigned188/304.','Oxoid':'Retain W10 M2224 37e8 original payload exact if source successor is metadata-only; bind actual W04 current4a3d origin and existing family-v2 prototype as external composition dependencies. Coordinator must select/review one nominal Oxoid combined candidate before installation, preserving source300 variable/CM0331 and source92139g/no historical catalogue. This does not claim a combined candidate was authored or installed here.','controls':'Both941/955 belong to W10 buffers; keep original PID/case/occurrences, new_owner/null-before, full scientific fields and old history. Bounded UNKNOWN correction only; no blanket change to280/938 or Wolfe/Hutner.'},'findings':[],'limitations':['Final successor bytes not available at preflight; no final retention or application approval yet.','No primary chemistry/source-science reassessment, role/export approval, other-worker edits, Git/GitHub mutation or new external session.','Seven current CultureMech rows and historical x4/x1 synonym event are different inventories; neither changes frozen188/304 assignment.','No generic provider2046 identity or prepared1L-to-dry39g substitution.'],'proof_files':['selected-source-lineage.json','baseline-fullcore.json','preflight-read-bindings.json']})
print(json.dumps({'status':'PASS','cases':len(ds),'occurrences':len(occurrences),'proposals':len(ps),'evidence':len(es),'captures':len(capchecks),'manifests':manifests,'pins':len(pins)},indent=2))
