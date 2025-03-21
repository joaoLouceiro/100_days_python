from requests import get

KEY = "8318d32efe2e48fd84d88795d65c2d13"
URL = "https://newsapi.org/v2/everything?"


def get_top_3_news(query):
    req = get(URL, {"q": query,
                    "apiKey": KEY,
                    "pageSize": 3,
                    "sortBy": "relevancy"})
    req.raise_for_status()
    return req.json()