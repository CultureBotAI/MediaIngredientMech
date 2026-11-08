import json,difflib
from guarded_writer_v2 import *
w=Writer();receipts=[]
for pid,row in w.rows.items():
 p=w.prepare(pid);dest=O/'payloads-v2'/pathlib.Path(row['owner_path']).name; receipts.append(w.write(p,dest))
 d=''.join(difflib.unified_diff(p['old_bytes'].decode().splitlines(True),dest.read_text().splitlines(True),fromfile=row['current_payload']['path'],tofile=str(dest.relative_to(O))))
 out=O/'validation/diffs-v2'/f'{pid}.diff';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(d)
(O/'write-receipts-v2.json').write_text(json.dumps({'native_writer':'mediaingredientmech.validation.write_validated.write_validated_ingredient','native_history':'mediaingredientmech.curate.curation_event.record_curation_event','rows':receipts},indent=2)+'\n')
print(json.dumps([{k:r[k] for k in ['dependency_id','payload','history_prefix_preserved']} for r in receipts],indent=2))
