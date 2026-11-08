"""Read-only source assessment; writes new evidence only below this directory."""
from pathlib import Path
from datetime import datetime, timezone
from decimal import Decimal
from html.parser import HTMLParser
import csv
import hashlib
import json
import subprocess
import yaml

OUT = Path(__file__).resolve().parent
W = OUT.parents[3]
C = Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107')
P = C / 'preflight/tenvit-final-application-route-v1'
W09 = C / 'workers/w09/worktree/.temp/tenvit-continuity-resolution-v1'
ART = W / 'reports/all_unmatched_20261107/worker-08'
NOW = datetime.now(timezone.utc).isoformat()
AUTHOR = 'worker08:/root/vitamins'
CASE = 'CM_NAME:d57e91ffaea6f0ab6ff0f3d6f0b04c26356c832e85dd83e9e2319874fda43506'

def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def canonical(value): return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
def read(path): return json.loads(path.read_text())
def save(name,obj):
    with (OUT/name).open('x') as f: json.dump(obj,f,indent=2,ensure_ascii=False); f.write('\n')
def bind(path): return {'path':str(path),'sha256':sha(path)}

class HTML(HTMLParser):
    def __init__(self):
        super().__init__(); self.rows=[]; self.row=None; self.cell=None; self.parts=[]; self.skip=0
    def handle_starttag(self,t,a):
        if t in ('script','style'): self.skip+=1
        if t=='tr': self.row=[]
        if t in ('td','th'): self.cell=[]
    def handle_data(self,d):
        if not self.skip and d.strip(): self.parts.append(d.strip())
        if self.cell is not None: self.cell.append(d)
    def handle_endtag(self,t):
        if t in ('script','style'): self.skip-=1
        if t in ('td','th') and self.cell is not None:
            if self.row is not None: self.row.append(' '.join(''.join(self.cell).split()))
            self.cell=None
        if t=='tr' and self.row is not None: self.rows.append(self.row); self.row=None

matrix=read(P/'eight-cases-and-scopes.json'); child=read(P/'ten-child-identity-matrix.json')
target=next(x for x in matrix['cases'] if x['case_id']==CASE)
assert canonical(target['source_case']) == target['case_input_sha256'] == '1c8fdd449fe96f1f9a8599fe72941fcf09ef4d0e68a5134be4fdf52b416d9868'
assert sha(P/'AUTHOR-TASK-W08.md') == 'e16acb227308669f7cc883d5d58b454b325331e2082480616d424bd75856448f'
ledger=[]; checks=[]
def check(name,passed,detail=None): checks.append({'check':name,'passed':bool(passed),'detail':detail})
def note(path,scope,kind='context',**extra):
    ledger.append({**bind(path),'read_at':NOW,'read_scope':scope,'kind':kind,**extra})

e6={x['evidence_id']:x for x in read(P/'captures/w06/evidence.json')['evidence']}
e8={x['evidence_id']:x for x in read(P/'captures/w08/evidence.json')['evidence']}
specs=[('JCM197',e6['C-E-jcm-197'],P/'captures/w09/primary/captures/C-E-jcm-197.capture'),
       ('NBRC837',e6['C-E-nbrc-837'],P/'captures/w09/primary/captures/C-E-nbrc-837.capture')]
for n,eid in [(1050,'1962216682ccb735'),(1086,'7d55379a5f033497'),(1226,'ede69c87ee45106a'),(1274,'19ea505c685bcbd1'),(903,'2630e40c26a0b155'),(925,'571507208cde7532')]:
    ev=e8['vm-fetch-'+eid]; specs.append(('NBRC'+str(n),ev,ART/ev['capture']['path']))
