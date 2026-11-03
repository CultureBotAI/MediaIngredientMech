import pathlib,json,hashlib,csv,io,datetime,sys
D=pathlib.Path(__file__).resolve().parents[1];R=D/'independent-review';Q=D/(sys.argv[1] if len(sys.argv)>1 else 'comment-remediation-v1');sha=lambda b:hashlib.sha256(b).hexdigest();M=json.loads((Q/'proposal-manifest.json').read_text());expected=[]
for n,h in M['artifact_sha256'].items():assert sha((Q/n).read_bytes())==h
assert M['sequence']==25 and M['historical_prefix_count']==24 and M['canonical_changed_cells']==4
assert M['native_original_receipt25_reproduced'] and M['native_corrected25_chain_replayed']
def table(b):
 lines=b.decode().splitlines(keepends=True);headers=[x for x in lines if x.startswith('#')];r=csv.DictReader(io.StringIO(''.join(x for x in lines if not x.startswith('#'))),delimiter='\t');return headers,r.fieldnames,list(r)
a=(Q/'original-canonical.tsv').read_bytes();b=(Q/'canonical-proposal.sssom.tsv').read_bytes();ha,ca,aa=table(a);hb,cb,bb=table(b);assert ha==hb and ca==cb and len(aa)==len(bb)==3014
changes=json.loads((Q/'comment-corrections.json').read_text());actual=[]
for i,(x,y) in enumerate(zip(aa,bb),1):
 for c in ca:
  if x[c]!=y[c]:actual.append({'position':i,'subject_id':x['subject_id'],'object_id':x['object_id'],'column':c,'before':x[c],'after':y[c]})
assert len(actual)==4 and {x['column'] for x in actual}=={'comment'}
for x,c in zip(actual,changes):
 assert (x['position'],x['subject_id'],x['object_id'],x['before'],x['after'])==(c['output_position'],c['subject_id'],c['object_id'],c['before'],c['after'])
 assert c['after']==c['native_current_comment_verbatim']+' Historical/superseded parent context: '+c['historical_comment_verbatim']
 assert c['before']==c['historical_comment_verbatim']+' '+c['native_current_comment_verbatim']
ra=json.loads((Q/'original-receipt25.json').read_text());rb=json.loads((Q/'receipt25-proposal.json').read_text());assert [k for k in ra if ra[k]!=rb[k]]==['after_sha256','changes'];assert len(ra['changes'])==len(rb['changes'])==107
oldcfg=json.loads((Q/'original-projection-config.json').read_text());newcfg=json.loads((Q/'projection-config-v3.json').read_text());assert newcfg['schema_version']==3 and oldcfg['schema_version']==2
for o,n in zip(oldcfg['rows'],newcfg['rows'],strict=True):
 n=dict(n);n['output']=dict(n['output']);key=(o['output']['subject_id'],o['output']['object_id']);c=next((c for c in changes if(c['subject_id'],c['object_id'])==key),None)
 if c:
  assert n['output']['comment']==c['after'];n['output']['comment']=c['before']
 assert n==o
for k in oldcfg:
 if k not in {'schema_version','canonical_after_sha256','rows'}:assert oldcfg[k]==newcfg[k]
out={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'reviewer':'/root/step7d_independent_review','proposal':str(Q),'manifest_sha256':sha((Q/'proposal-manifest.json').read_bytes()),'canonical_before_sha256':sha(a),'canonical_after_sha256':sha(b),'receipt25_after_sha256':sha((Q/'receipt25-proposal.json').read_bytes()),'status':'Exact four-cell proposal comparison passed; execution guard control review and actual publication/final head remain required','cells':actual,'no_scientific_cell_header_row_order_or_count_change':True,'receipt_batch25_and_24_prefix_unchanged':True,'native_original_and_successor_receipt_replay_reported_in_frozen_receipt':True,'original_projection_config_preserved':True,'configuration_only_four_comments_plus_version_and_provenance_metadata':True,'findings':[],'final_head_approval':False}
p=R/(Q.name+'-independent-proposal-review.json');assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n');print(p,sha(p.read_bytes()))
