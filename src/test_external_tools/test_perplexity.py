import yaml
from perplexity import Perplexity


def test_perplexity():
    client = Perplexity()

    response = client.search.create(query="latest AI developments 2024", max_results=1, max_tokens_per_page=1024)

    print(yaml.dump(response.model_dump()))
