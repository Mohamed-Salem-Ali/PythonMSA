import requests
import json

def get_stock_data():
    api_key = "your_valid_api_key"  # Replace with your actual API key
    symbol = "IBM"
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&outputsize=full&apikey={api_key}"
    response = requests.get(url)
    
    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()
        
        # Check if the API returned an error message
        if "Error Message" in data:
            print("Error:", data["Error Message"])
            return None
        elif "Meta Data" in data:
            last_refreshed = data["Meta Data"]["3. Last Refreshed"]
            price = data["Time Series (5min)"][last_refreshed]["1. open"]
            return price
        else:
            print("Unexpected response format:", data)
            return None
    else:
        print("Failed to retrieve data:", response.status_code)
        return None

# Use the function to get stock prices
stock_prices = {}
price = get_stock_data()
symbol = "IBM"
if price is not None:
    stock_prices[symbol] = price

print(f"{symbol}: {price}")