

# Slot: ontology_mapping 


_Ontology term mapping (CHEBI/FOODON)_





URI: [mediaingredientmech:ontology_mapping](https://w3id.org/mediaingredientmech/ontology_mapping)
Alias: ontology_mapping

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IngredientRecord](IngredientRecord.md) | Core record for a media ingredient with ontology mapping, synonyms, and curat... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [OntologyMapping](OntologyMapping.md) |
| Domain Of | [IngredientRecord](IngredientRecord.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [IngredientRecord](IngredientRecord.md) |


<details>
<summary>Advanced Properties</summary>
**Term Bindings:**
- EnumBinding({
  'obligation_level': ObligationLevelEnum(text='REQUIRED', description='The metadata element is required to be present in the model'),
  'binds_value_of': 'ontology_id'
})

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:ontology_mapping |
| native | mediaingredientmech:ontology_mapping |




## LinkML Source

<details>
```yaml
name: ontology_mapping
description: Ontology term mapping (CHEBI/FOODON)
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
alias: ontology_mapping
owner: IngredientRecord
domain_of:
- IngredientRecord
range: OntologyMapping
bindings:
- obligation_level: REQUIRED
  binds_value_of: ontology_id

```
</details>