from pathlib import Path
from datetime import datetime, timezone
import hashlib, importlib.util, json, subprocess, sys
import yaml
from mediaingredientmech.validation.write_validated import validate_ingredient

W=Path.cwd(); R=W/'.temp/w05-buffer-parts-v1/review'
B=W/'reports/all_unmatched_20261107/worker-05'
S=W/'.temp/w05-buffer-parts-v1'; T=S/'inputs/buffer-source-parts-triage-v1'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def osh(d): return hashlib.sha256(json.dumps(d,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
def bind(p): return {'path':str(p.relative_to(W)) if p.is_relative_to(W) else str(p),'sha256':sha(p)}
builder=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/kgm-unmapped-20261107/claw/scripts/build_mim_ingredient_sssom.py')
assert sha(builder)==sha(B/'final-correction-v1/inputs/pinned-native-row-builder.py')
spec=importlib.util.spec_from_file_location('buffer_review_native',builder)
m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m)
props=json.loads((B/'tellurium-polypeptone-v1/core/proposals.json').read_text())['proposals']
ids=['CHEM-C1193-HEPES-1221','CHEM-C1193-HEPES-1474','CHEM-C1193-DSMZ_394_1137-Tris','CHEM-C1193-JCM_1061-Tris']
reviews=[]
for pid in ids:
 p=next(p for p in props if p['proposal_id']==pid)
 after=B/p['after_capture']['path']; old=B/'correction-1193-v1/chemicals/proposed'/after.name
 assert sha(after)==p['after_capture']['sha256']
 a=yaml.safe_load(after.read_text());b=yaml.safe_load(old.read_text())
 assert 'components' not in a and 'component_assertion' not in a
 assert len(b['components'])==2 and b['component_assertion']['method']=='RECIPE_TRANSCRIPTION'
 assert a['curation_history'][:-1]==b['curation_history']
 assert a['ontology_mapping']['evidence'][0]['evidence_type']=='LLM_SUGGESTION'
 unchanged_keys=[k for k in a if a[k]==b.get(k)]
 changes={k:{'before':b.get(k),'after':a.get(k)} for k in set(a)|set(b) if a.get(k)!=b.get(k)}
 assert set(changes)=={'components','component_assertion','notes','ontology_mapping','curation_history'}
 errors=[str(e) for e in validate_ingredient(a)];assert not errors
 rows=m._row_from_yaml(after,{},{},{},{},record=a,owners={})
 oldrows=m._row_from_yaml(old,{},{},{},{},record=b,owners={})
 assert len(rows)==len(oldrows)==1
 assert rows[0]['predicate_id']=='skos:exactMatch' and rows[0]['object_id']==a['identifier']
 for rev in ['5156d92bec6bd885ca8bae3c5e18bfdce0069176','0bac12cabfd1f67f212631d8eef9aa46379f6b41']:
  raw=subprocess.check_output(['git','show',rev+':'+str(after.relative_to(W))]); assert hashlib.sha256(raw).hexdigest()==sha(after)
 reviews.append({'proposal_id':pid,'selected_proposal_object_sha256':osh(p),'old_capture':bind(old),'after_capture':p['after_capture'],'selected_yaml':bind(after),'strict_errors':errors,'old_material_components':b['components'],'old_component_assertion':b['component_assertion'],'historical_to_selected_changes':changes,'unchanged_fields':unchanged_keys,'current_native_rows':rows,'original_native_rows':oldrows,'all_prior_history_preserved':True,'present_at_first_publication_5156_and_base_0bac':True,'payload_change_in_this_supplement':False})
read_paths=[Path(x) for x in ['MAPPING_SEMANTICS.md','.claude/skills/review-yaml-record/SKILL.md','.claude/skills/add-media/SKILL.md','docs/record-reviews.md','docs/record-review-profile.md','docs/stock_components.md','src/mediaingredientmech/schema/mediaingredientmech.yaml']]
inputs=[bind(W/p) for p in read_paths]+[bind(T/n) for n in ['ASSESSMENT.json','primary-capture-index.json','new-hepes-components-finding-v1.json','new-tris-components-finding-v1.json','nbrc1221.txt','nbrc1474.txt','dsm394.txt','dsm1137.txt','jcm1061.txt','dsm394.pdf','dsm1137.pdf']]
comment=json.loads((S/'issues/comment6718873227.json').read_text())
out={'reviewer':'/root/final_skeptical','at':datetime.now(timezone.utc).isoformat(),'base':'0bac12cabfd1f67f212631d8eef9aa46379f6b41','inputs':inputs,'builder':bind(builder),'payload_checks':reviews,'chronology':{'prior_selected_history_timestamp':reviews[0]['historical_to_selected_changes']['curation_history']['after'][-1]['timestamp'],'triage_at':json.loads((T/'ASSESSMENT.json').read_text())['at'],'github_comment_created_at':comment['created_at'],'first_publication_commit':'5156d92bec6bd885ca8bae3c5e18bfdce0069176','first_publication_commit_author_and_committer_time':subprocess.check_output(['git','show','-s','--format=%aI%n%cI','5156d92bec6bd885ca8bae3c5e18bfdce0069176'],text=True).splitlines(),'conclusion':'The preserved private correction history precedes the triage and current GitHub filing. The filing precedes first Git publication. Original before-fix reports carry no independently verified report time; no precise before-fix disclosure time or retroactive filing-first claim is inferred.'},'limitations':['Native rows are exact producer projections with empty owner/suppression indexes, not maintained export release or coordinator family-owner selection.','Historical-to-selected changes occurred in the prior final-correction packet; this supplement does not reauthor or reapply them.','Full campaign accounting/overlay validation and saved native review are root-owned and are not claimed by these four-record checks.']}
o=R/'independent-payload-checks-v1.json';assert not o.exists();o.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n');print(o,sha(o));print('PASS',len(reviews),'complete payloads')
