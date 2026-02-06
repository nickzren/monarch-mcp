"""Public API surfaces for Monarch MCP tool classes.

`ALL_TOOLS` and `API_CLASS_MAP` were removed in v0.2.0. FastMCP now handles tool
registration and dispatching directly in `monarch_mcp.server`.
"""

from .chemical import ChemicalApi
from .disease import DiseaseApi
from .entity import EntityApi
from .gene import GeneApi
from .histopheno import HistoPhenoApi
from .mapping import MappingApi
from .phenotype import PhenotypeApi
from .protein import ProteinApi
from .search import SearchApi
from .similarity import SimilarityApi
from .variant import VariantApi

__all__ = [
    "ChemicalApi",
    "DiseaseApi",
    "EntityApi",
    "GeneApi",
    "HistoPhenoApi",
    "MappingApi",
    "PhenotypeApi",
    "ProteinApi",
    "SearchApi",
    "SimilarityApi",
    "VariantApi",
]
