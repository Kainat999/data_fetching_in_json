import asyncio
import aiohttp
import json

API_KEY = "6dee1cebfab04c0f01810073f2ac480a"

async def fetch_data(session, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    async with session.get(url) as response:
        data = await response.json()
        return city, data

async def fetch_all_data(cities):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session, city) for city in cities]
        results = await asyncio.gather(*tasks)
        return dict(results)

if __name__ == "__main__":
    cities = [
        'New York', 'Hoboken', 'Hudson', 'Long Island City', 'Jersey City', 'Weehawken',
        'Queensbridge Houses', 'Union City', 'West New York', 'Brooklyn', 'Kings', 'Manhattan',
        'New York County', 'Guttenberg', 'Carnegie Hill', 'North Bergen', 'Secaucus', 'Bayonne',
        'City Line', 'Fairview', 'East New York', 'Oak Island Junction', 'Cliffside Park',
        'Bensonhurst', 'North Beach', 'Lyndhurst', 'Edgewater', 'Harrison', 'Kearny', 'Ridgefield',
        'North Arlington', 'East Newark', 'Newark', 'Bronx County', 'Moonachie', 'Lyndhurst',
        'Coney Island', 'Palisades Park', 'Belleville', 'Rutherford'
    ]

    loop = asyncio.get_event_loop()
    weather_data = loop.run_until_complete(fetch_all_data(cities))

    with open("weather_data.json", "w") as json_file:
        json.dump(weather_data, json_file, indent=4)
