import socket
import threading
import time
from datetime import datetime

# Since we don't know the size of each message from the client,
#   it always be 64.
# - will have a number that indicates the number of bytes that we are to receive.
HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
# print(f'SERVER: {SERVER}')
ADDRESS = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

# Setting up server socket.
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Anything that connects to this address, will hit the socket endpoint.
# - binding this socket to this address.
server_socket.bind(ADDRESS)

def handle_client(connection, address):
    print(f'[NEW CONNECTION] - {address} @ {datetime.now().strftime('%H:%M:%S')}')
    connected = True
    while connected:
        # how many bytes to recieve from the client.
        # - blocking line of code
        # - will not proceed unless we recieve a message from the client.
        message_length = connection.recv(HEADER).decode(FORMAT)
        if message_length:
            message_length = int(message_length)
            message = connection.recv(message_length).decode(FORMAT)
    
            if message == DISCONNECT_MESSAGE:
                connected = False

            text = f'\t[{address}] @ {datetime.now().strftime('%H:%M:%S')}'
            text += f'\n\t\tmessage: "{message}"'
            print(text)
            # print(f'\t[{address}] - {message}')
        
    connection.close()

def start():
    # listening for new connections
    server_socket.listen()
    time.sleep(1)
    print(f'\t[LISTENING] - {SERVER} @ {datetime.now().strftime('%H:%M:%S')}')
    # continue to listen until <condition>
    while True:
        # blocking line - wait on this line until a new connection on the server.
        # - store the object for connection (socket object).
        # - address is the information about the connection (PORT/IPA)
        connection, address = server_socket.accept()
        thread = threading.Thread(target = handle_client, args = (connection, address))
        thread.start()
        print(f'\t[ACTIVE CONNECTIONS] - {threading.active_count() - 1}')

print(f'[STARTING] - server is spooling up @ {datetime.now().strftime('%H:%M:%S')}')
time.sleep(1)
print('\t..')
time.sleep(1)
print('\t...')
time.sleep(2)
print('\t....')
time.sleep(1)
print(f'[READY] - server is ready and listening @ {datetime.now().strftime('%H:%M:%S')}')
start()