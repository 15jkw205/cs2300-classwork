# Name: Jakob West
# Class: CS 2300-001
# Due: Friday, September 22nd @ 11:59 PM
# Assignment: Programming Assignment #1 Part 5


# =================================================================
# Part 5 - Finding all possible dot products and outputting to files
# =================================================================


# dot product of two matrices function --> r,s,u,v,w
def dot_product(matrix1, matrix2):
    if len(matrix1) != 2 or len(matrix2) != 2 or len(matrix1[0]) != 1 or len(matrix2[0]) != 1:
        raise ValueError("This function is for 2x1 matrices.")

    result = [[0]]

    for i in range(2):
        result[0][0] += matrix1[i][0] * matrix2[i][0]

    return result

#end dot_product function



r = [[-1], [-2]]
s = [[-3], [3]]
u = [[2], [-1]]
v = [[3], [1]]
w = [[1], [3]]
result = 0


user_input = input("\nPlease enter two matrices to perform "
                   + "dot product on, the choices are r,s,u,v,w" 
                   "\n(separated by a space!): ")

matrices = user_input.split()

if len(matrices) == 2:
    Matrix1, Matrix2 = matrices

    # case rs
    if (Matrix1 == "r" and Matrix2 == "s") or (Matrix1 == "s" and Matrix2 == "r"):
       result = dot_product(r, s)
       result_str = str(result[0][0])

       file_name  = "jwest_p5_outrs.txt"

       with open(file_name, "w") as file:
           file.write(result_str)


    # case ru
    elif (Matrix1 == "r" and Matrix2 == "u") or (Matrix1 == "u" and Matrix2 == "r"):
        result = dot_product(r, u)
        result_str = str(result[0][0])

        file_name  = "jwest_p5_outru.txt"
       
        with open(file_name, "w") as file:
            file.write(result_str)


    # case rv
    elif (Matrix1 == "r" and Matrix2 == "v") or (Matrix1 == "v" and Matrix2 == "r"):
        result = dot_product(r, v)
        result_str = str(result[0][0])

        file_name  = "jwest_p5_outrv.txt"

        with open(file_name, "w") as file:
           file.write(result_str)


    # case rw
    elif (Matrix1 == "r" and Matrix2 == "w") or (Matrix1 == "w" and Matrix2 == "r"):
        result = dot_product(r, w)
        result_str = str(result[0][0])

        file_name  = "jwest_p5_outrw.txt"

        with open(file_name, "w") as file:
           file.write(result_str)


    # case su
    elif (Matrix1 == "s" and Matrix2 == "u") or (Matrix1 == "u" and Matrix2 == "s"):
        result = dot_product(s, u)
        result_str = str(result[0][0])

        file_name  = "jwest_p5_outsu.txt"

        with open(file_name, "w") as file:
           file.write(result_str)


    # case sv
    elif (Matrix1 == "s" and Matrix2 == "v") or (Matrix1 == "v" and Matrix2 == "s"):
        result = dot_product(s, v)
        result_str = str(result[0][0])

        file_name  = "jwest_p5_outsv.txt"

        with open(file_name, "w") as file:
           file.write(result_str)
        

    # case sw
    elif (Matrix1 == "s" and Matrix2 == "w") or (Matrix1 == "w" and Matrix2 == "s"):
        result = dot_product(s, w)
        result_str = str(result[0][0])

        file_name  = "jwest_p5_outsw.txt"

        with open(file_name, "w") as file:
           file.write(result_str)
        

    # case uv
    elif (Matrix1 == "u" and Matrix2 == "v") or (Matrix1 == "v" and Matrix2 == "u"):
        result = dot_product(u, v)
        result_str = str(result[0][0])

        file_name  = "jwest_p5_outuv.txt"

        with open(file_name, "w") as file:
           file.write(result_str)
        

    # case uw
    elif (Matrix1 == "u" and Matrix2 == "w") or (Matrix1 == "w" and Matrix2 == "u"):
        result = dot_product(u, w)
        result_str = str(result[0][0])

        file_name  = "jwest_p5_outuw.txt"

        with open(file_name, "w") as file:
           file.write(result_str)


    # case vw
    elif (Matrix1 == "v" and Matrix2 == "w") or (Matrix1 == "w" and Matrix2 == "v"):
        result = dot_product(v, w)
        result_str = str(result[0][0])

        file_name  = "jwest_p5_outvw.txt"

        with open(file_name, "w") as file:
           file.write(result_str)


    else:
        print("You have entered an invalid option. Please try again.\n")


else:
    print("There seems to be an error with your input.\n"
            + "Please make sure to only enter two words.")
   
    
# End Assignment #1 Part 5 
