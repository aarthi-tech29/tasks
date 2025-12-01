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

# ========================Using API directly given the location latitude and longitude=================================================

# import os # used to read environment variables (your API key)
# import requests
# from dotenv import load_dotenv

# # Load variables from .env file
# load_dotenv()  # loads .env
# # api_key = os.getenv("OPENWEATHER_API_KEY")
# # print(api_key) # to get api key login https://openweathermap.org/-click your profile icon-Select My API keys

# # Store API key & location
# OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
# LAT = 8.741222    # Tirunelveli  # LAT = 28.6139 LON = 77.2090 - for Delhi
# LON = 77.694626    # Tirunelveli
# MIN_PLEASANT = 15  # °C
# MAX_PLEASANT = 25  # °C

# def should_go_for_walk():
#     if not OPENWEATHER_API_KEY:
#         raise RuntimeError("Set OPENWEATHER_API_KEY environment variable")

# # Build the weather API URL
#     url = (
#         "https://api.openweathermap.org/data/2.5/weather"
#         f"?lat={LAT}&lon={LON}&units=metric&appid={OPENWEATHER_API_KEY}"
#     )
# # Call the API - Fetch weather data
#     response = requests.get(url, timeout=10) #sends the request to the API
#     response.raise_for_status()
#     data = response.json() # converts the JSON response into a Python dictionary
#     # print(data)

# # Check the temperature
#     temp = data.get("main", {}).get("temp") 
#     temp_is_pleasant = isinstance(temp, (int, float)) and (MIN_PLEASANT <= temp <= MAX_PLEASANT)

# # Check if it's raining
#     weather = data.get("weather", [])
#     weather_main = weather[0].get("main", "").lower() if weather else ""
#     has_rain_field = bool(data.get("rain"))
#     is_raining = has_rain_field or weather_main in ("rain", "drizzle", "thunderstorm", "squall")

# # Final Decision: Walk or Not?
#     if (not is_raining) and temp_is_pleasant:
#         return {"suggestion": "Go for a walk", "reason": f"temp {temp}°C is pleasant and it is not raining."}
#     # else:
#     #     reasons = []
#     #     if is_raining:
#     #         reasons.append("it is raining")
#     #     if not temp_is_pleasant:
#     #         reasons.append(f"temp {temp}°C not pleasant (pleasant is {MIN_PLEASANT}-{MAX_PLEASANT}°C)")
#     #     return {"suggestion": "Do not go for a walk", "reason": " and ".join(reasons)}
#     else:
#         return {
#             "suggestion": "Do not go for a walk",
#             "reason": f"It is raining OR the temperature ({temp}°C) is not pleasant."
#         }

# if __name__ == "__main__":
#     result = should_go_for_walk()
#     print(result)
# =======================================Using API location only for India======================================================
import os
import requests
from dotenv import load_dotenv

# Load API key
load_dotenv()
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

MIN_PLEASANT = 15
MAX_PLEASANT = 25

def get_coordinates_from_city(city_name):
    """
    Convert city name to latitude & longitude using OpenWeather Geocoding API.
    Accepts only exact city name match.
    """
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},IN&limit=5&appid={OPENWEATHER_API_KEY}"
    response = requests.get(url, timeout=10)
    data = response.json()

    if not data:
        return None  # No city found

    # Accept only exact match (case-insensitive)
    for result in data:
        if result["name"].lower() == city_name.lower():
            return result["lat"], result["lon"]

    # If no exact match, reject
    return None

def get_auto_location():
    """
    Get current location automatically using IP geolocation.
    """
    url = "https://ipapi.co/json/"
    response = requests.get(url, timeout=10)
    data = response.json()
    return data["latitude"], data["longitude"], data["city"]

def should_go_for_walk(lat, lon):
    """
    Check weather and decide walking suggestion.
    """
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={OPENWEATHER_API_KEY}"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()

    temp = data.get("main", {}).get("temp")
    weather = data.get("weather", [])
    weather_main = weather[0].get("main", "").lower() if weather else ""

    is_pleasant = isinstance(temp, (int, float)) and (MIN_PLEASANT <= temp <= MAX_PLEASANT)
    is_raining = weather_main in ("rain", "drizzle", "thunderstorm")

    if is_pleasant and not is_raining:
        return {"suggestion": "Go for a walk", "reason": f"Temperature {temp}°C is pleasant and no rain."}
    else:
        return {"suggestion": "Do not go for a walk", "reason": f"Rain or unpleasant temperature ({temp}°C)."}

if __name__ == "__main__":
    if not OPENWEATHER_API_KEY:
        raise RuntimeError("Please set OPENWEATHER_API_KEY")

    user_city = input("Enter city name: ").strip()

    if user_city:
        result = get_coordinates_from_city(user_city)
        if result is None:
            print("Invalid city name. Please type the full correct city name.")
            exit()
        lat, lon = result
        print(f"Using location: {user_city}")
    else:
        lat, lon, auto_city = get_auto_location()
        print(f"Auto-detected location: {auto_city}")

    result = should_go_for_walk(lat, lon)
    print(result)
# ===============================================================================================
#  Using API any location(worldwide)
# ===============================================================================================
import os
import requests
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

MIN_PLEASANT = 15
MAX_PLEASANT = 25

def get_place_coordinates(place_name):
    """
    Use OpenWeather Geo API to get coordinates, country, and state info.
    Accepts only exact match for the name.
    """
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={place_name}&limit=10&appid={API_KEY}"
    response = requests.get(url, timeout=10).json()

    if not response:
        return None, "Place not found. Please type the FULL correct name."

    # Check exact match only
    for result in response:
        if result.get("name", "").strip().lower() == place_name.lower():
            lat = result.get("lat")
            lon = result.get("lon")
            state = result.get("state", "N/A")
            country = result.get("country", "N/A")
            matched_name = result.get("name")
            return {"lat": lat, "lon": lon, "state": state, "country": country, "name": matched_name}, None

    return None, "Exact place name not found. Please type the FULL correct name."


def get_weather(lat, lon):
    """
    Fetch weather data from OpenWeather Weather API using coordinates.
    """
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    response = requests.get(url, timeout=10).json()
    return response


def should_go_for_walk(temp, weather_status):
    """
    Decide whether to go for a walk based on temperature and weather.
    """
    is_pleasant = MIN_PLEASANT <= temp <= MAX_PLEASANT
    is_raining = weather_status.lower() in ["rain", "drizzle", "thunderstorm"]

    if is_pleasant and not is_raining:
        return "Go for a walk", f"Temperature {temp}°C is pleasant and not raining."
    else:
        return "Do not go for a walk", f"Rain or unpleasant temperature ({temp}°C)."


# ================= MAIN PROGRAM =================

if not API_KEY:
    raise RuntimeError("Please set OPENWEATHER_API_KEY in your .env file.")

place = input("Enter full place name (city/state/village/etc): ").strip()

if len(place) < 3:
    print("Please type at least 3 letters of a valid place name.")
    exit()


place_info, error = get_place_coordinates(place)

if error:
    print(error)
    exit()

# Fetch weather using coordinates
weather_data = get_weather(place_info["lat"], place_info["lon"])

temp = weather_data["main"]["temp"]
weather_status = weather_data["weather"][0]["main"]
suggestion, reason = should_go_for_walk(temp, weather_status)

print({
    "searched_input": place,
    "matched_place": place_info["name"],
    "state_or_province": place_info["state"],
    "country": place_info["country"],
    "temperature": temp,
    "weather": weather_status,
    "suggestion": suggestion,
    "reason": reason
})


