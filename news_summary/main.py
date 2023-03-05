import asyncio
from docx import Document
from summaryzer import return_article_summary
import configparser
from welcome import Welcome
from text_to_speech import return_speech
from speech_command import speech_command
from openai_async import get_openai_conclusion
from weather import Weather

async def main_async():
    # Configuration
    config = configparser.ConfigParser()
    config.read('config.ini')
    country_code = config.get('NEWS SUMMARIZER', 'country_code')
    user_name = config.get('NEWS SUMMARIZER', 'user_name')
    document = Document()
    welcome = Welcome()
    welcome_user = welcome.return_welcome_message(user_name)

    # Welcome massage
    print(welcome_user)
    return_speech(welcome_user)

    # Options based on the user decision
    while True:
        print("1. Weather information for today \n2. News summaries \n3. AI Conversation")
        # user_decision = input("> ")
        user_decision = speech_command()

        # Weather info
        if "weather" in user_decision:
            weather = Weather()
            weather_summary = weather.return_weather_summary()
            print(await get_openai_conclusion(weather_summary))
            return_speech(await get_openai_conclusion(weather_summary))
            continue

        # News summaries
        if "news" in user_decision:
            async for summary, article_url in return_article_summary(country_code):
                print(summary, article_url)
                return_speech(summary)
                document.add_paragraph(
                    summary + ' ' + article_url)
            document.save('news.docx')
            continue

        # Conversation with AI
        if "openai" or "ai" in user_decision:
            while True:
                command = speech_command()
                print(await get_openai_conclusion(command))
                return_speech(await get_openai_conclusion(command))

if __name__ == '__main__':
    asyncio.run(main_async())
