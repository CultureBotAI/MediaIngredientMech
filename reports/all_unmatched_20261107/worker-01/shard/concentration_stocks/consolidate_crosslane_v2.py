import pathlib,json,copy,hashlib,datetime,sys,yaml
sys.path.insert(0,str(pathlib.Path('src').resolve()))
from mediaingredientmech.validation.write_validated import write_validated_ingredient
from mediaingredientmech.curate.curation_event import record_curation_event
R=pathlib.Path('reports/all_unmatched_20261107/worker-01');O=R/'shard/concentration_stocks';N=R/'shard/named_stocks';C=O/'captures';P=O/'proposals'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat().replace('+00:00','Z');save=lambda p,x:p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
D=json.loads((O/'decisions.fragment.json').read_text());E=json.loads((O/'evidence.fragment.json').read_text());Q=json.loads((O/'proposals.fragment.json').read_text());qs={q['proposal_id']:q for q in Q['proposals']};ds={d['case_id']:d for d in D['decisions']}
archive=O/'before-crosslane-v2';archive.mkdir(exist_ok=False)
for n in ['decisions','evidence','proposals']:(archive/(n+'.fragment.json')).write_bytes((O/(n+'.fragment.json')).read_bytes())
request=N/'crosslane-consolidation-request.json';req=json.loads(request.read_text());captured=C/'crosslane-request-observed-v2.json';captured.write_bytes(request.read_bytes())
rows=[];added={e['evidence_id'] for e in E['evidence']}
for m in req['records']:
 q=qs[m['canonical_proposal_id']];old=copy.deepcopy(q['after_capture']);bp=O/old['path'];assert sha(bp)==old['sha256'];a=yaml.safe_load(bp.read_text());raw=m['named_raw_label_to_preserve_nonresolving']
 if raw and raw not in [s['synonym_text'] for s in a['synonyms']]:a['synonyms'].append(dict(synonym_text=raw,synonym_type='REJECTED_LABEL',source='Frozen named-stock occurrence '+','.join(m['named_occurrence_ids'])+'; source-qualified binding only, no global alias resolution.'))
 if 'SULFIDE' in q['proposal_id']:
  detail='NBRC1257 uses 12 g Na2S·9H2O plus 50 mL distilled water; NBRC1321 uses 24 g plus 100 mL. Both give the same precursor-to-added-water ratio, call the preparation 1.0 M, specify filtration and storage under N2. This is formulation equivalence at scaled batch size, not a claim that either is made up to a final volume.'
 elif 'BICARBONATE' in q['proposal_id']:detail='NBRC1257 and NBRC1321 both specify 8.4 g NaHCO3 plus 100 mL distilled water, CO2 saturation and autoclaving in tightly sealed CO2-filled bottles. The source qualification and complete preparation establish the same stock; neither source states make-up to a final 100 mL.'
 elif 'METAL' in q['proposal_id']:detail='Both lane proposals transcribe the same NBRC943 Metal salt solution44 table. In named case116 it is a 50 mL nested component of Modified Hutner solution, not the whole Hutner preparation or an exact alias for it. Canonical stock identity is shared; the parent keeps its separate stock identity.'
 else:detail='NBRC1339 and its TOGO M2041 recipe refer to the same 250 mM phenanthrene in DMSO stock, filtered with DMSO-safe filters. The unqualified Phenanthrene solution label requires this occurrence context.'
 a['notes']+=' Cross-lane deduplication: '+detail
 a['ontology_mapping']['evidence'].append(dict(evidence_type='MANUAL_CURATION',source=m['primary_evidence'][0]['url'],notes=detail))
 record_curation_event(a,curator='worker01_add_media_source_stock',action='CORRECTED',changes='Consolidate exact cross-lane proposal identity and preserve source-specific labels as REJECTED_LABEL. '+detail+' Earlier draft payloads/reviews remain immutable; no maintained records are changed.',previous_status='MAPPED',new_status='MAPPED',llm_assisted=True)
 pp=P/(bp.stem+'-v2.yaml');assert not pp.exists();write_validated_ingredient(a,pp);q['superseded_after_capture']=old;q['after_capture']=dict(root='artifact',path=str(pp.relative_to(O)),sha256=sha(pp));q['description']+=' '+detail;q['additional_case_backlinks']=[m['named_case_id']];q['crosslane_bindings']=m['named_occurrence_bindings'];q['crosslane_relation']='auxiliary_component' if 'METAL' in q['proposal_id'] else 'same_whole_stock'
 for pe in m['primary_evidence']:
  source=N/pe['capture']['path'];assert sha(source)==pe['capture']['sha256'];ep=C/('crosslane-'+source.name)
  if not ep.exists():ep.write_bytes(source.read_bytes())
  else:assert sha(ep)==sha(source)
  eid='CS-XL-'+pe['evidence_id'];item=copy.deepcopy(pe);item.update(evidence_id=eid,capture=dict(root='artifact',path=str(ep.relative_to(O)),sha256=sha(ep)),case_ids=q['case_ids'])
  if eid not in added:E['evidence'].append(item);added.add(eid)
  else:
   ee=next(x for x in E['evidence'] if x['evidence_id']==eid);ee['case_ids']=sorted(set(ee['case_ids']+q['case_ids']))
  if eid not in q['evidence_ids']:q['evidence_ids'].append(eid)
  for cid in q['case_ids']:
   if eid not in ds[cid]['evidence_ids']:ds[cid]['evidence_ids'].append(eid)
 for cid in q['case_ids']:ds[cid]['reasoning']+=' '+detail
 rows.append(dict(proposal_id=q['proposal_id'],canonical_owner_path=q['owner_path'],after_capture=q['after_capture'],worker01_root_after_capture=dict(root='artifact',path='shard/concentration_stocks/'+q['after_capture']['path'],sha256=q['after_capture']['sha256']),cs_case_ids=q['case_ids'],named_case_id=m['named_case_id'],named_case_index=m['named_case_index'],named_occurrence_ids=m['named_occurrence_ids'],retired_proposal_id=m['named_retired_proposal_id'],retired_named_capture=m['named_retained_after_capture'],relation=q['crosslane_relation'],scientific_basis=detail))
