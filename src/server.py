import sys
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)

serverPort = 5005
serverSocket.bind(("", serverPort))
serverSocket.listen(1)

while True:
    print("Ready to serve...")
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]

        file = open(filename[1:])
        outputdata = file.read()

        header = (
            "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: "
            + str(len(outputdata))
            + "\r\n\r\n"
        )
        connectionSocket.send(header.encode())
        for i in range(len(outputdata)):
            connectionSocket.send(outputdata[i].encode())

        connectionSocket.close()

    except IOError:
        error_header = "HTTP/1.1 404 Not Found\r\n\r\n"
        error_message = "<html><head></head><body><h1>404 Not Found</h1></body></html>"
        connectionSocket.send((error_header + error_message).encode())

        connectionSocket.close()

    finally:
        connectionSocket.close()
