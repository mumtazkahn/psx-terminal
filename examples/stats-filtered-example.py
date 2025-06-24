import requests
import json

# Default: Get breadth indicators only
stats_type = "breadth"
url = f"https://psxterminal.com/api/stats?type={stats_type}"

# Alternative options (uncomment to use):
# Get all statistics
# url = "https://psxterminal.com/api/stats"

# Get specific market stats
# url = "https://psxterminal.com/api/stats?type=REG"
# url = "https://psxterminal.com/api/stats?type=IDX"
# url = "https://psxterminal.com/api/stats?type=sectors"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"Market Statistics Response ({stats_type}):")
    print(json.dumps(data, indent=2))
else:
    print(f"Error: {response.status_code}")