"""Read-only source binding for ten-vitamin routing; writes only this report directory."""
from pathlib import Path
import hashlib,json,subprocess,datetime,yaml
M=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech'); C=M/'.temp/all-unmatched-20261107'; I=C/'integration/worktree'; D=C/'preflight/tenvit-final-application-route-v1'; P=C/'workers/w09/worktree/.temp/tenvit-continuity-resolution-v1'
sha=lambda b:hashlib.sha256(b).hexdigest()
refs={}
def put(name,obj):
 p=D/name;p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('x') as f:json.dump(obj,f,indent=2,ensure_ascii=False);f.write('\n')
def pin(p,copy=None):
 p=Path(p);b=p.read_bytes();r={'path':str(p),'sha256':sha(b),'bytes':len(b)};refs[str(p)]=r
 if copy:
  q=D/'captures'/copy;q.parent.mkdir(parents=True,exist_ok=True)
  with q.open('xb') as f:f.write(b)
  r['captured_path']=str(q.relative_to(D))
 return r
def git(r,*args):return subprocess.check_output(['git','-C',str(r),*args])
def canon(x):return sha(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode())
def load(p):pin(p);return json.loads(p.read_text())
start=datetime.datetime.now(datetime.UTC).isoformat()
for p in [M/'AGENTS.md',I/'MAPPING_SEMANTICS.md',M/'.claude/skills/add-media/SKILL.md',I/'src/mediaingredientmech/curate/campaign_owner_apply.py']:
 pin(p,p.name)
issue=load(D/'issue1237-comment-6719499726-network.json');assert issue['id']==6719499726
before=I/'data/ingredients/mapped/Wolfes_Vitamin_Mix.yaml';candidate=P/'candidates/current-culturebotht-v2/data/ingredients/mapped/Wolfes_Vitamin_Mix.yaml'
assert pin(before,'before-Wolfes_Vitamin_Mix.yaml')['sha256']=='709749bd7c83c38a09400fc1893885ead753847ff9d1cbbe4ec76b431d349738'
assert pin(candidate,'candidate-fe607027.yaml')['sha256']=='fe6070272f269fde7683696e4c46a331902ab88baac8c5cc93db7bddf9d0ec1b'
b=yaml.safe_load(before.read_text());a=yaml.safe_load(candidate.read_text());fields=[k for k in set(a)|set(b) if a.get(k)!=b.get(k)];assert set(fields)=={'components','component_assertion','notes','curation_history'};assert a['curation_history'][:-1]==b['curation_history']
for s in ['HANDOFF.json','MANIFEST.json','source-routing.json','nominal-ten-vitamin-source-description.json','ADJUDICATION.json','OPTIONS.json','validation/current-origin-bridges.json','history/captures/Mixes.csv','primary/captures/C-E-jcm-197.capture','primary/captures/C-E-nbrc-837.capture','primary/captures/vm-fetch-2630e40c26a0b155.capture']:
 pin(P/s,('w09/'+s) if s not in ['MANIFEST.json','source-routing.json'] else None)
for s in ['HANDOFF.json','assessment.json','exact-source-and-candidate-audit.json']:
 pin(C/'preflight/tenvit-continuity-triage-v1'/s,'triage/'+s)
route=load(P/'source-routing.json');case_rows=[]
for x in route['cases']:
 s=x['source_case'];d=x['prior_disposition_full']['current_decision'];case_rows.append({'worker':x['worker'],'case_id':x['case_id'],'case_input_sha256':x['case_sha256'],'source_label':s['source_label'],'occurrence_ids':d['occurrence_ids'],'source_case':s,'prior_decision':d})
assert len(case_rows)==8 and sum(len(x['occurrence_ids']) for x in case_rows)==71
put('eight-cases-and-scopes.json',{'counts':route['counts'],'cases':case_rows,'partitions':route['partitions'],'limits':route['limits']})
all_cases=[]
for p in sorted((C/'queue/preliminary-v5/shards').glob('*.json')):
 d=load(p);all_cases.extend(d['cases'])
