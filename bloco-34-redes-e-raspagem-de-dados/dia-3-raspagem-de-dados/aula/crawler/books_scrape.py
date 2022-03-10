from parsel import Selector
import requests


URL_BASE = "http://books.toscrape.com/catalogue/"
next_page_url = 'page-1.html'


while next_page_url:
    response = requests.get(URL_BASE + next_page_url)
    selector = Selector(text=response.text)


    for product in selector.css(".product_pod"):
        title = product.css("h3 a::attr(title)").get()
        price = product.css(".price_color:: text").re(r"£\d+\.\d{2}")
        href = product.css(".image_container a::attr(href)").get()

        detail_page = requests.get(URL_BASE + href)
        detail_selector = Selector(text=detail_page.text)

        description = detail_selector.css("#product_description ~ p::text").get()

        suffix = "...more"

        if description.endswith(suffix):
            description = description[:-len(suffix)]
        # print(title)
        # print(price)
        print(description)

    next_page_url = selector.css(".next a::attr(href)").get()