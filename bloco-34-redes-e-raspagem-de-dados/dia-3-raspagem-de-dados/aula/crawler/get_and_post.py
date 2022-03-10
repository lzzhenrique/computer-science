import requests

response = requests.get('https://www.nasa.gov/')
print(response.status_code)
print(response.headers["Content-Type"])

print(response.text)

print(response.content)

response = requests.post("http://httpbin.org/post", data="some content")
print(response.text)

response = requests.get("http://httpbin.org/get", headers={"Accept": "application/json"})
print(response.text)

response = requests.get("http://httpbin.org/image/png")
print(response.content)

response = requests.get("http://httpbin.org/get")
# Equivalente ao json.loads(response.content)
print(response.json())
