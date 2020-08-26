"""

Example script fetching financial information from Yahoo using 
the BeautifulSoup4 module.

Author: Mark Topacio

"""

from bs4 import BeautifulSoup
import requests

def fetch_info(symbol):

    url = f"https://finance.yahoo.com/quote/{symbol}?p={symbol}&.tsrc=fin-srch"
    r = requests.get(url)

    soup = BeautifulSoup(r.text, "html.parser")

    # points of interest as defined by 'data-test'
    POI = ["PREV_CLOSE-value", "OPEN-value", "BID-value", "ASK-value",
           "DAYS_RANGE-value", "FIFTY_TWO_WK_RANGE-value"]
    AKA = ["Previous Close", "Open", "Bid", "Ask", "Day's Range", 
           "Fifty-Two Week Range"]

    values = dict()

    for i, p in enumerate(POI):
        value = soup.find("td", {"data-test":p})
        values[AKA[i]] = value.text

    return values

if __name__=="__main__":

    info = fetch_info('SPY')
    print(info)



