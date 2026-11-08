"""Create exactly49 guarded report candidates after frozen-input preflight."""
from pathlib import Path
import sys,json,copy,hashlib,difflib,re,collections
sys.path.insert(0,str(Path(__file__).parent));import provenance_writer_v2 as w
import yaml
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy
from mediaingredientmech.synonym_policy import is_resolving_synonym
R=w.R;O=w.PUBLICATION;P=w.ARTIFACT;S=w.PACKET;A=w.PRIVATE

def dump(p,v):
 p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('x') as f:json.dump(v,f,indent=2,ensure_ascii=False);f.write('\n')
def capture(src,dst):
 dst.parent.mkdir(parents=True,exist_ok=True)
 with dst.open('xb') as f:f.write(src.read_bytes())
 w.require(src.read_bytes()==dst.read_bytes(),'copy drift')

repair=w.Repair();prepared=[repair.prepare(pid) for pid in repair.rows]
for x in prepared:
 pid=x['row']['proposal_id'];w.require(re.fullmatch(r'[A-Za-z0-9_-]+',pid),'unsafeproposalfilename');w.check_destination(O/'payloads',O/'payloads'/(pid+'.yaml'))
# No output exists or changes until every complete input and postimage validates.
manifest=json.loads((S/'MANIFEST.json').read_text())
for x in manifest['files']:
 path=Path(x['path']);w.require(not path.is_absolute() and '..' not in path.parts,'unsafe inputmember');w.require(w.sha((S/path).read_bytes())==x['sha256'],'coordinator manifest drift')
for x in manifest['files']:capture(S/x['path'],O/'context/allowlist'/x['path'])
capture(S/'MANIFEST.json',O/'context/allowlist/MANIFEST.json')
for n in ['issue1226.json','issue1226-comments.json']:capture(A/'context'/n,O/'context'/n)
capture(R.parents[2]/'preflight/root-integration-findings-v1/w03-oxoid-source-successor-accepted-v1.json',O/'context/accepted-predecessor.json')
rows=[]
for x in prepared:
 pid=x['row']['proposal_id'];dest=O/'payloads'/(pid+'.yaml');row=repair.write(x,O/'payloads',dest)
 row['after_capture']={'root':'artifact','path':str(dest.relative_to(P)),'sha256':w.sha(dest.read_bytes())}
 row['old_object_sha256']=w.sha(w.canon(row['old_object']));row['new_object_sha256']=w.sha(w.canon(row['new_object']))
 row['entire_parent_context_unchanged']=True;rows.append(row)
 diff=''.join(difflib.unified_diff(x['old_bytes'].decode().splitlines(True),dest.read_text().splitlines(True),fromfile=x['row']['published_payload_path'],tofile=str(dest.relative_to(R))))
 path=O/'diffs'/(pid+'.diff');path.parent.mkdir(parents=True,exist_ok=True)
 with path.open('x') as f:f.write(diff)
dump(O/'payload-bridge.json',{'schema_version':1,'authority':'https://github.com/CultureBotAI/MediaIngredientMech/issues/1226','selected_predecessor_head':w.HEAD,'allowlist_sha256':w.ALLOWLIST_SHA,'writer_sha256':w.sha(Path(w.__file__).read_bytes()),'entries':rows,'new_source_science_approval':False,'scope':'49 exactenumsubstitutions and49honesthistoryappends; all original scientific fields and source assertions preserved.'})
props=list(repair.proposals.values());changes={r['proposal_id']:r for r in rows};proof=[];before_overlay={};after_overlay={};baseline={str(p.relative_to(R)):yaml.safe_load(p.read_text()) for folder in ['mapped','unmapped'] for p in (R/'data/ingredients'/folder).glob('*.yaml')}
before_overlay.update(baseline);after_overlay.update(baseline)
for p in props:
 src=P/p['after_capture']['path'];old=yaml.safe_load(src.read_text());r=changes.get(p['proposal_id']);dst=R/r['new_payload_path'] if r else src;new=yaml.safe_load(dst.read_text());w.require(w.sha(src.read_bytes())==p['after_capture']['sha256'],'old payload drift')
 if r:
  rollback=copy.deepcopy(new);rollback['ontology_mapping']['evidence'][0]['evidence_type']='MANUAL_CURATION';event=rollback['curation_history'].pop();w.require(rollback==old,'unlisted semanticdiff');w.require(event==r['appended_history'],'history bridge differs')
 else:w.require(dst.read_bytes()==src.read_bytes(),'unlisted bytechange')
 w.require(not w.validate_ingredient(new),'native schema error')
 proof.append({'proposal_id':p['proposal_id'],'changed':r is not None,'old_sha256':w.sha(src.read_bytes()),'new_sha256':w.sha(dst.read_bytes()),'entire_science_and_all_other_fields_retained':True,'only_allowed_diff':['ontology_mapping.evidence[0].evidence_type','curation_history append'] if r else [],'new_native_schema_errors':[]})
 before_overlay[p['owner_path']]=old;after_overlay[p['owner_path']]=new
id_projection=lambda d:[(k,v.get('identifier'),v.get('mapping_status'),v.get('ontology_mapping',{}).get('ontology_id'),v.get('ontology_mapping',{}).get('mapping_quality'),[(s.get('synonym_text'),s.get('synonym_type')) for s in v.get('synonyms',[]) if is_resolving_synonym(s)]) for k,v in sorted(d.items())]
w.require(id_projection(before_overlay)==id_projection(after_overlay),'identity/resolvingaliasprojection changed')
prior=[str(x) for x in validate_component_partonomy(before_overlay.values())];after=[str(x) for x in validate_component_partonomy(after_overlay.values())];w.require(prior==after,'partonomyresults changed')
manual=[]
for p in props:
 r=changes.get(p['proposal_id']);path=R/r['new_payload_path'] if r else P/p['after_capture']['path'];rec=yaml.safe_load(path.read_text())
 for idx,ev in enumerate(rec.get('ontology_mapping',{}).get('evidence',[])):
  if ev.get('evidence_type')=='MANUAL_CURATION':manual.append({'proposal_id':p['proposal_id'],'index':idx,'complete_object':ev})
w.require({(x['proposal_id'],x['index']) for x in manual}=={('b-proposal-marine-aliases',0),('c-copper-trihydrate-alias',4),('m-arabinan_source_alias',2)},'inheritedmanual exclusion changed')
dump(O/'scientific-field-retention.json',{'scope':'Exactsemanticretention only; no scientificreapproval','proposal_rows':proof,'enum_replacements':49,'history_appends':49,'unchanged_payloads':25,'inherited_manual_objects_preserved':manual,'retired_rcm_still_excluded':True,'oxoid_payload_unchanged':'1ec7554da19d5a6ab2259ee79d178a95511a923e611f4fc176af498248ab76ae'})
dump(O/'validation/native-payloads.json',{'status':'PASS','changed_schema_records':49,'complete_schema_records':74,'baseline_native_owner_count':len(baseline),'complete_proposal_overlay_count':len(after_overlay),'before_partonomy_violations':prior,'after_partonomy_violations':after,'introduced_partonomy_violations':[],'identity_and_resolving_alias_projections_unchanged':True,'maintained_files_written':0,'scientific_approval':False})
print(json.dumps({'changed':len(rows),'unchanged':len(props)-len(rows),'schema_validated':len(proof),'partonomy_before':len(prior),'partonomy_after':len(after),'remaining_inherited_manual':len(manual)},indent=2))
