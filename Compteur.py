import pygame,time, sys
from pygame.locals import*
pygame.init()
screen_size = (300,200)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("timer")
time_left = 30 #duration of the timer in seconds
crashed  = False
font = pygame.font.SysFont("Somic Sans MS", 30)
color = (255, 255, 255)

while not crashed:
    for event in pygame.event.get():
        if event.type == QUIT:
            crashed = True
    total_mins = time_left//60 # minutes left
    total_sec = time_left-(60*(total_mins)) #seconds left
    time_left -= 1
    if time_left > -1:
        text = font.render(("Time left: "+str(total_mins)+":"+str(total_sec)), True, color)
        screen.blit(text, (85, 90))
        pygame.display.flip()
        screen.fill((20,20,20))
        time.sleep(1)#making the time interval of the loop 1sec
    else:
        text = font.render("Time's up!!", True, color)
        screen.blit(text, (85, 90))
        pygame.display.flip()
        screen.fill((20,20,20))




pygame.quit()
sys.exit()
'''import pygame
from pygame.locals import *
import queue

class Utils:
    def get_mouse_event(self):
        # get coordinates of the mouse
        position = pygame.mouse.get_pos()
        
        # return left click status and mouse coordinates
        return position

    def left_click_event(self):
        # store mouse buttons
        mouse_btn = pygame.mouse.get_pressed()
        # create flag to check for left click event
        left_click = False

        if mouse_btn[0]: #and e.button == 1:
            # change left click flag
            left_click = True

        return left_click'''
