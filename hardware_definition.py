from pyControl.hardware import *
from hex_port import Hex_port  # adjust import path if hex_port.py lives in a devices/ subfolder

board = Breakout_1_2()  # TODO: confirm this matches your breakout board's hardware revision

port1 = Hex_port(board.port_1, rising_event='lick1', falling_event='lick_off1')
