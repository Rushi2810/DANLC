# Function to divide two numbers
def div(num1, num2):
    """
    This function takes two parameters: num1 and num2.
    It returns the result of dividing num1 by num2.
    If num2 is zero, it handles the division by zero error.
    """
    try:
        result = num1 / num2  # Division operation
        return result
    except ZeroDivisionError:  # Handle division by zero
        return "Division by zero is not allowed."

# Calling the div function with two numbers
output = div(10, 2)

# Display the result
print("The result of division is:", output)

# Output:
# The result of division is: 5.0
