import os
import openai
from dotenv import load_dotenv
from news import NewsScraper

load_dotenv()


def get_openAI_data(article_text):
    openai.api_key = os.getenv('OPENAIKEY')
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=f'Podsumuj ten artykuł w języku polskim w około 50 słówach """ {article_text} """ ',
      temperature=0.5,
      max_tokens=256,
      top_p=1,
      stop=None,
    )

    return response['choices'][0]['text']


def return_article_summary():
    news_scraper = NewsScraper()
    articles = news_scraper.get_news_urls()

    summaries = []
    for article in articles:
        summary = get_openAI_data(article)
        summaries.append([summary])
    return summaries
