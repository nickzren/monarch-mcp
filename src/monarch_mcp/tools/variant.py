from typing import Any, Dict
from ..client import MonarchClient
from .entity import EntityApi

class VariantApi:
    def __init__(self):
        self.entity_api = EntityApi()

    async def get_variant_info(self, client: MonarchClient, variant_id: str) -> Dict[str, Any]:
        return await self.entity_api.get_entity(client, variant_id)

    async def get_variant_gene_associations(
        self,
        client: MonarchClient,
        variant_id: str,
        limit: int = 20,
        offset: int = 0
    ) -> Dict[str, Any]:
        return await self.entity_api.get_associations(
            client,
            subject=[variant_id],
            category=["biolink:VariantToGeneAssociation"],
            limit=limit,
            offset=offset
        )

    async def get_variant_disease_associations(
        self,
        client: MonarchClient,
        variant_id: str,
        limit: int = 20,
        offset: int = 0
    ) -> Dict[str, Any]:
        return await self.entity_api.get_associations(
            client,
            subject=[variant_id],
            category=["biolink:VariantToDiseaseAssociation"],
            limit=limit,
            offset=offset
        )

    async def get_variant_phenotype_associations(
        self,
        client: MonarchClient,
        variant_id: str,
        limit: int = 20,
        offset: int = 0
    ) -> Dict[str, Any]:
        return await self.entity_api.get_associations(
            client,
            subject=[variant_id],
            category=["biolink:VariantToPhenotypicFeatureAssociation"],
            limit=limit,
            offset=offset
        )

    async def get_gene_variants(
        self,
        client: MonarchClient,
        gene_id: str,
        limit: int = 20,
        offset: int = 0
    ) -> Dict[str, Any]:
        return await self.entity_api.get_associations(
            client,
            object=[gene_id],
            category=["biolink:VariantToGeneAssociation"],
            limit=limit,
            offset=offset
        )

    async def get_variants_by_disease(
        self,
        client: MonarchClient,
        disease_id: str,
        limit: int = 20,
        offset: int = 0
    ) -> Dict[str, Any]:
        return await self.entity_api.get_associations(
            client,
            object=[disease_id],
            category=["biolink:VariantToDiseaseAssociation"],
            limit=limit,
            offset=offset
        )
