# -*- coding: utf-8 -*-
"""
 Copyright © 2014, Emutex Ltd.
 All rights reserved.
 http://www.emutex.com

 Author: Nicolás Pernas Maradei <nicolas.pernas.maradei@emutex.com>

 See license in LICENSE file.

 This example is inspired on Arduino Blink example.
 http://arduino.cc/en/Tutorial/Blink

"""

# Import the time module enable sleeps between turning the led on and off.
import time

# Import the GPIOGalileoGen2 class from the wiringx86 module.
from wiringx86 import GPIOGalileoGen2 as GPIO

# Create a new instance of the GPIOGalileoGen2 class.
# Setting debug=True gives information about the interaction with sysfs.
gpio = GPIO(debug=False)
pin = 13
state = gpio.HIGH

# Set pin 13 to be used as an output GPIO pin.
print 'Setting up pin %d' % pin
gpio.pinMode(pin, gpio.OUTPUT)

print 'Blinking pin %d now...' % pin
try:
    while(True):
        # Write a state to the pin. ON or OFF.
        gpio.digitalWrite(pin, state)

        # Toggle the state.
        state = gpio.LOW if state == gpio.HIGH else gpio.HIGH

        # Sleep for a while.
        time.sleep(0.5)

# When you get tired of seeing the led blinking kill the loop with Ctrl-C.
except KeyboardInterrupt:
    # Leave the led turned off.
    print '\nCleaning up...'
    gpio.digitalWrite(pin, gpio.LOW)

    # Do a general cleanup. Calling this function is not mandatory.
    gpio.cleanup()
