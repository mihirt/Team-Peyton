import pygame

pygame.init()
drum = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/drum_tom_mid_hard.wav")
drum.play()
print("done")
