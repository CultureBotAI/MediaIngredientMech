# Enum: IngredientGraphPredicateEnum 




_Closed edge vocabulary. `title` is the canonical label `predicate` must carry (RO labels as in ro.db). Allowed endpoint node types are enforced by the planned qc-causal-graphs gate; biolink_predicate is the planned KGX projection._



URI: [mediaingredientmech:IngredientGraphPredicateEnum](https://w3id.org/mediaingredientmech/IngredientGraphPredicateEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| BFO:0000051 | BFO:0000051 | a core relation that holds between a whole and its part |
| BFO:0000050 | BFO:0000050 | a core relation that holds between a part and its whole |
| rdfs:subClassOf | rdfs:subClassOf | RDFS subclass axiom: the subject class is a subclass of the object class (eve... |
| skos:broadMatch | skos:broadMatch | SKOS mapping relation: the object is a broader concept than the subject |
| RO:0018033 | RO:0018033 | A is a deprotonated form of B if and only if A is chemical entity that is a B... |
| RO:0018034 | RO:0018034 | A is a protonated form of B if and only if A is chemical entity that is a Brø... |
| RO:0018036 | RO:0018036 | Two chemicals are tautomers if they can be readily interconverted |
| RO:0002020 | RO:0002020 | Holds between p and c when p is a transport process or transporter activity a... |
| RO:0002233 | RO:0002233 | p has input c iff: p is a process, c is a material entity, c is a participant... |
| RO:0002234 | RO:0002234 | p has output c iff c is a participant in p, c is present at the end of p, and... |
| RO:0004009 | RO:0004009 | p has primary input c if (a) p has input c and (b) the goal of process is to ... |
| RO:0004008 | RO:0004008 | p has primary output c if (a) p has output c and (b) the goal of process is t... |
| RO:0002505 | RO:0002505 | p has intermediate c if and only if p has parts p1, p2 and p1 has output c, a... |
| RO:0000057 | RO:0000057 | a relation between a process and a continuant, in which the continuant is som... |
| RO:0000056 | RO:0000056 | a relation between a continuant and a process, in which the continuant is som... |
| RO:0002352 | RO:0002352 | inverse of has input |
| RO:0002353 | RO:0002353 | inverse of has output |
| RO:0002327 | RO:0002327 | c enables p iff c is capable of p and c acts to execute p |
| RO:0002326 | RO:0002326 | c contributes to p when c is part of some c' that is capable of p, and c is c... |
| RO:0002331 | RO:0002331 | c involved_in p if and only if c enables some process p', and p' is part of p |
| RO:0002224 | RO:0002224 | x starts with y if and only if x has part y and the time point at which x sta... |
| RO:0002230 | RO:0002230 | x ends with y if and only if x has part y and the time point at which x ends ... |
| RO:0001025 | RO:0001025 | a relation between two independent continuants, the target and the location, ... |
| RO:0002342 | RO:0002342 | Holds between p and m when p is a transportation or localization process and ... |
| RO:0002436 | RO:0002436 | An interaction relationship in which the two partners are molecular entities ... |
| RO:0000053 | RO:0000053 | Inverse of characteristic_of |
| MIM.vocab:satisfies_cofactor_requirement | None | Chemical to a ProteinTraitsMech COFACTOR_REQ_* record whose xrefs contain exa... |
| RO:0002411 | RO:0002411 | p is causally upstream of q iff p is causally related to q, the end of p prec... |
| RO:0002304 | RO:0002304 | p is causally upstream of, positive effect q iff p is casually upstream of q,... |
| RO:0002305 | RO:0002305 | p is causally upstream of, negative effect q iff p is casually upstream of q,... |
| RO:0002213 | RO:0002213 | p positively regulates q iff p regulates q, and p increases the rate or magni... |
| RO:0002212 | RO:0002212 | p negatively regulates q iff p regulates q, and p decreases the rate or magni... |
| RO:0012006 | RO:0012006 | a relation between a continuant and a process, in which the continuant is a s... |
| RO:0002566 | RO:0002566 | The entity or characteristic A is causally upstream of the entity or characte... |




## Slots

| Name | Description |
| ---  | --- |
| [predicate_id](predicate_id.md) |  |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech






## LinkML Source

<details>
```yaml
name: IngredientGraphPredicateEnum
description: Closed edge vocabulary. `title` is the canonical label `predicate` must
  carry (RO labels as in ro.db). Allowed endpoint node types are enforced by the planned
  qc-causal-graphs gate; biolink_predicate is the planned KGX projection.
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
permissible_values:
  BFO:0000051:
    text: BFO:0000051
    description: a core relation that holds between a whole and its part
    meaning: BFO:0000051
    annotations:
      biolink_predicate:
        tag: biolink_predicate
        value: biolink:has_part
      bridge_kinds:
        tag: bridge_kinds
        value: HYDRATE_PART ION_PART COMPONENT
    title: has part
  BFO:0000050:
    text: BFO:0000050
    description: a core relation that holds between a part and its whole
    meaning: BFO:0000050
    annotations:
      biolink_predicate:
        tag: biolink_predicate
        value: biolink:part_of
    title: part of
  rdfs:subClassOf:
    text: rdfs:subClassOf
    description: 'RDFS subclass axiom: the subject class is a subclass of the object
      class (every instance of the subject is an instance of the object).'
    meaning: rdfs:subClassOf
    annotations:
      biolink_predicate:
        tag: biolink_predicate
        value: biolink:subclass_of
      bridge_kinds:
        tag: bridge_kinds
        value: STRUCTURAL_FORM
    title: is a
  skos:broadMatch:
    text: skos:broadMatch
    description: 'SKOS mapping relation: the object is a broader concept than the
      subject. Restates the record''s own SSSOM skos:broadMatch row (FORM_OF_PARENT).'
    meaning: skos:broadMatch
    annotations:
      biolink_predicate:
        tag: biolink_predicate
        value: none
      bridge_kinds:
        tag: bridge_kinds
        value: FORM_OF_PARENT
    title: has broader match
  RO:0018033:
    text: RO:0018033
    description: A is a deprotonated form of B if and only if A is chemical entity
      that is a Brønsted–Lowry Base (i.e., can receive a proton) and by adding some
      nonzero number of protons transforms it into B.
    meaning: RO:0018033
    annotations:
      biolink_predicate:
        tag: biolink_predicate
        value: biolink:related_to
      bridge_kinds:
        tag: bridge_kinds
        value: PROTONATION
    title: is deprotonated form of
  RO:0018034:
    text: RO:0018034
    description: A is a protonated form of B if and only if A is chemical entity that
      is a Brønsted–Lowry Acid (i.e., can give up a proton) and by removing some nonzero
      number of protons transforms it into B.
    meaning: RO:0018034
    annotations:
      biolink_predicate:
        tag: biolink_predicate
        value: biolink:related_to
      bridge_kinds:
        tag: bridge_kinds
        value: PROTONATION
    title: is protonated form of
  RO:0018036:
    text: RO:0018036
    description: Two chemicals are tautomers if they can be readily interconverted.
    meaning: RO:0018036
    annotations:
      biolink_predicate:
        tag: biolink_predicate
        value: biolink:related_to
      bridge_kinds:
        tag: bridge_kinds
        value: TAUTOMER
    title: is tautomer of
  RO:0002020:
    text: RO:0002020
    description: Holds between p and c when p is a transport process or transporter
      activity and the outcome of this p is to move c from one location to another.
    meaning: RO:0002020
    annotations:
      biolink_predicate:
        tag: biolink_predicate
        value: biolink:affects
      object_aspect_qualifier:
        tag: object_aspect_qualifier
        value: transport
    title: transports
  RO:0002233:
    text: RO:0002233
    description: 'p has input c iff: p is a process, c is a material entity, c is
      a participant in p, c is present at the start of p, and the state of c is modified
      during p.'
    meaning: RO:0002233
    annotations:
      biolink_predicate:
        tag: biolink_predicate
        value: biolink:has_input
    title: has input
  RO:0002234:
    text: RO:0002234
    description: p has output c iff c is a participant in p, c is present at the end
      of p, and c is not present in the same state at the beginning of p.
    meaning: RO:0002234
    annotations:
      biolink_predicate:
        tag: biolink_predicate
        value: biolink:has_output
    title: has output
  RO:0004009:
    text: RO:0004009
    description: p has primary input c if (a) p has input c and (b) the goal of process
      is to modify, consume, or transform c.
    meaning: RO:0004009
    annotations:
      biolink_predicate:
        tag: biolink_predicate
        value: biolink:has_input
    title: has primary input
  RO:0004008:
    text: RO:0004008
    description: p has primary output c if (a) p has output c and (b) the goal of
      process is to modify, produce, or transform c.
    meaning: RO:0004008
    annotations:
      biolink_predicate:
        tag: biolink_predicate
        value: biolink:has_output
    title: has primary output
  RO:0002505:
    text: RO:0002505
    description: p has intermediate c if and only if p has parts p1, p2 and p1 has
      output c, and p2 has input c
    meaning: RO:0002505
    annotations:
      biolink_predicate:
        tag: biolink_predicate
        value: biolink:has_participant
    title: has intermediate
  RO:0000057:
    text: RO:0000057
    description: a relation between a process and a continuant, in which the continuant
      is somehow involved in the process
    meaning: RO:0000057
    annotations:
      biolink_predicate:
        tag: biolink_predicate
        value: biolink:has_participant
    title: has participant
  RO:0000056:
    text: RO:0000056
    description: a relation between a continuant and a process, in which the continuant
      is somehow involved in the process
    meaning: RO:0000056
    annotations:
      biolink_predicate:
        tag: biolink_predicate
        value: biolink:participates_in
    title: participates in
  RO:0002352:
    text: RO:0002352
    description: inverse of has input
    meaning: RO:0002352
    annotations:
      biolink_predicate:
        tag: biolink_predicate
        value: biolink:participates_in
    title: input of
  RO:0002353:
    text: RO:0002353
    description: inverse of has output
    meaning: RO:0002353
    annotations:
      biolink_predicate:
        tag: biolink_predicate
        value: biolink:participates_in
    title: output of
  RO:0002327:
    text: RO:0002327
    description: c enables p iff c is capable of p and c acts to execute p.
    meaning: RO:0002327
    annotations:
      biolink_predicate:
        tag: biolink_predicate
        value: biolink:enables
    title: enables
  RO:0002326:
    text: RO:0002326
    description: c contributes to p when c is part of some c' that is capable of p,
      and c is capable of some p' that is part of p (RO's editor note; RO gives no
      textual definition). In GO usage p is a molecular function.
    meaning: RO:0002326
    annotations:
      biolink_predicate:
        tag: biolink_predicate
        value: biolink:contributes_to
    title: contributes to
  RO:0002331:
    text: RO:0002331
    description: c involved_in p if and only if c enables some process p', and p'
      is part of p
    meaning: RO:0002331
    annotations:
      biolink_predicate:
        tag: biolink_predicate
        value: biolink:actively_involved_in
    title: involved in
  RO:0002224:
    text: RO:0002224
    description: 'x starts with y if and only if x has part y and the time point at
      which x starts is equivalent to the time point at which y starts. Formally:
      α(y) = α(x) ∧ ω(y) < ω(x), where α is a function that maps a process to a start
      point, and ω is a function that maps a process to an end point.'
    meaning: RO:0002224
    annotations:
      biolink_predicate:
        tag: biolink_predicate
        value: biolink:has_part
    title: starts with
  RO:0002230:
    text: RO:0002230
    description: 'x ends with y if and only if x has part y and the time point at
      which x ends is equivalent to the time point at which y ends. Formally: α(y)
      > α(x) ∧ ω(y) = ω(x), where α is a function that maps a process to a start point,
      and ω is a function that maps a process to an end point.'
    meaning: RO:0002230
    annotations:
      biolink_predicate:
        tag: biolink_predicate
        value: biolink:has_part
    title: ends with
  RO:0001025:
    text: RO:0001025
    description: a relation between two independent continuants, the target and the
      location, in which the target is entirely within the location
    meaning: RO:0001025
    annotations:
      biolink_predicate:
        tag: biolink_predicate
        value: biolink:located_in
    title: located in
  RO:0002342:
    text: RO:0002342
    description: Holds between p and m when p is a transportation or localization
      process and the outcome of this process is to move c from one location to another,
      and the route taken by c follows a path that crosses m.
    meaning: RO:0002342
    annotations:
      biolink_predicate:
        tag: biolink_predicate
        value: biolink:related_to
    title: results in transport across
  RO:0002436:
    text: RO:0002436
    description: An interaction relationship in which the two partners are molecular
      entities that directly physically interact with each other for example via a
      stable binding interaction or a brief interaction during which one modifies
      the other.
    meaning: RO:0002436
    annotations:
      biolink_predicate:
        tag: biolink_predicate
        value: biolink:physically_interacts_with
    title: molecularly interacts with
  RO:0000053:
    text: RO:0000053
    description: Inverse of characteristic_of
    meaning: RO:0000053
    annotations:
      biolink_predicate:
        tag: biolink_predicate
        value: biolink:has_attribute
    title: has characteristic
  MIM.vocab:satisfies_cofactor_requirement:
    text: MIM.vocab:satisfies_cofactor_requirement
    description: Chemical to a ProteinTraitsMech COFACTOR_REQ_* record whose xrefs
      contain exactly the chemical's grounding.
    annotations:
      biolink_predicate:
        tag: biolink_predicate
        value: biolink:related_to
    title: satisfies cofactor requirement
  RO:0002411:
    text: RO:0002411
    description: p is causally upstream of q iff p is causally related to q, the end
      of p precedes the end of q, and p is not an occurrent part of q.
    meaning: RO:0002411
    annotations:
      biolink_predicate:
        tag: biolink_predicate
        value: biolink:affects
    title: causally upstream of
  RO:0002304:
    text: RO:0002304
    description: p is causally upstream of, positive effect q iff p is casually upstream
      of q, and the execution of p is required for the execution of q.
    meaning: RO:0002304
    annotations:
      biolink_predicate:
        tag: biolink_predicate
        value: biolink:affects
    title: causally upstream of, positive effect
  RO:0002305:
    text: RO:0002305
    description: p is causally upstream of, negative effect q iff p is casually upstream
      of q, and the execution of p decreases the execution of q.
    meaning: RO:0002305
    annotations:
      biolink_predicate:
        tag: biolink_predicate
        value: biolink:affects
    title: causally upstream of, negative effect
  RO:0002213:
    text: RO:0002213
    description: p positively regulates q iff p regulates q, and p increases the rate
      or magnitude of execution of q.
    meaning: RO:0002213
    annotations:
      biolink_predicate:
        tag: biolink_predicate
        value: biolink:regulates
    title: positively regulates
  RO:0002212:
    text: RO:0002212
    description: p negatively regulates q iff p regulates q, and p decreases the rate
      or magnitude of execution of q.
    meaning: RO:0002212
    annotations:
      biolink_predicate:
        tag: biolink_predicate
        value: biolink:regulates
    title: negatively regulates
  RO:0012006:
    text: RO:0012006
    description: a relation between a continuant and a process, in which the continuant
      is a small molecule that inhibits the process
    meaning: RO:0012006
    annotations:
      biolink_predicate:
        tag: biolink_predicate
        value: biolink:affects
    title: is small molecule inhibitor of
  RO:0002566:
    text: RO:0002566
    description: The entity or characteristic A is causally upstream of the entity
      or characteristic B, A having an effect on B. An entity corresponds to any biological
      type of entity as long as a mass is measurable. A characteristic corresponds
      to a particular specificity of an entity (e.g., phenotype, shape, size).
    meaning: RO:0002566
    annotations:
      biolink_predicate:
        tag: biolink_predicate
        value: biolink:affects
    title: causally influences

```
</details>