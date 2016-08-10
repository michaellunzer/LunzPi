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

import threading
import traceback

from datetime import datetime, time

import time as time1
import ImageDraw
from PIL import Image
import ImageFont
from rgbmatrix import Adafruit_RGBmatrix

matrix = Adafruit_RGBmatrix(16, 1)
font = ImageFont.load("helvR08.pil")

now = datetime.now()
now_time = now.time()


#Colors
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
lightblue = (0,221,237)
blue = "blue"
mint = (146, 224, 173)
green = "green"

red1 = (229, 1, 18)
red2 = (181, 11, 23)
red3 = (147, 8, 18) 
red4 = (61, 0, 4)

#ColorLocations

TimeColor = blue
AMPMColor = green

def night_mode():

    if now_time >= time(5,30) and now_time <= time(23,30):      
        global TimeColor, AMPMColor
        TimeColor = red3
        AMPMColor = red4
    else:
        global TimeColor, AMPMColor
        TimeColor = blue
        AMPMColor = green

# Clear matrix on exit.  Otherwise it's annoying if you need to break and
# fiddle with some code while LEDs are blinding you. 

def clearOnExit():
    matrix.Clear()

atexit.register(clearOnExit)


# image = Image.new("RGB", (32, 16), (black))
# draw = ImageDraw.Draw(image)

#Clock Area:
def clockArea():
    
    drawstring1 = time1.strftime(" %-I:%M:%S") 
    #drawstring2 = time1.strftime("%p")

    if int(time1.strftime("%-I")) < 10:
        #print(int(time.strftime("%-I")))
        draw.text((1,6), drawstring1, font=font, fill=TimeColor)
        #draw.text((19,6), drawstring2, font=font, fill=AMPMColor)
    else:
        #print(int(time.strftime("%-I")))
        draw.text((-3,6), drawstring1, font=font, fill=TimeColor)
        #draw.text((19,6), drawstring2, font=font, fill=AMPMColor)
   
# #Weather Area:
def getYahooWeather():
#     # threading.Timer(900.0, getYahooWeather).start()
    yahoo_result = pywapi.get_weather_from_yahoo('94062', 'imperial')
#     #weather_condition = "sunny"
#     global weather_condition
    weather_condition = string.lower(yahoo_result['condition']['text'])
    print(weather_condition)
    return weather_condition



def weatherArea(weather_condition):
#      #Weather Pictures Area   



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



delay_LED = 1
delay_weather = 10  # 15*60
time_LED = 0
time_weather = 0
current_time = 0
count = 0

try:
    while True:
        count +=1
        current_time = int(time1.time())
        # print current_time
        if (current_time > time_LED):
            night_mode()
            image = Image.new("RGB", (32, 16), (black))
            draw = ImageDraw.Draw(image)
            clockArea()
            matrix.SetImage(image.im.id) #write to the screen
            time_LED = current_time
            print "update LED time = ", count, "current time = ", current_time
            # time1.sleep(4)
        if (current_time > time_weather + delay_weather):
            yahoo_result = pywapi.get_weather_from_yahoo('97210', 'imperial')
            weather_condition = string.lower(yahoo_result['condition']['text'])
            #getYahooWeather()
            
            weatherArea(weather_condition)
            print weather_condition
            time_weather = current_time

            # need to get the weather info to write to the screen!!!
# except:
#     print "didn't work"
except Exception, e:
    traceback.print_exc()





# try:  
#     while True:
#         night_mode()
#         image = Image.new("RGB", (32, 16), (black))
#         draw = ImageDraw.Draw(image)
#         clockArea()
#         #weatherArea()
#         matrix.SetImage(image.im.id) #write to the screen
#         #time1.sleep(5) 
# except:
#     print "didn't work"
