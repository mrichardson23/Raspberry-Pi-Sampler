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
	inputValue7 = GPIO.input(7)
	inputValue8 = GPIO.input(8)
	inputValue9 = GPIO.input(9)
	if (inputValue7 == True):
		soundA.play()
	if (inputValue8 == True):
		soundB.play()
	if (inputValue9 == True):
		soundC.play()
	sleep(.01)
