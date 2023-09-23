# Name: Jakob West
# Class: CS 2300-001
# Due: Friday, September 22nd @ 11:59 PM
# Assignment: Programming Assignment #1 Part 7


# =======================================================================
# Part 7 - Finding the Dot Product & Transposing matrices using libraries
# =======================================================================

import numpy as np

r = np.array([[-1], [-2]])
s = np.array([[-3], [3]])
u = np.array([[2], [-1]])
v = np.array([[3], [1]])
w = np.array([[1], [3]])


# fill Matrix A using numpy
file_name = "jwest_mat1.txt"
mat1 = np.loadtxt(file_name)


# fill Matrix B using numpy
file_name = "jwest_mat2.txt"
mat2 = np.loadtxt(file_name)


# fill Matrix C using numpy
file_name = "jwest_mat3.txt"
mat3 = np.loadtxt(file_name)


# fill Matrix D using numpy
file_name = "jwest_mat4.txt"
mat4 = np.loadtxt(file_name)



# calculating the dot product using numpy library

# case rs
result = np.dot(r.ravel(), s.ravel())
result_str = str(result)

file_name  = "jwest_p7_outDrs.txt"

with open(file_name, "w") as file:
    file.write(result_str)


# case ru
result = np.dot(r.ravel(), u.ravel())
result_str = str(result)

file_name = "jwest_p7_outDru.txt"

with open(file_name, "w") as file:
    file.write(result_str)


# case rv
result = np.dot(r.ravel(), v.ravel())
result_str = str(result)

file_name  = "jwest_p7_outDrv.txt"

with open(file_name, "w") as file:
    file.write(result_str)


# case rw
result = np.dot(r.ravel(), w.ravel())
result_str = str(result)

file_name  = "jwest_p7_outDrw.txt"

with open(file_name, "w") as file:
    file.write(result_str)


# case su
result = np.dot(s.ravel(), u.ravel())
result_str = str(result)

file_name  = "jwest_p7_outDsu.txt"

with open(file_name, "w") as file:
    file.write(result_str)


# case sv
result = np.dot(s.ravel(), v.ravel())
result_str = str(result)

file_name  = "jwest_p7_outDsv.txt"

with open(file_name, "w") as file:
    file.write(result_str)


# case sw
result = np.dot(s.ravel(), w.ravel())
result_str = str(result)

file_name  = "jwest_p7_outDsw.txt"

with open(file_name, "w") as file:
    file.write(result_str)


# case uv
result = np.dot(u.ravel(), v.ravel())
result_str = str(result)

file_name  = "jwest_p7_outDuv.txt"

with open(file_name, "w") as file:
    file.write(result_str)


# case uw
result = np.dot(u.ravel(), w.ravel())
result_str = str(result)

file_name  = "jwest_p7_outDuw.txt"

with open(file_name, "w") as file:
    file.write(result_str)


# case vw
result = np.dot(v.ravel(), w.ravel())
result_str = str(result)

file_name  = "jwest_p7_outDvw.txt"

with open(file_name, "w") as file:
    file.write(result_str)



# transposing the matrices using numpy library

# case r
transposed_matrix = r.T

file_name = "jwest_p7_outTr.txt"

with open(file_name, "w") as file:
    for row in transposed_matrix:
        file.write("\t".join(map(str, row)) + "\n")


# case s
transposed_matrix = s.T

file_name = "jwest_p7_outTs.txt"

with open(file_name, "w") as file:
    for row in transposed_matrix:
        file.write("\t".join(map(str, row)) + "\n")

        
# case u
transposed_matrix = u.T

file_name = "jwest_p7_outTu.txt"

with open(file_name, "w") as file:
    for row in transposed_matrix:
        file.write("\t".join(map(str, row)) + "\n")
        

# case v
transposed_matrix = v.T

file_name = "jwest_p7_outTv.txt"

with open(file_name, "w") as file:
    for row in transposed_matrix:
        file.write("\t".join(map(str, row)) + "\n")
        

# case w
transposed_matrix = w.T

file_name = "jwest_p7_outTw.txt"

with open(file_name, "w") as file:
    for row in transposed_matrix:
        file.write("\t".join(map(str, row)) + "\n")
        

# case mat1
transposed_matrix = mat1.T

file_name = "jwest_p7_outTmat1.txt"

with open(file_name, "w") as file:
    for row in transposed_matrix:
        file.write("\t".join(map(str, row)) + "\n")

# case mat2
transposed_matrix = mat2.T

file_name = "jwest_p7_outTmat2.txt"

with open(file_name, "w") as file:
    for row in transposed_matrix:
        file.write("\t".join(map(str, row)) + "\n")
        

# case mat3
transposed_matrix = mat3.T

file_name = "jwest_p7_outTmat3.txt"

with open(file_name, "w") as file:
    for row in transposed_matrix:
        file.write("\t".join(map(str, row)) + "\n")
        

# case mat4
transposed_matrix = mat4.T

file_name = "jwest_p7_outTmat4.txt"

with open(file_name, "w") as file:
    for row in transposed_matrix:
        file.write("\t".join(map(str, row)) + "\n")


# End Assignment #1 Part 7
