import yaml
from tavily import TavilyClient


def test_tavily_search():
    tavily_search = TavilyClient()

    response = tavily_search.search("What is LangGraph?", max_results=2)

    print(yaml.dump(response))


def test_tavily_extract():
    tavily_client = TavilyClient()
    response = tavily_client.extract("https://docs.tavily.com/documentation/api-reference/endpoint/search")

    print(yaml.dump(response))
