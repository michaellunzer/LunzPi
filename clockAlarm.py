#!/usr/bin/python
import csv
import urllib

import os
import pywapi
import string

import sys
import subprocess

import re

import time
import ImageDraw
from PIL import Image
import ImageFont
from rgbmatrix import Adafruit_RGBmatrix


matrix = Adafruit_RGBmatrix(16, 1)
# font = ImageFont.load("helvR08.pil")

# count = 0
# volume = 0

# oldimage = None

# status = {"time": None, "weather": None, "temp": None, "volume": None, "progressbar": None}

# NewStatus = {"time": None, "weather": None, "temp": None, "volume": None, "progressbar": None}
 

# #Colors
# white = (255,255,255)
# red = (255,0,0)
# black = (0,0,0)
# lightblue = (0,221,237)
# blue = "blue"

# red1 = (229, 1, 18)
# red2 = (181, 11, 23)
# red3 = (147, 8, 18) 
# red4 = (61, 0, 4)

# #ColorLocations

# VolumeColor = red1
# ProgressbarColor = red2
# TimeColor = black
# AMPMColor = black


 
# while True:
    
    
#     time.sleep(1)
    
#     white = (255,255,255)
#     red = (255,0,0)
#     black = (0,0,0)
#     lightblue = (0,221,237)
    
#     image = Image.new("RGB", (32, 16), (white))

#     draw = ImageDraw.Draw(image)
#     drawstring1 = time.strftime(" %-I:%M") 
#     drawstring2 = time.strftime("%p")
   


#Clock Area:
    

    # if int(time.strftime("%-I")) < 10:
    #     #print(int(time.strftime("%-I")))
    #     draw.text((1,6), drawstring1, font=font, fill=TimeColor)
    #     draw.text((19,6), drawstring2, font=font, fill=AMPMColor)
    # else:
    #     #print(int(time.strftime("%-I")))
    #     draw.text((-3,6), drawstring1, font=font, fill=TimeColor)
    #     #draw.text((19,6), drawstring2, font=font, fill=AMPMColor)
    


# Show RGB test pattern (separate R, G, B color values)



image = Image.new("1", (32, 16))

draw  = ImageDraw.Draw(image)

row = 0
column = 0

while True:
    if column < 31:
        # for row in range(15):
        for column in range(31):
            draw.line((row, 0, 0, column), fill=1)
            #row = 1
            row = row + 2
            column = column + 1

            matrix.SetImage(image.im.id)
            time.sleep(.1)

else:
    row = 0
    column = 0
    draw.line((row, 0, 0, column), fill=0)
    row = row + 1
    column = column + 1

    matrix.SetImage(image.im.id)
    time.sleep(.1)
    

# for b in range(16):
#     for g in range(8):
#         for r in range(8):
#             matrix.SetPixel(
#               (b / 4) * 8 + g,
#               (b & 3) * 8 + r,
#               (r * 0b001001001) / 2,
#               (g * 0b001001001) / 2,
#                b * 0b00010001)


#time.sleep(10)
matrix.Clear()

    
    
    
    # if image.im == oldimage:
    #     print("pass")
    # else:
    #     oldimage == image.im.copy()
    #     #print("hi")
    #     matrix.SetImage(image.im.id)
