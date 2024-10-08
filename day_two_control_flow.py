def get_direction() -> str:
    full_directions = ["left", "right", "straight"]
    directions: dict[str, str] = {direction: direction[0] for direction in full_directions}

    while True:
        try:
            user_input = input("Which direction would you like to go? \n'left', 'right', 'straight', or 'quit' (or 'q') to exit: ")
            if user_input in ["quit", "q"]:
                print("You have exited the game.")
                return "quit"
            elif user_input in directions:
                return directions[user_input]
            else:
                raise ValueError("Invalid input. Please enter 'left', 'right', 'straight', or 'quit'.")
        except ValueError as e:
            print(e)


def handle_direction(direction: str) -> None:
    if direction != "quit":
        print(f"You chose direction: {direction}")


def main() -> None:
    direction: str = get_direction()
    handle_direction(direction)


if __name__ == "__main__":
    main()