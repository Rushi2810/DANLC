def count_words_in_file(file_name):
    """
    This function counts the total number of words in the given file.
    """
    total_words = 0
    try:
        with open(file_name, 'r') as file:  # Open the file in read mode
            for line in file:  # Loop through each line in the file
                words = line.split()  # Split the line into words (separated by spaces)
                total_words += len(words)  # Count the number of words in the line
        print(f"Total number of words: {total_words}")  # Display the total word count
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
    return total_words

# Calling the function to count and display the number of words in 'ABC.txt'
count_words_in_file('ABC.txt')

"""
Output:
Total number of words: 11
"""
