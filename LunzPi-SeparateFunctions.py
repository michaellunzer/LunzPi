#!/usr/bin/python
import csv
import urllib

import os
import pywapi
import string

import sys
import subprocess

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

white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
lightblue = (0,221,237)
    

count = 0


def LunzPiClock():
            
    while (count < 100):   
        image = Image.new("RGB", (32, 16), (black))
        draw = ImageDraw.Draw(image)


        drawstring1 = time.strftime("%I:%M") 
        drawstring2 = time.strftime("%p")
    #Clock Area:
        draw.text((-1,0), drawstring1, font=font, fill="blue")
        draw.text((19,6), drawstring2, font=font, fill=red)
        matrix.SetImage(image.im.id)
        time.sleep(1)
        print( os.system("date"))
        #print("it worked!")


LunzPiClock()


"""
while (count < 100):
   

    
    #"Current temp is " + gettemp(url)  +" degrees."
    
    #for n in range(32, -image.size[0], -1): # Scroll R to L
    #matrix.SetImage(image.im.id) #, n, 0)
    #time.sleep(5)
    #matrix.Clear()
    #time.sleep(2)

#Weather Area:

    yahoo_result = pywapi.get_weather_from_yahoo('97210', 'imperial')
    
    #print "Yahoo says: It is " + string.lower(yahoo_result['condition']['text']) + " and " + yahoo_result['condition']['temp'] + "F now in Portland.\n\n"
    
    print os.system("top")
    
    #count +=1
    #print count
    
    weather_condition = string.lower(yahoo_result['condition']['text']) 
    
    weather_temp = yahoo_result['condition']['temp']
    
    #print weather_temp
    
    if weather_temp >= "70":
        draw.text((-1,-3), weather_temp, font=font, fill="red")
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
        draw.line((30,3) + (30 ,15), fill="blue")
        draw.line((28,3) + (28 ,15), fill=lightblue)
        draw.line((23,3) + (23 ,15), fill="blue")
        draw.line((18,3) + (18 ,8), fill=lightblue)
        draw.line((26,3) + (26 ,15), fill="blue")
        draw.line((21,3) + (21 ,15), fill=lightblue)
        
    elif weather_condition == "rain":
        draw.ellipse((28, 0) +(32, 4), fill="grey")
        draw.ellipse((23, 0) +(27, 4), fill="white")
        draw.ellipse((18, 0) +(22, 4), fill="grey")
        draw.line((30,3) + (30 ,15), fill="blue")
        draw.line((28,3) + (28 ,15), fill="blue")
        draw.line((23,3) + (23 ,15), fill="blue")
        draw.line((18,3) + (18 ,8), fill="blue")
        draw.line((26,3) + (26 ,15), fill="blue")
        draw.line((21,3) + (21 ,15), fill="blue")    
        
    elif weather_condition == "fair":
        draw.ellipse((28, 0) +(32, 4), fill="grey")
        draw.ellipse((21, 0) +(25, 4), fill="grey")
        draw.ellipse((16, 0) +(20, 4), fill="grey")
        
        
        
    else:
        draw.line((0, 0) + image.size, fill=128)
        draw.line((0, image.size[1], image.size[0], 0), fill=128)



#MPC Volume Area:

   # def get_mpc_status():
    #    mpc_status = os.getenv(mpc_status, os.system("mpc status"))
        #mpc_status2 = str(mpc_status)
     #   print mpc_status
       # return "mpc_status[7:10]: ", mpc_status[7:10]
    
    #get_mpc_status()

   # def display_volume():  
    volume = subprocess.check_output("mpc status | grep volume", shell=True, stderr=subprocess.STDOUT)  
    volume = volume[7:volume.find("%")]
   # print volume
            
    if volume < "6.25":
        draw.line((0,15) + (0 ,15), fill=128)
    
    else:
        draw.text((6,-1), volume, font=font, fill="red")
    

    matrix.SetImage(image.im.id)

"""