recipes={}
for name,ev,path in specs:
    check(name+'_capture_hash',sha(path)==ev['capture']['sha256'])
    h=HTML();h.feed(path.read_text())
    start=next(i for i,r in enumerate(h.rows) if len(r)>=3 and r[-3]=='Biotin')
    parts=[]
    for i in range(start,len(h.rows)):
        r=h.rows[i]
        if len(r)<3: continue
        label,value,unit=r[-3:]
        parts.append({'printed_name':label,'printed_amount':value,'printed_unit':unit,'basis':'listed_water_input' if label=='Distilled water' else 'listed_source_batch','capture_table_row_index':i})
        if label=='Distilled water': break
    recipes[name]={'source_id':name,'capture':bind(path),'original_evidence_id':ev['evidence_id'],'url':ev['url'],'original_accessed_at':ev['accessed_at'],'locator':'Trace vitamins table' if name=='JCM197' else '***Trace vitamins table' if name=='NBRC837' else '**Vitamin solution table','inputs':parts,'final_stock_volume':None,'no_inferred_final_concentration':True}
    text='\n'.join(h.parts)
    (OUT/(name+'-source-text.txt')).write_text(text+'\n')
    note(path,'All recipe composition, stock tables and preparation text inspected; HTML navigation is not scientific evidence. Source text is locally derived, not a new remote retrieval.','primary_source',url=ev['url'],original_accessed_at=ev['accessed_at'],original_evidence_id=ev['evidence_id'],derived_text=bind(OUT/(name+'-source-text.txt')))

preparations={
 'JCM197':{'stock':'Filter sterilize the trace vitamins while gassing with N2.','addition':'Aseptically and anaerobically add trace vitamins under N2-CO2 (80:20).','parent_only':'Parent autoclaving under N2-CO2 (80:20); adjust final parent pH to 6.8.','excluded':'8% NaHCO3, separately autoclaved 5% reducing-agent stocks, mineral-stock pH 7 with 1 N KOH, and parent pH are not vitamin-stock ingredients or pH. No quantified nitrogen part is asserted.'},
 'NBRC837':{'stock':'Filter-sterile vitamin solution; no explicit vitamin-stock N2-gassing instruction.','addition':'Aseptically and anaerobically add the vitamin solution.','parent_only':'Parent autoclaving under N2/CO2 (80/20); parent pH 6.8.','excluded':'Do not transfer JCM197 stock gassing. Separate 5% sulfide/cysteine preparations and trace-mineral pH 7/KOH are different preparations.'},
 'NBRC903':{'stock':'Filter sterilize vitamin solution. No vitamin-stock gas or pH instruction is stated.','addition':'Before inoculation, aseptically and anaerobically add vitamin solution, sulfur and sulfide.','parent_only':'Parent pH 7 and autoclaving under N2.','excluded':'Three successive days of 105 C sulfur sterilization, neutralized 5% sulfide stock, and mineral-stock KOH/pH 6.5 then 7 do not describe the vitamin stock.'},
 'NBRC1050':{'stock':'Filter-sterile vitamin solution; anaerobic addition.','parent_only':'Parent pH 7 adjusted with H2SO4, N2 autoclaving; separate 5% sulfide stock.','excluded':'Trace-element NaOH/pH adjustment and basal sulfuric acid are not vitamin-stock parts.'},
 'NBRC1086':{'stock':'Filter-sterile vitamin solution; aseptic anaerobic addition.','parent_only':'Parent H2/CO2 (80/20) autoclaving and bottle pressure 150 kPa; separate 6% cysteine/sulfide preparations.','excluded':'No vitamin-stock gas, pressure or mineral-stock NaOH is inferred.'},
 'NBRC1226':{'stock':'Vitamin solution sterilized by filtration, then added aseptically and anaerobically with sterile syringes.','parent_only':'Parent dispensed under N2/CO2 (80/20), then autoclaved at 121 C for 15 min.','excluded':'Bicarbonate, cysteine/sulfide and trace-element NTA/KOH preparations remain separate.'},
 'NBRC1274':{'stock':'Vitamin solution sterilized by filtration; aseptic anaerobic addition before inoculation.','parent_only':'Parent N2/CO2 (80/20) handling, autoclaving, final pH 6.8.','excluded':'Separate sulfur sterilization, neutralized 5% sulfide and mineral NaOH are not vitamin-stock components or instructions.'},
 'NBRC925':{'stock':'Filter-sterile vitamins added aseptically and anaerobically.','parent_only':'Parent N2/CO2 (80/20) autoclaving, final pH 7.2–7.5; separate 3% reducing-agent stocks.','excluded':'Trace-element NaOH/pH and reducing-agent N2 preparation do not specify vitamin-stock gas/pH.'}}
for name in recipes: recipes[name]['preparation_partition']=preparations[name]
def nominal_signature(r):
    def norm(s):return s.replace('·','-').replace('Ca-pantothenate','Calcium pantothenate').replace('Vitamin B1 2','Vitamin B12')
    return [(norm(p['printed_name']),str(Decimal(p['printed_amount']).normalize()),p['printed_unit']) for p in r['inputs']]
