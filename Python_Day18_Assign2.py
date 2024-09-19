import numpy as np

# Employee data for full-time employees
full_time_employees = np.array([
    [101, 'John Doe', 'Full-Time', 55000],
    [102, 'Jane Smith', 'Full-Time', 60000],
    [103, 'Mike Johnson', 'Full-Time', 52000]
])

# Employee data for part-time employees
part_time_employees = np.array([
    [201, 'Alice Brown', 'Part-Time', 25000],
    [202, 'Bob Wilson', 'Part-Time', 28000],
    [203, 'Emily Davis', 'Part-Time', 22000]
])

# Combine full-time and part-time employee data
combined_employees = np.vstack((full_time_employees, part_time_employees))

# Print the combined dataset
print("Comprehensive Employee Dataset:")
print(combined_employees)

# Expected output:
# [['101' 'John Doe' 'Full-Time' '55000']
#  ['102' 'Jane Smith' 'Full-Time' '60000']
#  ['103' 'Mike Johnson' 'Full-Time' '52000']
#  ['201' 'Alice Brown' 'Part-Time' '25000']
#  ['202' 'Bob Wilson' 'Part-Time' '28000']
#  ['203' 'Emily Davis' 'Part-Time' '22000']]
