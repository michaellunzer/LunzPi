#!/usr/bin/python
import csv
import urllib

import atexit

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
font = ImageFont.load("helvR08.pil")

count = 0
volume = 0

oldimage = None

status = {"time": None, "weather": None, "temp": None, "volume": None, "progressbar": None}

NewStatus = {"time": None, "weather": None, "temp": None, "volume": None, "progressbar": None}
 

#Colors
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
lightblue = (0,221,237)
blue = "blue"
mint = (146, 224, 173)

red1 = (229, 1, 18)
red2 = (181, 11, 23)
red3 = (147, 8, 18) 
red4 = (61, 0, 4)

#ColorLocations

VolumeColor = red1
ProgressbarColor = mint
TimeColor = blue
AMPMColor = red

# Clear matrix on exit.  Otherwise it's annoying if you need to break and
# fiddle with some code while LEDs are blinding you.

def clearOnExit():
    matrix.Clear()

atexit.register(clearOnExit)

 
while True:
    
    
    time.sleep(2)
    
    # white = (255,255,255)
    # red = (255,0,0)
    # black = (0,0,0)
    # lightblue = (0,221,237)
    #mint = (146, 224, 173)
    
    image = Image.new("RGB", (32, 16), (black))

    draw = ImageDraw.Draw(image)
    drawstring1 = time.strftime(" %-I:%M") 
    drawstring2 = time.strftime("%p")
   
#Weather Area:
    
    #print(count)

    #if count % 1000 == 0:
      #  yahoo_result = pywapi.get_weather_from_yahoo('94062', 'imperial')
        
    #count+=1
    
    #print "Yahoo says: It is " + string.lower(yahoo_result['condition']['text']) + " and " + yahoo_result['condition']['temp'] + "F now in Portland.\n\n"

    #print(count)
    
    #weather_condition = string.lower(yahoo_result['condition']['text']) 

    weather_condition = "fair"

    #print(weather_condition)
    
    #NewStatus["weather"] = weather_condition
    
    #weather_temp = yahoo_result['condition']['temp']

    weather_temp = "61"

    #print(weather_temp)
    
    #NewStatus["temp"] = weather_temp
    
    #print(yahoo_result)
    
    
    
    if weather_temp >= "70":
        draw.text((0,-1), weather_temp, font=font, fill="red")
        draw.ellipse((11,1) + (12, 1), fill="red")
    elif weather_temp >= "60":
        draw.text((0,-1), weather_temp, font=font, fill="orange")
        draw.ellipse((9,2) + (10, 3), fill="red")
    elif weather_temp >= "50":
        draw.text((0,-1), weather_temp, font=font, fill="yellow")
        draw.ellipse((9,2) + (10, 3), fill="red")
    elif weather_temp >= "40":
        draw.text((0,-1), weather_temp, font=font, fill=lightblue)
        draw.ellipse((9,2) + (10, 3), fill="red")
    else:
        draw.text((-1,-1), weather_temp, font=font, fill="blue")
        draw.ellipse((9,2) + (10, 3), fill="red")
    
    #draw.text((-1,-1), weather_temp, font=font, fill="green")
    
    if weather_condition == "sunny":
        draw.ellipse((28, 0) +(32, 4), fill="yellow")
        
    elif weather_condition == "cloudy":
        draw.ellipse((28, 0) +(32, 4), fill="white")
        draw.ellipse((23, 0) +(27, 4), fill="white")
        draw.ellipse((18, 0) +(22, 4), fill="white")
        
    elif weather_condition == "mostly cloudy":
        draw.ellipse((30, 0) +(34, 4), fill="grey")
        draw.ellipse((25, 2) +(29, 6), fill="grey")
        draw.ellipse((21, 0) +(25, 4), fill="grey")

