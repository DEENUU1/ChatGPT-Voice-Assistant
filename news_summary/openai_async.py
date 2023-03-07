import openai
import aiohttp
import configparser


async def get_openai_conclusion(prompt) -> str:
    """ This is a async function that allows to make async request to the openai API """
    config = configparser.ConfigParser()
    config.read('config.ini')
    openai.api_key = config.get("NEWS SUMMARIZER", 'openai_api_key')
    try:
        async with aiohttp.ClientSession() as session:
            response = await session.post(
                "https://api.openai.com/v1/engines/text-davinci-003/completions",
                json={
                    "prompt": prompt,
                    "temperature": 0.2,
                    "max_tokens": 256,
                    "stop": None
                },
                headers = {
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {openai.api_key}"
                }
            )
            response_data = await response.json()
            return response_data['choices'][0]['text']
    except aiohttp.ClientConnectorError:
        return "No internet connection. Try again."
