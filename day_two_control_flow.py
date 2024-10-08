def get_direction() -> str:
    user_input = input("Which direction would you like to go? \n'left', 'right', or 'straight': ")
    
    while user_input not in ["right", "left", "straight"]:
        user_input = input("Invalid input. Please enter 'left', 'right', or 'straight': ")
    
    directions = {
        "left": "l",
        "right": "r",
        "straight": "s"
    }
    
    return directions[user_input]


def main() -> None:
    direction = get_direction()
    print(f"You chose direction: {direction}")
    

if __name__ == "__main__":
    main()