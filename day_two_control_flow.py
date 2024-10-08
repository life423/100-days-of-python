import pygame

# Configuration class
class Config:
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    SCREEN_TITLE = "2D Platformer - Player Movement"
    BACKGROUND_COLOR = (135, 206, 235)  # Light blue color

    PLAYER_COLOR = (0, 102, 204)  # A shade of blue for the player
    PLAYER_SIZE = 50  # Size of the player square
    PLAYER_STEP = 10  # Step size for the player's movement

# Initialize Pygame
def initialize_pygame():
    # Initialize all imported Pygame modules
    pygame.init()
    # Set up the display with specified width, height, and title
    screen = pygame.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
    pygame.display.set_caption(Config.SCREEN_TITLE)
    return screen

# Handle player movement
# This function updates the player's position based on key presses
# The player moves in steps, meaning the player moves a fixed distance each time a key is pressed
# The movement is restricted to ensure the player does not move off-screen
def handle_player_movement(keys, player_pos):
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_pos['x'] = max(0, player_pos['x'] - Config.PLAYER_STEP)
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_pos['x'] = min(Config.SCREEN_WIDTH - Config.PLAYER_SIZE, player_pos['x'] + Config.PLAYER_STEP)
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player_pos['y'] = max(0, player_pos['y'] - Config.PLAYER_STEP)
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player_pos['y'] = min(Config.SCREEN_HEIGHT - Config.PLAYER_SIZE, player_pos['y'] + Config.PLAYER_STEP)

# Handle events such as quitting the game
# This function listens for events and returns False if the user wants to quit
# Otherwise, it returns True to keep the game running
def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

# Draw player on screen
# This function draws the player at the current position on the screen
# The player is represented as a rectangle
def draw_player(screen, player_pos):
    pygame.draw.rect(screen, Config.PLAYER_COLOR, (player_pos['x'], player_pos['y'], Config.PLAYER_SIZE, Config.PLAYER_SIZE))

# Main game loop
# This is the main function that runs the game loop
# It initializes Pygame, sets up the player position, and keeps the game running until the user quits
def main():
    # Initialize Pygame and set up the game window
    screen = initialize_pygame()
    # Initial player position is in the center of the screen
    player_pos = {'x': Config.SCREEN_WIDTH // 2, 'y': Config.SCREEN_HEIGHT // 2}

    running = True
    while running:
        # Handle events like quitting the game
        running = handle_events()

        # Get the state of all keys and update player position if necessary
        keys = pygame.key.get_pressed()
        handle_player_movement(keys, player_pos)

        # Fill the screen with the background color
        screen.fill(Config.BACKGROUND_COLOR)

        # Draw the player in the updated position
        draw_player(screen, player_pos)

        # Update the display to show the new state
        pygame.display.flip()

    # Quit Pygame and close the window when the game loop ends
    pygame.quit()

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()