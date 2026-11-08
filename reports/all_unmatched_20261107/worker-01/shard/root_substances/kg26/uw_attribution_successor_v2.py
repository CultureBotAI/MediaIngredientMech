from pathlib import Path
import json,yaml,hashlib,sys,copy
sys.path.insert(0,str(Path('src').resolve()))
from mediaingredientmech.validation.write_validated import write_validated_ingredient
O=Path('reports/all_unmatched_20261107/worker-01/shard/root_substances/kg26');R=O.parents[2];C=O/'captures';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
m=json.loads((C/'uw-dependency-manifest-v1.json').read_text());qj=json.loads((O/'proposals.fragment.json').read_text());g=json.loads((C/'uw-dependency-guard-regression-v1.json').read_text());targets=yaml.safe_load((C/'uw-native-targets-v1.yaml').read_text())
for p in m['proposals']:
 src=R/p['after_capture']['path'];a=yaml.safe_load(src.read_text());assert a['curation_history'][-1]['curator']=='claude';a['curation_history'][-1]['curator']='worker01-uw-borax-dependency-curation';dst=src.with_name(src.name.replace('-v1','-v2'));assert not dst.exists();write_validated_ingredient(a,dst);p['after_capture']['path']=str(dst.relative_to(R));p['after_capture']['sha256']=sha(dst)
 q=next(x for x in qj['proposals'] if x['proposal_id']==p['proposal_id']);q['after_capture']=p['after_capture'];z=next(x for x in g['guards'] if x['owner_path']==p['owner_path']);z['after_path']=str(dst);z['after_sha256']=sha(dst);next(x for x in targets['targets'] if x['path']==str(src))['path']=str(dst)
g['attribution_successor']='New event names actual worker01 process; initial proposal bytes retained. Existing historical curator events unchanged.'
(C/'uw-dependency-manifest-v2.json').write_text(json.dumps(m,indent=2)+'\n');(C/'uw-dependency-guard-regression-v2.json').write_text(json.dumps(g,indent=2)+'\n');(C/'uw-native-targets-v2.yaml').write_text(yaml.safe_dump(targets,sort_keys=False));(O/'proposals.fragment.json').write_text(json.dumps(qj,indent=2,ensure_ascii=False)+'\n')
p=O/'evidence.fragment.json';e=json.loads(p.read_text());x=next(x for x in e['evidence'] if x['evidence_id']=='KG26-UW-GUARD-REGRESSION-V1');x['capture']['path']=str((C/'uw-dependency-guard-regression-v2.json').relative_to(R));x['capture']['sha256']=sha(C/'uw-dependency-guard-regression-v2.json');p.write_text(json.dumps(e,indent=2,ensure_ascii=False)+'\n')
s=(O/'native_uw_review_v1.py').read_text().replace('uw-dependency-manifest-v1','uw-dependency-manifest-v2').replace('uw-native-targets-v1','uw-native-targets-v2').replace('uw-dependency-guard-regression-v1','uw-dependency-guard-regression-v2').replace('uw-native-inspect-v1','uw-native-inspect-v2').replace('uw-native-author-review-v1','uw-native-author-review-v2').replace('uw-native-save-log-v1','uw-native-save-log-v2').replace("rp.write_text(yaml.safe_dump(review,sort_keys=False,allow_unicode=True))","rp.write_text(yaml.dump(review,Dumper=NoAlias,sort_keys=False,allow_unicode=True))")
s=s.replace("rp=C/'uw-native-author-review-v2.yaml'","class NoAlias(yaml.SafeDumper):\n def ignore_aliases(self,data):return True\nrp=C/'uw-native-author-review-v2.yaml'")
(O/'native_uw_review_v2.py').write_text(s)
