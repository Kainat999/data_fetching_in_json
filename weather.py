import asyncio
import aiohttp
import json

API_KEY = "6dee1cebfab04c0f01810073f2ac480a" 

async def fetch_data(city_name, session):
    web_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': API_KEY
    }

    async with session.get(web_url, params=params) as response:
        if response.status == 200:
            data = await response.json()
            return city_name, data
        else:
            print(f"Failed to fetch data for {city_name}. Return Status code: {response.status}")
            return city_name, None

async def fetch_all_data(city_names):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(city_name, session) for city_name in city_names]
        return await asyncio.gather(*tasks)

def store_fetching_data_of_city(city_data):
    city_weather_data = {city_name: data for city_name, data in city_data if data}

    with open("weather_data.json", "w") as json_file:
        json.dump(city_weather_data, json_file, indent=4)

if __name__ == "__main__":
    cities = ['New York', 
              'Hoboken', 
              'Hudson',  
              'Long Island City', 
              'Jersey City', 
              'Weehawken', 
              'Queensbridge Houses', 
              'Union City', 
              'West New York', 
              'Brooklyn', 
              'Kings', 
              'Manhattan', 
              'New York County', 
              'Guttenberg', 
              'Carnegie Hill', 
              'North Bergen', 
              'Secaucus', 
              'Bayonne', 
              'City Line', 
              'Fairview', 
              'East New York', 
              'Oak Island Junction', 
              'Cliffside Park', 
              'Bensonhurst', 
              'North Beach', 
              'Lyndhurst', 
              'Edgewater', 
              'Harrison', 
              'Kearny', 
              'Ridgefield', 
              'North Arlington', 
              'East Newark', 
              'Newark', 
              'Bronx County', 
              'Moonachie', 
              'Lyndhurst',
               'Coney Island', 
              'Palisades Park', 
              'Belleville', 
              'Rutherford']  

    loop = asyncio.get_event_loop()
    city_data = loop.run_until_complete(fetch_all_data(cities))
    store_fetching_data_of_city(city_data)
