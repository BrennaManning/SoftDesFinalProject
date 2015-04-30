import pygame
pygame.init

screen = pygame.display.set_mode((100,100))
while True:
	for event in pygame.event.get():
		print event