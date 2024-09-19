def calculate_mean(test_dict):
    """
    This function calculates the mean of the values in a dictionary.
    """
    total_sum = 0  # Initialize the sum of values
    count = 0  # Initialize the count of values

    # Iterate over the dictionary to sum the values and count them
    for value in test_dict.values():
        total_sum += value  # Add value to the total sum
        count += 1  # Increment the count for each value

    if count == 0:  # Avoid division by zero
        return "Error: No values to calculate mean."
    
    mean = total_sum / count  # Calculate mean
    return mean

# Example usage:
test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}
mean_value = calculate_mean(test_dict)
print(f"Mean of the dictionary values: {mean_value}")

"""
Output:
Mean of the dictionary values: 6.2
"""
