import json,csv
from pathlib import Path
P=Path('reports/all_unmatched_20261107/worker-10');S=P/'successor-v1';D=json.loads((S/'decisions.json').read_text())['decisions'];PR=json.loads((S/'proposals.json').read_text())['proposals']
with (S/'case-index.tsv').open('w') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['index','case_id','source_label','disposition','proposal_ids','missing_fact','independent_review','review_evidence_ids'])
 for i,d in enumerate(D):w.writerow([i,d['case_id'],d['source']['source_label'],d['disposition'],';'.join(d['proposal_ids']),d.get('missing_requirement') or '',d['independent_review']['status'],';'.join(d['independent_review']['evidence_ids'])])
with (S/'proposal-index.tsv').open('w') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['proposal_id','case_ids','owner_path','kind','before_sha256','after_capture_path','after_sha256'])
 for p in PR:w.writerow([p['proposal_id'],';'.join(p['case_ids']),p['owner_path'],p['kind'],p['before_sha256'] or '',p['after_capture']['path'],p['after_capture']['sha256']])
print('indexes',len(D),len(PR))
