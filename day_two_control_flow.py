import pygame

class Game:
    def __init__(self) -> None:
        """
        Initialize the game, including Pygame and game variables like player position.
        """
        # Game configuration
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600
        self.SCREEN_TITLE = "2D Platformer - Player Movement"
        self.BACKGROUND_COLOR = (135, 206, 235)  # Light blue color

        self.PLAYER_COLOR = (0, 102, 204)  # A shade of blue for the player
        self.PLAYER_SIZE = 50  # Size of the player square
        self.PLAYER_STEP = 50  # Step size for the player's movement

        # Initialize Pygame and set up player position
        self.screen = self.initialize_pygame()
        self.player_pos = {'x': self.SCREEN_WIDTH // 2, 'y': self.SCREEN_HEIGHT // 2}
        self.running = True

    def initialize_pygame(self) -> pygame.Surface:
        """
        Initialize all imported Pygame modules and set up the display with specified width, height, and title.

        Returns:
            pygame.Surface: The screen surface to draw on.
        """
        pygame.init()
        screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption(self.SCREEN_TITLE)
        return screen

    def handle_events(self) -> None:
        """
        Listen for events such as quitting the game and player movement.
        Updates the running state and player's position accordingly.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.handle_player_movement(event.key)

    def handle_player_movement(self, key: int) -> None:
        """
        Update the player's position based on key presses.
        The player moves in steps, meaning the player moves a fixed distance each time a key is pressed.
        The movement is restricted to ensure the player does not move off-screen.

        Args:
            key (int): The key that was pressed.
        """
        # Dictionary to map keys to movement vectors
        movement_directions = {
            pygame.K_LEFT: (-self.PLAYER_STEP, 0),
            pygame.K_a: (-self.PLAYER_STEP, 0),
            pygame.K_RIGHT: (self.PLAYER_STEP, 0),
            pygame.K_d: (self.PLAYER_STEP, 0),
            pygame.K_UP: (0, -self.PLAYER_STEP),
            pygame.K_w: (0, -self.PLAYER_STEP),
            pygame.K_DOWN: (0, self.PLAYER_STEP),
            pygame.K_s: (0, self.PLAYER_STEP)
        }

        if key in movement_directions:
            dx, dy = movement_directions[key]
            new_x = self.player_pos['x'] + dx
            new_y = self.player_pos['y'] + dy
            # Ensure the player does not move off-screen
            self.player_pos['x'] = max(0, min(self.SCREEN_WIDTH - self.PLAYER_SIZE, new_x))
            self.player_pos['y'] = max(0, min(self.SCREEN_HEIGHT - self.PLAYER_SIZE, new_y))

    def draw_player(self) -> None:
        """
        Draw the player at the current position on the screen.
        The player is represented as a rectangle.
        """
        pygame.draw.rect(self.screen, self.PLAYER_COLOR, (self.player_pos['x'], self.player_pos['y'], self.PLAYER_SIZE, self.PLAYER_SIZE))

    def run(self) -> None:
        """
        Main game loop that runs the game.
        Handles events, updates game state, and redraws the screen.
        """
        while self.running:
            self.handle_events()
            self.screen.fill(self.BACKGROUND_COLOR)
            self.draw_player()
            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()