# Система автоматического перевода Синергия

Проект представляет собой нейросетевую систему перевода текста (с русского на английский) на базе архитектуры Transformer (Hugging Face).

## Технологии
* **Бэкенд:** Python, FastAPI, PyTorch, Transformers (модель Helsinki-NLP/opus-mt-ru-en).
* **Фронтенд:** HTML, CSS, JavaScript (Fetch API).

## Как запустить проект локально
1. Создайте виртуальное окружение: `python -m venv .venv`
2. Активируйте его (Windows): `.\.venv\Scripts\Activate.ps1`
3. Установите библиотеки: `python -m pip install fastapi uvicorn transformers torch sentencepiece`
4. Запустите сервер: `uvicorn backend.main:app --reload`
5. Откройте файл `frontend/index.html` в любом браузере.

## Автор
Студент Университета «Синергия» (практика).
