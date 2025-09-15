import pytest
import os
import logging
from dotenv import load_dotenv
from api_frame.todo_api import TodoApi

load_dotenv()

# 🔧 Настройка логирования один раз при запуске Pytest
def pytest_configure(config):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(),  # вывод в консоль
            logging.FileHandler("test.log")  # запись в файл
        ]
    )
    logging.info("Логирование инициализировано через conftest.py")

# 🌐 Фикстура для base_url
@pytest.fixture(scope="session")
def get_base_url():
    return os.getenv('BASE_URL')

# 📦 Фикстура для API-клиента
@pytest.fixture()
def get_todo_data(get_base_url):
    return TodoApi(get_base_url)

# 🔢 COUNT из .env
@pytest.fixture(scope="session")
def get_default_count_todo_items() -> int:
    count = os.getenv("DEFAULT_COUNT_TODO_ITEMS", "5")
    try:
        return int(count)
    except ValueError:
        pytest.fail("DEFAULT_COUNT_TODO_ITEMS должен быть числом")