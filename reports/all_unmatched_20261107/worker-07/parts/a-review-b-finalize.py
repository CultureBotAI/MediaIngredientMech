"""Assemble independently authored review after primary remediation inspection."""
import datetime,hashlib,importlib.util,json,sys
from pathlib import Path
import yaml
from mediaingredientmech.validation.write_validated import validate_ingredient
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy,load_ingredient_records
R=Path(__file__).resolve().parents[1]
Q=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
spec=importlib.util.spec_from_file_location('review_notes',R/'parts/a-review-b-build.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
notes=dict(m.NOTES)
notes.update({
90:'I independently checked the frozen seven occurrences, all six cited PMID/DOI metadata records and five family-specific primary pursuits. Park and Zhu accessible abstract/paywall pages do not expose reagent formula; Fischer Wiley challenges and Mogensen/Shcolnick Elsevier landing pages likewise do not resolve sodium count or hydration. Precise per-family missing requirements are supported. Follonier EDTA in another case is not transferred.',
91:'My initial challenge identified Sigma V6629 in the complete frozen UTEX DAS occurrence. I independently read the recovered original UTEX catalogue linkage and official Sigma V6629 cyanocobalamin/CAS68-19-9 specification. The revised source-specific cyanocobalamin correction is supported; the initial generic Vitamin_B12 alias proposal is withdrawn. No generic cobalamin-to-cyano synonym is approved.',
95:'I read DSMZ110,78 and110a original PDFs: each explicitly uses25mL1N NaOH in meat extraction, with differing parent media and separate extraction water. Three source-qualified nominal stocks preserve1N and exact occurrence subsets; UNKNOWN completeness is appropriate for unreported stock solvent and manufacture. No final-medium normality or cross-source identity is asserted. Unrelated cysteine inheritance text was removed.',
108:'I independently read recovered TOGO M2256 JSON: component_name explicitly Magnesium Sulfate (anhydrous),0.1g; this agrees with frozen form and CHEBI32599. Other hydrates cannot absorb this alias.',
109:'I independently read recovered TOGO M3175 component and narrative: Sodium citrate tribasic dihydrate,3g, fixes both trisodium stoichiometry and two waters. CHEBI32142 and the bounded alias are supported.',
111:'I independently read recovered M3057 CH3COONa200mg and M3221 CH3COONa0.0683g, including M3221 narrative. Formula supports sodium acetate without adding waters. Frozen anomalous flattened units remain preserved; no final-dose recalculation is approved.',
116:'I independently inspected Schaechter1958 original Table1 image and footnote(c): Na(NH4)HPO4·4H2O1.74g/L,50x concentrate, explicitly used by rows14–22. Nine frozen Schaechter occurrences resolve to CAS7783-13-3; official Sigma/Thermo/Roth formula evidence independently agrees. I read exact CHEBI190300 term object: inorganic phosphate salt, definition lacking C-H bonds, non-obsolete. This is a deliberately broad asymmetric parent, never exact identity. I read Follonier full Methods: separate bioreactor NaNH4PO4·4H2O cannot establish three Durner/E2 flask occurrences. Durner, four Hassan and one Tseng fulltext attempts remain unavailable and are separately documented; no generic salt synonym is added.',
118:'I independently read original JCM825 now retrieved:3% L-cysteine·HCl·H2O solution10mL, matching frozen MediaDive4784. The nominal stock preserves explicit L/HCl/monohydrate, unreported percent basis and stockpH, and keeps stock and solute identities separate.',
121:'I checked all13 original JCM source families for14 occurrences and the new nominal payloads, including gas, sterilization, parent-medium dose and pH scope. JCM1463 explicitly inherits1462 with NaCl adjustment only. JCM1422 current4mL versus frozen10mL discrepancy is retained explicitly; neither stock strength nor frozen dose is silently changed. Every5% stock uses UNKNOWN completeness and unspecified percent basis without inventing solvent or stockpH.',
128:'I independently read recovered M2577 component_name L-Cysteine x HCl,0.1g. L and hydrochloride are explicit, without monohydrate; CHEBI91247 bounded alias is supported. This claim does not approve the complete inherited owner payload.',
134:'I checked six original JCM families for seven frozen occurrences and each nominal payload. TOGO M708 independently says it follows JCM687 with methanol replaced by formate. JCM706 source explicitly says0.05mL stock per4.7mL medium; my final challenge corrected the erroneous10mL basis. All5% L/HCl/monohydrate boundaries and individual source doses remain, without global stock alias or invented percent convention.'})

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def jread(p):return json.loads(p.read_text())
now=datetime.datetime.now(datetime.UTC).isoformat()
ds=jread(R/'parts/b-decisions.json')['decisions'];es=jread(R/'parts/b-evidence.json')['evidence'];ps=jread(R/'parts/b-proposals.json')['proposals'];cs=jread(R/'parts/b-input.json')['cases']
input_hashes={f:sha(R/f) for f in ['parts/b-input.json','parts/b-decisions.json','parts/b-evidence.json','parts/b-proposals.json','parts/b-family-review.json']}
errors=[];occ=[];evcheck=[];pc=[];case_rows=[]
for i,(c,d) in enumerate(zip(cs,ds),70):
 if c['case_id']!=d['case_id']:errors.append(f'case mismatch{i}')
 if set(d['occurrence_ids'])!={o['occurrence_id'] for o in c['occurrences']}:errors.append(f'occurrence scope mismatch{i}')
 digest=hashlib.sha256(json.dumps(c,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
 if digest!=d['case_input_sha256']:errors.append(f'case digest{i}')
 for o in c['occurrences']:
  p=Q/o['full_recipe_snapshot'];h=sha(p);v=yaml.safe_load(p.read_text())
  for step in o['component_path'].strip('/').split('/'):v=v[int(step)] if isinstance(v,list) else v[step]
  matched=v==o['raw_component']
  if h!=o['source_file_sha256'] or not matched:errors.append(f'raw occurrence mismatch{o["occurrence_id"]}')
  occ.append({'case_id':c['case_id'],'occurrence_id':o['occurrence_id'],'source_file':o['full_recipe_snapshot'],'sha256':h,'pointer':o['component_path'],'raw_component_matches':matched})
 case_rows.append({'index':i,'case_id':c['case_id'],'raw_source_label':c['raw_source_label'],'occurrence_ids':d['occurrence_ids'],'case_input_sha256':d['case_input_sha256'],'status':'complete','independent_assessment':notes[i],'evidence_ids_examined':d['evidence_ids'],'proposal_ids_examined':d['proposal_ids']})
for e in es:
 c=e['capture'];p=(Q if c['root']=='source' else R)/c['path'];h=sha(p);ok=h==c['sha256']
 if not ok:errors.append(f'evidence hash {e["evidence_id"]}')
 if e['kind'] in ('primary_source','ontology') and not e.get('accessed_at'):errors.append(f'missing access time {e["evidence_id"]}')
 evcheck.append({'evidence_id':e['evidence_id'],'path':c['path'],'sha256':h,'matches':ok,'kind':e['kind']})
records=load_ingredient_records(Path('data/ingredients'));replaced={p['owner_path'] for p in ps if p['kind']=='edit_existing_owner'}
oldids={yaml.safe_load(Path(p).read_text())['identifier'] for p in replaced}
records=[v for v in records if v.get('identifier') not in oldids]
for p in ps:
 cap=p['after_capture'];path=R/cap['path'];h=sha(path);v=yaml.safe_load(path.read_text());errs=[str(x) for x in validate_ingredient(v)]
 if h!=cap['sha256']:errors.append(f'proposal hash {p["proposal_id"]}')
 if errs:errors.append(f'proposal schema {p["proposal_id"]}: {errs}')
 if p['kind']=='edit_existing_owner' and sha(Path(p['owner_path']))!=p['before_sha256']:errors.append(f'baseline owner changed {p["proposal_id"]}')
 records.append(v);pc.append({'proposal_id':p['proposal_id'],'path':cap['path'],'sha256':h,'schema_errors':errs,'status':'bounded_payload_reviewed'})
violations=[str(x) for x in validate_component_partonomy(records)]
if violations:errors.extend(violations)
integ={'reviewer':'/root/primary_a','checked_at':now,'input_hashes':input_hashes,'case_count':len(cs),'occurrence_checks':occ,'evidence_checks':evcheck,'proposal_checks':pc,'partonomy_violations':violations,'errors':errors,'scientific_approval_established':False}
(R/'captures/a-review-b-integrity-final.json').write_text(json.dumps(integ,indent=2,ensure_ascii=False)+'\n')
if errors:print(json.dumps(errors,indent=2));sys.exit(1)
resolutions={
'A-REVIEW-B-91':'Resolved by primary UTEX/Sigma V6629 cyanocobalamin evidence, source-specific correction and withdrawal of generic Vitamin_B12 alias proposal.',
'A-REVIEW-B-90':'Resolved by all seven occurrences bound to five exact primary-reference families with separately inspected pursuits/access limitations and precise remaining chemical requirements.',
'A-REVIEW-B-116':'Resolved by all17 occurrences bound to four source families; original Schaechter Table1 establishes nine tetrahydrate identities and actionable CAS proposal; other eight retain documented independent gaps.',
'A-REVIEW-B-EVIDENCE-KINDS':'Resolved: MediaDive WrongCall and JCM Nothing found responses retained as unsuccessful_search; successful recipe/ontology evidence remains separately scoped.',
'A-REVIEW-B-STOCK-SCOPE':'Resolved: JCM706 dose corrected to0.05mL per4.7mL; JCM1422 current4mL/frozen10mL discrepancy preserved; inheritance wording scoped only to the relevant cases.'}
findings=[]
for f in jread(R/'parts/a-review-b-findings-initial.json')['findings']:
 findings.append({**f,'status':'resolved','resolution':resolutions[f['id']]})
out={'reviewer':'/root/primary_a','primary_author':'/root/primary_b','reviewed_at':now,'status':'complete','scope':f'All{len(cs)} cases indices70:140, all{len(occ)} complete frozen recipe occurrences, and all{len(ps)} final exact payloads. Independent claim-level source/proposal review; native full-owner publication review is separate.','input_hashes':input_hashes,'cases':case_rows,'findings':findings,'proposal_payloads':pc,'integrity_capture':{'path':'captures/a-review-b-integrity-final.json','sha256':sha(R/'captures/a-review-b-integrity-final.json')},'shared_review_separation':{'JCM900':'I independently review B110 exact primary stock payload; C reviews A38/47 source applicability. Coordinator combination with equivalent JCM979 requires separate integration review.','JCM1209':'I independently review B122 exact stock payload against original JCM1209 table; B independently reviews C156 source applicability.','C-P01':'B reviews C-authored NTA payload; C reviews A55 source applicability. No author self-review replaces an independent claim review.'},'limitations':['Inherited full owner payload publication eligibility remains subject to coordinator native review and existing WITHHOLD/REJECTED gates.','Nominal stock proposals preserve source unknowns and do not establish final culture concentrations or source-wide synonym equivalence.','Paywall/challenge responses establish pursuit and access limits only; unresolved source salt forms remain unresolved.','This review pins the exact author bytes above; coordinator integration deltas require separate independent review.']}
(R/'parts/a-review-b-final.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'cases':len(cs),'occurrences':len(occ),'evidence':len(es),'proposals':len(ps),'schema_errors':0,'partonomy_violations':0,'report_sha256':sha(R/'parts/a-review-b-final.json'),'input_hashes':input_hashes},indent=2))
