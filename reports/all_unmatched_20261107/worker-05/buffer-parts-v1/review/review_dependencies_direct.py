import json,hashlib,importlib.util,sys
from pathlib import Path
from datetime import datetime,timezone
import yaml
R=Path.cwd();S=R/'.temp/w05-buffer-parts-v1';Q=S/'review';N=S/'dependencies-direct-v1';B=R/'reports/all_unmatched_20261107/worker-05'
def h(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def j(p):return json.loads(Path(p).read_text())
def oh(v):return hashlib.sha256(json.dumps(v,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
def bind(p):return {'path':str(Path(p).relative_to(R)) if Path(p).is_relative_to(R) else str(p),'sha256':h(p)}
def cap(c):
 p=S/c['path'].split('buffer-parts-v1/',1)[1] if c['path'].startswith('buffer-parts-v1/') else B/c['path'];assert h(p)==c['sha256'];return p
man=j(N/'MANIFEST.json');members=man.get('members',man.get('files'));mc=[]
for x in members:
 p=N/x['path'];assert h(p)==x['sha256'];mc.append({'path':x['path'],'sha256':h(p)})
oldPs={p['proposal_id']:p for p in j(S/'dependencies/proposals.json')['proposals']};ps=j(N/'proposals.json')['proposals'];assert len(ps)==len(oldPs)
peer=j(Q/'dependencies/main-review.json');peerp={p['proposal_id']:p for p in peer['payload_reviews']}
oldobs=j(S/'dependencies/source-observations.json');newobs=j(N/'source-observations.json');assert oldobs==newobs
builder=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/kgm-unmapped-20261107/claw/scripts/build_mim_ingredient_sssom.py');assert h(builder)==h(B/'final-correction-v1/inputs/pinned-native-row-builder.py');sys.path.insert(0,str(builder.parent));spec=importlib.util.spec_from_file_location('review_dep_direct_builder',builder);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
changed=[];unchanged=[]
for p in ps:
 old=oldPs[p['proposal_id']];aP=cap(old['after_capture']);zP=cap(p['after_capture'])
 if h(aP)==h(zP):assert p==old;unchanged.append({'proposal_id':p['proposal_id'],'after_capture':p['after_capture'],'scientific_review':bind(Q/'dependencies/main-review.json'),'actual_reviewer':'/root/final_skeptical/preservation_audit'});continue
 a=yaml.safe_load(aP.read_text());z=yaml.safe_load(zP.read_text());idx=peerp[p['proposal_id']]['field_checks']['component_index'];assert z['components'][idx]['component_id']=='mesh:D010461' and a['components'][idx]['component_id']=='kgmicrobe.ingredient:peptone'
 for i,(x,y) in enumerate(zip(a['components'],z['components'])):
  assert {k:v for k,v in x.items() if k!='component_id'}=={k:v for k,v in y.items() if k!='component_id'}
  if i!=idx:assert x==y
 assert len(a['components'])==len(z['components']);assert z['curation_history'][:-1]==a['curation_history'];assert z['component_assertion']['evidence'][:-1]==a['component_assertion']['evidence']
 assert z['component_assertion']['method']==a['component_assertion']['method']=='LABEL_ENUMERATION';assert z['component_assertion']['completeness']==a['component_assertion']['completeness']=='COMPLETE'
 protected={k:a.get(k)==z.get(k) for k in a.keys()|z.keys() if k not in ['components','component_assertion','curation_history','notes']};assert all(protected.values())
 assert z['notes'].startswith(a['notes']) and z['component_assertion']['notes'].startswith(a['component_assertion']['notes'])
 before=m._row_from_yaml(aP,{},{},{},{},record=a,owners={});after=m._row_from_yaml(zP,{},{},{},{},record=z,owners={});assert len(before)==len(after)==1
 assert all(before[0].get(k)==after[0].get(k) for k in before[0].keys()|after[0].keys() if k!='source')
 tid=peerp[p['proposal_id']]['target_id'];obs=[x for x in newobs['rows'] if x['target_id']==tid]
 assert all('peptone' in x['literal'].lower() for x in obs)
 rawscope=[{'csv_row':x['csv_row_including_header'],'field':x['field'],'literal':x['literal'],'source_links':x['source_links'],'source_taxon':x['genus']+' '+x['species'],'complete_source_object_sha256':oh(x)} for x in obs]
 specific={'PC03':'The glucose peptone-yeast extract observation explicitly names peptone; glucose and yeast remain separate.','PC16':'The Peptone-yeast extract-glucose observation explicitly names the generic input; it is not made identical to the reordered PC03 preparation.','PC17':'The explicit peptone+beef+yeast list does not imply the peptone itself derives from beef; adjacent extract scope stays separate.','PC18':'Both peptone+yeast observations retain their original source columns and two distinct source contexts; no whole-formulation equivalence is inferred.','PC19':'The yeast extract+peptone observation names the generic part; it is not merged with the reversed-order owner.'}[tid]
 assess=specific+' The final reference to the independently reviewed ordinary generic mesh:D010461 Peptone owner is supported. Exact complete final payload read, with original labels, quantities/absence, all other parts, prior assertion evidence, history, whole-owner identity, roles/statistics and source holds preserved. New ComponentEvidence is explicitly agent-assisted CURATED_DATASET, not a new human MappingEvidence assertion. COMPLETE remains relative to named-input enumeration. No Bacto, mammalian origin, enzyme, manufacturer, culture recipe completeness, source-assay or export approval follows.'
 changed.append({'target_id':tid,'proposal_id':p['proposal_id'],'proposal_object_sha256':oh(p),'after_capture':p['after_capture'],'reviewer':'/root/final_skeptical','primary_author':'/root/buffer_tris','assessment':assess,'complete_payload_read':True,'protected_fields':protected,'component_before':a['components'][idx],'component_after':z['components'][idx],'actual_source_rows':rawscope,'complete_native_before':before,'complete_native_after':after,'previous_full_scientific_review':bind(Q/'dependencies/main-review.json'),'previous_reviewer':'/root/final_skeptical/preservation_audit','limitations':'Unchanged whole-owner mappings/other part references are preserved historical claims, not newly approved by this bounded generic-reference review.'})
assert len(changed)==5 and len(unchanged)==10
ev0={e['evidence_id']:e for e in j(S/'dependencies/evidence.json')['evidence']};ev=j(N/'evidence.json')['evidence'];new=[]
for e in ev:
 cap(e['capture'])
 if e['evidence_id'] in ev0:assert e==ev0[e['evidence_id']]
 else:new.append({'evidence_id':e['evidence_id'],'kind':e['kind'],'capture':e['capture'],'supports_or_contradicts':e['supports_or_contradicts']})
v={'reviewer':'/root/final_skeptical','completed_at':datetime.now(timezone.utc).isoformat(),'verdict':'pass_with_limitations','payload_reviews':changed,'unchanged_payload_reuse':unchanged,'manifest':bind(N/'MANIFEST.json'),'verified_manifest_members':mc,'source_observations':bind(N/'source-observations.json'),'source_observations_exact_prior':True,'actual_read_scope':'All five complete final YAMLs, source literal/column/taxon/citation fields of six rows, exact prior full scientific assessments and current source/case-delta metadata. The child independently reviewed all130 complete database rows and source passages; no new full underlying-paper or organism-taxonomy approval is claimed here.','new_evidence_reviews':new,'parent_exact_review':bind(Q/'direct-parent-independent-review-v1.json'),'interpretation':bind(Q/'ontology-interpretation-reassessment-v1.json'),'case_deltas':bind(N/'case-deltas.json'),'finding_dispositions':[{'finding_id':'PEPTONE-SOURCE-001','status':'EXACT_PRIOR_BOUNDED_CORRECTIONS_RETAINED','assessment':'All ten prior ambiguous withdrawals including FAB and rumen-base references remain exact. No withdrawn component is restored by the direct generic identifier update.'}],'source_owner_export_approval':False}
p=Q/'dependency-direct-reference-review-v1.json';assert not p.exists();p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n');print(h(p),len(mc),len(new))
