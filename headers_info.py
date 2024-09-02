import requests

target_url = "https://httpbin.org/headers"
response = requests.get(target_url)
print(response.text)
