def find_largest_and_smallest(numbers):
    """
    This function takes a list of numbers and returns the largest and smallest number in the list.
    It does not use built-in functions like max() or min().

    """
    if len(numbers) == 0:
        return "Error: The list is empty."
    
    # Initialize largest and smallest to the first element in the list
    largest = smallest = numbers[0]
    
    # Iterate through the list starting from the second element
    for number in numbers[1:]:
        if number > largest:
            largest = number  # Update largest if current number is greater
        if number < smallest:
            smallest = number  # Update smallest if current number is smaller
    
    return largest, smallest

# Example usage:
numbers = [3, 5, 7, 2, 8, -1, 4, 10, -12]
largest, smallest = find_largest_and_smallest(numbers)
print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")

"""
Output:
Largest number: 10
Smallest number: -12
"""
