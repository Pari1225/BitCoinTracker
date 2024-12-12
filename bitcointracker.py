import requests
import mysql.connector
from datetime import datetime

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'bitcoin_db'
}

# API URL
API_URL = "https://api.coindesk.com/v1/bpi/currentprice.json"


def fetch_bitcoin_data():
    response = requests.get(API_URL)
    data = response.json()
    usd_rate = data['bpi']['USD']['rate_float']

    # Parse timestamp and convert to MySQL DATETIME format
    timestamp_with_tz = data['time']['updatedISO']
    timestamp = datetime.fromisoformat(timestamp_with_tz.replace("Z", "+00:00")).strftime('%Y-%m-%d %H:%M:%S')

    # Example low/high values (could be replaced by another API call)
    low = usd_rate * 0.95
    high = usd_rate * 1.05
    return timestamp, usd_rate, low, high

def insert_data_to_db(timestamp, usd_rate, low, high):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    query = """
    INSERT INTO bitcoin_prices (timestamp, usd_rate, low, high)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (timestamp, usd_rate, low, high))
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    timestamp, usd_rate, low, high = fetch_bitcoin_data()
    insert_data_to_db(timestamp, usd_rate, low, high)
    print(f"Data inserted: {timestamp}, USD Rate: {usd_rate}, Low: {low}, High: {high}")
