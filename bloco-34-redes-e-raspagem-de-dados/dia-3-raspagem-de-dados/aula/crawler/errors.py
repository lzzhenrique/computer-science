from urllib import response
import requests
import time
count = 0

for _ in range(1500):
    response = requests.get("https://www.nasa.gov/")
    count += 1
    print(response.status_code, count)
