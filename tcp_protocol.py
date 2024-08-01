class TCPProtocol:
    def handle_message(self, message):
        # Placeholder for actual read/write logic
        print(f"Received message: {message}")
        return f"Echo: {message}"
