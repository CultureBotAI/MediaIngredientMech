import pathlib,json,hashlib
O=pathlib.Path('.temp/peptone-final-dependencies-v1');old=(O/'author-plan.json').read_bytes(); d=json.loads(old)
row=next(r for r in d['rows'] if r['owner_path'].endswith('/Marine_agar_2216.yaml'))
assert row['new_component']['concentration_unit']=='G_PER_SOURCE_SCRATCH_FORMULA_BATCH'
oldtext='Preserve existing5.0G_PER_L as inherited nominal expression; do not infer final-volume standardization, dry-product fraction or chloramphenicol inheritance.'
newtext='Preserve the current W04 source-qualified5.0G_PER_SOURCE_SCRATCH_FORMULA_BATCH, all17 dry rows, PARTIAL scope,55.2520g-versus55.1g discrepancy and unresolved Magnesium Chloride form. Water1000mL remains preparation context, not an established final volume or dry-product component; do not infer lot fractions or chloramphenicol inheritance.'
for e in row['append_evidence']:
 assert oldtext in e['notes'];e['notes']=e['notes'].replace(oldtext,newtext)
assert oldtext in row['event_text'];row['event_text']=row['event_text'].replace(oldtext,newtext)
d['supersedes_draft_plan']={'path':'author-plan.json','sha256':hashlib.sha256(old).hexdigest(),'reason':'Before payload generation, current W04 source readback supersedes old baseline quantity wording in draft narrative. Actual planned component objects were already exact current source units. No payload had been generated.'}
(O/'author-plan-v2.json').write_text(json.dumps(d,indent=2)+'\n');print(hashlib.sha256((O/'author-plan-v2.json').read_bytes()).hexdigest())
