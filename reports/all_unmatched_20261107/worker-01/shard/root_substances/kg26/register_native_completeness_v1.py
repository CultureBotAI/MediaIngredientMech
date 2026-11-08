import pathlib,json,hashlib,datetime
R=pathlib.Path('reports/all_unmatched_20261107/worker-01');O=R/'shard/root_substances/kg26';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();now=datetime.datetime.now(datetime.timezone.utc).isoformat().replace('+00:00','Z')
D=json.loads((O/'decisions.fragment.json').read_text());E=json.loads((O/'evidence.fragment.json').read_text());Q=json.loads((O/'proposals.fragment.json').read_text());indices=[166,167,170,171,172,175,182,183,186];cid=[d['case_id'] for d in D['decisions'] if d['allocation_index'] in indices]
urls={'selenate167-authoritative-web-v1':'https://www.fishersci.com/shop/products/sodium-selenate-decahydrate-99-9-metals-basis-thermo-scientific/AA1423922','selenate167-ols-parent-v1':'https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:77775','borate175-supplier-web-v1':'https://www.sigmaaldrich.com/US/en/product/sigald/s9640','borate175-structure-web-v1':'https://journals.iucr.org/e/issues/2008/05/00/wm2174/wm2174.pdf'}
for e in E['evidence']:
 if not e['evidence_id'].startswith('KG26-COMP-'):continue
 stem=pathlib.Path(e['capture']['path']).stem;p=R/e['capture']['path'];a=json.loads(p.read_text())
 if e['kind'] in ['current_owner_inspection','validation']:e['kind']='local_validation'
 if e['kind']=='search_result':e['kind']='ontology'
 if 'ols-' in stem and e['kind']=='primary_source':e['kind']='ontology'
 prov=p.with_suffix('.provenance.json')
 if not prov.exists():prov=p.with_name(p.stem+'.provenance.json')
 if prov.exists():m=json.loads(prov.read_text());e['url']=m.get('url');e['accessed_at']=m.get('retrieved_at',m.get('observed_at',e['accessed_at']))
 else:e['url']=urls.get(stem);e['accessed_at']=a.get('retrieved_at',a.get('at',e['accessed_at']))
 if e['kind'] in ['primary_source','ontology']:assert e['url'],stem
native=pathlib.Path('reviews/structured/20261108T043714Z-w01-kg-identity-proposals-author/review.yaml');copy=O/'captures/native-identity-author-review-v1.yaml';copy.write_bytes(native.read_bytes());eid='KG26-COMP-NATIVE-IDENTITY-V1';E['evidence'].append(dict(evidence_id=eid,kind='native_record_review',capture=dict(root='artifact',path=str(copy.relative_to(R)),sha256=sha(copy)),locator='Complete immutable native author batch review;9 proposed payloads,original owners and bound primary inputs',supports_or_contradicts='Sourceidentity/formulation self-review; strict9files0errors and proposedpartonomy0violations. Independent review and wholepublicationrelease stillrequired.',url=None,accessed_at=now,case_ids=cid))
for d in D['decisions']:
 if d['allocation_index'] in indices:d['evidence_ids'].append(eid)
for q in Q['proposals']:
 if q['proposal_id']!='KG26-PROP-163-NONNAMES':q['evidence_ids'].append(eid)
for n,a in [('decisions',D),('evidence',E),('proposals',Q)]: (O/(n+'.fragment.json')).write_text(json.dumps(a,indent=2,ensure_ascii=False)+'\n')
print('registered native review and normalized evidence contract')
