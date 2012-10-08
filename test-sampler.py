import pygame.mixer
from time import *
import sys

pygame.mixer.init(48000, -16, 2, 1024)
pygame.init()

soundA = pygame.mixer.Sound("/usr/share/sounds/alsa/Front_Center.wav")
soundB = pygame.mixer.Sound("/usr/share/sounds/alsa/Front_Left.wav")
soundC = pygame.mixer.Sound("/usr/share/sounds/alsa/Front_Right.wav")

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
