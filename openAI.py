import os
import openai
from dotenv import load_dotenv

load_dotenv()


def get_openAI_data(article_text):
    openai.api_key = os.getenv('OPENAIKEY')
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=f'Podsumuj ten artykuł w języku polskim w około 500 słówach """ {article_text} """ ',
      temperature=0.5,
      max_tokens=256,
      top_p=1,
      stop=None,
    )

    return response['choices'][0]['text']

