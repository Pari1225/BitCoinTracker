import mysql.connector
import matplotlib.pyplot as plt
from datetime import datetime

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'bitcoin_db'
}

def fetch_data_from_db():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    query = "SELECT timestamp, usd_rate FROM bitcoin_prices ORDER BY timestamp"
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data

def plot_data(data):
    # Extract timestamps and USD rates
    timestamps = [row[0].strftime('%Y-%m-%d %H:%M:%S') if isinstance(row[0], datetime) else row[0] for row in data]
    usd_rates = [row[1] for row in data]

    # Convert timestamps to datetime objects
    timestamps = [datetime.strptime(ts, '%Y-%m-%d %H:%M:%S') for ts in timestamps]

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, usd_rates, marker='o', linestyle='-', label='USD Rate')
    plt.title('Bitcoin Price Trend')
    plt.xlabel('Time')
    plt.ylabel('Price (USD)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig('bitcoin_price_trend.png')
    plt.show()


if __name__ == "__main__":
    data = fetch_data_from_db()
    plot_data(data)
