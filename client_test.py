import socket
import sys


def client_program():
    # Default server settings
    host = 'localhost'
    port = 5000

    # Check if arguments are provided
    if len(sys.argv) == 3:
        host = sys.argv[1]
        port = int(sys.argv[2])

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((host, port))
        print(f"Connected to server at {host}:{port}")

        while True:
            # Get user input
            message = input("Enter message to send (type 'bye' to exit): ")

            # Exit condition
            if message.lower().strip() == 'bye':
                print("Disconnecting from server.")
                break

            # Send the message to the server
            client_socket.send(message.encode())

            # Receive the response from the server
            try:
                response = client_socket.recv(1024).decode()
                print(f"Received from server: {response}")
            except socket.error as e:
                print(f"Error receiving data: {e}")
                break

    except socket.error as e:
        print(f"Error connecting to server: {e}")
    finally:
        # Close the connection
        client_socket.close()


if __name__ == '__main__':
    client_program()
