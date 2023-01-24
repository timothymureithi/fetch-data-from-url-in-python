import requests

url = "https://www.nordpoolgroup.com/api/marketdata/page/10?currency=EUR"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error:", response.status_code)
