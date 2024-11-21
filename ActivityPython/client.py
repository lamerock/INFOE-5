import socket

# Step 1: Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: Connect to the server
client_socket.connect(('localhost', 12345))  # Connect to the same IP and port as the server

# Step 3: Send a message to the server
message = "Hello Server! This is the client."
client_socket.send(message.encode())

# Step 4: Receive a response from the server
response = client_socket.recv(1024).decode()
print(f"Received from server: {response}")

# Step 5: Close the connection
client_socket.close()
