import pyttsx3


def return_speech(text: str):
    """ This function allows to convert text to speech
        For now only in english """
    engine = pyttsx3.init()
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[1].id)
    engine.say(text)
    engine.runAndWait()


