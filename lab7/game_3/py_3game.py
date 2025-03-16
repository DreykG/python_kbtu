import pygame as pygame
from random import *


pygame.init()

WIDTH, HIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HIGHT))
pygame.display.set_caption("Third Game")

WHITE = (255,255,255)
RED = (255, 0 ,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
font = pygame.font.Font(None,36)

x_sphere, y_sphere = (WIDTH//2), (HIGHT//2)
w_sphere, h_sphere = 50, 50
color_sphere = RED
color_berry = BLUE


score = 0
berry_r = 15
berry_exist = False
sphere_r = 25
RUN = True
step = 20
berry_x, berry_y = randint(step+w_sphere, WIDTH-step-w_sphere), randint(step+h_sphere, HIGHT-step-h_sphere)
while RUN:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and y_sphere <= HIGHT - h_sphere - step:
                y_sphere += step
            if event.key == pygame.K_UP and y_sphere >= h_sphere + step:
                y_sphere -= step
            if event.key == pygame.K_RIGHT and x_sphere <= WIDTH - w_sphere - step:
                x_sphere += step
            if event.key == pygame.K_LEFT and x_sphere >=  w_sphere + step:
                x_sphere -= step
        if (x_sphere - 15) <= berry_x <= (x_sphere+15) and (y_sphere - 15) <= berry_y <= (y_sphere+15):
            pygame.draw.circle(screen, WHITE, (berry_x, berry_y), berry_r)
            berry_exist = False
            score += 1
            
    
    
    if berry_exist == False:
        berry_x, berry_y = randint(step+w_sphere, WIDTH-step-w_sphere), randint(step+h_sphere, HIGHT-step-h_sphere)
        berry_exist = True
            
    text_score = font.render(f"Your score: {score}", True, BLACK)
    text_view = text_score.get_rect(center=(100,50))
    screen.blit(text_score, text_view)
    
    pygame.draw.circle(screen, BLUE, (berry_x, berry_y),berry_r)
    pygame.draw.circle(screen, RED, (x_sphere, y_sphere), sphere_r)
    
    pygame.display.flip()
    pygame.display.update()
    
    
    
    
    
pygame.quit()