import socket
import time
import pickle

HEADER_SIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    client_socket, address = s.accept()
    print(f'Connection from {address} has been established!')
    
    d = {1: 'Hey', 2: 'There'}
    message = pickle.dumps(d)
    
    message = bytes(f'{len(message): < {HEADER_SIZE}}', 'utf-8') + message
    
    client_socket.send(message)
    
    while True:
        time.sleep(3)
        message = f'The time is: {time.time()}'
        message = f'{len(message): < {HEADER_SIZE}}' + message
        client_socket.send(bytes(message, 'utf-8'))