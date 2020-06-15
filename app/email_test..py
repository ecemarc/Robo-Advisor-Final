from sendgrid.helpers.mail import *
import sendgrid
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from sendgrid.helpers.mail import Mail, From, To, Subject, PlainTextContent, HtmlContent, SendGridException
import urllib.request as urllib
from urllib.parse import urlencode
from urllib.error import HTTPError

MY_ADDRESS = os.environ.get("MY_EMAIL_ADDRESS")
# api_key = "V3UasxutRd6umNS6zqQ6jA.qGZ7iW61hA25OWVHFV7a1aGBxK1Lt9-kb18jKZM-roM"

# message = Mail(from_email="em4063@stern.nyu.edu", to_emails="em4063@stern.nyu.edu",
#                subject="E-Z Stock Acticity", plain_text_content="how are you?/", html_content="html_content")
# # html_content = "Hello, thank you for visiting us today. Below please find your search results for today:"
sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
print(os.environ.get('SENDGRID_API_KEY'))
from_email = Email("ecemarcelli@gmail.com")
to_email = To("ecemar@edpausa.com")
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, to_email, subject, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)


# try:
#     sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
#     response = sg.send(message)
#     from_email = Email("ecemarcelli@gmail.com")
#     to_email = To("ecemar@edpausa.com")
#     subject = "Sending with SendGrid is Fun"
#     content = Content(
#         "text/plain", "and easy to do anywhere, even with Python")
#     mail = Mail(from_email, to_email, subject, content)
#     response = sg.client.mail.send.post(request_body=mail.get())
#     print(response.status_code)
#     print(response.status_code)
#     print(response.body)
#     print(response.headers)

#     # print("*****************************************************")
#     # # referenced geeksforgeeks upper-lower input applications
#     # print("SELECTED SYMBOL:" + selected_stock.upper())
#     # print("*****************************************************")
#     # print("REQUESTING STOCK MARKET DATA...")
#     # print("REQUEST TIME: " + " " + now.strftime("%Y-%m-%d %H:%M:%S"))

#     # print("*****************************************************")
#     # print(f"LATEST DAY: {last_refreshed}")
#     # print(f"LATEST CLOSE: {usd_price(float(last_closing_price))}")
#     # print(f"RECENT HIGH: {usd_price(float(recent_highest))}")
#     # print(f"RECENT LOW: {usd_price(float(recent_lowest))}")

#     # print("*****************************************************")
#     # print("YOU CAN ACCESS DATA VIA:" + str(csv_file_path))
#     # print("*****************************************************")
#     # print("*****************************************************")
#     # print("*****************************************************")
# except Exception as e:
#     print("ERROR")
