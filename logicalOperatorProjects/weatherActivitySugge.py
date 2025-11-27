# 36.Weather-Based Activity Suggestion: Suggest "Go for a walk" if it is NOT (!) raining AND (&&) the temperature is pleasant.

# Weather-Based Activity Suggestion

# print("----- Weather-Based Activity Suggestion -----")

# # Input
# is_raining = input("Is it raining? (yes/no): ").lower()
# temperature = float(input("Enter current temperature (°C): "))

# # Define pleasant temperature range
# pleasant_min = 20
# pleasant_max = 30

# # Suggest activity
# if is_raining != "yes" and pleasant_min <= temperature <= pleasant_max:
#     print("Go for a walk!")
# else:
#     print("Better to stay indoors")

# ========================Using API=================================================
import os # used to read environment variables (your API key)
import requests
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()  # loads .env
# api_key = os.getenv("OPENWEATHER_API_KEY")
# print(api_key) # to get api key login https://openweathermap.org/-click your profile icon-Select My API keys

# Store API key & location
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
LAT = 8.741222    # Tirunelveli  # LAT = 28.6139 LON = 77.2090 - for Delhi
LON = 77.694626    # Tirunelveli
MIN_PLEASANT = 15  # °C
MAX_PLEASANT = 25  # °C

def should_go_for_walk():
    if not OPENWEATHER_API_KEY:
        raise RuntimeError("Set OPENWEATHER_API_KEY environment variable")

# Build the weather API URL
    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?lat={LAT}&lon={LON}&units=metric&appid={OPENWEATHER_API_KEY}"
    )
# Call the API - Fetch weather data
    response = requests.get(url, timeout=10) #sends the request to the API
    response.raise_for_status()
    data = response.json() # converts the JSON response into a Python dictionary
    # print(data)

# Check the temperature
    temp = data.get("main", {}).get("temp") 
    temp_is_pleasant = isinstance(temp, (int, float)) and (MIN_PLEASANT <= temp <= MAX_PLEASANT)

# Check if it's raining
    weather = data.get("weather", [])
    weather_main = weather[0].get("main", "").lower() if weather else ""
    has_rain_field = bool(data.get("rain"))
    is_raining = has_rain_field or weather_main in ("rain", "drizzle", "thunderstorm", "squall")

# Final Decision: Walk or Not?
    if (not is_raining) and temp_is_pleasant:
        return {"suggestion": "Go for a walk", "reason": f"temp {temp}°C is pleasant and it is not raining."}
    # else:
    #     reasons = []
    #     if is_raining:
    #         reasons.append("it is raining")
    #     if not temp_is_pleasant:
    #         reasons.append(f"temp {temp}°C not pleasant (pleasant is {MIN_PLEASANT}-{MAX_PLEASANT}°C)")
    #     return {"suggestion": "Do not go for a walk", "reason": " and ".join(reasons)}
    else:
        return {
            "suggestion": "Do not go for a walk",
            "reason": f"It is raining OR the temperature ({temp}°C) is not pleasant."
        }

if __name__ == "__main__":
    result = should_go_for_walk()
    print(result)
