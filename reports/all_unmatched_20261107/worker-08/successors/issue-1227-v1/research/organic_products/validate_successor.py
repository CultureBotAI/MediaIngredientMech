"""Read-only source, payload and immutable-input checks for the organic successor."""
import copy,datetime,hashlib,json,pathlib
import yaml
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy
from mediaingredientmech.validation.write_validated import validate_ingredient
B=pathlib.Path('reports/all_unmatched_20261107/worker-08');O=B/'successors/issue-1227-v1/research/organic_products'
SRC=pathlib.Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(p):
    with pathlib.Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def dg(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest()
def dump(name,x):
    p=O/name
    if p.exists():raise RuntimeError('No overwrite: '+str(p))
    p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
A=json.loads((O/'assignment.json').read_text());D=json.loads((O/'decisions.json').read_text())['decisions'];P=json.loads((O/'proposals.json').read_text())['proposals']
E={x['evidence_id']:x for x in json.loads((B/'successors/issue-1201-v1/evidence.json').read_text())['evidence']}
E.update({x['evidence_id']:x for x in json.loads((O/'evidence-additions.json').read_text())['evidence']})
C={x['case_id']:x for x in json.loads((B/'provenance/shard-08.json').read_text())['cases']}
ad={x['case_id']:x for x in A['decisions']};ap={x['proposal_id']:x for x in A['proposals']};pm={x['proposal_id']:x for x in P}
assert set(ad)=={x['case_id']for x in D} and set(ap)==set(pm)
readledger={};caseassess=[];errs=[];immutable=[]
for d in D:
    old=ad[d['case_id']];c=C[d['case_id']]
    for k in ['case_input_sha256','source','occurrence_ids','preserved_native_decisions','proposal_ids','owner_records']:
        assert d[k]==old[k],(d['case_id'],k)
    assert dg(c)==d['case_input_sha256']
    sources=[]
    for eid in d['evidence_ids']:
        e=E[eid];cap=e['capture'];p=(B if cap['root']=='artifact'else SRC)/cap['path'];data=p.read_bytes();actual=hashlib.sha256(data).hexdigest();assert actual==cap['sha256'],str(p)
        key=cap['root']+':'+cap['path'];rr=readledger.setdefault(key,{'capture':cap,'kinds':[],'evidence_ids':[],'locators':[],'case_ids':[],'read_status':'exact retained capture bytes read and SHA256 verified; original URL/acquisition time unchanged','new_remote_access':eid.startswith('op1227-nbrc')or eid.startswith('op1227-failed')})
        for field,val in [('kinds',e['kind']),('evidence_ids',eid),('locators',e['locator']),('case_ids',d['case_id'])]:
            if val not in rr[field]:rr[field].append(val)
        if p.suffix in ['.json','.yaml','.yml']:
            # Parse full records, rather than declaring success on just a digest.
            if p.suffix=='.json':json.loads(data)
            else:yaml.safe_load(data)
        if e['kind'] in ['primary_source','ontology','source_snapshot','unsuccessful_search']:sources.append({'evidence_id':eid,'capture':cap,'locator':e['locator'],'kind':e['kind']})
    context=[]
    for oc in c.get('occurrences',[]):
        q=SRC/oc['full_recipe_snapshot'];raw=q.read_bytes();assert hashlib.sha256(raw).hexdigest()==oc['source_file_sha256']
        obj=yaml.safe_load(raw);v=obj
        for t in oc['component_path'].split('/'):v=v[int(t)]if isinstance(v,list)else v[t]
        assert v==oc['raw_component'],oc['occurrence_id']
        context.append({'occurrence_id':oc['occurrence_id'],'recipe_id':oc['recipe_id'],'capture':{'root':'source','path':oc['full_recipe_snapshot'],'sha256':oc['source_file_sha256']},'locator':oc['component_path'],'raw_component_sha256':dg(v),'full_record_parsed':True})
    if not d['proposal_ids']:assert d['no_change_reason']
    for pid in d['proposal_ids']:assert d['case_id']in pm[pid]['case_ids']
    caseassess.append({'case_id':d['case_id'],'case_input_sha256':d['case_input_sha256'],'final_decision_sha256':dg(d),'source_label':d['source']['source_label'],'source_outcome':d['disposition'],'author_appraisal':d['reasoning'],'source_applicability':d['applicability'],'missing_fact_or_boundary':d['missing_requirement'],'proposal_ids':d['proposal_ids'],'source_evidence':sources,'complete_occurrence_contexts':context,'all_original_occurrences_preserved':True,'all_native_decisions_preserved':True,'all_embedded_case_holds_bound_by_unchanged_case_digest':True,'independent_review':'pending; author reassessment only'})
baseline={str(p):yaml.safe_load(p.read_text())for p in pathlib.Path('data/ingredients').rglob('*.yaml')}
base_viol=validate_component_partonomy(baseline.values());assert not base_viol
allprops=[]
for f in (B/'successors/issue-1227-v1/research').glob('*/assignment.json'):
    allprops+=json.loads(f.read_text())['proposals']
overlay=copy.deepcopy(baseline);payloads=[];owners=set()
for q in allprops:
    p=pm.get(q['proposal_id'],q);path=B/p['after_capture']['path'];record=yaml.safe_load(path.read_text());assert sha(path)==p['after_capture']['sha256'];assert p['owner_path']not in owners;owners.add(p['owner_path'])
    if p['proposal_id']in pm:
        old=ap[p['proposal_id']];assert(p['kind'],p['owner_path'],p['before_sha256'],p['case_ids'])==(old['kind'],old['owner_path'],old['before_sha256'],old['case_ids'])
        if p['before_sha256']:assert sha(p['owner_path'])==p['before_sha256']
        assert not validate_ingredient(record)
        orig=yaml.safe_load((B/old['after_capture']['path']).read_text());assert record.get('curation_history',[])[:len(orig.get('curation_history',[]))]==orig.get('curation_history',[])
        for k in ['occurrence_statistics','nutritional_roles','environmental_roles','biological_roles','metabolic_roles','application_roles','roles','culturemech_reference','supplied_form']:
            assert record.get(k)==orig.get(k),(p['proposal_id'],k)
        for cid in p['case_ids']:assert p['proposal_id']in next(d for d in D if d['case_id']==cid)['proposal_ids']
        payloads.append({'proposal_id':p['proposal_id'],'owner_path':p['owner_path'],'before_sha256':p['before_sha256'],'after_sha256':sha(path),'input_after_sha256':old['after_capture']['sha256'],'changed':sha(path)!=old['after_capture']['sha256'],'all_history_roles_counts_source_links_preserved':True})
    overlay[p['owner_path']]=record
viol=validate_component_partonomy(overlay.values());assert not viol,list(map(str,viol))
components=[]
unmapped={
 ('op1201-r2a-medium',2):'The named Casamino-acids constituent is retained. The generic catalog owner FOODON:03315719 denotes the broader mammalian milk-protein hydrolysate class and is shared with casein peptone; the vitamin-assay registry owner specifies a narrower grade absent here. No exact identity bridge is established by a shared name alone.',
 ('op1201-trypticase-soy-broth',0):'Source definition explicitly names pancreatic digest of casein (casitone). The catalog Tryptone owner carries this only as a related synonym with multiple product scopes; assigning the named source digest to one product identity needs a process/product-scope bridge. No component is forced to the broader milk-hydrolysate FOODON class.',
 ('op1201-trypticase-soy-broth',1):'Source specifies papaic soybean digest. Generic soy-peptone owners share a broader vegetable-protein hydrolysate identity with unresolved exact product/process aliases; no exact papaic-digest identity is independently established by those inherited aliases. The named constituent remains usable as UNMAPPED under section6.',
 ('op1201-amphotericin-stock',0):'The source does not select amphotericin A/B or supplied counterion/formulation. NCIT:C124792 requires B; the existing generic Amphotericin owner is UNMAPPED. Preserve the named constituent and source concentration without inventing a congener.'}
for p in P:
    x=overlay[p['owner_path']]
    for i,c in enumerate(x.get('components',[])):
        candidates=[{'path':path,'identifier':v['identifier'],'preferred_term':v['preferred_term'],'sha256':sha(path)if pathlib.Path(path).exists()else None}for path,v in baseline.items()if v.get('mapping_status')!='REJECTED' and v.get('identifier')==c.get('component_id')]
        explanation=unmapped.get((p['proposal_id'],i),'Exact named constituent reference is retained at the source-established form; native entity/label admission passes. This does not approve target roles, whole products or export payloads.')
        if p['proposal_id']=='op1201-r2a-medium'and i==5:explanation='Coordinator-routed OP1227-REF-002: source ontology definition literally names pyruvate; CHEBI:15361 is the exact named anion entity. This reference asserts that definition-level part only, not a sodium salt, supplied reagent grade or quantity.'
        components.append({'proposal_id':p['proposal_id'],'component_index':i,'component':c,'assertion_method':x['component_assertion']['method'],'completeness':x['component_assertion']['completeness'],'catalog_candidates':candidates,'appraisal':explanation})
# Verify every old selected payload and the maintained publication surfaces remain unchanged.
for p in A['proposals']:assert sha(B/p['after_capture']['path'])==p['after_capture']['sha256'];immutable.append({'path':p['after_capture']['path'],'sha256':p['after_capture']['sha256']})
prev=json.loads((B/'provenance/maintained-surfaces-before.json').read_text())['files'];changed=[]
for p,h in prev.items():
    if not pathlib.Path(p).is_file()or sha(p)!=h:changed.append(p)
assert not changed,changed
dump('source-read-ledger.json',{'at':NOW,'scope':'All51 frozen source cases, full source records through exact occurrence locators, and retained evidence bytes used in this bounded author reassessment. Remote retrieval was repeated only for the three explicit nalidixic URLs. Historical literature captures retain their original limited inspected scope; no unread full-paper claim.','captures':list(readledger.values()),'failed_exact_reads':['NBRC1314','TOGO M2023'],'successful_new_primary_read':'NBRC1301','case_ids':[d['case_id']for d in D]})
dump('source-assessment.json',{'at':NOW,'author':'worker08:/root/organics','case_reviews':caseassess,'approval_boundary':'Author full-scope reassessment; separate independent review pending. No native hold, role, supported export or coalescence approval.'})
dump('component-reference-assessment.json',{'at':NOW,'scope':'Every immediate component in the31 organic selected payloads; UNMAPPED is permitted and is not automatically a defect.','component_reviews':components})
dump('validation.json',{'at':NOW,'status':'PASS','case_count':len(D),'proposal_count':len(P),'changed_payload_count':sum(x['changed']for x in payloads),'unchanged_payload_count':sum(not x['changed']for x in payloads),'all_case_digests_occurrences_native_holds_preserved':True,'all31_exact_preimages_and_history_roles_counts_checked':True,'all_referenced_capture_hashes_verified':len(readledger),'all_active_overlay_payloads':len(allprops),'baseline_records':len(baseline),'overlay_records':len(overlay),'baseline_partonomy_errors':list(map(str,base_viol)),'overlay_partonomy_errors':list(map(str,viol)),'maintained_files_verified':len(prev),'maintained_changed':changed,'payloads':payloads,'immutable_predecessor_payloads':immutable,'scientific_approval':False,'independent_review':'pending'})
print(json.dumps({'status':'PASS','cases':len(D),'payloads':len(P),'captures':len(readledger),'components':len(components),'baseline_records':len(baseline),'overlay_records':len(overlay)}))
