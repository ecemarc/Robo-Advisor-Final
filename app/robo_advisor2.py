
def main():  # DDEFINE FOR OPTION TO START OVER

    # my-secure-project/my_script.py

    import requests
    import csv
    import os
    import re
    import json
    from dotenv import load_dotenv

    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import Mail
    from sendgrid.helpers.mail import Mail, From, To, Subject, PlainTextContent, HtmlContent, SendGridException
    import datetime
    import matplotlib
    import matplotlib.pyplot as plt
    import matplotlib.ticker as ticker

    now = datetime.datetime.now()

    load_dotenv()  # > loads contents of the .env file into the script's environment

    # getting the key from .env
    api_key = os.environ.get("ALPHAVANTAGE_API_KEY")

    # REFERENCED https://github.com/prof-rossetti/intro-to-python/blob/master/exercises/api-client/solution.py

    def getting_url(symbol_input):

        request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol_input}&apikey={api_key}"
        response = requests.get(request_url)
        parsed_response = json.loads(response.text)  # class to dict
        return parsed_response

    # followed Guided Screen Cast

    # def process_ticker(selected_stock):
    #     request_url = getting_url(symbol)  # this did not work, switched to the next approach
    # need to change parsed_response to dictionaary

    def change_response(parsed_response):
        time_series = parsed_response["Time Series (Daily)"]
        rows = []  # professor reosetti's robo example demo
        for date, daily_prices in time_series.items():
            row = {
                "timestamp": date,
                "open": float(daily_prices["1. open"]),
                "high": float(daily_prices["2. high"]),
                "low": float(daily_prices["3. low"]),
                "close": float(daily_prices["4. close"]),
                "volume": int(daily_prices["5. volume"])
            }
            rows.append(row)
        return rows

    def usd_price(last_closing_price):
        return f"${last_closing_price:,.2f}"  # usd conversion

    def write_to_csv(rows, csv_file_Path):
        csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]
        with open(csv_file_path, "w") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
            writer.writeheader()  # uses fieldnames set above
            for row in rows:
                writer.writerow(row)

        return True

    # USER INPUT-VALIDATING THE INPUT

    if __name__ == "__main__":  # revisited rock-paper and input module
        while True:
            symbol_input = input(
                "Please enter the company symbol to access information: ")
            # fixed to acccept both lower and upper level alhabetical values, length of 4 or less.
            if len(symbol_input) > 4 or not re.match("^[A-Za-z]*$", symbol_input):
                print("Invalid ticker, please Re-enter:")
            else:
                getting_url(symbol_input)

            # resolved the error isse by entering invalid ticker in place of demo on browser and saw "Error Message
            if "Error Message" in getting_url(symbol_input):
                print("Stock could not be found, please enter a valid ticker!")

            else:
                break

        # followed Professor Rosetti's guided video
        parsed_response = getting_url(symbol_input)
        # IMPORTANT: IF YOU RUN INTO KEYERROR DUE TO BELOW LINE, PLEASE UNTAG THE THREE LINES TO GET AN OUTPUT.TXT FILE DETAILING THE ERROR. IT HAPPENS DUE TO LIMITATIONS OF THE API
        # text_file = open("Output.txt", "w")
        # text_file.write(json.dumps(parsed_response))
        # text_file.close()

        last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

        rows = change_response(parsed_response)  # define for write.csv
        row = change_response(parsed_response)  # define for plottin
        # matching the name from above change_response
        time_series = parsed_response["Time Series (Daily)"]

        dates = list(time_series.keys())

        # taking the "0" from dates list "2020-06-05 14:50:00"   //is latest date first?? MAKE SURE
        latest = dates[0]

        last_closing_price = time_series[latest]["4. close"]

        # breakpoint()

        recent_highs = []  # creating a list of highs to find the highest
        recent_lows = []  # creating a list of lows to find the highest

        for date in dates:
            recent_high = time_series[date]["2. high"]
            recent_highs.append(float(recent_high))
            recent_low = time_series[date]["3. low"]
            recent_lows.append(float(recent_low))

        recent_highest = max(recent_highs)
        recent_lowest = min(recent_lows)

        csv_file_path = os.path.join(os.path.dirname(
            __file__), "..", "data", "prices.csv")  # ESTABLISHING CSV FILEPATH

        write_to_csv(rows, csv_file_path)

        f_csv_filepath = csv_file_path.split(
            "..")[1]  # adopted from Prof Rosetti example

        print("*****************************************************")
        # referenced geeksforgeeks upper-lower input applications
        print("SELECTED SYMBOL:" + symbol_input.upper())
        print("*****************************************************")
        print("REQUESTING STOCK MARKET DATA...")
        print("REQUEST TIME: " + " " + now.strftime("%Y-%m-%d %H:%M:%S"))

        print("*****************************************************")
        print(f"LATEST DAY: {last_refreshed}")
        print(f"LATEST CLOSE: {usd_price(float(last_closing_price))}")
        print(f"RECENT HIGH: {usd_price(float(recent_highest))}")
        print(f"RECENT LOW: {usd_price(float(recent_lowest))}")

        print("*****************************************************")
        print(f"YOU CAN ACCESS DATA VIA: {f_csv_filepath}")
        print("*****************************************************")
        print("*****************************************************")
        print("*****************************************************")

        # VALIDATING INPUT FOR GRAPH

        while True:
            line_graph = input(
                "IF A GRAPH WOULD BE HELPFUL PLEASE ENTER YES OR OTHERWISE PRESS ANY KEY TO EXIT: ")
            if line_graph == "YES" or line_graph == "yes":
                print("*****************************************************")
                print(
                    "AFTER VIEWING THE GRAPH, FOR MORE OPTIONS INCLUDING FREE ADVICE PLEASE EXIT WINDOW.")
                print("*****************************************************")
                closing_prices = []
                for cp in row:
                    closing_prices.append(cp["close"])
                graph_dates = sorted(dates)
                fig, ax = plt.subplots()  # defiins ax variable

                # used https://matplotlib.org/3.1.1/gallery/ticks_and_spines/tick-locators.html for linearlocator
                ax.xaxis.set_major_locator(plt.LinearLocator(12))
                ax.yaxis.set_major_locator(plt.LinearLocator(6))

                #  used https://matplotlib.org/3.1.1/gallery/pyplots/dollar_ticks.html for formatting to dollar sign
                formatter = ticker.FormatStrFormatter('$%1.2f')
                formatter2 = ticker.FuncFormatter(
                    lambda x, p: format(int(x), ','))
                # used https://stackoverflow.com/questions/51734218/formatting-y-axis-matplotlib-with-thousands-separator-and-font-size
                ax.yaxis.set_major_formatter(formatter2)
                ax.yaxis.set_major_formatter(formatter)

                plt.plot(graph_dates, closing_prices)
                # used the Charts Excersize in class for line_graph

                plt.xlabel('Date', fontsize=12)
                plt.ylabel('Daily Close Price', fontsize=12)
                # referenced geeksforgeeks upper-lower input applications
                plt.title('Last Quarter Prices: ' +
                          symbol_input.upper(), fontsize=18)
                plt.show()
                break
            else:
                break
            # VALIDATING INPUT FOR ADVICE
        while True:
            advice_answer = input(
                "WOULDYOU LIKE US TO EVALUATE THE RISK FOR YOU? PLEASE ENTER YES OR OTHERWISE PRESS ANY KEY TO CONTINUE FOR OTHER OPTIONS: ")
            if advice_answer == "YES" or advice_answer == "yes":
                if (float(last_closing_price)-float(recent_lowest))/float(last_closing_price) >= 0.30:  # CALCULATION
                    print("*****************************************************")
                    print(
                        "INVESTMENT ADVICE: THIS IS A HIGH RISK STOCK. PLEASE BE CAUTIOUS! ")
                    print("*****************************************************")
                    print(
                        "GOOD LUCK WITH YOUR INVESTMENTS PLEASE VISIT US AGAIN FOR MORE MARKET DRIVEN ADVICE ON STOCKS!")
                    print("******************************************************")
                    break
                elif (float(last_closing_price)-float(recent_lowest))/float(last_closing_price) >= 0.20:
                    print("******************************************************")
                    print("INVESTMENT ADVICE: IN NORMAL CISRCUMSTANCES THIS WOULD BE CONSIDERED A HIGH RISK STOCK, CONSIDERING TODAY'S VOLATILE MARKETS, IT IS MEDIUM RISK, STILL BE CAUTIOUS! ")
                    print("******************************************************")
                    print(
                        "GOOD LUCK WITH YOUR INVESTMENTS PLEASE VISIT US AGAIN FOR MORE MARKET DRIVEN ADVICE ON STOCKS!")
                    print("******************************************************")
                    break
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

            else:
                print("*******************************************************")
                print(
                    "GOOD LUCK WITH YOUR INVESTMENTS PLEASE VISIT US AGAIN FOR MORE MARKET DRIVEN ADVICE ON STOCKS!")
                print("*******************************************************")
                exit()

    # GOING BACK TO BEGINNING

    restart = input(
        "If you would like to start over please enter YES, otherwise press any other key to exit?")
    if restart == "yes" or restart == "YES":
        main()
    else:
        print("*******************************************************")
        print("GOOD LUCK WITH YOUR INVESTMENTS PLEASE VISIT US AGAIN FOR MORE MARKET DRIVEN ADVICE ON STOCKS!")
        print("*******************************************************")
        exit()


main()
