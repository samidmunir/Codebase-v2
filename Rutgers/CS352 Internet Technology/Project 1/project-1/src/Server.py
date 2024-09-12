import socket
import sys

# Create the server socket.
def start_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', port))
    server_socket.listen(1)
    
    print(f'Server is listening on port: {port}.')
    
    # Accept new connections.
    connection, address = server_socket.accept()
    print(f'\tConnection from {address}...')
    
    while True:
        # Receive data from the client
        data = connection.recv(1024).decode()
        if not data:
            break
        
        print(f'\tReceived: {data}')
        
        # Process the data (convert to uppercase)
        data_to_uppercase = data.swapcase()
        
        # Send the updated data back to the client
        connection.sendall(data_to_uppercase.encode())
    
    # Close the connection.
    connection.close()
    print('\n*** Connection closed ***')
    
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 Server.py PORT')
        sys.exit(1)
    
    port = int(sys.argv[1])
    start_server(port)