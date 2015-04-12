#!/usr/bin/python
import csv
import urllib

import time
import ImageDraw
from PIL import Image
import ImageFont
from rgbmatrix import Adafruit_RGBmatrix


matrix = Adafruit_RGBmatrix(32, 1)
image = Image.new("RGB", (1024, 32), (0,0,0))

font = ImageFont.load("10x20.pil")

url  = "http://api.thingspeak.com/channels/15486/feed.csv?key=1X5610SMHNUIF9XL"
response = urllib.urlopen(url)
cr = csv.reader(response)

rows=list(cr)

row1=rows[1]

print float(row1[2])
drawstring =  "Current temp is " + row1[2] +" degrees."
print "Current temp is " + row1[2] +" degrees."

red = (255,0,0)

draw = ImageDraw.Draw(image)

draw.text((0,1), drawstring, font=font, fill=red)

for n in range(32, -image.size[0], -1): # Scroll R to L
            matrix.SetImage(image.im.id, n, 0)
            time.sleep(0.025)
matrix.Clear()



