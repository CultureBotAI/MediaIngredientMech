

# Slot: xrefs 


_CURIEs denoting exactly this node's entity (e.g. the GO term an EC record maps to). Never the record identifier, a parent, or a related form: those are separate nodes joined by an edge._





URI: [mediaingredientmech:xrefs](https://w3id.org/mediaingredientmech/xrefs)
Alias: xrefs

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CausalNode](CausalNode.md) | A node in an ingredient mechanism graph |  no  |






## Properties

* Range: [String](String.md)

* Multivalued: True

* Regex pattern: `^[A-Za-z][A-Za-z0-9._-]*:[A-Za-z0-9._~-]+$`




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:xrefs |
| native | mediaingredientmech:xrefs |




## LinkML Source

<details>
```yaml
name: xrefs
description: 'CURIEs denoting exactly this node''s entity (e.g. the GO term an EC
  record maps to). Never the record identifier, a parent, or a related form: those
  are separate nodes joined by an edge.'
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
alias: xrefs
owner: CausalNode
domain_of:
- CausalNode
range: string
multivalued: true
pattern: ^[A-Za-z][A-Za-z0-9._-]*:[A-Za-z0-9._~-]+$

```
</details>