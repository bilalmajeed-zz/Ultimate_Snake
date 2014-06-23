# By Ivan Nesevski and Bilal Majeed on June 2/2013
# This is the main code for the PLayer and AI mode of the game
# This is called from the "main.py" file

#IMPORT THE NEEDED MODULES
import pygame, sys, os, aiClasses, ai, math
from pygame.locals import *
import random

os.environ['SDL_VIDEODRIVER']='windib' #required for winXP

#CONSTANTS
right, left, up, down = 20, -20, 10, -10
color = 0,0,0
block_size = 20
size = width, height = 1000, 740

pygame.mixer.init()
clock = pygame.time.Clock() #defines the clock for the timer of the game
pauseClock = pygame.time.Clock()
music = pygame.mixer.Sound('music/epic_music.ogg')


def game(music_play):
    import gameOver
    
    pygame.init()
    pygame.display.set_caption('Ultimate Snake')
    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
    game = True
     
    while game == True:
        #plays the music if its not off
        if music_play != "off":
            music.play(-1)
            
        #defines the bgColor, color and the speed of the snake
        bgColor = 0, 0, 0
        color = 255, 255, 255

        snake2 = aiClasses.Snake(screen, 320, 280, "images/green.bmp")
        snake = aiClasses.Snake(screen, 320, 240, "images/part.bmp")

        score2 = aiClasses.Score(screen, True)        
        score = aiClasses.Score(screen)

        food = aiClasses.Food(screen, snake, snake2) 
        food2 = aiClasses.Food(screen, snake, snake2, True)
        snk2Dead = False

        font = pygame.font.SysFont("Helvetica", 25)
        font2 = pygame.font.SysFont("Helvetica", 40)

        came_from = "R"
        came_from2 = ""

        pCount = 0
        clock.tick_busy_loop()
        timer = 180000 #sets the time of the game to 3min
                       #game will end in 3min
        pause = 0
        
        while True:
            clock.tick_busy_loop() 
            pos_xy = [] #defines a list with x,y position of each part
                        #of the snake
            
            #appends the positions to pos_xy
            for each in snake2.parts[3:]:
                pos_xy.append((each.position.x, each.position.y))

            #finds the difference in positions between the AI snake and
            #and the food1 and food2 position
            foodPos = math.fabs(snake2.head.position.x - food.position[0])
            food2Pos = math.fabs(snake2.head.position.x - food2.position[0])

            #decides which food is closer and goes for that food
            if foodPos >= food2Pos:
                goFood = 2
            else:
                goFood = 1
                           
            if snk2Dead == False:
                #tells the AI to move, calls the ai function ai.py
                if goFood == 2:
                    came_from, came_from2= ai.ai(food2, snake2, came_from, came_from2, pos_xy)
                elif goFood == 1:
                    came_from, came_from2= ai.ai(food, snake2, came_from, came_from2, pos_xy)
                                 
            goFood = 0

            #if the escape key is pressed then the game will quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                
                #press 'p' to pause and unpause the game
                #it goes into a infinite loop when "p" is pressed
                if event.type == KEYDOWN:
                    if event.key == K_p:
                        pygame.mixer.pause()
                        pCount = 1
                        pauseClock.tick() #ticks the clock for the pauseClock
                        while 1:
                            event = pygame.event.wait()
                            if event.type == KEYDOWN:
                                if event.key == K_p:
                                    pygame.mixer.unpause()
                                    break
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                                if event.key == K_ESCAPE:
                                    pygame.quit()
                                    sys.exit()
                        pauseClock.tick() #ticks it again

                # use the arrow keys to move the snake
                #THIS IS FOR PLAYER 1
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        snake.change_direction(right)                    
                    elif event.key == K_LEFT:
                        snake.change_direction(left)
                    elif event.key == K_UP:
                        snake.change_direction(up)
                    elif event.key == K_DOWN:
                        snake.change_direction(down)

            # change the bgColor to rainbow colors
            while score.score >= 1000 or score2.score >= 1000: 
                int1 = random.randrange(0, 255)
                int2 = random.randrange(0, 255)
                int3 = random.randrange(0, 255)
                bgColor = int1, int2, int3
                break

            # if the player dies
            if not snake.move(food, food2, score):
                game = False #game ends and goes to the gameOver screen
                break #breaks the game loop

            # if the ai dies
            if not snake2.move(food, food2, score2):
                snk2Dead = True

            screen.fill(bgColor) #fills the background

            pause = pauseClock.get_time() #finds how long the game
                                          #was paused for
            
            if pCount == 1: #works everytime the game is paused
                timer = (timer - clock.get_time()) + pause
                pCount = 0
            else:
                timer -= clock.get_time()

            if timer <= 0: #what happens when the time runs out
                pygame.time.delay(1000)
                game = False
                break
            
            if snk2Dead == False: #when the AI is not dead
                snake2.update() #updates the AI's snake
                food2.update() #updates the food for the AI

            snake.update() #updates the snake for the player
            food.update() #updates the food for the player
            
            score2.update(color) #updates the scores
            score.update(color)           
            
            #BLITS THE SPEED STATUS OF THE SNAKES
            if food.delay == 80:
                speedPic = pygame.image.load('images/normalSpeed.bmp').convert()
                screen.blit(speedPic, (550, 3))

            elif food.delay == 40:
                speedPic = pygame.image.load('images/fastSpeed.bmp').convert()
                screen.blit(speedPic, (550, 5))
                
            elif food.delay == 120:
                speedPic = pygame.image.load('images/slowSpeed.bmp').convert()
                screen.blit(speedPic, (550, 5))
            
            #draws a line that seperates the statusbar from the game
            pygame.draw.line(screen, color, (0, 40), (1000, 40))

            #defines the time variables
            t = (timer/1000)/60.0
            timeText = font.render("Time:", True, color)
            time = font.render(str("%.2f" % t), True, color)
            #blits the time text and the time
            screen.blit(timeText, (250, 10))
            screen.blit(time, (310, 10))
            
            pygame.display.update() #updates the display
            pygame.time.delay(food.delay) #changes the speed of the snakes

        #IF THE GAME HAS ENDED
        while game == False:
            music.stop()
                                      
            #shows the gameOver screen
            gameOver.scoresListMulti(font2, score.score, score2.score, music_play, True)
            pygame.display.update()
