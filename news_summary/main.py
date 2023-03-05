import asyncio
from docx import Document
from summaryzer import return_article_summary
import configparser
from welcome import Welcome
from text_to_speech import return_speech
from weather import get_weather_conclusion


async def main_async():
    config = configparser.ConfigParser()
    config.read('config.ini')
    country_code = config.get('NEWS SUMMARIZER', 'country_code')
    user_name = config.get('NEWS SUMMARIZER', 'user_name')
    document = Document()
    welcome = Welcome()
    welcome_user = welcome.return_welcome_message(user_name)

    print(welcome_user)
    return_speech(welcome_user)

    while True:
        print("1. Weather information for today \n2. News summaries")
        user_decision = input("> ")

        if user_decision == "1":
            print(await get_weather_conclusion())
            return_speech(await get_weather_conclusion())
            continue

        if user_decision == "2":
            async for summary, article_url in return_article_summary(country_code):
                print(summary, article_url)
                return_speech(summary)
                document.add_paragraph(
                    summary + ' ' + article_url)
            document.save('news.docx')
            continue

if __name__ == '__main__':
    asyncio.run(main_async())
