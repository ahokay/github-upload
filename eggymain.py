import requests
from bs4 import BeautifulSoup as bs
import time
url = "https://www.aldi.co.uk/gardenline-hanging-egg-chair/p/804050451817800"
webhooksurl = "https://maker.ifttt.com/trigger/update/with/key/knbNMb-MvHCbkL59SRgyKdc9oWZddFGdkivnw6ea16s"
webhooksurl2 = "https://maker.ifttt.com/trigger/bitcoin/with/key/hUVRJhLAo8VbMsBmNKKQIb5hY0G1fauQQ493N-Thg8e"


def operator():
    counter = 1
    while True:
        try:
            data = requests.get(url)
            soup = bs(data.text, "html.parser")
            availability = soup.find("span", {"class": "product-details__storeAvailabilityLabel product-details__storeAvailabilityLabel--bold"}).text
            result = availability.strip()
            if result == "Coming soonOnline Exclusive! Not available in store":
                print(f"unavailable {counter}")
                counter += 1
            else:
                message = {"value1": "THERE HAS BEEN A CHANGE ON THE EGG CHAIR AVAILABILITY"}
                print("possible change")
                requests.post(webhooksurl, message)
                requests.post(webhooksurl2, message)
        except Exception:
            message = {"value1": "There was an error in loading the egg chair webpage, there may possibly be a change on the Aldi egg chair webpage, check the website"}
            print("Error, possible change")
            requests.post(webhooksurl, message)
            requests.post(webhooksurl2, message)
        time.sleep(5)


if __name__ == "__main__":
    operator()