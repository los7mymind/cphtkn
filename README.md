# Анализатор служебных переговоров

Для старта программы пропишите в терминале:
cd ./src && uvicorn main:app --reload
cd ./src/uiuxpython && streamlit run uiux.py


Структура папок:

backend/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── upload_routes.py
│   │   ├── processing_routes.py
│   └── services/
│       ├── __init__.py
│       ├── file_upload_service.py
│       ├── neural_network_service.py
│       ├── text_processing_service.py
│       └── response_service.py
├── models/
│   ├── __init__.py
│   └── neural_networks.py
├── utils/
│   ├── __init__.py
│   ├── file_utils.py
│   ├── network_utils.py
│   └── response_utils.py
├── tests/
│   ├── __init__.py
│   ├── test_upload.py
│   ├── test_processing.py
│   └── test_response.py
├── .env
├── requirements.txt
├── README.md
└── run.py

Описание папок и файлов:
app/: Главный каталог приложения.

init.py: Инициализирует приложение.
main.py: Основной файл для запуска приложения.
config.py: Конфигурации приложения, такие как параметры нейронных сетей, настройки базы данных и т.д.
routes/: Папка с маршрутами (endpoints) для API.
upload_routes.py: Маршруты для загрузки аудиофайлов.
processing_routes.py: Маршруты для обработки данных.
services/: Папка с бизнес-логикой приложения.
file_upload_service.py: Сервисы для работы с загрузкой файлов.
neural_network_service.py: Сервисы для взаимодействия с нейронными сетями.
text_processing_service.py: Сервисы для обработки текста, полученного от нейронных сетей.
response_service.py: Сервисы для формирования и отправки ответов на фронтэнд.
models/: Папка для моделей данных и нейронных сетей.

neural_networks.py: Определение и загрузка моделей нейронных сетей.
utils/: Вспомогательные функции.

file_utils.py: Утилиты для работы с файлами.
network_utils.py: Утилиты для взаимодействия с нейронными сетями.
response_utils.py: Утилиты для формирования ответов.
tests/: Папка для тестов.

test_upload.py: Тесты для загрузки файлов.
test_processing.py: Тесты для обработки данных.
test_response.py: Тесты для отправки ответов.
.env: Файл с переменными окружения (например, конфиденциальные данные и настройки).

requirements.txt: Список зависимостей для проекта.

README.md: Описание проекта и инструкции по запуску.