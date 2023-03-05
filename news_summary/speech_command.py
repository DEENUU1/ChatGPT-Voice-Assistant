import speech_recognition


def speech_command():
    """ THis function allows to return text from user's speech """
    recognizer = speech_recognition.Recognizer()
    while True:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                text = recognizer.recognize_google(audio)
                text = text.lower()
                return text

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            continue



