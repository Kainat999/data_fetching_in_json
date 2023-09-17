import requests
import json

# my api key ... genrated by my account    openweathermap.org

API_KEY = "6dee1cebfab04c0f01810073f2ac480a"  

def fetching_dataof_city(city_name):
    web_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': API_KEY
    }

    response = requests.get(web_url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to fetch data for {city_name}. Return Status code: {response.status_code}")
        return None

def store_fetching_dataof_city(city_names):
    city_weather_data = {}

    for city_name in city_names:
        city_data = fetching_dataof_city(city_name)
        if city_data:
            city_weather_data[city_name] = city_data

    with open("weather_data.json", "w") as json_file:
        json.dump(city_weather_data, json_file, indent=4)

if __name__ == "__main__":
    #Example cities mai bad m ar add kr lon gi 
    cities = ["London", "Paris", "New York", "Tokyo"]

    store_fetching_dataof_city(cities)
