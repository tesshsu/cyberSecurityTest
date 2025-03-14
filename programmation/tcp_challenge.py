import socket
import math

# Replace these with the actual server host and port from the challenge
HOST = "127.0.0.1"  # Example: "challenges.hack.me" or an IP address
PORT = 12345        # Example: 5000, 1337, etc.

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the server
    client_socket.connect((HOST, PORT))
    print("Connected to server")

    # Receive data from the server
    data = client_socket.recv(1024).decode().strip()
    print(f"Received: {data}")

    # Split the input into two numbers
    n1, n2 = map(float, data.split())

    # Calculate: sqrt(n1) * n2, rounded to 2 decimal places
    result = round(math.sqrt(n1) * n2, 2)

    # Convert result to string with 2 decimal places
    response = f"{result:.2f}"
    print(f"Sending: {response}")

    # Send the response back to the server
    client_socket.send((response + "\n").encode())  # Add \n if server expects it

    # Optional: Receive a reply from the server
    reply = client_socket.recv(1024).decode().strip()
    print(f"Server reply: {reply}")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the socket
    client_socket.close()
    print("Connection closed")