from subprocess import call
from pythonosc import dispatcher, osc_server

def display(unused_addr, v1='../../small.mp4'):
    # cmd = ['omxplayer', '--display', '5', '-o', 'alsa', v1]
    cmd = 'omxplayer --display 5 '+ v1
    print('command : ', cmd)
    call(cmd, shell=True)

def main():
    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/d", display)
    server = osc_server.ThreadingOSCUDPServer(("127.0.0.1", 5002), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()

if __name__ == '__main__':
    main()