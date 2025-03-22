from random import *
import pygame, sys
from pygame.locals import *
import random

pygame.init()
FPS = 60
FramePerSec = pygame.time.Clock()

#Screen
WIDTH, HIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HIGHT))
background = pygame.image.load(r"lab8\game_1f\road.jpg")
background = pygame.transform.scale(background, (WIDTH,HIGHT))
pygame.display.set_caption("Race")

#Font
font = pygame.font.Font(None, 36)

#Face
face_w, face_h = 150,200
face = pygame.image.load(r"lab8\game_1f\face.png")
face = pygame.transform.scale(face,(face_w,face_h))
step_face = 10
face_x = 350
face_y = 600

#GEM
gem_w,gem_h = 100,100
gem = pygame.image.load(r"lab8\game_1f\gem.png")
gem = pygame.transform.scale(gem, (gem_w,gem_h))
step_gem = 10
gem_exist = False
score = 0


#Fall object
object_w, object_h = 150,150
object = pygame.image.load(r"lab8\game_1f\rock.png")
object = pygame.transform.scale(object, (object_w,object_h))
step_object = 10
object_exist = False

#Function reset game
def reset_game():
    global object_spawn_x,object_spawn_y
    object_spawn_x,object_spawn_y = randint(20, WIDTH-20), -10
    object_exist = True


RUN = True
while RUN:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
    #Checking Pressing       
    keys = pygame.key.get_pressed()
    if pygame.key.get_pressed()[K_LEFT] and face_x > (step_face):
            face_x = face_x - step_face
    if pygame.key.get_pressed()[K_RIGHT] and face_x < (WIDTH-(step_face+face_w)):
            face_x = face_x + step_face
            
    #Generatex xy for objects(rock)  
    if object_exist == False:
        object_spawn_x,object_spawn_y = randint(20, WIDTH-object_w), -10
        object_exist = True
    #Generatex xy for gems and falling gems  
    if gem_exist == False:
        gem_xy = [randint(20, WIDTH-object_w), -10]
        gem_exist = True
    if gem_exist:
        gem_xy[1] += 10
        if gem_xy[1] == HIGHT:
            gem_exist = False
    #Gfalling rocks
    if object_exist == True:
        object_spawn_y += step_object
        if object_spawn_y == HIGHT:
            object_exist = False
    
    #Filling of screen and imaging of face,rocks and gems
    screen.blit(background, (0,0))
    screen.blit(face,(face_x,face_y))
    screen.blit(gem,(gem_xy))
    screen.blit(object,(object_spawn_x,object_spawn_y))

    
    #Checking on collision
    if (object_spawn_y == face_y-(face_h//2) + (face_h//2)//2) and (face_x - face_h//2 <object_spawn_x < face_x+face_h//2):
        print("STOLKNOVENIE")
        screen.fill((255,0,0))
        text_game_over = font.render("GAME OVER",True,(255,255,255))
        screen.blit(text_game_over,(350,400))
        score = 0
        pygame.display.flip()
        pygame.time.wait(3000)
        reset_game()
    #Adding score
    if (gem_xy[1] == face_y + (face_h//2)//2) and (face_x - face_h//2 <gem_xy[0] < face_x+face_h//2):
        gem_exist = False
        score += 5

    
    
    #Texting "score"       
    text_score = font.render(f"Score: {score}", True, (255,255,255))
    screen.blit(text_score, (50,50))
    pygame.display.flip()
    pygame.display.update()
    FramePerSec.tick(FPS)
    
pygame.quit()
        
    
            