import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('127.0.0.1', 12345)
client.connect(server_address)


message = "Привет, Сервер"
client.send(message.encode())

response = client.recv(1024).decode()

print(f"{response}")
