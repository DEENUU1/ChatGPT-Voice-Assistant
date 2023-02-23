import asyncio
from docx import Document
from summaryzer import return_article_summary
import pyttsx3
import configparser


def return_speech(summary: str):
    engine = pyttsx3.init()
    engine.say(summary)
    engine.runAndWait()


async def main_async():
    config = configparser.ConfigParser()
    config.read('config.ini')
    language = config.get('NEWS SUMMARIZER', 'language')
    country_code = config.get('NEWS SUMMARIZER', 'country_code')

    document = Document()

    async for summary, article_url in return_article_summary(country_code, language):
        print(summary, article_url)

        return_speech(summary)
        document.add_paragraph(
            summary + ' ' + article_url
        )

    document.save('news.docx')

if __name__ == '__main__':
    asyncio.run(main_async())