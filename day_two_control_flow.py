import pygame

# Configuration class
class Config:
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    SCREEN_TITLE = "2D Platformer - Player Movement"
    BACKGROUND_COLOR = (135, 206, 235)  # Light blue color

    PLAYER_COLOR = (255, 0, 0)  # Red color for the player
    PLAYER_SIZE = 50  # Size of the player square
    PLAYER_SPEED = 5  # Speed of the player's movement

# Initialize Pygame
def initialize_pygame():
    pygame.init()
    screen = pygame.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
    pygame.display.set_caption(Config.SCREEN_TITLE)
    return screen

# Handle player movement
def handle_player_movement(keys, player_pos):
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_pos['x'] -= Config.PLAYER_SPEED
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_pos['x'] += Config.PLAYER_SPEED
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player_pos['y'] -= Config.PLAYER_SPEED
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player_pos['y'] += Config.PLAYER_SPEED

# Draw player on screen
def draw_player(screen, player_pos):
    pygame.draw.rect(screen, Config.PLAYER_COLOR, (player_pos['x'], player_pos['y'], Config.PLAYER_SIZE, Config.PLAYER_SIZE))

# Main game loop
def main():
    screen = initialize_pygame()
    player_pos = {'x': Config.SCREEN_WIDTH // 2, 'y': Config.SCREEN_HEIGHT // 2}

    running = True
    while running:
        # Event handling to close the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get key states
        keys = pygame.key.get_pressed()
        handle_player_movement(keys, player_pos)

        # Fill the screen with the background color
        screen.fill(Config.BACKGROUND_COLOR)

        # Draw the player
        draw_player(screen, player_pos)

        # Update the display
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()