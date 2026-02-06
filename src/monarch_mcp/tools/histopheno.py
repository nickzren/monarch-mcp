from typing import Any, Dict
from ..client import MonarchClient

class HistoPhenoApi:
    """
    Tool for retrieving histopheno data from the Monarch API.
    """

    async def get_histopheno(self, client: MonarchClient, id: str) -> Dict[str, Any]:
        """
        Retrieves histopheno data for a given entity ID.
        """
        return await client.get(f"histopheno/{id}")
