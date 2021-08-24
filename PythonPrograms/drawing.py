import pygame
import random
#
# This code is adapted from code presented in:
# programarcadegames.com/index.php?chapter=introduction_to_graphics&lang=en#section_5
#


pygame.init()  # Initialize the Pygame environment

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
SOMECOLOUR = (255, 162, 0)
PI = 3.1416

# global rectColour = BLUE  Can't initialize a global where it's declared
global rectColour
rectColour = BLUE

global m_x, m_y


theSize = (400, 500)  # width, height
# Set up screen as our display window.
screen = pygame.display.set_mode(theSize)

pygame.display.set_caption("My Picture") #Window Name

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

screen.fill(SOMECOLOUR)  # Background colour for our screen

# Set up some stuff that doesn't change position on the screen.


#pygame.draw.SHAPE(WHERE?, COLOURVALUES(RGB), [X topleft,Y topleft] , horizontalWidth, verticalHeight
pygame.draw.rect(screen, rectColour, [5, 10, 100, 50], 0)
# 5 is upper left corner x, 10 is upper left corner y, 100 is horizontal width, 50 is vertical height
# For the final paramater value -- 0 means fill the rectangle, value > 0 means non-filled rectangle
# with that edge width.
pygame.draw.circle(screen, RED, [130, 110], 50, 0)

# Integer value Variable Setup
greenRectUL_X = 80
greenRectUL_Y = 110
blueRectUL_W = 100
blueRectUL_X = 5
blueRectUL_y = 10

pygame.draw.rect(screen, rectColour, [blueRectUL_X, blueRectUL_y, blueRectUL_W, 50], 0)
pygame.draw.rect(screen, GREEN, [greenRectUL_X, greenRectUL_Y, 10, 40], 0)

pygame.display.flip()  # Now actually draw the stuff you've set up.

bounce = True #Did the Bluerectangle hit the right hand side
leftMBPress = False  # Did the user press the left mouse button down

# -------- Main Program Loop -----------

while not done:

    # print("At top of main program loop!")

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

##        if event.type == pygame.MOUSEMOTION:
##            print ("MOUSEMOTION event!")

    # --- Game logic should go here (When running through for loops BREAK!)

    # --- Drawing code should go here (When running through for loops BREAK!)
    screen.fill(SOMECOLOUR)  # Background colour for our screen
    pygame.draw.circle(screen, RED, [130, 110], 50, 0) # STATIC CIRCLE

    # --- Blue rectangle passively moves from left to right
    if (bounce == True):
        for x in range(0, 400-blueRectUL_W):
            if blueRectUL_X <= 400-blueRectUL_W:
                blueRectUL_X += 1
                break;
            else:
                print("Hit Right side of window!")
                rectColour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
                SOMECOLOUR = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
                bounce = False
                break
    # --- Blue rectangle passively moves from right to left
    if (bounce == False):
        for x in range(0,400-blueRectUL_W):
            if blueRectUL_X >= 0:
                blueRectUL_X -= 1
                break
            else:
                print("Hit left side of window!")
                rectColour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
                SOMECOLOUR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                bounce = True
                break
    pygame.draw.rect(screen, rectColour, [blueRectUL_X, blueRectUL_y, blueRectUL_W, 50], 0)
    # Move the green rectangle diagonally down and to the right a little bit if the left mouse button is pressed.

    if (leftMBPress == True):
        greenRectUL_X += 1
        greenRectUL_Y += 1
    else:
        greenRectUL_X= 80
        greenRectUL_Y= 110

    pygame.draw.rect(screen, GREEN, [greenRectUL_X, greenRectUL_Y, 10, 40], 0)


    pygame.display.flip()



    # --- Limit to 60 frames per second
    clock.tick(60)

print("Quitting the program!")
pygame.quit()
