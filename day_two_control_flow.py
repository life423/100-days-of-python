# Day 2 of 100 Days of Code: Advanced Control Flow Logic Showcase

import random

# A function that categorizes random numbers using advanced control flow logic
def number_classification_game() -> None:
    """
    Classify numbers into multiple categories based on specific rules.
    Showcases nested if-else, match-case, and ternary operator.
    """
    print("\nWelcome to the Number Classification Game!\n")
    rounds = 5  # Number of rounds to generate random numbers
    
    for _ in range(rounds):
        num = random.randint(-100, 100)
        classification = ""

        # Using nested if-else to determine if a number is positive, negative, or zero
        if num > 0:
            classification += "Positive "
        elif num < 0:
            classification += "Negative "
        else:
            classification += "Zero"

        # Additional checks for even/odd using match-case
        if num != 0:
            match num % 2:
                case 0:
                    classification += "Even"
                case 1:
                    classification += "Odd"
                case -1:
                    classification += "Odd"

        # Prime number check using a custom function
        if num > 1:
            classification += " and Prime" if is_prime(num) else " and Not Prime"

        # Display results with conditional logic
        action = "Celebrate!" if num == 42 else "Keep going..."
        print(f"Number: {num} -> {classification}. {action}")

    print("\nGame over. Thanks for playing!\n")


def is_prime(num: int) -> bool:
    """
    Determines if a number is prime.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if num is a prime number, False otherwise.
    """
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


# Advanced control flow showcase with list comprehension and loop control
def control_flow_list_logic() -> None:
    """
    Demonstrates complex control flow by applying advanced rules to a list of numbers.
    """
    random_numbers = [random.randint(1, 100) for _ in range(10)]
    print("\nAdvanced List Logic:\n")
    print(f"Original List: {random_numbers}\n")

    # Filter out even numbers, then square them if they're greater than 50, else cube them
    transformed_numbers = [
        (x ** 2 if x > 50 else x ** 3) if x % 2 == 0 else "Skipped"
        for x in random_numbers
    ]
    
    # Display the transformation
    for idx, value in enumerate(transformed_numbers):
        print(f"Index {idx}: {'Transformed' if value != 'Skipped' else 'Skipped'} -> {value}")


if __name__ == "__main__":
    number_classification_game()
    control_flow_list_logic()