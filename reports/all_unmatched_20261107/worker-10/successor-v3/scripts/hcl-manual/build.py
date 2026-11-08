from pathlib import Path
import json,hashlib,datetime,copy,shutil,subprocess,itertools,sys
import yaml
sys.path.insert(0,str(Path.cwd()/'src'))
from mediaingredientmech.validation.write_validated import write_validated_ingredient
from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.validation.component_partonomy import load_ingredient_records,validate_component_partonomy
R=Path.cwd();C=R.parents[2];A=R/'reports/all_unmatched_20261107/worker-10';O=A/'successor-v3/hcl-manual';P=R/'.temp/all-unmatched-worker-10/successor-v3/hcl-manual';W=C/'workers/w05/worktree/.temp/final-preparation-comparison-v1';T=C/'preflight/family-findings-triage-v1';I=C/'preflight/final-intake-candidate-v1';Q=C/'queue/preliminary-v5'
for d in ['inputs','captures','proposed','validation']: (O/d).mkdir(exist_ok=True)
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def sh(b):return hashlib.sha256(b).hexdigest()
def canon(x):return sh(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode())
bindings={}
def bind(p,role):
 p=Path(p);b=p.read_bytes();r={'path':str(p),'sha256':sh(b),'bytes':len(b),'role':role};bindings[str(p)]=r;return r

def read(p,role='source input'):bind(p,role);return json.loads(Path(p).read_text())
def save(p,x):
 p=Path(p);assert not p.exists(),p;p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n');return bind(p,'new artifact')
def cp(p,name,role):
 p=Path(p);dst=O/name;dst.parent.mkdir(exist_ok=True,parents=True);assert not dst.exists(),dst;shutil.copyfile(p,dst);b=bind(p,role);assert sh(dst.read_bytes())==b['sha256'];return {'root':'artifact','path':str(dst.relative_to(A)),'sha256':b['sha256']}
start=now();head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()
ps=read(A/'successor-v2/proposals.json')['proposals'];ds=read(A/'successor-v2/decisions.json')['decisions'];es=read(A/'successor-v2/evidence.json')['evidence'];em={x['evidence_id']:x for x in es};pm={x['proposal_id']:x for x in ps};cases=read(Q/'shards/shard-10.json')['cases'];allentries=read(I/'all-active-proposal-entries-v1.json')['entries'];entries={x['index']:x for x in allentries}
ids=[939,943,944,946,980];caseix=[65,87,94,102,125,178];pids=[entries[i]['proposal_id']for i in ids];selected=[pm[k]for k in pids];new_ids={k:'sv3-hm-'+k.replace('sv1-buffers-','').replace('sv1-kg-','')for k in pids}
save(O/'inputs/exact-selected-objects.json',{'base_head':head,'entries':[entries[i]for i in ids+[106]],'decisions':[ds[i]for i in caseix],'cases':[cases[i]for i in caseix],'proposals':selected,'source_ledger_hashes':{str(p.relative_to(A)):sh(p.read_bytes())for p in [A/'successor-v2/decisions.json',A/'successor-v2/proposals.json',A/'successor-v2/evidence.json']}})
for rel in ['MAPPING_SEMANTICS.md','.claude/skills/add-media/SKILL.md','src/mediaingredientmech/schema/mediaingredientmech.yaml','src/mediaingredientmech/validation/write_validated.py','src/mediaingredientmech/validation/component_partonomy.py','scripts/validate_strict.py'] :bind(R/rel,'native contract or validator')
issue=read(A/'successor-v3/inputs/issue1237-live.json','live issue capture supplied by root')
for n in ['findings-matrix-v2.json','bound-origin-entries-v2.json','w05-source-index-v2.json','w05-packet-verification.json']:read(T/n,'coordinator frozen triage')
for n in ['primary-chemicals/entry-assessments-v2.json','primary-chemicals/pair-assessments-v4.json','primary-chemicals/findings.json','primary-chemicals/family-coverage.json','primary-biologicals/comparison-v2.json','primary-biologicals/findings-v1.json','primary-biologicals/unresolved-options-v3.json','skeptical-review/final-scientific-review.json','skeptical-review/source-observation-004.json','skeptical-review/final-assembly-review.json']:read(W/n,'prior primary/skeptical comparison; selected scope only')
# Preserve complete selected family objects, not just quotations.
chem_entries=read(W/'primary-chemicals/entry-assessments-v2.json');chem_pairs=read(W/'primary-chemicals/pair-assessments-v4.json');bio=read(W/'primary-biologicals/comparison-v2.json')
save(O/'inputs/prior-selected-comparison.json',{'chemical_entries':[x for x in chem_entries if x['entry_index']in[106,939,943,944,946]],'chemical_pairs':[x for x in chem_pairs if set(x['entries'])<={106,939,943,944,946}],'biological_entry':next(x for x in bio['entry_assessments']if x['entry_index']==980),'biological_pairs':[x for x in bio['pairwise_comparisons']if 980 in x['entry_indices']],'scope':'Complete selected entry/pair objects; original authors and old assertions retained. Other W05 families are not newly reviewed.'})
# Preserve all original source cases and full frozen recipe snapshots; verify raw component selectors.
contexts=[]
for i in caseix:
 c=cases[i];assert canon(c)==ds[i]['case_input_sha256'];snap=[]
 for j,o in enumerate(c.get('occurrences',[])):
  p=Q/o['full_recipe_snapshot'];assert sh(p.read_bytes())==o['source_file_sha256'];d=yaml.safe_load(p.read_text());v=d
  for part in o['component_path'].split('/'):v=v[int(part)]if isinstance(v,list)else v[part]
  assert v==o['raw_component'];cap=cp(p,f'inputs/case{i}-recipe{j}.yaml','complete frozen receiving recipe')
  snap.append({'occurrence':o,'capture':cap,'parsed_complete_recipe':d,'raw_component_match':True})
 contexts.append({'source_index':i,'case_id':c['case_id'],'canonical_case_sha256':canon(c),'complete_case':c,'source_snapshots':snap})
