from clients.exercises.exercises_schema import CreateExerciseRequestSchema, ExercisesResponseSchema, ExerciseSchema, \
    GetExerciseResponseSchema
from tools.assertions.base import assert_equal


def assert_create_exercise_response(request: CreateExerciseRequestSchema, response: ExercisesResponseSchema):
    """
    Проверяет, что ответ на создания упражнения соответствует данным из запроса.

    :param request: Исходный запрос на создания упражнения.
    :param response: Ответ API с данными упражнения.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(request.title, response.exercise.title, "title")
    assert_equal(request.max_score, response.exercise.max_score, "max_score")
    assert_equal(request.min_score, response.exercise.min_score, "min_score")
    assert_equal(request.estimated_time, response.exercise.estimated_time, "estimated_time")
    assert_equal(request.course_id, response.exercise.course_id, "course_id")
    assert_equal(request.order_index, response.exercise.order_index, "order_index")
    assert_equal(request.description, response.exercise.description, "description")

def assert_exercise(request: ExerciseSchema, response: ExerciseSchema):
    """
    Проверяет, что фактические данные упражнения соответствуют ожидаемым.

    :param request: Исходный запрос на создания упражнения.
    :param response: Ответ API с данными упражнения.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(request.id, response.id, "id")
    assert_equal(request.title, response.title, "title")
    assert_equal(request.max_score, response.max_score, "max_score")
    assert_equal(request.min_score, response.min_score, "min_score")
    assert_equal(request.estimated_time, response.estimated_time, "estimated_time")
    assert_equal(request.course_id, response.course_id, "course_id")
    assert_equal(request.order_index, response.order_index, "order_index")
    assert_equal(request.description, response.description, "description")

def assert_get_exercise_response(
        get_exercise_response: GetExerciseResponseSchema,
        create_exercise_response: ExercisesResponseSchema
):
    """
    Проверяет, что ответ на получение упражнения соответствует ответу на его создание.

    :param get_exercise_response: Ответ API при запросе данных файла.
    :param create_exercise_response: Ответ API при создании файла.
    :raises AssertionError: Если данные файла не совпадают.
    """
    assert_exercise(get_exercise_response.exercise, create_exercise_response.exercise)