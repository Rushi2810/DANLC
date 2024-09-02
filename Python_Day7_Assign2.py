def is_armstrong_number(number):
  """Checks if a number is an Armstrong number.

  Args:
    number: The number to check.

  Returns:
    True if the number is an Armstrong number, False otherwise.
  """

  original_number = number
  num_digits = len(str(number))
  sum_of_powers = 0

  while number > 0:
    digit = number % 10
    sum_of_powers += digit ** num_digits
    number //= 10

  return original_number == sum_of_powers

# Get input from the user
number = int(input("Enter a number: "))

# Check if the number is an Armstrong number
if is_armstrong_number(number):
  print(number, "is an Armstrong number.")
else:
  print(number, "is not an Armstrong number.")

# Example output:
# If the user enters 153, the output will be:
# 153 is an Armstrong number.

# If the user enters 125, the output will be:
# 125 is not an Armstrong number.