save(O/'inputs/full-source-contexts.json',contexts)
# Copy exact primary bytes, preserving original retrieval timestamps and evidence records.
evidence=[];primary=[];seen=set()
for prop in selected:
 for eid in prop['evidence_ids']:
  if eid in seen:continue
  seen.add(eid);e=em[eid]
  if e['kind'] not in ['primary_source','ontology'] or not e.get('url'):continue
  if eid=='sv1-kg-bd-manual-browser':continue
  p=A/e['capture']['path'];assert sh(p.read_bytes())==e['capture']['sha256'];cap=cp(p,'captures/'+eid+p.suffix,'original evidence capture');new=copy.deepcopy(e);new['evidence_id']='sv3-hm-'+eid;new['capture']=cap;new['original_evidence_id']=eid;new['original_capture']=e['capture'];new['case_ids']=[d['case_id']for d in ds if d.get('source_index')in caseix and eid in d['evidence_ids']];evidence.append(new);primary.append({'original_evidence':e,'successor_evidence_id':new['evidence_id'],'capture':cap})
# Worker02 read-only comparison context includes its exact cases, decisions, products and both complete captures.
w2=next(x for x in chem_entries if x['entry_index']==106);save(O/'inputs/w02-entry106-context.json',w2)
for e in w2['selected_primary_capture_bindings']:
 p=Path(e['path']);assert sh(p.read_bytes())==e['sha256'];orig=e['original_evidence_record'];eid='sv3-hm-w02-'+orig['evidence_id'];cap=cp(p,'captures/w02-'+p.name,'read-only worker02 primary');n=copy.deepcopy(orig);n.update(evidence_id=eid,capture=cap,case_ids=[ds[i]['case_id']for i in caseix if i!=178],comparison_context_only=True,original_evidence_record=orig);evidence.append(n)
 for sourcecase in w2.get('raw_source_cases',[]):pass
