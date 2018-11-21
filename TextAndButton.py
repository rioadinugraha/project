import pygame.font

#class derived from python crash course book by eric matthes

class text():

    def __init__(self,txt,screen,msg):
        #screen detection
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #text initialization
        self.width, self.height = txt.background_width,txt.background_height
        self.button_colour = txt.box_colour
        self.text_colour =txt.text_colour
        self.font = pygame.font.SysFont(txt.font,txt.font_size)

        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect = self.rect.move(txt.x_coordinate,txt.y_coordinate)
        self.prep_msg(msg)

    #message preparation
    def prep_msg(self,msg):
        self.msg_image = self.font.render(msg, True, self.text_colour, self.button_colour)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center =self.rect.center

    #making the button appear on screen
    def draw_button(self):
        self.screen.fill(self.button_colour, self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)
