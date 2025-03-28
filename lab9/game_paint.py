import pygame as pygame

pygame.init()
FPS = 120
FramePerSec = pygame.time.Clock()

#Keys:
# "1" - draw
# "2" - delete
# "w" - +radius
# "s" - -radius
# "r" - red color
# "b" - blue color
# "g" - green color

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
radius = 20
mouse_x = WIDTH/2
mouse_y = HEIGHT/2
color = RED
t_c = "RED"

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
            if event.key == pygame.K_w and radius < 75:
                radius += 5
            if event.key == pygame.K_s and radius > 5:
                radius -= 5

        #change color:
            if event.key == pygame.K_r:
                color = RED
                t_c = "RED"
            if event.key == pygame.K_g:
                color = GREEN
                t_c = "GREEN"
            if event.key == pygame.K_b:
                color = BLUE
                t_c = "BLUE"
                
            if event.key == pygame.K_1:
                draw = True
            if event.key == pygame.K_2:
                draw = False
                
    if draw:
        if trace:
            positions_draw.append((mouse_x,mouse_y,color,radius))
        mode = "Drawing"
    else:
        mode = "Deleting"
        if trace:
            positions_draw.append((mouse_x,mouse_y,WHITE,radius))
    
    for x,y,c,rad in positions_draw:
        pygame.draw.circle(screen,c,(x,y), rad)
    
    
    text1 = font.render("1-Draw", True,BLACK)
    text2 = font.render("2-Remove", True,BLACK)
    textr = font.render("r-Red", True,BLACK)
    textg = font.render("g-Green", True,BLACK)
    textb = font.render("b-Blue", True,BLACK)
    text_rb = font.render("w-Radius+", True,BLACK)
    text_rl = font.render("s-Radius-", True,BLACK)
    text_r_now = font.render(f"Radius: {radius}", True,BLACK)
    text_mode = font.render(f"Mode: {mode}", True,BLACK)
    text_color = font.render(f"{t_c}", True,color)
    
    screen.blit(text1, (10,10))
    screen.blit(text2, (10,30))
    screen.blit(textr, (10,50))
    screen.blit(textg, (10,70))
    screen.blit(textb, (10,90))
    screen.blit(text_rb, (600,10))
    screen.blit(text_rl, (600,30))
    screen.blit(text_r_now, (600,50))
    screen.blit(text_mode, (0, 680))
    screen.blit(text_color,(0,660))
    
    pygame.display.flip()
    pygame.display.update()
    FramePerSec.tick(FPS)
    
    
pygame.quit()