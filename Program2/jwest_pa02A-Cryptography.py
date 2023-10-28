# Name: Jakob West
# Class: CS 2300-001
# Due: Friday, October 27th @ 11:59 PM
# Assignment: Programming Assignment #2 Part A - Cryptography

import numpy as np

# Part A1.1: Set up the 4x4 coding matrix

A = np.array ([
    [1, -1, -1, 1],
    [2, -3, -5, 4],
    [-2, -1, -2, 2],
    [3, -3, -1, 2]
])


A_inv = np.linalg.inv(A)

# converts the string of text into its hexadecimal-unicode equivalent
def text_to_unicode_hex(text):
    unicode_hex = [hex(ord(char))[2:] for char in text]
    return unicode_hex


# Example usage:
text = "NCS-2014"
unicode_hex_list = text_to_unicode_hex(text)
print(unicode_hex_list)


# Part A1.2: Function to convert decimal value to character
def decimal_to_char(decimal):
    return chr(decimal)

# Part A1.2: Function to encode a plaintext message
def encode_message(message):
    encoded_message = []
    for char in message:
        decimal_value = char_to_decimal(char)
        encoded_vector = [decimal_value, 0, 0, 0]

        # Split the vector into 4-element column vectors
        while len(encoded_vector) > 0:
            encoded_message.append(encoded_vector[:4])
            encoded_vector = encoded_vector[4:]

    return encoded_message

# Part A1.3: Function to encode the message using matrix A
def cipher_matrix(A, B):
    encoded_matrix = []
    for i in range(len(B)):
        encoded_row = []
        for j in range(len(A[0])):
            sum = 0
            for k in range(len(A)):
                sum += A[i][k] * B[k][j]
            encoded_row.append(sum)
        encoded_matrix.append(encoded_row)

    return encoded_matrix

    return decoded_message

# Part A2.1: Accept user input for a plaintext message
plaintext = input("Enter a plaintext message: ")

# Part A2.1: Encode the message using matrix A
encoded_message = encode_message(plaintext)

# Part A2.2: Decode the message using the inverse of matrix A
A_inv = [
    [2, -3, -1, 3],
    [1, -3, -1, 3],
    [1, -5, -2, -1],
    [1, 4, 2, 2]
]

decoded_message = decode_message(encoded_message, A_inv)

# Part A2.2: Display the results
print("Encoded Message:", encoded_message)
print("Decoded Message:", "".join([decimal_to_char(decimal) for decimal in decoded_message]))


