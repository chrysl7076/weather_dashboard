import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

API_KEY = '389267a52ee7d80ab5340e2487061cd3'  # Replace with your OpenWeatherMap API key
CITIES = input("Enter city names separated by commas: ").split(',')
CITIES = [city.strip() for city in CITIES]

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

weather_data = []

for city in CITIES:
    params = {'q': city, 'appid': API_KEY, 'units': 'metric'}
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        weather_data.append({'City': city, 'Temperature (°C)': temp})
    else:
        print(f"⚠️ Failed to fetch weather for {city}")

# Create DataFrame
df = pd.DataFrame(weather_data)
df.to_csv("current_weather.csv", index=False)

# Plotting
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.barplot(x='City', y='Temperature (°C)', data=df, palette='viridis')
plt.title("Current Temperature by City")
plt.ylabel("Temperature (°C)")
plt.xlabel("City")
plt.tight_layout()
plt.savefig("static/dashboard.png")  # Save in static folder
plt.show()

print("✅ dashboard.png created in /static folder")
