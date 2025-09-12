import random
from requests import Response

def get_random_items_by_completed_flag(response: Response,count: int = 10, completed_flag = True ):
    try:
        response_json = response.json()
    except ValueError:
        raise ValueError("Ответ не является валидным JSON")

    completed_items = [item for item in response_json if item.get("completed") is completed_flag]
    if len(completed_items) < count:
        raise ValueError("Недостаточно объектов")
    return random.sample(completed_items, count)