check('nominal_three_source_inputs_agree',nominal_signature(recipes['JCM197'])==nominal_signature(recipes['NBRC837'])==nominal_signature(recipes['NBRC903']))
check('common_nine_four_sources_agree',all(nominal_signature(recipes[n])==nominal_signature(recipes['NBRC1050']) for n in ['NBRC1086','NBRC1274','NBRC925']))
check('nominal_counts',all(len(recipes[n]['inputs'])==11 for n in ['JCM197','NBRC837','NBRC903','NBRC1226']) and all(len(recipes[n]['inputs'])==10 for n in ['NBRC1050','NBRC1086','NBRC1274','NBRC925']))

ncma_path=W09/'captures/ncma-medium6-current.pdf'; ncma_receipt=read(W09/'captures/ncma-medium6-current-receipt.json')
check('NCMA_original_capture_pin',sha(ncma_path)==ncma_receipt['sha256'])
ncma_text=subprocess.check_output(['pdftotext','-layout',str(ncma_path),'-'],text=True)
(OUT/'NCMA6-derived-text.txt').write_text(ncma_text)
ncma_names=['Pyridoxine HCl','Thiamine HCl','Riboflavin','Nicotinic Acid','Calcium pantothenate','p-Aminobenzoic acid','Thioctic acid','Biotin','Folic acid','Vitamin B12','Potassium phosphate monobasic']
ncma_values=['10.0','5.0','5.0','5.0','5.0','5.0','5.0','2.0','2','0.1','900']
ncma={'source_id':'NCMA6','capture':bind(ncma_path),'capture_receipt':bind(W09/'captures/ncma-medium6-current-receipt.json'),'url':ncma_receipt['url'],'original_accessed_at':ncma_receipt['accessed_at'],'locator':'Complete one-page PDF: Composition per liter table and final preparation sentence','inputs':[{'printed_name':n,'printed_amount':v,'printed_unit':'mg','basis':'per_liter_explicit_source_heading'} for n,v in zip(ncma_names,ncma_values)],'carrier':{'name':'distilled water','quantity':None,'unit':None},'preparation':'Add components to distilled water and filter sterilize.','scope':'Positive eleven-solute phosphate-containing source claim. No numeric 1.0 L/L water claim, no CB association, no new NCMA owner.'}
note(ncma_path,'Complete single-page primary PDF read through actual pdftotext extraction; no network retrieval claimed.','primary_source',url=ncma_receipt['url'],original_accessed_at=ncma_receipt['accessed_at'],derived_text=bind(OUT/'NCMA6-derived-text.txt'))

mix=P/'captures/w09/history/captures/Mixes.csv'; csvrows=list(csv.reader(mix.read_text().splitlines())); block=csvrows[37:51]
check('CB_complete_block_boundary',block[0][0:2]==['Media',"Wolfe's vitamin mix"] and csvrows[51]==['','',''])
cbparts=[{'printed_name':r[0],'printed_amount':r[1],'printed_unit':r[2],'csv_line':i+1} for i,r in enumerate(csvrows) if 41<=i<=50]
cb={'capture':bind(mix),'original_accessed_at':'2026-11-08T08:11:21.012422+00:00','original_capture_metadata':bind(W09/'history/capture-manifest.json'),'locator':'CSV lines 38–51; metadata line 40; ten solute rows 42–51','inputs':cbparts,'metadata':{'X':'100','description':block[1][1]},'solvent':None,'preparation':None,'scope':'Transcribe printed mg/L values without applying X as a multiplier. Ten named solutes, explicit Cyanocobalamin. No listed water or phosphate input in this complete block; absence is not a purity assertion.'}
note(mix,'Complete Wolfe generic block lines 38–51 with adjacent block delimiters inspected, not the unrelated entire CSV.','raw_source',original_accessed_at=cb['original_accessed_at'],original_capture_metadata=cb['original_capture_metadata'])

