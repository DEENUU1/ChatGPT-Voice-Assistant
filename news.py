import json
import os

from dotenv import load_dotenv
from requests import get


load_dotenv()


class News:
    """ This class allows to return news urls """

    def __init__(self):
        self.api_key = os.getenv('NEWS_KEY')

    def _get_news_urls(self):
        base_url = f'https://newsapi.org/v2/top-headlines?country=PL&apiKey={self.api_key}'
        result = get(base_url)
        json_result = json.loads(result.content)
        articles = json_result['articles']

        if result.status_code == 200:
            return [article['url'] for article in articles]
        else:
            raise Exception("It doesn't work")

