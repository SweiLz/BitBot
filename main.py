from node_class import NodePub,NodeSub


def main():
    microphone = NodeSub("tcp://127.0.0.1:5000","microphone")
    speaker = NodePub("tcp://127.0.0.1:4000")

    def play_microphone(data):
        speaker.send("speaker",data)

    microphone.run(play_microphone)


if __name__ == '__main__':
    main()