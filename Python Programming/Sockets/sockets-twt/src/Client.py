import socket
import time

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connecting client socket with the server socket
client_socket.connect(ADDRESS)

# function to send messages to the server.
def send(message):
    message = message.encode(FORMAT)
    # first message is the length to come
    message_length = len(message)
    send_length = str(message_length).encode(FORMAT)
    # adding byte spaces of HEADER - len(send_length)
    send_length += b' ' * (HEADER - len(send_length))
    client_socket.send(send_length)
    client_socket.send(message)

send('Hello world!')
time.sleep(1)
send('Message #2')
time.sleep(1)
send('Message #3')
time.sleep(1)
send(DISCONNECT_MESSAGE)