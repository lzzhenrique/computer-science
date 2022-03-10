from parsel import Selector
import requests

BASE_URL = "https://httpbin.org/encoding/utf8"


request = requests.get(BASE_URL)
print(request.text)
