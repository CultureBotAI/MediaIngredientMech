"""Promote only two reviewed native-generator subject blocks, preserving other bytes."""
from pathlib import Path
import csv, hashlib, json, io, sys
RUN=Path(__file__).resolve().parents[1]
ROOT=RUN/'mim'
ALLOWED={
 'MIM:D-_-melezitose_Monohydrate': {('skos:broadMatch','CHEBI:6731'),('skos:exactMatch','cas:10030-67-8'),('skos:exactMatch','kgmicrobe.compound:d-_-melezitose_monohydrate')},
 'MIM:Carnitine_Hydrochloride': {('skos:broadMatch','CHEBI:17126'),('skos:exactMatch','kgmicrobe.compound:carnitine_hydrochloride')},
}
def sha(b): return hashlib.sha256(b).hexdigest()
def split(data):
 lines=data.decode().splitlines(keepends=True)
 start=next(i for i,x in enumerate(lines) if not x.startswith('#'))
 fields=next(csv.reader([lines[start]],delimiter='\t'))
 rows=list(csv.DictReader(lines[start:],delimiter='\t'))
 if len(rows)!=len(lines[start+1:]) or any(None in r or None in r.values() for r in rows): raise ValueError('Malformed TSV rows')
 return lines[:start+1],fields,list(zip(rows,lines[start+1:],strict=True))
def scoped(before,candidate,allowed):
 pre,fields,old=split(before);_,newfields,new=split(candidate)
 if fields!=newfields: raise ValueError('Generator columns differ')
 targets={s:[(r,line) for r,line in new if r['subject_id']==s] for s in allowed}
 for subject,wanted in allowed.items():
  actual=[(r['predicate_id'],r['object_id']) for r,_ in targets[subject]]
  if len(actual)!=len(wanted) or set(actual)!=wanted: raise ValueError('Missing, duplicate or unexpected native target rows: '+subject)
 seen=set();used=set();out=[]
 native={(subject,r['object_id']):(r,line) for subject,items in targets.items() for r,line in items}
 for row,line in old:
  sid=row['subject_id']
  if sid not in targets: out.append(line);continue
  key=(sid,row['object_id'])
  if key not in native or key in used: raise ValueError('Existing scoped row cannot be aligned without removal or duplication')
  native_row,native_line=native[key]
  if key==('MIM:Carnitine_Hydrochloride','CHEBI:17126'):
   # Retain this unadjudicated inherited alias; generator omission alone is
   # not a scientific decision about the unresolved salt/stereochemistry.
   if row.get('other')!='DL-carnitine|4-amino-2-hydroxy-N,N,N-trimethyl-4-oxobutan-1-aminium chloride' or native_row.get('other')!='': raise ValueError('Deferred DL-carnitine retention precondition changed')
   preserved=dict(native_row,other='DL-carnitine')
   stream=io.StringIO();writer=csv.DictWriter(stream,fieldnames=fields,delimiter='\t',lineterminator='\n');writer.writerow(preserved);native_line=stream.getvalue()
  out.append(native_line);used.add(key);seen.add(sid)
 if seen!=set(allowed): raise ValueError('A scoped subject was absent from canonical input')
 # Native rows that did not exist before append after every original position.
 # This preserves all frozen source-position bindings, including negative holds.
 out.extend(line for key,(row,line) in native.items() if key not in used)
 result=(''.join(pre)+''.join(out)).encode()
 _,_,after=split(result)
 if [(i,line) for i,(r,line) in enumerate(old,1) if r['subject_id'] not in allowed]!=[(i,line) for i,(r,line) in enumerate(after,1) if r['subject_id'] not in allowed]: raise ValueError('Unrelated row bytes or positions changed')
 return result

