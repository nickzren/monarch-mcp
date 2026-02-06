from typing import Any, Dict, List, Optional
from ..client import MonarchClient

class EntityApi:
    """
    Core tool for retrieving entities and their associations from the Monarch API.
    """

    async def get_entity(self, client: MonarchClient, entity_id: str) -> Dict[str, Any]:
        """
        Retrieves the entity with the specified ID.
        """
        return await client.get(f"entity/{entity_id}")

    async def get_entity_associations_by_category(
        self,
        client: MonarchClient,
        entity_id: str,
        category: str,
        traverse_orthologs: bool = False,
        direct: bool = False,
        query: Optional[str] = None,
        sort: Optional[List[str]] = None,
        facet_fields: Optional[List[str]] = None,
        facet_queries: Optional[List[str]] = None,
        filter_queries: Optional[List[str]] = None,
        limit: int = 20,
        offset: int = 0
    ) -> Dict[str, Any]:
        """
        Retrieves association data for a given entity and association category.
        """
        params = {
            "traverse_orthologs": traverse_orthologs,
            "direct": direct,
            "query": query,
            "sort": sort,
            "facet_fields": facet_fields,
            "facet_queries": facet_queries,
            "filter_queries": filter_queries,
            "limit": limit,
            "offset": offset
        }
        params = {k: v for k, v in params.items() if v is not None}
        return await client.get(f"entity/{entity_id}/{category}", params=params)

    async def get_associations(
        self,
        client: MonarchClient,
        category: Optional[List[str]] = None,
        subject: Optional[List[str]] = None,
        predicate: Optional[List[str]] = None,
        object: Optional[List[str]] = None,
        entity: Optional[List[str]] = None,
        direct: bool = False,
        compact: bool = False,
        limit: int = 20,
        offset: int = 0,
    ) -> Dict[str, Any]:
        """
        Retrieves associations using the generic /association endpoint.
        """
        params = {
            "category": category,
            "subject": subject,
            "predicate": predicate,
            "object": object,
            "entity": entity,
            "direct": direct,
            "compact": compact,
            "limit": limit,
            "offset": offset,
        }
        params = {k: v for k, v in params.items() if v is not None}
        return await client.get("association", params=params)

    async def get_associations_advanced(
        self,
        client: MonarchClient,
        category: Optional[List[str]] = None,
        subject: Optional[List[str]] = None,
        subject_category: Optional[List[str]] = None,
        subject_namespace: Optional[List[str]] = None,
        subject_taxon: Optional[List[str]] = None,
        predicate: Optional[List[str]] = None,
        object: Optional[List[str]] = None,
        object_category: Optional[List[str]] = None,
        object_namespace: Optional[List[str]] = None,
        object_taxon: Optional[List[str]] = None,
        entity: Optional[List[str]] = None,
        direct: bool = False,
        compact: bool = False,
        facet_fields: Optional[List[str]] = None,
        facet_queries: Optional[List[str]] = None,
        filter_queries: Optional[List[str]] = None,
        limit: int = 20,
        offset: int = 0,
    ) -> Dict[str, Any]:
        """
        Advanced association query with all available filters.
        """
        params = {
            "category": category,
            "subject": subject,
            "subject_category": subject_category,
            "subject_namespace": subject_namespace,
            "subject_taxon": subject_taxon,
            "predicate": predicate,
            "object": object,
            "object_category": object_category,
            "object_namespace": object_namespace,
            "object_taxon": object_taxon,
            "entity": entity,
            "direct": direct,
            "compact": compact,
            "facet_fields": facet_fields,
            "facet_queries": facet_queries,
            "filter_queries": filter_queries,
            "limit": limit,
            "offset": offset,
        }
        params = {k: v for k, v in params.items() if v is not None}
        return await client.get("association", params=params)

    async def get_entities_batch(
        self,
        client: MonarchClient,
        entity_ids: List[str]
    ) -> List[Dict[str, Any]]:
        """
        Get information for multiple entities at once.
        """
        results = []
        for entity_id in entity_ids:
            try:
                result = await client.get(f"entity/{entity_id}")
                results.append(result)
            except Exception as e:
                results.append({"id": entity_id, "error": str(e)})
        return results
