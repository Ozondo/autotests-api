from tools.assertions.schema import validate_json_schema
from tools.fakers import fake

from clients.users.private_users_client import get_private_users_client, AuthentificationUsersSchema
from clients.users.public_users_client import get_public_users_client

from clients.users.users_schema import CreateUserRequestSchema, GetUserResponseSchema

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=fake.email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)

create_user_response = public_users_client.create_user(request=create_user_request)
print("Создание пользователя ", create_user_response)

authentification_user = AuthentificationUsersSchema(
    email=create_user_request.email,
    password=create_user_request.password,
)

private_users_client = get_private_users_client(user=authentification_user)

get_user_response = private_users_client.get_user_api(user_id=create_user_response.user.id)
get_user_response_json = get_user_response.json()
get_user_response_schema = GetUserResponseSchema.model_json_schema()
print("Получение данных пользователя ", get_user_response_json)

validate_json_schema(instance=get_user_response_json, schema=get_user_response_schema)
print("Сравнение json контракта ", get_user_response_schema)
