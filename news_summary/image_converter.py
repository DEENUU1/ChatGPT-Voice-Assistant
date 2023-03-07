import requests
import json
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

LICENSE_CODE = config.get("NEWS SUMMARIZER", "image_to_text_licence")
USERNAME = "KACPER"


def image_to_text(image_name: str, language: str) -> str:
    """ This function allows to convert image into text with OCR API """
    with open(f'images/{image_name}', 'rb') as image_file:
        image_data = image_file.read()

    base_url = f"https://www.ocrwebservice.com/restservices/processDocument?gettext=true&language={language}"
    request = requests.post(base_url, data=image_data, auth=(
        USERNAME, LICENSE_CODE
    ))
    response = json.loads(request.content)
    return response

