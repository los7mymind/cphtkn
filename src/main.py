from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from utils.mp3_to_wav import convert_mp3_to_wav, save_audio_file
import mimetypes
import os

app = FastAPI()

class PredictionResponse(BaseModel):
    filename: str
    content_type: str
    wav_file: str

@app.post("/transcribe/", response_model=PredictionResponse)
async def transcribe_audio(file: UploadFile = File(...), save_directory: str = "uploads"):
    try:
        print("Получен запрос на загрузку файла для транскрибации")
        contents = await file.read()
        
        print(f"Файл получен: {file.filename}, размер: {len(contents)} байт")
        
        # Использование имени загруженного файла
        save_filename = file.filename

        # Сохранение загруженного файла
        save_path = os.path.join(save_directory, save_filename)
        save_audio_file(save_path, contents)
        
        # Конвертация файла в WAV
        wav_file = convert_mp3_to_wav(save_path)
        
        # Удаление исходного MP3 файла
        os.remove(save_path)
        print(f"Исходный файл {save_path} удален после конвертации")
        
        print("Файл успешно конвертирован и сохранен.")
        
        # Определение типа содержимого файла по его расширению
        content_type, _ = mimetypes.guess_type(save_path)

        # Если тип содержимого не определен, установите значение по умолчанию
        content_type = content_type or "application/octet-stream"

        return PredictionResponse(
            filename=file.filename,
            content_type=content_type,
            wav_file=wav_file
        )
    except Exception as e:
        print("Ошибка:", e)
        raise HTTPException(status_code=500, detail="Ошибка при обработке файла")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
