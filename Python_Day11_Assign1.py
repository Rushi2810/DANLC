def divide_numbers(num1, num2):
    """
    Function to divide two numbers and handle division by zero.
    """
    try:
        # Attempt to perform the division
        result = num1 / num2
    except ZeroDivisionError:
        # If a division by zero occurs, return an error message
        return "Error: Division by zero is not allowed."
    else:
        # If no exception occurs, return the result of the division
        return result

# Example usage
num1 = 10
num2 = 0

output = divide_numbers(num1, num2)
print(output)

# Output:
# Error: Division by zero is not allowed.
