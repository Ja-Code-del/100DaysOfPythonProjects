def calculate_bmi(weight: float, height: float) -> float:
    """
    Calculate the Body Mass Index (BMI) given weight and height.
    BMI = weight / (height ^ 2)
    """
    return weight / (height * height)


def get_diagnostic(bmi: float) -> str:
    """
    Get the diagnostic message based on the BMI value.
    Uses predefined BMI thresholds to determine the category and corresponding message.
    """
    # Define BMI thresholds for different categories
    BMI_THRESHOLDS = {
        'underweight': (None, 18.5),
        'normal': (18.5, 24.9),
        'overweight': (25, 29.9),
        'obesity': (30, None)
    }

    # Define diagnostic messages for each category
    DIAGNOSTICS = {
        'underweight': "Underweight, your BMI indicates that you are vulnerable to health problems",
        'normal': "You are of normal weight.\nYour BMI does not increase health risks",
        'overweight': "Warning, you are overweight.\nYour BMI indicates that you may be pre-obese",
        'obesity': "Your BMI indicates that you are obese.\nPlease consult a doctor as your health risk is increased"
    }

    # Determine the diagnostic based on the BMI value
    for category, (low, high) in BMI_THRESHOLDS.items():
        if (low is None or bmi >= low) and (high is None or bmi < high):
            return DIAGNOSTICS[category]

    return "Diagnostic not available"


def get_float_input(prompt: str) -> float:
    """
    Prompt the user for a float input with error handling.
    Repeats until a valid float is entered.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Input error. Please make sure to enter a valid number.")


def get_int_input(prompt: str) -> int:
    """
    Prompt the user for an integer input with error handling.
    Repeats until a valid integer is entered.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Input error. Please make sure to enter a valid integer.")


def main():
    """
    Main function to calculate and display BMI and diagnostic messages.
    Handles user inputs and loops to allow multiple calculations.
    """
    print("APP TO CALCULATE YOUR BODY MASS INDEX")

    while True:
        # Prompt for user age
        user_age = get_int_input("Please enter your age: ")

        if 18 <= user_age <= 65:
            # Prompt for weight and height
            user_weight = get_float_input("Ok, enter your weight in kilograms: ")
            user_height = get_float_input("And your height in meters: ")

            if user_height > 0 and user_weight > 0:
                # Calculate BMI and get diagnostic message
                user_bmi = calculate_bmi(user_weight, user_height)
                user_diagnostic = get_diagnostic(user_bmi)

                # Display results
                print(f"Your weight is: {user_weight} Kg")
                print(f"Your height is: {user_height} m")
                print(f"YOUR BMI IS {user_bmi:.2f} Kg/m²")
                print(user_diagnostic)
                print("Source: WHO")

                while True:
                    # Prompt to quit or restart
                    quit = input("Do you want to quit? Type 'yes'.\nTo try another test, type 'no': ").strip().lower()
                    if quit in ('yes', 'no'):
                        break
                    else:
                        print("Please type 'yes' or 'no'")

                if quit == 'yes':
                    break
            else:
                print("Error! Unable to calculate your BMI:\nMake sure no data is null")
        else:
            print("Sorry, your age must be between 18 and 65 years")


if __name__ == "__main__":
    main()
