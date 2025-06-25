# Program to demonstrate try/except in Python

try:
    # Ask user to input two numbers
    num1 = int(input("Enter the numerator: "))
    num2 = int(input("Enter the denominator: "))

    # Perform division
    result = num1 / num2

    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

except ValueError:
    print("Error: Please enter valid integers.")

except Exception as e:
    print("An unexpected error occurred:", e)

finally:
    print("This block always runs (cleanup code if needed).")