def self_check():
 header=b'# mapping_date: "2026-11-01"\nsubject_id\tpredicate_id\tobject_id\n'
 before=header+b'MIM:A\tskos:closeMatch\tCHEBI:1\nMIM:Other\tskos:exactMatch\tCHEBI:2\n'
 candidate=header+b'MIM:A\tskos:broadMatch\tCHEBI:1\nMIM:A\tskos:exactMatch\tkgmicrobe.compound:a\nMIM:Other\tskos:closeMatch\tCHEBI:999\n'
 allowed={'MIM:A':{('skos:broadMatch','CHEBI:1'),('skos:exactMatch','kgmicrobe.compound:a')}}
 result=scoped(before,candidate,allowed)
 assert result.splitlines(keepends=True)[3] == b'MIM:Other\tskos:exactMatch\tCHEBI:2\n'
 assert result.endswith(b'MIM:A\tskos:exactMatch\tkgmicrobe.compound:a\n')
 for bad in [header, candidate+candidate.splitlines(keepends=True)[2], candidate.replace(b'kgmicrobe.compound:a',b'kgmicrobe.ingredient:a')]:
  try: scoped(before,bad,allowed)
  except ValueError: pass
  else: raise AssertionError('Unsafe candidate accepted')
 header2=b'subject_id\tpredicate_id\tobject_id\tother\n'
 before2=header2+b'MIM:Carnitine_Hydrochloride\tskos:broadMatch\tCHEBI:17126\tDL-carnitine|4-amino-2-hydroxy-N,N,N-trimethyl-4-oxobutan-1-aminium chloride\n'
 native2=header2+b'MIM:Carnitine_Hydrochloride\tskos:broadMatch\tCHEBI:17126\t\n'
 retained=scoped(before2,native2,{'MIM:Carnitine_Hydrochloride':{('skos:broadMatch','CHEBI:17126')}})
 assert retained.endswith(b'\tDL-carnitine\n') and b'4-amino' not in retained
 return {'checks':['deferred DL-carnitine preserved while amide retired','unrelated row byte and position preservation','missing target refusal','duplicate target refusal','unexpected namespace refusal'],'passed':5}

if __name__=='__main__':
 tests=self_check()
 if sys.argv[1:]==['--self-check']:
  print(json.dumps(tests));raise SystemExit(0)
 if sys.argv[1:]!=['--apply']: raise SystemExit('Use --self-check or --apply')
 path=ROOT/'mappings/ingredient_mappings.sssom.tsv';candidate=ROOT/'output/sssom-scientific-audit/final.sssom.tsv'
 before=path.read_bytes();expected=(RUN/'provenance/baseline-canonical.sssom.tsv').read_bytes()
 if before!=expected: raise ValueError('Canonical input changed since sealed baseline')
 for r in json.loads((RUN/'audit901/combined-apply.json').read_text())['records']:
  if sha((ROOT/r['source_record']).read_bytes())!=r['after_yaml_sha256']: raise ValueError('Owner changed after guarded apply')
 generated=candidate.read_bytes();result=scoped(before,generated,ALLOWED)
 _,_,rows=split(result)
 for r,_ in rows:
  if r['subject_id'] in ALLOWED and r['predicate_id']=='skos:broadMatch' and 'CAS:10030-67-8' in r.get('other',''): raise ValueError('Hydrate CAS leaked onto parent')
  if r['subject_id'] in ALLOWED and '4-amino-2-hydroxy-N,N,N-trimethyl-4-oxobutan-1-aminium chloride' in r.get('other',''): raise ValueError('Rejected amide synonym remains')
 path.write_bytes(result)
 receipt={'generator_candidate':str(candidate.relative_to(ROOT)),'candidate_sha256':sha(generated),'before_sha256':sha(before),'after_sha256_before_header_bump':sha(result),'subjects':sorted(ALLOWED),'old_rows':len(split(before)[2]),'new_rows':len(rows),'unrelated_rows_preserved_byte_identical':len([r for r,_ in rows if r['subject_id'] not in ALLOWED]),'self_checks':tests}
 (RUN/'audit901/scoped-promotion.json').write_text(json.dumps(receipt,indent=2)+'\n')
 print(json.dumps(receipt,indent=2))
