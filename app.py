import streamlit as st

# Настройки страницы
st.set_page_config(page_title="UnlockHT", page_icon="🔓", layout="centered")

# Стилизация с помощью CSS
st.markdown("""
    <style>
    @font-face {
        font-family: 'CROWDEN';
        src: url('CROWDEN.ttf') format('truetype');
    }
    body {
        background-color: #333333;
        font-family: 'Helvetica Neue', sans-serif;
        color: #ffffff;
    }
    .main-container {
        background-color: #444444;
        border-radius: 10px;
        padding: 2rem;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
        max-width: 800px;
        margin: 2rem auto;
    }
    .main-container:hover {
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
    }
    .stButton button {
        background-color: #ff5722;
        color: #ffffff;
        border: none;
        padding: 0.75rem 1.5rem;
        border-radius: 5px;
        font-size: 1rem;
        margin-top: 1rem;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.3s ease;
    }
    .stButton button:hover {
        background-color: #e64a19;
        transform: translateY(-2px);
    }
    .stButton button:active {
        transform: translateY(1px);
    }
    .stRadio > div {
        display: flex;
        justify-content: space-around;
        margin-top: 1rem;
        font-size: 1rem;
        color: #ff5722;
    }
    .stTextInput > div > input {
        border: 2px solid #ff5722;
        border-radius: 5px;
        padding: 0.5rem;
        margin-top: 0.5rem;
        font-size: 1rem;
        background-color: #555555;
        color: #ffffff;
        transition: border-color 0.3s ease;
    }
    .stTextInput > div > input:focus {
        border-color: #e64a19;
    }
    .stTextArea > div > textarea {
        border: 2px solid #ff5722;
        border-radius: 5px;
        padding: 0.5rem;
        margin-top: 0.5rem;
        font-size: 1rem;
        background-color: #555555;
        color: #ffffff;
        transition: border-color 0.3s ease;
    }
    .stTextArea > div > textarea:focus {
        border-color: #e64a19;
    }
    h1 {
        font-family: 'CROWDEN', sans-serif;
        color: #2ade93;
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 1rem;
    }
    h2, h3, p {
        color: #ffffff;
    }
    h2 {
        font-size: 2rem;
        font-weight: bold;
        text-align: center;
        margin-top: 2rem;
    }
    h3 {
        font-size: 1.5rem;
        font-weight: bold;
        text-align: center;
        margin-top: 1.5rem;
    }
    p {
        font-size: 1rem;
        text-align: center;
    }
    .footer {
        text-align: center;
        padding: 2rem 0;
        color: #888888;
    }
    .file-upload-container {
        margin: 0 auto;
        text-align: center;
    }
    .file-upload-container > label {
        display: block;
        font-size: 1rem;
        margin-bottom: 0.5rem;
    }
    .file-upload-container input[type='file'] {
        display: none;
    }
    .file-upload-container label[for='file-upload'] {
        display: inline-block;
        padding: 0.5rem 1rem;
        background-color: #ff5722;
        color: white;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .file-upload-container label[for='file-upload']:hover {
        background-color: #e64a19;
    }
    </style>
    """, unsafe_allow_html=True)

# Основной контейнер
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Заголовок и описание
st.title("🔓 UnlockHT")
st.write("<h2>Загрузите запись голосового разговора</h2>", unsafe_allow_html=True)

# Загрузка файла
st.markdown('<div class="file-upload-container">', unsafe_allow_html=True)
uploaded_file = st.file_uploader("Выберите файл", type=["wav", "mp3"], help="Форматы файлов: WAV, MP3")
st.markdown('</div>', unsafe_allow_html=True)

# Тип переговоров
st.write("<h2>Тип переговоров</h2>", unsafe_allow_html=True)
conversation_type = st.radio(
    "",
    ('Диспетчер и машинист', 'Пример 1', 'Пример 2', 'Пример 3')
)

# Кнопка для отправки
if st.button('Submit'):
    if uploaded_file is not None:
        st.success("Файл загружен успешно!")
    else:
        st.error("Пожалуйста, загрузите файл перед отправкой.")

# Расшифровка текста
st.write("<h2>Расшифровка текста</h2>", unsafe_allow_html=True)
transcription = st.text_area("")

# Поле для ввода имени файла и кнопка загрузки
st.write("<h2>Сохранение расшифровки</h2>", unsafe_allow_html=True)
file_name = st.text_input("Введите имя файла", help="Укажите имя файла для сохранения расшифровки")
if st.button('Download'):
    if transcription and file_name:
        st.success(f"Файл {file_name}.txt успешно сохранен!")
    else:
        st.error("Пожалуйста, введите текст расшифровки и имя файла перед загрузкой.")

# Закрытие основного контейнера
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        <p>Created with ❤️ by UnlockHT</p>
    </div>
    """, unsafe_allow_html=True)
