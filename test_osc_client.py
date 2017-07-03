"""Small example OSC client

This program sends 10 random values between 0.0 and 1.0 to the /filter address,
waiting for 1 seconds between each value.
"""

import random
import time

from pythonosc import osc_message_builder
from pythonosc import udp_client


if __name__ == "__main__":

    client = udp_client.SimpleUDPClient("192.168.1.243", 4001)
    client.send_message("/d", "../../small.mp4")
