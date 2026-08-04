

# Slot: component_name 


_Component ingredient name as listed in the recipe (e.g. "FeCl3 x 6 H2O")._





URI: [mediaingredientmech:component_name](https://w3id.org/mediaingredientmech/component_name)
Alias: component_name

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StockComponent](StockComponent.md) | One constituent of a stock solution or defined medium recipe — a component in... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [StockComponent](StockComponent.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [StockComponent](StockComponent.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:component_name |
| native | mediaingredientmech:component_name |




## LinkML Source

<details>
```yaml
name: component_name
description: Component ingredient name as listed in the recipe (e.g. "FeCl3 x 6 H2O").
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
alias: component_name
owner: StockComponent
domain_of:
- StockComponent
range: string
required: true

```
</details>