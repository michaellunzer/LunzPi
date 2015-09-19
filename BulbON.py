#!/usr/bin/python

# Smart Bulb Colorific! Control With Bluez
# Author: Tony DiCola
#
# This script will cycle a Smart Bulb Colorific! Bluetooth Low Energy light bulb
# through a rainbow of different hues.
#
# Dependencies:
# - You must install the pexpect library, typically with 'sudo pip install pexpect'.
# - You must have bluez installed and gatttool in your path (copy it from the
#   attrib directory after building bluez into the /usr/bin/ location).
#
# License: Released under an MIT license: http://opensource.org/licenses/MIT



import colorsys
import math
import sys
import time

import pexpect



# Get bulb address from command parameters.
if len(sys.argv) != 2:
    print 'Error must specify bulb address as parameter!'
    print 'Usage: sudo python colorific.py <bulb address>'
    print 'Example: sudo python BulbON.py D6:23:4B:09:AC:E6'
    sys.exit(1)
bulb = sys.argv[1]

# Run gatttool interactively.
gatt = pexpect.spawn('gatttool -I')

# Connect to the device.
gatt.sendline('connect {0}'.format(bulb))
gatt.expect('Connection successful')

gatt.sendline('char-write-cmd 0x001b FF000000')
