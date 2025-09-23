import pytest

from Tests.API.Helpers.Assertions import Asserts
from Tests.API.Helpers.helpers import Helpers
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

@pytest.mark.todos
def test_my_todos(get_todo_data, get_default_count_todo_items):
    reg_response = get_todo_data.todo_list()
    reg_response = Helpers.get_random_items_by_completed_flag(
        response=reg_response,
        count=get_default_count_todo_items,
        completed_flag=True
    )
    Asserts.assert_all_completed(reg_response, completed= True)

@pytest.mark.todos
def test_my_todos2(get_todo_data, get_default_count_todo_items):
    reg_response = get_todo_data.todo_list()
    reg_response = Helpers.get_random_items_by_completed_flag(
        response=reg_response,
        count=get_default_count_todo_items,
        completed_flag=False
    )
    Asserts.assert_all_completed(reg_response, completed= False)

@pytest.mark.todos
@pytest.mark.parametrize("todo_id, status",[
    ('abc',404),
    (-10,404),
])
def test_todo_invalid_id(get_todo_data, todo_id, status):
    reg_response = get_todo_data.todo_list(todo_id = todo_id)
    logging.info(reg_response.json())
    Asserts.assert_status_code(reg_response, status)
    Asserts.assert_json_empty(reg_response)