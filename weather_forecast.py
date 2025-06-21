import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

API_KEY = '389267a52ee7d80ab5340e2487061cd3'  # Replace with your real API key
  # Replace with your API key
BASE_URL = 'https://api.openweathermap.org/data/2.5/forecast'

# User input for cities
CITIES = input("Enter city names separated by commas: ").split(',')
CITIES = [city.strip() for city in CITIES]

def get_forecast_data(city):
    params = {'q': city, 'appid': API_KEY, 'units': 'metric'}
    r = requests.get(BASE_URL, params=params)
    if r.status_code != 200:
        print(f"⚠️ Couldn't fetch data for {city}")
        return None

    data = r.json()
    forecast_list = data['list']
    
    # Extracting day-wise temperature
    daily_data = {}
    for entry in forecast_list:
        dt = datetime.strptime(entry['dt_txt'], '%Y-%m-%d %H:%M:%S')
        day = dt.date()
        temp = entry['main']['temp']
        if day not in daily_data:
            daily_data[day] = []
        daily_data[day].append(temp)
    
    # Calculate average temp per day
    averages = [{'City': city, 'Date': str(day), 'Avg Temp (°C)': sum(temps)/len(temps)} 
                for day, temps in daily_data.items()]
    
    return averages[:5]  # Get only next 5 days

# Combine all city forecasts
all_data = []
for city in CITIES:
    forecast = get_forecast_data(city)
    if forecast:
        all_data.extend(forecast)

# Create DataFrame
df = pd.DataFrame(all_data)
df.to_csv('5_day_forecast.csv', index=False)

# Plotting
sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='Date', y='Avg Temp (°C)', hue='City', marker="o")
plt.title("5-Day Temperature Forecast")
plt.tight_layout()
plt.savefig("5_day_forecast.png")
plt.show()

print("✅ Forecast chart saved as '5_day_forecast.png'")
