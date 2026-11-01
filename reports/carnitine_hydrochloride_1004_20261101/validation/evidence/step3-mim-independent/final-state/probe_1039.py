from pathlib import Path
from datetime import datetime,timezone
import hashlib,importlib.util,json,sys
OUT=Path(__file__).resolve().parent;RUN=OUT.parents[1];MIM=RUN/'step3-mim'
raw=(MIM/'UNIFIED_INGREDIENT_MAPPING.tsv').read_bytes()
result={'checked_at':datetime.now(timezone.utc).isoformat(),'artifact_sha256':hashlib.sha256(raw).hexdigest(),'sources':{}}
for name,p in [('original',RUN/'step3-analyzer-1039/original/analyze_step3_final.py'),('fixed',RUN/'analyze_step3_final.py')]:
 s=importlib.util.spec_from_file_location('independent_parser_'+name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
 fields,rows=m.table(raw) if name=='original' else m.table(raw,format='plain')
 result['sources'][name]={'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'rows':len(rows),'occurrences':sum(int(r['occurrence_count']) for r in rows),'hash_prefixed':[r['ingredient_name'] for r in rows if r['ingredient_name'].startswith('#')]}
assert result['sources']['original']['rows']==4166 and result['sources']['original']['occurrences']==209323
assert result['sources']['fixed']['rows']==4170 and result['sources']['fixed']['occurrences']==209330
assert set(result['sources']['fixed']['hash_prefixed'])=={'#N2','#N2O','#argon','#Ar'}
assert result['sources']['fixed']['sha256']=='fb887535cc5f4e244d1830aa5576e74dc672535fe802fa786f18792e7e29926e'
result['production_bytes_unchanged']=hashlib.sha256((MIM/'UNIFIED_INGREDIENT_MAPPING.tsv').read_bytes()).hexdigest()==result['artifact_sha256'];assert result['production_bytes_unchanged']
(OUT/'1039-parser-proof.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
