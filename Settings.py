import pygame

class Settings():

    def __init__(self):
        # screen settings
        self.screen_width = 1000
        self.screen_height = 600
        #background image property of https://www.reddit.com/r/wallpapers/comments/1x8aw5/dark_space/
        self.bg = pygame.image.load('C:\\untitled\\First work\\Time dilation\\space.jpg')
        #background by http://wallpaperlepi.com/downloadsites/black-clock-time-wallpaper.html
        self.bg_main = pygame.image.load ('C:\\untitled\\First work\\Time dilation\\clock.jpg')
        self.bg_main = pygame.transform.scale(self.bg_main,(1000,600))
        self.bg_color = (230, 230, 230)
        self.Trace = []

        #music settings
        #music by hiroyuki sawano gundam unicorn
        self.bg_music = pygame.mixer.Sound('C:\\untitled\\First work\\Time dilation\\bgmusic.wav')
        #sound by https://www.soundjay.com/clock-sounds-1.html
        self.bg_music_main = pygame.mixer.Sound('C:\\untitled\\First work\\Time dilation\\clocksound.wav')


        #ship settings
        self.ship1location = 50
        self.ship2location = 150
        self.DefaultHorizontalSpeed = 10
        self.maxHorizontalMovement = 400

        #light settings
        self.baseSpeed = float(10)

        #simulation settings
        self.loops = 40
        self.interval = 0.1
        self.status = 0

    def changestatus(self,num):
        self.status = num

    def addTrace(self,object):
        self.Trace.append(object)

    def getTrace(self):
        return self.Trace

class txt():

    #create a class with all the attribute a button or text has
    def __init__(self,height,width,box_colour,text_colour,font_size,font,x_coordinate,y_coordinate):
        self.background_width = width
        self.background_height = height
        self.box_colour = box_colour
        self.text_colour = text_colour
        self.font_size = font_size
        self.font = font
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
