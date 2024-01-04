import pyttsx3

text_file = open('test.txt', 'r')
data = text_file.read()

tts = pyttsx3.init()

voices = tts.getProperty('voices')

# Задать голос по умолчанию
tts.setProperty('voice', 'com.apple.voice.compact.ru-RU.Milena')

tts.setProperty("rate", 150)
tts.setProperty("volume", 1)
# tts.say(data)

tts.save_to_file(data, 'pyttsx3.wav')
tts.runAndWait()

text_file.close()
