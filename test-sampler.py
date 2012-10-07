import pygame.mixer
from time import *
import sys

pygame.mixer.init(48000, -8,2,15000)
pygame.init()

soundA = pygame.mixer.Sound("/usr/share/sounds/KDE-Im-Cant-Connect.ogg")
soundB = pygame.mixer.Sound("/usr/share/sounds/KDE-Im-Message-In.ogg")
soundC = pygame.mixer.Sound("/usr/share/sounds/KDE-Im-Message-Out.ogg")

print "Sampler Ready."

count = 0

while True:
	try:
		soundA.play()
		sleep(soundA.get_length())
		soundA.stop()
		count = count + 1
		print "playing:", count
	except KeyboardInterrupt:
		sys.exit()
