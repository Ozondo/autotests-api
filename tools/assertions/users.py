from clients.users.public_users_client import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.base import assert_equal

from clients.users.users_schema import UserSchema, GetUserResponseSchema


def assert_create_users_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    """
    Проверяет, что ответ на создание пользователя соответствует запросу.

    :param request: Исходный запрос на создание пользователя.
    :param response: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(response.user.email, request.email,"email")
    assert_equal(response.user.last_name, request.last_name, "last_name")
    assert_equal(response.user.first_name, request.first_name, "first_name")
    assert_equal(response.user.middle_name, request.middle_name, "middle_name")

def assert_user(actual: UserSchema, expected: UserSchema):
    """
    Проверяет, что ответ на запрос соответствует данным пользователя.

    :param actual: Исходные данные пользователя.
    :param expected: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual.id, expected.id,"id")
    assert_equal(actual.email, expected.email,"email")
    assert_equal(actual.last_name, expected.last_name, "last_name")
    assert_equal(actual.first_name, expected.first_name, "first_name")
    assert_equal(actual.middle_name, expected.middle_name, "middle_name")

def assert_get_user_response(get_user_response: GetUserResponseSchema, create_user_response: CreateUserResponseSchema):
    """
    Проверяет, что модель ответа на запрос о данных пользователя совпадает с моделью запроса на  создания пользователя

    :param get_user_response: Модель ответа с данными пользователя.
    :param create_user_response: Модель с данными создания пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_user(
        actual=get_user_response.user,
        expected=create_user_response.user
    )