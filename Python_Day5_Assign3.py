import random  # Importing the random module to generate random numbers

# Generate 5 random numbers
random_numbers = [random.randint(1, 100) for _ in range(5)]

# Display the generated random numbers
print("Random numbers:", random_numbers)

# Find the maximum and minimum of the random numbers
max_num = max(random_numbers)  # Using max() to get the largest number
min_num = min(random_numbers)  # Using min() to get the smallest number

# Display the maximum and minimum numbers
print("Maximum number:", max_num)
print("Minimum number:", min_num)

# Output example (since numbers are random, output will vary):
# Random numbers: [45, 89, 12, 67, 23]
# Maximum number: 89
# Minimum number: 12
