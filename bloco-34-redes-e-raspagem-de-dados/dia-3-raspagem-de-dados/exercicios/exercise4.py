from parsel import Selector
import requests

suffix = '...more'
BASE_URL = "http://books.toscrape.com/catalogue/the-grand-design_405/index.html"

request = requests.get(BASE_URL)
selector = Selector(text=request.text)
product = selector.css(".product_page")

title = product.css('.row .product_main h1::text').get()
price = product.css('.row .product_main .price_color::text').re(r"£\d+\.\d{2}")
image = product.css('img').attrib['src']

# exerc 5
in_stock = product.css(".product_main .availability::text").re_first("\d")

description = product.css('.row ~ p::text').get()

if description.endswith(suffix):
    description = description[:-len(suffix)]

print(in_stock)
# print(f"{title}, {price[0]}, {description}, {image}.")
