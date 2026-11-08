import pathlib,json,copy,hashlib,datetime,sys,yaml
sys.path.insert(0,str(pathlib.Path('src').resolve()))
from mediaingredientmech.validation.write_validated import write_validated_ingredient
from mediaingredientmech.curate.curation_event import record_curation_event
R=pathlib.Path('reports/all_unmatched_20261107/worker-01');O=R/'shard/concentration_stocks';C=O/'captures';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat().replace('+00:00','Z');save=lambda p,x:p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
D=json.loads((O/'decisions.fragment.json').read_text());E=json.loads((O/'evidence.fragment.json').read_text());Q=json.loads((O/'proposals.fragment.json').read_text());q=next(q for q in Q['proposals'] if q['proposal_id']=='CS-PROP-NBRC943_METAL_SALT_44_STOCK');d=next(d for d in D['decisions'] if d['allocation_index']==98)
archive=O/'before-metal44-v3';archive.mkdir(exist_ok=False)
for n in ['decisions','evidence','proposals']:(archive/(n+'.fragment.json')).write_bytes((O/(n+'.fragment.json')).read_bytes())
old=copy.deepcopy(q['after_capture']);p=O/old['path'];assert sha(p)==old['sha256'];a=yaml.safe_load(p.read_text());before=copy.deepcopy(a)
oldtext='This is a distinct10fold moreconcentrated preparation, not an alias or merge of those candidates.'
newtext='This formulation has tenfold the precursor mass per stated added-water volume of those candidates. An exact ratio of final solution concentrations is not established because measured final volumes are not supplied. The source preparations are therefore not merged.'
assert oldtext in a['notes'];a['notes']=a['notes'].replace(oldtext,newtext)
for e in a['ontology_mapping']['evidence']:e['notes']=e['notes'].replace(oldtext,newtext)
record_curation_event(a,curator='worker01_add_media_source_stock',action='CORRECTED',changes='Correct active Metal44 comparison prose: tenfold precursor mass per added-water volume, not a demonstrated tenfold final concentration. Literal component amounts and units are unchanged. Prior draft wording remains in immutable proposal/history, explicitly superseded by this event.',previous_status='MAPPED',new_status='MAPPED',llm_assisted=True)
after=O/'proposals/NBRC943_Metal_Salt_44_Stock-v3.yaml';assert not after.exists();write_validated_ingredient(a,after);assert a['components']==before['components'] and a['curation_history'][:-1]==before['curation_history'];q['superseded_after_capture_v2']=old;q['after_capture']=dict(root='artifact',path=str(after.relative_to(O)),sha256=sha(after));q['description']=q['description'].replace(oldtext,newtext);d['reasoning']=d['reasoning'].replace(oldtext,newtext)
audit=json.loads((O/'completeness-audit-all78-v1.json').read_text());audit=json.loads(json.dumps(audit,ensure_ascii=False).replace(oldtext,newtext));save(O/'completeness-audit-all78-v2.json',audit)
con=json.loads((C/'crosslane-consolidation-final-v2.json').read_text());con['at']=now();con['supersedes']='crosslane-consolidation-final-v2.json for Metal44 corrected prose payload only; other canonical payloads unchanged'
for x in con['records']:
 if x['proposal_id']==q['proposal_id']:x['after_capture']=q['after_capture'];x['worker01_root_after_capture']=dict(root='artifact',path='shard/concentration_stocks/'+q['after_capture']['path'],sha256=q['after_capture']['sha256'])
save(C/'crosslane-consolidation-final-v3.json',con);receipt=C/'metal44-prose-quantity-correction-v3.json';save(receipt,dict(at=now(),origin='Coordinator root identified imprecise final-concentration comparison',before_capture=old,after_capture=q['after_capture'],old_text=oldtext,new_text=newtext,components_unchanged=True,history_preserved=True,maintained_data_changed=False))
eid='CS-COMP-METAL44-QUANTITY-V3';E['evidence'].append(dict(evidence_id=eid,kind='local_validation',capture=dict(root='artifact',path=str(receipt.relative_to(O)),sha256=sha(receipt)),locator='Exact prior/current payload hashes, active wording correction and preserved literal components',supports_or_contradicts='Final concentration ratio is not inferred from added-water ratio.',url=None,accessed_at=now(),case_ids=q['case_ids']));d['evidence_ids'].append(eid);q['evidence_ids'].append(eid)
for d in D['decisions']:d['evidence_ids']=[x for x in d['evidence_ids'] if x!='CS-COMP-NATIVE-STOCK-V2']
for q in Q['proposals']:q['evidence_ids']=[x for x in q['evidence_ids'] if x!='CS-COMP-NATIVE-STOCK-V2']
for n,x in [('decisions',D),('evidence',E),('proposals',Q)]:save(O/(n+'.fragment.json'),x)
print(after,sha(after))
