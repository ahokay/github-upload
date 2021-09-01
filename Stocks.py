import requests
from bs4 import BeautifulSoup as bs
import time
from datetime import datetime

exchangerateurl = "https://api.exchangeratesapi.io/latest?base=USD?access_key=8b9d700d1bfa6f773bd8bc9e0bd28e4c"
stocks = ["gme", "pltr", "uwmc", "rkt", "bned"]
url = "https://www.marketwatch.com/investing/stock/"
investments = {"gme": 1721.04, "pltr": 800, "uwmc": 218.34, "rkt": 181.44, "bned": None}
opening = {"gme": 236.09, "pltr": 21.38, "uwmc": 8.4832137442, "rkt": 26.1350675335, "bned": None}
currentprice = {"gme": None, "pltr": None, "uwmc": None, "rkt": None, "bned": None}
rate = None
webhooksurl = "https://maker.ifttt.com/trigger/bitcoin/with/key/hUVRJhLAo8VbMsBmNKKQIb5hY0G1fauQQ493N-Thg8e"

def pricefinder():
    global currentprice
    for i in stocks:
        try:
            data = requests.get(url+i)
            soup = bs(data.text, "html.parser")
            soup2 = soup.find("div", {"class": "intraday__data"})
            price = soup2.find("bg-quote", {"class": "value"}).text
            currentprice[i] = float(price)
        except Exception:
            currentprice[i] = "Unavailable"


def pricedifference(ticker):
    string = ""
    try:
        percentagedifference = round(((currentprice[ticker] - opening[ticker]) / opening[ticker] * 100), 2)
        if percentagedifference >= 0:
            string += f"(+{percentagedifference}%)"
        else:
            string += f"(-{-percentagedifference}%)"
        return string
    except Exception:
        return ""


def printer():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    string = f"{current_time} \n"
    for i in stocks:
        string += f"{i.upper()}: ${currentprice[i]} {pricedifference(i)}\n"
    print(string)


def operator():
    while True:
        pricefinder()
        printer()
        time.sleep(10)

if __name__ == "__main__":
    operator()