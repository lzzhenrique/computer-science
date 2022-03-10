# from parsel import Selector
import requests

BASE_URL = "https://api.github.com/users/"
users = ['mojombo', 'defunkt', 'pjhyett', 'wycats']
counter = 0

while counter != len(users):
    request = requests.get(BASE_URL + users[counter])
    counter += 1
    print(request.text)
