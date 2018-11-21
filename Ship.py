import pygame
from pygame.sprite import Sprite
#class derived from python crash course book by eric matthes
class Ship(Sprite):

    def __init__(self,settings,screen,shipPosition):
        #initialize ship
        self.screen = screen

        super(Ship,self).__init__()

        self.ai_Settings = settings
        # load the ship image and get its rect.
        #sprite property of http://millionthvector.blogspot.de
        self.image = pygame.image.load('C:\\untitled\\First work\\Time dilation\\fighterspr1.png')
        self.image = pygame.transform.scale(self.image,(100,56))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Ship starting positions
        self.rect.centerx = shipPosition
        self.rect.bottom = self.screen_rect.bottom
        # store a decimal for ship center
        self.centerX = float(self.rect.centerx)
    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def changex(self,speed):
        self.centerX += speed
        self.rect.centerx = self.centerX
