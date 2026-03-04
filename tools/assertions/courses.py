from clients.courses.courses_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema, \
    GetCoursesResponseSchema, CreateCourseResponseSchema, CreateCourseRequestSchema
from clients.courses.courses_schema import CourseSchema
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.files import assert_file
from tools.assertions.users import assert_user


def assert_update_course_response(request: UpdateCourseRequestSchema, response: UpdateCourseResponseSchema):
    """
    Проверяет, что ответ на обновление курса соответствует данным из запроса.

    :param request: Исходный запрос на обновление курса.
    :param response: Ответ API с обновленными данными курса.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual=response.course.title, expected=request.title, name="title")
    assert_equal(actual=response.course.max_score, expected=request.max_score, name="max_score")
    assert_equal(actual=response.course.min_score, expected=request.min_score, name="min_score")
    assert_equal(actual=response.course.description, expected=request.description, name="description")
    assert_equal(actual=response.course.estimated_time, expected=request.estimated_time, name="estimated_time")


def assert_course(actual: CourseSchema, expected: CourseSchema):
    """
    Проверяет, что фактические данные курса соответствуют ожидаемым.

    :param actual: Фактические данные курса.
    :param expected: Ожидаемые данные курса.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual=actual.id, expected=expected.id, name="id")
    assert_equal(actual=actual.title, expected=expected.title, name="title")
    assert_equal(actual=actual.max_score, expected=expected.max_score, name="max_score")
    assert_equal(actual=actual.min_score, expected=expected.min_score, name="min_score")
    assert_equal(actual=actual.description, expected=expected.description, name="description")
    assert_equal(actual=actual.estimated_time, expected=expected.estimated_time, name="estimated_time")

    assert_file(actual=actual.preview_file, expected=expected.preview_file)
    assert_user(actual=actual.created_by_user, expected=expected.created_by_user)

def assert_courses_response(
        get_courses_response: GetCoursesResponseSchema,
        create_courses_responses: list[CreateCourseResponseSchema]
):
    """
    Проверяет, что ответ на получение списка курсов соответствует ответам на их создание.

    :param get_courses_response: Ответ API при запросе списка курсов.
    :param create_courses_responses: Список API ответов при создании курсов.
    :raises AssertionError: Если данные курсов не совпадают.
    """
    assert_length(get_courses_response.courses, create_courses_responses, "courses")

    for index, create_course_response in enumerate(create_courses_responses):
        assert_course(actual=get_courses_response.courses[index], expected=create_course_response.course)

def assert_create_course_response(
    actual: CreateCourseResponseSchema,
    expected: CreateCourseRequestSchema
):
    """
    Проверяет, что фактические данные создания курса соответствуют ожидаемым.

    :param actual: Фактические данные курса.
    :param expected: Ожидаемые данные курса.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual=actual.course.title, expected=expected.title, name="title")
    assert_equal(actual=actual.course.max_score, expected=expected.max_score, name="max_score")
    assert_equal(actual=actual.course.min_score, expected=expected.min_score, name="min_score")
    assert_equal(actual=actual.course.description, expected=expected.description, name="description")
    assert_equal(actual=actual.course.estimated_time, expected=expected.estimated_time, name="estimated_time")

    assert_equal(actual=actual.course.preview_file.id, expected=expected.preview_file_id, name="preview_file_id")
    assert_equal(actual=actual.course.created_by_user.id, expected=expected.created_by_user_id, name="created_by_user")
