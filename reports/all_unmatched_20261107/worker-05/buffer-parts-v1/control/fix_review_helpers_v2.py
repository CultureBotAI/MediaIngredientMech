from pathlib import Path
C=Path('.temp/w05-buffer-parts-v1/control')
p=C/'build_native_consolidated.py';s=p.read_text().replace('import argparse,json,hashlib,importlib.util,yaml','import argparse,json,hashlib,importlib.util,yaml,shlex')
start=s.index('checks=[dict(');end=s.index('\nreview=dict(',start)
s=s[:start]+'''checks=[dict(check_id='SCIENCE',name='Independent complete selected source and payload review',status='passed',required=True,summary='Non-command scientific judgment by the separately named reviewer, exact scope in PEER.',target_ids=ids,evidence_ids=['PEER'])]
for key,filename,name,es in [('ACCOUNTING','final-structural-audit.receipt.json','Exact frozen campaign accounting',['ACCOUNTING']),('LINEAGE','lineage.receipt.json','Original proposal lineage audit',['LINEAGE']),('OVERLAY','full-overlay.receipt.json','Guarded full payloads and complete substituted baseline',['NATIVE']),('STRICT','full-strict.receipt.json','Strict closed-schema complete payload checks',['STRICT']),('ROWS','consolidated-validation.receipt.json','Full native mapping projections and invariant assertions',['ROWS'])]:
 receipt=P/'validation'/filename;rc=j(receipt);assert rc['exit_code']==0
 evidence.append(dict(evidence_id=key+'-COMMAND',kind='validation',reference=str(receipt.relative_to(W)),snapshot_sha256=sha(receipt),accessed_at=at,support='supports',summary='Actual executable command, completion time and exit code.'))
 checks.append(dict(check_id=key,name=name,status='passed',required=True,command=shlex.join(rc['command']),exit_code=rc['exit_code'],expected_exit_code=0,summary='Actual command completed against the declared final selected bytes; no maintained or release approval.',target_ids=ids,evidence_ids=es+[key+'-COMMAND']))
# Reinspect after adding command-receipt dependencies so the native source binding covers them.
context += [str((P/'validation'/n).relative_to(W)) for n in ['final-structural-audit.receipt.json','lineage.receipt.json','full-overlay.receipt.json','full-strict.receipt.json','consolidated-validation.receipt.json']]
inspection=mod.inspect_source(W,targets,context)
''' +s[end:]
q=C/'build_native_consolidated_v2.py';assert not q.exists();q.write_text(s)
p=C/'write_final_reports.py';s=p.read_text();s=s.replace("'tris/primary-assessment.json'","'tris/source-assessment.json'").replace("'media/component-assessments-v2.json'","'media/component-assessments-v3.json'").replace("'parents/final/assessment.json'","'parents/primary-assessment.json','parents/selection-receipt.json','parents-direct-v1/scientific-plan.json','parents-direct-v1/author-receipt.json'")
s=s.replace(" if q.is_file():F['consolidated_successor']['scoped_bindings'].append(dict(path=rel,sha256=sha(q)))"," assert q.is_file(),('Missing required scope binding',rel)\n F['consolidated_successor']['scoped_bindings'].append(dict(path=rel,sha256=sha(q),scope='Historical and final assessment stages retain distinct authorship; canonical selected fragments determine the current payload.'))")
s=s.replace("['new-finding-before-fix.json','media-new-finding-v1.json','parents-new-finding-v1.json']","['new-finding-before-fix.json','media-new-finding-v1.json','parents-new-finding-v1.json','preliminary-helper-review-v1.json']")
q=C/'write_final_reports_v2.py';assert not q.exists();q.write_text(s)
print('W05-CONSOLIDATED-MECH-001/002 helper successors written; originals retained')
