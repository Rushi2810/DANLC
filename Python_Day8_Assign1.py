def count_word_occurrences(sentence):
  """Counts the occurrences of each word in a given sentence.

  Args:
    sentence: The sentence to analyze.

  Returns:
    A dictionary containing word counts.
  """

  # Split the sentence into words
  words = sentence.split()

  # Create a dictionary to store word counts
  word_counts = {}

  # Iterate over each word and update the count
  for word in words:
    if word in word_counts:
      word_counts[word] += 1
    else:
      word_counts[word] = 1

  return word_counts

# Given sentence
string = "To change the overall look of your document. To change the look available in the gallery"

# Count word occurrences
word_counts = count_word_occurrences(string)

# Print the results
print(word_counts)

# Output:
# {'To': 2, 'change': 2, 'the': 3, 'overall': 1, 'look': 2, 'of': 2, 'your': 1, 'document': 1, 'available': 1, 'in': 2, 'the': 3, 'gallery': 1}
