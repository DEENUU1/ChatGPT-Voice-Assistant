import os

import aiohttp
import openai
from dotenv import load_dotenv

from news import News

load_dotenv()

async def get_openAI_data_async(article_text):
    openai.api_key = os.getenv('OPEN_AI_KEY')
    async with aiohttp.ClientSession() as session:
        response = await session.post(
            "https://api.openai.com/v1/engines/text-davinci-003/completions",
            json={
                "prompt": f'Podsumuj ten artykuł w języku polskim w około 100 słowach """ {article_text} """" ',
                "temperature": 0.2,
                "max_tokens": 256,
                "stop": None
            },
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {openai.api_key}"
            }
        )
        response_data = await response.json()
        return response_data['choices'][0]['text']



async def return_article_summary_async():
    news = News()
    articles = news.get_news_urls()

    summaries = []
    for article in articles:
        summary = await get_openAI_data_async(article)
        summaries.append([summary])
        yield summary
