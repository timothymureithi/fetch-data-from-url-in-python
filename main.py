import requests

url = 'https://www.nordpoolgroup.com/api/marketdata/page/10?currency=,,,EUR'
response = requests.get(url)
data = response.json()

tromso_data = [item for item in data if item['name'] == 'Tromsø']

# Print the startTime for each item
for item in tromso_data:
    print(item['startTime'])
