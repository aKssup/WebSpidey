import requests
from bs4 import BeautifulSoup

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
    "Accept-Encoding": "gzip, deflate", 
    "Accept-Language": "en-US,en;q=0.9", #removed host - but re-check 
    "Upgrade-Insecure-Requests": "1", 
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Safari/605.1.15"
}

url = f"https://slickdeals.net/forums/filtered/?f=4&sortfield=threadstarted&sortorder=desc"
myResponse = requests.get(url, headers=headers)
soup = BeautifulSoup(myResponse.content, 'html.parser')

#data = soup.select_one("span", attr={"class": "blueprint"})
#print(data)
data = soup.select('span.blueprint')
for specData in data:
    aElements = specData.find_all('a')
    for aData in aElements:
        #print(aData.text)
        print(aData['href'])

#print(data)




