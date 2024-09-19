def count_words_in_file(filename):
  """Counts the total number of words in a text file.

  Args:
    filename: The name of the text file.

  Returns:
    The total number of words in the file.
  """

  with open(filename, 'r') as file:
    content = file.read()
    words = content.split()
    return len(words)

# Count the words in "ABC.txt"
word_count = count_words_in_file("ABC.txt")

# Print the result
print("Total words in ABC.txt:", word_count)

#Output
#Total words in ABC.txt: 2