#need to draw windy!!!!!~~~~
    elif weather_condition == "mostly cloudy/windy":
        draw.ellipse((30, 0) +(34, 4), fill="grey")
        draw.ellipse((25, 2) +(29, 6), fill="grey")
        draw.ellipse((21, 0) +(25, 4), fill="grey")

    elif weather_condition == "partly cloudy":
        draw.ellipse((30, 0) +(34, 4), fill="grey")
        draw.ellipse((25, 2) +(29, 6), fill="grey")
        draw.ellipse((21, 0) +(25, 4), fill="grey")
    
    elif weather_condition == "light rain":
        draw.ellipse((28, 0) +(32, 4), fill="grey")
        draw.ellipse((23, 0) +(27, 4), fill="grey")
        draw.ellipse((18, 0) +(22, 4), fill="grey")
        draw.line((30,3) + (30 ,8), fill="blue")
        draw.line((28,3) + (28 ,8), fill=lightblue)
        draw.line((23,3) + (23 ,8), fill="blue")
        draw.line((18,3) + (18 ,8), fill=lightblue)
        draw.line((26,3) + (26 ,8), fill="blue")
        draw.line((21,3) + (21 ,8), fill=lightblue)
        
    elif weather_condition == "rain":
        draw.ellipse((28, 0) +(32, 4), fill="grey")
        draw.ellipse((23, 0) +(27, 4), fill="white")
        draw.ellipse((18, 0) +(22, 4), fill="grey")
        draw.line((30,3) + (30 ,8), fill="blue")
        draw.line((28,3) + (28 ,8), fill="blue")
        draw.line((23,3) + (23 ,8), fill="blue")
        draw.line((18,3) + (18 ,8), fill="blue")
        draw.line((26,3) + (26 ,8), fill="blue")
        draw.line((21,3) + (21 ,8), fill="blue")    
        
    elif weather_condition == "fair":
        draw.ellipse((28, 0) +(32, 4), fill="grey")
        draw.ellipse((21, 0) +(25, 4), fill="grey")
        draw.ellipse((16, 0) +(20, 4), fill="grey")
        
    else:
        draw.line((0, 0) + image.size, fill=128)
        draw.line((0, image.size[1], image.size[0], 0), fill=128)

#Clock Area:
    

    if int(time.strftime("%-I")) < 10:
        #print(int(time.strftime("%-I")))
        draw.text((1,6), drawstring1, font=font, fill=TimeColor)
        draw.text((19,6), drawstring2, font=font, fill=AMPMColor)
    else:
        #print(int(time.strftime("%-I")))
        draw.text((-3,6), drawstring1, font=font, fill=TimeColor)
        draw.text((19,6), drawstring2, font=font, fill=AMPMColor)
    
#MPC Volume Area:
    
        
    mpcstatus = subprocess.check_output("mpc status", shell=True, stderr=subprocess.STDOUT)

    match = re.search(r' (\d+)\%', mpcstatus)
 
 
    if match:
        volume = int(match.groups()[0])
        
        #print("volume = {volume}".format(volume = volume))

        if volume <= 0:
            print("volume is less than 0%")    
        elif volume <= 6:
            draw.line((0,15) + (0 ,15), fill=VolumeColor)
        elif volume <= 12:
            draw.line((0,14) + (0 ,15), fill=VolumeColor)
        elif volume <= 18:
            draw.line((0,13) + (0 ,15), fill=VolumeColor)
        elif volume <= 25:
            draw.line((0,12) + (0 ,15), fill=VolumeColor)
        elif volume <= 31:
            draw.line((0,11) + (0 ,15), fill=VolumeColor)
        elif volume <= 37:
            draw.line((0,10) + (0 ,15), fill=VolumeColor)
        elif volume <= 43:
            draw.line((0,9) + (0 ,15), fill=VolumeColor)
        elif volume <= 50:
            draw.line((0,8) + (0 ,15), fill=VolumeColor)
        elif volume <= 56:
            draw.line((0,7) + (0 ,15), fill=VolumeColor)
        elif volume <= 62:
            draw.line((0,6) + (0 ,15), fill=VolumeColor)
        elif volume <= 68:
            draw.line((0,5) + (0 ,15), fill=VolumeColor)
        elif volume <= 75:
            draw.line((0,4) + (0 ,15), fill=VolumeColor)
        elif volume <= 81:
            draw.line((0,3) + (0 ,15), fill=VolumeColor)
        elif volume <= 87:
            draw.line((0,2) + (0 ,15), fill=VolumeColor)
        elif volume <= 93:
            draw.line((0,1) + (0 ,15), fill=VolumeColor)
        elif volume <= 100:
            draw.line((0,0) + (0 ,15), fill=VolumeColor)
        else:
            draw.text((6,-1), str(volume), font=font, fill="orange")
            print('volume outside range (else)')
    
