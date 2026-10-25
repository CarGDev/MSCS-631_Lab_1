import sys
from socket import *

host = sys.argv[1]
port = int(sys.argv[2])
filename = sys.argv[3]

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((host, port))

requestMessage = (
    "GET /" + filename + " HTTP/1.1\r\nHost: " + host + ":" + str(port) + "\r\n\r\n"
)
clientSocket.send(requestMessage.encode())

responseMessage = ""
while True:
    response = clientSocket.recv(4096)
    if not response:
        break

    responseMessage += response.decode()

print(responseMessage[: responseMessage.index("\r\n\r\n")])

if "\r\n\r\n" in responseMessage:
    content = responseMessage[responseMessage.index("\r\n\r\n") + 4 :]
    print(content)


clientSocket.close()
