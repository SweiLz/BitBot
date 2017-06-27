import zmq
import threading

class NodePub:
    def __init__(self, addr="tcp://127.0.0.1:5000"):
        self.ctx = zmq.Context()
        self.pub = self.ctx.socket(zmq.PUB)
        self.pub.bind(addr)
    
    def send(self, topic, pyobj):
        self.pub.send_string(topic, zmq.SNDMORE)
        self.pub.send_pyobj(pyobj)
    
class NodeSub:
    def __init__(self, addr="tcp://127.0.0.1:5000",topic=None):
        self.ctx = zmq.Context()        
        self.sub = self.ctx.socket(zmq.SUB)
        self.sub.setsockopt_string(zmq.SUBSCRIBE,topic)
        self.sub.connect(addr)

    def loop(self):
        while True:
            self.topic = self.sub.recv_string()
            self.msgs = self.sub.recv_pyobj()
            self.call(self.msgs)

    def run(self, callback):
        self.call = callback
        self.thread = threading.Thread(target=self.loop)
        self.thread.start()
    


# speaker_alsa = NodeSub("127.0.0.1:5000","speaker_alsa")

# def callback(msg):
#     print("OK:",msg)



# speaker_hdmi.run(callback)
# speaker_alsa.run(callback)
# while True:
#     print("..")
#     time.sleep(3)

#################################### PUBLISHER
# import time
# from node_class import NodePub

# def main():
#     stock_data = {
#         'symbol': 'ABB',
#         'price' : 230
#     }
#     stock_data2 = [10,20,30,40,50] 

#     fb_bot = NodePub("tcp://127.0.0.1:5000")

#     while True:
#         fb_bot.send('speaker_hdmi',stock_data)
#         time.sleep(1)

# if __name__ == '__main__':
#     main()

######################## SUBSCRIBE
# from node_class import NodeSub
# import pyaudio


# def main():
#     speaker_hdmi = NodeSub("tcp://127.0.0.1:5000","speaker_dmi")
#     microphone = NodeSub("tcp://127.0.0.1:5000","microphone")

#     def ok(msg):
#         print("OK:",msg['symbol'])
    
#     FORMAT = pyaudio.paInt16
#     CHANNELS = 2
#     RATE = 44100
#     audio = pyaudio.PyAudio()
#     stream = audio.open(format=FORMAT,channels=CHANNELS,rate=RATE,output=True)
    
#     def speak(data):
#         stream.write(data)
    

#     microphone.run(speak)

    

# if __name__ == '__main__':
#     main()