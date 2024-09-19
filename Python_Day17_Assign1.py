import numpy as np

def create_special_array():
    """
    This function creates three arrays:
    - One array of 10 zeros
    - One array of 10 ones
    - One array of 10 fives
    """
    zeros_array = np.zeros(10)  # Create an array of 10 zeros
    ones_array = np.ones(10)    # Create an array of 10 ones
    fives_array = np.full(10, 5)  # Create an array of 10 fives

    result_array = np.concatenate([zeros_array, ones_array, fives_array])  # Concatenate the arrays
    return result_array

# Example usage:
result = create_special_array()
print(f"Array of 10 zeros, 10 ones, and 10 fives: \n{result}")

"""
Output:
Array of 10 zeros, 10 ones, and 10 fives: 
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 5. 5. 5. 5. 5. 5. 5. 5. 5. 5.]
"""
