# app/robo_advisor.py
# my-secure-project/my_script.py
import json
from dotenv import load_dotenv
import os
import csv
import requests
# print(os.getenv("ALPHAVANTAGE_API_KEY"))  # > None

load_dotenv()  # > loads contents of the .env file into the script's environment


api_key = os.getenv("ALPHAVANTAGE_API_KEY")


print(api_key)

symbol = "IBM"
request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"
response = requests.get(request_url)
print(type(response))  # class
print(response.status_code)  # we got 200, sso good to go
print(response.text)  # string-need to import json module


# parse use the json module called jason.loads to change response.text to dictionary
parsed_response = json.loads(response.text)  # class to dict

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]


time_series = parsed_response["Time Series (Daily)"]

dates = list(time_series.keys())

# taking the "0" from dates list "2020-06-05 14:50:00"   //is latest date first?? MAKE SURE
latest = dates[0]

last_closing_price = time_series[latest]["4. close"]


def usd_price(last_closing_price):
    return f"${last_closing_price:,.2f}"  # > $12,000.71

# breakpoint()


recent_highs = []  # creating a list of highs to find the highest
recent_lows = []

for date in dates:
    recent_high = time_series[date]["2. high"]
    recent_highs.append(float(recent_high))
    recent_low = time_series[date]["3. low"]
    recent_lows.append(float(recent_low))


recent_highest = max(recent_highs)  # creating a list and
recent_lowest = min(recent_lows)
#
#
#
# csv_file_path = "data/prices.csv"  # a relative filepath

csv_file_path = os.path.join(os.path.dirname(
    __file__), "..", "data", "prices.csv")

csv_column_headers = ["timestamp", "open", "high", "low", "close", "volume"]

# timestamp, open, high, low, close, volume

with open(csv_file_path, "w") as csv_file:  # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=csv_column_headers)
    writer.writeheader()  # uses fieldnames set above
    for date in dates:
        minute_prices = time_series[date]

        writer.writerow({
            "timestamp": date,
            "open": minute_prices["1. open"],
            "high": minute_prices["2. high"],
            "low": minute_prices["3. low"],
            "close": minute_prices["4. close"],
            "volume": minute_prices["5. volume"]
        })


print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")

print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {usd_price(float(last_closing_price))}")
print(f"RECENT HIGH: {usd_price(float(recent_highest))}")
print(f"RECENT LOW: {usd_price(float(recent_lowest))}")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("DATA_TO_CSV: {csv_file_path}...")
print("-------------------------")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")

# print("-------------------------")
# print("SELECTED SYMBOL: XYZ")
# print("-------------------------")
# print("REQUESTING STOCK MARKET DATA...")
# print("REQUEST AT: 2018-02-20 02:00pm")
# print("-------------------------")
# print("LATEST DAY: 2018-02-20")
# print("LATEST CLOSE: $100,000.00")
# print("RECENT HIGH: $101,000.00")
# print("RECENT LOW: $99,000.00")
# print("-------------------------")
# print("RECOMMENDATION: BUY!")
# print("RECOMMENDATION REASON: TODO")
# print("-------------------------")
# print("HAPPY INVESTING!")
# print("-------------------------")
