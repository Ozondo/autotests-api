import pytest
from pydantic import BaseModel, EmailStr

from clients.authentification.authentification_client import get_authentification_client, AuthentificationClient
from clients.users.private_users_client import get_private_users_client, PrivateUsersClient
from clients.users.public_users_client import (
    PublicUsersClient, get_public_users_client, CreateUserRequestSchema, CreateUserResponseSchema)

from clients.private_http_builder import AuthentificationUsersSchema

class UserFixture(BaseModel):
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def email(self) -> EmailStr:  # Быстрый доступ к email пользователя
        return self.request.email

    @property
    def password(self) -> str: # Быстрый доступ к password пользователя
        return self.request.password

    @property
    def authentification_user(self) -> AuthentificationUsersSchema:
        return AuthentificationUsersSchema(email=self.email, password=self.password)


@pytest.fixture
def authentification_client() -> AuthentificationClient:
    return get_authentification_client()

@pytest.fixture
def public_users_client() -> PublicUsersClient:
    return get_public_users_client()

@pytest.fixture
def private_users_client(
        authentification_client: AuthentificationClient,
        function_user: UserFixture
) -> PrivateUsersClient:
    return get_private_users_client(user=function_user.authentification_user)

@pytest.fixture
def function_user(public_users_client: PublicUsersClient) -> UserFixture:
    request = CreateUserRequestSchema()
    response = public_users_client.create_user(request=request)
    return UserFixture(request=request, response=response)