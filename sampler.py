import pygame.mixer
from time import *
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.IN)
GPIO.setup(8, GPIO.IN)
GPIO.setup(9, GPIO.IN)

pygame.mixer.init(48000, -8,1,15000)
pygame.init()

soundA = pygame.mixer.Sound("/usr/share/sounds/KDE-Im-Cant-Connect.ogg")
soundB = pygame.mixer.Sound("/usr/share/sounds/KDE-Im-Message-In.ogg")
soundC = pygame.mixer.Sound("/usr/share/sounds/KDE-Im-Message-Out.ogg")

while True:
	if (GPIO.input(7) == True):
		soundA.play()
	if (GPIO.input(8) == True):
		soundB.play()
	if (GPIO.input(9) == True):
		soundC.play()
	sleep(.01)
