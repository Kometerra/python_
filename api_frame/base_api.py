import requests
import logging

class BaseApi:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.session()

    def _send_request(self, method, endpoint, **kwargs):
        url = f'{self.base_url}{endpoint}'
        try:
            response = self.session.request(method, url, **kwargs)
        except requests.exceptions.RequestException as e:
            logging.error(f"Ошибка запроса: {e}")
            raise

        # Логируем ошибочные ответы, но не выбрасываем исключение
        if response.status_code >= 400:
            logging.warning(f"HTTP {response.status_code}: {response.text}")

        return response

    def get_request(self, endpoint, **kwargs):
        return self._send_request('GET', endpoint, **kwargs)

    def post_request(self, endpoint, **kwargs):
        return self._send_request('POST', endpoint, **kwargs)

    def put_request(self, endpoint, **kwargs):
        return self._send_request('PUT', endpoint, **kwargs)
