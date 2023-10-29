# Name: Jakob West
# Class: CS 2300-001
# Due: Friday, October 27th @ 11:59 PM
# Assignment: Programming Assignment #2 Part A - Cryptography

import numpy as np


# FUNCTIONS!!! 

# Converts the string of text into its hexadecimal-unicode equivalent
def text_to_unicode_hex(text):
    unicode_hex = [hex(ord(char))[2:] for char in text]
    return unicode_hex


# Converts a list of unicode-hexadecimal into its a numpy array equivalent with
# 4 columns of decimal numbers 
def unicode_hex_to_decimal(input_list):
    
    # Convert Unicode-hex numbers to decimal values
    decimal_values = [int(hex_str, 16) for hex_str in input_list]

    # Determine the number of rows needed to have 4 columns
    num_columns = 4
    num_rows = (len(decimal_values) + num_columns - 1) // num_columns

    # Calculate the total number of elements needed to fill the matrix
    total_elements = num_rows * num_columns

    # Fill in the remaining slots with zeros
    while len(decimal_values) < total_elements:
        decimal_values.append(0)

    # Reshape the list into a numpy matrix with 4 columns
    matrix = np.array(decimal_values).reshape(num_rows, num_columns)

    return matrix


# Converts a numpy matrix back into a string of text
def numpy_matrix_to_text(matrix):
    num_rows, num_columns = matrix.shape  # Get the dimensions of the matrix
    text_values = []

    for col in range(num_columns):
        for row in range(num_rows):
            value = matrix[row, col] # Convert each element to an integer

            if (value == 51):
                value += 1
                
            if (value != 0 & value != 1): 
                text_values.append(str(value))

    # Join the list of values into a single string with spaces
    text_string = ' '.join(text_values)
    
    return text_string


# Converts ASCII values back to characters
def ascii_to_characters(input_str):
    # Split the input string into a list of ASCII values
    ascii_values = input_str.split()

    # Convert each ASCII value to a character and join them
    characters = ''.join([chr(int(ascii_value)) for ascii_value in ascii_values])

    return characters



# Part A1.1: The invertible endcoding matrix - Matrix A

A = np.array ([
    [1, -1, -1, 1],
    [2, -3, -5, 4],
    [-2, -1, -2, 2],
    [3, -3, -1, 2]
])


print("Welcome to Part A of Programming Assignment #2 in CS 2300!\n", end='\n')
print("\nHere are the answers to Part A2.1\n", end='\n')

# Open the file for reading
with open("input-A21.txt", "r") as file:
    password = file.read()


# Part A1.2: Encrypting the message - Matrix B
unicode_hex_list = text_to_unicode_hex(password)
encrypted_matrix = unicode_hex_to_decimal(unicode_hex_list)

B_partA_21 = np.transpose(encrypted_matrix)

print("This is Matrix: B (Encrypting the message) --> ")
print(B_partA_21)

'''
Question #1: Why does this plaintext matrix have to be made up of column vectors of 4
elements?
*** Answer: In order to multiply matrices, the column size of the first matrix must
be the same as the row size of the second matrix, i.e, Matrix A has 4 rows and 4 columns
which means that Matrix B must have 4 rows, so the matrices can multiply properly. This
is a fundamental rule of multiplying matrices!!!

1st Matrix ---> (nx4) * (4xm) <-- 2nd Matrix --- where n and m are all real numbers

'''


# encode the message - Cipher Matrix C
C_partA_21 = np.dot(A, B_partA_21) # Matrix A * Matrix B
print("\nThis is Matrix: C (Encode the message) --> ")
print(C_partA_21)
print()



print("\nHere are the answers to Part A2.2\n", end='\n')

# Part A1.4 The inverse of Matrix A - Used for decrypting the message
A_inv = np.linalg.inv(A)

# Read the numbers from the input file
with open("input-A22.txt", "r") as file:
    numbers = [int(num) for num in file.read().split()]

# Determine the number of rows needed to have 4 columns
num_columns = 4
num_rows = (len(numbers) + num_columns - 1) // num_columns

# Calculate the total number of elements needed to fill the matrix
total_elements = num_rows * num_columns

# Fill in the remaining slots with zeros
while len(numbers) < total_elements:
    numbers.append(0)

# Reshape the list into a numpy matrix with 4 columns
matrix = np.array(numbers).reshape(num_rows, num_columns)


# Encrypting the matrix - Matrix B
B_partA_22 = np.transpose(matrix)

# Print the resulting matrix
print("This is Matrix: B (Part A2.2) --> ")
print(B_partA_22)


# Create a cipher Matrix from the file matrix
C_partA_22 = np.dot(A, B_partA_22) # Matrix A * Matrix B
print("\nThis is Matrix: C (Encode the message) --> ")
print(C_partA_22)


# Decoding/Decrypting the message
resulting_matrix = np.dot(A_inv, C_partA_22)
resulting_matrix = resulting_matrix.astype(int)

string_numbers = numpy_matrix_to_text(resulting_matrix)

final_string = ascii_to_characters(string_numbers)

# Export the result to a new text file
with open("output-A22.txt", "w") as file:
    file.write(final_string)

print("\n" + final_string, end='\n')
print("Result has been saved to 'output-A22.txt'")


# End of Part A of Programming Assignment #2 - CS2300
