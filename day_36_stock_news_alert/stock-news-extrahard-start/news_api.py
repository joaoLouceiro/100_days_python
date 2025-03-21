from requests import get

KEY = "***REMOVED***"
URL = "https://newsapi.org/v2/everything?"


def get_top_3_news(query):
    req = get(URL, {"q": query,
                    "apiKey": KEY,
                    "pageSize": 3,
                    "sortBy": "relevancy"})
    req.raise_for_status()
    return req.json()