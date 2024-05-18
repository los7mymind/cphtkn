from pydub import AudioSegment, silence
import noisereduce as nr
import numpy as np
import whisper


# Загрузка аудио файла
audio = AudioSegment.from_wav("input.wav")

# Получение фреймов в виде массива numpy
samples = np.array(audio.get_array_of_samples())

# Применение шумоподавления
reduced_noise = nr.reduce_noise(y=samples, sr=audio.frame_rate)

# Конвертация обратно в AudioSegment
reduced_noise_audio = audio._spawn(reduced_noise.astype(np.int16).tobytes())


# Удаление тишины из аудио
chunks = silence.split_on_silence(reduced_noise_audio, 
                                  min_silence_len=500,  # минимальная длительность тишины для ее удаления (в миллисекундах)
                                  silence_thresh=-60  # порог тишины в децибелах
                                 )

# Объединение всех фрагментов обратно в одно аудио
processed_audio = AudioSegment.empty()
for chunk in chunks:
    processed_audio += chunk

# Сохранение обработанного аудио
processed_audio.export("output.wav", format="wav")


# Загрузка модели Whisper
model = whisper.load_model("base")

# Распознавание речи
result = model.transcribe("output.wav", language="ru")

# Получение распознанного текста
recognized_text = result["text"]
print("Распознанный текст:", recognized_text)


with open("output.txt", "w", encoding="utf-8") as text_file:
    text_file.write(recognized_text)
