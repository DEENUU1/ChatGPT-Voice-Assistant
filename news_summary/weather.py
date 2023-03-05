from dataclasses import dataclass
import json

import openai
import aiohttp
from requests import get
import configparser


@dataclass
class WeatherInfo:
    temp: float
    feels_like: float
    wind_speed: float


class Weather:
    """ This class allows to work with OpenWeatherMap API to return weather data
        based on the user localization """

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.api_key = config.get('NEWS SUMMARIZER', 'weather_api_key')
        self.city_name = config.get('NEWS SUMMARIZER', 'city_name')

    def get_weather(self):
        base_url = 'http://api.openweathermap.org/data/2.5/weather?appid='
        url = (base_url + self.api_key + "&q=" + self.city_name + "&units=metric&lang=en")
        result = get(url)
        json_result = json.loads(result.content)

        if result.status_code == 200:
            weather_temp = json_result['main']['temp']
            weather_feels = json_result['main']['feels_like']
            wind_speed = json_result['wind']['speed']

            return WeatherInfo(
                temp=weather_temp,
                feels_like=weather_feels,
                wind_speed=wind_speed)
        else:
            raise Exception("Nie działa")


async def get_weather_conclusion() -> str:
    """ This method is taking a weather data and then AI is returning a decision
        on how to wear based on the weather """
    config = configparser.ConfigParser()
    config.read('config.ini')
    openai.api_key = config.get("NEWS SUMMARIZER", 'openai_api_key')
    weather = Weather()
    weather_info = weather.get_weather()
    async with aiohttp.ClientSession() as session:
        response = await session.post(
            "https://api.openai.com/v1/engines/text-davinci-003/completions",
            json={
                "prompt": f"Weather temperature is {weather_info.temp} Celsius degree"
                          f"the temperature feels like {weather_info.feels_like} "
                          f"and the wind speed is {weather_info.wind_speed}"
                          f"Tell me what temperature is right now, and tell me how can I dress for these conditions.",
                "temperature": 0.2,
                "max_tokens": 256,
                "stop": None
            },
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {openai.api_key}"
            }
        )
        response_data = await response.json()
        return response_data['choices'][0]['text']
