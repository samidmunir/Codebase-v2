import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

# this is a stream of data (so how big of chunks of data to receive at a time)
full_message = ''
while True:
    # message = s.recv(1024)
    message = s.recv(8)
    if len(message) <= 0:
        break
    full_message += message.decode('utf-8')
print(full_message)