# tools/web_search.py

from langchain_community.tools.tavily_search import TavilySearchResults

# Create search tool instance
web_search_tool = TavilySearchResults(k=3)
