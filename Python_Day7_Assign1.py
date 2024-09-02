def is_palindrome(string):
  """Checks if a string is a palindrome.

  Args:
    string: The string to check.

  Returns:
    True if the string is a palindrome, False otherwise.
  """

  # Remove non-alphanumeric characters and convert to lowercase
  cleaned_string = ''.join(char.lower() for char in string if char.isalnum())

  # Reverse the cleaned string
  reversed_string = cleaned_string[::-1]

  # Compare the cleaned string with its reversed version
  return cleaned_string == reversed_string

# Get input from the user
string = input("Enter a string: ")

# Check if the string is a palindrome
if is_palindrome(string):
  print(string, "is a palindrome.")
else:
  print(string, "is not a palindrome.")

# Example output:
# If the user enters "racecar", the output will be:
# racecar is a palindrome.

# If the user enters "hello", the output will be:
# hello is not a palindrome.
