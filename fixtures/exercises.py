import pytest
from pydantic import BaseModel

from clients.exercises.exercises_client import ExercisesClient, get_exercises_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, ExercisesResponseSchema

from fixtures.users import UserFixture
from fixtures.courses import CoursesFixture

class ExercisesFixture(BaseModel):
    request: CreateExerciseRequestSchema
    response: ExercisesResponseSchema

@pytest.fixture
def exercises_client(function_user: UserFixture) -> ExercisesClient:
    return get_exercises_client(function_user.authentification_user)

@pytest.fixture
def function_exercises(function_courses: CoursesFixture , exercises_client: ExercisesClient) -> ExercisesFixture:
    request = CreateExerciseRequestSchema(course_id=function_courses.response.course.id)
    response = exercises_client.create_exercise(request)

    return ExercisesFixture(request=request, response=response)


