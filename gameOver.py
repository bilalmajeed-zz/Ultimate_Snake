# By Bilal Majeed and Ivan Nesevski on June 2/2013
# These are the classes for the AI for the snake game, this file
# is called from multiai.py, multiPlayer.py, singlePlayer.py

#IMPORT THE NEEDED MODULES
import pygame, sys, os
from pygame.locals import *

os.environ['SDL_VIDEODRIVER']='windib' #required for winXP

#CONSTANTS
white = 255, 255, 255
blue = 0, 0, 255
black = 0, 0, 0
size = width, height = 900, 740

def scoresListSingle(scores, music_play):
    import menu, singlePlayer
    
    """ shows the top 5 highscores of all time
        and also shows buttons to play again, quit, and return to menu.
        THIS IS FOR THE SINGLEPLAYER MODE """
    
    font2 = pygame.font.SysFont('Helvetica', 25) #defines the font
    
    sListText1 = font2.render("1:", True, white) #1st place
    sList1 = font2.render(str(scores[0]), True, white)

    sListText2 = font2.render("2:", True, white) #2nd place
    sList2 = font2.render(str(scores[1]), True, white)

    sListText3 = font2.render("3:", True, white) #3rd place
    sList3 = font2.render(str(scores[2]), True, white)

    sListText4 = font2.render("4:", True, white) #4th place
    sList4 = font2.render(str(scores[3]), True, white)

    sListText5 = font2.render("5:", True, white) #5th place
    sList5 = font2.render(str(scores[4]), True, white)

    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption('Ultimate Snake')
    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
    sel_sound = pygame.mixer.Sound('music/menu_select.ogg')
    click_sound = pygame.mixer.Sound('music/menu_button.ogg')     
    y = 370
    game_over = True
    
    #loads the buttons (play again, return to menu, and quit)
    again = pygame.image.load("images/menu_again.bmp").convert()
    back_menu = pygame.image.load("images/menu_menu.bmp").convert()
    quit_game = pygame.image.load("images/menu_q.bmp").convert()
    again_select = pygame.image.load("images/menu_again_sel.bmp").convert()
    menu_select = pygame.image.load("images/menu_menu_sel.bmp").convert()
    quit_select = pygame.image.load("images/menu_q_sel.bmp").convert()
    over = pygame.image.load("images/gameover_single.bmp").convert() 
    
    while game_over == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                    
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    
            if event.type == KEYUP:
                if event.key == K_DOWN:
                    if y != 570:
                        sel_sound.play()
                        y += 100
                        
                elif event.key == K_UP:
                    if y != 370:
                        sel_sound.play()
                        y += -100

                elif event.key == K_RETURN:
                    if y == 370:
                        click_sound.play()
                        singlePlayer.game(music_play)
                        game_over = False

                    elif y == 470:
                        click_sound.play()
                        menu.menu()
                        game_over = False

                    elif y == 570:
                        click_sound.play()
                        pygame.quit()
                        sys.exit()

        screen.blit(over, (0, 0))

        #blits all the scores
        screen.blit(sListText1, (180, 370))
        screen.blit(sList1, (230, 370))
        screen.blit(sListText2, (180, 420))
        screen.blit(sList2, (230, 420))
        screen.blit(sListText3, (180, 470))
        screen.blit(sList3, (230, 470))
        screen.blit(sListText4, (180, 520))
        screen.blit(sList4, (230, 520))
        screen.blit(sListText5, (180, 570))
        screen.blit(sList5, (230, 570))

        #blits the buttons
        if y == 370:
            screen.blit(again_select, (400, 370))
            screen.blit(back_menu, (400, 470))
            screen.blit(quit_game, (400, 570))
        elif y == 470:
            screen.blit(again, (400, 370))
            screen.blit(menu_select, (400, 470))
            screen.blit(quit_game, (400, 570))
        elif y == 570:
            screen.blit(again, (400, 370))
            screen.blit(back_menu, (400, 470))
            screen.blit(quit_select, (400, 570))
            
        pygame.display.update()

def scoresListMulti(font, score1, score2, music_play, ai = False):
    import menu, multiPlayer, multiai
    """ shows the top 5 highscores of all time
        and also shows buttons to play again, quit, and return to menu.
        THIS IS FOR THE SNAKE WARS MODE """

    #shows the neccessary text if the Player 1 or PLayer 2 has won
    if score1 > score2:

        if ai:
            whoWonText = font.render("Player won with "+str(score1)+" points", True, white)
            whoWonText2 = font.render("Computer lost with "+str(score2)+" points", True, white)
        else:
            whoWonText = font.render("Player 1 won with "+str(score1)+" points", True, white)
            whoWonText2 = font.render("Player 2 lost with "+str(score2)+" points", True, white)

    elif score2 > score1:
        if ai:
            whoWonText = font.render("Computer won with "+str(score2)+" points", True, white)
            whoWonText2 = font.render("Player lost with "+str(score1)+" points", True, white)
        else:
            whoWonText = font.render("Player 2 won with "+str(score2)+" points", True, white)
            whoWonText2 = font.render("Player 1 lost with "+str(score1)+" points", True, white)
        

    else:
        whoWonText = font.render("It was a tie with "+str(score1)+" points", True, white)        
        whoWonText2 = font.render("", True, white)
            
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption('Ultimate Snake')
    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
    sel_sound = pygame.mixer.Sound('music/menu_select.ogg')
    click_sound = pygame.mixer.Sound('music/menu_button.ogg')     
    y = 370
    game_over = True
    
    #loads the buttons (play again, return to menu, and quit)
    again = pygame.image.load("images/menu_again.bmp").convert()
    back_menu = pygame.image.load("images/menu_menu.bmp").convert()
    quit_game = pygame.image.load("images/menu_q.bmp").convert()
    again_select = pygame.image.load("images/menu_again_sel.bmp").convert()
    menu_select = pygame.image.load("images/menu_menu_sel.bmp").convert()
    quit_select = pygame.image.load("images/menu_q_sel.bmp").convert()
    over = pygame.image.load('images/gameover_multi.bmp').convert()    
    
   
    while game_over == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                    
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    
            if event.type == KEYUP:
                if event.key == K_DOWN:
                    if y != 570:
                        sel_sound.play()
                        y += 100
                        
                elif event.key == K_UP:
                    if y != 370:
                        sel_sound.play()
                        y += -100

                elif event.key == K_RETURN:
                    if y == 370:
                        click_sound.play()
                        if ai:
                            multiai.game(music_play)
                        else:
                            multiPlayer.game(music_play)
                        game_over = False

                    elif y == 470:
                        click_sound.play()
                        menu.menu()
                        game_over = False

                    elif y == 570:
                        click_sound.play()
                        pygame.quit()
                        sys.exit()

        screen.blit(over, (0, 0))

        #blits the text for who won
        screen.blit(whoWonText, (25, 290))
        screen.blit(whoWonText2, (25, 350))

        #blits the buttons
        if y == 370:
            screen.blit(again_select, (500, 320))
            screen.blit(back_menu, (500, 420))
            screen.blit(quit_game, (500, 520))
        elif y == 470:
            screen.blit(again, (500, 320))
            screen.blit(menu_select, (500, 420))
            screen.blit(quit_game, (500, 520))
        elif y == 570:
            screen.blit(again, (500, 320))
            screen.blit(back_menu, (500, 420))
            screen.blit(quit_select, (500, 520))
            
        pygame.display.update()
