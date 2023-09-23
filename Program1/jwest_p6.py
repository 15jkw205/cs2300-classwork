# Name: Jakob West
# Class: CS 2300-001
# Due: Friday, September 22nd @ 11:59 PM
# Assignment: Programming Assignment #1 Part 6


# =========================================
# Part 6 - Transposing matrices from Part 1
# =========================================


# transpose matrix function --> Part 1 transposed
def transpose_matrix(matrix):
    
    num_rows = len(matrix)
    num_columns = len(matrix[0])

    # creates an empty matrix with swapped dimensions
    transposed_matrix = [[0 for _ in range(num_rows)] for _ in range(num_columns)]


    for i in range(num_rows):
        for j in range(num_columns):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix

# end transpose matrix function



mat1 = []
mat2 = []
mat3 = []
mat4 = []


# create mat1 matrix
file_name = "jwest_mat1.txt"

with open(file_name, "r") as file:
            
    for line in file:
        
        elements = line.strip().split()
        row = [int(e) for e in elements]
        mat1.append(row)


# create mat2 matrix
file_name = "jwest_mat2.txt"

with open(file_name, "r") as file:
            
    for line in file:
        
        elements = line.strip().split()
        row = [int(e) for e in elements]
        mat2.append(row)


# create mat3 matrix
file_name = "jwest_mat3.txt"

with open(file_name, "r") as file:
            
    for line in file:
        
        elements = line.strip().split()
        row = [int(e) for e in elements]
        mat3.append(row)


# create mat4 matrix
file_name = "jwest_mat4.txt"

with open(file_name, "r") as file:
            
    for line in file:
        
        elements = line.strip().split()
        row = [float(e) for e in elements]
        mat4.append(row)



# transpose mat1 and output
mat1_T = transpose_matrix(mat1)

file_name = "jwest_p6_mat1.txt"

with open(file_name, "w") as file:
    for row in mat1_T:
        file.write("\t".join(map(str, row)) + "\n")


# transpose mat2 and output
mat2_T = transpose_matrix(mat2)

file_name = "jwest_p6_mat2.txt"

with open(file_name, "w") as file:
    for row in mat2_T:
        file.write("\t".join(map(str, row)) + "\n")


# transpose mat3 and output
mat3_T = transpose_matrix(mat3)

file_name = "jwest_p6_mat3.txt"

with open(file_name, "w") as file:
    for row in mat3_T:
        file.write("\t".join(map(str, row)) + "\n")


# transpose mat4 and output
mat4_T = transpose_matrix(mat4)

file_name = "jwest_p6_mat4.txt"

with open(file_name, "w") as file:
    for row in mat4_T:
        file.write("\t".join(map(str, row)) + "\n")

            
# End Assignment #1 Part 6 