# Manufacturer editions and failed requests are immutable historical captures.
bdev=read(W/'primary-biologicals/evidence-v1.json')['evidence'];manualrefs=['BIO-NEW-bd-second-edition-nmsu','BIO-NEW-bd-columbia-manufacturer-mirror','BIO-NEW-bd-manual','BIO-NEW-bd-manual-second-edition-mirror'];manual=[]
for ref in manualrefs:
 e=next(x for x in bdev if x['evidence_ref']==ref);rel=e.get('body_path',e.get('path'));p=W.parent.parent/rel;assert p.exists(),p;assert sh(p.read_bytes())==e['sha256'];cap=cp(p,'captures/'+p.name,ref);meta=W.parent.parent/e['metadata_path'];assert sh(meta.read_bytes())==e['metadata_sha256'];mcap=cp(meta,'captures/'+meta.name,'original retrieval receipt');eid='sv3-hm-'+ref.lower();n={'evidence_id':eid,'kind':e['kind'],'capture':cap,'url':e['url'],'accessed_at':e['accessed_at'],'locator':e['locator'],'supports_or_contradicts':'Actual 2009 second-edition PDF supports only its nominal printed formulation; older edition is version context and HTTP404 bodies are failed attempts. No historical lot equivalence.','case_ids':[ds[178]['case_id']],'original_capture_metadata':e,'retrieval_receipt':mcap};evidence.append(n);manual.append(n)
manual2009=manual[0];manualurl=manual2009['url'];manualhash=manual2009['capture']['sha256'];manualtime=manual2009['accessed_at']
# Derive readable page extract from actual copied PDF. Preserve full file and image byte bindings.
pdf=A/manual2009['capture']['path'];subprocess.run(['pdftotext','-f','167','-l','171','-layout',str(pdf),str(O/'captures/bd-2009-columbia-pp155-159.txt')],check=True)
cp(W/'primary-biologicals/new-primary/bd-columbia-page158.png','captures/bd-2009-page158.png','historical visual extraction checked against actual PDF')
cp(P/'older-manual.txt','captures/older-manual.txt','new text extraction of older capture; not a replacement version')
wrapper=em['sv1-kg-bd-manual-browser'];cap=cp(A/wrapper['capture']['path'],'captures/historical-search-wrapper.json','historical search wrapper, not direct PDF');evidence.append({'evidence_id':'sv3-hm-wrapper-context','kind':'source_snapshot','capture':cap,'url':wrapper['url'],'accessed_at':wrapper['accessed_at'],'locator':'Original web-search result wrapper; preserve discovery/indexed snippet only.','supports_or_contradicts':'Supersedes the evidential use of sv1-kg-bd-manual-browser as a positive primary PDF. Original evidence object remains immutable. It is not the actual manual bytes.','case_ids':[ds[178]['case_id']],'historical_evidence_record':wrapper})
# Ignored-inclusive native inventory: preserve every current owner hash, active exact identifier and relevant label hits.
owners=[];hits=[];records=[]
for p in sorted((R/'data/ingredients').rglob('*.yaml')):
 r=yaml.safe_load(p.read_text());records.append(r);b=bind(p,'maintained owner read only');owners.append(b)
 names=[r.get('preferred_term','')]+[x.get('synonym_text','')for x in r.get('synonyms',[])];text=' '.join(names).casefold(); wanted={entries[i]['identifier']for i in ids}
 if r.get('identifier')in wanted or any(k in text for k in ['columbia','hydrochloric','hcl']):hits.append({'path':str(p.relative_to(R)),'sha256':b['sha256'],'record':r})
