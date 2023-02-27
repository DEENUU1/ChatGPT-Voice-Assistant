from datetime import datetime
import calendar
from weather import Weather


class Welcome:
    @staticmethod
    def _get_current_time() -> str:
        get_time = datetime.now()
        return get_time.strftime("%H:%M")

    @staticmethod
    def _get_current_data() -> str:
        get_date = datetime.today()
        return calendar.day_name[get_date.weekday()]

    def return_welcome_message(self, user_name: str) -> str:
        message = f"Welcome {user_name} today is {self._get_current_data()}" \
                  f" {self._get_current_time()}. You are about to hear today's" \
                  f"news release. Have a good day and see you later! "
        return message

    @staticmethod
    def return_weather_info() -> str:
        weather = Weather()
        message = f"Today is {weather.get_weather().temp} celsius degrees" \
                  f"sensed temperature is equal to {weather.get_weather().feels_like} celsius degrees" \
                  f"and the wind speed {weather.get_weather().wind_speed} kilometer per hour"
        return message