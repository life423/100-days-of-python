def get_direction() -> str:
    directions: dict[str, str] = {
        "left": "l",
        "right": "r",
        "straight": "s"
    }

    while True:
        try:
            user_input = input("Which direction would you like to go? \n'left', 'right', 'straight', or 'quit' to exit: ")
            if user_input in ["quit", "q"]:
                print("You have exited the game.")
                return "quit"
            elif user_input in directions:
                return directions[user_input]
            else:
                raise ValueError("Invalid input. Please enter 'left', 'right', 'straight', or 'quit'.")
        except ValueError as e:
            print(e)


def main() -> None:
    direction: str = get_direction()
    if direction != "quit":
        print(f"You chose direction: {direction}")


if __name__ == "__main__":
    main()