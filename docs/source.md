

# Slot: source 



URI: [mediaingredientmech:source](https://w3id.org/mediaingredientmech/source)
Alias: source

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IngredientSynonym](IngredientSynonym.md) | Alternative name or raw text variant for an ingredient |  no  |
| [ComponentEvidence](ComponentEvidence.md) | Evidence supporting an IngredientRecord |  no  |
| [StockComponent](StockComponent.md) | One constituent in an IngredientRecord |  no  |
| [MappingEvidence](MappingEvidence.md) | Evidence for an ontology mapping |  no  |
| [SourceOccurrence](SourceOccurrence.md) | An occurrence count attributed to a specific upstream source, with the source... |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:source |
| native | mediaingredientmech:source |




## LinkML Source

<details>
```yaml
name: source
alias: source
domain_of:
- MappingEvidence
- IngredientSynonym
- SourceOccurrence
- ComponentEvidence
- StockComponent
range: string

```
</details>