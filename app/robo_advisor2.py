# my-secure-project/my_script.py
import re
import json
from dotenv import load_dotenv
import os
import csv
import requests

import datetime
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


import datetime
now = datetime.datetime.now()
# print(os.getenv("ALPHAVANTAGE_API_KEY"))  # > None

load_dotenv()  # > loads contents of the .env file into the script's environment


api_key = os.getenv("ALPHAVANTAGE_API_KEY")


# print(api_key)

# REFERENCED https://github.com/prof-rossetti/intro-to-python/blob/master/exercises/api-client/solution.py

def getting_url(symbol_input):
    symbol_input = selected_stock
    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol_input}&apikey={api_key}"
    return request_url

# followed Guided Screen Cast


def process_ticker(symbol):
    request_url = getting_url(symbol)  # requesting API
    response = requests.get(request_url)
    # parse use the json module called jason.loads to change response.text to dictionary
    parsed_response = json.loads(response.text)  # class to dict
    return parsed_response

    # professor Rosetti's guided solutions


def transform_response(parsed_response):
    time_series_info = parsed_response["Time Series (Daily)"]
    all_rows = []
    for date, daily_prices in time_series_info.items():
        row = {
            "timestamp": date,
            "open": float(daily_prices["1. open"]),
            "high": float(daily_prices["2. high"]),
            "low": float(daily_prices["3. low"]),
            "close": float(daily_prices["4. close"]),
            "volume": int(daily_prices["5. volume"])
        }
        all_rows.append(row)
    return all_rows


# def write_csv(rows, csv_file_path):
#     with open(csv_file_path, "w") as csv_file:  # "w" means "open the file for writing"

#         writer = csv.DictWriter(csv_file, fieldnames=csv_column_headers)
#         writer.writeheader()  # uses fieldnames set above
#         for row in all_rows:
#             writer.writeheader()
#     return True
#     # for date in dates:
#     #     minute_prices = time_series[date]

#     writer.writerow({
#         "timestamp": date,
#         "open": minute_prices["1. open"],
#         "high": minute_prices["2. high"],
#         "low": minute_prices["3. low"],
#         "close": minute_prices["4. close"],
#         "volume": minute_prices["5. volume"]
    # })

# print(type(response))  # class
# print(response.status_code)  # we got 200, sso good to go
# print(response.text)  # string-need to import json module


