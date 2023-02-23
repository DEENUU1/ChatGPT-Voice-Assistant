import os

import aiohttp
import openai
import configparser

from news import News


async def get_openAI_summary(article_url: str, language: str):
    config = configparser.ConfigParser()
    config.read('config.ini')
    openai.api_key = config.get('NEWS SUMMARIZER', 'openai_api_key')
    async with aiohttp.ClientSession() as session:
        response = await session.post(
            "https://api.openai.com/v1/engines/text-davinci-003/completions",
            json={
                "prompt": f'Podsumuj ten artykuł w języku {language} w około 100 słowach """ {article_url} """" ',
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


async def return_article_summary(country_code: str, language: str):
    news = News()
    article_urls = news._get_news_urls(country_code)

    summaries = []
    for article_url in article_urls:

        summary = await get_openAI_summary(article_url, language)
        summaries.append([summary])
        yield summary, article_url
