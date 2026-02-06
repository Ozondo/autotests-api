from httpx import Response

from clients.api_client import APIClient
from typing import TypedDict
from clients.private_http_builder import get_private_http_client, AuthentificationTypedDict


class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка упражнений.
    """
    courseId: str

class Exercise(TypedDict):
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class ExercisesResponseDict(TypedDict):
    exercises: Exercise

class GetExercisesTypedDict(TypedDict):
    courses: list[Exercise]

class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на создания упражнения.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class UpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса для обновления упражнения.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None

class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """
    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Метод для получения списка упражнений.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url='/api/v1/exercises', params=query)

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Метод создания упражнения.

        :param request: Данные для создания упражнения
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url='/api/v1/exercises', json=request)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения упражнения.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=f'/api/v1/exercises/{exercise_id}')

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Метод обновления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :param request: Словарь с обновленными данными для упражнения
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(url=f'/api/v1/exercises/{exercise_id}', json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(url=f'/api/v1/exercises/{exercise_id}')

    def get_exercises(self, query: GetExercisesQueryDict) -> ExercisesResponseDict:
        """
        Метод для получения списка упражнений в формате json

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта json
        """
        return self.get_exercises_api(query=query).json()

    def get_exercise(self, exercise_id: str) -> ExercisesResponseDict:
        """
        Метод получения упражнения в формате json

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта json
        """
        return self.get_exercise_api(exercise_id=exercise_id).json()

    def create_exercise(self, request: CreateExerciseRequestDict) -> ExercisesResponseDict:
        """
        Метод создания упражнения в формате json

        :param request: Данные для создания упражнения
        :return: Ответ от сервера в виде объекта json
        """
        return self.create_exercise_api(request=request).json()

    def update_exercise(self, request: UpdateExerciseRequestDict, exercise_id: str) -> ExercisesResponseDict:
        """
        Метод обновления упражнения в формате json

        :param exercise_id: Идентификатор упражнения.
        :param request: Словарь с обновленными данными для упражнения
        :return: Ответ от сервера в виде объекта в json
        """
        return self.update_exercise_api(exercise_id=exercise_id, request=request).json()

def get_exercises_client(user: AuthentificationTypedDict) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user=user))