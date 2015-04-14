'''
Created on Apr 13, 2015

@author: Sarah Nathanson
'''
import pygame, sys
from pygame.locals import *
import random

pygame.init()
HEIGHT=300
WIDTH=400
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Alphabet Soup')

#colors
WHITE = (255, 255, 255)
YELLOW = (250, 250, 210)

#fonts
fontObj = pygame.font.Font('freesansbold.ttf', 32)
fontTitle = pygame.font.Font('freesansbold.ttf', 48)
fontSmall = pygame.font.Font('freesansbold.ttf', 16)

#title screen objects setup

#start button
startText=fontObj.render("Start", True, WHITE, YELLOW)
startRect=startText.get_rect()
startRect.center=(WIDTH//2,HEIGHT*.75)

#title text
titleText=fontTitle.render("Alphabet Soup", True, YELLOW)
titleRect=titleText.get_rect()
titleRect.center=(WIDTH//2,HEIGHT*.25)

#instruction text
instructionTextLine1=fontSmall.render("Mouse over the letters in alphabetical", True, YELLOW)
instructionRectLine1=instructionTextLine1.get_rect()
instructionRectLine1.center=(WIDTH//2,HEIGHT//2)

instructionTextLine2=fontSmall.render("order to eat them!", True, YELLOW)
instructionRectLine2=instructionTextLine2.get_rect()
instructionRectLine2.center=(WIDTH//2,HEIGHT//2+18)

#win screen screen objects setup

#title text
winText=fontTitle.render("You win!", True, YELLOW)
winRect=winText.get_rect()
winRect.center=(WIDTH//2,HEIGHT*.4)

#menu button
menuText=fontObj.render("Main Menu", True, WHITE, YELLOW)
menuRect=menuText.get_rect()
menuRect.center=(WIDTH//2,HEIGHT*.6)

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

while True:#entire game loop
    while True: # title screen loop
        DISPLAYSURF.fill(WHITE)
        #blit objects
        DISPLAYSURF.blit(startText, startRect)
        DISPLAYSURF.blit(titleText, titleRect)
        DISPLAYSURF.blit(instructionTextLine1, instructionRectLine1)
        DISPLAYSURF.blit(instructionTextLine2, instructionRectLine2)
        
        #start game when mouse over start
        if abs(pygame.mouse.get_pos()[0]-startRect.center[0])<(startRect.width//2) and abs(pygame.mouse.get_pos()[1]-startRect.center[1])<(startRect.height//2):
            break;
            
        #quit option  
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
    
    #game setup
    a=[]#list of lists of letter parts
    for i in range(0,26):
        #make list of letter parts in list
        a.append([fontObj.render(chr(97+i), True, WHITE)]);
        a[i].append(a[i][0].get_rect())
        a[i][1].center=(random.randrange(400),random.randrange(300))
    
    while True: # soup game loop
        DISPLAYSURF.fill(YELLOW)
        for i in a:#go through each list of letter parents
            i[1].center=(i[1].center[0]+random.randrange(-2,3),i[1].center[1]+random.randrange(-2,3))#move letter randomnly
            
            #don't let letter go with 20 pixels of screen edges
            if i[1].center[0] < 20:
                i[1].center=(20,i[1].center[1])
            if i[1].center[0] > WIDTH-20:
                i[1].center = (380,i[1].center[1])
            if i[1].center[1] < 20:
                i[1].center=(i[1].center[0],20)
            if i[1].center[1] > HEIGHT-20:
                i[1].center = (i[1].center[0],280)
                
            DISPLAYSURF.blit(i[0], i[1])
            
            #if mouse touches letter that currently is earliest in the alphabet, remove that letter fromt he list
            if abs(pygame.mouse.get_pos()[0]-i[1].center[0])<(i[1].width//2) and abs(pygame.mouse.get_pos()[1]-i[1].center[1])<(i[1].height//2) and a.index(i)==0:
                a.remove(i)
                
        #go to win screen if no more letters
        if len(a) == 0:
            break;
               
        #quit option
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
        pygame.display.update()
        fpsClock.tick(FPS)
        
    while True:#win screen loop
        DISPLAYSURF.fill(WHITE)
        #blit objects
        DISPLAYSURF.blit(winText, winRect)
        DISPLAYSURF.blit(menuText, menuRect)
        
        if abs(pygame.mouse.get_pos()[0]-menuRect.center[0])<(menuRect.width//2) and abs(pygame.mouse.get_pos()[1]-menuRect.center[1])<(menuRect.height//2):
            break;
        
        #quit option
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
