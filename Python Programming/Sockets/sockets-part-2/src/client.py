import socket

HEADER_SIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

while True:
    # this is a stream of data (so how big of chunks of data to receive at a time)
    full_message = ''
    new_message = True
    while True:
        # message = s.recv(1024)
        message = s.recv(16)
        if new_message:
            print(f'new message length: {message[:HEADER_SIZE]}')
            message_length = int(message[:HEADER_SIZE])
            new_message = False
        full_message += message.decode('utf-8')
        if len(full_message) - HEADER_SIZE == message_length:
            print('full message received.')
            print(full_message[HEADER_SIZE:])
            new_message = True
            full_message = ''
    print(full_message)