assert not any(r.get('identifier')in{entries[i]['identifier']for i in ids}and r.get('mapping_status')!='REJECTED'for r in records)
save(O/'inputs/native-owner-lookup.json',{'at':now(),'ignored_and_hidden_included':True,'inventory_count':len(owners),'inventory':owners,'relevant_hits':hits,'exact_proposed_identifier_active_hits':[],'limit':'No new identity minted; current source-qualified successor identifiers retained. Mixed Columbia_Blood_Agar_Base provenance remains coordinator continuity dependency; no wholesale repurposing.'})
# Pair-level correction is conditional, never a new equality or disjointness assertion.
relation=('Literal 25%, 32% and 35% are retained as source specifications, not normalized comparable fractions. '
'The cited sources do not state a common percentage basis, carrier, grade or assay tolerance; the exact same-or-distinct preparation relation is unresolved. '
'TOGO M2305/M2746 explicitly calls its 25% input concentrated, so that qualitative label does not exclude a numerical percentage. '
'If comparable definitions and assay ranges were established, a real strength difference could be assessed; they are not established here. '
'Before co-installing overlapping candidates, the coordinator must choose an explicit common bounded partial-material scope preserving every source context, or obtain comparable preparation/product evidence. No owner merge or arbitrary winner is selected.')
nominal35old='This source-specified acid reagent is distinct from dry/gaseous HCl and from nominal 25% or 32% preparations.'
nominal35new='This source-specified acid reagent is not equated to pure dry/gaseous HCl. Its relation to nominal 25% and 32% preparations is unresolved because comparable percentage and material specifications are absent.'
def replace_strings(x):
 if isinstance(x,str):return x.replace(nominal35old,nominal35new)
 if isinstance(x,list):return [replace_strings(v)for v in x]
 if isinstance(x,dict):return {k:replace_strings(v)for k,v in x.items()}
 return x
