from typing import Any, Dict, List
from ..client import MonarchClient
from .entity import EntityApi

class PhenotypeApi:
    """
    Phenotype-specific queries and matching for Monarch, refactored for the v3 API.
    """
    def __init__(self):
        self.entity_api = EntityApi()

    async def phenotype_profile_search(
        self,
        client: MonarchClient,
        phenotype_ids: List[str],
        search_group: str = "Human Diseases",
        metric: str = "ancestor_information_content",
        limit: int = 10,
    ) -> Dict[str, Any]:
        """
        Search for entities (e.g., diseases) that best match a profile of phenotypes.
        """
        termset = ",".join(phenotype_ids)
        params = {"metric": metric, "limit": limit}
        return await client.get(f"semsim/search/{termset}/{search_group}", params=params)

    async def get_phenotype_gene_associations(
        self,
        client: MonarchClient,
        phenotype_id: str,
        limit: int = 20,
        offset: int = 0
    ) -> Dict[str, Any]:
        """Get genes associated with a phenotype."""
        return await self.entity_api.get_associations(
            client,
            subject=[phenotype_id],
            category=["biolink:GeneToPhenotypicFeatureAssociation"],
            limit=limit,
            offset=offset
        )

    async def get_phenotype_disease_associations(
        self,
        client: MonarchClient,
        phenotype_id: str,
        limit: int = 20,
        offset: int = 0
    ) -> Dict[str, Any]:
        """Get diseases associated with a phenotype."""
        return await self.entity_api.get_associations(
            client,
            subject=[phenotype_id],
            category=["biolink:DiseaseToPhenotypicFeatureAssociation"],
            limit=limit,
            offset=offset
        )

    async def get_diseases_with_phenotype(
        self,
        client: MonarchClient,
        phenotype_id: str,
        limit: int = 20,
        offset: int = 0
    ) -> Dict[str, Any]:
        """Get diseases that have a specific phenotype."""
        return await self.entity_api.get_associations(
            client,
            object=[phenotype_id],
            category=["biolink:DiseaseToPhenotypicFeatureAssociation"],
            limit=limit,
            offset=offset
        )

    async def get_genes_with_phenotype(
        self,
        client: MonarchClient,
        phenotype_id: str,
        limit: int = 20,
        offset: int = 0
    ) -> Dict[str, Any]:
        """Get genes that cause a specific phenotype."""
        return await self.entity_api.get_associations(
            client,
            object=[phenotype_id],
            category=["biolink:GeneToPhenotypicFeatureAssociation"],
            limit=limit,
            offset=offset
        )
