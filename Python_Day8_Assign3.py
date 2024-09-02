def reverse_words(string):
  """Reverses the words in a string.

  Args:
    string: The input string.

  Returns:
    The string with words reversed.
  """

  words = string.split()
  reversed_words = words[::-1]
  return " ".join(reversed_words)

# Given string
string = "Deeptech Python Training"

# Reverse words
reversed_string = reverse_words(string)

# Print the result
print(reversed_string)

# Output:
# Training Python Deeptech
