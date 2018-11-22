import simulationfunctions as sf
import pygame
import Settings as st
from Ship import Ship
import time
import sys
from Light import Light
import timeDilCalc as tc
import TextAndButton as textprep
import matplotlib.pyplot as plt
from Trace import Trace
from Mirror import mirror
import os

def run_simulation(speedratio):

    #initializing empty variables and lists
    cycle = 0
    time_elapsed = 0
    text = []
    run_once = 0
    temporary_time = 0
    rect_limit = 144
    #initializing pygame and setting values
    pygame.init()
    Setting = st.Settings()

    #obtaining time ratio
    timeDilation = tc.timeDilation(speedratio)
    ratio = timeDilation.gettimeratio()

    #screen and music initialized
    screen = pygame.display.set_mode((Setting.screen_width, Setting.screen_height))
    pygame.display.set_caption("Time Dilation demonstration")
    bg_music = Setting.bg_music
    bg_music.set_volume(0.4)
    bg_music.play(-1)
    #make the ships
    ship1 = Ship(Setting,screen,Setting.ship1location)
    ship2 = Ship(Setting,screen,Setting.ship2location)
    #background display
    screen.blit(Setting.bg,[0,0])

    #make Light
    firstLight = Light(Setting,screen,ship1)
    secondLight = Light(Setting,screen,ship2)
    reflect = mirror(screen)
    Tracelist = []


    #set the speed for light and ship
    speed1= Setting.baseSpeed
    speed2 = Setting.baseSpeed * ratio
    speedHorizontal = Setting.DefaultHorizontalSpeed * ratio * speedratio

    #set up all text and buttons for module
    text = sf.initialize_simulation_text(text,screen)
    text_2_settings = st.txt(30,50,(0,0,0),(255,255,255),30,"arial",100,75)
    text_4_settings = st.txt(30,50,(0,0,0),(255,255,255),30,"arial",500,75)
    #main loop
    while True:
        #loop so that the animation doesn't crash
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.quit()
                    main()
        Tracelist.append(Trace(screen,secondLight))

        # update the screen

        sf.updatescreen(Setting,speed1,speed2,speedHorizontal,screen,ship1,ship2,firstLight,secondLight,reflect)

        # draw text and buttons
        for i in text:
            i.draw_button()
        #if function to reverse the light's direction
        cycle += 1
        if cycle%Setting.loops == 0 and cycle != 0:
            speed1 = -speed1
        if secondLight.temporary_y <= rect_limit and run_once == 0:
            speed2 = -speed2
            positionalRecorrection = rect_limit + (secondLight.rect.y - rect_limit)
            secondLight.sety(positionalRecorrection)
            run_once = 1

        #checking actual time and relative time then updating the text boxes
        time_elapsed += Setting.interval
        time_elapsed = sf.round_half_up(time_elapsed,2)
        temporary_time = temporary_time + (Setting.interval*ratio)
        ship_time_elapsed = sf.round_half_up(temporary_time,2)

        text[1]= textprep.text(text_2_settings,screen,str(time_elapsed))
        text[3] = textprep.text(text_4_settings,screen,str(ship_time_elapsed) )

        #drawing display at the end
        pygame.display.flip()

        #delaying the iteration to give a more realistic time differential
        time.sleep(Setting.interval)

        #ending the animation loop if time within ship is greater than given threshold
        if ship_time_elapsed > Setting.shiptimelimit:
            break
    #updating time data and finalizing screen
    ship_time_elapsed = sf.round_half_up(8,6)
    time_elapsed = sf.round_half_up(8/ratio,2)
    text[3] = textprep.text(text_4_settings,screen,str(ship_time_elapsed))
    text[1] = textprep.text(text_2_settings,screen,str(time_elapsed))

    sf.updatescreen(Setting,speed1,speed2,speedHorizontal,screen,ship1,ship2,firstLight,secondLight,reflect)
    for i in Tracelist:
        i.drawTrace()
    for i in text:
        i.draw_button()

    #final loop to display conclusion
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.quit()
                    main()
        pygame.display.flip()


def main():
    #initialization
    speedratio = 0
    text = []
    pygame.init()
    Setting = st.Settings()
    screen = pygame.display.set_mode((Setting.screen_width, Setting.screen_height))
    pygame.display.set_caption("Time Dilation")
    screen.blit(Setting.bg_main,[0,0])


    #music set up
    bg_music = Setting.bg_music_main
    bg_music.set_volume(0.9)
    bg_music.play(-1)

    #text and button set up
    text = sf.initialize_main_text(text,screen)

    for i in text:
        i.draw_button()

    #main loop

    while True:
        speedratio = sf.check_event_main(Setting,text,speedratio)
        speedratio = sf.round_half_up(speedratio,2)
        text_3_settings = st.txt(40,40,(255,252,252),(0,0,0),25,"times new roman",250,160)
        text[2] = textprep.text(text_3_settings,screen,str(speedratio))
        text[2].draw_button()
        pygame.display.flip()
        if Setting.status == 1:
            pygame.quit()
            Setting.changestatus(0)
            run_simulation(speedratio)
        elif Setting.status == 2:
            Setting.changestatus(0)
            graph(speedratio)

def graph(speedratio):

    #plotting graph for time dilation
    timeDilation = tc.timeDilation(speedratio)
    ratio = timeDilation.gettimeratio()
    xcoordinate = []
    ycoordinate = []
    for time in range (0, 80+1):
        xresult = 0.1*time
        yresult = xresult*ratio
        xcoordinate.append(xresult)
        ycoordinate.append(yresult)

    plt.scatter(xcoordinate,ycoordinate,cmap = plt.cm.Blues,s =100)
    plt.tick_params(axis='both',labelsize=15)
    plt.xlabel("Actual time",fontsize = 14)
    plt.title ("Time Dilation time comparison", fontsize = 20)
    plt.ylabel("Time within moving ship",fontsize = 14)
    plt.axis([0,8,0,8])
    plt.show()


os.environ['SDL_VIDEO_WINDOW_POS'] = "100,100"
main()
