from pydub import AudioSegment
import os

def convert_mp3_to_wav(file_path: str) -> str:
    """
    Конвертирует MP3 файл в WAV и сохраняет его.
    
    :param file_path: Путь к MP3 файлу.
    :return: Путь к сконвертированному WAV файлу.
    """
    print(f"Начало конвертации файла {file_path} в формат WAV.")
    wav_file = os.path.splitext(file_path)[0] + '.wav'
    sound = AudioSegment.from_mp3(file_path)
    sound.export(wav_file, format="wav")
    print(f"Файл успешно конвертирован в {wav_file}.")
    return wav_file

def save_audio_file(file_path: str, audio_data: bytes):
    """
    Сохраняет аудиоданные в файл.
    
    :param file_path: Путь к файлу, куда будут сохранены аудиоданные.
    :param audio_data: Содержимое аудиофайла в байтах.
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'wb') as file:
        file.write(audio_data)
    print(f"Файл успешно сохранен в {file_path}.")
    return file_path
