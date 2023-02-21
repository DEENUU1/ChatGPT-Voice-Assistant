import json
import os
from dotenv import load_dotenv
from requests import get
from bs4 import BeautifulSoup
from openAI import get_openAI_data
import re

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
            return [article['url'] for article in articles]
        else:
            raise Exception("It doesn't work")

    def get_html_text(self):
        articles = []
        for url in self.get_news():
            result = get(url)
            soup = BeautifulSoup(result.content, 'html.parser')
            text = re.sub(r'\n\s*\n', r'\n\n', soup.get_text().strip(), flags=re.M)[:4049]
            if len(text) >= 4097:
                del text
            else:
                articles.append([text])
        return articles

    def summary(self):
        summaries = []
        for article in self.get_html_text():
            summary = get_openAI_data(article)
            summaries.append([summary])
        return summaries

obj = News()
print(obj.summary())