import pygame
from pygame.sprite import Sprite
#class derived from python crash course book by eric matthes
class mirror(Sprite):

    def __init__(self,screen):
        #initializing light values
        super(mirror,self).__init__()
        self.screen = screen

        #initializing Trace
        self.image = pygame.image.load ('C:\\untitled\\First work\\Time dilation\\whiteline.png')
        self.image =  pygame.transform.scale(self.image,(1000,5))
        self.rect = self.image.get_rect()
        self.rect.centery = 141

    def drawmirror(self):
        self.screen.blit(self.image,self.rect)
