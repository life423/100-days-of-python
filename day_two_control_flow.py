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
        self.PLAYER_STEP = 10  # Step size for the player's movement

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
        Listen for events such as quitting the game.
        Updates the running state accordingly.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def handle_player_movement(self, keys: pygame.key.ScancodeWrapper) -> None:
        """
        Update the player's position based on key presses.
        The player moves in steps, meaning the player moves a fixed distance each time a key is pressed.
        The movement is restricted to ensure the player does not move off-screen.

        Args:
            keys (pygame.key.ScancodeWrapper): The state of all keys.
        """
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.player_pos['x'] = max(0, self.player_pos['x'] - self.PLAYER_STEP)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.player_pos['x'] = min(self.SCREEN_WIDTH - self.PLAYER_SIZE, self.player_pos['x'] + self.PLAYER_STEP)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.player_pos['y'] = max(0, self.player_pos['y'] - self.PLAYER_STEP)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.player_pos['y'] = min(self.SCREEN_HEIGHT - self.PLAYER_SIZE, self.player_pos['y'] + self.PLAYER_STEP)

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
            keys = pygame.key.get_pressed()
            self.handle_player_movement(keys)
            self.screen.fill(self.BACKGROUND_COLOR)
            self.draw_player()
            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()