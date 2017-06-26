from subprocess import DEVNULL, STDOUT, check_call
from pythonosc import dispatcher
from pythonosc import osc_server


def display(unused_addr, v1):
    cmd = ['omxplayer', '--display', '0', '-o', 'alsa', '../../small.mp4']
    check_call(cmd, stdout=DEVNULL, stderr=STDOUT)


parser = argparse.ArgumentParser()
parser.add_argument("--ip",
                    default="127.0.0.1", help="The ip to listen on")
parser.add_argument("--port",
                    type=int, default=5001, help="The port to listen on")
args = parser.parse_args()
dispatcher = dispatcher.Dispatcher()
dispatcher.map("/d", display)
server = osc_server.ThreadingOSCUDPServer(
    (args.ip, args.port), dispatcher)
print("Serving on {}".format(server.server_address))
