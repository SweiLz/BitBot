from node_class import NodeSub
import pyaudio


def main():
    speaker = NodeSub("tcp://127.0.0.1:4000","speaker")
    
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT,channels=CHANNELS,rate=RATE,output=True)
    
    def speaker_out(data):
        stream.write(data)

    speaker.run(speaker_out)
    

if __name__ == '__main__':
    main()