

# Slot: pubchem_cid 


_PubChem Compound Identifier (CID), stored as a positive integer. Populated by the PubChem enrichment path in `scripts/enrich_chemical_properties.py` when chemical properties are sourced from PubChem rather than ChEBI._





URI: [mediaingredientmech:pubchem_cid](https://w3id.org/mediaingredientmech/pubchem_cid)
Alias: pubchem_cid

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ChemicalProperties](ChemicalProperties.md) | Chemical structure and properties for CHEBI-mapped ingredients |  no  |






## Properties

* Range: [Integer](Integer.md)

* Minimum Value: 1




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:pubchem_cid |
| native | mediaingredientmech:pubchem_cid |




## LinkML Source

<details>
```yaml
name: pubchem_cid
description: PubChem Compound Identifier (CID), stored as a positive integer. Populated
  by the PubChem enrichment path in `scripts/enrich_chemical_properties.py` when chemical
  properties are sourced from PubChem rather than ChEBI.
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
alias: pubchem_cid
owner: ChemicalProperties
domain_of:
- ChemicalProperties
range: integer
minimum_value: 1

```
</details>