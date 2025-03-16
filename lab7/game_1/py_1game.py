import pygame as pygame
from datetime import * 
import datetime
import math

pygame.init()

WIDTH, HEIGHT = 900, 800 
screen = pygame.display.set_mode((WIDTH,HEIGHT))
background = pygame.image.load(r"lab7\game_1\clock.png")
background = pygame.transform.scale(background, (WIDTH,HEIGHT))
pygame.display.set_caption("First game")

ar_min = pygame.image.load(r"lab7\game_1\min_hand.png")
ar_min = pygame.transform.scale(ar_min, (100,400))

ar_sec = pygame.image.load(r"lab7\game_1\sec_hand.png")
ar_sec = pygame.transform.scale(ar_sec, (100,400))

Center = (WIDTH//2, HEIGHT//2)

RUN = True
while RUN:
    screen.blit(background,(0,0))
    
    now = datetime.datetime.now()
    minutes, seconds = now.minute, now.second
    sec_angle = -6 * seconds
    min_angle = -6 * minutes
    
    def rotate_and_blit(image,angle,center):
        rotated_image = pygame.transform.rotate(image,angle)
        rect = rotated_image.get_rect(center=center)
        screen.blit(rotated_image,rect.topleft)
    
    rotate_and_blit(ar_min,min_angle,Center)
    rotate_and_blit(ar_sec, sec_angle,Center)
    pygame.display.flip()
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
            
    pygame.time.delay(1000)
pygame.quit()