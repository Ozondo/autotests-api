from clients.private_http_builder import AuthentificationUsersSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client, CreateUserRequestSchema
from tools.fakers import get_random_email

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)

create_user_response = public_users_client.create_user(request=create_user_request)
print(f'Create user: {create_user_response}')

authentification_user = AuthentificationUsersSchema(
    email=create_user_request.email,
    password=create_user_request.password,
)
private_users_client = get_private_users_client(user=authentification_user)

get_user_response = private_users_client.get_user(create_user_response.user.id)
print(f'Get user data: {get_user_response}')