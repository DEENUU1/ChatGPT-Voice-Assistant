import os
import openai
from dotenv import load_dotenv
import asyncio

load_dotenv()


async def get_openAI_data(url):
    openai.api_key = os.getenv('OPENAIKEY')
    response = await openai.Completion.create(
      model="text-davinci-003",
      prompt=f"Summarize the content of {url}",
      temperature=0.5,
      max_tokens=256,
      top_p=1,
      stop=None,
    )

    return response.choinces[0].text
