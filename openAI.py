import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAIKEY')

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Hej co u ciebie?",
  temperature=0,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)
