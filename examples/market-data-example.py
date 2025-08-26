import requests
import json

# Default: Get specific symbol data
market = "REG"
symbol = "HUBC"
url = f"https://psxterminal.com/api/ticks/{market}/{symbol}"

# Alternative options (uncomment to use):

# Get all symbols
# url = "https://psxterminal.com/api/symbols"

# Get different market types  
# url = "https://psxterminal.com/api/ticks/REG/MARI"

# Get market statistics
# url = "https://psxterminal.com/api/stats/REG"
# url = "https://psxterminal.com/api/stats/breadth"

# Get company information
# url = "https://psxterminal.com/api/companies/HUBC"

# Get fundamental analysis
# url = "https://psxterminal.com/api/fundamentals/HUBC"

# Get dividend history
# url = "https://psxterminal.com/api/dividends/MARI"

# Get historical kline data (limit required, max 100)
# url = "https://psxterminal.com/api/klines/HUBC/1h?limit=50"
# url = "https://psxterminal.com/api/klines/HUBC/1h?start=1756000000000&end=1756200000000&limit=10"

# Get single kline by exact timestamp
# url = "https://psxterminal.com/api/klines/HUBC/1h/1756202400000"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"API Response:")
    print(json.dumps(data, indent=2))
else:
    print(f"Error: {response.status_code}")
    print(f"Response: {response.text}")