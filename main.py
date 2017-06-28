from node_class import NodePub,NodeSub


def main():
    microphone = NodeSub("tcp://192.168.1.244:5000","microphone")
    speaker = NodePub("tcp://127.0.0.1:4000")

    def play_microphone(data):
        # print("Recieve data")
        speaker.send("speaker",data)

    microphone.run(play_microphone)


if __name__ == '__main__':
    main()