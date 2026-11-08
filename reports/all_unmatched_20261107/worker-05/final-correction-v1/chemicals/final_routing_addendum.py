from pathlib import Path
from datetime import datetime, timezone
import json, hashlib, yaml, copy, difflib, sys
sys.path.insert(0,str(Path('src').resolve()))
from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.validation.write_validated import write_validated_ingredient
O=Path(__file__).resolve().parent; S=O.parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ref(p):return {'root':'artifact','path':'final-correction-v1/chemicals/'+str(p.relative_to(O)),'sha256':sha(p)}
def dump(n,x):
 p=O/n;assert not p.exists();p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
P=json.loads((O/'proposals-v2.json').read_text());p=next(x for x in P if x['proposal_id']=='CHEM-C1193-tellurium-dioxide');src=O/Path(p['after_capture']['path']).relative_to('final-correction-v1/chemicals');d=yaml.safe_load(src.read_text());before=copy.deepcopy(d)
old='Separate coordinator issue routing remains pending; the Tris issue does not cover this owner.'
assert old in d['notes'];d['notes']=d['notes'].replace(old,'Coordinator issue routing is now filed at https://github.com/CultureBotAI/MediaIngredientMech/issues/1240; the separate Tris issue #1238 does not cover this owner.')
record_curation_event(d,curator='Codex worker05 /root/chemicals_research final report correction',action='CORRECTED_REPORT_PROPOSAL',changes='Update current issue-routing note after reading filed #1240. Preserve the original before-fix referral and prior history; no scientific, component, identity or grade change.',previous_status=d['mapping_status'],new_status=d['mapping_status'],llm_assisted=True,llm_model='gpt-6',timestamp=datetime.now(timezone.utc).isoformat())
dst=O/'proposed-v3'/src.name;assert not dst.exists();dst.parent.mkdir(exist_ok=True);write_validated_ingredient(d,dst,target_class='IngredientRecord');assert yaml.safe_load(dst.read_text())==d
dp=O/'tellurium-routing-v3.diff';assert not dp.exists();dp.write_text(''.join(difflib.unified_diff(src.read_text().splitlines(True),dst.read_text().splitlines(True),fromfile=str(src),tofile=str(dst))))
p['final_correction']['v2_after_capture']=p['after_capture'];p['final_correction']['v3_routing_diff']=ref(dp);p['after_capture']=ref(dst);dump('proposals-v3.json',P)
F=json.loads((O/'finding-dispositions-v1.json').read_text());E=json.loads((O/'evidence-v1.json').read_text())
for f in F['findings']:
 if f['finding_id']=='W05-FINAL-CHEM-NEW-01':
  f['github_routing']='https://github.com/CultureBotAI/MediaIngredientMech/issues/1240';n=json.loads((O/'new-tellurium-grade-finding-v1.json').read_text());f['primary_evidence_bindings']=[e for e in n['primary_evidence'] if e['kind'] in ['primary_source','ontology']]
 elif f['finding_id'] in ['W05-FINAL-CHEM-NEW-02','W05-FINAL-CHEM-NEW-03']:
  f['github_routing']='https://github.com/CultureBotAI/MediaIngredientMech/issues/1237#issuecomment-6718873227'
 f['final_payloads']=[{'proposal_id':p['proposal_id'],'after_capture':p['after_capture']} for p in P if p['proposal_id'] in [r['proposal_id'] for r in f.get('final_payloads',[])]]
F['predecessor_finding_ledger']=ref(O/'finding-dispositions-v1.json');F['current_proposal_manifest']=ref(O/'proposals-v3.json');F['routing_captures']=[{'path':str(x),'sha256':sha(x)} for x in [S/'issues/latest-eight-final-v1.json',S/'issues/final-followups-v1/1237-comments.json']];dump('finding-dispositions-v2.json',F)
dump('routing-addendum-v3.json',{'author':'/root/chemicals_research','before':ref(src),'after':ref(dst),'diff':ref(dp),'proposals':ref(O/'proposals-v3.json'),'guarded_schema_and_roundtrip':'PASS','changed_current_fields':['notes'],'appended_history_events':1,'scientific_claims_unchanged':True,'supersession':'All case conclusions, source read ledger, occurrence routes and conditional matrix remain scientifically identical. This addendum replaces only the Tellurium after hash in their proposal-v2 bindings. Full independent review must bind proposals-v3.'})
print(json.dumps({'proposal_manifest_sha256':sha(O/'proposals-v3.json'),'tellurium_sha256':sha(dst),'finding_ledger_sha256':sha(O/'finding-dispositions-v2.json')}))
