from datetime import datetime
import calendar
from weather import Weather


class Welcome:
    """ This class is returning welcome messages """
    @staticmethod
    def _get_current_time() -> str:
        """ This method is returning local time """
        get_time = datetime.now()
        return get_time.strftime("%H:%M")

    @staticmethod
    def _get_current_data() -> str:
        """ This method is returning local date """
        get_date = datetime.today()
        return calendar.day_name[get_date.weekday()]

    def return_welcome_message(self, user_name: str) -> str:
        """ This method is returning welcome message """
        message = f"Welcome {user_name} today is {self._get_current_data()}" \
                  f" {self._get_current_time()}. You are about to hear today's " \
                  f"news release. Have a good day and see you later! "
        return message