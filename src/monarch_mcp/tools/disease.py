from typing import Any, Dict
from ..client import MonarchClient
from .entity import EntityApi

class DiseaseApi:
    """
    Convenience wrappers for disease-specific queries using the core EntityApi.
    """
    def __init__(self):
        self.entity_api = EntityApi()

    async def get_disease_phenotype_associations(
        self,
        client: MonarchClient,
        disease_id: str,
        limit: int = 20,
        offset: int = 0
    ) -> Dict[str, Any]:
        """Gets a table of phenotypes associated with a disease."""
        return await self.entity_api.get_associations(
            client,
            subject=[disease_id],
            category=["biolink:DiseaseToPhenotypicFeatureAssociation"],
            limit=limit,
            offset=offset
        )

    async def get_disease_gene_associations(
        self,
        client: MonarchClient,
        disease_id: str,
        limit: int = 20,
        offset: int = 0
    ) -> Dict[str, Any]:
        """Gets a table of genes associated with a disease."""
        return await self.entity_api.get_associations(
            client,
            subject=[disease_id],
            category=["biolink:CausalGeneToDiseaseAssociation", "biolink:CorrelatedGeneToDiseaseAssociation"],
            limit=limit,
            offset=offset
        )

    async def get_disease_treatments(
        self,
        client: MonarchClient,
        disease_id: str,
        limit: int = 20,
        offset: int = 0
    ) -> Dict[str, Any]:
        """Get treatments for a disease."""
        return await self.entity_api.get_associations(
            client,
            object=[disease_id],
            category=["biolink:ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation"],
            predicate=["biolink:treats_or_applied_or_studied_to_treat",
                       "biolink:ameliorates_condition"],
            limit=limit,
            offset=offset
        )

    async def get_disease_variants(
        self,
        client: MonarchClient,
        disease_id: str,
        limit: int = 20,
        offset: int = 0
    ) -> Dict[str, Any]:
        """Get genetic variants associated with a disease."""
        return await self.entity_api.get_associations(
            client,
            object=[disease_id],
            category=["biolink:VariantToDiseaseAssociation"],
            limit=limit,
            offset=offset
        )

    async def get_disease_inheritance(
        self,
        client: MonarchClient,
        disease_id: str,
        limit: int = 20,
        offset: int = 0
    ) -> Dict[str, Any]:
        """Get inheritance pattern for a disease."""
        return await self.entity_api.get_associations(
            client,
            subject=[disease_id],
            category=["biolink:DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation"],
            limit=limit,
            offset=offset
        )