assert len(all_cases)==1879 and len({x['case_id'] for x in all_cases})==1879
cb_exact=[x for x in all_cases if str(x['source_label']).casefold()=="wolfe's vitamin mix"]
put('frozen-case-accounting.json',{'source_scope':'All ten explicit frozen shard files, including ignored files; no live membership inferred','total':len(all_cases),'generic_cb_label_case_matches':cb_exact,'explanation':'The generic CB owner is already mapped and has no exact-name case in this unmatched queue. A dependent correction must cite genuine comparator-review causes, not invent a CB campaign case or relabel JCM/NBRC occurrences.'})
workers={};selected=[]
for w,v,oldv,pid in [('06','successor-v5','successor-v4','C-P-JCM197'),('08','successors/issue-1227-plain-flour-v1','successors/issue-1227-v1','vm1201-prop-nbrc903-vitamin')]:
 root=C/f'workers/w{w}/worktree';art=root/f'reports/all_unmatched_20261107/worker-{w}';head=git(root,'rev-parse','HEAD').decode().strip();branch=git(root,'branch','--show-current').decode().strip();remote=(D/f'w{w}-remote.txt').read_text().split();assert remote[0]==head and remote[1]=='refs/heads/'+branch
 sel=pin(art/v/'selection.json',f'w{w}/selection.json'); hand=pin(art/v/'HANDOFF.json',f'w{w}/HANDOFF.json')
 obs={'head':head,'branch':branch,'remote_ref':remote[1],'selector':sel,'handoff':hand,'publication_vs_acceptance':'Current Git publication verified; no scientific acceptance inferred','core':{},'protected_publication_paths':[]}
 cores={}
 for n in ['decisions','proposals','evidence']:
  p=art/v/f'{n}.json';r=pin(p,f'w{w}/{n}.json');rel=str(p.relative_to(root));assert git(root,'show',head+':'+rel)==p.read_bytes();obs['core'][n]=r;cores[n]=json.loads(p.read_text())[n]
 matches=[p for p in cores['proposals'] if p['proposal_id']==pid];assert len(matches)==1;prop=matches[0];old=next(p for p in json.loads((art/oldv/'proposals.json').read_text())['proposals'] if p['proposal_id']==pid)
 pp=art/prop['after_capture']['path'];pr=pin(pp,f'w{w}/selected-payload.yaml');assert pr['sha256']==prop['after_capture']['sha256'];assert git(root,'show',head+':'+str(pp.relative_to(root)))==pp.read_bytes();assert prop==old
 relevant=[x for x in cores['decisions'] if x['case_id'] in prop['case_ids']];assert len(relevant)==len(prop['case_ids'])
 old_ds={x['case_id']:x for x in json.loads((art/oldv/'decisions.json').read_text())['decisions']}
 obs['selected_origin']={'proposal':prop,'proposal_canonical_sha256':canon(prop),'proposal_unchanged_from_predecessor':True,'payload':pr,'case_decisions':relevant,'case_objects_unchanged_from_predecessor':all(x==old_ds[x['case_id']] for x in relevant),'existing_generic_cb_target_proposals':[x for x in cores['proposals'] if x.get('owner_path')=='data/ingredients/mapped/Wolfes_Vitamin_Mix.yaml']}
 for x in relevant:
  frozen=next(y for y in all_cases if y['case_id']==x['case_id']);assert canon(frozen)==x['case_input_sha256']
 assert git(root,'rev-parse','HEAD').decode().strip()==head
 workers[w]=obs;selected.append((w,prop))
put('published-origin-bridges.json',workers)
W=C/'workers/w08/worktree/reports/all_unmatched_20261107/worker-08';V=W/'successors/issue-1227-v1/research/vitamins_mixtures';R=W/'successors/issue-1227-v1/independent-review/vitamins_mixtures/component-review.json'
review=load(R);pin(R,'w08/component-review.json');ontology=load(V/'component-ontology-lookup.json');pin(V/'component-ontology-lookup.json','w08/component-ontology-lookup.json');pin(V/'final-v2/exact-form-ontology-lookup.json','w08/exact-form-ontology-lookup.json')
for f in ['shared-CAS_68-19-9_properties.json','shared-CAS_68-19-9_synonyms.json']:
 pin(W/'research/vitamins_mixtures/captures'/f,'w08/'+f)
ids=['CHEBI:30961','CHEBI:30753','CHEBI:16494','CHEBI:15940','CHEBI:17015','CHEBI:49105',None,'CHEBI:15956','CHEBI:27470','CHEBI:17439']
owner_paths={}
for p in sorted((I/'data/ingredients/mapped').glob('*.yaml')):
 y=yaml.safe_load(p.read_text())
 if y.get('mapping_status')=='MAPPED' and y.get('identifier') in set(ids)|{'CHEBI:31345','CHEBI:176843'}:owner_paths.setdefault(y['identifier'],[]).append((p,y))
