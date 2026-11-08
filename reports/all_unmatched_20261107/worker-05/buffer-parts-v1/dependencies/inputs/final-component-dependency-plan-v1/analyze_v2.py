from pathlib import Path
import subprocess,json,hashlib,datetime,sys,collections,yaml
R=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech');C=R/'.temp/all-unmatched-20261107';O=Path(__file__).resolve().parent;D=C/'integration/final-application-accounting-v1';M=D/'materialized-v4';S=C/'integration/final-same-target-reconciliation-v2';A=C/'integration/family-reconciliations-v1'
sha=lambda b:hashlib.sha256(b).hexdigest();pins={}
def load(p):
 b=p.read_bytes();pins[str(p)]=sha(b);return json.loads(b)
def record(p):
 b=p.read_bytes();pins[str(p)]=sha(b);return yaml.safe_load(b)
def save(n,x):
 with(O/n).open('x')as f:json.dump(x,f,indent=2,ensure_ascii=False);f.write('\n')
conf=load(D/'observer-config-v4.json');workers={x['worker_slot']:x for x in conf['workers']};base=Path(conf['baseline_owner_root']);inv=load(M/'before-owner-inventory.json')['owners'];baseline={}
for name,h in inv.items():
 p=base/name;assert sha(p.read_bytes())==h;baseline[name]=record(p)
assert len(baseline)==2956
origins=load(M/'origins.json');rels=load(D/'relations-v2/proposed-component-consumers.json');shared=load(D/'relations-v2/shared-identifier-targets.json');oldcouple=load(C/'preflight/final-intake-candidate-v1/identifier-component-dependencies-v1.json');oldscience=load(C/'workers/w03/worktree/.temp/complete-identifier-dependencies-v1/science-b/consumer-ledger.json')
proposed={};trans=[];binding=[]
for origin in origins:
 w=workers[origin['worker_slot']];p=origin['proposal'];path=w['artifact_prefix']+'/'+p['after_capture']['path'];b=subprocess.check_output(['git','-C',w['worktree'],'show',origin['published_head']+':'+path]);h=sha(b);assert h==origin['payload_sha256']==p['after_capture']['sha256'];r=yaml.safe_load(b);key=origin['origin_id'];proposed[key]={'record':r,'origin':origin,'path':p['owner_path'],'payload_sha256':h};binding.append({'origin_id':key,'head':origin['published_head'],'git_path':path,'payload_sha256':h})
 before=origin['before_preflight'].get('before_path');br=baseline.get(before)if before else None
 if br and(br.get('identifier')!=r.get('identifier')or br.get('mapping_status')!=r.get('mapping_status')):
  trans.append({'source':'published_origin','origin_id':key,'before_path':before,'before_sha256':inv[before],'declared_owner_path':p['owner_path'],'after_payload_sha256':h,'before_identifier':br.get('identifier'),'after_identifier':r.get('identifier'),'before_status':br.get('mapping_status'),'after_status':r.get('mapping_status'),'application_approved':False})
# Reproduce all435 exact MIM_CATALOG references; no proposed winner selected.
claims=[]
for key,item in proposed.items():
 for i,c in enumerate(item['record'].get('components')or[]):
  if c.get('reference_scope')=='MIM_CATALOG':claims.append({'origin':key,'index':i,'component':c,'payload_sha256':item['payload_sha256']})
assert len(claims)==len(rels)==435
refmap={(x['consumer_origin_id'],x['selector']):x for x in rels}
for x in claims:
 y=refmap[x['origin'],f'components[{x["index"]}]'];assert x['component']==y['full_component_object']and x['payload_sha256']==y['consumer_payload_sha256']
# Exact37 supplemental candidates are alternatives, not accepted replacements.
cs=load(S/'publication-v4/candidate-summary-v4.json');combined=[]
for g in cs['groups']:
 p=S/g['candidate']['path'];assert sha(p.read_bytes())==g['candidate']['sha256'];r=record(p);bp=g['source_before_path'];br=baseline.get(bp)if bp else None
 entry={'candidate_id':g['candidate_id'],'source_path':str(p),'owner_path':g['owner_path'],'source_before_path':bp,'candidate_sha256':sha(p.read_bytes()),'record':r,'operation':g['operation'],'status':g['status'],'dependency_notes':g.get('dependencies'),'scientific_approval':False};combined.append(entry)
 if br and(br.get('identifier')!=r.get('identifier')or br.get('mapping_status')!=r.get('mapping_status')):
  trans.append({'source':'combined_candidate_alternative','origin_id':g['candidate_id'],'before_path':bp,'before_sha256':inv[bp],'declared_owner_path':g['owner_path'],'after_payload_sha256':entry['candidate_sha256'],'before_identifier':br.get('identifier'),'after_identifier':r.get('identifier'),'before_status':br.get('mapping_status'),'after_status':r.get('mapping_status'),'application_approved':False})
