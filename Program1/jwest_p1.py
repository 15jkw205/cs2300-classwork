# Name: Jakob West
# Class: CS 2300-001
# Due: Friday, September 22nd @ 11:59 PM
# Assignment: Programming Assignment #1 Part 1


# ====================================================
# Part 1 - Generate and wrtie out 4 matrices to files
# ====================================================

# 1st Output Matrix - Mat1 (columns first, rows second)

num_cols = 5 # first name - Jakob
num_rows = 4 # last name - West

array_2D = []
initial_val = 1
increment = 1


for j in range(num_cols):
    column = []
    
    for i in range(num_rows):
        column.append(initial_val)
        initial_val += increment

    array_2D.append(column)

    
file_name = "jwest_mat1.txt"

with open(file_name, "w") as file:
    for i in range(num_rows):
        for j in range(num_cols):
            file.write(str(array_2D[j][i]) + "\t")
            
        file.write("\n")


        
# 2nd Ouput Matrix - Mat2 (rows first, columns second)

array_2D = []
initial_val = 2
increment = 3


for i in range(num_rows):
    row = []
    
    for j in range(num_cols):
        row.append(initial_val)
        initial_val += increment

    array_2D.append(row)


file_name = "jwest_mat2.txt"

with open(file_name, "w") as file:
    for row in array_2D:
        file.write("\t".join(map(str, row)) + "\n")



# 3rd Output Matrix - Mat3

num_rows = 2
num_cols = 4
array_2D = []
initial_val = 10
increment = -2


for j in range(num_cols):
    column = []
    
    for i in range(num_rows):
        column.append(initial_val)
        initial_val += increment

    array_2D.append(column)

    
file_name = "jwest_mat3.txt"

with open(file_name, "w") as file:
    for i in range(num_rows):
        for j in range(num_cols):
            file.write(str(array_2D[j][i]) + "\t")
            
        file.write("\n")



# 4th Output Matrix - Mat4

num_rows = 4
num_cols = 2
array_2D = []
initial_val = -6.0
increment = 1.5


for i in range(num_rows):
    row = []
    
    for j in range(num_cols):
        row.append(initial_val)
        initial_val += increment

    array_2D.append(row)


file_name = "jwest_mat4.txt"

with open(file_name, "w") as file:
    for row in array_2D:
        file.write("\t".join(map(str, row)) + "\n")

    
# End Assignment #1 Part 1

