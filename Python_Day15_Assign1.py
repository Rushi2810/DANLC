def get_unique_items(set1, set2):
    """
    This function returns the unique items from two sets.
    It uses the union operation to combine the elements from both sets without duplicates.
    """
    return set1.union(set2)  # Use union() to get all unique items from both sets

# Example usage:
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
result = get_unique_items(set1, set2)
print(f"Unique items from both sets: {result}")

"""
Output:
Unique items from both sets: {70, 40, 10, 50, 20, 60, 30}
"""
