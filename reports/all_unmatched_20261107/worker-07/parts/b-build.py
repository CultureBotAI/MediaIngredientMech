"""2026-11-08 primary_b: materialize manually authored source assessments/proposals.
No scientific decisions are inferred by this helper. Read inputs are frozen recipes,
manually authored assessments, verified network captures and baseline owner bytes.
Writes only assigned worker artifacts; all approvals/holds remain unchanged.
"""
import json,pathlib,hashlib,datetime,copy,re,sys
import yaml
ROOT=pathlib.Path(__file__).resolve().parents[1]
REPO=ROOT.parents[2]
QUEUE=pathlib.Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
CASES=json.loads((ROOT/'parts/b-input.json').read_text())['cases']
ASSESS=json.loads((ROOT/'parts/b-assessments.json').read_text())
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def cap(path,root='artifact'):
 p=(ROOT if root=='artifact' else QUEUE)/path
 return {'root':root,'path':path,'sha256':sha(p)}
E=[];D=[];P=[]
def ev(eid,kind,path,locator,support,url=None,at=None,cids=None,root='artifact'):
 x={'evidence_id':eid,'kind':kind,'capture':cap(path,root),'locator':locator,'supports_or_contradicts':support,'url':url}
 if url:x['accessed_at']=at
 if cids:x['case_ids']=cids
 E.append(x);return eid
retrievals=[]
for fn in ['b-retrievals.json','b-extra-retrievals.json','b-curl-retrievals.json']:
 path=ROOT/'parts'/fn
 if path.exists():retrievals+=json.loads(path.read_text())
primary_by_case={c['case_id']:[] for c in CASES}
primary_by_url={}
seen=set()
for r in retrievals:
 if not r['success'] or r.get('path') in seen:continue
 seen.add(r['path'])
 eid='B-PRIMARY-'+hashlib.sha256(r['path'].encode()).hexdigest()[:14]
 kind='ontology' if '/ols4/' in r['url'] else 'primary_source'
 body=(ROOT/r['path']).read_text(errors='replace') if not r['path'].endswith('.pdf') else ''
 failure=('Nothing found.' in body or '"WrongCall"' in body)
 if failure:kind='unsuccessful_search'
 ev(eid,kind,r['path'],'Exact captured response for '+r['url'],('Response is an application error: WrongCall unsupported API endpoint or JCM Nothing found. HTTP transport success is not recipe/identity evidence.' if failure else 'Source-specific ingredient text, formulation or identity fields; applicability is bounded by each case assessment.'),r['url'],r['accessed_at'],r.get('case_ids'))
 for cid in r.get('case_ids',[]):primary_by_case[cid].append(eid)
 primary_by_url[r['url']]=eid
ontology={}
for r in json.loads((ROOT/'parts/b-ontology-retrievals.json').read_text()):
 if not r['success']:continue
 eid='B-ONTOLOGY-'+r['identifier'];ontology[r['identifier']]=eid
 ev(eid,'ontology',r['path'],'_embedded.terms[obo_id='+r['identifier']+']: label, description, synonym and annotation fields','Identity/form reference only; does not approve source assignment or owner publication.',r['url'],r['accessed_at'])
for url,eid in primary_by_url.items():
 if '/ols4/' in url and 'obo_id=' in url:ontology[url.split('obo_id=')[1]]=eid
owner_cache={}
def owner(name):
 if name is None:return None
 path=(REPO/'data/ingredients/mapped'/f'{name}.yaml').resolve()
 rel=path.relative_to(REPO).as_posix()
 if not path.exists():raise ValueError(rel)
 if rel not in owner_cache:
  raw=path.read_bytes();dst='captures/b-owner-'+path.name;(ROOT/dst).write_bytes(raw)
  eid='B-OWNER-'+path.stem
  ev(eid,'source_snapshot',dst,'Complete original baseline owner bytes at '+rel,'Existing owner scope, aliases, history and inherited caveats; no whole-record approval.')
  owner_cache[rel]=(yaml.safe_load(raw),eid)
 return {'path':rel,'sha256':sha(path)}
