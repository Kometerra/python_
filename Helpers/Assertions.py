from requests import Response

class Asserts:

    def assert_status_code(response: Response, expected_code: int):
        actual_code = response.status_code
        assert actual_code == expected_code, \
        f'Ожидался статус код "{expected_code}", но получен {actual_code}. Тело ответа {response.text}'

    def assert_json_has_key(response: Response, key: str):
        response_json = response.json()
        assert key in response_json, \
        f'Ключ "{key}" отсутствует в JSON - ответе'

    def assert_json_is_list(response: Response):
        response_json = response.json()
        assert isinstance(response_json,list), \
        f'Ожидался тип данных list'

    def assert_json_has_key_value(response: Response, key: str, value):
        response_json = response.json()
        assert key in response_json, f'Ключ "{key}" отсутствует в JSON - ответе'
        actual_value = response_json[key]
        assert actual_value == value, f'Ожидалось "{value}" \n получено "{actual_value}"'

    def assert_all_completed(items: list):
        assert all(item.get("completed") is True for item in items), (
            "Не все элементы имеют completed=True"
        )