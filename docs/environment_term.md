

# Slot: environment_term 


_ENVO term CURIE (e.g. `ENVO:00000044` for peatland)_





URI: [mediaingredientmech:environment_term](https://w3id.org/mediaingredientmech/environment_term)
Alias: environment_term

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EnvironmentContext](EnvironmentContext.md) | Environmental context annotation for an ingredient |  no  |






## Properties

* Range: [String](String.md)

* Required: True

* Regex pattern: `^ENVO:\d{7,8}$`




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:environment_term |
| native | mediaingredientmech:environment_term |




## LinkML Source

<details>
```yaml
name: environment_term
description: ENVO term CURIE (e.g. `ENVO:00000044` for peatland)
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
alias: environment_term
owner: EnvironmentContext
domain_of:
- EnvironmentContext
range: string
required: true
pattern: ^ENVO:\d{7,8}$

```
</details>