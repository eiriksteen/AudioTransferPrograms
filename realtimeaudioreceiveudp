#uses udp to receive audio in real time

import pyaudio
from socket import *

def receiveAudio():
    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(("", serverPort))

    print("Ready")

    chunk = 1024 
    sample_format = pyaudio.paInt16 
    channels = 1
    fs = 44100  

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    output=True)

    while True:
        audioChunk, clientAddress = serverSocket.recvfrom(2048)
        stream.write(audioChunk)

        try:
            if audioChunk.decode() == "done":
                break
        except:
            continue

    stream.stop_stream()
    stream.close()

    serverSocket.close()

receiveAudio()
