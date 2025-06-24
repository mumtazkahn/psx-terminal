import requests
import json

# Default: Get specific market type data
market = "REG"
url = f"https://psxterminal.com/api/market-data?market={market}"

# Alternative options (uncomment to use):
# Get all market data
# url = "https://psxterminal.com/api/market-data"

# Get specific market types
# url = "https://psxterminal.com/api/market-data?market=FUT"
# url = "https://psxterminal.com/api/market-data?market=IDX"
# url = "https://psxterminal.com/api/market-data?market=ODL"
# url = "https://psxterminal.com/api/market-data?market=BNB"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"Market Data Response for {market} market:")
    print(json.dumps(data, indent=2))
else:
    print(f"Error: {response.status_code}")