# 1. Exceptional Weather Forecast
# Objective: The aim of this assignment is to enhance your understanding of exception handling by creating a weather forecast application that gracefully handles unexpected user input and provides user-friendly error messages.

# Task 1: Start
# Begin by setting up a simple user input loop that asks the user to enter the temperature in Fahrenheit.

# Ensure that your program only accepts numerical input and provides a friendly error message if the user enters something that can't be converted to a number.

# Task 2: Temperature Conversion
# Write a function that converts the Fahrenheit temperature to Celsius. Remember that the formula is (Fahrenheit - 32) * 5/9.

# Use a try block to catch any potential errors during the conversion process, such as division by zero or overflow errors.

# Task 3: User Experience
# Implement an else block that prints the converted temperature in a user-friendly format.

# Add a finally block that thanks the user for using the weather forecast application, ensuring that this message is displayed regardless of whether an exception was caught or not.
# Task 1: Start
# I'll begin by setting up a simple user input simulation, since I cannot directly take user inputs here.
# For demonstration purposes, I'll simulate inputs as a list of values that might include both valid and invalid entries.
# Normally, you would use a loop with input() function in a real application.


# Task 2: Temperature Conversion
def convert_to_celsius(fahrenheit):
    while True:
        try:
        # Convert the input to float and calculate Celsius
         celsius = (fahrenheit - 32) * 5/9
        except ValueError:
        # Handle non-numeric input
            return "Error: Please enter a valid numerical temperature in Fahrenheit."
        except Exception as e:
        # Catch all other exceptions
            return f"Error: An unexpected error occurred - {e}"
        else:
            # If no exceptions, return the Celsius conversion
            return (f"{fahrenheit:.2f}°F is equal to {celsius:.2f}°C")
        finally:
            # Thank the user
            print("Thank you for using the weather forecast application.")

while True:
    fahrenheit = input("Enter a temperature in Fahrenheit: ")
    try:
        fahrenheit = float(fahrenheit)
    except ValueError:
        print("Error: Please enter a valid numerical temerature in Fahrenheit.")
    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")
    else:
        print(convert_to_celsius(fahrenheit))
        break