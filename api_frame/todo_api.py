from api_frame.base_api import BaseApi

class TodoApi(BaseApi):
    REG_ENDPOINT = 'todos'

    def todo_list(self, valid=True, todo_id = None):
        endpoint = self.REG_ENDPOINT if valid else self.REG_ENDPOINT + "s"
        if todo_id is not None:
            endpoint += f'/{todo_id}'
        return self.get_request(endpoint)
