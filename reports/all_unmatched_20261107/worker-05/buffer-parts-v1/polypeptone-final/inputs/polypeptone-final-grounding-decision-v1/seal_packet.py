from pathlib import Path
import datetime,hashlib,json,subprocess
import yaml
D=Path(__file__).parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def save(n,x):
 p=D/n;assert not p.exists();p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
b=json.loads((D/'source-bindings.json').read_text());old=yaml.safe_load((D/'snapshot/authentic-before-Polypeptone.yaml').read_text());w5=yaml.safe_load((D/'snapshot/w05-Polypeptone.yaml').read_text());w6=yaml.safe_load((D/'snapshot/w06-Polypeptone.yaml').read_text())
checks={
 'all_52_external_input_hashes_unchanged':all(sha(Path(i['path']))==i['sha256'] for i in b['inputs']),
 'w05_original_history_prefix':w5['curation_history'][:len(old['curation_history'])]==old['curation_history'],
 'w06_original_history_prefix':w6['curation_history'][:len(old['curation_history'])]==old['curation_history'],
 'all_original_raw_synonym_texts_retained': [x['synonym_text'] for x in old['synonyms']]==[x['synonym_text'] for x in w5['synonyms']]==[x['synonym_text'] for x in w6['synonyms']],
 'current_local_source_equals_frozen':json.loads((D/'quantity-current-source-comparison.json').read_text())['matches_frozen'],
 'foodon_material_ancestry':{'material entity','food material','food material (to be processed)'}=={x['label'] for x in json.loads((D/'fresh-primary/foodon-ancestors.json').read_text())['_embedded']['terms']},
 'all_quantity_comments_captured':all(len(json.loads((D/f'cm-issue{n}-comments.json').read_text()))==json.loads((D/f'cm-issue{n}-body.json').read_text())['comments'] for n in [118,150,408]),
 'no_mentions_in_drafts':all('@' not in (D/f).read_text() for f in ['issue1202-addendum-draft.md','quantity-note.md']),
}
for n,h in b['heads'].items():
 root=Path(__file__).parents[3]/'workers'/n/'worktree' if False else Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107')/'workers'/n/'worktree'
 checks[n+'_local_head_unchanged']=subprocess.check_output(['git','-C',str(root),'rev-parse','HEAD']).decode().strip()==h
assert all(checks.values()),checks
save('integrity-checks.json',{'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS','checks':checks,'limitations':'Input/content checks only; no native candidate, science approval, CI or release claim.'})
texts=[x['synonym_text'] for x in w5['synonyms'] if x['synonym_type']=='CATALOG_VARIANT']
save('decision.json',{
 'schema_version':1,'author':'/root/next23_context','kind':'proposed_scientific_decision_preflight','issue':'https://github.com/CultureBotAI/MediaIngredientMech/issues/1202','status':'RECOMMEND_GENERIC_LOCAL_PLUS_SUPPORTED_BROADER_MATERIAL','final_candidate_authored':False,'independent_final_owner_approval':False,
 'recommended_scope':'Named Polypeptone preparation with supplier/product version unspecified; not a union claiming all peptone brands are identical.',
 'identifier':'kgmicrobe.ingredient:polypeptone','ontology_mapping':{'ontology_id':'FOODON:03315306','ontology_label':'protein hydrolyzates','mapping_quality':'NARROW_MATCH','expected_predicate':'skos:broadMatch','expected_own_registry_identity_row':True,'output_generated':False},
 'supports_now':['Primary peptone/protein-hydrolysate material relation','FoodOn material ancestry, not a flavouring-role edge','Local distinct named preparation instead of parent-as-identity','No need for unknown supplier, lot or peptide formula to assert broader material relation'],
 'not_supported':['MICRO:0000179 exact identity for bare MediaDive442 or all original owner routes','MICRO:0000178 as unrestricted generic peptone term','BD equal-parts components on generic owner','Automatic product-specific synonym resolution to generic owner','Role or release approval'],
 'remaining_coupling':{'bd_specific_aliases':texts,'recommendation':'Preserve text/source as provenance-only with specific-versus-generic claim rationale, or retain these exact token claims withheld pending source-qualified representation. Notes alone do not change resolver behavior.','retain_five_existing_rejected_labels':[x['synonym_text'] for x in w5['synonyms'] if x['synonym_type']=='REJECTED_LABEL'],'retain_cases':b['selected_proposals']['w05']['case_ids']+b['selected_proposals']['w06']['case_ids'],'retain_both_author_histories':True,'retain_mapping_source_withhold_and_roles':True},
 'alternatives':[{'id':'BD_exact_scope','id_candidate':'MICRO:0000179','science':'Supported for the explicitly BD equal-parts blended product; not selected for the current mixed-source generic owner. Requires authentic bounded continuity and source applicability, not lot-level formula research.'},{'id':'self_only_registry','science':'Current fragment is incomplete under semantics§3; do not keep self-only grounding as final while the broader material relation is supported.'}],
 'quantity_gap':{'original_finding':'W05-POLY-SOURCE-001','deduplicated_tracking':['https://github.com/CultureBotAI/CultureMech/issues/150','https://github.com/CultureBotAI/CultureMech/issues/408'],'separate_from_parent_relation':True,'current_local_recipe_matches_frozen':True,'remote_main_not_checked':True,'quantity_corrected':False},
 'source_bindings_sha256':sha(D/'source-bindings.json'),'assessment_sha256':sha(D/'ASSESSMENT.md'),'issue_draft_sha256':sha(D/'issue1202-addendum-draft.md')})
save('HANDOFF.json',{'schema_version':1,'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'author':'/root/next23_context','status':'SEALED_PROPOSED_DECISION_FOR_ROOT_AND_DISTINCT_REVIEWER','head_bindings':b['heads'],'inputs':len(b['inputs']),'recommendation':'Generic local Polypeptone identity plus FOODON03315306 broader material; no forced BD identity; finish three BD alias claims before whole-owner acceptance.','changed_source_payloads':0,'native_tests_run':False,'primary_fresh_requests':4,'source_gap_route':'Existing open CultureMech150/408; exact new M122 instance, no source edit.','artifacts':{f:sha(D/f) for f in ['ASSESSMENT.md','decision.json','issue1202-addendum-draft.md','quantity-note.md','source-bindings.json','integrity-checks.json']},'limits':['Decision authoring, not independent final combined-owner approval','No source-case membership, owner merge, scientific role or release admission','All final exact candidate bytes still need the already-required distinct review','Quantity current-local identity verified; no assertion about remote CultureMech main']})
files=[p for p in sorted(D.rglob('*')) if p.is_file() and p.name!='MANIFEST.json'];save('MANIFEST.json',{'schema_version':1,'members':[{'path':str(p.relative_to(D)),'sha256':sha(p),'bytes':p.stat().st_size} for p in files]});m=json.loads((D/'MANIFEST.json').read_text());assert all(sha(D/x['path'])==x['sha256'] for x in m['members'])
print(json.dumps({'members':len(files),'handoff_sha256':sha(D/'HANDOFF.json'),'manifest_sha256':sha(D/'MANIFEST.json'),'decision_sha256':sha(D/'decision.json'),'issue_draft_sha256':sha(D/'issue1202-addendum-draft.md'),'quantity_note_sha256':sha(D/'quantity-note.md')},indent=2))
