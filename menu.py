# By Ivan Nesevski and Bilal Majeed on June 2/2013
# This file has the classes for the main menu and also
# the function thta runs it. This file is called from
# gameOver.py and main.py

#IMPORT THE NEEDED MODULES
import pygame, sys, os, multiai
from pygame.locals import *

os.environ['SDL_VIDEODRIVER']='windib' #required for winXP

#CONSTANTS
size = width, height = 640, 610
black = (0, 0, 0)

class Menu:
    """ This class updates the main screen of the menu """
    def __init__(self, screen):
        self.screen = screen
        self.title = pygame.image.load('images/menutitle.bmp').convert()
        self.singleplayer = pygame.image.load('images/menu_s.bmp').convert()
        self.multiplayer = pygame.image.load('images/menu_m.bmp').convert()
        self.options = pygame.image.load('images/menu_o.bmp').convert()
        self.quit = pygame.image.load('images/menu_q.bmp').convert()
        self.s_select = pygame.image.load('images/menu_s_sel.bmp').convert()
        self.m_select = pygame.image.load('images/menu_m_sel.bmp').convert()
        self.o_select = pygame.image.load('images/menu_o_sel.bmp').convert()
        self.q_select = pygame.image.load('images/menu_q_sel.bmp').convert()
        
    def update(self, y):
        """ updates the display with the buttons according to what
            is selected """
        self.screen.blit(self.title, (70, 5))
        if y == 220:
            self.screen.blit(self.s_select, (170, 220))
            self.screen.blit(self.multiplayer, (170, 320))
            self.screen.blit(self.options, (170, 420))
            self.screen.blit(self.quit, (170, 520))
        elif y == 320:
            self.screen.blit(self.singleplayer, (170, 220))
            self.screen.blit(self.m_select, (170, 320))
            self.screen.blit(self.options, (170, 420))
            self.screen.blit(self.quit, (170, 520))
        elif y == 420:
            self.screen.blit(self.singleplayer, (170, 220))
            self.screen.blit(self.multiplayer, (170, 320))
            self.screen.blit(self.o_select, (170, 420))
            self.screen.blit(self.quit, (170, 520))
        elif y == 520:
            self.screen.blit(self.singleplayer, (170, 220))
            self.screen.blit(self.multiplayer, (170, 320))
            self.screen.blit(self.options, (170, 420))
            self.screen.blit(self.q_select, (170, 520))

class Multiplayer:
    """ This class updates the screen when selecting which gamemode """
    def __init__(self, screen):
        self.screen = screen
        self.title = pygame.image.load('images/menutitle.bmp').convert()
        self.human = pygame.image.load('images/menu_h.bmp').convert()
        self.comp = pygame.image.load('images/menu_c.bmp').convert()
        self.back = pygame.image.load('images/menu_b.bmp').convert()
        self.h_select = pygame.image.load('images/menu_h_sel.bmp').convert()
        self.c_select = pygame.image.load('images/menu_c_sel.bmp').convert()
        self.b_select = pygame.image.load('images/menu_b_sel.bmp').convert()

    def update(self, y):
        """ updates the display with the buttons according to what
            is selected """
        self.screen.blit(self.title, (70, 5))
        if y == 220:
            self.screen.blit(self.h_select, (170, 220))
            self.screen.blit(self.comp, (170, 320))
            self.screen.blit(self.back, (170, 420))
        elif y == 320:
            self.screen.blit(self.human, (170, 220))
            self.screen.blit(self.c_select, (170, 320))
            self.screen.blit(self.back, (170, 420))
        elif y == 420:
            self.screen.blit(self.human, (170, 220))
            self.screen.blit(self.comp, (170, 320))
            self.screen.blit(self.b_select, (170, 420))

class Options:
    """ This class updates the screen when in options"""
    def __init__(self, screen):
        self.screen = screen
        self.title = pygame.image.load('images/menutitle.bmp').convert()
        self.on = pygame.image.load('images/onbut.bmp').convert()
        self.off = pygame.image.load('images/offbut.bmp').convert()
        self.onpress = pygame.image.load('images/onbutpres.bmp').convert()
        self.offpress = pygame.image.load('images/offbutpres.bmp').convert()
        self.music = pygame.image.load('images/menu_mu.bmp').convert()
        self.mu_select = pygame.image.load('images/menu_mu_sel.bmp').convert()
        self.back = pygame.image.load('images/menu_b.bmp').convert()
        self.b_select = pygame.image.load('images/menu_b_sel.bmp').convert()
        self.help = pygame.image.load('images/menu_hp.bmp').convert()
        self.hp_select = pygame.image.load('images/menu_hp_sel.bmp').convert()

    def update(self, but, y):
        """ updates the display with the buttons according to what
            is selected """
        self.screen.blit(self.title, (70, 5))
        if y == 220:
            self.screen.blit(self.mu_select, (170, 220))
            if but == 0:
                self.screen.blit(self.on, (300, 260))
            elif but == 1:
                self.screen.blit(self.off, (300, 260))  
            elif but == 2:
                self.screen.blit(self.onpress, (300, 260))
            elif but == 3:
                self.screen.blit(self.offpress, (300, 260))
            self.screen.blit(self.help, (170, 320))
            self.screen.blit(self.back, (170, 420))
        elif y == 320:
            self.screen.blit(self.music, (170, 220))
            if but == 0:
                self.screen.blit(self.on, (300, 247))
            elif but == 1:
                self.screen.blit(self.off, (300, 247))  
            elif but == 2:
                self.screen.blit(self.onpress, (300, 247))
            elif but == 3:
                self.screen.blit(self.offpress, (300, 247))
            self.screen.blit(self.hp_select, (170, 320))
            self.screen.blit(self.back, (170, 420))
        elif y == 420:
            self.screen.blit(self.music, (170, 220))
            if but == 0:
                self.screen.blit(self.on, (300, 247))
            elif but == 1:
                self.screen.blit(self.off, (300, 247))  
            elif but == 2:
                self.screen.blit(self.onpress, (300, 247))
            elif but == 3:
                self.screen.blit(self.offpress, (300, 247))
            self.screen.blit(self.help, (170, 320))
            self.screen.blit(self.b_select, (170, 420))

