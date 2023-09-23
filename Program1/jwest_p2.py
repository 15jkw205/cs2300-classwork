# Name: Jakob West
# Class: CS 2300-001
# Due: Friday, September 22nd @ 11:59 PM
# Assignment: Programming Assignment #1 Part 2


# ====================================================
# Part 2 - Adding all possible matrix combinations
# ====================================================


# Add matrices function --> Used for A + B
def add_matrices(matrix1, matrix2):
    
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return None


    result = []
    
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    return result

# end add_matricies function



A = []
B = []
result_add = []


user_input = input("\nPlease enter the two matricies you would like to add"
      + " (separated by a space!):\n")

matrices = user_input.split()

if len(matrices) == 2:
    Matrix1, Matrix2 = matrices

    if (Matrix1 == "Mat1" and Matrix2 == "Mat2") | (Matrix1 == "Mat2"
                                                    and Matrix2 == "Mat1"):

        # Fill Matrix A
        file_name = "jwest_mat1.txt"
        with open(file_name, "r") as file:
            
            for line in file:
        
                elements = line.strip().split()
                row = [int(e) for e in elements]
                A.append(row)



        # Fill Matrix B
        file_name = "jwest_mat2.txt"
        with open(file_name, "r") as file:
            
            for line in file:
        
                elements = line.strip().split()
                row = [int(e) for e in elements]
                B.append(row)
    


        # Add Matrix A and B (A + B or B + A) 
        result_add = add_matrices(A, B)

        if result_add:
            
            file_name = "jwest_p2_out12.txt"

            with open(file_name, "w") as file:
                for row in result_add:
                    file.write("\t".join(map(str, row)) + "\n")
                    
        
    else:
        print("\nThe entered matricies cannot be added!\n")

        
else:
    print("There seems to be an error with your input.\n"
          + "Please make sure to only enter two words.")

    
# End Assignment #1 Part 2
