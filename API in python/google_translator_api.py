import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os
recog_1 = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
    print("Speak hello! to intiate the translation !")
    print("------------------------------------------")
    recog_1.adjust_for_ambient_noise(source, duration=0.2)
    audio = recog_1.listen(source)
    Mytext = recog_1.recognize_google(audio)
    Mytext = Mytext.lower()


if 'hello' in Mytext:
    translator = Translator()
    from_lang = 'en'
    to_lang = 'mr'

with mic as source:

    print("Speak a sentence...")
    recog_1.adjust_for_ambient_noise(source, duration=0.2)
    audio = recog_1.listen(source)
    get_sentence = recog_1.recognize_google(audio)
    try:
        print("Phase to be Translated :" + get_sentence)

        text_to_translate = translator.translate(get_sentence, src=from_lang, dest=to_lang)
        text = text_to_translate.text
        speak = gTTS(text=text, lang=to_lang, slow=False)
        speak.save("captured_voice.mp3")
        os.system("start captured_voice.mp3")

    except sr.UnknownValueError:
        print("Unable to Understand the Input")

    except sr.RequestError as e:
        print("Unable to provide Required Output".format(e))
