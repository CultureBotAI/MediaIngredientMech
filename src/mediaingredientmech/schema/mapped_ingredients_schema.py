# Auto generated from mapped_ingredients_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-03-22T20:03:03
# Schema: mapped-ingredients-schema
#
# id: https://w3id.org/culturemech/mapped-ingredients
# description: LinkML schema for aggregating successfully mapped media ingredients with proper ontology terms. This provides statistics and tracking for ingredients that have been successfully mapped to ontology terms (CHEBI, FOODON, etc.).
# license: MIT

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Datetime, Float, Integer, String
from linkml_runtime.utils.metamodelcore import XSDDateTime

metamodel_version = "1.7.0"
version = None

# Namespaces
CHEBI = CurieNamespace('CHEBI', 'http://purl.obolibrary.org/obo/CHEBI_')
ENVO = CurieNamespace('ENVO', 'http://purl.obolibrary.org/obo/ENVO_')
FOODON = CurieNamespace('FOODON', 'http://purl.obolibrary.org/obo/FOODON_')
CULTUREMECH = CurieNamespace('culturemech', 'https://w3id.org/culturemech/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = CULTUREMECH


# Types

# Class references
class MappedIngredientPreferredTerm(extended_str):
    pass


@dataclass(repr=False)
class MappedIngredientsCollection(YAMLRoot):
    """
    Root container for all successfully mapped media ingredients
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CULTUREMECH["MappedIngredientsCollection"]
    class_class_curie: ClassVar[str] = "culturemech:MappedIngredientsCollection"
    class_name: ClassVar[str] = "MappedIngredientsCollection"
    class_model_uri: ClassVar[URIRef] = CULTUREMECH.MappedIngredientsCollection

    generation_date: Optional[Union[str, XSDDateTime]] = None
    total_mapped_count: Optional[int] = None
    total_instances: Optional[int] = None
    media_count: Optional[int] = None
    mapped_ingredients: Optional[Union[dict[Union[str, MappedIngredientPreferredTerm], Union[dict, "MappedIngredient"]], list[Union[dict, "MappedIngredient"]]]] = empty_dict()
    summary_by_category: Optional[Union[Union[dict, "MappedCategorySummary"], list[Union[dict, "MappedCategorySummary"]]]] = empty_list()
    summary_by_ontology: Optional[Union[Union[dict, "OntologySummary"], list[Union[dict, "OntologySummary"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.generation_date is not None and not isinstance(self.generation_date, XSDDateTime):
            self.generation_date = XSDDateTime(self.generation_date)

        if self.total_mapped_count is not None and not isinstance(self.total_mapped_count, int):
            self.total_mapped_count = int(self.total_mapped_count)

        if self.total_instances is not None and not isinstance(self.total_instances, int):
            self.total_instances = int(self.total_instances)

        if self.media_count is not None and not isinstance(self.media_count, int):
            self.media_count = int(self.media_count)

        self._normalize_inlined_as_list(slot_name="mapped_ingredients", slot_type=MappedIngredient, key_name="preferred_term", keyed=True)

        if not isinstance(self.summary_by_category, list):
            self.summary_by_category = [self.summary_by_category] if self.summary_by_category is not None else []
        self.summary_by_category = [v if isinstance(v, MappedCategorySummary) else MappedCategorySummary(**as_dict(v)) for v in self.summary_by_category]

        if not isinstance(self.summary_by_ontology, list):
            self.summary_by_ontology = [self.summary_by_ontology] if self.summary_by_ontology is not None else []
        self.summary_by_ontology = [v if isinstance(v, OntologySummary) else OntologySummary(**as_dict(v)) for v in self.summary_by_ontology]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MappedIngredient(YAMLRoot):
    """
    A media ingredient with proper ontology mapping
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CULTUREMECH["MappedIngredient"]
    class_class_curie: ClassVar[str] = "culturemech:MappedIngredient"
    class_name: ClassVar[str] = "MappedIngredient"
    class_model_uri: ClassVar[URIRef] = CULTUREMECH.MappedIngredient

    preferred_term: Union[str, MappedIngredientPreferredTerm] = None
    ontology_id: Optional[str] = None
    ontology_label: Optional[str] = None
    ontology_source: Optional[Union[str, "OntologySourceEnum"]] = None
    occurrence_count: Optional[int] = None
    media_occurrences: Optional[Union[Union[dict, "MappedMediaOccurrence"], list[Union[dict, "MappedMediaOccurrence"]]]] = empty_list()
    concentration_info: Optional[Union[Union[dict, "MappedConcentrationInfo"], list[Union[dict, "MappedConcentrationInfo"]]]] = empty_list()
    synonyms: Optional[Union[str, list[str]]] = empty_list()
    mapping_quality: Optional[Union[str, "MappingQualityEnum"]] = None
    environmental_context: Optional[Union[Union[dict, "EnvironmentContext"], list[Union[dict, "EnvironmentContext"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.preferred_term):
            self.MissingRequiredField("preferred_term")
        if not isinstance(self.preferred_term, MappedIngredientPreferredTerm):
            self.preferred_term = MappedIngredientPreferredTerm(self.preferred_term)

        if self.ontology_id is not None and not isinstance(self.ontology_id, str):
            self.ontology_id = str(self.ontology_id)

        if self.ontology_label is not None and not isinstance(self.ontology_label, str):
            self.ontology_label = str(self.ontology_label)

        if self.ontology_source is not None and not isinstance(self.ontology_source, OntologySourceEnum):
            self.ontology_source = OntologySourceEnum(self.ontology_source)

        if self.occurrence_count is not None and not isinstance(self.occurrence_count, int):
            self.occurrence_count = int(self.occurrence_count)

        if not isinstance(self.media_occurrences, list):
            self.media_occurrences = [self.media_occurrences] if self.media_occurrences is not None else []
        self.media_occurrences = [v if isinstance(v, MappedMediaOccurrence) else MappedMediaOccurrence(**as_dict(v)) for v in self.media_occurrences]

        if not isinstance(self.concentration_info, list):
            self.concentration_info = [self.concentration_info] if self.concentration_info is not None else []
        self.concentration_info = [v if isinstance(v, MappedConcentrationInfo) else MappedConcentrationInfo(**as_dict(v)) for v in self.concentration_info]

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        if self.mapping_quality is not None and not isinstance(self.mapping_quality, MappingQualityEnum):
            self.mapping_quality = MappingQualityEnum(self.mapping_quality)

        if not isinstance(self.environmental_context, list):
            self.environmental_context = [self.environmental_context] if self.environmental_context is not None else []
        self.environmental_context = [v if isinstance(v, EnvironmentContext) else EnvironmentContext(**as_dict(v)) for v in self.environmental_context]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EnvironmentContext(YAMLRoot):
    """
    Environmental context annotation for a mapped ingredient. Links an ingredient to an ENVO environment with a
    relevance qualifier explaining why the ingredient is associated with that environment.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CULTUREMECH["EnvironmentContext"]
    class_class_curie: ClassVar[str] = "culturemech:EnvironmentContext"
    class_name: ClassVar[str] = "EnvironmentContext"
    class_model_uri: ClassVar[URIRef] = CULTUREMECH.EnvironmentContext

    environment_term: str = None
    relevance: Union[str, "EnvironmentRelevanceEnum"] = None
    environment_label: Optional[str] = None
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.environment_term):
            self.MissingRequiredField("environment_term")
        if not isinstance(self.environment_term, str):
            self.environment_term = str(self.environment_term)

        if self._is_empty(self.relevance):
            self.MissingRequiredField("relevance")
        if not isinstance(self.relevance, EnvironmentRelevanceEnum):
            self.relevance = EnvironmentRelevanceEnum(self.relevance)

        if self.environment_label is not None and not isinstance(self.environment_label, str):
            self.environment_label = str(self.environment_label)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MappedMediaOccurrence(YAMLRoot):
    """
    Reference to a specific medium containing the mapped ingredient
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CULTUREMECH["MappedMediaOccurrence"]
    class_class_curie: ClassVar[str] = "culturemech:MappedMediaOccurrence"
    class_name: ClassVar[str] = "MappedMediaOccurrence"
    class_model_uri: ClassVar[URIRef] = CULTUREMECH.MappedMediaOccurrence

    medium_name: str = None
    medium_category: Optional[Union[str, "MediaCategoryEnum"]] = None
    medium_file_path: Optional[str] = None
    ingredient_index: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.medium_name):
            self.MissingRequiredField("medium_name")
        if not isinstance(self.medium_name, str):
            self.medium_name = str(self.medium_name)

        if self.medium_category is not None and not isinstance(self.medium_category, MediaCategoryEnum):
            self.medium_category = MediaCategoryEnum(self.medium_category)

        if self.medium_file_path is not None and not isinstance(self.medium_file_path, str):
            self.medium_file_path = str(self.medium_file_path)

        if self.ingredient_index is not None and not isinstance(self.ingredient_index, int):
            self.ingredient_index = int(self.ingredient_index)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MappedConcentrationInfo(YAMLRoot):
    """
    Concentration information for a mapped ingredient
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CULTUREMECH["MappedConcentrationInfo"]
    class_class_curie: ClassVar[str] = "culturemech:MappedConcentrationInfo"
    class_name: ClassVar[str] = "MappedConcentrationInfo"
    class_model_uri: ClassVar[URIRef] = CULTUREMECH.MappedConcentrationInfo

    value: Optional[str] = None
    unit: Optional[Union[str, "ConcentrationUnitEnum"]] = None
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        if self.unit is not None and not isinstance(self.unit, ConcentrationUnitEnum):
            self.unit = ConcentrationUnitEnum(self.unit)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MappedCategorySummary(YAMLRoot):
    """
    Summary statistics for mapped ingredients in a media category
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CULTUREMECH["MappedCategorySummary"]
    class_class_curie: ClassVar[str] = "culturemech:MappedCategorySummary"
    class_name: ClassVar[str] = "MappedCategorySummary"
    class_model_uri: ClassVar[URIRef] = CULTUREMECH.MappedCategorySummary

    category: Union[str, "MediaCategoryEnum"] = None
    media_with_mapped: Optional[int] = None
    total_mapped_instances: Optional[int] = None
    unique_mapped_count: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, MediaCategoryEnum):
            self.category = MediaCategoryEnum(self.category)

        if self.media_with_mapped is not None and not isinstance(self.media_with_mapped, int):
            self.media_with_mapped = int(self.media_with_mapped)

        if self.total_mapped_instances is not None and not isinstance(self.total_mapped_instances, int):
            self.total_mapped_instances = int(self.total_mapped_instances)

        if self.unique_mapped_count is not None and not isinstance(self.unique_mapped_count, int):
            self.unique_mapped_count = int(self.unique_mapped_count)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OntologySummary(YAMLRoot):
    """
    Summary statistics by ontology source
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CULTUREMECH["OntologySummary"]
    class_class_curie: ClassVar[str] = "culturemech:OntologySummary"
    class_name: ClassVar[str] = "OntologySummary"
    class_model_uri: ClassVar[URIRef] = CULTUREMECH.OntologySummary

    ontology_source: Union[str, "OntologySourceEnum"] = None
    unique_terms_count: Optional[int] = None
    total_instances: Optional[int] = None
    coverage_percentage: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ontology_source):
            self.MissingRequiredField("ontology_source")
        if not isinstance(self.ontology_source, OntologySourceEnum):
            self.ontology_source = OntologySourceEnum(self.ontology_source)

        if self.unique_terms_count is not None and not isinstance(self.unique_terms_count, int):
            self.unique_terms_count = int(self.unique_terms_count)

        if self.total_instances is not None and not isinstance(self.total_instances, int):
            self.total_instances = int(self.total_instances)

        if self.coverage_percentage is not None and not isinstance(self.coverage_percentage, float):
            self.coverage_percentage = float(self.coverage_percentage)

        super().__post_init__(**kwargs)


# Enumerations
class MappingQualityEnum(EnumDefinitionImpl):

    DIRECT_MATCH = PermissibleValue(
        text="DIRECT_MATCH",
        description="Direct match to ontology term")
    SYNONYM_MATCH = PermissibleValue(
        text="SYNONYM_MATCH",
        description="Matched via synonym")
    INFERRED = PermissibleValue(
        text="INFERRED",
        description="Mapping inferred from context")
    MANUAL_CURATION = PermissibleValue(
        text="MANUAL_CURATION",
        description="Manually curated mapping")
    NEEDS_REVIEW = PermissibleValue(
        text="NEEDS_REVIEW",
        description="Mapping needs expert review")

    _defn = EnumDefinition(
        name="MappingQualityEnum",
    )

class MediaCategoryEnum(EnumDefinitionImpl):

    ALGAE = PermissibleValue(
        text="ALGAE",
        description="Algae culture media")
    BACTERIAL = PermissibleValue(
        text="BACTERIAL",
        description="Bacterial culture media")
    ARCHAEA = PermissibleValue(
        text="ARCHAEA",
        description="Archaea culture media")
    FUNGAL = PermissibleValue(
        text="FUNGAL",
        description="Fungal culture media")
    SPECIALIZED = PermissibleValue(
        text="SPECIALIZED",
        description="Specialized or mixed culture media")
    UNKNOWN = PermissibleValue(
        text="UNKNOWN",
        description="Category not specified")

    _defn = EnumDefinition(
        name="MediaCategoryEnum",
    )

class ConcentrationUnitEnum(EnumDefinitionImpl):

    G_PER_L = PermissibleValue(
        text="G_PER_L",
        description="Grams per liter")
    MG_PER_L = PermissibleValue(
        text="MG_PER_L",
        description="Milligrams per liter")
    UG_PER_L = PermissibleValue(
        text="UG_PER_L",
        description="Micrograms per liter")
    MOLAR = PermissibleValue(
        text="MOLAR",
        description="Molar concentration")
    MILLIMOLAR = PermissibleValue(
        text="MILLIMOLAR",
        description="Millimolar concentration")
    MICROMOLAR = PermissibleValue(
        text="MICROMOLAR",
        description="Micromolar concentration")
    PERCENT = PermissibleValue(
        text="PERCENT",
        description="Percentage (w/v or v/v)")
    VARIABLE = PermissibleValue(
        text="VARIABLE",
        description="Variable or unspecified amount")

    _defn = EnumDefinition(
        name="ConcentrationUnitEnum",
    )

class EnvironmentRelevanceEnum(EnumDefinitionImpl):
    """
    Describes why an ingredient is relevant to a particular environment.
    """
    NATURAL_SOURCE = PermissibleValue(
        text="NATURAL_SOURCE",
        description="Ingredient is naturally found in or sourced from this environment")
    REQUIRED_FOR_ORGANISM = PermissibleValue(
        text="REQUIRED_FOR_ORGANISM",
        description="Required for cultivating organisms from this environment")
    SELECTIVE_AGENT = PermissibleValue(
        text="SELECTIVE_AGENT",
        description="Selectively promotes growth of organisms from this environment")
    ENVIRONMENT_MIMIC = PermissibleValue(
        text="ENVIRONMENT_MIMIC",
        description="Helps replicate the chemical conditions of this environment in vitro")
    COMMONLY_USED = PermissibleValue(
        text="COMMONLY_USED",
        description="Commonly used in media targeting organisms from this environment")

    _defn = EnumDefinition(
        name="EnvironmentRelevanceEnum",
        description="Describes why an ingredient is relevant to a particular environment.",
    )

class OntologySourceEnum(EnumDefinitionImpl):

    CHEBI = PermissibleValue(
        text="CHEBI",
        description="Chemical Entities of Biological Interest")
    FOODON = PermissibleValue(
        text="FOODON",
        description="Food Ontology")
    NCIT = PermissibleValue(
        text="NCIT",
        description="NCI Thesaurus")
    MESH = PermissibleValue(
        text="MESH",
        description="Medical Subject Headings")
    UBERON = PermissibleValue(
        text="UBERON",
        description="Uber Anatomy Ontology")
    ENVO = PermissibleValue(
        text="ENVO",
        description="Environment Ontology")
    OTHER = PermissibleValue(
        text="OTHER",
        description="Other ontology source")

    _defn = EnumDefinition(
        name="OntologySourceEnum",
    )

# Slots
class slots:
    pass

slots.mappedIngredientsCollection__generation_date = Slot(uri=CULTUREMECH.generation_date, name="mappedIngredientsCollection__generation_date", curie=CULTUREMECH.curie('generation_date'),
                   model_uri=CULTUREMECH.mappedIngredientsCollection__generation_date, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.mappedIngredientsCollection__total_mapped_count = Slot(uri=CULTUREMECH.total_mapped_count, name="mappedIngredientsCollection__total_mapped_count", curie=CULTUREMECH.curie('total_mapped_count'),
                   model_uri=CULTUREMECH.mappedIngredientsCollection__total_mapped_count, domain=None, range=Optional[int])

slots.mappedIngredientsCollection__total_instances = Slot(uri=CULTUREMECH.total_instances, name="mappedIngredientsCollection__total_instances", curie=CULTUREMECH.curie('total_instances'),
                   model_uri=CULTUREMECH.mappedIngredientsCollection__total_instances, domain=None, range=Optional[int])

slots.mappedIngredientsCollection__media_count = Slot(uri=CULTUREMECH.media_count, name="mappedIngredientsCollection__media_count", curie=CULTUREMECH.curie('media_count'),
                   model_uri=CULTUREMECH.mappedIngredientsCollection__media_count, domain=None, range=Optional[int])

slots.mappedIngredientsCollection__mapped_ingredients = Slot(uri=CULTUREMECH.mapped_ingredients, name="mappedIngredientsCollection__mapped_ingredients", curie=CULTUREMECH.curie('mapped_ingredients'),
                   model_uri=CULTUREMECH.mappedIngredientsCollection__mapped_ingredients, domain=None, range=Optional[Union[dict[Union[str, MappedIngredientPreferredTerm], Union[dict, MappedIngredient]], list[Union[dict, MappedIngredient]]]])

slots.mappedIngredientsCollection__summary_by_category = Slot(uri=CULTUREMECH.summary_by_category, name="mappedIngredientsCollection__summary_by_category", curie=CULTUREMECH.curie('summary_by_category'),
                   model_uri=CULTUREMECH.mappedIngredientsCollection__summary_by_category, domain=None, range=Optional[Union[Union[dict, MappedCategorySummary], list[Union[dict, MappedCategorySummary]]]])

slots.mappedIngredientsCollection__summary_by_ontology = Slot(uri=CULTUREMECH.summary_by_ontology, name="mappedIngredientsCollection__summary_by_ontology", curie=CULTUREMECH.curie('summary_by_ontology'),
                   model_uri=CULTUREMECH.mappedIngredientsCollection__summary_by_ontology, domain=None, range=Optional[Union[Union[dict, OntologySummary], list[Union[dict, OntologySummary]]]])

slots.mappedIngredient__preferred_term = Slot(uri=CULTUREMECH.preferred_term, name="mappedIngredient__preferred_term", curie=CULTUREMECH.curie('preferred_term'),
                   model_uri=CULTUREMECH.mappedIngredient__preferred_term, domain=None, range=URIRef)

slots.mappedIngredient__ontology_id = Slot(uri=CULTUREMECH.ontology_id, name="mappedIngredient__ontology_id", curie=CULTUREMECH.curie('ontology_id'),
                   model_uri=CULTUREMECH.mappedIngredient__ontology_id, domain=None, range=Optional[str])

slots.mappedIngredient__ontology_label = Slot(uri=CULTUREMECH.ontology_label, name="mappedIngredient__ontology_label", curie=CULTUREMECH.curie('ontology_label'),
                   model_uri=CULTUREMECH.mappedIngredient__ontology_label, domain=None, range=Optional[str])

slots.mappedIngredient__ontology_source = Slot(uri=CULTUREMECH.ontology_source, name="mappedIngredient__ontology_source", curie=CULTUREMECH.curie('ontology_source'),
                   model_uri=CULTUREMECH.mappedIngredient__ontology_source, domain=None, range=Optional[Union[str, "OntologySourceEnum"]])

slots.mappedIngredient__occurrence_count = Slot(uri=CULTUREMECH.occurrence_count, name="mappedIngredient__occurrence_count", curie=CULTUREMECH.curie('occurrence_count'),
                   model_uri=CULTUREMECH.mappedIngredient__occurrence_count, domain=None, range=Optional[int])

slots.mappedIngredient__media_occurrences = Slot(uri=CULTUREMECH.media_occurrences, name="mappedIngredient__media_occurrences", curie=CULTUREMECH.curie('media_occurrences'),
                   model_uri=CULTUREMECH.mappedIngredient__media_occurrences, domain=None, range=Optional[Union[Union[dict, MappedMediaOccurrence], list[Union[dict, MappedMediaOccurrence]]]])

slots.mappedIngredient__concentration_info = Slot(uri=CULTUREMECH.concentration_info, name="mappedIngredient__concentration_info", curie=CULTUREMECH.curie('concentration_info'),
                   model_uri=CULTUREMECH.mappedIngredient__concentration_info, domain=None, range=Optional[Union[Union[dict, MappedConcentrationInfo], list[Union[dict, MappedConcentrationInfo]]]])

slots.mappedIngredient__synonyms = Slot(uri=CULTUREMECH.synonyms, name="mappedIngredient__synonyms", curie=CULTUREMECH.curie('synonyms'),
                   model_uri=CULTUREMECH.mappedIngredient__synonyms, domain=None, range=Optional[Union[str, list[str]]])

slots.mappedIngredient__mapping_quality = Slot(uri=CULTUREMECH.mapping_quality, name="mappedIngredient__mapping_quality", curie=CULTUREMECH.curie('mapping_quality'),
                   model_uri=CULTUREMECH.mappedIngredient__mapping_quality, domain=None, range=Optional[Union[str, "MappingQualityEnum"]])

slots.mappedIngredient__environmental_context = Slot(uri=CULTUREMECH.environmental_context, name="mappedIngredient__environmental_context", curie=CULTUREMECH.curie('environmental_context'),
                   model_uri=CULTUREMECH.mappedIngredient__environmental_context, domain=None, range=Optional[Union[Union[dict, EnvironmentContext], list[Union[dict, EnvironmentContext]]]])

slots.environmentContext__environment_term = Slot(uri=CULTUREMECH.environment_term, name="environmentContext__environment_term", curie=CULTUREMECH.curie('environment_term'),
                   model_uri=CULTUREMECH.environmentContext__environment_term, domain=None, range=str,
                   pattern=re.compile(r'^ENVO:\d{7,8}$'))

slots.environmentContext__environment_label = Slot(uri=CULTUREMECH.environment_label, name="environmentContext__environment_label", curie=CULTUREMECH.curie('environment_label'),
                   model_uri=CULTUREMECH.environmentContext__environment_label, domain=None, range=Optional[str])

slots.environmentContext__relevance = Slot(uri=CULTUREMECH.relevance, name="environmentContext__relevance", curie=CULTUREMECH.curie('relevance'),
                   model_uri=CULTUREMECH.environmentContext__relevance, domain=None, range=Union[str, "EnvironmentRelevanceEnum"])

slots.environmentContext__notes = Slot(uri=CULTUREMECH.notes, name="environmentContext__notes", curie=CULTUREMECH.curie('notes'),
                   model_uri=CULTUREMECH.environmentContext__notes, domain=None, range=Optional[str])

slots.mappedMediaOccurrence__medium_name = Slot(uri=CULTUREMECH.medium_name, name="mappedMediaOccurrence__medium_name", curie=CULTUREMECH.curie('medium_name'),
                   model_uri=CULTUREMECH.mappedMediaOccurrence__medium_name, domain=None, range=str)

slots.mappedMediaOccurrence__medium_category = Slot(uri=CULTUREMECH.medium_category, name="mappedMediaOccurrence__medium_category", curie=CULTUREMECH.curie('medium_category'),
                   model_uri=CULTUREMECH.mappedMediaOccurrence__medium_category, domain=None, range=Optional[Union[str, "MediaCategoryEnum"]])

slots.mappedMediaOccurrence__medium_file_path = Slot(uri=CULTUREMECH.medium_file_path, name="mappedMediaOccurrence__medium_file_path", curie=CULTUREMECH.curie('medium_file_path'),
                   model_uri=CULTUREMECH.mappedMediaOccurrence__medium_file_path, domain=None, range=Optional[str])

slots.mappedMediaOccurrence__ingredient_index = Slot(uri=CULTUREMECH.ingredient_index, name="mappedMediaOccurrence__ingredient_index", curie=CULTUREMECH.curie('ingredient_index'),
                   model_uri=CULTUREMECH.mappedMediaOccurrence__ingredient_index, domain=None, range=Optional[int])

slots.mappedConcentrationInfo__value = Slot(uri=CULTUREMECH.value, name="mappedConcentrationInfo__value", curie=CULTUREMECH.curie('value'),
                   model_uri=CULTUREMECH.mappedConcentrationInfo__value, domain=None, range=Optional[str])

slots.mappedConcentrationInfo__unit = Slot(uri=CULTUREMECH.unit, name="mappedConcentrationInfo__unit", curie=CULTUREMECH.curie('unit'),
                   model_uri=CULTUREMECH.mappedConcentrationInfo__unit, domain=None, range=Optional[Union[str, "ConcentrationUnitEnum"]])

slots.mappedConcentrationInfo__notes = Slot(uri=CULTUREMECH.notes, name="mappedConcentrationInfo__notes", curie=CULTUREMECH.curie('notes'),
                   model_uri=CULTUREMECH.mappedConcentrationInfo__notes, domain=None, range=Optional[str])

slots.mappedCategorySummary__category = Slot(uri=CULTUREMECH.category, name="mappedCategorySummary__category", curie=CULTUREMECH.curie('category'),
                   model_uri=CULTUREMECH.mappedCategorySummary__category, domain=None, range=Union[str, "MediaCategoryEnum"])

slots.mappedCategorySummary__media_with_mapped = Slot(uri=CULTUREMECH.media_with_mapped, name="mappedCategorySummary__media_with_mapped", curie=CULTUREMECH.curie('media_with_mapped'),
                   model_uri=CULTUREMECH.mappedCategorySummary__media_with_mapped, domain=None, range=Optional[int])

slots.mappedCategorySummary__total_mapped_instances = Slot(uri=CULTUREMECH.total_mapped_instances, name="mappedCategorySummary__total_mapped_instances", curie=CULTUREMECH.curie('total_mapped_instances'),
                   model_uri=CULTUREMECH.mappedCategorySummary__total_mapped_instances, domain=None, range=Optional[int])

slots.mappedCategorySummary__unique_mapped_count = Slot(uri=CULTUREMECH.unique_mapped_count, name="mappedCategorySummary__unique_mapped_count", curie=CULTUREMECH.curie('unique_mapped_count'),
                   model_uri=CULTUREMECH.mappedCategorySummary__unique_mapped_count, domain=None, range=Optional[int])

slots.ontologySummary__ontology_source = Slot(uri=CULTUREMECH.ontology_source, name="ontologySummary__ontology_source", curie=CULTUREMECH.curie('ontology_source'),
                   model_uri=CULTUREMECH.ontologySummary__ontology_source, domain=None, range=Union[str, "OntologySourceEnum"])

slots.ontologySummary__unique_terms_count = Slot(uri=CULTUREMECH.unique_terms_count, name="ontologySummary__unique_terms_count", curie=CULTUREMECH.curie('unique_terms_count'),
                   model_uri=CULTUREMECH.ontologySummary__unique_terms_count, domain=None, range=Optional[int])

slots.ontologySummary__total_instances = Slot(uri=CULTUREMECH.total_instances, name="ontologySummary__total_instances", curie=CULTUREMECH.curie('total_instances'),
                   model_uri=CULTUREMECH.ontologySummary__total_instances, domain=None, range=Optional[int])

slots.ontologySummary__coverage_percentage = Slot(uri=CULTUREMECH.coverage_percentage, name="ontologySummary__coverage_percentage", curie=CULTUREMECH.curie('coverage_percentage'),
                   model_uri=CULTUREMECH.ontologySummary__coverage_percentage, domain=None, range=Optional[float])

