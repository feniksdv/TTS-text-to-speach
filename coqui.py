# from TTS.api import TTS
#
# tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)
#
# file_path = 'test1.txt'
#
#
# def read_file_in_chunks(file_path, chunk_size=180):
#     with open(file_path, 'r') as file:
#         remainder = ''
#         while True:
#             chunk = file.read(chunk_size)
#             if not chunk:
#                 yield remainder
#                 break
#             last_space = chunk.rfind(' ')
#             if last_space != -1:
#                 yield remainder + chunk[:last_space]
#                 remainder = chunk[last_space + 1:]
#             else:
#                 yield remainder + chunk
#                 remainder = ''
#
#
# # generate speech by cloning a voice using default settings
# chunk_counter = 1
# for chunk in read_file_in_chunks(file_path):
#     text = chunk
#     audio_path = f"output_test{chunk_counter}.wav"
#     tts.tts_to_file(text=text,
#                     file_path=audio_path,
#                     speaker_wav="voice/dictor.mp3",
#                     language="ru",
#                     split_sentences=True
#                     )
#     chunk_counter += 1

import torch
from TTS.api import TTS

device = "cuda" if torch.cuda.is_available() else "cpu"

print(TTS().list_models())

tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2", progress_bar=False).to(device)

file_path = 'test.txt'
with open(file_path, 'r') as file:
    chunk = file.read()

tts.tts_to_file(
    text=chunk,
    speaker_wav="voice/dictor.mp3",
    language="ru",
    file_path="coqui.mp3",
    split_sentences=True
)
