"""Qualify one existing literature citation as context under filed #718."""
from copy import deepcopy
from html.parser import HTMLParser
import hashlib,json,sys
from pathlib import Path
W=Path(__file__).resolve().parents[4];sys.path.insert(0,str(W/'src'))
import yaml
from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.curate.publication_guard import FrozenFile
from mediaingredientmech.ingredient_bundle_refresh import publish_new_files
from mediaingredientmech.validation.write_validated import write_validated_ingredient
R=Path(__file__).resolve().parent;A=R.parent;O=W/'.temp/w02-final-corrections-v1';OUT=R/'water'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x):
 p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('x') as f:json.dump(x,f,indent=2,ensure_ascii=False);f.write('\n')
def cap(p):return {'root':'artifact','path':str(p.relative_to(A)),'sha256':sha(p)}
def main():
 OUT.mkdir(exist_ok=False)
 ledger=A/'continuation-1201-v1/proposals.json';props=json.loads(ledger.read_text())['proposals'];old=next(p for p in props if p['proposal_id']=='a2-proposal-water-source-quality-provenance')
 source=A/old['after_capture']['path'];preimage=W/old['owner_path'];assert sha(source)==old['after_capture']['sha256'] and sha(preimage)==old['before_sha256']
 original=O/'frozen-w04-review/science/reviewer-b/captures/pmc9569759-html.body';receipt=original.with_suffix('.receipt.json');meta=json.loads(receipt.read_text());assert sha(original)==meta['sha256']
 frozen=[FrozenFile.capture(p) for p in [ledger,source,preimage,original,receipt]]
 record=yaml.safe_load(source.read_text());oldentry=deepcopy(record['ontology_mapping']['evidence'][1]);assert oldentry['pmid']=='36233206' and oldentry['supports']=='SUPPORT'
 class Text(HTMLParser):
  def __init__(self):super().__init__();self.text=[]
  def handle_data(self,data):self.text.append(data)
 parsed=Text();parsed.feed(original.read_text());content=' '.join(' '.join(parsed.text).split());assert oldentry['snippet'] in content
 claim='The cited article uses distilled water as a negative-control vehicle in the fish-collagen mouse experiment (abstract and animal methods). This is a genuine contextual mention, not evidence establishing this MIM molecular-water grounding, interchangeability of water preparations, or a microbial functional role. The original automatic citation and snippet are retained; exact-owner and role support are withheld.'
 record['ontology_mapping']['evidence'][1]['supports']='PARTIAL';record['ontology_mapping']['evidence'][1]['explanation']=claim
 record_curation_event(record,curator='worker02 /root',action='CORRECTED',changes='Under #718, qualify PMID36233206 as adjacent literature context (PARTIAL), preserving the genuine snippet, citation, LITERATURE type and all previous history. No water identity, quality, synonym or role is changed or approved.',llm_assisted=True)
 copied=OUT/'captures/PMC9569759.html';copied.parent.mkdir(parents=True,exist_ok=True)
 with copied.open('xb') as f:f.write(original.read_bytes())
 with (OUT/'captures/original-retrieval-receipt.json').open('xb') as f:f.write(receipt.read_bytes())
 stage=O/'water-stage/Distilled_Water.yaml';stage.parent.mkdir(parents=True,exist_ok=True);assert not stage.exists();write_validated_ingredient(record,stage)
 dest=OUT/'after/Distilled_Water.yaml';dest.parent.mkdir(parents=True,exist_ok=True)
 def verify():
  for s in frozen:s.verify()
 publish_new_files([(dest,stage.read_bytes())],verify);verify()
 eid='w02-final-water-contextual-literature';proposal=deepcopy(old);proposal['after_capture']=cap(dest);proposal['evidence_ids'].append(eid);proposal['description']+=' PMID36233206 remains genuine contextual literature only; its support is PARTIAL, with no exact-owner or role validation.'
 proposal['mapping_consequence']='No identity, grounding, preferred-label, synonym or role change. Qualify only adjacent literature applicability; all quality/source/whole-owner/export holds remain.'
 evidence={'evidence_id':eid,'kind':'primary_source','capture':cap(copied),'url':meta['url'],'accessed_at':meta['started_at'],'locator':'PMID36233206/PMC9569759 abstract and animal-experiment methods; complete original HTML retained','supports_or_contradicts':claim,'case_ids':old['case_ids'],'original_capturer':'W04 /root/reviewer-b','current_assessor':'worker02 /root'}
 save(OUT/'citation-disposition.json',{'author':'worker02 /root','old_after_capture':old['after_capture'],'complete_new_after_capture':proposal['after_capture'],'old_entry':oldentry,'new_entry':record['ontology_mapping']['evidence'][1],'primary_capture':cap(copied),'issue':'https://github.com/CultureBotAI/MediaIngredientMech/issues/718','scope':claim,'other_fields_unchanged_except_appended_history':True,'independent_review':'pending'})
 save(OUT/'fragments.json',{'author':'worker02 /root','decisions':[],'proposals':[proposal],'evidence':[evidence],'superseded_proposal_ids':[],'proposal_authors':{old['proposal_id']:['worker02 /root']}})
 print(json.dumps({'proposals':1,'contextual_literature_entries':1,'owner_sha256':sha(dest)}))
if __name__=='__main__':main()
