# By Ivan Nesevski and Bilal Majeed on June 2/2013
# This is the main code for the Multiplayer mode of the game
# This is called from the "main.py" file

#IMPORT THE NEEDED MODULES
import pygame, sys, os, multiClasses
from pygame.locals import *
import random

os.environ['SDL_VIDEODRIVER']='windib' #required for winXP

#CONSTANTS
right, left, up, down = 20, -20, 10, -10
bgColor = 0, 0, 0
color = 255, 255, 255
block_size = 20
size = width, height = 500, 740
winSize = w, h = 1000, 740

pygame.mixer.init()
clock = pygame.time.Clock() #defines the clock for the timer of the game
pauseClock = pygame.time.Clock()
music = pygame.mixer.Sound('music/epic_music.ogg')

def game(music_play):
    import gameOver
    
    pygame.init()
    pygame.display.set_caption('Ultimate Snake')
    screen = pygame.display.set_mode(winSize, pygame.FULLSCREEN)
    game = True
     
    while game == True:
        #plays the music if not off
        if music_play != "off":
            music.play(-1)
            
        #defines the bgColor, color and the speed of the snake
        bgColor = 0, 0, 0
        color = 255, 255, 255
        count = 0
        delay = 80
        
        dieCount = 0
        font = pygame.font.SysFont("Helvetica", 25)
        
        score = multiClasses.Score(screen)
        snake = multiClasses.Snake(screen, 320, 340, 'images/part.bmp', False)
        food = multiClasses.Food(screen, snake)
        snake1dead = False
        snk1deathCount = 0

        score2 = multiClasses.Score(screen, True)
        snake2 = multiClasses.Snake(screen, 820, 340, 'images/green.bmp', True)
        food2 = multiClasses.Food(screen, snake2, True)
        snake2dead = False
        snk2deathCount = 0

        pCount = 0
        clock.tick_busy_loop()
        timer = 180000 #sets the time of the game to 3min
                       #game will end in 3min
        pause = 0
        
        while True:
            clock.tick_busy_loop()
            pause = 0

            #if the escape key is pressed then the game will quit
            for event in  pygame.event.get():
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
                        snake2.change_direction(right)                    
                    elif event.key == K_LEFT:
                        snake2.change_direction(left)
                    elif event.key == K_UP:
                        snake2.change_direction(up)
                    elif event.key == K_DOWN:
                        snake2.change_direction(down)

                # use the arrow keys to move the snake
                #THIS is FOR PLAYER 2
                if event.type == KEYDOWN:
                    if event.key == K_d:
                        snake.change_direction(right)                    
                    elif event.key == K_a:
                        snake.change_direction(left)
                    elif event.key == K_w:
                        snake.change_direction(up)
                    elif event.key == K_s:
                        snake.change_direction(down)

            # change the bgColor to rainbow colors
            if score.score >= 1000 or score2.score >= 1000:
                int1 = random.randrange(0, 255)
                int2 = random.randrange(0, 255)
                int3 = random.randrange(0, 255)
                bgColor = int1, int2, int3
                
            # if snake1 dies
            if not snake.move(food, score):
                snake1dead = True
                if snk1deathCount == 0:
                    dieCount += 1
                    snk1deathCount = 1

            # if snake2 dies
            if not snake2.move(food2, score2):
                snake2dead = True
                if snk2deathCount == 0:
                    dieCount += 1
                    snk2deathCount = 1

            #if both the snakes are dead
            if dieCount == 2:
                pygame.time.delay(1000)
                game = False #stops the game
                break #breaks the loop

            screen.fill(bgColor) #fills the background
            
            pause = pauseClock.get_time() #finds how long the game
                                          #was paused for
            if pCount == 1: #works everytime the game is paused
                timer = (timer - clock.get_time()) + pause
                pCount = 0
            else:
                timer -= clock.get_time()

            if timer <= 0:
                dieCount = 2
            
            if snake1dead == False: #when Player1 is not dead
                snake.update()
                food.update()
            else: #if player one is dead
                snkdeadText = font.render("Player 1 has killed itself", True, color)
                snkdeadText2 = font.render("The game will end after Player 2 is dead", True, color)
                screen.blit(snkdeadText, (100,240))
                screen.blit(snkdeadText2, (100,280))
                delay = food2.delay

            if snake2dead == False: #when Player2 is not dead
                snake2.update()
                food2.update()
            else: #if Player2 is dead
                snkdeadText = font.render("Player 2 has killed itself", True, color)
                snkdeadText2 = font.render("The game will end after Player 1 is dead", True, color)
                screen.blit(snkdeadText, (600,240))
                screen.blit(snkdeadText2, (600,280))
                delay = food.delay

            #updates the score for the snakes
            score.update(color)           
            score2.update(color)      

            #FIGURES OUT WHICH FOOD.DELAY TO FOLLOW
            #by the means of a alogrithim
            foodDelay = food.delay + food2.delay
            if snake1dead == False and snake2dead == False:
                if foodDelay == 120:
                    delay = 40
                elif foodDelay == 80:
                    delay = 40
                elif foodDelay == 160:
                    delay = 80
                elif foodDelay == 200:
                    delay = 120
                        
            #BLITS THE SPEED STATUS OF THE SNAKES
            if delay == 80:
                speedPic = pygame.image.load('images/normalSpeed.bmp').convert()          
                screen.blit(speedPic, (550, 3))
                
            elif delay == 40:
                speedPic = pygame.image.load('images/fastSpeed.bmp').convert()                
                screen.blit(speedPic, (550, 5))
                
            elif delay == 120:
                speedPic = pygame.image.load('images/slowSpeed.bmp').convert()
                screen.blit(speedPic, (550, 5))
    
            #draws a line that seperates the statusbar from the game
            pygame.draw.line(screen, color, (500, 40), (500,740))
            #draws a line that splits the screen into two peieces
            pygame.draw.line(screen, color, (0, 40), (1000, 40))

            #defines the time variables
            t = (timer/1000)/60.0
            timeText = font.render("Time:", True, color)
            time = font.render(str("%.2f" % t), True, color)
            #blits the time text and the time
            screen.blit(timeText, (250, 10))
            screen.blit(time, (310, 10))
            
            pygame.display.update() #updates the display
            pygame.time.delay(delay) #changes the speed of the snakes            

        #IF THE GAME HAS ENDED
        while game == False:                     
            music.stop()
            #shows the gameOver screen 
            gameOver.scoresListMulti(font, score.score, score2.score, music_play)
            pygame.display.update()

