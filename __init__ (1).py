import googletrans
import speech_recognition
import gtts
import playsound

# print(googletrans.LANGUAGES)
# print(googletrans.LANGCODES)

input_lang="hi"
output_lang="en"

recognizer=speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Speak Now")
    voice=recognizer.listen(source)
    text=recognizer.recognize_google(voice,language=input_lang)
    print(text)

translator=googletrans.Translator()
translator_text=translator.translate(text,dest=output_lang)
print(translator_text.text)
converted_audio=gtts.gTTS(translator_text.text,lang=output_lang)
converted_audio.save("Hello.mp3")
playsound.playsound("Hello.mp3")

