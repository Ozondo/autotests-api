import httpx


login_payload = {
  "email": "user@example.com",
  "password": "string"
}

login_response = httpx.post('http://127.0.0.1:8000/api/v1/authentication/login', json=login_payload)
login_response_data = login_response.json()

print(f"Status code: {login_response.status_code}")
print(f"Login response: {login_response_data}")

token_payload = login_response_data['token']['accessToken']
headers = {"Authorization": f"Bearer {token_payload}"}

get_user_response = httpx.get('http://127.0.0.1:8000/api/v1/users/me', headers=headers)
get_user_response_data = get_user_response.json()

print(f"Status code: {get_user_response.status_code}")
print(f"Login response: {get_user_response_data}")