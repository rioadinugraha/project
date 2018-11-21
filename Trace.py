import pygame
from pygame.sprite import Sprite
#class derived from python crash course book by eric matthes
class Trace(Sprite):

    def __init__(self,screen,secondLight):
        #initializing light values
        super(Trace,self).__init__()
        self.screen = screen

        #initializing Trace
        self.image = pygame.image.load ('C:\\untitled\\First work\\Time dilation\\dot.png')
        self.image =  pygame.transform.scale(self.image,(3,3))
        self.rect = self.image.get_rect()
        self.rect.centerx = secondLight.rect.centerx
        self.rect.top = secondLight.rect.top

    def drawTrace(self):
        self.screen.blit(self.image,self.rect)
