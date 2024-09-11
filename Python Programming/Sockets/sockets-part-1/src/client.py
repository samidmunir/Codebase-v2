import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

# this is a stream of data (so how big of chunks of data to receive at a time)
message = s.recv(1024)
print(message.decode('utf-8'))