occurrences=[]
ev_by_source={n:e for n,e,p in specs}
for o in target['source_case']['occurrences']:
    f=C/'queue/preliminary-v5'/o['full_recipe_snapshot']; data=yaml.safe_load(f.read_text()); key,idx=o['component_path'].split('/')
    num=int(next(s['value'].split(':')[-1] for s in o['recipe_source_identifiers'] if s['path']=='/media_term/term/id'))
    group='nominal_ten' if num==903 else 'different_ten_NBRC1226' if num==1226 else 'common_nine'
    check(o['occurrence_id']+'_recipe_hash',sha(f)==o['source_file_sha256'])
    check(o['occurrence_id']+'_exact_component',data[key][int(idx)]==o['raw_component'])
    occurrences.append({'occurrence_id':o['occurrence_id'],'recipe_id':o['recipe_id'],'frozen_recipe':bind(f),'component_path':o['component_path'],'raw_component':o['raw_component'],'frozen_source_filename':o['source_file'],'source_identifier':'nbrc.medium:'+str(num),'partition':group,'primary_evidence_id':ev_by_source['NBRC'+str(num)]['evidence_id'],'primary_recipe_key':'NBRC'+str(num),'comparator_correction_trigger':num==903,'CB_occurrence_asserted':False,'disposition':'Keep existing case/source hold and dose. No source-index repair or implicit whole-case routing.'})
    note(f,'Exact target component, nested vitamin composition, parent preparation and source metadata inspected; full file hash rebound. Other ingredient ontology fields are preserved context, not independently approved.','frozen_source_context')

before=yaml.safe_load((P/'captures/before-Wolfes_Vitamin_Mix.yaml').read_text()); candidate=yaml.safe_load((P/'captures/candidate-fe607027.yaml').read_text())
check('W09_five_authentic_history_events',candidate['curation_history'][:5]==before['curation_history'] and len(before['curation_history'])==5)
check('CB_candidate_ten_literal_rows',[(p['component_name'],p['concentration_value'],p['concentration_unit']) for p in candidate['components']]==[(p['printed_name'],p['printed_amount'],'MG_PER_L') for p in cbparts])
child_checks=[]
for ch in child['children']:
    owner=Path(ch['active_owner']['path']); ob=yaml.safe_load(owner.read_text()); actual=sha(owner)
    check('current_child_owner_'+str(ch['candidate_component_index']),actual==ch['active_owner']['sha256'] and ob['identifier']==ch['active_identity'])
    child_checks.append({'source_name':ch['literal_component']['component_name'],'candidate_index':ch['candidate_component_index'],'current_owner':bind(owner),'current_identity':ob['identifier'],'planning_reference':ch['recommended_component_id'],'scope':ch['reason'],'whole_owner_approval':False})

for x in matrix['cases']: check('frozen_family_case_'+x['case_id'],canonical(x['source_case'])==x['case_input_sha256'])
family_counts={'cases':len(matrix['cases']),'CM_occurrences':sum(len(x['occurrence_ids']) for x in matrix['cases']),'separate_KG_holds':sum(len(x['source_case'].get('original_kg_entry',{}).get('downstream_holds',[])) for x in matrix['cases']),'excluded_contexts':sum(v for k,v in matrix['partitions'].items() if k.startswith('excluded_')),'nominal_context_upper_bound':sum(v for k,v in matrix['partitions'].items() if k.startswith('nominal_'))}
check('family_context_counts_not_admission',family_counts==matrix['counts'])
selection=ART/'successors/issue-1227-plain-flour-v1/selection.json'
check('published_selector_pin',sha(selection)=='335806d22ce278eaf628930b521d7164f0dee2493a19fbc790ae3c273d179f92')
head=subprocess.check_output(['git','-C',str(W),'rev-parse','HEAD'],text=True).strip()
check('starting_worker_head',head=='79d44c84fe550741bbd8de00c119c48560f30bc1')
for n in ['AUTHOR-TASK-W08.md','source-bindings.json','ten-child-identity-matrix.json','eight-cases-and-scopes.json','captures/triage/assessment.json','captures/triage/exact-source-and-candidate-audit.json','captures/triage/HANDOFF.json','captures/w09/ADJUDICATION.json','captures/w09/OPTIONS.json','captures/w09/HANDOFF.json','captures/w09/nominal-ten-vitamin-source-description.json','captures/before-Wolfes_Vitamin_Mix.yaml','captures/candidate-fe607027.yaml','captures/w08/selected-payload.yaml','captures/w06/selected-payload.yaml','issue1237-comment-6719499726-network.json']:
    note(P/n,'Full substantive source/comparison assertions inspected. Family matrix is continuity context; this assessment does not repeat all W06 receiving-source research or release its cases.' if n=='eight-cases-and-scopes.json' else 'Complete relevant document inspected; previous author/reviewer identity and approval limits retained.')