family=[]
fh=load(A/'HANDOFF.json')
# Declared v1 family records; new v2 will be supplied separately when sealed.
for p in sorted((A/'candidates').glob('*.yaml'))+sorted((A/'blocked-prototypes').glob('*.yaml')):
 r=record(p)
 if 'vitamin' in p.name.lower():continue
 family.append({'path':str(p),'sha256':sha(p.read_bytes()),'record':r,'application_approved':False})
ids=collections.defaultdict(list)
for path,r in baseline.items():
 if r.get('mapping_status')!='REJECTED' and r.get('identifier'):ids[r['identifier']].append(path)
transby=collections.defaultdict(list)
for t in trans:
 if t['before_identifier']!=t['after_identifier']or t['after_status']=='REJECTED':transby[t['before_identifier']].append(t)
proposedids=collections.defaultdict(list)
for k,v in proposed.items():
 if v['record'].get('mapping_status')!='REJECTED':proposedids[v['record'].get('identifier')].append(k)
for x in claims:
 cid=x['component']['component_id'];bowners=ids[cid];impacts=transby[cid];x.update({'consumer_owner_path':proposed[x['origin']]['path'],'baseline_target_paths':bowners,'conditional_owner_transitions':impacts,'proposed_target_origins':proposedids[cid]})
 if impacts:x['classification']='REFERENCE_SCOPE_CHANGES_CONDITIONALLY'
 elif not bowners:x['classification']='REQUIRES_NEW_TARGET_OWNER_BINDING'
 elif len(bowners)>1:x['classification']='BASELINE_SHARED_IDENTIFIER_NO_OWNER_WINNER'
 else:x['classification']='NO_IDENTIFIER_TRANSITION_IMPACT_DETECTED'
 x['scientific_scope_approval']=False
# Every baseline inbound reference to any transitioning identifier.
inbound=[]
for path,r in baseline.items():
 for i,c in enumerate(r.get('components')or[]):
  if c.get('reference_scope')=='MIM_CATALOG'and c.get('component_id')in transby:
   inbound.append({'consumer_path':path,'consumer_sha256':inv[path],'selector':f'components[{i}]','component':c,'assertion':r.get('component_assertion'),'conditional_owner_transitions':transby[c['component_id']]})
# Summarize the supplemental candidate references and exact effects on historical consumers.
supp=[]
for entry in combined+family:
 r=entry['record']
 for i,c in enumerate(r.get('components')or[]):
  if c.get('reference_scope')=='MIM_CATALOG':supp.append({'candidate':entry['candidate_id'] if 'candidate_id' in entry else Path(entry['path']).name,'payload_sha256':entry.get('candidate_sha256',entry.get('sha256')),'owner_path':entry.get('owner_path'),'selector':f'components[{i}]','component':c,'baseline_target_paths':ids[c['component_id']],'conditional_owner_transitions':transby[c['component_id']],'scientific_approval':False})
summary={'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'observer_cutoff':conf['observed_at'],'baseline_owners':len(baseline),'published_origins':len(proposed),'published_MIM_CATALOG_claims':len(claims),'shared_identifier_groups':len(shared),'source_transition_rows':len([x for x in trans if x['source']=='published_origin']),'combined_transition_rows':len([x for x in trans if x['source']=='combined_candidate_alternative']),'affected_baseline_claims':len(inbound),'claim_classifications':dict(collections.Counter(x['classification']for x in claims)),'combined_candidates':len(combined),'v1_family_candidates':len(family),'supplemental_MIM_CATALOG_claims':len(supp),'no_global_overlay_or_owner_choice':True}
save('summary-v1.json',summary);save('source-bindings.json',binding);save('current-transitions.json',trans);save('all-435-proposed-claims.json',claims);save('affected-baseline-claims.json',inbound);save('supplemental-claims.json',supp);save('combined-candidate-bindings.json',[{k:v for k,v in x.items()if k!='record'}for x in combined]);save('family-v1-bindings.json',[{k:v for k,v in x.items()if k!='record'}for x in family]);save('input-pins.json',pins)
print(json.dumps(summary,indent=2));print('AFFECTED OLD IDS',list(transby.keys()&{x['component']['component_id']for x in inbound+claims}));print('NEW TARGETS',[(x['origin'],x['index'],x['component']['component_id'])for x in claims if x['classification']=='REQUIRES_NEW_TARGET_OWNER_BINDING'])
