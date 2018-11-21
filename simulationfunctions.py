import Settings
import math
import pygame
import sys
import Settings as st
import TextAndButton as textprep

#screen reblit
def updatescreen(Setting, speed1,speed2,speedHorizontal,screen,ship1,ship2,firstLight,secondLight,reflect):
    screen.blit(Setting.bg,[0,0])
    ship1.blitme()
    ship2.blitme()
    reflect.drawmirror()
    firstLight.drawlight()
    secondLight.drawlight()
    ship2.changex(speedHorizontal)
    secondLight.changex(speedHorizontal)
    firstLight.changey(speed1)
    secondLight.changey(speed2)

#main text initialization
def initialize_main_text(text,screen):
    speedratio = 0
    text_1_settings = st.txt(30,60,(0,0,0),(255,255,255),50,"book antiqua",450,30)
    text.append (textprep.text(text_1_settings,screen,"Time Dilation Simulation"))

    text_2_settings = st.txt(30,50,(255,255,255),(0,0,0),25,"times new roman",235,120)
    text.append(textprep.text(text_2_settings,screen,"Ratio to speed of light"))

    text_3_settings = st.txt(40,40,(255,252,252),(0,0,0),25,"times new roman",250,160)
    text.append(textprep.text(text_3_settings,screen,str(speedratio)))

    text_4_settings = st.txt(35,35,(255,252,252),(0,0,0),25,"times new roman",300,162)
    text.append(textprep.text(text_4_settings,screen,">"))

    text_5_settings = st.txt(35,35,(255,252,252),(0,0,0),25,"times new roman",350,162)
    text.append(textprep.text(text_5_settings,screen,">>"))

    text_6_settings = st.txt(35,35,(255,252,252),(0,0,0),25,"times new roman",200,162)
    text.append(textprep.text(text_6_settings,screen,"<"))

    text_7_settings = st.txt(35,35,(255,252,252),(0,0,0),25,"times new roman",150,162)
    text.append(textprep.text(text_7_settings,screen,"<<"))

    text_8_settings = st.txt(20,50,(255,255,255),(0,0,0),25,"times new roman",235,230)
    text.append(textprep.text(text_8_settings,screen,"start simulation"))

    text_8_settings = st.txt(20,50,(255,255,255),(0,0,0),25,"times new roman",235,270)
    text.append(textprep.text(text_8_settings,screen,"plot graph"))

    return text
#property of https://realpython.com/python-rounding/ making numbers properly rounded
def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier

#main event checker but currently unused because of bugs in turning starting simulation wiwhin the function
def check_event_main(Setting,text,speedratio):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            if text[3].rect.collidepoint(mouse_x,mouse_y) and speedratio + 0.01 <1:
                speedratio += 0.01
            elif text[4].rect.collidepoint(mouse_x,mouse_y) and speedratio + 0.1 <1:
                speedratio += 0.1
            elif text[5].rect.collidepoint(mouse_x,mouse_y) and speedratio - 0.01 >0:
                speedratio -= 0.01
            elif text[6].rect.collidepoint(mouse_x,mouse_y) and speedratio -0.1 >0:
                speedratio -= 0.1
            elif text[7].rect.collidepoint(mouse_x,mouse_y):
                Setting.changestatus(1)
            elif text[8].rect.collidepoint(mouse_x,mouse_y):
                Setting.changestatus(2)
    return speedratio


def initialize_simulation_text(text,screen):
    time_elapsed = 0
    ship_time_elapsed = 0
    text_1_settings = st.txt(30,50,(0,0,0),(255,255,255),30,"Times new roman",100,30)
    text.append(textprep.text(text_1_settings,screen,"Actual time elapsed"))

    text_2_settings = st.txt(30,50,(0,0,0),(255,255,255),30,"arial",100,75)
    text.append(textprep.text(text_2_settings,screen,str(time_elapsed) ))

    text_3_settings = st.txt(30,50,(0,0,0),(255,255,255),30,"Times new roman",500,30)
    text.append(textprep.text(text_3_settings,screen,"time elapsed within moving ship"))

    text_4_settings = st.txt(30,50,(0,0,0),(255,255,255),30,"arial",500,75)
    text.append(textprep.text(text_4_settings,screen,str(ship_time_elapsed)))

    return text
