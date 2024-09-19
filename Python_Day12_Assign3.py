def find_duplicates(numbers):
    """
    This function takes a list of numbers and returns a list of duplicate values.
    """
    duplicates = []  # List to store duplicate values
    seen = set()  # Set to track seen numbers

    for number in numbers:
        if number in seen and number not in duplicates:
            duplicates.append(number)  # Add the number to duplicates if seen more than once
        else:
            seen.add(number)  # Add the number to seen set if it's encountered for the first time

    return duplicates

# Example usage:
numbers = [1, 2, 3, 2, 4, 5, 6, 4, 7, 8, 8]
duplicate_values = find_duplicates(numbers)
print(f"Duplicate values: {duplicate_values}")

"""
Output:
Duplicate values: [2, 4, 8]
"""
