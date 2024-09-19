def count_occurrences(tuplex, value):
    """
    This function counts how many times a given value appears in a tuple.
    
    :param tuplex: tuple, the input tuple of elements
    :param value: int/float, the value to count
    :return: int, the number of occurrences of the value in the tuple
    """
    count = 0  # Initialize count
    
    for item in tuplex:  # Iterate through the tuple
        if item == value:  # Check if the current item matches the target value
            count += 1  # Increment count if a match is found
    
    return count

# Example usage:
tuplex = (2, 4, 5, 6, 2, 3, 4, 4, 7)
value_to_find = 4
occurrences = count_occurrences(tuplex, value_to_find)
print(f"Number of times {value_to_find} appears: {occurrences}")

"""
Output:
Number of times 4 appears: 3
"""
