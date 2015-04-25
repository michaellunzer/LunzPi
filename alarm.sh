
mpc clear

mpc volume 20

mpc add spotify:user:michaellunzer:playlist:53WupSpTZzYgLhG5wYPZ6t

mpc play

mpc volume 40

sleep 1

mpc volume 50

sleep 5

mpc status

sleep 1

cd LunzPi
python clock.py




#(///while :; do ASDFdate +%I:%Mp ; sleep 200 ; done) | sudo ./ASDFrpi-rgb-led-matrix/text-example -f ./rpi-rgb-led-matrix/fonts/6x13.bdf -r 16 -c1 -C0,255,255
