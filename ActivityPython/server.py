import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind(('localhostt', 12345))

# Enable the server to accept connections
server_socket.listen()

print("Server is listening...")

# Accept a connection
client_socket, address = server_socket.accept()
print(f"Connection from {address} has been established!")

# Receive data from the client
data = client_socket.recv(1024).decode('utf-8')
print(f"Received from client: {data}")

# Send a response
client_socket.send("Hello, Client!".encode('utf-8'))

# Close the sockets
client_socket.close()
server_socket.close()
