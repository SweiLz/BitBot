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
    for x in range(10):
        # client.send_message("/n", "../../small.mp4")
        client.send_message("/n", "resources/emotions/test_effect_01.mp4")
        print(x)
        time.sleep(3)
