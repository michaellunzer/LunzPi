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
font = ImageFont.load("helvR08.pil")
#url  = "http://api.thingspeak.com/channels/15486/feed.csv?key=1X5610SMHNUIF9XL"
#def gettemp(url):
#    response = urllib.urlopen(url)
#    cr = csv.reader(response)
#    rows=list(cr)
#    row1=rows[100]
#    return row1[2]

#print "Current temp is " + gettemp(url)  +" degrees."
count = 0
volume = 0

oldimage = None

status = {"time": None, "weather": None, "temp": None, "volume": None, "progressbar": None}

NewStatus = {"time": None, "weather": None, "temp": None, "volume": None, "progressbar": None}
 

 
while True:
    
    
    time.sleep(1)
    
    white = (255,255,255)
    red = (255,0,0)
    black = (0,0,0)
    lightblue = (0,221,237)
    
    image = Image.new("RGB", (32, 16), (black))

    draw = ImageDraw.Draw(image)
    drawstring1 = time.strftime("%I:%M") 
    drawstring2 = time.strftime("%p")
    #"Current temp is " + gettemp(url)  +" degrees."
    
    #for n in range(32, -image.size[0], -1): # Scroll R to L
    #matrix.SetImage(image.im.id) #, n, 0)
    #time.sleep(5)
    #matrix.Clear()
    #time.sleep(2)

#Weather Area:
    
    #print(count)

    if count % 1000 == 0:
        yahoo_result = pywapi.get_weather_from_yahoo('97210', 'imperial')
        
    count+=1
    
    #print "Yahoo says: It is " + string.lower(yahoo_result['condition']['text']) + " and " + yahoo_result['condition']['temp'] + "F now in Portland.\n\n"

    #print(count)
    
    weather_condition = string.lower(yahoo_result['condition']['text']) 
    
    NewStatus["weather"] = weather_condition
    
    weather_temp = yahoo_result['condition']['temp']
    
    NewStatus["temp"] = weather_temp
    
    #print(yahoo_result)
    
    #print weather_temp
    
    if weather_temp >= "70":
        draw.text((-1,-1), weather_temp, font=font, fill="red")
        draw.ellipse((9,2) + (10, 3), fill="red")
    elif weather_temp >= "60":
        draw.text((-1,-1), weather_temp, font=font, fill="orange")
        draw.ellipse((9,2) + (10, 3), fill="red")
    elif weather_temp >= "50":
        draw.text((-1,-1), weather_temp, font=font, fill="yellow")
        draw.ellipse((9,2) + (10, 3), fill="red")
    elif weather_temp >= "40":
        draw.text((-1,-1), weather_temp, font=font, fill=lightblue)
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
    draw.text((-1,6), drawstring1, font=font, fill="blue")
    draw.text((19,6), drawstring2, font=font, fill=red)
    
#MPC Volume Area:
    
    #volume = subprocess.check_output("mpc status | grep volume", shell=True, stderr=subprocess.STDOUT)  
    #time.sleep(1)
    #volume = volume[7:volume.find("%")]
    #volume = int(volume)
    #volume = int(re.search(r"\d+\%", volume)[:-1])

    
    mpcstatus = subprocess.check_output("mpc status", shell=True, stderr=subprocess.STDOUT)
    print(repr(mpcstatus))
    match = re.search(r'(\d+)\%', mpcstatus)
    #print(match)
    
    """print(repr(mpcstatus))
    print(type(mpcstatus))"""
    
    print(repr(match))
    print(type(match))
    
 
    
    if match:
        volume = int(match.groups()[0])
        
        print("volume = {volume}".format(volume = volume))
        
         
        if volume <= 0:
            print("volume is less than 0%")    
        elif volume <= 6:
            draw.line((0,15) + (0 ,15), fill=128)
        elif volume <= 12:
            draw.line((0,14) + (0 ,15), fill=128)
        elif volume <= 18:
            draw.line((0,13) + (0 ,15), fill=128)
        elif volume <= 25:
            draw.line((0,12) + (0 ,15), fill=128)
        elif volume <= 31:
            draw.line((0,11) + (0 ,15), fill=128)
        elif volume <= 37:
            draw.line((0,10) + (0 ,15), fill=128)
        elif volume <= 43:
            draw.line((0,9) + (0 ,15), fill=128)
        elif volume <= 50:
            draw.line((0,8) + (0 ,15), fill=128)
        elif volume <= 56:
            draw.line((0,7) + (0 ,15), fill=128)
        elif volume <= 62:
            draw.line((0,6) + (0 ,15), fill=128)
        elif volume <= 68:
            draw.line((0,5) + (0 ,15), fill=128)
        elif volume <= 75:
            draw.line((0,4) + (0 ,15), fill=128)
        elif volume <= 81:
            draw.line((0,3) + (0 ,15), fill=128)
        elif volume <= 87:
            draw.line((0,2) + (0 ,15), fill=128)
        elif volume <= 93:
            draw.line((0,1) + (0 ,15), fill=128)
        elif volume <= 95:
            draw.line((0,0) + (0 ,15), fill=128)
        else:
            draw.text((6,-1), str(volume), font=font, fill="orange")
            print('volume outside range (else)')
    
    
    if image.im == oldimage:
        print("pass")
    else:
        oldimage == image.im.copy()
        #print("hi")
        matrix.SetImage(image.im.id)
