# pip install requests
import requests
from itertools import cycle

# List of proxies
proxies = [
    {"http": "http://130.61.171.71:8080", "https": "http://130.61.171.71:8080"},
    {"http": "http://101.128.78.202:32650", "https": "http://101.128.78.202:32650"},
    # ...add more
]

# Create a cycle object for infinite rotation
proxy = cycle(proxies)

target_url = "https://example.com"

for i in range(4):
    # Get the next proxy in line
    next_proxy = next(proxy)
    response = requests.get(target_url, proxies=next_proxy)
    print(response.text)
