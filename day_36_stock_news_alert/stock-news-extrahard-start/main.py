from stock import Stock
import message
import news_api

STOCK_SYMBOL = "TSLA"
COMPANY_NAME = "Tesla Inc"

stock = Stock(STOCK_SYMBOL, COMPANY_NAME)
stock_variance = stock.get_24_hour_variance()
if -5 <= stock_variance  >= 5:
    top_news =news_api.get_top_3_news(COMPANY_NAME)
    for article in top_news["articles"]:
        sms = message.Message(title=article["title"], message=article["description"], symbol=STOCK_SYMBOL, percent=stock_variance)
        print(sms.format())

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

