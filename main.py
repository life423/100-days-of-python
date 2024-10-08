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

def main() -> None:
    """
    Main function to gather user input and calculate BMI.

    This function uses hardcoded values for weight and height,
    calculates BMI using the imperial system, and prints the result.
    """
    weight: float = 200 # pounds
    height: float = 73 #inches
  
    bmi_imperial: float = bmi_calc_imperial(weight, height)
    print(f"Here is your BMI {bmi_imperial:.2f}")

if __name__ == "__main__":
    main()