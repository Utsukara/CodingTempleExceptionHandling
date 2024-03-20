# 2. The Recipe Ratio Adjuster
# Objective: The aim of this assignment is to create a program that adjusts the quantities of a recipe based on the number of servings, handling any type of arithmetic errors or user input exceptions.

# Task 1: Start
# Ask the user for the number of servings the recipe is originally for and the number of servings they wish to make.

# Ensure that the user inputs are valid numbers and handle any ValueError that arises from improper input.

# Task 2: Quantity Calculation
# Calculate the adjustment factor by dividing the desired servings by the original servings.

# Use a try block to catch any arithmetic errors that may occur during the calculation.

# Task 3: Serving Success
# If the calculation is successful, display the adjusted recipe quantities to the user.

# Use a finally block to print a message encouraging the user to enjoy their cooking, regardless of the outcome of the calculation.


def adjust_recipe(original_servings, desired_servings, ingredients):
    try:
        original_servings = float(original_servings)
        desired_servings = float(desired_servings)

        if original_servings <= 0 or desired_servings <= 0:
            raise ValueError("Servings must be greater than 0.")

        adjustment_factor = desired_servings / original_servings
        adjusted_ingredients = [(quantity * adjustment_factor, description) for quantity, description in ingredients]

        return "\n".join([f"{quantity:.2f} {description}" for quantity, description in adjusted_ingredients]), "Enjoy your cooking!"
    except ValueError as e:
        return f"Error: {e}. Please enter valid numerical values.", None
    except ZeroDivisionError:
        return "Error: Original servings cannot be zero.", None
    except Exception as e:
        return f"Unexpected error: {e}", None
    finally:
        print("Try your best and I am sure it will taste great!")

ingredients = [
    (1, "tablespoon unsalted butter"),
    (0.5, "tablespoon extra-virgin olive oil"),
    (4, "3-ounce beef tenderloin medallions, pounded 3/4-inch thick"),
    (1, "small shallot, minced"),
    (1, "garlic clove, minced"),
    (0.25, "pound button mushrooms, sliced 1/4-inch thick"),
    (0.25, "cup Cognac or other brandy"),
    (2, "teaspoons Dijon mustard"),
    (0.25, "cup heavy cream"),
    (0.25, "cup veal demiglace"),
    (2, "teaspoons Worcestershire sauce"),
    (1, "tablespoon finely chopped scallions"),
    (1, "teaspoon finely chopped fresh flat-leaf parsley")
]

while True:
    original_servings = 2
    print(f"This recipe is originally meant to serve {original_servings} people.")
    desired_servings = input("Enter the number of servings you wish to make: ")

    result, message = adjust_recipe(original_servings, desired_servings, ingredients)
    if message:
        print(result)
        print(message)
        break  # Exit the loop if the calculation was successful
    else:
        print(result)
