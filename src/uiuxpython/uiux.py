import streamlit as st
import requests

# Установка заголовка
st.title('UnlockHT. Анализатор служебных переговоров.')

# Загрузка файла
st.subheader('Загрузите запись голосового разговора')
uploaded_file = st.file_uploader("", type=["mp3"])

# Кнопка для отправки файла
if st.button('Отправить'):
    
    # Поле для расшифровки текста (только для чтения)
    st.subheader('Расшифровка текста')
    transcription = st.text_area("", height=200, disabled=True)

    if uploaded_file:
        files = {'file': (uploaded_file.name, uploaded_file.getvalue())}
        response = requests.post("http://127.0.0.1:8000/transcribe/", files=files)
        if response.status_code == 200:
            transcription_data = response.json()
            transcription.text_area("", transcription_data["transcription"], height=200, disabled=True)
        else:
            st.write("Ошибка при расшифровке файла")
    else:
        st.write("Файл не загружен")
