def read_file_line_by_line(filename):
    """Reads the content from a text file line by line.

    Args:
        filename: The name of the text file.
    """

    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("Error: File not found:", filename)

# file address
filename = "E:/Practicals/DANLC/ABC.txt"

# Read the content from the specified file
read_file_line_by_line(filename)

#Output:
#Hello world
