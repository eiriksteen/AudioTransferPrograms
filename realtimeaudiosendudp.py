#uses UDP to send real time audio

import pyaudio
from socket import *

def sendAudio(seconds):
    serverName = "192.168.0.139"
    serverPort = 12000

    clientSocket = socket(AF_INET, SOCK_DGRAM)

    chunk = 1024 
    sample_format = pyaudio.paInt16 
    channels = 1
    fs = 44100 
    #seconds = 3

    p = pyaudio.PyAudio()

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)
                    
                    
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        clientSocket.sendto(data, (serverName, serverPort))


    clientSocket.sendto("done".encode(), (serverName, serverPort))

    stream.stop_stream()
    stream.close()

    p.terminate()
    clientSocket.close()

    print('Finished recording')
    
    
sendAudio(10)