newprops=[];newrecs=[];diffs=[];guard=[]
for ix in ids:
 oldp=pm[entries[ix]['proposal_id']];before=A/oldp['after_capture']['path'];assert sh(before.read_bytes())==oldp['after_capture']['sha256'];cp(before,'inputs/before-'+before.name,'exact selected predecessor payload');old=yaml.safe_load(before.read_text());rec=copy.deepcopy(old)
 if ix!=980:
  # Preserve every existing history object literally, while correcting active assertions.
  hist=rec.pop('curation_history');rec=replace_strings(rec);rec['curation_history']=hist
  rec['notes']+=' Successor-v3 relation correction: '+relation
  rec['component_assertion']['notes']+=' '+relation
  rec['ontology_mapping']['evidence'].append({'evidence_type':'LLM_SUGGESTION','source':'https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2305','notes':'LLM-assisted bounded comparison under issue1237, independently checked against exact source captures. '+relation})
  change='Correct unsupported cross-strength disjointness and record conditional relations among nominal-percent and qualitative HCl preparations under CHEM-COMP-004. Preserve all literal specifications, source routes, component assertions, quantities and original history; no consolidation or release.'
  desc=replace_strings(oldp['description'])+' '+relation
 else:
  details=('Recovered manufacturer-authored BD Difco & BBL Manual, second edition 2009, printed p158 (PDF page170), hosted by NMSU. '
   f'Original capture {manualtime}, SHA256 {manualhash}. '
   'The approximate per-liter Difco table lists pancreatic digest of casein10g, Proteose Peptone No.3 5g, yeast extract5g, beef heart infusion from500g 3g, corn starch1g, sodium chloride5g and agar15g; the footnote allows adjustment/supplementation to meet performance criteria. '
   'It directs suspension of44g powder in1L purified water. Those are manufacturer preparation/formula statements, not dry-product mass fractions, final yield, or an identified historical JCM lot. '
   'The same page separately gives BBL42.5g (including13.5g agar, meat peptic digest and heart pancreatic digest) and DifcoEH39g (including12g agar and different nutrient inputs). '
   'The older mirrored manual has different heart wording and BBL proportions and is retained as separate version context. The old search wrapper and failed official/mirror requests remain historical leads, not primary manual evidence.')
  rec['notes']+=' Successor-v3 evidence repair: '+details+' Mixed existing Columbia_Blood_Agar_Base owner continuity remains a separate coordinator obligation; this does not authorize an independent new-owner installation.'
  rec['ontology_mapping']['evidence'].append({'evidence_type':'LLM_SUGGESTION','source':manualurl,'notes':'LLM-assisted source comparison and registry-scope assessment; no human manual-curation claim. '+details})
  rec['component_assertion']['evidence']=[{'evidence_type':'RECIPE_SOURCE','source':manualurl,'source_record':'BD Difco & BBL Manual, Second Edition (2009), Columbia Agars, printed page158 / PDF page170','notes':details}]
  rec['component_assertion']['notes']='Seven named constituents only, scoped to the nominal 2009 Difco manufacturer formulation. PARTIAL is retained for the source-qualified JCM1270 input: exact historical lot and any performance-related adjustments are unverified. No blood or reconstitution water is a dry-base component.'
  rec['supplied_form'][0]['notes']+=' '+details
  change='Replace search-wrapper-as-primary evidential support with exact recovered BD2009 manual PDF and page158 provenance under BIO-F07; retain original wrappers, older edition and failed URLs historically. Components, source-qualified identity and original history retained; no historical lot or release approval.'
  desc=oldp['description']+' '+details
 record_curation_event(rec,curator='codex_worker10_successor_v3_bio_research',action='CORRECTED',changes=change,previous_status=old['mapping_status'],new_status=old['mapping_status'],llm_assisted=True)
 assert rec['curation_history'][:-1]==old['curation_history'];assert rec['components']==old['components']
 target=O/'proposed'/before.name;write_validated_ingredient(rec,target);cap={'root':'artifact','path':str(target.relative_to(A)),'sha256':sh(target.read_bytes())};newrecs.append(rec)
 p=copy.deepcopy(oldp);p['proposal_id']=new_ids[oldp['proposal_id']];p['description']=desc;p['after_capture']=cap;p['independent_review']={'status':'pending','evidence_ids':[]};p['before_sha256']=None
 p['supersedes']={'proposal_id':oldp['proposal_id'],'proposal_object_sha256':canon(oldp),'payload':oldp['after_capture'],'selected_core':'successor-v2/proposals.json','reason':'CHEM-COMP-004'if ix!=980 else'BIO-F07','replace_selected_proposal_not_add_second_owner':True}
 p['evidence_ids']=[e for e in p['evidence_ids']if e!='sv1-kg-bd-manual-browser']+[e['evidence_id']for e in evidence if (ds[178]['case_id']in e.get('case_ids',[]))==(ix==980)]
 p['publication_holds']=list(dict.fromkeys(p.get('publication_holds',[])+([relation]if ix!=980 else['Original mixed Columbia_Blood_Agar_Base owner continuity, historical lot composition and all full owner/role/export admission remain unapproved.','Historical search wrapper sv1-kg-bd-manual-browser is not positive primary manual support in this successor.'])))
 p['applicable_occurrence_ids']=[o for i in caseix if ds[i]['case_id']in p['case_ids']for o in ds[i]['occurrence_ids']]
 newprops.append(p);diffs.append({'entry_index':ix,'before_payload':oldp['after_capture'],'after_payload':cap,'changed_fields':[k for k in old.keys()|rec.keys()if old.get(k)!=rec.get(k)],'field_changes':{k:{'before':old.get(k),'after':rec.get(k)}for k in old.keys()|rec.keys()if old.get(k)!=rec.get(k)},'all_original_history_exact_prefix':True,'components_unchanged':True,'identifier_unchanged':old['identifier']==rec['identifier']})
 guard.append({'proposal_id':p['proposal_id'],'payload':cap,'validator':'write_validated_ingredient closed IngredientRecord','errors':0})
