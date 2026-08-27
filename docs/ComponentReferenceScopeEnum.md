# Enum: ComponentReferenceScopeEnum 




_Resolution scope of a StockComponent.component_id._



URI: [mediaingredientmech:ComponentReferenceScopeEnum](https://w3id.org/mediaingredientmech/ComponentReferenceScopeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| MIM_CATALOG | None | The CURIE is the primary identifier of at least one active MIM record |
| EXTERNAL_TERM | None | The CURIE is a deliberate ontology or registry reference for which MIM has no... |
| UNMAPPED | None | The component is named but has no component_id |




## Slots

| Name | Description |
| ---  | --- |
| [reference_scope](reference_scope.md) | Resolution status and intended scope of component_id |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech






## LinkML Source

<details>
```yaml
name: ComponentReferenceScopeEnum
description: Resolution scope of a StockComponent.component_id.
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
permissible_values:
  MIM_CATALOG:
    text: MIM_CATALOG
    description: The CURIE is the primary identifier of at least one active MIM record.
      Because the catalog still has tracked duplicate-identifier families, this denotes
      the represented entity and is not guaranteed to select one physical YAML row.
  EXTERNAL_TERM:
    text: EXTERNAL_TERM
    description: The CURIE is a deliberate ontology or registry reference for which
      MIM has no active record; no local record is implied or fabricated.
  UNMAPPED:
    text: UNMAPPED
    description: The component is named but has no component_id.

```
</details>