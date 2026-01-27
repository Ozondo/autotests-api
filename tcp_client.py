import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 12345)
client.connect(server_address)


message = "Hello Server!"
client.send(message.encode())

response = client.recv(1024).decode()

print(f"{response}")
