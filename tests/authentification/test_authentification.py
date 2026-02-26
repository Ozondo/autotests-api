import pytest

from http import HTTPStatus

from clients.authentification.authentification_client import AuthentificationClient
from clients.authentification.authentification_schema import LoginRequestSchema, LoginResponseSchema
from fixtures.users import UserFixture

from tools.assertions.authentification import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema


@pytest.mark.authentification
@pytest.mark.regression
class TestAuthentification:
    def test_login(self, function_user: UserFixture, authentification_client: AuthentificationClient):
        request = LoginRequestSchema(email=function_user.email, password=function_user.password)
        response = authentification_client.login_api(request=request)
        response_data = LoginResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_login_response(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())