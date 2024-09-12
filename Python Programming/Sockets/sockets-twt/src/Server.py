import socket
import threading
import sys
import time

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
# print(f'SERVER: {SERVER}')
ADDRESS = (SERVER, PORT)

# Setting up server socket.
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Anything that connects to this address, will hit the socket endpoint.
# - binding this socket to this address.
server_socket.bind(ADDRESS)

def handle_client(connection, address):
    pass

def start():
    # listening for new connections
    server_socket.listen()
    # continue to listen until <condition>
    while True:
        # blocking line - wait on this line until a new connection on the server.
        # - store the object for connection (socket object).
        # - address is the information about the connection (PORT/IPA)
        connection, address = server_socket.accept()
        thread = threading.Thread(target = handle_client, args = (connection, address))
        thread.start()
        print(f'[ACTIVE CONNECTIONS] - {threading.activeAcount() - 1}')

print('[STARTING] - server is spooling up')
time.sleep(2)
print('[READY] - server is ready and listening')
start()