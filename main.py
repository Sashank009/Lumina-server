import socket
import threading
from protocols.tcp_protocol import TCPProtocol

class DeviceHandler(threading.Thread):
    def __init__(self, connection, address):
        threading.Thread.__init__(self)
        self.connection = connection
        self.address = address
        self.protocol = TCPProtocol()

    def run(self):
        print(f"Connected to {self.address}")
        while True:
            data = self.connection.recv(1024).decode()
            if not data:
                break
            response = self.protocol.handle_message(data)
            self.connection.send(response.encode())
        self.connection.close()
        print(f"Disconnected from {self.address}")

class Server:
    def __init__(self, host='localhost', port=5000):
        self.host = host
        self.port = port

    def start(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen(5)
        print(f"Server listening on {self.host}:{self.port}")

        while True:
            connection, address = server_socket.accept()
            handler = DeviceHandler(connection, address)
            handler.start()

if __name__ == "__main__":
    server = Server()
    server.start()
