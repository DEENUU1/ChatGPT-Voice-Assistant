import asyncio
from docx import Document
from summaryzer import return_article_summary
import configparser
from welcome import Welcome
from text_to_speech import return_speech


async def main_async():
    config = configparser.ConfigParser()
    config.read('config.ini')
    country_code = config.get('NEWS SUMMARIZER', 'country_code')
    user_name = config.get('NEWS SUMMARIZER', 'user_name')

    document = Document()

    welcome = Welcome()
    welcome_user = welcome.return_welcome_message(user_name)
    welcome_weather = welcome.return_weather_info()

    print(welcome_user)
    return_speech(welcome_user)

    print(welcome_weather)
    return_speech(welcome_weather)

    async for summary, article_url in return_article_summary(country_code):
        print(summary, article_url)

        return_speech(summary)
        document.add_paragraph(
            summary + ' ' + article_url
        )

    document.save('news.docx')


if __name__ == '__main__':
    asyncio.run(main_async())