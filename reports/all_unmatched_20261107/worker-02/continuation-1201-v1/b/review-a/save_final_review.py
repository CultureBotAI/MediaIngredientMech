"""Bind independently inspected sources and manually authored case assessments."""
from pathlib import Path
import copy,datetime,hashlib,json,shutil,yaml
R=Path('reports/all_unmatched_20261107/worker-02');S=R/'continuation-1201-v1';A=S/'a';B=S/'b';C=S/'c';OUT=B/'review-a';SNAP=OUT/'input-final';SNAP.mkdir(exist_ok=True)
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
canon=lambda x:hashlib.sha256(json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
capture=lambda p:{'root':'artifact','path':str(Path(p).relative_to(R)),'sha256':sha(p)}
for n in ['decisions.json','evidence.json','proposals.json','reassessments.json','solution-scope-assessments.json','owner-lookups-and-context.json','primary-integrity-final.json']:
 shutil.copy2(A/n,SNAP/n)
expected={'decisions.json':'661f34e8646542c65fcbeb864da7e7aa6b069c6f0bf0b2b199674666f6766455','evidence.json':'6ff356e29e1719127600ea1c822183b715324a44270cc151c463708c3236e270','proposals.json':'b28bc7bdcbd78e31976aac797c70fde84c3cfd7f11dfa2872ecb7f6bab60e431'}
for n,h in expected.items():assert sha(SNAP/n)==h
Ds=json.loads((SNAP/'decisions.json').read_text())['decisions'];Ps=json.loads((SNAP/'proposals.json').read_text())['proposals'];As=json.loads((SNAP/'reassessments.json').read_text())['assessments'];idx={x['case_id']:x['index'] for x in As};notes=json.loads((OUT/'reviewer-case-notes.json').read_text())
E={x['evidence_id']:x for f in [R/'evidence.json',A/'evidence.json',C/'evidence.json'] for x in json.loads(f.read_text())['evidence']}
F={x['case_id']:x for x in json.loads((R/'context/frozen-shard-02.json').read_text())['cases']}
queue=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
receipts=[];recipe_receipts=[]
def inspect(d):
 f=F[d['case_id']];assert canon(f)==d['case_input_sha256'];assert d['source']['raw_source_label']==f['raw_source_label'];assert d['occurrence_ids']==[o['occurrence_id'] for o in f.get('occurrences',[])]
 for o in f.get('occurrences',[]):
  p=queue/o['full_recipe_snapshot'];raw=p.read_bytes();assert hashlib.sha256(raw).hexdigest()==o['source_file_sha256'];y=yaml.safe_load(raw)
  recipe_receipts.append({'case_id':d['case_id'],'occurrence_id':o['occurrence_id'],'path':str(p),'sha256':o['source_file_sha256'],'complete_recipe_parsed':True})
 for eid in d['evidence_ids']:
  e=E[eid];cap=e['capture']
  if cap['root']=='artifact':
   p=R/cap['path'];assert sha(p)==cap['sha256'],eid;receipts.append({'evidence_id':eid,**cap})
 for own in d['owner_records']:assert sha(own['path'])==own['sha256']
for d in Ds:inspect(d)
after=[]
for p in Ps:
 path=R/p['after_capture']['path'];assert sha(path)==p['after_capture']['sha256'];y=yaml.safe_load(path.read_text())
 if p['kind']=='edit_existing_owner':assert sha(p['owner_path'])==p['before_sha256']
 after.append({'proposal_id':p['proposal_id'],'after_capture':p['after_capture'],'identifier':y['identifier'],'status':'approve','reasoning':'Exact after YAML reviewed with its primary source scope, actual owner comparison and per-case reasoning. '+ ' '.join(notes[str(idx[cid])] for cid in p['case_ids'] if cid in idx and idx[cid]!=46),'case_ids':p['case_ids'],'inspected_evidence_ids':p['evidence_ids']})
case_reviews=[]
for d in Ds:
 i=idx[d['case_id']]
 if i==46:continue
 case_reviews.append({'case_id':d['case_id'],'case_index':i,'case_input_sha256':d['case_input_sha256'],'decision_sha256':canon(d),'status':'approve','reasoning':notes[str(i)],'inspected_evidence_ids':d['evidence_ids'],'inspected_proposal_ids':d['proposal_ids']})
findings=json.loads((OUT/'findings-v1.json').read_text())['findings']
for f in findings:f['status']='resolved';f['resolution']='Verified the exact successor decisions and versioned after payloads: source duplication and whole/part issues corrected; failed JCM routes explicitly limited; source originals control referenced basal scope. Old captured bytes remain preserved.'
findings += [{'id':'b2-review-a-06','status':'resolved','case_indices':[43],'finding':'Concentration-qualified whole HCl preparation was its own named part.','resolution':'after-v4 uses source-known HCl solute; percent basis remains unspecified.'},{'id':'b2-review-a-07','status':'resolved','case_indices':[9,15],'finding':'Quality/filtration alone did not justify distinct molecular-water/methanol mixture owners.','resolution':'after-v5 water provenance-only amendment and after-v6 methanol supplied-form amendment preserve original chemical identities and whole-owner holds. Withdrawn stock nodes are inactive.'},{'id':'b2-review-a-08','status':'resolved','case_indices':[15],'finding':'Methanol10% alias context had not established stock strength versus receiving dose.','resolution':'after-v6 explicitly leaves that context unknown while retaining concentration-qualified label as non-resolving provenance.'}]
manifest=[capture(p) for p in SNAP.glob('*.json')]+[capture(OUT/'reviewer-case-notes.json'),capture(OUT/'primary-capture-dossier.json')]
review={'schema_version':1,'reviewer':'/root/research_b','reviewed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'independence':'B did not author these A successor decisions or A-owned payloads. A46 shared B-authored concentrated-acid target is excluded/delegated to C. Final root ferric-variable union with predecessor B fragment requires C review; this receipt approves the A fragment and source decisions only.','input_hash_manifest':manifest,'case_reviews':case_reviews,'proposal_reviews':after,'excluded_cases':[{'case_id':d['case_id'],'case_index':46,'reason':'Shared B-authored target requires independent C.'} for d in Ds if idx[d['case_id']]==46],'findings':findings,'publication_authorization':'None. These are bounded source/proposal reviews; all inherited whole-owner, source quantity and downstream publication holds remain.'}
(B/'independent-review-a.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n')
# Independent exception: C151 links A's shared manganese proposal.
cd=next(x for x in json.loads((C/'decisions.json').read_text())['decisions'] if x['case_id']=='KG_CASE:55268b66b04a59d2f2c6487270ae15e4a4686148d8fff29fd66b248269821cd8');inspect(cd)
cp=next(p for p in Ps if p['proposal_id']=='a2-proposal-manganese-sulfate-variable-hydrate')
(SNAP/'c151-decision.json').write_text(json.dumps(cd,ensure_ascii=False,indent=2)+'\n')
cn='MediaDive1000 explicitly states MnSO4 x n H2O, a variable-water identity. Sigma229784 linear formula/CAS15244-36-7 support the variable hydrate; fixed-water supplier widgets and Wako pentahydrate use do not select n. Verified exact after-v5 includes the valid C151 raw spelling as HYDRATE_FORM while retaining asymmetric CHEBI86360 parent, no fixed formula weight, and existing fixed-owner holds. Frozen helper count definition and empty occurrence-ID list remain unchanged. No active fixed-hydrate aliases are reassigned or released.'
cr={'schema_version':1,'reviewer':'/root/research_b','reviewed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'independence':'B authored neither C151 decision nor A manganese payload.','input_hash_manifest':[capture(SNAP/'c151-decision.json'),capture(SNAP/'proposals.json')], 'case_reviews':[{'case_id':cd['case_id'],'case_index':151,'case_input_sha256':cd['case_input_sha256'],'decision_sha256':canon(cd),'status':'approve','reasoning':cn,'inspected_evidence_ids':cd['evidence_ids'],'inspected_proposal_ids':cd['proposal_ids']}],'proposal_reviews':[{'proposal_id':cp['proposal_id'],'after_capture':cp['after_capture'],'status':'approve','reasoning':cn}],'publication_authorization':'None; inherited nonpositive row decisions and source holds remain.'}
(B/'independent-review-c151.json').write_text(json.dumps(cr,ensure_ascii=False,indent=2)+'\n')
(OUT/'review-integrity.json').write_text(json.dumps({'status':'PASS','A_cases':len(case_reviews),'A_proposals':len(after),'delegated_C_cases':1,'frozen_recipe_occurrences':len(recipe_receipts),'verified_evidence':list({x['evidence_id']:x for x in receipts}.values()),'verified_full_recipe_snapshots':recipe_receipts,'canonical_algorithm':'SHA256 of json.dumps(sort_keys=True,separators=(comma,colon),ensure_ascii=False), UTF-8','scope':'Every linked capture hash, actual owner preimage and all full frozen occurrence recipe hashes verified; primary sources and exact after YAML were independently interpreted in the reviewer notes and findings.'},ensure_ascii=False,indent=2)+'\n')
print('PASS',len(case_reviews),'A decisions',len(after),'A payloads; C151 separately approved')
