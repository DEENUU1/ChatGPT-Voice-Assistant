import asyncio
from docx import Document
from summaryzer import return_article_summary
import pyttsx3


def return_speech(summary):
    engine = pyttsx3.init()
    engine.say(summary)
    engine.runAndWait()


async def main_async():
    document = Document()

    async for summary, article_url in return_article_summary():
        print(summary, article_url)

        return_speech(summary)

        document.add_paragraph(
            summary + ' ' + article_url
        )

    document.save('news.docx')

if __name__ == '__main__':
    asyncio.run(main_async())