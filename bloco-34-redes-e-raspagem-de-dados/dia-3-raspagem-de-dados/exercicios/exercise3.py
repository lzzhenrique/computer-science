# from parsel import Selector
import requests

BASE_URL = "https://www.scrapethissite.com/pages/advanced/?gotcha=headers"
headers = {'user-agent': 'Chrome/97.0.4692.99', "Accept": "text/html"}

request = requests.get(BASE_URL, headers=headers)
print(request)
print(request.text)
