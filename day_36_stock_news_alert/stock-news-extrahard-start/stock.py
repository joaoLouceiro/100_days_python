from functools import reduce

import stock_api
from datetime import date, timedelta



class Stock:
    def __init__(self, symbol: str, company_name: str):
        self.symbol = symbol
        self.company_name = company_name

    def get_daily_data(self):
        return stock_api.get_daily_time_series(self.symbol)

    def get_24_hour_variance(self) -> float:
        """
        Returns the rate of price change in the last 24 hours, in percentage
        """
        yesterday = (date.today() - timedelta(days=1)).strftime("%Y-%m-%d")
        day_before = (date.today() - timedelta(days=2)).strftime("%Y-%m-%d")

        daily_time_series = self.get_daily_data()
        try:
            yesterday_data = daily_time_series[yesterday]
            day_before_data = daily_time_series[day_before]
        except KeyError:
            print("No stock data found for specified period")
        else:
            yesterday_data.pop("5. volume")
            day_before_data.pop("5. volume")
            yesterday_avg = self.__get_average(yesterday_data.values())
            day_before_avg = self.__get_average(day_before_data.values())
            return ((yesterday_avg - day_before_avg) / day_before_avg) * 100

    def __get_average(self, data):
        return reduce(lambda a, b: float(a) + float(b), data) / len(data)







