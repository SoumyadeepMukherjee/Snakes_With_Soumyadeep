#Importing modules
import pygame
import random
import os

#Initialising
pygame.mixer.init()
pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
home = (255, 125, 89)
bg1 = (131, 255, 115)
bg2 = (125, 242, 255)

# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("Snakes_With_Soumyadeep")
pygame.display.update()

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_screen(text,color,x,y):
    screen_text = font.render(text, True , color)
    gameWindow.blit(screen_text, [x,y])
    
def plot_snake(gameWindow, color, snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])
    
#Welcome Screen
def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(home)
        text_screen("Welcome to Snakes",black, 260,250)
        text_screen("Press Enter to Play!",black,230,290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gameLoop()
                
        pygame.display.update()
        clock.tick(60)

# Game Loop
def gameLoop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snk_list=[]
    snk_length=1
    velocity_x=0
    velocity_y=0
    init_velocity = 5
    snake_size = 20
    score =0
    fps = 60
    #Check if hiscore file exists
    if (not os.path.exists("hiscore.txt")):
        with open("hiscore.txt", "w") as f:
            f.write("0")
    
    with open("hiscore.txt","r") as f:
        hiscore = f.read()
    
    food_x = random.randint(0, screen_width)
    food_y = random.randint(0, screen_height)
    
    while not exit_game:
        if game_over or exit_game:
            with open("hiscore.txt","w") as f:
                f.write(str(hiscore))
            gameWindow.fill(bg2)
            text_screen("Game Over! Press Enter to Play Again",red,100,250)
            text_screen("Your Score: "+str(score),red,250,300)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
                
        else:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                        
                    if event.key == pygame.K_q:
                        score+=10

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:
                score+=10
                food_x = random.randint(20, screen_width/2)
                food_y = random.randint(20, screen_height/2)
                snk_length+=3
                if score>int(hiscore):
                    hiscore=score

            gameWindow.fill(bg1)
            text_screen("Score: " + str(score) + "  High Score:"+ str(hiscore) , red,5,5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
            
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            
            if len(snk_list)>snk_length:
                del snk_list[0]
            
            if head in snk_list[:-1]:
                game_over=True
                
                
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over=True
            plot_snake(gameWindow, black ,snk_list, snake_size)
            
        pygame.display.update()
        clock.tick(fps)


    pygame.quit()
    quit()

welcome()
