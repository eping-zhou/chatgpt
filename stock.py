import requests
import json
import os
from datetime import date,timedelta

# API endpoint and parameters
api_key = "Nhs5dcM8GekZ7YQIGAHGNi_ojckrvTpY"
symbol = "AAPL"

# Get current date
today = date.today()

# Iterate through dates from 2023-06-01 to the current date
start_date = date(2023, 6, 1)
date_range = [start_date + timedelta(days=i) for i in range((today - start_date).days + 1)]

# List to store data for all dates
all_data = []

# Fetch data for each date
for date in date_range:
    date_str = date.strftime("%Y-%m-%d")
    endpoint = f"https://api.polygon.io/v1/open-close/{symbol}/{date_str}?adjusted=true&apiKey={api_key}"
    response = requests.get(endpoint)

    if response.status_code == 200:
        data = response.json()
        all_data.append(data)
    else:
        print(f"Error occurred while fetching data for {date_str}")
        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.content.decode('utf-8')}")

# Save all data to a JSON file
filename = "AAPL.json"
file_path = os.path.join(os.getcwd(), filename)

with open(file_path, "w") as file:
    json.dump(all_data, file)

print(f"Data saved successfully to {file_path}")

print("////")