# By Ivan Nesevski and Bilal Majeed on June 2/2013
# This is the main code for the Multiplayer mode of the game
# This is called from the "main.py" file

#IMPORT THE NEEDED MODULES
import pygame, sys, os, classes, highScores
from pygame.locals import *
import random
os.environ['SDL_VIDEODRIVER']='windib' #required for winXP

#CONSTANTS
right, left, up, down = 20, -20, 10, -10
bgColor = 255, 255, 255
scoreColor = 0, 0, 0
timeColor = 0, 0, 0
block_size = 20
size = width, height = 900, 740
scores = []

pygame.mixer.init()
clock = pygame.time.Clock()  #defines the clock for the timer of the game
pauseClock = pygame.time.Clock()
music = pygame.mixer.Sound('music/single_music.ogg')

def game(music_play):
    import gameOver
    
    pygame.init()
    pygame.display.set_caption('Ultimate Snake')
    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

    #trys to get the highScore and saves them, if it cant then it assumes
    #that the highScore is 0
    try:
        highscore = highScores.read()
        scores = highScores.save()
    except:
        highscore = 0
        scores = []

    game = True
     
    while game == True:
        #plays the music if not off
        if music_play != "off":
            music.play(-1)
            
        #defines the bgColor, timeColor, scoreColor
        bgColor = 0, 0, 0
        scoreColor = 255, 255 , 255
        timeColor = 255, 255, 255

        timer = 10000 #sets the time to get the food to 10sec

        count = 1 #count is used to write the scores once
        
        score = classes.Score(screen, highscore)
        snake = classes.Snake(screen)
        food = classes.Food(screen, snake)

        pause = 0
        pCount = 0
        font = pygame.font.SysFont("Helvetica", 25)
        clock.tick()
        
        while True:
            clock.tick()
            pause = 0

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
                #it goes into an infinite loop when "p" is pressed
                if event.type == KEYDOWN:
                    if event.key == K_p:
                        pygame.mixer.pause() #pauses music
                        pCount = 1
                        pauseClock.tick() #ticks the clock for the pauseClock
                        while 1:
                            event = pygame.event.wait()
                            if event.type == KEYDOWN:
                                if event.key == K_p:
                                    pygame.mixer.unpause() #resumes music
                                    break
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                                if event.key == K_ESCAPE:
                                    pygame.quit()
                                    sys.exit()
                        pauseClock.tick() #ticks it again

                # use the arrow keys to move the snake
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        snake.change_direction(right)                    
                    elif event.key == K_LEFT:
                        snake.change_direction(left)
                    elif event.key == K_UP:
                        snake.change_direction(up)
                    elif event.key == K_DOWN:
                        snake.change_direction(down)

            #changes the color to the time text to red when the time
            #left is less than or equal to 3 seconds
            if timer/1000 <= 3:
                timeColor = 255, 0, 0
            else:
                timeColor = 255, 255, 255

            # chnage the bgColor to rainbow colors
            if score.score >= 1000:
                int1 = random.randrange(0, 255)
                int2 = random.randrange(0, 255)
                int3 = random.randrange(0, 255)
                bgColor = int1, int2, int3         

            # if the snake dies
            if not snake.move(food, score):
                scores.append(score.score)
                if score.score > highscore:
                   highscore = score.score
                game = False #stops the game
                break #breaks the loop

            screen.fill(bgColor) #fills the background
            snake.update() #updates the snake
            score.update(scoreColor) #updates the score
            food.update() #updates the food
            
            pause = pauseClock.get_time() #finds how long the game was
                                          #paused for
            
            #if the user does not collect the food after 10sec - GAME OVER
            if pCount == 1:
                timer = (timer - clock.get_time()) + pause
                pCount = 0
            else:
                timer -= clock.get_time()

            #BLITS THE SPEED STATUS OF THE SNAKES
            if food.delay == 80:
                speedPic = pygame.image.load('images/normalSpeed.bmp').convert()
                screen.blit(speedPic, (450, 7))
            elif food.delay == 40:
                speedPic = pygame.image.load('images/fastSpeed.bmp').convert()
                screen.blit(speedPic, (450, 7))
            elif food.delay == 120:
                speedPic = pygame.image.load('images/slowSpeed.bmp').convert()
                screen.blit(speedPic, (450, 7))

            
            #stop this game when the time has gone out
            if timer <= 0:
                scores.append(score.score)
                if score.score > highscore:
                    highscore = score.score
                game = False 
                break
            
            if snake.extend_snake == True:
                timer = 10000
            
            #draws a line that seperates the statusbar from the game
            pygame.draw.line(screen, scoreColor, (0, 40), (1000, 40))

            #defines the time variables
            timeText = font.render("Time:", True, timeColor)
            time = font.render(str(timer/1000), True, timeColor)
            #blits the time text and the time
            screen.blit(timeText, (250, 10))
            screen.blit(time, (310, 10))

            pygame.display.update() #updates the display
            pygame.time.delay(food.delay) #changes the speed of the snakes

        #IF THE GAME HAS ENDED
        while game == False:
            music.stop()
            
            #writes the highScore to the file
            if count == 1:
                highScores.write(scores)
                s = sorted(scores)
                count = 2
                
            #shows the gameOver screen
            gameOver.scoresListSingle(s[::-1], music_play)
            break
            
