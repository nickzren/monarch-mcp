from typing import Any, Dict
from ..client import MonarchClient
from .entity import EntityApi

class ProteinApi:
    def __init__(self):
        self.entity_api = EntityApi()

    async def get_protein_info(self, client: MonarchClient, protein_id: str) -> Dict[str, Any]:
        return await self.entity_api.get_entity(client, protein_id)

    async def get_protein_interactions(
        self,
        client: MonarchClient,
        protein_id: str,
        limit: int = 20,
        offset: int = 0
    ) -> Dict[str, Any]:
        return await self.entity_api.get_associations(
            client,
            entity=[protein_id],
            category=["biolink:PairwiseGeneToGeneInteraction"],
            predicate=["biolink:interacts_with"],
            limit=limit,
            offset=offset
        )

    async def get_protein_functions(
        self,
        client: MonarchClient,
        protein_id: str,
        limit: int = 20,
        offset: int = 0
    ) -> Dict[str, Any]:
        return await self.entity_api.get_associations(
            client,
            subject=[protein_id],
            category=["biolink:MacromolecularMachineToMolecularActivityAssociation"],
            predicate=["biolink:enables"],
            limit=limit,
            offset=offset
        )

    async def get_protein_processes(
        self,
        client: MonarchClient,
        protein_id: str,
        limit: int = 20,
        offset: int = 0
    ) -> Dict[str, Any]:
        return await self.entity_api.get_associations(
            client,
            subject=[protein_id],
            category=["biolink:MacromolecularMachineToBiologicalProcessAssociation"],
            predicate=["biolink:actively_involved_in", "biolink:participates_in"],
            limit=limit,
            offset=offset
        )

    async def get_protein_locations(
        self,
        client: MonarchClient,
        protein_id: str,
        limit: int = 20,
        offset: int = 0
    ) -> Dict[str, Any]:
        return await self.entity_api.get_associations(
            client,
            subject=[protein_id],
            category=["biolink:MacromolecularMachineToCellularComponentAssociation"],
            predicate=["biolink:located_in", "biolink:is_active_in"],
            limit=limit,
            offset=offset
        )

    async def get_proteins_by_function(
        self,
        client: MonarchClient,
        molecular_activity_id: str,
        limit: int = 20,
        offset: int = 0
    ) -> Dict[str, Any]:
        return await self.entity_api.get_associations(
            client,
            object=[molecular_activity_id],
            category=["biolink:MacromolecularMachineToMolecularActivityAssociation"],
            predicate=["biolink:enables"],
            limit=limit,
            offset=offset
        )
