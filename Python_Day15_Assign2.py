def symmetric_difference(set1, set2):
    """
    This function returns the symmetric difference of two sets.
    The symmetric difference contains elements that are in either set1 or set2, but not in both.
    """
    return set1.symmetric_difference(set2)  # Use symmetric_difference() to get unique items in either set

# Example usage:
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
result = symmetric_difference(set1, set2)
print(f"Symmetric difference of set1 and set2: {result}")

"""
Output:
Symmetric difference of set1 and set2: {20, 70, 10, 60}
"""
