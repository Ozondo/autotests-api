import pytest
from pydantic import BaseModel, EmailStr

from clients.authentification.authentification_client import get_authentification_client, AuthentificationClient
from clients.users.public_users_client import (
    PublicUsersClient, get_public_users_client, CreateUserRequestSchema, CreateUserResponseSchema)

class UserFixture(BaseModel):
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def email(self) -> EmailStr:  # Быстрый доступ к email пользователя
        return self.request.email

    @property
    def password(self) -> str: # Быстрый доступ к password пользователя
        return self.request.password


@pytest.fixture
def authentification_client() -> AuthentificationClient:
    return get_authentification_client()

@pytest.fixture
def public_users_client() -> PublicUsersClient:
    return get_public_users_client()

@pytest.fixture
def function_user(public_users_client: PublicUsersClient) -> UserFixture:
    request = CreateUserRequestSchema()
    response = public_users_client.create_user(request=request)
    return UserFixture(request=request, response=response)