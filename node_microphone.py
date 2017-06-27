from node_class import NodePub
import pyaudio

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024


def main():
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK)

    mic = NodePub("tcp://127.0.0.1:5000")

    while True:
        data = stream.read(CHUNK)
        mic.send('microphone', data)

    stream.stop_stream()
    stream.close()
    audio.terminate()

if __name__ == '__main__':
    main()