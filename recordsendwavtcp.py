from socket import *
import recordplaywavfile

serverName = "192.168.0.139"
serverPort = 12001
BUFFER_SIZE = 2048

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

filename = "test.wav"
recordplaywavfile.recordWavFile(filename, 3)

f = open(filename, "rb")

while True:
    bytesRead = f.read(BUFFER_SIZE)

    if not bytesRead:
        break

    clientSocket.send(bytesRead)


result = clientSocket.recv(2048)
print(result.decode())
clientSocket.close()
