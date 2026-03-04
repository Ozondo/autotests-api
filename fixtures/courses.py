import pytest
from pydantic import BaseModel

from clients.courses.courses_client import get_course_client, CourseClient
from clients.courses.courses_schema import CreateCourseRequestSchema, CreateCourseResponseSchema
from fixtures.users import UserFixture
from fixtures.files import FilesFixture

class CoursesFixture(BaseModel):
    request: CreateCourseRequestSchema
    response: CreateCourseResponseSchema

@pytest.fixture
def courses_client(function_user: UserFixture) -> CourseClient:
    return get_course_client(function_user.authentification_user)

@pytest.fixture
def function_courses(
        courses_client: CourseClient,
        function_user: UserFixture,
        function_file: FilesFixture,
) -> CoursesFixture:
    request = CreateCourseRequestSchema(
        preview_file_id=function_file.response.file.id,
        created_by_user_id=function_user.response.user.id
    )
    response = courses_client.create_course(request)

    return CoursesFixture(request=request, response=response)