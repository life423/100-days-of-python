def bmi_calc_imperial(weight: float, height: float) -> float:
    """
    Calculate BMI using the imperial system.

    Args:
        weight (float): Weight in pounds.
        height (float): Height in inches.

    Returns:
        float: The calculated Body Mass Index (BMI).
    """
    return (weight * 703) / (height ** 2)

def convert_height_to_inches(feet: int, inches: int) -> float:
    """
    Convert height given in feet and inches to total inches.

    Args:
        feet (int): Height in feet.
        inches (int): Additional height in inches.

    Returns:
        float: Total height in inches.
    """
    return feet * 12 + inches

def main() -> None:
    """
    Main function to gather user input and calculate BMI.

    This function prompts the user for weight in pounds and height in feet and inches,
    converts the height to inches, calculates BMI using the imperial system, and prints the result.
    If the user enters invalid input, they are prompted to try again.
    """
    while True:
        try:
            user_input = {
                "weight": float(input("Enter your weight in pounds: ")),
                "feet": int(input("Enter your height (feet): ")),
                "inches": int(input("Enter your height (inches): "))
            }

            height: float = convert_height_to_inches(user_input["feet"], user_input["inches"])
            bmi_imperial: float = bmi_calc_imperial(user_input["weight"], height)
            print(f"Here is your BMI: {bmi_imperial:.2f}")
            break
        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()