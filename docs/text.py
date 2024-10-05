import pygame, sys

# Initialize Pygame
pygame.init()

# Set the size of the screen
screen_size = (500, 500)
screen = pygame.display.set_mode(screen_size)

# Set the color of the rectangle
rect_color = (255, 0, 0)  # (R, G, B)

# Set the dimensions and position of the rectangle
rect_width = 100
rect_height = 50
rect_x = 200
rect_y = 200
background = pygame.image.load("image\Background\Background.jpg")
# Create a rectangle object
#rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

# Draw the rectangle onto the screen
#pygame.draw.rect(screen, rect_color, rect)

# Update the display
pygame.display.update()

# Run the game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0, 0))
    pygame.display.flip()