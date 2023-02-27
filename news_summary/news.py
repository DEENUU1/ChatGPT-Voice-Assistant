import json

import configparser
from requests import get


class News:
    """ This class allows to return news urls """

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.api_key = config.get('NEWS SUMMARIZER', 'news_api_key')

    def _get_news_urls(self, country_code: str):
        base_url = f'https://newsapi.org/v2/top-headlines?country={country_code}&apiKey={self.api_key}'
        result = get(base_url)
        json_result = json.loads(result.content)
        articles = json_result['articles']

        if result.status_code == 200:
            return [article['url'] for article in articles]
        else:
            raise Exception("It doesn't work")

