import yaml
from firecrawl import Firecrawl


def test_firecrawl_search():
    client = Firecrawl()

    response = client.search(query="latest AI developments 2024", limit=2)

    print(yaml.dump(response.model_dump()))


def test_firecrawl_scrape():
    client = Firecrawl()

    response = client.scrape(
        url="https://iot-analytics.com/ai-2024-10-most-notable-stories/",
        formats=["markdown"],
    )

    print(yaml.dump(response.model_dump()))
