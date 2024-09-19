import numpy as np

def create_matrix():
    """
    This function creates a 3x3 matrix with values ranging from 2 to 10.
    """
    matrix = np.arange(2, 11).reshape(3, 3)  # Create array with values from 2 to 10 and reshape into 3x3 matrix
    return matrix

# Example usage:
result = create_matrix()
print(f"3x3 matrix with values ranging from 2 to 10:\n{result}")

"""
Output:
3x3 matrix with values ranging from 2 to 10:
[[ 2  3  4]
 [ 5  6  7]
 [ 8  9 10]]
"""
