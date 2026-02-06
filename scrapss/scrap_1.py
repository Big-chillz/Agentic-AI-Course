import requests

url = "https://api.coingecko.com/api/v3/simple/price"

paramsss = {
    "ids":["bitcoin", "ethereum"],
    "vs_currencies":"usd"
        }

par = {"null":"null"}

coins = ["bitcoin", "ethereum"]
csv_file = "crypto_prices.csv"
response = requests.get(url,params=paramsss)
if response.status_code == 200 :
    data = response.json()
    print(data)
elif response.status_code == 404 :
    print("Resource not found")     
elif response.status_code ==403 :
    print("Access forbidden")
else :
    print("An error occurred")