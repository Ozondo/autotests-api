from api_client_get_user import get_public_users_client
from clients.files.files_client import get_files_client, CreateFileRequestDict
from clients.courses.courses_client import get_course_client, CreateCourseRequestDict
from clients.private_http_builder import AuthentificationTypedDict
from clients.users.public_users_client import CreateUserRequestDict
from tools.fakers import get_random_email

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestDict(
    email=get_random_email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string"
)

create_user_response = public_users_client.create_user(request=create_user_request)

authentification_user = AuthentificationTypedDict(
    email=create_user_request["email"],
    password=create_user_request["password"],
)

files_client = get_files_client(authentification_user)
courses_client = get_course_client(authentification_user)

create_file_request = CreateFileRequestDict(
    filename='file.png',
    directory='courses',
    upload_file='./testdata/files/file.png'
)

create_file_response = files_client.create_file(request=create_file_request)
print('Create file data', create_file_response)

create_course_request = CreateCourseRequestDict(
    title='Python',
    maxScore=100,
    minScore=10,
    description='Python API course',
    estimatedTime='2 weeks',
    previewFileId=create_file_response['file']['id'],
    createdByUserId=create_user_response['user']['id'],
)

create_course_response = courses_client.create_course(request=create_course_request)
print(f'Create course: {create_course_response}')