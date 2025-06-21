import os
import requests
import matplotlib.pyplot as plt
from datetime import datetime

# === CONFIG ===
API_KEY = '389267a52ee7d80ab5340e2487061cd3'  # Replace with your OpenWeatherMap API key
CITIES = [
    'Delhi', 'Mumbai', 'Bangalore', 'Kolkata', 'Chennai',
    'Coimbatore', 'Agra', 'Pune', 'Kochi', 'Jaipur'
]
CURRENT_URL = 'http://api.openweathermap.org/data/2.5/weather'
FORECAST_URL = 'http://api.openweathermap.org/data/2.5/forecast'
OUTPUT_FOLDER = 'static'
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# === MAIN LOOP ===
for idx, city in enumerate(CITIES, start=1):
    print(f"\n🔄 Processing {city}...")

    # ==== 1. CURRENT WEATHER ====
    current_params = {'q': city, 'appid': API_KEY, 'units': 'metric'}
    current_res = requests.get(CURRENT_URL, params=current_params)

    if current_res.status_code == 200:
        data = current_res.json()
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind_speed = data['wind']['speed']
        description = data['weather'][0]['description'].capitalize()

        # Create current weather bar chart
        fig, ax = plt.subplots()
        values = [temp, feels_like, humidity, pressure, wind_speed]
        labels = ['Temp (°C)', 'Feels Like', 'Humidity (%)', 'Pressure (hPa)', 'Wind (m/s)']
        colors = ['skyblue', 'lightgreen', 'orange', 'lightcoral', 'violet']

        ax.barh(labels, values, color=colors)
        ax.set_title(f'{city} – {description}', fontsize=12)
        ax.set_xlim([0, max(values) + 10])
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        ax.text(0.95, 0.01, f'Updated: {timestamp}', transform=ax.transAxes,
                fontsize=8, color='gray', ha='right')
        plt.tight_layout()
        file_current = f'dashboard_{idx}_{city}.png'
        plt.savefig(os.path.join(OUTPUT_FOLDER, file_current))
        plt.close()
        print(f'[✔] Current weather chart saved: {file_current}')
    else:
        print(f'[✘] Failed to fetch current weather for {city}')
        continue

    # ==== 2. 5-DAY FORECAST ====
    forecast_params = {'q': city, 'appid': API_KEY, 'units': 'metric'}
    forecast_res = requests.get(FORECAST_URL, params=forecast_params)

    if forecast_res.status_code == 200:
        forecast_data = forecast_res.json()
        forecasts = forecast_data['list']

        # Extract 5-day daily temperature at 12:00 PM
        dates = []
        temps = []
        for forecast in forecasts:
            dt_txt = forecast['dt_txt']
            if "12:00:00" in dt_txt:
                date = dt_txt.split()[0]
                temp_day = forecast['main']['temp']
                dates.append(date)
                temps.append(temp_day)

        # Create forecast temperature line chart
        plt.figure(figsize=(6, 4))
        plt.plot(dates, temps, marker='o', color='teal')
        plt.title(f'{city} – 5-Day Forecast (12PM Temp)', fontsize=12)
        plt.xlabel('Date')
        plt.ylabel('Temperature (°C)')
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        file_forecast = f'forecast_{idx}_{city}.png'
        plt.savefig(os.path.join(OUTPUT_FOLDER, file_forecast))
        plt.close()
        print(f'[✔] Forecast chart saved: {file_forecast}')
    else:
        print(f'[✘] Failed to fetch forecast for {city}')

print("\n✅ All charts generated successfully in 'static/' folder.")

