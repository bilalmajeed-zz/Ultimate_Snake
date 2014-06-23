# By Bilal Majeed and Ivan Nesevski on June 2/2013
# This is the code for the AI for the snake game, this file
# is called from the multiai.py file

import pygame, sys, os, random #import the needed modules
from pygame.locals import * 

os.environ['SDL_VIDEODRIVER']='windib' #required to run on winXP

#CONSTANTS
right, left, up, down = 20, -20, 10, -10
bgColor = 255, 255, 255
black = 0,0,0
scoreColor = 0, 0, 0
block_size = 20
size = width, height = 1000, 740


def ai(food, snake, came_from, came_from2, pos_xy):
    """ This function contains all the code for the AI to work
        food = which food to eat
        snake = defines the snake
        came_from = where did the snake come from (left/right)
        came_from2 = where did the snake come from (up/down)
        pos_xy = list  of the positions of all the snake parts

        return came_from and came_from2 """

    #------IF THE SNAKE IS GOING RIGHT
    if snake.direction == right:
        
        #if the food is to the left of the snake's head
        if food.position[0] < snake.head.position.x:

            #if the snake was going up
            if came_from2 == "U":
                #if there is anything  below the snake's head
                if (snake.head.position.x, snake.head.position.y  + 20) in pos_xy:
                    snake.change_direction(up)
                    came_from2 = "U"
                else:
                    snake.change_direction(down)
                    snake.change_direction(left)
                    came_from = "L"

            #if the snake was going down
            elif came_from2 == "D":
                #if there is anything above the snake's head
                if (snake.head.position.x, snake.head.position.y - 20) in pos_xy:
                    snake.change_direction(down)
                    came_from2 = "U"
                else:
                    snake.change_direction(up)
                    snake.change_direction(left)
                    came_from = "L"

            # if the snake was going right
            else:
                snake.change_direction(up)
                snake.change_direction(left)
                came_from = "L"

        #if the food is to the right of the snake's head
        elif food.position[0] > snake.head.position.x:

            #if there is anything to the right of the snake's head
            if (snake.head.position.x + 20, snake.head.position.y) in pos_xy:

                if came_from2 == "U":
                    snake.change_direction(up)
                    came_from2 = "U"
                elif came_from2 == "D":
                    snake.change_direction(down)
                    came_from2 = "D"

            else:
                snake.change_direction(right)
                came_from = "R"
                                
        #if the food is below the snake's head
        elif food.position[1] < snake.head.position.y:

            #if there is anything is between the food and the snake
            if (snake.head.position.x, snake.head.position.y - 20) in pos_xy:
                snake.change_direction(right)
                came_from = "R"
            else:
                snake.change_direction(up)
                came_from2 = "U"

        #if the food is above the snake                    
        elif food.position[1] > snake.head.position.y:

            #if there is anything inbetween the food and the snake
            if (snake.head.position.x, snake.head.position.y + 20) in pos_xy:
                snake.change_direction(right)
                came_from = "R"
            else:
                snake.change_direction(down)
                came_from2 = "D"


    #------IF THE SNAKE IS GOING LEFT                            
    elif snake.direction == left:

        #if the food is to the left of the snake
        if food.position[0] < snake.head.position.x:

            #anything infront of the snake
            if (snake.head.position.x - 20, snake.head.position.y) in pos_xy:
                if came_from2 == "U":
                    snake.change_direction(up)
                    came_from2 = "U"
                elif came_from2 == "D":
                    snake.change_direction(down)
                    came_from2 = "D"         
            else:         
                snake.change_direction(left)
                came_from = "L"

        #if the food is to the right of the snake                    
        elif food.position[0] > snake.head.position.x:
            if came_from2 == "U":

                #anything above
                if (snake.head.position.x, snake.head.position.y - 20) in pos_xy:
                    snake.change_direction(down)
                    came_from2 = "D"

                else:                            
                    snake.change_direction(up)
                    snake.change_direction(right)
                    came_from = "R"
                            
            elif came_from2 == "D":

                #anything below
                if (snake.head.position.x, snake.head.position.y + 20) in pos_xy:
                    snake.change_direction(up)
                    came_from2 = "U"

                else:                            
                    snake.change_direction(down)
                    snake.change_direction(right)
                    came_from = "R"
                    
            else:
                snake.change_direction(down)
                snake.change_direction(right)
                came_from = "R"

        #if the food is above the snake                    
        elif food.position[1] < snake.head.position.y:

            #anything between the food and the snake
            if (snake.head.position.x, snake.head.position.y - 20) in pos_xy:
                snake.change_direction(left)
                came_from = "L"
            else:
                snake.change_direction(up)
                came_from2 = "U"

        #if the food is below the snakes                    
        elif food.position[1] > snake.head.position.y:

            #anything between the snake and the food
            if (snake.head.position.x, snake.head.position.y + 20) in pos_xy: 
                snake.change_direction(left)
                came_from = "L"
            else:
                snake.change_direction(down)
                came_from2 = "D"
        
    #------IF THE SNAKE IS GOING UP                        
    elif snake.direction == up:

        #if the food is to the left of the snake
        if food.position[0] < snake.head.position.x:

            #if there is anything beside the snake (left)
            if (snake.head.position.x - 20, snake.head.position.y) in pos_xy:
                snake.change_direction(up)

                #if there is anything infront of the snake and to the left
                if (snake.head.position.x, snake.head.position.y - 20) in pos_xy:
                    if (snake.head.position.x - 20, snake.head.position.y) in pos_xy:
                        snake.change_direction(right)
                        came_from = "R"
                    else:
                        snake.change_direction(left)
                        came_from = "L"
                else:
                    snake.change_direction(up)   
                    came_from2 = "U"
            else:
                snake.change_direction(left)
                came_from = "L"

        #if the food is to the right of the snake
        elif food.position[0] > snake.head.position.x:

            # if there is anything to the right and infront of the snake
            if (snake.head.position.x + 20, snake.head.position.y) in pos_xy:
                if (snake.head.position.x, snake.head.position.y - 20) in pos_xy:
                    snake.change_direction(left)
                    came_from = "L"
                else:
                    snake.change_direction(up)
                    came_from2 = "U"
            else:
                snake.change_direction(right)
                came_from = "R"

        #if the food is infront of the snake
        elif food.position[1] < snake.head.position.y:

            #if there is anything between the snake and the food
            if (snake.head.position.x, snake.head.position.y - 20) in pos_xy: 
                if came_from == "L":
                    snake.change_direction(left)
                    came_from = "L"
                elif came_from == "R":
                    snake.change_direction(right)
                    came_from = "R"
                                    
                if came_from2 == "U":
                    if came_from == "L":
                        snake.change_direction(left)
                        came_from = "L"
                    elif came_from == "R":
                        snake.change_direction(right)
                        came_from = "R"

        #if the food is behind the snake
        elif food.position[1] > snake.head.position.y:
            if came_from == "L":
                snake.change_direction(left)
                snake.change_direction(down)
                came_from2 = "D"
            elif came_from == "R":
                snake.change_direction(right)
                snake.change_direction(down)
                came_from2 = "D"
            else:
                snake.change_direction(right)
                snake.change_direction(down)
                came_from2 = "D"

    #-------IF THE SNAKE IS GOING DOWN
    elif snake.direction == down:

        #if the snake is to the left of the snake
        if food.position[0] < snake.head.position.x:
            #if there is anything behead the head of the snake
            if (snake.head.position.x - 20, snake.head.position.y) in pos_xy:
                snake.change_direction(down)
                came_from2 = "D"

                #if there is anything infront of the snake and to the left
                if (snake.head.position.x, snake.head.position.y + 20) in pos_xy:
                    if (snake.head.position.x - 20, snake.head.position.y) in pos_xy:
                        snake.change_direction(right)
                        came_from = "R"
                    else:
                        snake.change_direction(left)
                        came_from = "L"
                        
            else:                            
                snake.change_direction(left)
                came_from = "L"

        #if the snake is to the right of the snake
        elif food.position[0] > snake.head.position.x:
            
            #if there is anything to the right of the snake
            if (snake.head.position.x + 20, snake.head.position.y) in pos_xy:
                snake.change_direction(down)
                came_from2 = "D"
                #if there anything infront of the snake and to the right
                if (snake.head.position.x, snake.head.position.y + 20) in pos_xy:
                    if (snake.head.position.x - 20, snake.head.position.y) in pos_xy:
                        snake.change_direction(left)
                        came_from = "L"
                
                    else:
                        snake.change_direction(right)
                        came_from = "R"
            else:
                snake.change_direction(right)
                came_from = "R"

        #if the food is infront of the snake
        elif food.position[1] > snake.head.position.y:
            #if there is anything infront or the right of the snake
            if (snake.head.position.x, snake.head.position.y + 20) in pos_xy:
                if (snake.head.position.x + 20, snake.head.position.y) in pos_xy:
                    snake.change_direction(left)
                    came_from = "L"
                #if there anything to the left
                elif (snake.head.position.x - 20, snake.head.position.y) in pos_xy:
                    snake.change_direction(right)
                    came_from = "R"
                else:
                    if came_from == "R":
                        snake.change_direction(right)
                        came_from = "R"
                    elif came_from == "L":
                        snake.change_direction(left)
                        came_from = "L"
            else:
                snake.change_direction(down)
                came_from2 = "D"

        #if the food is underneath the snake                                
        elif food.position[1] < snake.head.position.y:
            if came_from == "L":
                snake.change_direction(left)
                snake.change_direction(up)
                came_from2 = "U"
            elif came_from == "R":
                snake.change_direction(right)
                snake.change_direction(up)
                came_from2 = "U"
            else:
                snake.change_direction(right)
                snake.change_direction(up)
                came_from2 = "U"

    
    return (came_from, came_from2) #returns came_from and came_from2
