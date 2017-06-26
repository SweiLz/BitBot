from node_class import NodeSub

def main():
    speaker_hdmi = NodeSub("127.0.0.1:5000","speaker_hdmi")

    def ok(msg):
        print("OK:",msg['symbol'])
    
    speaker_hdmi.run(ok)

if __name__ == '__main__':
    main()