class Help:
    def __init__(self, screen):
        self.screen = screen
        self.title = pygame.image.load('images/menutitle.bmp').convert()
        self.b_select = pygame.image.load('images/menu_b_sel.bmp').convert()
        self.help_screen = pygame.image.load('images/help_screen.bmp').convert()

    def update(self, y):
        self.screen.blit(self.title, (70, 5))
        self.screen.blit(self.help_screen, (0, 200))
        self.screen.blit(self.b_select, (170, 420))
        

def menu():
    """ this function runs the main menu """
    import singlePlayer, multiPlayer
    
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption('Ultimate Snake')
    screen = pygame.display.set_mode(size)
    #loads sounds for playback
    sel_sound = pygame.mixer.Sound('music/menu_select.ogg')
    click_sound = pygame.mixer.Sound('music/menu_button.ogg')
    main_menu = True
    music_play = "on"

    while True:
        menu = Menu(screen)
        multi = Multiplayer(screen)
        options = Options(screen)
        hp = Help(screen)
        update = 0 # 0 = main, 1 = multiplayer select, 2 = options, 3 = help
        but = 0
        y = 220

        while main_menu == True:
          
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if event.type == KEYDOWN:
                    #if the escape key is pressed then the game will quit
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    #changes the buttons to look pressed   
                    if event.key == K_RETURN:
                        if update == 2:
                            if y == 220:
                                if but == 0:
                                    but = 2 
                                elif but == 1:
                                    but = 3
                    
                     
                if event.type == KEYUP:
                    #cycle down the menu   
                    if event.key == K_DOWN:  
                        if update != 0:
                            if y != 420:
                                sel_sound.play()
                                y += 100

                        else:
                            if y != 520:
                                sel_sound.play()
                                y += 100 
                                
                    #cycle up the menu     
                    elif event.key == K_UP:
                        if update != 3:
                            if y != 220:
                                sel_sound.play()
                                y += -100

                        else:
                            if y != 420:
                                sel_sound.play()
                                y += -100
                                
                        
                    elif event.key == K_RETURN:
                        if y == 220:
                            if update == 0:
                                #start singleplayer
                                click_sound.play()
                                singlePlayer.game(music_play)
                                main_menu = False
                                
                            elif update == 1:
                                #start snake wars - human vs. human
                                click_sound.play()
                                multiPlayer.game(music_play)
                                main_menu = False

                            elif update == 2:
                                #changes button to on and off
                                if but == 2:
                                    click_sound.play()
                                    but = 1 #music off
                                    music_play = "off"
                                elif but == 3:
                                    click_sound.play()
                                    but = 0 #music on
                                    music_play = "on"
                                
                        elif y == 320:
                            if update == 0:
                                #goes back to previous menu
                                click_sound.play()
                                update = 1
                                y = 220
                                
                            elif update == 1:
                                #start snake wars - human vs. computer
                                click_sound.play()
                                multiai.game(music_play)
                                main_menu = False

                            elif update == 2:
                                #goes back to previous menu
                                click_sound.play()
                                update = 3
                                y = 420

                        elif y == 420:
                            if update == 0:
                                #goes back to previous menu
                                click_sound.play()
                                update = 2
                                y = 220
                                
                            elif update == 1:
                                #goes back to previous menu
                                click_sound.play()
                                update = 0
                                y = 220

                            elif update == 2:
                                #goes back to previous menu
                                click_sound.play()
                                update = 0
                                y = 220

                            elif update == 3:
                                #goes back to previous menu
                                click_sound.play()
                                update = 2
                                y = 220
                                
                        elif y == 520:
                            #quits the game
                            click_sound.play()
                            pygame.quit()
                            sys.exit()                
                                
            screen.fill(black)
            #updates the screen
            if update == 0:
                menu.update(y)
            elif update == 1:
                multi.update(y)
            elif update == 2:
                options.update(but, y)
            elif update == 3:
                hp.update(y)
                
                
            pygame.display.update()
