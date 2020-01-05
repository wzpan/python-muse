# a toy example to demostrate how to 
# interact with Muse Headband in Python.
# author: josephpan m[AT]hahack.com
# 2019-11-21

import struct
import socket
import time
import random
import subprocess
import argparse

from pythonosc import dispatcher
from pythonosc import osc_server
from pythonosc import udp_client

def alpha_handler(unused_addr, args, value):
    """
    Handler for alpha absolute value.
    Can be One Average or Four Float values.

    If you set the OSC Stream Brainwaves to `All values` 
    at Muse Monitor, you should change the param to: 

    def alpha_handler(unused_addr, args, ch1, ch2, ch3, ch4):
    """
    print("alpha value: {}".format(value))


def beta_handler(unused_addr, args, value):
    """
    Handler for beta absolute value.
    Can be One Average or Four Float values.

    If you set the OSC Stream Brainwaves to `All values` 
    at Muse Monitor, you should change the param to: 

    def beta_handler(unused_addr, args, ch1, ch2, ch3, ch4):
    """
    print("beta value: {}".format(value))


def delta_handler(unused_addr, args, value):
    """
    Handler for delta absolute value.
    Can be One Average or Four Float values.

    If you set the OSC Stream Brainwaves to `All values` 
    at Muse Monitor, you should change the param to: 

    def delta_handler(unused_addr, args, ch1, ch2, ch3, ch4):
    """
    print("delta value: {}".format(value))


def theta_handler(unused_addr, args, value):
    """
    Handler for theta absolute value.
    Can be One Average or Four Float values.

    If you set the OSC Stream Brainwaves to `All values` 
    at Muse Monitor, you should change the param to: 

    def theta_handler(unused_addr, args, ch1, ch2, ch3, ch4):
    """
    print("theta value: {}".format(value))


def gamma_handler(unused_addr, args, value):
    """
    Handler for gamma absolute value.
    Can be One Average or Four Float values.

    If you set the OSC Stream Brainwaves to `All values` 
    at Muse Monitor, you should change the param to: 

    def gamma_handler(unused_addr, args, ch1, ch2, ch3, ch4):
    """
    print("gamma value: {}".format(value))


def mellow_handler(unused_addr, args, value):
    print("mellow value: {}".format(value))
    return


def concen_handler(unused_addr, args, value):
    print("concentration value: {}".format(value))    
    return


def blink_handler(unused_addr, args, blink):
    if blink:
        print("blink")


def jaw_clench_handler(unused_addr, args, jaw):
    if jaw:
        print("Jaw_Clench")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",
                        default="127.0.0.1",
                        help="The ip to listen on")
    parser.add_argument("--port",
                        type=int,
                        default=5000,
                        help="The port to listen on")
    args = parser.parse_args()

    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/muse/elements/alpha_absolute", alpha_handler, "EEG")
    dispatcher.map("/muse/elements/beta_absolute", beta_handler, "EEG")
    dispatcher.map("/muse/elements/delta_absolute", delta_handler, "EEG")
    dispatcher.map("/muse/elements/theta_absolute", theta_handler, "EEG")
    dispatcher.map("/muse/elements/gamma_absolute", gamma_handler, "EEG")
    dispatcher.map("/muse/elements/blink", blink_handler, "EEG")
    dispatcher.map("/muse/elements/jaw_clench", jaw_clench_handler, "EEG")
    dispatcher.map("/muse/algorithm/concentration", concen_handler, "EEG")    

    server = osc_server.ThreadingOSCUDPServer(
        (args.ip, args.port), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()
