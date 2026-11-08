from pathlib import Path
from datetime import datetime, timezone
import json, yaml, hashlib, copy, difflib, sys
sys.path.insert(0,str(Path('src').resolve()))
from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.validation.write_validated import write_validated_ingredient
O=Path(__file__).resolve().parent
P=json.loads((O/'proposals-v1.json').read_text()); D=json.loads((O/'decisions-v1.json').read_text())
NOW=datetime.now(timezone.utc).isoformat(); AUTHOR='Codex worker05 /root/chemicals_research final report correction'
def sha(b): return hashlib.sha256(b).hexdigest()
def ref(p): return {'root':'artifact','path':'final-correction-v1/chemicals/'+str(p.relative_to(O)),'sha256':sha(p.read_bytes())}
def dump(n,x):
 p=O/n;assert not p.exists();p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
facts={
 'CHEM-C1193-ethanol95-atcc_1490':'Source-specific context: ATCC 1490 defines the vitamin K1 receiving stock with 0.15 ml vitamin K1 and 30 ml of nominal 95% ethanol. ATCC 1703 and 1539 explicitly reuse that recipe, represented by TOGO M2576, M2574 and M2618. The three routed occurrences remain together. These receiving-stock quantities do not define the percentage basis or balance of the supplied ethanol.',
 'CHEM-C1193-ethanol95-atcc_1257':'Source-specific context: ATCC 1257 ETSA, represented by TOGO M2568, lists 100 ml of nominal 95% ethanol in the hemin receiving stock and 50 ml in the menadione receiving stock. The separately added 100 ml and 50 ml water belong to those receiving stocks, not to the unidentified balance of the supplied ethanol. Preserve the one frozen occurrence and its two nested source uses; the flattened 150 g/L value is not a measured ethanol concentration.',
 'CHEM-C1193-ethanol95-atcc_1524':'Source-specific context: ATCC 1527 reproduces the ATCC 1524 vitamin K1 preparation, represented by TOGO M2724: 0.15 ml vitamin K1 and 30 ml nominal 95% ethanol. Preserve that one routed occurrence. This matches the stated receiving-stock inputs in ATCC 1490, while neither historical ethanol product identity nor percentage basis is established.',
 'CHEM-C1193-ethanol95-dsmz_78':'Source-specific context: DSMZ 78 defines vitamin K1 stock with 0.1 ml vitamin K1 and 20 ml nominal 95% ethanol; its vitamin K3 instructions dissolve menadione at 5 mg/ml in that ethanol and then dilute to 0.05 mg/ml with water. DSMZ 104 and 212a explicitly refer to medium 78 for K1. The captured current DSMZ 110 representation links the shared MediaDive K1 solution 125 and K3 solution 5540. Preserve all twelve routed occurrences and distinguish the subsequent K3 water dilution from the unspecified balance of supplied 95% ethanol.'
}
receipts=[]
for p in P:
 src=O/Path(p['after_capture']['path']).relative_to('final-correction-v1/chemicals'); before=src.read_bytes();assert sha(before)==p['after_capture']['sha256'];d=yaml.safe_load(before);old=copy.deepcopy(d)
 if p['proposal_id'] in facts:
  text=facts[p['proposal_id']];d['notes']+=' '+text
  record_curation_event(d,curator=AUTHOR,action='CORRECTED_REPORT_PROPOSAL',changes='Preserve the exact source-specific receiving-stock inputs and occurrence lineage alongside the conditional family assessment. This adds no percentage-basis, balance, distinctness or winning-owner inference.',previous_status=d['mapping_status'],new_status=d['mapping_status'],llm_assisted=True,llm_model='gpt-6',timestamp=NOW)
  p['description']+=' '+text
 dst=O/'proposed-v2'/src.name;assert not dst.exists();dst.parent.mkdir(exist_ok=True);write_validated_ingredient(d,dst,target_class='IngredientRecord');assert yaml.safe_load(dst.read_text())==d
 if d==old:dst.write_bytes(before)
 assert d['curation_history'][:len(old['curation_history'])]==old['curation_history']
 delta=O/'diffs-v2'/src.with_suffix('.diff').name;delta.parent.mkdir(exist_ok=True);delta.write_text(''.join(difflib.unified_diff(before.decode().splitlines(True),dst.read_text().splitlines(True),fromfile=str(src),tofile=str(dst))))
 p['final_correction']['v1_after_capture']=p['after_capture'];p['after_capture']=ref(dst);p['final_correction']['v2_diff']=ref(delta)
 receipts.append({'proposal_id':p['proposal_id'],'v1':ref(src),'v2':ref(dst),'changed':d!=old,'guarded_write':'PASS','roundtrip_equal':True,'history_prefix_preserved':True,'diff':ref(delta)})