# Source-case decisions: retain complete raw identity, exact occurrences and all prior source holds.
newdec=[]
for i in caseix:
 old=ds[i];d=copy.deepcopy(old);d=replace_strings(d)if i==87 else d;d['proposal_ids']=[new_ids.get(k,k)for k in d['proposal_ids']];d['issue_refs']=list(dict.fromkeys(d.get('issue_refs',[])+[issue['url']]));d['independent_review']={'status':'pending','evidence_ids':[]};d['reviewer']='/root/bio_research';d['review_authorship']='Primary successor science by /root/bio_research; not original payload author. Prior buffer skeptical-review participation disclosed; no inherited acceptance. Separate skeptical successor review required.'
 if i!=178:
  d['disposition']='stock_product_mixture_context';d['reasoning']+=' Successor-v3: '+relation;d['applicability']+=' Existing source occurrences only; W02 M2305/M2746 is comparative evidence and does not add its cases or occurrences to this proposal.';d['missing_requirement']='Bounded named preparation remains supportable. Comparable percentage/product evidence or an explicit common partial-material convention is required before overlap reconciliation/co-installation; not a prerequisite for recording the literal source input.'
 else:
  d['reasoning']='JCM1270 identifies the44g BD-Difco dry base before separate950mL water and50mL sheep blood. The actual manufacturer-authored BD2009 second-edition PDF, captured from NMSU, printedp158/PDFpage170, verifies the seven nominal Difco constituents and separately distinguishes BBL andEH. This replaces the original web-search wrapper as primary support. The approximate formula and performance-adjustment footnote do not prove a historical lot. Retain PARTIAL names-only components and no dry mass-ratio inference. Direct JCM sheep blood differs from MediaDive steps naming horse blood; MediaDive table gives100mLsheep/900mLwater. These receiving-medium discrepancies do not add blood or water to the dry base.'
  d['applicability']='Only frozen mediadive.ingredient:2046 BD-Difco44g row associated with JCM1270. Nominal2009 manufacturer formulation is supporting product context, not a historical-lot certificate. Existing mixed generic Columbia owner continuity remains coordinator work; no new broad source routes or alternate-product equivalence.'
  d['missing_requirement']='No missing fact blocks the bounded manual-evidence correction. Historical lot details and existing mixed-owner continuity/admission remain separate limitations.'
 d['evidence_ids']=[e for e in d['evidence_ids']if e!='sv1-kg-bd-manual-browser']+[e['evidence_id']for e in evidence if d['case_id']in e.get('case_ids',[])]
 d['successor_v3_reassessment']={'finding_id':'CHEM-COMP-004'if i!=178 else'BIO-F07','prior_decision_sha256':canon(old),'prior_selected_core':'successor-v2/decisions.json','prior_payload_authorship':False,'prior_review_not_inherited':True,'source_case_and_occurrences_unchanged':True,'old_completion_reassessment_is_historical':True,'enum_retagging_deferred_to_root_issue1226':True,'release_authorization':False}
 assert d['case_input_sha256']==old['case_input_sha256']and d['source']==old['source']and d['occurrence_ids']==old['occurrence_ids'];newdec.append(d)
# Source-scope and pair receipt is itself evidence; it does not make shared partial-class convention decisions.
comparisons=[]
for a,b in itertools.combinations([106,939,943,944,946],2):
 comparisons.append({'entries':[a,b],'classification':'unresolved_exact_preparation_relation','positive_facts':{'106':'M2305/M2746 literal25%,10mL; narrative concentrated','939':'qualitative concentrated, differing receiving doses only','943':'M3216 literal35%,10mL','944':'JCM770 literal32%,1mL','946':'JCM431/899 literal25%,12.5/5mL'},'reason':relation,'conditional_options':['Retain source-qualified proposals on explicit co-installation hold while comparable material evidence is obtained.','Coordinator may define one nominal partial scope with every original source/case/history obligation; this would be a declared scope convention, not demonstrated historical formulation equality.'],'prohibited_inference':'Unknown percentage basis, absent carrier or source number establishes neither equality nor disjointness.'})
