from node_class import NodeSub
import pyaudio


def main():
    speaker_hdmi = NodeSub("tcp://127.0.0.1:5000","speaker_dmi")
    microphone = NodeSub("tcp://127.0.0.1:5000","microphone")

    def ok(msg):
        print("OK:",msg['symbol'])
    
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT,channels=CHANNELS,rate=RATE,output=True)
    
    def speak(data):
        stream.write(data)
    

    microphone.run(speak)

    

if __name__ == '__main__':
    main()