import requests
import json

# Get all available symbols
url = "https://psxterminal.com/api/symbols"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Symbols List Response:")
    print(json.dumps(data, indent=2))
else:
    print(f"Error: {response.status_code}")