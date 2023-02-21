import json
import os
from dataclasses import dataclass

from dotenv import load_dotenv
from requests import get

load_dotenv()


@dataclass()
class NewsInfo:
    title: str
    url: str


class News:
    """ This class allows to return news """

    def __init__(self):
        self.api_key = os.getenv('NEWS_KEY')

    def get_news(self, country_code):
        base_url = f'https://newsapi.org/v2/top-headlines?country={country_code}&apiKey={self.api_key}'
        result = get(base_url)
        json_result = json.loads(result.content)
        articles = json_result['articles']

        if result.status_code == 200:
            article_list = []
            for article in articles:
                article_title = article['title']
                article_url = article['url']

                article_list.append(NewsInfo(
                                    title=article_title,
                                    url=article_url
                ))

            return article_list
        return Exception("It doesn't work")


obj = News()
print(obj.get_news('PL'))