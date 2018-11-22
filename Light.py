import pygame
from pygame.sprite import Sprite
#class derived from python crash course book by eric matthes
class Light(Sprite):

    def __init__(self,setting,screen,ship):
        #initializing light values
        super(Light,self).__init__()
        self.screen = screen

        #light image derived from capcom fighting games
        #initializing light
        self.image = pygame.image.load('C:\\untitled\\First work\\Time dilation\\light.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #initializing rect values
        self.rect.y = float(self.rect.y)
        self.rect.x = float(self.rect.x)
        self.temporary_y = self.rect.y
        self.temporary_x = self.rect.x

    #below are functions to change positions
    def changey(self, speed):
        self.temporary_y -= float(speed)
        self.rect.y = self.temporary_y

    def sety(self,value):
        self.rect.y = float(value)

    def changex(self,speed):
        self.temporary_x += speed
        self.rect.x = self.temporary_x

    def drawlight(self):
        self.screen.blit(self.image,self.rect)
