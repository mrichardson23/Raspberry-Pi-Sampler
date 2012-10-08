import pygame.mixer
from time import *
import RPi.GPIO as GPIO
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.IN)
GPIO.setup(8, GPIO.IN)
GPIO.setup(9, GPIO.IN)

pygame.mixer.init(48000, -16, 1, 1024)
pygame.init()

soundA = pygame.mixer.Sound("/usr/share/sounds/alsa/Front_Center.wav")
soundB = pygame.mixer.Sound("/usr/share/sounds/alsa/Front_Left.wav")
soundC = pygame.mixer.Sound("/usr/share/sounds/alsa/Front_Right.wav")

soundChannel = pygame.mixer.Channel(1)

print "Sampler Ready."
while True:
	try:
		if (GPIO.input(7) == True):
			soundChannel.play(soundA)
			sleep(soundA.get_length())
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