assessment={'author':'/root/bio_research','observed_review_start':read(O/'review-start.json'),'science_frozen_at':now(),'scope':{'w10_entries':ids,'w10_case_indices':caseix,'w02_context_entry':106,'w02_mutations':False,'hcl_pairs_all10':comparisons,'excluded':'No combined Oxoid300/921 or phosphate873/940 candidate; no other family rewrite.'},'authorship':'Did not author original HCl buffers or KG980. Previously independently reviewed buffers successor, now explicitly corrects its missed boundary. Authored separate worker10 Oxoid921 comparator; no independent self-review or candidate change of921 here.','manufacturer_review':{'actual_pdf':manual2009,'visual_page158_checked':True,'title_copyright':'Second Edition2009, copyright Becton Dickinson and Company2009','formula_basis':'Approximate formula per liter; footnote adjusted/supplemented as required to meet performance criteria.44g powder suspended in1Lwater is a preparation instruction, not final yield or water inside powder.','constituents':[{'name':n,'printed_grams_per_liter':v}for n,v in [('Pancreatic Digest of Casein',10),('Proteose Peptone No.3',5),('Yeast Extract',5),('Beef Heart, Infusion from500g',3),('Corn Starch',1),('Sodium Chloride',5),('Agar',15)]],'older_edition':'Separate older mirrored excerpt uses BeefHeartInfusion3g wording; BBL lists casein12g,animal-tissue digest5g,yeast3g,beefextract3g rather than2009casein10/meatpeptic5/yeast5/heartpancreatic3. Not a silent substitute.','historical_wrapper':'Preserved verbatim, withdrawn as active primary support without rewriting old evidence object.','no_historical_lot_claim':True},'case_assessments':[{'source_index':d['source_index'],'case_id':d['case_id'],'reasoning':d['reasoning'],'applicability':d['applicability'],'missing_requirement':d['missing_requirement']}for d in newdec],'source_captures':primary,'manual_editions_and_failures':manual,'all_old_artifacts_preserved':True,'native_inventory_count':len(records),'validation':'Isolated guarded payloads; schema/partonomy receipt separate.','no_scientific_role_export_or_release_approval':True,'new_findings':[]}
asscap=save(O/'primary-review.json',assessment)
evidence.append({'evidence_id':'sv3-hm-primary-review','kind':'source_snapshot','capture':{'root':'artifact','path':str((O/'primary-review.json').relative_to(A)),'sha256':asscap['sha256']},'locator':'All6case assessments,10HCl pair relations, actual2009manual/olderedition boundaries and exact reused-capture provenance','supports_or_contradicts':'Source-bound successor corrections only; independent skeptical review pending.','case_ids':[d['case_id']for d in newdec]})
for d in newdec:d['evidence_ids']=list(dict.fromkeys(d['evidence_ids']+['sv3-hm-primary-review']))
for p in newprops:p['evidence_ids']=list(dict.fromkeys(p['evidence_ids']+['sv3-hm-primary-review']))
save(O/'decision-fragment.json',{'decisions':newdec});save(O/'proposals-fragment.json',{'proposals':newprops});save(O/'evidence-fragment.json',{'evidence':evidence});save(O/'old-new-field-diffs.json',diffs)
save(O/'validation/guarded-write.json',{'at':now(),'targets':guard,'count':len(guard),'errors':0,'new_MappingEvidence_types':['LLM_SUGGESTION'],'inherited_enums_unchanged_for_root1226':True})
baseline=validate_component_partonomy(records);overlay=validate_component_partonomy(records+newrecs);save(O/'validation/partonomy.json',{'at':now(),'baseline_record_count':len(records),'proposed_count':len(newrecs),'baseline_violations':[vars(v)for v in baseline],'overlay_violations':[vars(v)for v in overlay]})
assert not baseline and not overlay
assert all(sh(Path(x['path']).read_bytes())==x['sha256']for x in owners)
save(O/'input-hashes.json',{'audit_execution_started_at':start,'audit_execution_finished_at':now(),'inputs':list(bindings.values()),'scope':'Actual read/copy/hash bindings; full primary text read scope described in primary-review, not inferred solely from hashcheck.','maintained_inventory_unchanged':True})
print(json.dumps({'proposals':len(newprops),'decisions':len(newdec),'new_evidence':len(evidence),'guard_errors':0,'partonomy_errors':len(overlay),'primary_review_sha256':asscap['sha256']}))
