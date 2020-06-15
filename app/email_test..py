from sendgrid.helpers.mail import *

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from sendgrid.helpers.mail import Mail, From, To, Subject, PlainTextContent, HtmlContent, SendGridException


import sendgrid
import os


##################################################
# Create a transactional template. #
# POST /templates #


MY_ADDRESS = os.environ.get("MY_EMAIL_ADDRESS")

message = Mail(from_email=From("em4063@stern.nyu.edu"), to_emails=To("em4063@stern.nyu.edu"),
               subject=Subject("E-Z Stock Acticity"), plain_text_content=PlainTextContent("how are you?"), html_content=HtmlContent("html_content"))

# sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))

# print(os.environ.get('SENDGRID_API_KEY'))
# from_email = Email("ecemarcelli@gmail.com")
# to_email = To("ecemar@edpausa.com")
# subject = "Sending with SendGrid is Fun"
# content = Content("text/plain", "and easy to do anywhere, even with Python")
# mail = Mail(from_email, to_email, subject, content)
# response = sg.client.mail.send.post(request_body=mail.get())
# print(response.status_code)
# print(response.body)
# print(response.headers)


try:
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))

    sendgrid_client = SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY')
    # subject = "Sending with SendGrid is Fun"
    response=sendgrid_client.send(message=message)
    print(response.status_code)
    print(response.body)
    print(response.headers)


except Exception as e:
    print("ERROR")

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
