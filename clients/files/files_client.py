from clients.api_client import APIClient
from httpx import Response

from clients.private_http_builder import AuthentificationUsersSchema, get_private_http_client
from clients.files.files_schema import CreateFileRequestSchema, FileResponseSchema


class FilesClient(APIClient):
    """
    Клиент для работы с /api/v1/files
    """
    def get_file_api(self, file_id: str) -> Response:
        """
        Метод получения файла.

        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=f'/api/v1/files/{file_id}')

    def create_file_api(self, request: CreateFileRequestSchema) -> Response:
        """
        Метод создания файла.

        :param request: Словарь с filename, directory, upload_file.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            url=f'/api/v1/files',
            data=request.model_dump(by_alias=True, exclude={'upload_file'}),
            files={"upload_file": open(request.upload_file, "rb")}
        )

    def delete_file_api(self, file_id: str) -> Response:
        """
        Метод удаления файла.

        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(url=f'/api/v1/files/{file_id}')

    def create_file(self, request: CreateFileRequestSchema) -> FileResponseSchema:
        """
        Метод создания файла в формате json

        :param request: Словарь с filename, directory, upload_file.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        response = self.create_file_api(request)
        return FileResponseSchema.model_validate_json(response.text)


def get_files_client(user: AuthentificationUsersSchema) -> FilesClient:
    """
    Функция создаёт экземпляр FilesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию FilesClient.
    """
    return FilesClient(client=get_private_http_client(user=user))