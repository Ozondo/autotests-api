from http import HTTPStatus

from clients.users.public_users_client import get_public_users_client
from clients.authentification.authentification_client import get_authentification_client

from clients.users.users_schema import CreateUserRequestSchema
from clients.authentification.authentification_schema import LoginRequestSchema, LoginResponseSchema

from tools.assertions.authentification import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema


def test_login():
    public_users_client = get_public_users_client()
    request = CreateUserRequestSchema()
    public_users_client.create_user(request=request)

    authentification_client = get_authentification_client()
    request = LoginRequestSchema(email=request.email, password=request.password)
    response = authentification_client.login_api(request=request)
    response_data = LoginResponseSchema.model_validate_json(response.text)

    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_login_response(response_data)
    validate_json_schema(response.json(), response_data.model_json_schema())
