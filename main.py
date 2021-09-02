from bs4 import BeautifulSoup
import requests

url1 = "https://newweb.nepalstock.com.np/today-price"
url2 = "https://merolagani.com/LatestMarket.aspx"


'''
#Get the html file
r = requests.get(url = url1)
htmcontent = r.content
print(htmcontent)
'''

headers = requests.utils.default_headers()

headers.update(
    {
        'User-Agent': 'My User Agent 1.0',
    }
)

response = requests.get(url1, headers=headers)
print(response.text)

#parse the html file
