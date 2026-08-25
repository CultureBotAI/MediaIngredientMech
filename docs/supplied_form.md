

# Slot: supplied_form


_The material actually ordered and delivered for this ingredient — the thing on the shelf, as distinct from the substance the record denotes. Multivalued because one ingredient is legitimately buyable in several forms (anhydrous vs a hydrate, free acid vs sodium salt) and a recipe may not say which. Keeps procurement detail OUT of the identity: the `identifier` optimises for how the node reads in the knowledge graph, and this slot carries what you would put on a purchase order._





URI: [mediaingredientmech:supplied_form](https://w3id.org/mediaingredientmech/supplied_form)
Alias: supplied_form

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IngredientRecord](IngredientRecord.md) | Core record for a media ingredient with ontology mapping, synonyms, and curat... |  no  |






## Properties

* Range: [SuppliedForm](SuppliedForm.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:supplied_form |
| native | mediaingredientmech:supplied_form |




## LinkML Source

<details>
```yaml
name: supplied_form
description: 'The material actually ordered and delivered for this ingredient — the
  thing on the shelf, as distinct from the substance the record denotes. Multivalued
  because one ingredient is legitimately buyable in several forms (anhydrous vs a
  hydrate, free acid vs sodium salt) and a recipe may not say which. Keeps procurement
  detail OUT of the identity: the `identifier` optimises for how the node reads in
  the knowledge graph, and this slot carries what you would put on a purchase order.'
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
alias: supplied_form
owner: IngredientRecord
domain_of:
- IngredientRecord
range: SuppliedForm
multivalued: true
inlined: true
inlined_as_list: true

```
</details>