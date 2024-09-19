def list_to_tuple(listx):
    """
    This function converts a list into a tuple.
    """
    return tuple(listx)  # Use the tuple() constructor to convert the list to a tuple

# Example usage:
listx = [5, 10, 7, 4, 15, 3]
result = list_to_tuple(listx)
print(f"Converted tuple: {result}")

"""
Output:
Converted tuple: (5, 10, 7, 4, 15, 3)
"""
