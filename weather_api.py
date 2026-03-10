import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# OpenWeatherMap API Key
API_KEY = "6e0dea41aa1d22c5f8c6ce5a87f8fc53"

# City Name
city = "Mumbai"

# API URL
url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"

# Send request
response = requests.get(url)

# Convert to JSON
data = response.json()

# Check if API returned correct data
if "list" not in data:
    print("API Error:", data)
    exit()

# Lists to store data
dates = []
temps = []
humidity = []

# Extract data
for item in data["list"]:
    dates.append(item["dt_txt"])
    temps.append(item["main"]["temp"])
    humidity.append(item["main"]["humidity"])

# Create dataframe
df = pd.DataFrame({
    "Date": dates,
    "Temperature": temps,
    "Humidity": humidity
})

# Plot graph
plt.figure(figsize=(12,6))

sns.lineplot(x="Date", y="Temperature", data=df, label="Temperature")
sns.lineplot(x="Date", y="Humidity", data=df, label="Humidity")

plt.xticks(rotation=45)

plt.title("Weather Data Visualization")
plt.xlabel("Date")
plt.ylabel("Values")

plt.tight_layout()

plt.show()
temps = []
humidity = []

for item in data["list"]:
    dates.append(item["dt_txt"])
    temps.append(item["main"]["temp"])
    humidity.append(item["main"]["humidity"])

df = pd.DataFrame({
    "Date": dates,
    "Temperature": temps,
    "Humidity": humidity
})

plt.figure(figsize=(12,6))

sns.lineplot(x="Date", y="Temperature", data=df, label="Temperature")
sns.lineplot(x="Date", y="Humidity", data=df, label="Humidity")

plt.xticks(rotation=45)

plt.title("Weather Data Visualization")
plt.xlabel("Date")
plt.ylabel("Values")

plt.tight_layout()
plt.show()