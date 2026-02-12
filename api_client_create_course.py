from clients.users.public_users_client import get_public_users_client
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.courses.courses_client import get_course_client
from clients.private_http_builder import AuthentificationUsersSchema
from clients.users.public_users_client import CreateUserRequestSchema
from clients.courses.courses_schema import CreateCourseRequestSchema

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema()

create_user_response = public_users_client.create_user(request=create_user_request)

authentification_user = AuthentificationUsersSchema(
    email=create_user_request.email,
    password=create_user_request.password,
)

files_client = get_files_client(authentification_user)
courses_client = get_course_client(authentification_user)

create_file_request = CreateFileRequestSchema(
    upload_file='./testdata/files/file.png'
)

create_file_response = files_client.create_file(request=create_file_request)
print('Create file data', create_file_response)

create_course_request = CreateCourseRequestSchema(
    previewFileId=create_file_response.file.id,
    createdByUserId=create_user_response.user.id,
)

create_course_response = courses_client.create_course(request=create_course_request)
print(f'Create course: {create_course_response}')