import pygame
import random
import math
from pygame import mixer
import os
#
# This code is adapted from code presented in:
# programarcadegames.com/index.php?chapter=introduction_to_graphics&lang=en#section_5
#

pygame.init()  # Initialize the Pygame environment
pygame.font.init()
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
SOMECOLOUR = (255, 162, 0)
sprinkles = (128,255,255)
CAKE     =(230,0,191)
single = 0
# global rectColour = BLUE  Can't initialize a global where it's declared
global rectColour
rectColour = BLUE
theImage = pygame.image.load('candle.png')
theImage = pygame.transform.smoothscale(theImage, (50, 50))
print(os.path.isfile('candle.png'))
global m_x, m_y

m_x = 0
m_y = 450
theSize = (400, 500)  # width, height
# Set up screen as our display window.
screen = pygame.display.set_mode(theSize)

pygame.display.set_caption("Happy Birthday!") #Window Name

# Loop until the user clicks the close button.
done = False
#background music

mixer.music.load('background.wav')
pygame.mixer.music.queue('bday.wav')
mixer.music.play(-1)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

screen.fill(SOMECOLOUR)  # Background colour for our screen

# Set up some stuff that doesn't change position on the screen.

# Integer value Variable Setup
blueRectUL_W = 100
blueRectUL_X = 5
blueRectUL_y = 10
plusx = 1
plusy = 6
toplist=[] #topping list or sprinkle list
middle=[]
del middle
middle = []
for i in range(0, 40):
    lucky = random.randint(0, 100)
    if (lucky >= 95):
        toplist.append((random.randint(185, 215), random.randint(310, 345)))
    elif (lucky >= 70):
        toplist.append((random.randint(135, 265), random.randint(360, 390)))
    else:
        toplist.append((random.randint(110, 290), random.randint(410, 490)))
for i in range(0,100):
    middle.append((random.randint(0, 390), random.randint(0, 490)))
