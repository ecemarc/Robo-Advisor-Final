
WELCOME TO E-Z STOCK ADVISORY. THIS PROGRAM WILL GIVE YOU STOCK INFORMATION AND INVESTMENT ADVICE BASED ON CURRENT MARKET  TRENDS. 
IMPORT FOLLOWING MODULES:

PREREQUISITS: 

Anaconda 3.7
Python 3.7
Pip


SET UP:

First step is to obtain your API KEY:

    Please go to (https://www.alphavantage.co/support/#api-key) to receive your unique API Key. Once you have your API Keytake a moment to create a new file wihtin the repository called ".env" to securely keep your real API key.

    e.g.ALPHAVANTAGE_API_KEY="rando345"

PACKAGES:

    
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



INSTALLATION:

1.Clone repo to your computer:
    https://github.com/ecemarc/Robo-Advisor-Final

2.Create an .env file to secure the API KEY(s)


TO START: 
Once you are Done with this step please navigate from your command line to the repository and run the script: python app/robo_advisor2.py

FEATURES:

1.Once you run the script, it will ask you to enter a valid stock ticker and print the latest informaion for it. 
2.It will give you an option to view a graph of the prices.
3.It will ask you if you want any advice for now. you can exit the code at this point or continue after with another stock ticker.   


LICENCE:

The repository is licenced under MIT Licence. 