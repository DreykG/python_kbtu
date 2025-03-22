import pygame as pygame
from random import *

pygame.init()

WIDTH, HIGHT = 400,400
screen = pygame.display.set_mode((WIDTH,HIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
speed = 15


#TImer
coldown = 10 
start_ticks = pygame.time.get_ticks()
#COLORS
RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)


#FOnt
font = pygame.font.Font(None, 40)

#Score
game_score = 0

#Snake
snake_step = 10
snake = [[100,50],[90,50],[80,50]]
part_body = [100,50]
snake_direction = "RIGHT"
change_to = snake_direction

#good apple
while True:
    apple_xy = [randint(5, (WIDTH // 10)) * 10, randint(5, (HIGHT // 10)) * 10]
    bad_ap_xy = [randint(5, (WIDTH // 10)) * 10, randint(5, (HIGHT // 10)) * 10]
    if apple_xy != part_body and bad_ap_xy != part_body :
        apple_exist=True
        bad_ap_exist = True
        break
RUN = True
stop = False
while RUN:
    #Filling screen into White
    screen.fill(WHITE)
    
    #All possible Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                change_to = "RIGHT"
            if event.key == pygame.K_UP and snake_direction != "DOWN":
                change_to = "UP"
            if event.key == pygame.K_DOWN and snake_direction != "UP":
                change_to = "DOWN"
    
    #Checking direction 
    snake_direction = change_to
    if snake_direction == "LEFT":
        part_body[0] -= snake_step
    if snake_direction == "RIGHT":
        part_body[0] += snake_step
    if snake_direction == "UP":
        part_body[1] -= snake_step
    if snake_direction == "DOWN":
        part_body[1] += snake_step

    
    #Adding new part body of snake
    snake.insert(0, list(part_body))
        
    #Checking on eat apples        
    if part_body == apple_xy:
        apple_exist = False
        bad_ap_exist = False
        game_score += 1
        speed = 15
    else:
        snake.pop()
        
    if part_body == bad_ap_xy:
        bad_ap_exist = False
        apple_exist = False
        game_score -= 1
        speed = 40
        
        
    
    #Spawn applesm if they dont exist
    if apple_exist == False:
        while True:
            apple_xy = [randint(5, (WIDTH // 10)) * 10, randint(5, (HIGHT // 10)) * 10]
            if apple_xy != part_body:
                apple_exist=True
                break
    #Drawing apples
    pygame.draw.rect(screen, RED, pygame.Rect(apple_xy[0], apple_xy[1], 10, 10))
    
    
    #Spawn bad apples:
    if bad_ap_exist == False:
        bad_ap_xy = [randint(5, (WIDTH // 10)) * 10, randint(5, (HIGHT // 10)) * 10]
        while True:
            bad_app_xy = [randint(5, (WIDTH // 10)) * 10, randint(5, (HIGHT // 10)) * 10]
            if bad_ap_xy != part_body:
                bad_ap_exist=True
                break
        
    pygame.draw.rect(screen, BLACK, pygame.Rect(bad_ap_xy[0], bad_ap_xy[1], 10, 10))
    
    
    #Drawing of snake body
    for p in snake:
        pygame.draw.rect(screen,(100,100,100), pygame.Rect(p[0], p[1], 10,10))
    
    #Collision 
    if part_body[0] < 0 or part_body[0] >= WIDTH or part_body[1] < 0 or part_body[1] >= HIGHT:
        stop = True
    
    for block in snake[1:]:
        if part_body == block:
            stop = True
    #TEXT
    text_score = font.render(f"Score: {game_score}", True, BLACK)
    screen.blit(text_score, (10,10))
    
    
    text_over = font.render("GAME OVER", True, BLACK)
    if stop:
        screen.fill(RED)
        screen.blit(text_over,(WIDTH//4,HIGHT//2))
        pygame.display.flip()
        pygame.time.wait(1000)
        RUN = False
    
    pygame.display.flip()
    clock.tick(speed)
    pygame.display.update()
    
pygame.quit()