confetti = False
bounce = True #Did the Blue rectangle hit the right hand side
leftMBPress = False  # Did the user press the left mouse button down
sKEYPress = False
rKEYPress = False
snow = False
soundswitch= False
# -------- Main Program Loop -----------
print("Happy Birthday press h to see all commands!")
while not done:
    # --- Main event loop

    for event in pygame.event.get():  # User did something, so get the front most event out of the queue
        # Typically you will only ever have one event in the queue at a time because of the speed of the main program loop.

        if event.type == pygame.QUIT:  # If user clicked close (X button at upper right hand corner of the drawing screen)
            print("QUIT event read from event queue!")
            done = True  # Flag that we are done so we exit this loop
        if event.type == pygame.MOUSEBUTTONDOWN:  # User has pressed left mouse button
            leftMBPress = True
            print("MOUSBUTTONDOWN event!")
        if event.type == pygame.MOUSEBUTTONUP:  # User has released left mouse button
            leftMBPress = False
            print("MOUSEBUTTONUP event!")
        if event.type == pygame.KEYDOWN:
            print("A KEY HAS BEEN PRESSED")
            if event.key == pygame.K_s: #user stopped the bouncing bday
                print("S has been pressed stopping Text...")
                sKEYPress = True
            if event.key == pygame.K_h:
                print("Happy Birthday Help!")
                print("S to stop the text!")
                print("Arrow up to move candle up")
                print("Arrow down to move candle down")
                print("Arrow left to move candle left")
                print("Arrow right to move candle right")
                if confetti == True:
                    print("Pressing mouse down will unleash confetti!")
                print("R to reset snow")
                print("Q to release snow")
            if (event.key == pygame.K_UP and confetti == False):
                m_y -= 10  # move circle 1 up 10 units
            if (event.key == pygame.K_DOWN and confetti == False):
                m_y += 10
            if (event.key == pygame.K_LEFT and confetti == False):
                m_x -= 10
            if (event.key == pygame.K_RIGHT and confetti == False):
                m_x += 10
            if (event.key == pygame.K_q):
                snow = True
            if event.key == pygame.K_r:
                snow = False
                middle = []
                for i in range(0, 100):
                    middle.append((random.randint(0, 390), random.randint(0, 490)))

    # --- Game logic should go here (When running through for loops BREAK!)
    if m_x >= 160 and m_x <= 190:
        if m_y >= 270 and m_y< 280:
            soundswitch = True
            confetti = True
            bounce = False
            sKEYPress = True
    if soundswitch == True and single == 0:
        pygame.mixer.music.stop()
        bday = pygame.mixer.Sound('bday.wav')
        bday.set_volume(0.2)
        bday.play(-1)
        single += 1
    if bounce == False:
        bouncingtxt = "Happy Birthday!"
    else:
        bouncingtxt = "Put Candle on Cake!"
    if confetti == True and leftMBPress == True:
        growth = 6
        lorr = random.randint(0,100) #left or right
        height =(random.randint(40, 120))
        slope = (random.randint(2,30))
        if lorr <= 50:
            rwidth = random.randint (30,80)
            rlength = random.randint (100,400)
            rect = m_x+rwidth/2, m_y-rlength/2, rwidth, rlength
            for i in range(m_y, height, -1):
                growth += 1
                pygame.draw.arc(screen, GREEN, rect,math.pi/2, math.pi,2)
                pygame.draw.circle(screen, RED, (rwidth/4+300, rlength/4), growth,int(growth/6))
                pygame.display.flip()
        else:
            growth = 6
            rwidth = random.randint(30,80)
            rlength = random.randint (100,400)
            rect = m_x-(rwidth-30), m_y-rlength/2, rwidth, rlength
            for i in range(m_y, height, -1):
                growth += 1
                pygame.draw.arc(screen, GREEN,rect, 0,math.pi/2,2)
                pygame.draw.circle(screen, RED, (rwidth/4+100, rlength/4), growth,int(growth/6))
                pygame.display.flip()


    # --- Drawing code should go here (When running through for loops BREAK!)
    screen.fill(SOMECOLOUR)  # Background colour for our screen
    pygame.draw.rect(screen, CAKE, [100, 400, 200, 100], 0) #base
    pygame.draw.rect(screen, CAKE, [125, 350, 150, 75], 0) #middle
    pygame.draw.rect(screen, CAKE, [175, 300, 50, 50], 0) #top!


    for i in range(0,len(toplist)):
        pygame.draw.circle(screen, sprinkles, (toplist[i]), 3, 0) #Sprinkles!
    # --- text passively moves from left to right
    if (bounce == True and sKEYPress == False):
        for x in range(0, 400-blueRectUL_W):
            if blueRectUL_X <= 400-225 and blueRectUL_y <= 250:
                blueRectUL_X += plusx
                blueRectUL_y += plusy
                break;
            else:
                rectColour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
                SOMECOLOUR = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
                bounce = False
                plusx = random.randint(1,3)
                plusy = random.randint(1,6)
                break

    # --- text passively moves from right to left
    if (bounce == False and sKEYPress == False):
        for x in range(0,400-blueRectUL_W):
            if blueRectUL_X >= 0 and blueRectUL_y >=0:
                    blueRectUL_X -= plusx
                    blueRectUL_y -= plusy
                    break
            else:
                rectColour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
                SOMECOLOUR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                bounce = True
                break
    if snow == True:
        for i in range(0, 500):
            for i in range(0, len(middle)):
                pygame.draw.circle(screen, (255, 255, 255), (middle[i]), 2, 0)
                middle[i] = (middle[i][0] - 0, middle[i][1] + 5)
            break



    if (rKEYPress == True):
        blueRectUL_y = 20
        blueRectUL_X = 20
        rKEYPress = False
    if (sKEYPress == True):
        blueRectUL_y = 0
        blueRectUL_X = 100

    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render(bouncingtxt, False, rectColour, SOMECOLOUR)
    screen.blit(textsurface, (blueRectUL_X, blueRectUL_y))
    screen.blit(theImage, (m_x,m_y))
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

print("Quitting the program!")
pygame.quit()
