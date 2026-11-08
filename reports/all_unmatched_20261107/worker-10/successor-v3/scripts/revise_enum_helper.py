from pathlib import Path
p=Path('.temp/all-unmatched-worker-10/successor-v3/enum_successor.py');s=p.read_text()
s=s.replace('def guarded_new(record, dest):', '''def owner_preimage(proposal):
 path=R/proposal['owner_path']
 if proposal['before_sha256']:
  if path.is_symlink() or not path.is_file() or sha(path)!=proposal['before_sha256']:raise ValueError('stale authentic owner preimage')
  return yaml.safe_load(path.read_text())
 if path.exists():raise ValueError('new-owner destination already exists')
 return {}

def explicit_successor(oldpid, newpid, value, es, correspondences):
 matches=[c for c in correspondences if c['old_proposal_id']==oldpid and c['new_proposal_id']==newpid and c['before_claim']==value]
 if len(matches)!=1:raise ValueError('missing or ambiguous explicit complete-claim correspondence')
 c=matches[0];idx=c['successor_index']
 if idx>=len(es) or es[idx]!=c['after_claim']:raise ValueError('explicit successor claim differs')
 if es[idx].get('evidence_type')!='LLM_SUGGESTION':raise ValueError('source revised claim lacks honest agent type')
 return idx, c

def guarded_new(record, dest):''')
s=s.replace("for name,dest in [('outside-path'", """existing=next(p for p in base if p['before_sha256']); stale=copy.deepcopy(existing);stale['before_sha256']='0'*64
 try:owner_preimage(stale)
 except ValueError as e:out.append({'control':'stale-authentic-owner','refused':True,'reason':str(e)})
 else:raise AssertionError('stale authentic owner accepted')
 fake_es=[{'evidence_type':'LLM_SUGGESTION','source':'unrelated','notes':'unrelated'}]
 try:explicit_successor('old','new',r['full_value'],fake_es,[])
 except ValueError as e:out.append({'control':'unrelated-llm-claim-at-same-index','refused':True,'reason':str(e)})
 else:raise AssertionError('implicit correspondence accepted')
 for name,dest in [('outside-path'""")
s=s.replace("bypid=collections.defaultdict(list)", """correspondences=[]
 for c in load(S/'serums/mapping-claim-correspondence.json')['claims']:
  if c.get('before_claim') is not None and c.get('after_claim') is not None:
   correspondences.append(dict(c,successor_index=int(c['pointer'].rsplit('/',1)[1]),correspondence_capture={'path':'successor-v3/serums/mapping-claim-correspondence.json','sha256':sha(S/'serums/mapping-claim-correspondence.json')}))
 for entry in load(S/'hcl-manual/mapping-claim-correspondence.json')['entries']:
  for c in entry['claim_correspondences']:
   correspondences.append({'old_proposal_id':entry['original_proposal_id'],'new_proposal_id':entry['successor_proposal_id'],'before_claim':c['original_claim'],'after_claim':c['successor_claim'],'successor_index':c['successor_index'],'correspondence_capture':{'path':'successor-v3/hcl-manual/mapping-claim-correspondence.json','sha256':sha(S/'hcl-manual/mapping-claim-correspondence.json')}})
 bypid=collections.defaultdict(list)""")
s=s.replace("before=yaml.safe_load((R/p['owner_path']).read_text()) if p['before_sha256'] else {}", "before=owner_preimage(p)")
s=s.replace("es=d.get('ontology_mapping',{}).get('evidence',[]);v=row['full_value'];", "assert row['current_capture']==bp[oldpid]['after_capture'] and row['owner_path']==bp[oldpid]['owner_path'] and row['before_sha256']==bp[oldpid]['before_sha256'];assert sha(A/row['current_capture']['path'])==row['current_capture']['sha256'];owner_preimage(bp[oldpid]);es=d.get('ontology_mapping',{}).get('evidence',[]);v=row['full_value'];")
a="""idx=int(re.fullmatch(r'ontology_mapping.evidence\\[(\\d+)\\]',row['field']).group(1));assert idx<len(es),(oldpid,'missing explicit successor claim')
     successor=es[idx];assert successor.get('evidence_type')=='LLM_SUGGESTION',(oldpid,idx,'author must type revised claim honestly')"""
b="""idx,correspondence=explicit_successor(oldpid,p['proposal_id'],v,es,correspondences)
     successor=es[idx];disp['explicit_source_author_correspondence']=correspondence"""
assert a in s;s=s.replace(a,b).replace('# Bind its complete successor at the same explicit slot; no inference from a mere string match.','# Bind the source author explicit complete before/after correspondence, never an assumed index.')
p.write_text(s)
