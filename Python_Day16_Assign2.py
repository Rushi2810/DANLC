import numpy as np

# Input list
my_list = [1, 2, 3, 4, 5]

# Convert to NumPy array
my_array = np.array(my_list)

# Display the array
print("Array:", my_array)  # Output: Array: [1 2 3 4 5]

# Display the first and last index
print("First index:", my_array[0])  # Output: First index: 1
print("Last index:", my_array[-1])  # Output: Last index: 5

# Multiply each element by 2
multiplied_array = my_array * 2

# Display the result
print("Array after multiplication by 2:", multiplied_array)  
# Output: Array after multiplication by 2: [ 2  4  6  8 10]
