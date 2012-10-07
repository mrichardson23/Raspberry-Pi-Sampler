import pygame.mixer
from time import *
import RPi.GPIO as GPIO
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.IN)
GPIO.setup(8, GPIO.IN)
GPIO.setup(9, GPIO.IN)

pygame.mixer.init(48000, -8,2,15000)
pygame.init()

soundA = pygame.mixer.Sound("/usr/share/sounds/KDE-Im-Cant-Connect.ogg")
soundB = pygame.mixer.Sound("/usr/share/sounds/KDE-Im-Message-In.ogg")
soundC = pygame.mixer.Sound("/usr/share/sounds/KDE-Im-Message-Out.ogg")

print "Sampler Ready."

while True:
	try:
		if (GPIO.input(7) == True):
			soundA.play()
			sleep(soundA.get_length())
			soundA.stop()
		if (GPIO.input(8) == True):
			soundB.play()
			sleep(soundB.get_length())
			soundB.stop()
		if (GPIO.input(9) == True):
			soundC.play()
			sleep(soundC.get_length())
			soundC.stop()
		sleep(.01)
	except KeyboardInterrupt:
		sys.exit()
