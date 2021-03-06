#receive wav file through tcp and play 

from socket import *
import recordplaywavfile
import pyaudio
import wave

def receiveAudio(filename):
    serverPort = 12001
    bufferSize = 2048

    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(("", serverPort))
    serverSocket.listen(1)

    print("ready")

    audio = b""
    connectionSocket, addr = serverSocket.accept()

    while True:
        audioChunk = connectionSocket.recv(bufferSize)

        audio += audioChunk

        if len(audioChunk) != bufferSize:
            break

    p = pyaudio.PyAudio()

    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 1
    fs = 44100  # Record at 44100 samples per second

    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(audio)
    wf.close()

    recordplaywavfile.playWavFile(filename)

    connectionSocket.send("success".encode())
    connectionSocket.close()
    serverSocket.close()


receiveAudio("audiofile.wav")
