import requests
import pandas as pd
# Send the GET request to the API
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&outputsize=full&apikey=A5NFB3AZA559K9T5'
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Print the response content
    print(response.json())
else:
    print("Error occurred while retrieving stock data. Status Code:", response.status_code)


# A5NFB3AZA559K9T5
import requests
import pandas as pd

# Replace 'YOUR_API_KEY' with your actual Alpha Vantage API key
api_key = 'A5NFB3AZA559K9T5'

# Define the list of symbols for the top 10 American tech companies
symbols = ['AAPL', 'MSFT', 'AMZN', 'GOOGL', 'FB', 'TSLA', 'NVDA', 'INTC', 'ADBE', 'PYPL']

# Create an empty dataframe to store the stock data
stock_data = pd.DataFrame()

# Fetch historical stock data for each symbol
for symbol in symbols:
    # Define the Alpha Vantage API URL for daily stock data
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&apikey={api_key}'

    # Send the GET request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract the stock data from the response
        data = response.json()['Time Series (Daily)']

        # Convert the data to a dataframe
        df = pd.DataFrame.from_dict(data, orient='index')
        df.index = pd.to_datetime(df.index)
        
        # Rename the columns and select only the 'close' price
        df.rename(columns={'4. close': symbol}, inplace=True)
        df = df[[symbol]]

        # Append the data to the stock_data dataframe
        stock_data = pd.concat([stock_data, df], axis=1)
    else:
        print(f"Error occurred while retrieving stock data for {symbol}. Status Code:", response.status_code)

# Sort the stock_data dataframe by date in ascending order
stock_data.sort_index(ascending=True, inplace=True)

# Filter the data for one year (adjust the dates as needed)
start_date = pd.Timestamp.now() - pd.DateOffset(years=1)
stock_data = stock_data.loc[start_date:]

# Print the stock_data dataframe
print(stock_data)



