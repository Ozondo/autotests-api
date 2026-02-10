from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthentificationUsersSchema
from clients.exercises.exercises_schema import (GetExercisesQuerySchema, CreateExerciseRequestSchema,
                                                UpdateExerciseRequestSchema, ExercisesResponseSchema)


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """
    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        Метод для получения списка упражнений.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url='/api/v1/exercises', params=query.model_dump(by_alias=True))

    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Метод создания упражнения.

        :param request: Данные для создания упражнения
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url='/api/v1/exercises', json=request.model_dump(by_alias=True))

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения упражнения.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=f'/api/v1/exercises/{exercise_id}')

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        """
        Метод обновления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :param request: Словарь с обновленными данными для упражнения
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(url=f'/api/v1/exercises/{exercise_id}', json=request.model_dump(by_alias=True))

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(url=f'/api/v1/exercises/{exercise_id}')

    def get_exercises(self, query: GetExercisesQuerySchema) -> ExercisesResponseSchema:
        """
        Метод для получения списка упражнений в формате json

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта json
        """
        response = self.get_exercises_api(query=query)
        return ExercisesResponseSchema.model_validate_json(response.text)

    def get_exercise(self, exercise_id: str) -> ExercisesResponseSchema:
        """
        Метод получения упражнения в формате json

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта json
        """
        response = self.get_exercise_api(exercise_id=exercise_id)
        return ExercisesResponseSchema.model_validate_json(response.text)

    def create_exercise(self, request: CreateExerciseRequestSchema) -> ExercisesResponseSchema:
        """
        Метод создания упражнения в формате json

        :param request: Данные для создания упражнения
        :return: Ответ от сервера в виде объекта json
        """
        response = self.create_exercise_api(request=request)
        return ExercisesResponseSchema.model_validate_json(response.text)

    def update_exercise(self, request: UpdateExerciseRequestSchema, exercise_id: str) -> ExercisesResponseSchema:
        """
        Метод обновления упражнения в формате json

        :param exercise_id: Идентификатор упражнения.
        :param request: Словарь с обновленными данными для упражнения
        :return: Ответ от сервера в виде объекта в json
        """
        response = self.update_exercise_api(exercise_id=exercise_id, request=request)
        return ExercisesResponseSchema.model_validate_json(response.text)

def get_exercises_client(user: AuthentificationUsersSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user=user))