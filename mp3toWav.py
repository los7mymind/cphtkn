from pydub import AudioSegment
import requests
import os


def download_and_convert_audio(url, save_path):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    response = requests.get(url)

    if response.status_code == 200:

        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Аудиофайл успешно загружен и сохранен в {save_path}")

        mp3_file = save_path
        wav_file = os.path.splitext(save_path)[0] + '.wav'
        sound = AudioSegment.from_mp3(mp3_file)
        sound.export(wav_file, format="wav")
        print(
            f"Аудиофайл успешно сконвертирован в WAV и сохранен в {wav_file}")

        os.remove(mp3_file)
        print(f"Исходный MP3 файл успешно удален")
    else:
        print("Ошибка при загрузке аудиофайла")


if __name__ == "__main__":
    audio_url = 'https://example.com/audio.mp3'

    save_path = 'audio/audio.mp3'

    download_and_convert_audio(audio_url, save_path)
