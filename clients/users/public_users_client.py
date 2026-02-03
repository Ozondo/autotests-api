from httpx import Response

from clients.api_client import APIClient
from typing import TypedDict

class CreateUserDict(TypedDict):
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class PublicUsersClient(APIClient):
    """
    Клиент для работы с endpoint-ами не требующими авторизации /api/v1/users
    """
    def create_user_api(self, request: CreateUserDict) -> Response:
        """
        Метод выполняет создание пользователя.

        :param request: Словарь с данными для создания пользователя
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url="/api/v1/users", json=request)