import asyncio
from docx import Document
from summaryzer import return_article_summary
import pyttsx3
import configparser
from datetime import datetime
import calendar


def return_speech(summary: str):
    engine = pyttsx3.init()
    engine.say(summary)
    engine.runAndWait()


def welcome_message(user_name: str) -> str:
    get_time = datetime.now()
    get_date = datetime.today()
    current_date = calendar.day_name[get_date.weekday()]
    current_time = get_time.strftime("%H:%M")
    message = f"Welcome {user_name} today is {current_date} {current_time}" \
              f" You are about to hear today's news release. Have a good day and see" \
              f" you later!"
    return message


async def main_async():
    config = configparser.ConfigParser()
    config.read('config.ini')
    language = config.get('NEWS SUMMARIZER', 'language')
    country_code = config.get('NEWS SUMMARIZER', 'country_code')
    user_name = config.get('NEWS SUMMARIZER', 'user_name')

    document = Document()

    welcome_user = welcome_message(user_name)
    print(welcome_user)
    return_speech(welcome_user)

    async for summary, article_url in return_article_summary(country_code, language):
        print(summary, article_url)

        return_speech(summary)
        document.add_paragraph(
            summary + ' ' + article_url
        )

    document.save('news.docx')


if __name__ == '__main__':
    asyncio.run(main_async())