D[6]['applicability']='This applies to the NaCOOH ingredient in TOGO M3211, Formate medium. Preserve the literal as a sodium-formate source alias, with the exact TOGO source locator. The previous Methanosarcina siciliae marine-medium title was erroneous and is superseded here; adjacent provider GMO enrichment is not independent reagent identification.'
for i in [13,25,65]:
 D[i]['applicability']='The stock composition is 10 mg thiamine HCl in 100 ml of 25 mM sodium phosphate buffer at pH 3.4. Filtration is explicit in NBRC 1321 and JCM 1125. JCM 403 does not explicitly state filtration of this stock; the JCM 1468 asterisk is unexplained. Preserve all four exact source lineages and receiving doses, without transferring preparation instructions between sources. This buffered stock is not the separate 0.2% TPP preparation or a neat thiamine salt. All identity and export holds remain.'
D[21]['applicability']='The six occurrences are duplicated recipe and solution representations of DSMZ 524 and 623, whose recipe texts specify 12 mg and 4 mg Na-meta silicate respectively. Those recipe texts do not specify supplier or hydration. Provider ingredient enrichment includes a CAS assignment, but that secondary metadata does not establish which historical reagent was used. No absent-hydration inference or exact anhydrous/hydrated mapping is authorized.'
D[18]['reasoning']+=' The two sources name a whole 1 M HEPES-KOH stock without enumerating material constituents. NEW-02 withdraws the inferred HEPES moiety and potassium-species material partonomy while preserving the useful nominal preparation description.'
D[26]['reasoning']+=' NEW-03 withdraws the inferred Tris-moiety and chloride-species material partonomy from both buffer candidates. The source-defined 1 M pH 7.5 and 0.5 M pH 8.0 specifications remain positive whole-preparation differences; no solvent, HCl input or neutralization ratio is inferred.'
D[26]['applicability']='The sixteen occurrences comprise seven weighed reagent contexts supporting Tris hydrochloride salt, six stock contexts specifying 1 M at pH 7.5, two stock contexts specifying 0.5 M at pH 8.0, and TOGO M2313 stating 50 mM at pH 7.8 in the receiving minimal medium. That last context does not define a separately prepared stock. Preserve all exact occurrence subsets. The filed #1238 grade correction applies only to the solid salt; NEW-03 separately withdraws unsupported material components from the two buffer candidates.'
dump('proposals-v2.json',P);dump('decisions-v2.json',D)
dump('payload-seal-v2.json',{'author':AUTHOR,'timestamp':NOW,'proposal_count':len(P),'case_count':len(D),'records':receipts,'files':{n:sha((O/n).read_bytes()) for n in ['proposals-v1.json','decisions-v1.json','proposals-v2.json','decisions-v2.json','evidence-v1.json']},'limitations':'Scientific read ledger and conditional matrix are separate additive files. Full independent review remains pending. No maintained data or projection gates were modified.'})
print(json.dumps({'counts':[len(D),len(P)],'files':{n:sha((O/n).read_bytes()) for n in ['proposals-v2.json','decisions-v2.json','payload-seal-v2.json']}}))
