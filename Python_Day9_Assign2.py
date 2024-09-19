def remove_duplicates(input_string):
    # List to store the result with no duplicate characters
    result = []
    
    # Set to keep track of characters that have already been seen
    seen = set()

    # Loop through each character in the input string
    for char in input_string:
        # Add the character if it is not a duplicate or it is a space (preserving spaces)
        if char not in seen or char == ' ':
            result.append(char)
            if char != ' ':
                seen.add(char)

    # Join the list of characters into a final string and return it
    return ''.join(result)

# Test the function with the given input
input_string = "String and String Function"
output_string = remove_duplicates(input_string)

# Print the output after removing duplicate characters
print("Output:", output_string)

# Expected Output:
# Output: String and Function
