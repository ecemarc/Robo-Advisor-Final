import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from sendgrid.helpers.mail import Mail, From, To, Subject, PlainTextContent, HtmlContent, SendGridException
import urllib.request as urllib
from urllib.parse import urlencode
from urllib.error import HTTPError

MY_ADDRESS = os.environ.get("MY_EMAIL_ADDRESS")


message = Mail(from_email="em4063@stern.nyu.edu", to_emails="em4063@stern.nyu.edu",
               subject="E-Z Stock Acticity", plain_text_content="how are you?/", html_content="html_content")
# html_content = "Hello, thank you for visiting us today. Below please find your search results for today:"

try:
    sg = SendGridAPIClient(os.environ["SENDGRID_API_KEY"])
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)

    # print("*****************************************************")
    # # referenced geeksforgeeks upper-lower input applications
    # print("SELECTED SYMBOL:" + selected_stock.upper())
    # print("*****************************************************")
    # print("REQUESTING STOCK MARKET DATA...")
    # print("REQUEST TIME: " + " " + now.strftime("%Y-%m-%d %H:%M:%S"))

    # print("*****************************************************")
    # print(f"LATEST DAY: {last_refreshed}")
    # print(f"LATEST CLOSE: {usd_price(float(last_closing_price))}")
    # print(f"RECENT HIGH: {usd_price(float(recent_highest))}")
    # print(f"RECENT LOW: {usd_price(float(recent_lowest))}")

    # print("*****************************************************")
    # print("YOU CAN ACCESS DATA VIA:" + str(csv_file_path))
    # print("*****************************************************")
    # print("*****************************************************")
    # print("*****************************************************")
except Exception as e:
    print("ERROR")
