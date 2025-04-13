import pygame as pygame
import ctypes
import psycopg2
from random import *
RUN = False
current_level =0

connect = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="vlad19supkbtu",
    host="localhost",
    port="5432" 
)
cursor = connect.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS snake(
    user_name VARCHAR(100),
    user_score INT,
    level INT
    );
    """)
connect.commit()
name = input("Input your nickname: \n")
text_query = "SELECT * FROM snake WHERE user_name=%s"
cursor.execute(text_query, (name,))
checking_on_old = cursor.fetchall()
connect.commit()

if checking_on_old:
    for row in checking_on_old:
        print(f"Your name: {row[0]} | your best score: {row[1]} | your level: {row[2]}")
    play_ch = int(input('''Would you like to start game?
1 - yes, 2 - no\n'''))
    if play_ch == 1:
        RUN = True
    else:
        RUN = False
else:
    query_add = "INSERT INTO snake (user_name, user_score, level) VALUES (%s,%s,%s)"
    cursor.execute(query_add, (name,0,current_level,))
    connect.commit()
    RUN = True
    

    






pygame.init()



WIDTH, HIGHT = 400,400
screen = pygame.display.set_mode((WIDTH,HIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
speed = 15
# Поднимаем окно поверх всех
hwnd = pygame.display.get_wm_info()['window']
ctypes.windll.user32.ShowWindow(hwnd, 5)         # SW_SHOW
ctypes.windll.user32.SetForegroundWindow(hwnd)   # Впереди всех
ctypes.windll.user32.SetFocus(hwnd) 




#TImer
coldown = 10 
start_ticks = pygame.time.get_ticks()
#COLORS
RED = (255,0,0)
WHITE = (255,255,255)
PINK = (237, 124, 247)
BLACK = (0,0,0)


#FOnt
font = pygame.font.Font(None, 40)
font2 = pygame.font.Font(None, 20)

#Score
game_score = 0

#Snake
snake_step = 10
snake = [[100,50],[90,50],[80,50]]
part_body = [100,50]
snake_direction = "RIGHT"
change_to = snake_direction

#Levels
levels = [
    [],
    [[100,200], [110,200], [120,200],[130,200],[140,200]],
    [[100,200], [110,200], [120,200],[130,200],[140,200],[150,200],[150,210],[150,220],[150,230]],
    [[100,200], [110,200], [120,200],[130,200],[140,200],[150,200],[150,210],[150,220],[150,230],[130,190],[130,180],[130,170],[130,160]]
    
]
walls = levels[current_level]

#good apple
while True:
    apple_xy = [randint(5, (WIDTH // 10)) * 10, randint(5, (HIGHT // 10)) * 10]
    bad_ap_xy = [randint(5, (WIDTH // 10)) * 10, randint(5, (HIGHT // 10)) * 10]
    if apple_xy != part_body and bad_ap_xy != part_body :
        apple_exist=True
        bad_ap_exist = True
        break
stop = False
paused = False
while RUN:
    
    #Filling screen into White
    screen.fill(PINK)
    
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
                
            if event.key == pygame.K_p:
                paused = True
                query = "UPDATE snake SET user_score=%s WHERE user_name=%s"
                cursor.execute(query, (game_score,name,))
                query2 = "UPDATE snake SET level=%s WHERE user_name=%s"
                cursor.execute(query2, (current_level,name,))
                connect.commit()
            
            while paused:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        paused = False
                        RUN = False
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                        paused = False  # снять с паузы

                pause_text = font2.render("Press P to continue", True, BLACK)
                screen.blit(pause_text, (150,370))
                pygame.display.update()
                clock.tick(5)
    
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
        pygame.draw.rect(screen,(255, 255, 0), pygame.Rect(p[0], p[1], 10,10))
        
    if game_score < 5:
        current_level = 0 
        walls = levels[current_level]
    elif game_score == 5:
        current_level = 1
        walls = levels[current_level]
    elif game_score == 10:
        current_level = 2
        walls = levels[current_level]
    elif current_level == 15:
        current_level = 3
        walls = levels[current_level]
        
    
    #Drawing walls
    for wall in walls:
        pygame.draw.rect(screen,(82, 82, 82), pygame.Rect(wall[0], wall[1], 10,10))
    
    
        
        
    #Collision 
    if part_body[0] < 0 or part_body[0] >= WIDTH or part_body[1] < 0 or part_body[1] >= HIGHT:
        stop = True
    
    for block in snake[1:]:
        if part_body == block:
            stop = True
            
    for wal_l in walls:
        if part_body == wal_l:
            stop = True
            
            
    #TEXT
    text_score = font.render(f"Score: {game_score}", True, BLACK)
    screen.blit(text_score, (10,10))
    text_level = font.render(f"Level: {current_level}", True, BLACK)
    screen.blit(text_level, (280,10))
    
    
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

query = "UPDATE snake SET user_score=%s WHERE user_name=%s"
cursor.execute(query, (game_score,name,))
query2 = "UPDATE snake SET level=%s WHERE user_name=%s"
cursor.execute(query2, (current_level,name,))


cursor.close()
connect.commit()

