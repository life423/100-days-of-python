import pygame

# Step 1: Initialize Pygame
pygame.init()

# Step 2: Set up the game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Basic GUI with Pygame"
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(SCREEN_TITLE)

# Set a background color (RGB)
background_color = (135, 206, 235)  # Light blue color

# Game loop to keep the window open
running = True
while running:
    # Event handling to close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with the background color
    screen.fill(background_color)

    # Update the display to reflect any changes
    pygame.display.flip()

# Quit Pygame
pygame.quit()