#ProgressBar Area:
    mpcstatus2 = subprocess.check_output("mpc status", shell=True, stderr=subprocess.STDOUT)
    match2 = re.search(r'\((\d+)\%\)', mpcstatus2)
   
    
    if match2:
        progressbar = int(match2.groups()[0])
        
        #print("progressbar = {progressbar}".format(progressbar = progressbar))
        
         
        if progressbar <= 0:
            print("progressbar is less than 0%")    
        elif progressbar <= 3.125:
            draw.line((0,15) + (0 ,15), fill=ProgressbarColor)
        elif progressbar <= 6.25:
            draw.line((0,15) + (1 ,15), fill=ProgressbarColor)
        elif progressbar <= 9.375:
            draw.line((0,15) + (2 ,15), fill=ProgressbarColor)
        elif progressbar <= 12.5:
            draw.line((0,15) + (3 ,15), fill=ProgressbarColor)
        elif progressbar <= 15.625:
            draw.line((0,15) + (4 ,15), fill=ProgressbarColor)
        elif progressbar <= 18.75:
            draw.line((0,15) + (5 ,15), fill=ProgressbarColor)
        elif progressbar <= 21.875:
            draw.line((0,15) + (6 ,15), fill=ProgressbarColor)
        elif progressbar <= 25:
            draw.line((0,15) + (7 ,15), fill=ProgressbarColor)
        elif progressbar <= 28.125:
            draw.line((0,15) + (8 ,15), fill=ProgressbarColor)
        elif progressbar <= 31.25:
            draw.line((0,15) + (9 ,15), fill=ProgressbarColor)
        elif progressbar <= 34.375:
            draw.line((0,15) + (10 ,15), fill=ProgressbarColor)
        elif progressbar <= 37.5:
            draw.line((0,15) + (11 ,15), fill=ProgressbarColor)
        elif progressbar <= 40.625:
            draw.line((0,15) + (12 ,15), fill=ProgressbarColor)
        elif progressbar <= 43.75:
            draw.line((0,15) + (13 ,15), fill=ProgressbarColor)
        elif progressbar <= 46.875:
            draw.line((0,15) + (14 ,15), fill=ProgressbarColor)
        elif progressbar <= 50:
            draw.line((0,15) + (15 ,15), fill=ProgressbarColor)
        elif progressbar <= 53.125:
            draw.line((0,15) + (16 ,15), fill=ProgressbarColor)
        elif progressbar <= 56.25:
            draw.line((0,15) + (17 ,15), fill=ProgressbarColor)
        elif progressbar <= 59.375:
            draw.line((0,15) + (18 ,15), fill=ProgressbarColor)
        elif progressbar <= 62.5:
            draw.line((0,15) + (19 ,15), fill=ProgressbarColor)
        elif progressbar <= 65.625:
            draw.line((0,15) + (20 ,15), fill=ProgressbarColor)
        elif progressbar <= 68.75:
            draw.line((0,15) + (21 ,15), fill=ProgressbarColor)
        elif progressbar <= 71.875:
            draw.line((0,15) + (22 ,15), fill=ProgressbarColor)
        elif progressbar <= 75:
            draw.line((0,15) + (23 ,15), fill=ProgressbarColor)
        elif progressbar <= 78.125:
            draw.line((0,15) + (24 ,15), fill=ProgressbarColor)
        elif progressbar <= 81.25:
            draw.line((0,15) + (25 ,15), fill=ProgressbarColor)
        elif progressbar <= 84.375:
            draw.line((0,15) + (26 ,15), fill=ProgressbarColor)
        elif progressbar <= 87.5:
            draw.line((0,15) + (27 ,15), fill=ProgressbarColor)
        elif progressbar <= 90.625:
            draw.line((0,15) + (28 ,15), fill=ProgressbarColor)
        elif progressbar <= 93.75:
            draw.line((0,15) + (29 ,15), fill=ProgressbarColor)
        elif progressbar <= 96.875:
            draw.line((0,15) + (30 ,15), fill=ProgressbarColor)
        elif progressbar <= 100:
            draw.line((0,15) + (31 ,15), fill=ProgressbarColor)
        else:
            draw.text((6,-1), str(progressbar), font=font, fill="orange")
            print('progressbar outside range (else)')
    
    
    
    # if image.im == oldimage:
    #     print("pass")
    # else:
    #     oldimage == image.im.copy()
    #     #print("hi")
        matrix.SetImage(image.im.id) #write to the screen
