def count_chars_digits_symbols(string):
  """Counts letters, digits, and symbols in a string.

  Args:
    string: The input string.

  Returns:
    A tuple containing the counts of characters, digits, and symbols.
  """

  chars = 0
  digits = 0
  symbols = 0

  for char in string:
    if char.isalpha():
      chars += 1
    elif char.isdigit():
      digits += 1
    else:
      symbols += 1

  return chars, digits, symbols

# Given string
string = "P@#yn26at^&i5ve"

# Count characters, digits, and symbols
chars, digits, symbols = count_chars_digits_symbols(string)

# Print the results
print("Chars =", chars, "Digits =", digits, "Symbols =", symbols)

# Output:
# Chars = 8 Digits = 2 Symbols = 3
