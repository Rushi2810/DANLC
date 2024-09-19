def read_file_line_by_line(file_name):
    """
    This function reads the content of a file line by line and displays each line on the screen.

    """
    try:
        with open(file_name, 'r') as file:  # Open file in read mode
            for line in file:  # Read each line in the file
                print(line.strip())  # Display line after removing any trailing newline or spaces
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")

# Calling the function to read and display contents of 'ABC.txt'
read_file_line_by_line('ABC.txt')

"""
Output:
Hello World
This is a test file.
Reading line by line.
"""
