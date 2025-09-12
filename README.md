# ИПР
## Установка зависимостей
 `pip install -r requirements.txt`
## Запуск тестов
 pytest -s -m todos
 pytest -m todos --html=report.html --cov=api_frame --cov-report=html
 