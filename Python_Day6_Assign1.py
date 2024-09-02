def is_palindrome(number):
  """Checks if a number is a palindrome.

  Args:
    number: The number to check.

  Returns:
    True if the number is a palindrome, False otherwise.
  """

  original_number = number
  reversed_number = 0

  while number > 0:
    last_digit = number % 10
    reversed_number = (reversed_number * 10) + last_digit
    number //= 10

  return original_number == reversed_number

# Get input from the user
num = int(input("Enter a number: "))

# Check if the number is a palindrome
if is_palindrome(num):
  print(num, "is a palindrome.")
else:
  print(num, "is not a palindrome.")

# Output:
# If you enter 121, the output will be:
# 121 is a palindrome.

# If you enter 123, the output will be:
# 123 is not a palindrome.
