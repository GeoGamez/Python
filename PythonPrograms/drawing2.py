#
# This code is adapted from code presented in:
# programarcadegames.com/index.php?chapter=introduction_to_graphics&lang=en#section_5
#

import pygame
import random

pygame.init()

# Define some colors
# (red, green, blue) triplets, each one in range 0-255.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

PI = 3.1416

global rectColour
global m_x, m_y  # Mouse x and y positions

global circ1_x, circ1_y  # x and y positions for circle 1

global circ2_x, circ2_y
global circ2_colour
circ2_colour = WHITE  # same as background initially, to make the circle invisible

global follower_x, follower_y  # x and y position offsets for "follower" rectangle

global displayImage
displayImage = False  # No image stuff unless user presses I key.
#theImage = pygame.image.load("Lina.jpg")

rectColour = RED
m_x = 0
m_y = 0

size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
keepgoing = True

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Set initial position for circle 1
circ1_x = 200
circ1_y = 100

# Set initial position of "surprise" circle 2 to that of circle 1
circ2_x = circ1_x
circ2_y = circ1_y

# Set an initial offset for "follower" rectangle
follower_x = 0
follower_y = 0

# -------- Main Program Loop -----------

# In an infinite processing loop until done gets set to true.

while keepgoing:

    # --- Main event loop

    # Check whether an event has occurred.
    for event in pygame.event.get():  # User did something

        # The stuff at this indentation level only gets executed when pygame has received and event via its get() function.

        if event.type == pygame.QUIT:  # If user clicked close
            keepgoing = False  # We are done so we exit the main processing loop.

        elif event.type == pygame.KEYDOWN:
            print("User pressed a key.")
            if (event.key == pygame.K_UP):
                circ1_y -= 10  # move circle 1 up 10 units
            if (event.key == pygame.K_DOWN):
                circ1_y += 10
            if (event.key == pygame.K_LEFT):
                circ1_x -= 10
            if (event.key == pygame.K_RIGHT):
                circ1_x += 10

            if (event.key == pygame.K_o):
                # Set initial position of "surprise" circle (O key pressed)
                # and make it appear other than background colour.
                circ2_x = circ1_x + 50
                circ2_y = circ1_y + 100
                circ2_colour = BLACK
            if (event.key == pygame.K_p):
                # Make "surprise" circle disappear (same as background colour)
                # when P key is pressed
                circ2_colour = WHITE

            if (event.key == pygame.K_i):
                # User wants to display the image
                displayImage = True
            if (event.key == pygame.K_u):
                # User wants to remove the image
                displayImage = False



        elif event.type == pygame.KEYUP:
            print("User let go of a key.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed mouse button down.")
        elif event.type == pygame.MOUSEBUTTONUP:
            print("User released the mouse button.")

        elif event.type == pygame.MOUSEMOTION:
            m_x, m_y = pygame.mouse.get_pos()
            print("x is ", m_x, " y is ", m_y)
            if (rectColour == RED):
                rectColour = BLUE
            else:
                rectColour = RED

            follower_x = m_x + random.randint(-50, 50)
            follower_y = m_y + random.randint(-50, 50)

    # --- Game logic should go here

    # --- Drawing code should go here

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)

    # Move the green circle slowly to the right continually
    # if the D key is held down!
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_d] == True):
        circ1_x += 1

    # Move the green circle slowly to the left continually
    # if the A key is held down!
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_a] == True):
        circ1_x -= 1

    # Draw a rectangle based on my current mouse cursor position!
    # Will end up making the rectangle move according to mouse movement!
    pygame.draw.rect(screen, rectColour, [m_x, m_y, 20, 40], 0)

    pygame.draw.rect(screen, BLACK, [follower_x, follower_y, 20, 25], 2)

    # Draw circle 1
    pygame.draw.circle(screen, GREEN, [circ1_x, circ1_y], 25, 3)

    # Draw/hide circle 2 "surprise circle" when user presses O/P key
    # Hiding it is done by drawing it in the same colour as the background.
    pygame.draw.circle(screen, circ2_colour, [circ2_x, circ2_y], 10, 0)

    # The stuff below here is stuff we want to always have on the screen
    # for whatever reason.

    # STATIC DRAWING STUFF

    # Draw on the screen a green line from (0, 0) to (100, 100)
    # that is 5 pixels wide.
    pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)

    # Draw on the screen several lines from (0, 10) to (100, 110)
    # 5 pixels wide using a while loop
    y_offset = 0
    while y_offset < 100:
        pygame.draw.line(screen, BLUE, [0, 10 + y_offset], [100, 110 + y_offset], 5)
        y_offset = y_offset + 10

    # Display the jpg image if the I key was pressed.
    if (displayImage == True):
        screen.blit(theImage, (100, 50))

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second

    # Wait a little bit.

    clock.tick(60)

pygame.quit()
