import json,hashlib,yaml,copy,re,html
from pathlib import Path
from datetime import datetime,timezone
R=Path.cwd();P=R/'reports/all_unmatched_20261107/worker-10';S=P/'successor-v1';K=S/'kg';I=S/'reviews/root-kg-v1-inputs';Q=R.parents[2]/'queue/preliminary-v5'
sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
v1=json.loads((S/'reviews/root-kg-review-v1.json').read_text());D=json.loads((K/'decisions.json').read_text())['decisions'];E={e['evidence_id']:e for e in json.loads((P/'evidence.json').read_text())['evidence']+json.loads((K/'evidence.json').read_text())['evidence']};PR=json.loads((K/'proposals.json').read_text())['proposals'];C=json.loads((Q/'shards/shard-10.json').read_text())['cases'];ix={c['case_id']:i for i,c in enumerate(C)}
old={d['case_id']:d for d in v1['case_assessments']};checks=[]
for d in D:
 i=ix[d['case_id']];assert d['case_input_sha256']==hashlib.sha256(json.dumps(C[i],sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest();r=copy.deepcopy(old[d['case_id']]);r['result']='accept_bounded_scope';r['checked_evidence']=[]
 for key in d['evidence_ids']:
  e=E[key];f=(P if e['capture']['root']=='artifact' else Q)/e['capture']['path'];assert sha(f)==e['capture']['sha256'];f.read_bytes();r['checked_evidence'].append({'evidence_id':key,'sha256':sha(f)})
 for o in d['owner_records']:assert sha(R/o['path'])==o['sha256']
 if i==178:r['assessment']='Re-read direct JCM1270:44g BD-Difco dry base,50mL sheepblood,950mL water and70C15min bloodtreatment. Author now states sheep everywhere; derivative MediaDive still incorrectly says horse and100mL. Exactdrybase identity unaffected. No bloodcomponent or changed quantitative source approved.'
 if i==183:r['assessment']='Followed direct primary JCM391→403 crossreference. JCM403 prints100mL10mM,pH7.1 sodiumphosphatebuffer in vitamins and separate25mM,pH3.4 in thiamine. New proposal preserves only first stock, nominalpartialphosphate and no exactsalt/ratio/solvent guess. All repeated citation claims corrected.'
 if i in [168,170]:r['assessment']='Historical DATABASE_MATCH evidence is now preserved byte-equivalent in mapping evidence and prior compound identifier explicit in notes/history. Named isomeric pigment mixture correction remains supported; no particular fraction or four-component proportion asserted.'
 if i==175:r['assessment']='Case-specific reasoning now correctly says MediaDive23. CAS127-09-3 and drysodiumacetate identity alreadyowned; no stockalias approval.'
 checks.append(r)
payloads=[]
for p in PR:
 f=P/p['after_capture']['path'];assert sha(f)==p['after_capture']['sha256'];a=yaml.safe_load(f.read_text());b=yaml.safe_load((R/p['owner_path']).read_text()) if p['kind']=='edit_existing_owner' else {}
 if b:assert sha(R/p['owner_path'])==p['before_sha256']
 archived=K/'history/author-v1/proposed'/f.name;oldpayload=yaml.safe_load(archived.read_text())
 payloads.append({'proposal_id':p['proposal_id'],'after_capture':p['after_capture'],'before_sha256':p['before_sha256'],'changed_fields_from_owner':[k for k in set(a)|set(b) if a.get(k)!=b.get(k)],'changed_fields_from_v1':[k for k in set(a)|set(oldpayload) if a.get(k)!=oldpayload.get(k)],'result':'accept_bounded_scope','limits':'Exact isolated payload only; no maintained application, inherited role/alias/export clearance or cross-shard merge.'})
lookup=json.loads((K/'component-owner-lookup.json').read_text())
for f,r in lookup['resolved_component_preimages'].items():assert sha(R/f)==r['sha256'];assert (R/f).read_text()==r['raw_text']
ind=next(p for p in PR if p['proposal_id']=='sv1-kg-indochrome-mixture');a=yaml.safe_load((P/ind['after_capture']['path']).read_text());b=yaml.safe_load((R/ind['owner_path']).read_text());assert all(e in a['ontology_mapping']['evidence'] for e in b['ontology_mapping']['evidence'])
report={'schema_version':1,'reviewer':'/root','author':'/root/kg_research','independence':v1['independence'],'reviewed_at':datetime.now(timezone.utc).isoformat(),'status':'complete','scope':'All38 KG successor decisions and19 exactpayloads after separate author remediation; allcurrentbindings rechecked. Historical44 unchanged cases are not in this review.','inputs':{n:sha(K/n) for n in ['decisions.json','evidence.json','proposals.json']},'initial_review':{'path':'successor-v1/reviews/root-kg-review-v1.json','sha256':sha(S/'reviews/root-kg-review-v1.json')},'case_assessments':checks,'payload_assessments':payloads,'finding_resolutions':[{'id':f['id'],'status':'corrected_and_rechecked','description':f['finding']} for f in v1['findings']],'additional_rechecks':['Case175 source-specific23 attribution corrected.','Five componentowners verified exactpreimages and scopes; broad proteosepeptone doesnot substitute brandedNo3, hence ColumbiaNo3 remainsUNMAPPED.','Unchanged G/H/B, namedproduct/material, PIPESacid, DLracemate and rice proposals retain initial source-specific rationale; no releaseapproval.','Bio53 can share swine1076b proposal only with independent bio applicability review and explicit final casebacklink.'],'limitations':v1['limitations']}
f=S/'reviews/root-kg-review-v2.json';assert not f.exists();f.write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n');print(len(checks),len(payloads),sha(f))
