import pygame.mixer
from time import sleep
import RPi.GPIO as GPIO
from sys import exit

GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.IN)
GPIO.setup(8, GPIO.IN)
GPIO.setup(9, GPIO.IN)

pygame.mixer.init(48000, -16, 1, 1024)

soundA = pygame.mixer.Sound("/usr/share/sounds/alsa/Front_Center.wav")
soundB = pygame.mixer.Sound("/usr/share/sounds/alsa/Front_Left.wav")
soundC = pygame.mixer.Sound("/usr/share/sounds/alsa/Front_Right.wav")

soundChannelA = pygame.mixer.Channel(1)
soundChannelB = pygame.mixer.Channel(2)
soundChannelC = pygame.mixer.Channel(3)

print "Sampler Ready."

while True:
	try:
		if (GPIO.input(7) == True):
			soundChannelA.play(soundA)
		if (GPIO.input(8) == True):
			soundChannelB.play(soundB)
		if (GPIO.input(9) == True):
			soundChannelC.play(soundC)
		sleep(.01)
	except KeyboardInterrupt:
		exit()
