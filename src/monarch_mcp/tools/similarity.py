from typing import Any, Dict, List
from ..client import MonarchClient

class SimilarityApi:
    """
    Semantic similarity calculations between entities.
    """

    async def compare_termsets(
        self,
        client: MonarchClient,
        subjects: List[str],
        objects: List[str],
        metric: str = "ancestor_information_content",
    ) -> Dict[str, Any]:
        """
        Get pairwise similarity between two sets of terms.
        """
        subjects_str = ",".join(subjects)
        objects_str = ",".join(objects)
        params = {"metric": metric}
        return await client.get(f"semsim/compare/{subjects_str}/{objects_str}", params=params)

    async def find_similar_terms(
        self,
        client: MonarchClient,
        termset: List[str],
        search_group: str,
        metric: str = "ancestor_information_content",
        directionality: str = "bidirectional",
        limit: int = 10,
    ) -> Dict[str, Any]:
        """
        Search for terms in a termset that are similar to a group of entities.
        """
        termset_str = ",".join(termset)
        params = {
            "metric": metric,
            "directionality": directionality,
            "limit": limit
        }
        return await client.get(f"semsim/search/{termset_str}/{search_group}", params=params)
