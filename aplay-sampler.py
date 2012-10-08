from time import *
import RPi.GPIO as GPIO
import sys
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.IN)
GPIO.setup(8, GPIO.IN)
GPIO.setup(9, GPIO.IN)

print("Sampler Ready.")

while True:
	try:
		if (GPIO.input(7) == True):
			os.system("aplay -f S16_LE /usr/share/sounds/alsa/Front_Center.wav")
		if (GPIO.input(8) == True):
			os.system("aplay -f S16_LE /usr/share/sounds/alsa/Front_Left.wav")
		if (GPIO.input(9) == True):
			os.system("aplay -f S16_LE /usr/share/sounds/alsa/Front_Right.wav")
		sleep(.01)
	except KeyboardInterrupt:
		sys.exit()
