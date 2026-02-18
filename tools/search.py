from crewai.tools import BaseTool
from pydantic import BaseModel, Field


class DuckDuckGoSearchInput(BaseModel):
    query: str = Field(..., description="Search query")


class DuckDuckGoSearchTool(BaseTool):
    name: str = "duckduckgo_search"
    description: str = "Search the web using DuckDuckGo"

    # 🔴 THIS annotation is mandatory in Pydantic v2
    args_schema: type[BaseModel] = DuckDuckGoSearchInput

    def _run(self, query: str) -> str:
        from langchain_community.tools import DuckDuckGoSearchRun

        search = DuckDuckGoSearchRun()
        return search.run(query)
