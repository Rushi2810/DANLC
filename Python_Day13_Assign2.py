def concatenate_dicts(*dicts):
    """
    This function concatenates multiple dictionaries into a single dictionary.
    """
    new_dict = {}  # Initialize an empty dictionary

    # Iterate through each dictionary and update the new dictionary with its key-value pairs
    for d in dicts:
        new_dict.update(d)  # Add the key-value pairs from the current dictionary to new_dict

    return new_dict

# Example usage:
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

result = concatenate_dicts(dic1, dic2, dic3)
print(f"Concatenated dictionary: {result}")

"""
Output:
Concatenated dictionary: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""