for index,c in enumerate(CASES,70):
 disp,oname,oids,reason,missing=ASSESS[str(index)]
 cid=c['case_id'];eid=ev(f'B-SOURCE-{index}','source_snapshot','parts/b-input.json',f'cases[{index-70}] exact complete original case','Binds raw source label, every occurrence, context and IDs for this exact case.',cids=[cid])
 refs=[eid]
 for j,o in enumerate(c['occurrences']):
  refs.append(ev(f'B-RECIPE-{index}-{j}','source_snapshot',o['full_recipe_snapshot'],o['component_path']+' plus complete recipe context','Frozen recipe including preparation, nested solutions, references, evidence and source identifiers for this occurrence.',cids=[cid],root='source'))
 refs+=primary_by_case[cid]
 refs += [ontology[x] for x in oids if x in ontology]
 ow=owner(oname)
 if ow:refs.append(owner_cache[ow['path']][1])
 issues=[]
 if index in [71,105]:issues.append('https://github.com/CultureBotAI/MediaIngredientMech/issues/1157')
 if index in [88,97,113]:issues.append('https://github.com/CultureBotAI/MediaIngredientMech/issues/905')
 if index==83:issues.append('https://github.com/CultureBotAI/MediaIngredientMech/issues/1169')
 if index in [86,124]:issues.append('https://github.com/CultureBotAI/CultureMech/issues/672')
 d={'case_id':cid,'case_input_sha256':hashlib.sha256(json.dumps(c,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest(),'source':{k:c[k] for k in ['source','source_case_id','source_label','raw_source_label']},'occurrence_ids':[o['occurrence_id'] for o in c['occurrences']],'disposition':disp,'reasoning':reason,'applicability':f"Applies only to raw label {c['source_label']!r}, all {len(c['occurrences'])} frozen occurrences and their complete captured recipe contexts. IDs and quantities are retained, not recalculated. "+reason,'evidence_ids':list(dict.fromkeys(refs)),'proposal_ids':[],'no_change_reason':missing or 'No maintained record is changed by this source review; any source alias proposal remains subject to final independent review.','missing_requirement':missing,'owner_records':[ow] if ow else [],'issue_refs':issues,'independent_review':{'status':'pending','evidence_ids':[]},'native_review_scope':'Source-only mapping assessment; identified owner assessment is limited to supplied identity and proposed delta. Root native formal owner review is separate; no whole-record/role approval.'}
 D.append(d)
def decision(i):return D[i-70]
def proposal(indices,oname,after,description,kind='edit_existing_owner',notes=None):
 owner_path='data/ingredients/mapped/'+oname+'.yaml';pid='B-PROPOSAL-'+oname
 before=None
 if kind=='edit_existing_owner':before=sha(REPO/owner_path)
 dst='proposed_owners/b-'+oname+'.yaml';(ROOT/dst).write_text(yaml.safe_dump(after,sort_keys=False,allow_unicode=True,width=100))
 refs=list(dict.fromkeys(e for i in indices for e in decision(i)['evidence_ids']))
 P.append({'proposal_id':pid,'case_ids':[decision(i)['case_id'] for i in indices],'description':description,'evidence_ids':refs,'owner_path':owner_path,'kind':kind,'before_sha256':before,'after_capture':cap(dst),'identity_predicate_consequences':'Preserve distinct form; own-identifier exactMatch. Existing parent mappings retain their direction. New registry-only preparation has no asserted chemical equivalence.','publication_review_obligation':'Coordinator must apply via guarded writers, withdraw inherited support for every changed owner byte, synchronize native exports, re-review full published payload and preserve all WITHHOLD/REJECTED gates. This proposal is not applied or approved for release.','cross_shard_conflict':'Coordinator must reconcile all proposals touching this owner from original baseline hashes, especially Calcium_Pantothenate/Cyanocobalamin/Na3-citrate_X_2_H2o and cysteine families. Never adopt another proposed after payload as before.' if kind=='edit_existing_owner' else 'Source-qualified formulation; compare other workers and existing generic owners before minting to avoid duplicate identity.','limitations':notes})
 for i in indices:
  decision(i)['proposal_ids'].append(pid);decision(i)['no_change_reason']=None
def history(after,action,changes):
 after.setdefault('curation_history',[]).append({'timestamp':NOW,'curator':'all-unmatched-20261107-worker07-primary_b','action':action,'changes':changes,'previous_status':after.get('mapping_status','MAPPED'),'new_status':after.get('mapping_status','MAPPED'),'llm_assisted':True})
alias_indices=[70,73,75,76,78,80,81,83,86,87,92,96,99,101,105,108,109,111,127,128,129,139]
groups={}
for i in alias_indices:groups.setdefault(ASSESS[str(i)][1],[]).append(i)
for name,indices in groups.items():
 original=owner_cache['data/ingredients/mapped/'+name+'.yaml'][0];after=copy.deepcopy(original);changes=[]
 for i in indices:
  label=CASES[i-70]['source_label']
  if label not in [s['synonym_text'] for s in after.get('synonyms',[])]:
   after.setdefault('synonyms',[]).append({'synonym_text':label,'synonym_type':'RAW_TEXT','source':'all-unmatched-20261107 worker07: '+decision(i)['case_id']});changes.append('Add source-verified same-substance alias '+repr(label))
 if name=='Sodium_Dithionite':
  target=json.loads((ROOT/'captures/b-ontology-CHEBI-61278.json').read_text())['_embedded']['terms'][0]
  bad=set(s.casefold() for s in target.get('synonyms',[])+[target['label']])
  for syn in after.get('synonyms',[]):
   if syn['synonym_text'].casefold() in bad and syn.get('synonym_type')!='REJECTED_LABEL':syn['synonym_type']='REJECTED_LABEL';changes.append('Reject unrelated scutellarin label '+repr(syn['synonym_text']))
  changes.append('Bounded correction follows issue1169; no full-row release approval')
 if changes:
  history(after,'SOURCE_REVIEW_PROPOSED_CORRECTION','; '.join(changes))
  proposal(indices,name,after,'; '.join(changes))
 else:
  for i in indices:decision(i)['no_change_reason']='Exact source label already present on the baseline owner; no alias edit needed. Existing release holds remain unchanged.'
# Explicit racemic aliases cannot remain on a stereospecific disodium(S)-malate owner.
name='Sodium_Malate';original=owner_cache['data/ingredients/mapped/'+name+'.yaml'][0];after=copy.deepcopy(original);changed=[]
for syn in after.get('synonyms',[]):
 if syn['synonym_text'] in ['DL-Na-malate','Na-DL-malate','Na2-DL-malate','Sodium DL-malate','DL-Sodium malate'] and syn.get('synonym_type')!='REJECTED_LABEL':
  syn['synonym_type']='REJECTED_LABEL';changed.append(syn['synonym_text'])
if changed:
 history(after,'REJECTED_WRONG_STEREOCHEMISTRY_ALIASES','Reject explicit DL racemate synonyms from CHEBI:91261 disodium (S)-malate: '+', '.join(changed)+'. Source cases remain unresolved for sodium stoichiometry; no reassignment to CHEBI:91260 is implied.')
 proposal([115,130],name,after,'Reject five DL/racemate aliases from S-specific malate owner; preserve source stoichiometry uncertainty.')
exec(compile((ROOT/'parts/b-supplement.py').read_text(),str(ROOT/'parts/b-supplement.py'),'exec'))
def write():
 (ROOT/'parts/b-decisions.json').write_text(json.dumps({'schema_version':1,'worker_slot':7,'phase':'shard','shard_sha256':sha(QUEUE/'shards/shard-07.json'),'decisions':D},indent=2,ensure_ascii=False)+'\n')
 (ROOT/'parts/b-evidence.json').write_text(json.dumps({'schema_version':1,'evidence':E},indent=2,ensure_ascii=False)+'\n')
 (ROOT/'parts/b-proposals.json').write_text(json.dumps({'schema_version':1,'proposals':P},indent=2,ensure_ascii=False)+'\n')
write()
print('case decisions',len(D),'evidence',len(E),'proposals',len(P))
