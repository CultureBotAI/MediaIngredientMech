# `data/ingredients/mapped/Laminaribiose.yaml`

## Verdict

Needs curation. The CHEBI:18411 label, structure, reviewed synonym, and final
SSSOM row agree with each other, but the CAS-RN lookup needs curator review
because PubChem now resolves the record's CAS to a different InChIKey, and the
carbon-source role is still provisional.

## Identity

- Reviewed record: `data/ingredients/mapped/Laminaribiose.yaml`.
- Identifier and grounding: `identifier: CHEBI:18411` with
  `ontology_mapping.ontology_id: CHEBI:18411`, label `laminarabiose`, source
  `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `34980-39-7`, molecular formula `C12H22O11`,
  InChI, and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Lactose` through `Lanthanum_Iii_Chloride`: exited 0 and wrote zero ERROR
  rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Lactose.yaml data/ingredients/mapped/Lactulose.yaml data/ingredients/mapped/Laminaribiose.yaml data/ingredients/mapped/Laminarin_From_Laminaria_Digitata.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for the four CHEBI-primary records.

## Evidence

- EBI OLS4 resolves `CHEBI:18411` as active `laminarabiose`, lists
  `Laminaribiose` as a related synonym, lists CAS `34980-39-7`, and lists the
  same InChI as the YAML record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:18411`; its
  `other` field contains the reviewed IUPAC synonym plus `CAS:34980-39-7`.
- Major: the record was created from a CAS-RN lookup, but PubChem now resolves
  `34980-39-7` to CID `122350` with InChIKey
  `YGEHCIVVZVBCLE-CRLSIFLLSA-N`, while the YAML/ChEBI structure has InChIKey
  `QIGJYVCQYDKYDW-LCOYTZNXSA-N`. The CHEBI mapping may still be correct for
  the preferred term, but the CAS-derived evidence and final `CAS:34980-39-7`
  payload need an explicit source-of-truth decision.
- Major: `nutritional_roles.CARBON_SOURCE` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence from CHEBI ancestry through
  `CHEBI:16646` and says review is recommended.
- The hidden and ignored-inclusive search over `mappings/ingredient_mappings.sssom.tsv`,
  `data`, `src`, `tests`, `reports`, and `docs` found the current final SSSOM
  row and no sibling MIM record that would split the same laminaribiose
  identity.

## Completeness

- The active CHEBI identity, CHEBI formula, CHEBI structure, aggregate copy, and
  final SSSOM row are present.
- The CAS RN should not be treated as reviewed until the PubChem/ChEBI
  structural conflict is resolved.
- The provisional carbon-source role needs curation before it can be treated as
  a supported role assertion.

## Recommended Edits

- Major: resolve CAS RN `34980-39-7` against `CHEBI:18411` and PubChem CID
  `122350`; then either keep the current ChEBI grounding with reviewed CAS
  provenance, move the CAS value off this record, or remap if the CultureBotHT
  row denoted the PubChem CID instead.
- Major: either replace `nutritional_roles.CARBON_SOURCE` with inspected source
  evidence for exact laminaribiose use, or remove the provisional role.
- Sync the aggregate copy and regenerate final SSSOM after any YAML changes;
  rerun strict, term, product, component, and SSSOM validation.