children=[]
for ix,(component,id_) in enumerate(zip(a['components'],ids,strict=True)):
 target=id_ or 'CHEBI:31345';owners=owner_paths[target];assert len(owners)==1;p,y=owners[0];rp=pin(p,'owners/'+p.name)
 rs=[x for x in review['entries'] if (x['proposal_id']=='vm1201-prop-nbrc903-vitamin' and x['component'].get('component_id')==target)]
 if id_=='CHEBI:17439':rs=[next(x for x in review['entries'] if x['component']['component_name']=='Cyanocobalamin')]
 if id_ is None:rs=[next(x for x in review['entries'] if x['proposal_id']=='vm1201-prop-nbrc903-vitamin' and x['component']['component_name']=='Ca-pantothenate')]
 assert len(rs)==1
 if id_:assert rs[0]['catalog_owner_context'][0]['sha256']==rp['sha256']
 facts=[x for x in ontology['rows'] if x['subject']==target]
 reason='The explicit CB named component and independently reviewed primary ontology descriptor support this immediate supplied-input identity; not a claim about procurement, roles, all owner fields, or exact whole-stock equivalence.'
 if id_ is None:reason='CB calcium pantothenate does not select D versus DL. The active CHEBI:31345 structure is D-specific; retain literal name and UNMAPPED with no component_id until actual form evidence or an exact non-D-specific target is established. No name-only match.'
 if id_=='CHEBI:17439':reason='CB explicitly prints Cyanocobalamin, and the exact active CHEBI:17439 owner plus primary descriptor/registry evidence support it. This conclusion does not transfer to nominal JCM/NBRC generic Vitamin B12.'
 if id_=='CHEBI:16494':reason+=' Generic lipoic acid is supported by CHEBI:16494; no R/S/racemate claim or approval of inherited DL-labelled owner fields is made.'
 children.append({'candidate_component_index':ix,'literal_component':component,'planning_disposition':'SUPPORTED_NAMED_INPUT_BINDING_REVIEW_FINAL_BYTES' if id_ else 'PRECISE_FORM_HOLD','recommended_component_id':id_,'recommended_reference_scope':'MIM_CATALOG' if id_ else 'UNMAPPED','active_owner':rp,'active_identity':y['identifier'],'primary_ontology_rows':facts,'primary_database':{'path':ontology['database'],'sha256_as_bound_by_published_extract':ontology['sha256'],'live_database_rehashed':False},'independent_w08_review_entry':rs[0],'reason':reason})
put('ten-child-identity-matrix.json',{'scope':'Planning of component assertions only, based on current bytes and preserved independent primary captures; not a fresh whole-owner scientific release review','supported_named_inputs':9,'precise_form_holds':1,'children':children,'nominal_recipe_extra_limits':['Generic Vitamin B12 remains UNMAPPED; do not select cyanocobalamin CHEBI:17439 or vitamer-class CHEBI:176843 as a distinct supplied substance.','Nominal 1L distilled water is a source-batch input, not evidence of final stock volume. CB source has no quantified solvent; do not add water.','Calcium pantothenate remains unqualified; no D-only target in either source.']})
put('candidate-boundary-checks.json',{'before_sha256':sha(before.read_bytes()),'candidate_sha256':sha(candidate.read_bytes()),'changed_top_fields':sorted(fields),'old_history_count':len(b['curation_history']),'all_history_prefix_preserved':True,'new_history_count':len(a['curation_history']),'nonchanged_fields':sorted(k for k in a if k not in fields),'all_ten_literal_candidate_components_remain_unmapped':all(x['reference_scope']=='UNMAPPED' and 'component_id' not in x for x in a['components']),'candidate_not_modified':True,'no_native_application_or_prototype_run':True,'operator_contract':'Existing edits require a genuine published edit_existing_owner original with the same owner path and authentic before hash. create requires genuine new_owner/null-before. Final payload may be separately composed and reviewed; original ledger/payload bindings stay exact.'})
for r in refs.values():assert sha(Path(r['path']).read_bytes())==r['sha256'],r['path']
put('source-bindings.json',{'started_at':start,'completed_at':datetime.datetime.now(datetime.UTC).isoformat(),'author':'/root/next23_context','scope':'Read-only integration preflight; no source/worker/code application or scientific approval','refs':list(refs.values()),'hash_rechecks_pass':True,'failed_attempts':[{'command':'gh api repos/CultureBotAI/MediaIngredientMech/issues/comments/6719499726','outcome':'Default sandbox connection unavailable; empty stdout artifact retained. Authorized escalated read-only retry succeeded. No approval timeout/rejection.'}]})
print(json.dumps({'workers':{w:x['head'] for w,x in workers.items()},'candidate_sha256':sha(candidate.read_bytes()),'cases':len(case_rows),'children':len(children),'refs':len(refs),'result':'READ_ONLY_BINDINGS_PASS'}))
