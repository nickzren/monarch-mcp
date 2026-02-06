from typing import Any, Dict
from ..client import MonarchClient
from .entity import EntityApi

class GeneApi:
    """
    Gene-specific queries for Monarch, refactored to use the core associations API.
    """
    def __init__(self):
        self.entity_api = EntityApi()

    async def get_gene_phenotype_associations(
        self,
        client: MonarchClient,
        gene_id: str,
        limit: int = 20,
        offset: int = 0
    ) -> Dict[str, Any]:
        """Get phenotypes associated with a gene."""
        return await self.entity_api.get_associations(
            client,
            subject=[gene_id],
            category=["biolink:GeneToPhenotypicFeatureAssociation"],
            limit=limit,
            offset=offset
        )

    async def get_gene_disease_associations(
        self,
        client: MonarchClient,
        gene_id: str,
        limit: int = 20,
        offset: int = 0
    ) -> Dict[str, Any]:
        """Get diseases associated with a gene."""
        return await self.entity_api.get_associations(
            client,
            subject=[gene_id],
            category=["biolink:GeneToDiseaseAssociation"],
            limit=limit,
            offset=offset
        )

    async def get_gene_expression_associations(
        self,
        client: MonarchClient,
        gene_id: str,
        limit: int = 20,
        offset: int = 0
    ) -> Dict[str, Any]:
        """Get expression data for a gene."""
        return await self.entity_api.get_associations(
            client,
            subject=[gene_id],
            category=["biolink:GeneToExpressionSiteAssociation"],
            limit=limit,
            offset=offset
        )

    async def get_gene_interactions(
        self,
        client: MonarchClient,
        gene_id: str,
        limit: int = 20,
        offset: int = 0
    ) -> Dict[str, Any]:
        """Get gene-gene interactions."""
        return await self.entity_api.get_associations(
            client,
            entity=[gene_id],
            category=["biolink:PairwiseGeneToGeneInteraction"],
            limit=limit,
            offset=offset
        )

    async def get_gene_orthologs(
        self,
        client: MonarchClient,
        gene_id: str,
        limit: int = 20,
        offset: int = 0
    ) -> Dict[str, Any]:
        """Get orthologous genes across species."""
        return await self.entity_api.get_associations(
            client,
            subject=[gene_id],
            category=["biolink:GeneToGeneHomologyAssociation"],
            predicate=["biolink:orthologous_to"],
            limit=limit,
            offset=offset
        )

    async def get_gene_pathways(
        self,
        client: MonarchClient,
        gene_id: str,
        limit: int = 20,
        offset: int = 0
    ) -> Dict[str, Any]:
        """Get pathways involving a gene."""
        return await self.entity_api.get_associations(
            client,
            subject=[gene_id],
            category=["biolink:GeneToPathwayAssociation"],
            limit=limit,
            offset=offset
        )

    async def get_diseases_by_gene(
        self,
        client: MonarchClient,
        gene_id: str,
        limit: int = 20,
        offset: int = 0
    ) -> Dict[str, Any]:
        """Get diseases caused by or associated with a gene (reverse lookup)."""
        return await self.entity_api.get_associations(
            client,
            object=[gene_id],
            category=["biolink:CausalGeneToDiseaseAssociation",
                      "biolink:CorrelatedGeneToDiseaseAssociation"],
            limit=limit,
            offset=offset
        )
