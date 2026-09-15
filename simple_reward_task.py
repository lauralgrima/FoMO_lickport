from pyControl.utility import *
import hardware_definition as hw

states = ['waiting', 'reward']
events = ['lick1']
initial_state = 'waiting'


def waiting(event):
    if event == 'lick1':
        goto_state('reward')


def reward(event):
    if event == 'entry':
        hw.port1.SOL.on()
        timed_goto_state('waiting', 50)  # 50 ms reward pulse
    elif event == 'exit':
        hw.port1.SOL.off()
