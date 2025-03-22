import pygame as pygame

pygame.init()
FPS = 120
FramePerSec = pygame.time.Clock()

#Keys:
# "1" - draw
# "2" - delete

#font
font = pygame.font.Font(None,26)

#COLORS
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)


#Screen
WIDTH, HEIGHT = 700,700
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Paint")

#Pencil
radius = 5
mouse_x = WIDTH/2
mouse_y = HEIGHT/2
color = RED

#position
positions_draw = []


trace = False
draw = False
RUN = True
while RUN:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
        
        if event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = pygame.mouse.get_pos()

        
        
        #CHECK on press mouse's keys:
        if event.type == pygame.MOUSEBUTTONDOWN:
            trace = True
            mouse_x, mouse_y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            trace = False
        
            
        #Check on click keyboard's keys:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and radius < 50:
                radius += 5
            if event.key == pygame.K_s and radius > 5:
                radius -= 5

        #change color:
            if event.key == pygame.K_r:
                color = RED
            if event.key == pygame.K_g:
                color = GREEN
            if event.key == pygame.K_b:
                color = BLUE
                
            if event.key == pygame.K_1:
                draw = True
            if event.key == pygame.K_2:
                draw = False
                
    if draw:
        if trace:
            positions_draw.append((mouse_x,mouse_y,color))
    else:
        if trace:
            positions_draw.append((mouse_x,mouse_y,WHITE))
    
    for x,y,c in positions_draw:
        pygame.draw.circle(screen,c,(x,y), radius)
    
    
    text1 = font.render("1-draw", True,BLACK)
    text2 = font.render("2-remove", True,BLACK)
    textr = font.render("r-red", True,BLACK)
    textg = font.render("g-green", True,BLACK)
    textb = font.render("b-blue", True,BLACK)
    text_rb = font.render("w-radius+", True,BLACK)
    text_rl = font.render("s-radius-", True,BLACK)
    
    screen.blit(text1, (10,10))
    screen.blit(text2, (10,30))
    screen.blit(textr, (10,50))
    screen.blit(textg, (10,70))
    screen.blit(textb, (10,90))
    screen.blit(text_rb, (600,10))
    screen.blit(text_rl, (600,30))
    
    pygame.display.flip()
    pygame.display.update()
    FramePerSec.tick(FPS)
    
    
pygame.quit()