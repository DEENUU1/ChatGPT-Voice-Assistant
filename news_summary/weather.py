from dataclasses import dataclass
import json

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

    def return_weather_summary(self):
        prompt = f"Weather temperature is {str(int(round(self.get_weather().temp, 1)))} Celsius degree " \
                 f"the temperature feels like {str(int(round(self.get_weather().feels_like, 1)))}" \
                 f"and the wind speed is {str(int(round(self.get_weather().wind_speed, 1)))}" \
                 f"Tell me what temperature is right now, and tell me how can I dress for these conditions."
        return prompt





