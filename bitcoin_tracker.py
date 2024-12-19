import requests
import mysql.connector
from datetime import datetime
import xml.etree.ElementTree as ET

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'bitcoin_db'
}

# API URL
API_URL = "https://api.coindesk.com/v1/bpi/currentprice.json"

def read_config(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    for task in root.findall('Tasks/Task'):
        if task.find('Name').text == "FetchBitcoinData":
            frequency_unit = task.find('Frequency/Unit').text
            frequency_value = int(task.find('Frequency/Value').text)
            print(f"Configuration Loaded: Run every {frequency_value} {frequency_unit}.")
            return frequency_value, frequency_unit

    # If the "FetchBitcoinData" task is not found, return default values or raise an error
    raise ValueError("FetchBitcoinData task not found in configuration file.")


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
    # Load configuration from XML
    config_path = "bitcoin_tracker.xml"
    frequency_value, frequency_unit = read_config(config_path)

    # Fetch and store Bitcoin data
    timestamp, usd_rate, low, high = fetch_bitcoin_data()
    insert_data_to_db(timestamp, usd_rate, low, high)
    print(f"Data inserted: {timestamp}, USD Rate: {usd_rate}, Low: {low}, High: {high}")