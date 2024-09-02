def factorial(num):
  """Calculates the factorial of a given number using a while loop.

  Args:
    num: The number to calculate the factorial of.

  Returns:
    The factorial of the number.
  """

  if num < 0:
    return "Factorial of negative numbers is not defined."

  factorial = 1
  while num > 0:
    factorial *= num
    num -= 1

  return factorial

# Get input from the user
number = int(input("Enter a number: "))

# Calculate the factorial
result = factorial(number)

# Print the result
print("The factorial of", number, "is", result)

# Example output:
# If the user enters 5, the output will be:
# The factorial of 5 is 120
