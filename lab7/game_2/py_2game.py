import pygame as pygame
import os
import re 

pygame.init()

WIDTH, HEIGHT = 800, 800 
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Second game")

WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
font = pygame.font.Font(None,36)

display = pygame.Rect(100,100,400,100)
play_button = pygame.Rect(330,305,150,60)
stop_button = pygame.Rect(330,376,150,60)
previus_button = pygame.Rect(130,343,150,60)
next_button = pygame.Rect(530,343,150,60)

music_folder = r"lab7\game_2"

playlist = [os.path.join(music_folder, f) for f in os.listdir(music_folder) if f.endswith('.mp3')]
current_track = 0

# Initialization Pygame
pygame.mixer.init()

# Load and play music
def play_track(index):
    pygame.mixer.music.load(playlist[index])
    pygame.mixer.music.play()

# Next music
def next_track():
    global current_track
    current_track = (current_track + 1) % len(playlist)
    play_track(current_track)

# Previous music
def previous_track():
    global current_track
    current_track = (current_track - 1) % len(playlist)
    play_track(current_track)
RUNNING = True
play_track(0)
while RUNNING:
    
    screen.fill(WHITE)
    
    #Just display
    pygame.draw.rect(screen, (133, 153, 133), pygame.Rect(100, 100, 600, 400))
    pygame.draw.rect(screen, (89,89,89), pygame.Rect(110, 110, 580, 380))
    
    
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(327,303,156,66))
    text_p = font.render("play", True, WHITE)
    text_rect_p = text_p.get_rect(center=play_button.center)
    pygame.draw.rect(screen, (171, 171, 171), play_button)
    screen.blit(text_p, text_rect_p)
    
    
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(327,373,156,66))
    text_s = font.render("stop", True, WHITE)
    text_rect_s = text_s.get_rect(center=stop_button.center)
    pygame.draw.rect(screen, (171, 171, 171), stop_button)
    screen.blit(text_s, text_rect_s)
    
    
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(127,340,156,66))
    text_pr = font.render("previus", True, WHITE)
    text_rect_pr = text_pr.get_rect(center=previus_button.center)
    pygame.draw.rect(screen, (171, 171, 171), previus_button)
    screen.blit(text_pr, text_rect_pr)
    
    
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(527,340,156,66))
    text_n = font.render("next", True, WHITE)
    text_rect_n = text_n.get_rect(center=next_button.center)
    pygame.draw.rect(screen, (171, 171, 171), next_button)
    screen.blit(text_n, text_rect_n)
    
    
    name_sound = playlist[current_track]
    s = name_sound.replace("lab7\game_2\\", "")
    s1 = s.replace(".mp3", "")
    text_sound = font.render(s1, True, WHITE)
    screen.blit(text_sound, (336, 230))
    
    
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if previus_button.collidepoint(event.pos):
                previous_track()
            if next_button.collidepoint(event.pos):
                next_track()
            if stop_button.collidepoint(event.pos):
                pygame.mixer.music.pause()
            if play_button.collidepoint(event.pos):
                pygame.mixer.music.unpause()
                
    
    

    pygame.display.flip()
    
pygame.quit()