if __name__ == "__main__":  # revisited rock-paper and input module
    while True:
        selected_stock = input(
            "Please enter the company symbol to access information: ")
        # stockoverflow
        if len(selected_stock) > 4 or not re.match("^[A-Z]*$", selected_stock):
            print("Invalid ticker, please Re-enter:")
        else:
            process_ticker(selected_stock)
        if "KeyError" in process_ticker(selected_stock):
            print("Stock could not be found, please enter a valid ticker!")
            # tried to replicate error checking from hiepnguneyen and megc on Github but is not working
        else:
            break

    # followed Professor Rosetti's guided video
    parsed_response = process_ticker(selected_stock)
    last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
    row = transform_response(parsed_response)
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

    # csv_file_path = "data/prices.csv"  # a relative filepath
    csv_file_path = os.path.join(os.path.dirname(
        __file__), "..", "data", "prices.csv")
    # timestamp, open, high, low, close, volume

    print("*****************************************************")
    # referenced geeksforgeeks upper-lower input applications
    print("SELECTED SYMBOL:" + selected_stock.upper())
    print("*****************************************************")
    print("REQUESTING STOCK MARKET DATA...")
    print("REQUEST TIME: " + " " + now.strftime("%Y-%m-%d %H:%M:%S"))

    print("*****************************************************")
    print(f"LATEST DAY: {last_refreshed}")
    print(f"LATEST CLOSE: {usd_price(float(last_closing_price))}")
    print(f"RECENT HIGH: {usd_price(float(recent_highest))}")
    print(f"RECENT LOW: {usd_price(float(recent_lowest))}")

    print("*****************************************************")
    print("YOU CAN ACCESS DATA VIA:" + str(csv_file_path))
    print("*****************************************************")
    print("*****************************************************")
    print("*****************************************************")

    while True:
        line_graph = input(
            "IF A GRAPH WOULD BE HELPFUL PLEASE ENTER YES OR OTHERWISE PRESS ANY KEY TO CONTINUE FOR OTHER OPTIONS: ")
        if line_graph == "YES" or "yes":
            print("*****************************************************")
            print(
                "AFTER VIEWING THE GRAPH, FOR MORE OPTIONS INCLUDING FREE ADVICE PLEASE EXIT WINDOW.")
            print("*****************************************************")
            closing_prices = []
            for cp in row:
                closing_prices.append(cp["close"])
            graph_dates = sorted(dates)
            fig, ax = plt.subplots()

            # used https://matplotlib.org/3.1.1/gallery/ticks_and_spines/tick-locators.html for linearlocator
            ax.xaxis.set_major_locator(plt.LinearLocator(12))
            ax.yaxis.set_major_locator(plt.LinearLocator(6))

            #  used https://matplotlib.org/3.1.1/gallery/pyplots/dollar_ticks.html for formatting to dollar sign
            formatter = ticker.FormatStrFormatter('$%1.2f')
            formatter2 = ticker.FuncFormatter(lambda x, p: format(int(x), ','))
            # used https://stackoverflow.com/questions/51734218/formatting-y-axis-matplotlib-with-thousands-separator-and-font-size
            ax.yaxis.set_major_formatter(formatter2)
            ax.yaxis.set_major_formatter(formatter)

            plt.plot(graph_dates, closing_prices)
            # used the Charts Excersize in class for line_graph

            plt.xlabel('Date', fontsize=12)
            plt.ylabel('Daily Close Price', fontsize=12)
            # referenced geeksforgeeks upper-lower input applications
            plt.title('Last Quarter Prices: ' +
                      selected_stock.upper(), fontsize=18)
            plt.show()

            break
        else:
            break

    while True:
        advice_answer = input(
            "WOULDYOU LIKE US TO EVALUATE THE RISK FOR YOU? PLEASE ENTER YES OR OTHERWISE PRESS ANY KEY TO CONTINUE FOR OTHER OPTIONS: ")
        if advice_answer == "YES" or "yes":
            if (float(last_closing_price)-float(recent_lowest))/float(last_closing_price) >= 0.30:
                print("*****************************************************")
                print(
                    "INVESTMENT ADVICE: THIS IS A HIGH RISK STOCK. PLEASE BE CAUTIOUS! ")
                print("*****************************************************")
                print(
                    "GOOD LUCK WITH YOUR INVESTMENTS PLEASE VISIT US AGAIN FOR MORE MARKET DRIVEN ADVICE ON STOCKS!")
                print("******************************************************")
            elif (float(last_closing_price)-float(recent_lowest))/float(last_closing_price) >= 0.20:
                print("******************************************************")
                print("INVESTMENT ADVICE: IN NORMAL CISRCUMSTANCES THIS WOULD BE CONSIDERED A HIGH RISK STOCK, CONSIDERING TODAY'S VOLATILE MARKETS, IT IS MEDIUM RISK, STILL BE CAUTIOUS! ")
                print("******************************************************")
                print(
                    "GOOD LUCK WITH YOUR INVESTMENTS PLEASE VISIT US AGAIN FOR MORE MARKET DRIVEN ADVICE ON STOCKS!")
                print("******************************************************")
            elif (float(last_closing_price)-float(recent_lowest))/float(last_closing_price) < 0.11:
                print("******************************************************")
                print("iNVESTMENT ADVICE: THIS IS MED-LOW RISK STOCK. ")
                print("******************************************************")
                print(
                    "GOOD LUCK WITH YOUR INVESTMENTS PLEASE VISIT US AGAIN FOR MORE MARKET DRIVEN ADVICE ON STOCKS!")
                print("*******************************************************")
            elif (float(last_closing_price)-float(recent_lowest))/float(last_closing_price) < 0.6:
                print("******************************************************")
                print("INVESTMENT ADVICE: THIS IS LOW RISK STOCK ")
                print("******************************************************")
                print(
                    "GOOD LUCK WITH YOUR INVESTMENTS PLEASE VISIT US AGAIN FOR MORE MARKET DRIVEN ADVICE ON STOCKS!")
                print("*******************************************************")
                break

        else:
            exit()
