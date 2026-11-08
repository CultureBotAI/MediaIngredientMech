import json,yaml,re,hashlib,datetime
from pathlib import Path
R=Path('reports/all_unmatched_20261107/worker-02'); C=R/'continuation-1201-v1/c'; A=json.loads((C/'assigned.json').read_text())['cases']
terms={130:['potassium sulfate','k2so4'],131:['copper sulfate','copper(ii) sulfate','cuso4'],132:['cherr'],133:['lipoprotein'],135:['ferrous','iron(2+) sulfate','feso4'],136:['nickel','nh42ni'],137:['magnesium sulfate','mgso4'],138:['ox bile','ox-bile','oxgall','bovine bile'],140:['manganese','mncl'],141:['copper sulfate','copper(ii) sulfate','cuso4'],142:['hexamethylene','polycarbonate'],144:['ferric','iron(3+) sulfate','fe2(so4)3','feso43'],147:['benzoate'],148:['pyruvate'],149:['mohr','ferrous ammonium','ammonium iron','fe(nh4)'],150:['formate','formiate'],151:['manganese sulfate','manganese(ii) sulfate','mnso4'],152:['calcium nitrate','ca(no3)'],153:['vanillate'],154:['ferrous','iron(2+) sulfate','feso4'],156:['mucin'],158:['copper nitrate','copper(ii) nitrate','cu(no3)'],159:['magnesium sulfate','mgso4'],160:['alum','alk(so4)'],161:['maltose'],164:['congocid','netropsin'],165:['cystein'],167:['vanadyl','vanadium(iv)','voso4'],168:['pyruvate'],169:['manganese sulfate','manganese(ii) sulfate','mnso4'],170:['butamine','dobutamine','butylamine'],171:['silicate','silicic'],172:['maltose'],173:['chaninin','chainin','isochainin'],175:['silicate','silicic'],176:['mohr','ferrous ammonium','ammonium iron','fe(nh4)'],177:['copper sulfate','copper(ii) sulfate','cuso4'],178:['magnesium nitrate','mg(no3)'],180:['emjh','leptospira','ellin'],181:['calcium sulfate','caso4'],182:['butamine','dobutamine','butylamine'],183:['ferric','iron(3+) sulfate','fe2(so4)3','feso43'],184:['manganese','mncl'],185:['vanadyl','vanadium(iv)','voso4'],186:['betaine'],187:['nickel','nh42ni']}
files=sorted(Path('data/ingredients').rglob('*.yaml')); corpus=[]
for p in files:
 b=p.read_bytes(); y=yaml.safe_load(b); corpus.append((p,b,y))
res=[]
for a in A:
 i=a['index']; hits=[]
 for p,b,y in corpus:
  labels=[y.get('preferred_term',''),y.get('identifier','')]+[s.get('synonym_text','') for s in y.get('synonyms',[])]
  # rglob traverses every matching path independently of Git ignore rules.
  if any(t in str(labels).lower() for t in terms[i]) or any(o['path']==str(p) for o in a['decision']['owner_records']):
   sha=hashlib.sha256(b).hexdigest(); dest=C/'owner-captures'/p.name;dest.parent.mkdir(exist_ok=True);dest.write_bytes(b)
   hits.append({'path':str(p),'sha256':sha,'identifier':y['identifier'],'preferred_term':y['preferred_term'],'mapping_status':y.get('mapping_status'),'labels':labels,'capture_path':str(dest.relative_to(R))})
 res.append({'index':i,'case_id':a['decision']['case_id'],'query_terms':terms[i],'searched_scope':'All data/ingredients/**/*.yaml via pathlib.rglob, including Git-ignored files; preferred_term/identifier/all synonym entries and explicitly inherited owner paths','files_examined':len(files),'matches':hits})
(C/'owner-lookup.json').write_text(json.dumps({'accessed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'lookups':res},indent=2)+'\n')
print('lookup cases',len(res),'files examined',len(files),'unique owners',len(list((C/'owner-captures').glob('*.yaml'))))
for x in res: print(x['index'],[(Path(m['path']).name,m['identifier'],m['mapping_status']) for m in x['matches']])
