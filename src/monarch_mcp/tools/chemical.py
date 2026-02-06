from typing import Any, Dict
from ..client import MonarchClient
from .entity import EntityApi

class ChemicalApi:
    def __init__(self):
        self.entity_api = EntityApi()

    async def get_chemical_info(self, client: MonarchClient, chemical_id: str) -> Dict[str, Any]:
        return await self.entity_api.get_entity(client, chemical_id)

    async def get_chemical_disease_associations(
        self,
        client: MonarchClient,
        chemical_id: str,
        limit: int = 20,
        offset: int = 0
    ) -> Dict[str, Any]:
        return await self.entity_api.get_associations(
            client,
            subject=[chemical_id],
            category=["biolink:ChemicalToDiseaseOrPhenotypicFeatureAssociation",
                      "biolink:ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation"],
            limit=limit,
            offset=offset
        )

    async def get_chemical_pathway_associations(
        self,
        client: MonarchClient,
        chemical_id: str,
        limit: int = 20,
        offset: int = 0
    ) -> Dict[str, Any]:
        return await self.entity_api.get_associations(
            client,
            subject=[chemical_id],
            category=["biolink:ChemicalToPathwayAssociation"],
            limit=limit,
            offset=offset
        )

    async def get_diseases_treated_by_chemical(
        self,
        client: MonarchClient,
        chemical_id: str,
        limit: int = 20,
        offset: int = 0
    ) -> Dict[str, Any]:
        return await self.entity_api.get_associations(
            client,
            subject=[chemical_id],
            category=["biolink:ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation"],
            predicate=["biolink:treats_or_applied_or_studied_to_treat",
                       "biolink:ameliorates_condition",
                       "biolink:preventative_for_condition"],
            limit=limit,
            offset=offset
        )

    async def get_chemicals_for_disease(
        self,
        client: MonarchClient,
        disease_id: str,
        limit: int = 20,
        offset: int = 0
    ) -> Dict[str, Any]:
        return await self.entity_api.get_associations(
            client,
            object=[disease_id],
            category=["biolink:ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation"],
            predicate=["biolink:treats_or_applied_or_studied_to_treat",
                       "biolink:ameliorates_condition",
                       "biolink:preventative_for_condition"],
            limit=limit,
            offset=offset
        )
