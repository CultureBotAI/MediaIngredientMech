import pathlib,json,hashlib,subprocess,datetime,yaml,collections
S=pathlib.Path('.temp/w05-dependency-route-a-confirmation-v1');R=S/'review';R.mkdir(parents=True,exist_ok=True)
C=pathlib.Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107');B=pathlib.Path('reports/all_unmatched_20261107/worker-05');P=B/'buffer-parts-v1';base='108e213e96f7d423ee345ce265d692e79063127c'
def j(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def oh(o):return hashlib.sha256(json.dumps(o,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
def bind(p):return {'path':str(p),'sha256':sha(p)}
def gitsha(p):return hashlib.sha256(subprocess.check_output(['git','show',base+':'+str(p)])).hexdigest()
assert subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()==base
plans=j(C/'preflight/final-component-dependency-plan-v2/missing-origin-options-12.json');planmap={x['owner_path']:x for x in plans}
core=j(P/'core/proposals.json')['proposals'];byowner=collections.defaultdict(list)
for p in core:byowner[p['owner_path']].append(p)
decisions=j(P/'core/decisions.json')['decisions'];di={d['case_id']:d for d in decisions};ps=j(P/'dependencies-direct-v1/proposals.json')['proposals'];science=j(P/'review/main-review.json');sr={x['proposal_id']:x for x in science['payload_reviews']};child=j(P/'review/dependencies/main-review.json');oldsr={x['proposal_id']:x for x in child['payload_reviews']}
assert len(core)==155 and len(decisions)==188 and len(ps)==15
parent=next(p for p in core if p['proposal_id']=='W05-FINAL-MAT-039');pr=yaml.safe_load((B/parent['after_capture']['path']).read_text());assert pr['identifier']=='mesh:D010461'
causal='KG_CASE:ba039f9e4a33baf69eb111ceb979cf6c9ad8fe788c13488f256338508ce94151'
# Use exact case in immutable route plan (avoids treating a hand-entered ID as evidence).
causal=next(iter(plans[0]['accountable_author_option']['case_hashes']))
assert di[causal]['case_input_sha256']==plans[0]['accountable_author_option']['case_hashes'][causal]
rows=[]
for p in ps:
 owner=p['owner_path'];assert len(byowner[owner])==1 and byowner[owner][0]==p
 assert p['kind']=='edit_existing_owner' and sha(pathlib.Path(owner))==p['before_sha256']
 cap=p['after_capture'];path=B/cap['path'];assert sha(path)==gitsha(path)==cap['sha256'];r=yaml.safe_load(path.read_text());before=yaml.safe_load(pathlib.Path(owner).read_text())
 assert sr[p['proposal_id']]['after_capture']==cap and sr[p['proposal_id']]['selected_proposal_object_sha256']==oh(p)
 dr=p['dependency_reassessment'];idx=int(dr['claim_key'].split('[')[-1].strip(']'));part=r['components'][idx]
 isnew=owner in planmap
 if isnew:
  plan=planmap[owner];assert p['before_sha256']==plan['before_sha256'];assert p['case_ids']==[causal];assert dr['causal_case_is_not_child_recipe_observation'];assert dr['case_input_sha256']==di[causal]['case_input_sha256']
  generic=plan['source_disposition']=='GENERIC_REFERENCE_MIGRATION_CANDIDATE'
 else:generic=False
 if generic:
  assert part['component_id']=='mesh:D010461' and part['reference_scope']=='MIM_CATALOG';assert r['component_assertion']['method']=='LABEL_ENUMERATION' and r['component_assertion']['completeness']=='COMPLETE';assert p['direct_generic_successor']['exact_parent_after_capture']==parent['after_capture'];assert p['direct_generic_successor']['new_part_identifier']=='mesh:D010461'
 else:assert 'component_id' not in part and part['reference_scope']=='UNMAPPED'
 assert r['curation_history'][:len(before.get('curation_history',[]))]==before.get('curation_history',[])
 for k in ['identifier','preferred_term','mapping_status','occurrence_statistics','synonyms']:
  # Existing composite source origins can already carry earlier bounded identity/label edits;
  # exact full-payload reviewed-byte proof above binds them rather than assuming baseline equality.
  if isnew:assert r.get(k)==before.get(k)
 rows.append({'proposal_id':p['proposal_id'],'owner_path':owner,'kind':p['kind'],'before_sha256':p['before_sha256'],'after_capture':cap,'published_git_blob_equal':True,'proposal_object_sha256':oh(p),'case_ids':p['case_ids'],'causal_parent_case_id':dr['causal_parent_case_id'],'causal_parent_case_input_sha256':dr['case_input_sha256'],'causal_parent_is_not_child_recipe_observation':dr['causal_case_is_not_child_recipe_observation'],'requested_route':'twelve_missing_authentic_origins' if isnew else 'existing_composed_origin','plan_disposition':planmap[owner]['source_disposition']if isnew else 'existing_compound_withdrawal_composition','claim_key':dr['claim_key'],'selected_part':part,'assertion_method':r['component_assertion']['method'],'assertion_completeness':r['component_assertion']['completeness'],'current_generic_parent':parent['after_capture']if generic else None,'prior_complete_scientific_review':{'capture':bind(P/'review/main-review.json'),'actual_reviewer':sr[p['proposal_id']]['actual_scientific_reviewer'],'assessment':sr[p['proposal_id']]['assessment'],'scope_note':'Exact final complete YAML and actual reviewed field/source scope; no fresh approval inferred from hashing.'},'original_child_full_review':{'capture':bind(P/'review/dependencies/main-review.json'),'actual_reviewer':child['reviewer'],'after_capture_at_that_review':oldsr[p['proposal_id']]['after_capture'],'unchanged_to_that_child_review':oldsr[p['proposal_id']]['after_capture']==cap},'full_parsed_payload_field_names':list(r),'history_prefix_preserved':True,'source_owner_export_approval':False})
assert sum(x['requested_route']=='twelve_missing_authentic_origins'for x in rows)==12
assert sum(x['current_generic_parent'] is not None for x in rows)==5
assert sum(x['requested_route']=='twelve_missing_authentic_origins'and x['current_generic_parent']is None for x in rows)==7
out={'reviewer':'/root/final_skeptical','at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'base_head':base,'scope':'Exact route-A authentic-origin/published-full-payload/causal-case bridge, with source-science reuse explicitly attributed. Current targeted scientific reassessment follows separately.','inputs':[bind(C/f'preflight/final-component-dependency-plan-v{v}/{n}')for v,n in [(1,'PLAN.md'),(1,'HANDOFF.json'),(1,'MANIFEST.json'),(2,'ROUTES.md'),(2,'HANDOFF.json'),(2,'MANIFEST.json'),(2,'missing-origin-options-12.json')]]+[bind(P/f'core/{n}.json')for n in ['decisions','proposals','evidence']], 'counts':{'current_cases':188,'current_proposals':155,'route_A_missing_origins_already_present':12,'generic_conditional':5,'ambiguous_reviewed_withdrawals':7,'existing_composed_origins':3,'all15_unique_actual_owner_paths':15,'new_proposals_required_by_this_origin_check':0},'payload_checks':rows,'generic_parent':{'proposal_id':parent['proposal_id'],'after_capture':parent['after_capture'],'selected_identity':pr['identifier'],'prior_plan_identity':'kgmicrobe.ingredient:peptone','assessment':'The prior plan explicitly made the five references conditional on the final reviewed generic identity. The later directly mapped MeSH Peptones parent and five exact dependent successors replace the earlier local destination, preserving its history; this is not unreviewed global replacement.'},'limits':['Complete payload preservation and exact before/after/case binding are not whole-owner, source-assay, role or export approval.','The broader twenty-claim scope includes three other-worker generic consumers and two negative controls; this15payload origin bridge does not approve or apply them.','No maintained change, new source case, duplicate owner or new child origin authored.']}
p=R/'origin-and-byte-bridge-v1.json';assert not p.exists();p.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n');print(json.dumps(bind(p)))
