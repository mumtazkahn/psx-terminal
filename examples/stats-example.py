import requests
import json

# Get market statistics
url = "https://psxterminal.com/api/stats"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Market Statistics Response:")
    print(json.dumps(data, indent=2))
else:
    print(f"Error: {response.status_code}")