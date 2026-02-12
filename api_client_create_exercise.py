from clients.private_http_builder import AuthentificationUsersSchema

from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema

from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema

from clients.courses.courses_client import get_course_client
from clients.courses.courses_schema import CreateCourseRequestSchema

from clients.exercises.exercises_client import get_exercises_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema()

create_user_response = public_users_client.create_user(request=create_user_request)

authentification_user = AuthentificationUsersSchema(
    email=create_user_request.email,
    password=create_user_request.password,
)

private_file_client = get_files_client(user=authentification_user)

create_file_request = CreateFileRequestSchema(upload_file='./testdata/files/file.png')

create_file_response = private_file_client.create_file(create_file_request)
print(f'Create file data: {create_file_response}')

private_courses_client = get_course_client(user=authentification_user)

create_courses_request = CreateCourseRequestSchema(
    previewFileId=create_file_response.file.id,
    createdByUserId=create_user_response.user.id,
)

create_courses_response = private_courses_client.create_course(create_courses_request)
print(f'Create course data: {create_courses_response}')

private_exercise_client = get_exercises_client(user=authentification_user)

create_exercises_request = CreateExerciseRequestSchema(courseId=create_courses_response.course.id,)

create_exercises_response = private_exercise_client.create_exercise(request=create_exercises_request)

print(f'Create exercises data: {create_exercises_response}')