for d in D['decisions']:d['evidence_ids']=[x for x in d['evidence_ids'] if x!='CS-COMP-NATIVE-STOCK-V1']
for q in Q['proposals']:q['evidence_ids']=[x for x in q['evidence_ids'] if x!='CS-COMP-NATIVE-STOCK-V1']
out=C/'crosslane-consolidation-final-v2.json';save(out,dict(at=now(),request_capture=dict(path=str(captured.relative_to(O)),sha256=sha(captured)),records=rows,integration='Emit one canonical proposal per identifier. Union named case/evidence backlinks into that proposal and both decisions. For Metal44 the named case references an auxiliary component, never a whole-Hutner exact mapping. Old named and CS proposal payloads/reviews remain historical. Scientific equivalence is supported here; final independent review is required.'))
eid='CS-XL-CONSOLIDATION-V2';ids=sorted({c for q in rows for c in q['cs_case_ids']});E['evidence'].append(dict(evidence_id=eid,kind='local_validation',capture=dict(root='artifact',path=str(out.relative_to(O)),sha256=sha(out)),locator='Exact canonical/retired proposal correspondence and all source occurrences; four full primary recipe comparisons',supports_or_contradicts='Establishes stock equivalence and preserves source batch quantities and auxiliary-component boundary.',url=None,accessed_at=now(),case_ids=ids))
for cid in ids:ds[cid]['evidence_ids'].append(eid)
for q in Q['proposals']:
 if q['proposal_id'] in [x['proposal_id'] for x in rows]:q['evidence_ids'].append(eid)
for n,x in [('decisions',D),('evidence',E),('proposals',Q)]:save(O/(n+'.fragment.json'),x)
print(json.dumps(rows,indent=2))
