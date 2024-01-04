# -*- coding: cp1251 -*-

import time

from gtts import gTTS

with open("test.txt", "r") as file:
    text = file.read()

total_chars = len(text)
processed_chars = 0

audio = gTTS(text=text, lang="ru", slow=False, tld="com.ru")

# Имитация процесса преобразования
for char in text:
    # Примерное отображение прогресса
    processed_chars += 1
    percentage = int(processed_chars / total_chars * 100)
    print(f"\rProcessing: {percentage}%", end="")
    time.sleep(0.01)  # Имитация обработки

# Сохранение аудиофайла
audio.save("gtts.mp3")
