LUMINA SERVER


GITHUB LINK :- 
https://github.com/Sashank009/Lumina-server.git
Lumina Server is a versatile and robust solution designed for real-time data communication in manufacturing plants. It excels in managing TCP/IP communication, allowing seamless data reading and writing across multiple devices simultaneously. Built with extensibility in mind, LuminaServer supports easy integration of additional communication protocols, ensuring future-proof adaptability.
At its core, Lumina Server utilizes multithreading to handle multiple device connections concurrently, ensuring efficient and uninterrupted data flow. This makes it an ideal choice for environments with numerous interconnected devices requiring reliable and continuous data exchange.
The project includes a refined client stub for testing TCP/IP communication, facilitating straightforward verification of server-client interactions. Additionally, comprehensive unit tests ensure that the system performs as expected under various conditions, enhancing reliability and robustness.
LuminaServer’s design prioritizes scalability and flexibility, making it suitable for a wide range of industrial applications. Whether it’s monitoring sensor data, controlling machinery, or managing automated processes, LuminaServer provides a stable and scalable platform for all your communication needs.
With its elegant architecture and future-ready capabilities, LuminaServer stands out as a powerful tool for modern manufacturing environments, ensuring efficient and reliable data management across diverse communication protocols.

HOW IT WORKS

a)	Support TCP/IP Communication (IP Address and Port Number) for Both Reading and Writing Values

How It’s Implemented:

•	TCP Communication: The server is set up using the socket library, which supports TCP/IP communication. This allows the server to send and receive data over the network.

•	IP Address and Port Number: The server listens on a specified IP address and port number, which are defined in the Server class constructor (host and port parameters).

•	Reading and Writing Values:
o	Reading: The server receives data from clients using self.connection.recv(1024).decode().
o	Writing: The server sends data back to clients using self.connection.send(response.encode()).
b)	Communicate with Multiple Devices Simultaneously

How It’s Implemented:

•	Concurrency: The DeviceHandler class extends threading.Thread. Each connection is handled in a separate thread, allowing the server to manage multiple connections simultaneously.

•	Thread Management: Each client connection starts a new DeviceHandler thread, which handles communication with that specific client independently of others.

c)	Support Future Additions of Communication Protocols

How It’s Implemented:

•	Protocol Abstraction: The TCPProtocol class in protocols/tcp_protocol.py acts as an abstraction layer for protocol-specific logic. This design allows for easy addition of new protocols.
 
•	Extensibility: To support new protocols, you can:
1.	Create a new protocol class (e.g., UDPProtocol) in the protocols/ directory.

2.	Implement the necessary methods for the new protocol.

3.	Update the server to use the new protocol class when needed.

d)	Provide a Stub to Test TCP/IP Communication

How It’s Implemented:

•	Client Stub: A simple client script (client_stub.py) is provided to test TCP/IP communication. This script connects to the server, sends messages, and receives responses.

•	Purpose: The client stub allows you to verify that the server is correctly receiving and responding to data, providing a basic test of TCP/IP communication functionality.

e)	Have Program/Code-Driven Unit Test Cases

How It’s Implemented:

•	Unit Tests: The tests/test_tcp_protocol.py file contains unit tests for the TCPProtocol class.
o	unittest Framework: Uses Python’s built-in unittest framework to define and run tests.
o	Test Case: The test_handle_message method checks if the TCPProtocol class processes messages correctly.

o	Automation: Tests are run automatically using python -m unittest discover, ensuring that changes to the code are validated.

SETUP TO RUN CODE

1.	Create the protocols Directory

2.	Create the tests Directory

3.	Create tcp_protocol.py python file in protocols directory

4.	Create test_tcp_protocol.py python file in tests directory

5.	Create client_test.py python file

6.	Add Code to tcp_protocol.py

7.	Add Code to test_tcp_protocol.py

8.	Add Code to client_test.py

HOW WE TEST IT

1.	Run the Server:

o	Open a terminal and navigate to the directory containing main.py.
o	Run: main.py
o	The server will start listening on localhost:5000. Running Client tests:
2.	Test with a Client Stub:

o	Run this client_stub.py code in another terminal
o	Enter a message and observe the server’s response.
3.	Terminate the Server:

o	Stop the server by pressing Ctrl + C in the terminal where it’s running.
Running Unit Tests

1.	Run the Tests:

o	In a terminal, navigate to the tests directory.
o	Run: test_tcp_protocol code
o	This will execute all tests in the tests directory and show the results.
Summary

•	Server: Listens for client connections and handles messages using TCP.
•	
•	Protocol Handling: Processes and responds to messages according to the protocol defined.
•	Client Stub: Allows you to interact with the server for testing.
•	Unit Tests: Validate that the protocol handling works as expected. 
