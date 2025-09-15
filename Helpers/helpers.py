import random
from requests import Response
from api_frame.base_api import BaseApi

class Helpers(BaseApi):
    @staticmethod
    def get_random_items_by_completed_flag(
        response: Response,
        count: int,
        completed_flag: bool = True
    ):
        try:
            response_json = response.json()
        except ValueError:
            raise ValueError("Ответ не является валидным JSON")

        completed_items = [
            item for item in response_json
            if item.get("completed") is completed_flag
        ]

        if len(completed_items) < count:
            raise ValueError(f"Недостаточно объектов с completed={completed_flag}: нужно {count}, найдено {len(completed_items)}")

        return random.sample(completed_items, count)