note(W09/'history/REPORT.md','Full history continuity report read; historical Git and 63/62 receiving audit are attributed to the prior W09 researchers, not newly repeated here.')
note(W09/'primary/source-preparation-assessment.json','Full preparation assessment read and compared with the primary recipe captures.')
note(W/'MAPPING_SEMANTICS.md','Sections 3 and 6 read for identity, source boundary and component-partonomy rules.')
note(W/'.claude/skills/add-media/SKILL.md','Formulation/source/identity and partonomy workflow read; no candidate writer invoked in this source-only phase.')

save('nominal-recipe-evidence.json',{'created_at':NOW,'author':AUTHOR,'role':'source_research_assessor_and_prior_W08_author_not_independent_final_reviewer','kind':'structured_source_facts_not_IngredientRecord','nominal_recipe_sources':{k:recipes[k] for k in ['JCM197','NBRC837','NBRC903']},'nominal_comparison':'Ten named input masses and one litre distilled-water input agree after documented HCl punctuation and calcium abbreviation normalization. Preparation remains partitioned. This is a nominal recipe assertion, not proof of identical supplied B12 form or common owner identity.','precise_unknowns':['Generic Vitamin B12 remains ungrounded; do not infer cyanocobalamin or adopt the vitamin-B12 class as a distinct supplied substance.','Unqualified calcium pantothenate does not select D or DL; no D-specific CHEBI:31345 binding follows.','Listed 1 L distilled water is an input batch, not stated final stock volume or 1 L/L water fraction.','No vitamin-stock pH, purchased lot or identical unreported gas handling is inferred.'],'NCMA_separate_positive_source':ncma,'CultureBotHT_source':cb,'whole_owner_or_route_approval':False})
save('occurrence-partitions.json',{'created_at':NOW,'author':AUTHOR,'case_id':CASE,'frozen_case_sha256':target['case_input_sha256'],'source_label':'Vitamin solution**','occurrences':occurrences,'excluded_preparation_sources':{k:recipes[k] for k in ['NBRC1050','NBRC1086','NBRC1226','NBRC1274','NBRC925']},'family_context':{'matrix':bind(P/'eight-cases-and-scopes.json'),'counts':family_counts,'partitions':matrix['partitions'],'limits':'All eight objects are hash-bound continuity context. Only the six W08 occurrences are reassessed here. The 65-context number is an upper bound, not a release or transfer of W06 ownership; all 84 KG holds, J887 access/dose limits, nested preparation distinctions and six exclusions remain.'},'case_or_payload_authored':False})
save('comparison-assessment.json',{'created_at':NOW,'author':AUTHOR,'prior_author_identity':'all-unmatched-worker08-issue1201-vitamins / all-unmatched-worker08-issue1227-vitamins','assessment_status':'SUPPORTED_SOURCE_FACTS_WITH_EXACT_OWNER_ASSOCIATION_HELD','starting_worker_head':head,'published_selector':bind(selection),'existing_before_owner':bind(P/'captures/before-Wolfes_Vitamin_Mix.yaml'),'W09_candidate':{**bind(P/'captures/candidate-fe607027.yaml'),'author_event':candidate['curation_history'][-1],'preserve_event_without_relabelling':True},'old_W08_candidate':bind(P/'captures/w08/selected-payload.yaml'),'old_W06_candidate':bind(P/'captures/w06/selected-payload.yaml'),'comparison_supersession':{'old_claim':'The published W08 NBRC903 description compares the nominal ten-vitamin recipe with the then-inspected Wolfe owner component list containing KH2PO4.','actual_before':'The maintained beforeimage really carries the later NCMA-derived phosphate and quantified-water assertion. Preserve those bytes/history.','current_source_correction':'The authentic CultureBotHT raw definition instead names ten solutes, including explicit Cyanocobalamin, and has no listed phosphate or water row. W09 proposes correcting this existing owner, not refuting the separate NCMA formula.','new_current_comparison':'After that bounded correction, phosphate cannot remain the asserted differentiator from the CB active component list. Exact CB versus JCM/NBRC association is still not established: explicit cyanocobalamin versus generic B12, printed mg/L plus X metadata versus batch masses and water input, and distinct/unknown preparation scopes must remain visible. Missing detail proves neither same nor distinct substance.','scope':'Only the NBRC903 occurrence triggers this comparator correction; none of the six W08 occurrences is asserted to be a CultureBotHT occurrence.'},'duplicate_candidate_obligation':'W08 vm1201-prop-nbrc903-vitamin and W06 C-P-JCM197 are reconciliation inputs for a common nominal input recipe. Do not install two source-number owners, silently rewrite the W06 proposal, convert either null-before original into an existing-owner edit, or release the JCM197 exact alias by this source report.','CB_component_planning_readback':child_checks,'final_review_required':'The final composed owner, new genuine existing-owner dependency proposal and changed case must receive authorship-separated review of exact final bytes. This source assessor authored earlier W08 science and supplies no independent final approval.','preserved_holds':['All source, identity, role, owner, export and application holds remain.','Historical61 remains; unrecovered April58 identities do not block the bounded current-source correction.','Generic JCM/NBRC B12 and calcium-pantothenate form holds remain; no carrier is added to CB.','NCMA eleven-solute source remains positive; numeric water claim stays unsupported under already filed CONT-NCMA-WATER-001.','No exact NCMA, ATCC/MD-VS or shared-owner association is made. TV-001/TV-002/TV-004 remain unresolved.']})
save('findings.json',{'created_at':NOW,'author':AUTHOR,'new_findings':[],'existing_lineage_reconfirmed':[{'id':'TV-003','claim':'Unbridged NCMA active decomposition on authentic CB owner; bounded existing-owner source correction supported.'},{'id':'CONT-NCMA-WATER-001','claim':'Actual NCMA page gives eleven solutes per litre and unquantified distilled water; old numeric 1.0 L/L is unsupported.'}],'no_fixes_performed':True})
save('source-read-ledger.json',{'created_at':NOW,'author':AUTHOR,'read_method':'Actual local primary HTML text/tables and PDF text extraction; raw CSV block; frozen occurrence components/stock/preparation contexts; complete prior owner/candidate and source continuity appraisals. No new network calls.','entries':ledger,'limitations':['Primary access times are retained from original evidence and never restamped as new retrievals.','No live ontology database or network release lookup was repeated; supplied primary descriptor matrix and current owner hashes were inspected as bounded planning context.','W06 family cases and 84 hold objects are preserved context, not newly scientifically approved; this task reassesses six W08 occurrences.','Broad initial console dumps were truncated; substantive source/child/formulation fields were subsequently read in bounded chunks.'],'failed_attempts':[{'operation':'Initial BeautifulSoup import for local HTML rendering','result':'ModuleNotFoundError: bs4; no source result claimed. Recovered with Python standard-library HTMLParser.'},{'operation':'Read preflight issue1237-comment-6719499726.json','result':'Empty preserved failed original retrieval; not relied upon. Successful issue1237-comment-6719499726-network.json body was read instead.'}]})
save('validation.json',{'created_at':NOW,'status':'PASS' if all(x['passed'] for x in checks) else 'FAIL','checks':checks,'count':len(checks),'failures':sum(not x['passed'] for x in checks),'scope':'Read-only source/case/hash/quantity invariants; no candidate schema, scientific independence or application approval implied.'})
members={f.name:sha(f) for f in sorted(OUT.iterdir()) if f.is_file() and f.name!='HANDOFF.json'}
save('HANDOFF.json',{'created_at':NOW,'status':'COMPLETE_SOURCE_RESEARCH','author':AUTHOR,'independent_final_reviewer':False,'case_id':CASE,'occurrence_count':6,'primary_recipe_pages_read':8,'NCMA_primary_PDF_pages_read':1,'source_recipe_supported':True,'exact_CB_nominal_association_approved':False,'case_payload_or_maintained_writes':False,'new_findings':[],'files':members,'next':'Root may author the bounded composed CB source correction and dependent edit, preserving W09 contribution and all historic inputs; exact final independent review remains required.'})
print(json.dumps({'status':'complete','validation_failures':sum(not x['passed'] for x in checks),'checks':len(checks),'handoff':str(OUT/'HANDOFF.json'),'sha256':sha(OUT/'HANDOFF.json')}))
