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

def initialize_pygame() -> pygame.Surface:
    """
    Initialize all imported Pygame modules and set up the display with specified width, height, and title.

    Returns:
        pygame.Surface: The screen surface to draw on.
    """
    pygame.init()
    screen = pygame.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
    pygame.display.set_caption(Config.SCREEN_TITLE)
    return screen

def handle_player_movement(keys: pygame.key.ScancodeWrapper, player_pos: dict) -> None:
    """
    Update the player's position based on key presses.
    The player moves in steps, meaning the player moves a fixed distance each time a key is pressed.
    The movement is restricted to ensure the player does not move off-screen.

    Args:
        keys (pygame.key.ScancodeWrapper): The state of all keys.
        player_pos (dict): The current position of the player.
    """
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_pos['x'] = max(0, player_pos['x'] - Config.PLAYER_STEP)
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_pos['x'] = min(Config.SCREEN_WIDTH - Config.PLAYER_SIZE, player_pos['x'] + Config.PLAYER_STEP)
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player_pos['y'] = max(0, player_pos['y'] - Config.PLAYER_STEP)
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player_pos['y'] = min(Config.SCREEN_HEIGHT - Config.PLAYER_SIZE, player_pos['y'] + Config.PLAYER_STEP)

def handle_events() -> bool:
    """
    Listen for events such as quitting the game.
    Returns False if the user wants to quit, otherwise returns True to keep the game running.

    Returns:
        bool: True if the game should continue running, False if it should quit.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def draw_player(screen: pygame.Surface, player_pos: dict) -> None:
    """
    Draw the player at the current position on the screen.
    The player is represented as a rectangle.

    Args:
        screen (pygame.Surface): The screen surface to draw on.
        player_pos (dict): The current position of the player.
    """
    pygame.draw.rect(screen, Config.PLAYER_COLOR, (player_pos['x'], player_pos['y'], Config.PLAYER_SIZE, Config.PLAYER_SIZE))

def main() -> None:
    """
    Main game loop that runs the game.
    Initializes Pygame, sets up the player position, and keeps the game running until the user quits.
    """
    screen = initialize_pygame()
    player_pos = {'x': Config.SCREEN_WIDTH // 2, 'y': Config.SCREEN_HEIGHT // 2}

    running = True
    while running:
        running = handle_events()
        keys = pygame.key.get_pressed()
        handle_player_movement(keys, player_pos)
        screen.fill(Config.BACKGROUND_COLOR)
        draw_player(screen, player_pos)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()