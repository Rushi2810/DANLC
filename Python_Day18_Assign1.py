import numpy as np

# Input temperatures
temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2])

# Identify days with hot or cold conditions
hot_days = np.where(temperatures > 35)[0]  # Days where temperature exceeds 35°C
cold_days = np.where(temperatures < 5)[0]  # Days where temperature drops below 5°C

print("Hot days (index):", hot_days)
print("Cold days (index):", cold_days)

# Expected output:
# Hot days (index): [2 5 9]  # Temperatures: 36.8°C, 38.7°C, 37.2°C
# Cold days (index): []       # No temperature below 5°C
