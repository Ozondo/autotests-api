import grpc

import user_sevice_pb2
import user_sevice_pb2_grpc


channel = grpc.insecure_channel('localhost:50051')
stub = user_sevice_pb2_grpc.UserServiceStub(channel)

response = stub.GetUser(user_sevice_pb2.GetUserRequest(username="Alice"))
print(response)