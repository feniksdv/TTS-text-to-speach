# V4
import os

import torch
from ruaccent import RUAccent

device = torch.device('cpu')
torch.set_num_threads(4)
local_file = 'model.pt'

if not os.path.isfile(local_file):
    torch.hub.download_url_to_file('https://models.silero.ai/models/tts/ru/v4_ru.pt',
                                   local_file)

model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
model.to(device)

file_path = 'test.txt'

accentizer = RUAccent()
accentizer.load(omograph_model_size='big_poetry', use_dictionary=True)


def read_file_in_chunks(file_path, chunk_size=800):
    with open(file_path, 'r') as file:
        remainder = ''
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                yield remainder
                break
            last_space = chunk.rfind(' ')
            if last_space != -1:
                yield remainder + chunk[:last_space]
                remainder = chunk[last_space + 1:]
            else:
                yield remainder + chunk
                remainder = ''


chunk_counter = 1
for chunk in read_file_in_chunks(file_path):
    chunk = accentizer.process_all(chunk)
    print(chunk)

    example_text = chunk
    sample_rate = 24000
    speaker = 'eugene'
    put_accent = False
    put_yo = False

    audio_path = f"silero_{chunk_counter}.wav"
    model.save_wav(text=example_text,
                   speaker=speaker,
                   sample_rate=sample_rate,
                   put_accent=put_accent,
                   put_yo=put_yo,
                   audio_path=audio_path)
    chunk_counter += 1
