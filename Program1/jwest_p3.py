# Name: Jakob West
# Class: CS 2300-001
# Due: Friday, September 22nd @ 11:59 PM
# Assignment: Programming Assignment #1 Part 3


# =====================================================
# Part 3 - Multiplying all possible matrix combinations
# =====================================================


# Multiply matrices function --> Used for C * D and D * C 
def multiply_matrices(matrix1, matrix2):
    
    if len(matrix1[0]) != len(matrix2):
        return None 

    
    result = []

    for i in range(len(matrix1)):
        row = []

        for j in range(len(matrix2[0])):
            dot_product = 0
            for k in range(len(matrix2)):
                dot_product += matrix1[i][k] * matrix2[k][j]

            row.append(dot_product)

        result.append(row)

    return result

# end multipy_matricies function



C = []
D = []
result_multiply = []


user_input = input("\nPlease enter the two matricies you would like to add"
      + " (separated by a space!):\n")

matricies = user_input.split()

if len(matricies) == 2:
    Matrix1, Matrix2 = matricies

    if (Matrix1 == "Mat3" and Matrix2 == "Mat4") | (Matrix1 == "Mat3"
                                                    and Matrix2 == "Mat4"):

        # Fill Matrix C
        file_name = "jwest_mat3.txt"
        with open(file_name, "r") as file:

            for line in file:

                elements = line.strip().split()
                row = [int(e) for e in elements]
                C.append(row)


        # Fill Matrix D
        file_name = "jwest_mat4.txt"
        with open(file_name, "r") as file:

            for line in file:

                elements = line.strip().split()
                row = [float(e) for e in elements]
                D.append(row)



        # Multiply Matrix C and D (order matters!)
        result_multiply = multiply_matrices(C, D)

        if result_multiply:

            file_name = "jwest_p3_out34.txt"

            with open(file_name, "w") as file:
                for row in result_multiply:
                    file.write("\t".join(map(str, row)) + "\n")

                
        else:
            print("Matrices cannot be multiplied due to "
                  + "incompatible dimensions.\n")


        # Multiplying Matrix D and C (order matters!)
        result_multiply = multiply_matrices(D,C)

        if result_multiply:

            file_name = "jwest_p3_out43.txt"

            with open(file_name, "w") as file:
                for row in result_multiply:
                    file.write("\t".join(map(str, row)) + "\n")

                
        else:
            print("Matrices cannot be multiplied due to "
                  + "incompatible dimensions.\n")

      
    else:
        print("\nThe entered matricies cannot be Multiplied!\n")

        
else:
    print("There seems to be an error with your input.\n"
          + "Please make sure to only enter two words.")


# End Assignment #1 Part 3
