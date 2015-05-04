#!/bin/bash

sudo apt-get update -y
sudo apt-get install netatalk python-dev python-imaging -y
sudo apt-get install git -y
sudo apt-get install build-essential -y
sudo apt-get install gcc -y
git clone https://github.com/michaellunzer/LunzPi
pip install pywapi
cd
git clone https://github.com/adafruit/rpi-rgb-led-matrix
cd rpi-rgb-led-matrix
make
cd ..