from requests import get, HTTPError

KEY_ALPHA = "GGK8LB3M78MVPHV1"
URL_ALPHA = 'https://www.alphavantage.co/query?'


class LimitRequestsException(Exception):
    pass

def __get_stock_data(function: str, params=None) -> dict:
    if params is None:
        params = {}
    params.update({"function": function,
                   "apikey": KEY_ALPHA})
    stock_req = get(url=URL_ALPHA, params=params)
    stock_req.raise_for_status()
    try:
        __check_response_for_errors(stock_req.json())
    except LimitRequestsException:
        # Workaround for AlphaVantage's daily request limit
        stock_req = __load_mock_daily_time_series()
    else:
        stock_req = stock_req.json()
    return stock_req

def __check_response_for_errors(response):
    if response.get("Error Message") is not None:
        raise HTTPError(response["Error Message"])
    if response.get("Information") is not None:
        raise LimitRequestsException

def get_daily_time_series(stock_symbol) -> dict:
    params = {"symbol": stock_symbol}
    stock_res = __get_stock_data(function="TIME_SERIES_DAILY", params=params)
    return stock_res["Time Series (Daily)"]

def __load_mock_daily_time_series():
    import json
    with open("stock_mock.json") as f:
        return json.load(f)
