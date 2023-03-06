# ChatGPT Voice Assistant ##
## Your desktop second brain ##

The application allows you to talk to the DaVinci-003 model by voice. You can talk to artificial intelligence thanks to speech recognition, listen to summaries of press articles downloaded from NewsAPI, and find out what the weather is like today and what you should wear.
The application is still in the development phase, I am still adding new features.

### Technology that I used:
- Python
- APIs:
    - openai API
    - NEWS API 
    - ocrwebservice API

## Demo

- [VIDEO DEMO ON YOUTUBE](https://youtu.be/yFJaFXsPRnk)

<img src="/files/2.gif.gif"/>
<img src="/files/1.png"/>

## FEATURES:

- Converting images into text and creating notes.
- Deleting unnecessary files from your computer.
- Turning off your keyboard to make it easier to clean.
- Summaries for Twitter posts.

## VERSIONS:

### V0.1:
- Downloading data from news API and returning summaries by chatGPT
- Text into speech
- Config file 
- Saving summaries to a .docx file

### V0.2: 
- Adding a name to the config file
- Returning local time and date
- Returning local weather information

### V0.3:
- Voice integration USER <-> PROGRAM
- Drawing conclusions from weather information.
- Handling Exceptions
- Explaining a code
- Voice chat with ChatGPT using speech recognizer

## Documentation FOR. EXE VERSION

1. Download the .exe version of the project from the newest release

2. Open the config file and choose your language, and country code (for example US/DE/PL)

3. Go to this website https://openai.com/api/ and create your API key, then paste it inside openai_api_key=<HERE>

```
open_api_key=asdas8d8as8
```

4. Go to this website https://newsapi.org/ and create your API key, then paste it inside 
news_api_key=<HERE>

```
news_api_key=dasd8asasd8
```

5. Go to this website https://openweathermap.org/api and create your API key (You gonna wait 1-3 hours) then paste it inside
weather_api_key=<HERE>

```
weather_api_key=dasdads8
```

6. Go to this website https://www.onlineocr.net/service/ocrwebservice and create an account, then paste information inside the config file.

```
ocr_name=ASDDd
image_to_text_licence=asdasd
```

7. Now you can run main.exe 



## Documentation 

If you wanna work with the code you can:

1. Clone the GitHub repository

```
git clone https://github.com/DEENUU1/news-summarizer.git
```

2. Install all packages

``` 
pip -r install requirements.txt
```





## License

[MIT](https://choosealicense.com/licenses/mit/)

