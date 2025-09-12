import pytest
from requests import Response

from helpers.assertions import Asserts
import logging


@pytest.mark.todos
def test_successful_todo(get_todo_data):
    reg_response = get_todo_data.todo_list()
    logging.info(reg_response.json())
    Asserts.assert_status_code(reg_response, 200)
    Asserts.assert_json_is_list(reg_response)


@pytest.mark.todos
def test_invalid_endpoint(get_todo_data):
    reg_response = get_todo_data.todo_list(valid = False)
    logging.info(reg_response.json())
    Asserts.assert_status_code(reg_response, 404)

@pytest.mark.todos
@pytest.mark.parametrize("todo_id, status",[
    (1,200),
    (2,200),
    (3,200)
])
def test_todo_by_id(get_todo_data, todo_id, status):
    reg_response = get_todo_data.todo_list(todo_id = todo_id)
    logging.info(reg_response.json())
    Asserts.assert_status_code(reg_response, status)
    Asserts.assert_json_has_key_value(reg_response, 'id', todo_id)
    Asserts.assert_json_has_key(reg_response, 'userId')