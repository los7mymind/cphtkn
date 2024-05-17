from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
from pydantic import BaseModel
import io
from pydub import AudioSegment
import os
import requests

app = FastAPI()

app.mount("/static", StaticFiles(directory="../static"), name="static")

class PredictionResponse(BaseModel):
    filename: str
    content_type: str
    prediction: str

@app.post("/upload", response_model=PredictionResponse)
async def upload_file(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        
        # Здесь вы можете передать содержимое файла вашей нейронной сети
        wav_format = await send_to_mp3toWav(contents)

        print("Отправлено")
        
        return JSONResponse(content={
            "filename": file.filename,
            "content_type": file.content_type,
            "wav_format": wav_format
        })
    except Exception as e:
        print("Ошибка:", e)
        raise HTTPException(status_code=500, detail="Ошибка при обработке файла")

# async def send_to_mp3toWav(audio_data: bytes) -> str:
#     # Преобразование содержимого в аудиоформат (если необходимо)
#     audio = AudioSegment.from_file(io.BytesIO(audio_data))
    
#     # Здесь должна быть логика передачи аудиофайла в нейронную сеть и получения предсказания
#     # Для примера используем заглушку
#     prediction = dummy_neural_network_predict(audio)
    
#     return prediction

async def send_to_mp3toWav(audio_data: bytes) -> str:
    try:
        # Определение URL-адреса, на который будет отправлен файл
        url = "http://127.0.0.1:8000/convert"
        
        # Отправка аудиоданных в формате multipart/form-data
        files = {'audio_file': audio_data}
        response = requests.post(url, files=files)
        
        # Проверка успешности запроса и получение результата
        if response.status_code == 200:
            return response.json().get("wav_format")
        else:
            raise Exception("Ошибка при отправке аудиофайла на конвертацию")
    except Exception as e:
        print("Ошибка при отправке аудиофайла на конвертацию:", e)
        raise

def dummy_neural_network_predict(audio):
    # Заглушка функции предсказания нейронной сети
    # Здесь должна быть реальная логика предсказания
    return "dummy_prediction"

@app.get("/")
async def root():
    return FileResponse("../static/index.html")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
