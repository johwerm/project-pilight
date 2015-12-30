#!/usr/bin/env python

""" Script to communicate with a power switching circuit. """

import subprocess
import RPi.GPIO as gpio

POWER_ALERT_INPUT_PIN = 10

def init():
    """ Initializes GPIO pins and IRQ. """
    gpio.setmode(gpio.BOARD)
    gpio.setup(POWER_ALERT_INPUT_PIN, gpio.IN)
    
    # Check initial state.
    if not gpio.input(POWER_ALERT_INPUT_PIN):
        # Add interrupt for future signals.
        gpio.wait_for_edge(POWER_ALERT_INPUT_PIN, gpio.RISING)

    shutdown()

def shutdown():
    """ The interrupt callback function, shutting down the RBPi. """
    gpio.cleanup()
    subprocess.call(["/sbin/shutdown", "-h", "now"])

# Start script.
init()
