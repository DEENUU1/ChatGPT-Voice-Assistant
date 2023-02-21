import json
import os
from dotenv import load_dotenv
from requests import get
from bs4 import BeautifulSoup

load_dotenv()


class News:
    """ This class allows to return news """

    def __init__(self):
        self.api_key = os.getenv('NEWS_KEY')

    def get_news(self):
        base_url = f'https://newsapi.org/v2/top-headlines?country=PL&apiKey={self.api_key}'
        result = get(base_url)
        json_result = json.loads(result.content)
        articles = json_result['articles']

        if result.status_code == 200:
            return [article['url'] for article in articles[:1]]
        else:
            raise Exception("It doesn't work")

    def get_html_text(self):
        html_text = []
        for url in self.get_news():
            result = get(url)
            soup = BeautifulSoup(result.content, 'html.parser')
            text = soup.get_text()
            html_text.append(text)
        return html_text
#
# obj = News()
# print(obj.get_html_text())