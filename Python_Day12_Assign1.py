def sum_of_list(items):
    """
    This function takes a list of items (numbers) and returns the sum of all the items in the list.

    """
    total = sum(items)  # Use the built-in sum() function to calculate the total
    return total

# Example usage:
numbers = [1, 2, 3, 4, 5]  # List of numbers to sum
result = sum_of_list(numbers)
print(f"Sum of all items in the list: {result}")

"""
Output:
Sum of all items in the list: 15
"""
