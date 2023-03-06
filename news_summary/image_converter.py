# import cv2
# from pytesseract import pytesseract
# import os
# from PIL import Image
#
#
# SOURCE_PATH = 'images/Screenshot_1.png'
# TESSERACT_PATH = 'tesseract/tesseract.exe'
#
#
# def image_to_text():
#     image = Image.open(SOURCE_PATH)
#     pytesseract.tesseract_cmd = TESSERACT_PATH
#     text = pytesseract.image_to_string(image, lang='pol')
#     return text
#
# print(image_to_text())


import requests
import json
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

LICENSE_CODE = config.get("NEWS SUMMARIZER", "image_to_text_licence")
USERNAME = "KACPER"


def image_to_text(image_name: str) -> str:
    with open(f'images/{image_name}', 'rb') as image_file:
        image_data = image_file.read()

    base_url = "https://www.ocrwebservice.com/restservices/processDocument?gettext=true&language=polish"
    request = requests.post(base_url, data=image_data, auth=(
        USERNAME, LICENSE_CODE
    ))
    response = json.loads(request.content)
    return response

