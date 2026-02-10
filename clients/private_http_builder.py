from httpx import Client
from pydantic import BaseModel

from clients.authentification.authentification_client import get_authentification_client
from clients.authentification.authentification_schema import LoginRequestSchema

class AuthentificationUsersSchema(BaseModel):
    """Модель пользователя для авторизации"""
    email: str
    password: str

def get_private_http_client(user: AuthentificationUsersSchema) -> Client:
    """
    Функция создаёт экземпляр httpx.Client с аутентификацией пользователя.

    :param user: Объект AuthenticationUserSchema с email и паролем пользователя.
    :return: Готовый к использованию объект httpx.Client с установленным заголовком Authorization.
    """
    authentification_client = get_authentification_client()

    login_request = LoginRequestSchema(email=user.email, password=user.password)
    login_response = authentification_client.login(login_request)

    return Client(
        timeout=100,
        base_url="http://localhost:8000",
        headers={
            "Authorization": f"Bearer {login_response.token.access_token}",
        }
    )