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