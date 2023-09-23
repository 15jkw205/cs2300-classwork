# Name: Jakob West
# Class: CS 2300-001
# Due: Friday, September 22nd @ 11:59 PM
# Assignment: Programming Assignment #1 Part 4


# ======================================================
# Part 4 - Adding & Multiplying matrices using libraries
# ======================================================

import numpy as np


# fill Matrix A using numpy
file_name = "jwest_mat1.txt"
A = np.loadtxt(file_name)


# fill Matrix B using numpy
file_name = "jwest_mat2.txt"
B = np.loadtxt(file_name)


# fill Matrix C using numpy
file_name = "jwest_mat3.txt"
C = np.loadtxt(file_name)


# fill Matrix D using numpy
file_name = "jwest_mat4.txt"
D = np.loadtxt(file_name)



# Adding A and B
result = A + B
file_name = "jwest_p4_outA12.txt"

with open(file_name, "w") as file:
    for row in result:
        file.write("\t".join(map(str, row)) + "\n")



# Multiplying C by D
result = C @ D
file_name = "jwest_p4_outM34.txt"

with open(file_name, "w") as file:
    for row in result:
        file.write("\t".join(map(str, row)) + "\n")


# Multiplying D by C
result = D @ C
file_name = "jwest_p4_outM43.txt"

with open(file_name, "w") as file:
    for row in result:
        file.write("\t".join(map(str, row)) + "\n")


# End Assignment #1 Part 4
