weather_data = {
    "London": {"temperature": "15°C", "conditions": "Cloudy", "wind_speed": "5 km/h", "humidity": "80%"},
    "New York": {"temperature": "20°C", "conditions": "Sunny", "wind_speed": "10 km/h", "humidity": "50%"},
    "Tokyo": {"temperature": "18°C", "conditions": "Rainy", "wind_speed": "7 km/h", "humidity": "90%"},
    "Sydney": {"temperature": "22°C", "conditions": "Windy", "wind_speed": "15 km/h", "humidity": "60%"},
    "Paris": {"temperature": "17°C", "conditions": "Foggy", "wind_speed": "3 km/h", "humidity": "85%"},
    "Berlin": {"temperature": "14°C", "conditions": "Partly Cloudy", "wind_speed": "6 km/h", "humidity": "70%"},
    "Madrid": {"temperature": "25°C", "conditions": "Sunny", "wind_speed": "12 km/h", "humidity": "40%"},
    "Rome": {"temperature": "28°C", "conditions": "Clear", "wind_speed": "8 km/h", "humidity": "50%"},
    "Moscow": {"temperature": "10°C", "conditions": "Rainy", "wind_speed": "4 km/h", "humidity": "75%"},
    "Beijing": {"temperature": "22°C", "conditions": "Sunny", "wind_speed": "14 km/h", "humidity": "55%"},
    "Ottawa": {"temperature": "12°C", "conditions": "Cloudy", "wind_speed": "3 km/h", "humidity": "80%"},
    "Brasilia": {"temperature": "30°C", "conditions": "Sunny", "wind_speed": "5 km/h", "humidity": "55%"},
    "Cairo": {"temperature": "33°C", "conditions": "Hot", "wind_speed": "11 km/h", "humidity": "20%"},
    "Buenos Aires": {"temperature": "21°C", "conditions": "Clear", "wind_speed": "9 km/h", "humidity": "70%"},
    "Abuja": {"temperature": "28°C", "conditions": "Sunny", "wind_speed": "8 km/h", "humidity": "65%"},
    "New Delhi": {"temperature": "30°C", "conditions": "Hazy", "wind_speed": "6 km/h", "humidity": "50%"},
    "Kuala Lumpur": {"temperature": "29°C", "conditions": "Rainy", "wind_speed": "12 km/h", "humidity": "85%"},
    "Cape Town": {"temperature": "20°C", "conditions": "Windy", "wind_speed": "13 km/h", "humidity": "70%"},
    "Seoul": {"temperature": "17°C", "conditions": "Clear", "wind_speed": "10 km/h", "humidity": "65%"},
    "Lagos": {"temperature": "27°C", "conditions": "Cloudy", "wind_speed": "8 km/h", "humidity": "80%"},
    "Jakarta": {"temperature": "31°C", "conditions": "Rainy", "wind_speed": "14 km/h", "humidity": "90%"},
    "Lima": {"temperature": "18°C", "conditions": "Foggy", "wind_speed": "5 km/h", "humidity": "85%"},
    "Mexico City": {"temperature": "20°C", "conditions": "Clear", "wind_speed": "10 km/h", "humidity": "65%"},
    "Nairobi": {"temperature": "25°C", "conditions": "Cloudy", "wind_speed": "6 km/h", "humidity": "75%"},
    "Dhaka": {"temperature": "30°C", "conditions": "Sunny", "wind_speed": "8 km/h", "humidity": "60%"},
    "Caracas": {"temperature": "28°C", "conditions": "Rainy", "wind_speed": "9 km/h", "humidity": "80%"},
    "Helsinki": {"temperature": "9°C", "conditions": "Partly Cloudy", "wind_speed": "5 km/h", "humidity": "75%"},
    "Copenhagen": {"temperature": "12°C", "conditions": "Clear", "wind_speed": "7 km/h", "humidity": "70%"},
    "Reykjavik": {"temperature": "7°C", "conditions": "Windy", "wind_speed": "10 km/h", "humidity": "80%"},
    "Stockholm": {"temperature": "13°C", "conditions": "Cloudy", "wind_speed": "4 km/h", "humidity": "60%"},
    "Jakarta": {"temperature": "31°C", "conditions": "Rainy", "wind_speed": "14 km/h", "humidity": "90%"},
    "Addis Ababa": {"temperature": "23°C", "conditions": "Partly Cloudy", "wind_speed": "8 km/h", "humidity": "70%"},
    "Tehran": {"temperature": "26°C", "conditions": "Sunny", "wind_speed": "5 km/h", "humidity": "40%"},
    "Amman": {"temperature": "24°C", "conditions": "Sunny", "wind_speed": "12 km/h", "humidity": "55%"},
    "Baghdad": {"temperature": "30°C", "conditions": "Hot", "wind_speed": "15 km/h", "humidity": "20%"},
    "Baku": {"temperature": "28°C", "conditions": "Sunny", "wind_speed": "8 km/h", "humidity": "60%"},
    "Kigali": {"temperature": "22°C", "conditions": "Cloudy", "wind_speed": "5 km/h", "humidity": "75%"},
    "Kinshasa": {"temperature": "30°C", "conditions": "Rainy", "wind_speed": "10 km/h", "humidity": "85%"},
}

print("Welcome to the Weather App! 🌦️")
print("You can check the weather for cities around the world.")

city = input("Enter the city name: ")

if city in weather_data:
    weather = weather_data[city]
    print(f"\nWeather for {city}:")
    print(f"Temperature: {weather['temperature']}")
    print(f"Conditions: {weather['conditions']}")
    print(f"Wind Speed: {weather['wind_speed']}")
    print(f"Humidity: {weather['humidity']}")
else:
    print(f"\nCity '{city}' not found. Please ensure the case matches exactly.")

print("\nThank you for using the Weather App! 🌞")