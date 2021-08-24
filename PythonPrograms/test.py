import pygame

# variables
global sq1  # square 1
global sq2  # square 2

global sq1_x  # square 1 x position
global sq1_y  # square 1 y position
global sq1_width  # square 1 width
global sq1_height  # square 1 height

global sq2_x  # square 2 x position
global sq2_y  # square 2 y position
global sq2_width  # square 2 width
global sq2_height  # square 2 height

global block
global block_x
global block_y
global block_height
global block_width

global sprinkles1

pygame.init()  # Initialize the Pygame environment

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 77)
PINK = (255, 102, 153)
BACKGROUND = (153, 255, 230)
FONT = (153, 153, 255)

# SCREENS
main_screen_width = 700  # main screen widht
main_screen_height = 500  # main screen hight
main_screen = pygame.display.set_mode(
    [main_screen_width,
     main_screen_height])  # setting the main screen's hight and width
pygame.display.set_caption("main screen")


def show_text(msg, color, x, y):
    text = font.render(msg, True, color)
    main_screen.blit(text, (x, y))


# creating the font
font = pygame.font.SysFont(None, 25)


# creating text
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


image = pygame.image.load('candle.png')
#pygame.transform.smoothscale(image, (50, 50))
block = image
block_rect = block.get_rect()
#pygame.transform.smoothscale(image, (50, 50))
x = block_rect.x
y = block_rect.y

clock = pygame.time.Clock()

speed1 = [1, 1]
speed2 = [1, 1]

sq1 = pygame.image.load("candle.png").convert_alpha()
sq1 = pygame.transform.scale(sq1, [50, 50])
sq2 = pygame.image.load("candle.png").convert_alpha()
sq2 = pygame.transform.scale(sq2, [50, 50])

sq1rect = sq1.get_rect()
sq2rect = sq2.get_rect()

running = True

# ----Main program loop-----#

while running:

    # --- Main event loop

    # Check whether an event has occurred.
    for event in pygame.event.get():  # User did something

        # The stuff at this indentation level only gets executed when pygame has received and event via its get() function.

        if event.type == pygame.QUIT:

            # If user clicked close
            keepgoing = False  # We are done so we exit the main processing loop.

        elif event.type == pygame.KEYDOWN:
            print("User pressed a key.")
            if (event.key == pygame.K_w):
                y -= 10  # move circle 1 up 10 units
            if (event.key == pygame.K_s):
                y += 10
            if (event.key == pygame.K_a):
                x -= 10
            if (event.key == pygame.K_d):
                x += 10

            if (event.key == pygame.K_i):
                # User wants to display the image
                x, y = block_rect.left, block_rect.top
                main_screen.blit(block, (x, y))

        elif event.type == pygame.KEYUP:
            print("User let go of a key.")

    # --- Game logic should go here

    # --- Drawing code should go here

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    main_screen.fill((153, 255, 230))

    # Move the green circle slowly to the right continually
    # if the D key is held down!
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_d] == True):
        x += 1

    # Move the green circle slowly to the left continually
    # if the A key is held down!
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_a] == True):
        x -= 1

    # left bouncing square
    sq1rect = sq1rect.move(speed1)
    # collision detection
    if sq1rect.left < 0 or sq1rect.right > main_screen_height:
        speed1[0] = -speed1[0]

    if sq1rect.top < 0 or sq1rect.bottom > main_screen_height:
        speed1[1] = -speed1[1]

    # right bouncing square
    sq2rect = sq2rect.move(speed2)
    # collision detection
    if sq2rect.left < 0 or sq2rect.right > main_screen_width:
        speed2[0] = -speed2[0]

    if sq2rect.top < 0 or sq2rect.bottom > main_screen_height:
        speed2[1] = -speed2[1]

    # The stuff below here is stuff we want to always have on the screen
    # for whatever reason.

    # STATIC DRAWING STUFF

    # Print some text on the window.

    # --- Go ahead and update the screen with what we've drawn.

    main_screen.blit(sq1, sq1rect)
    main_screen.blit(sq2, sq2rect)

    pygame.display.flip()
    # --- Limit to 60 frames per second

    # Wait a little bit.

    clock.tick(60)

pygame.quit()