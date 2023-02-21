import json
import os
from dotenv import load_dotenv
from requests import get
from bs4 import BeautifulSoup
import re

load_dotenv()


class News:
    """ This class allows to return news """

    def __init__(self):
        self.api_key = os.getenv('NEWS_KEY')

    def get_news_urls(self):
        base_url = f'https://newsapi.org/v2/top-headlines?country=PL&apiKey={self.api_key}'
        result = get(base_url)
        json_result = json.loads(result.content)
        articles = json_result['articles']

        if result.status_code == 200:
            return [article['url'] for article in articles]
        else:
            raise Exception("It doesn't work")


class NewsScraper(News):
    """ This class allows to scrape data from the urls """

    def get_html_text(self):
        articles = []
        for url in self.get_news_urls():
            result = get(url)
            soup = BeautifulSoup(result.content, 'html.parser')
            text = re.sub(r'\n\s*\n', r'\n\n', soup.get_text().strip(), flags=re.M)[:4049]
            articles.append([text])
        return articles


    # def return_article_summary(self):
    #     summaries = []
    #     for article in self.get_html_text():
    #         summary = get_openAI_data(article)
    #         summaries.append([summary])
    #     return summaries
