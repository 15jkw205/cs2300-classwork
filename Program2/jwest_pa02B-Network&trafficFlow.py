# Name: Jakob West
# Class: CS 2300-001
# Due: Friday, October 27th @ 11:59 PM
# Assignment: Programming Assignment #2 Part B - Network/Traffic Flow

import numpy as np

# Function to perform Gauss-Jordan elimination
def gauss_jordan_elimination(A, B):
    n = len(A)

    # Augmenting the matrix A with the matrix B
    augmented_matrix = np.column_stack((A, B))

    for i in range(n):
        # Partial pivot
        pivot_row = i
        for j in range(i + 1, n):
            if abs(augmented_matrix[j][i]) > abs(augmented_matrix[pivot_row][i]):
                pivot_row = j
        augmented_matrix[[i, pivot_row]] = augmented_matrix[[pivot_row, i]]

        # Make the diagonal element 1
        diagonal_element = augmented_matrix[i][i]
        augmented_matrix[i] /= diagonal_element

        # Eliminate other rows
        for j in range(n):
            if j != i:
                factor = augmented_matrix[j][i]
                augmented_matrix[j] -= factor * augmented_matrix[i]

    return augmented_matrix[:, n:]

# Input values for Flow 1, Flow 2, Flow 3, Flow 4
flow_values = [400, 350, 800, 600]

# Coefficients of the linear equations
A = np.array([
    [1, 1, 0, 0],
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [0, 0, 1, 1]
], dtype=float)

# Solve the system of equations using Gauss-Jordan elimination
solutions = gauss_jordan_elimination(A, flow_values)

# Extract and display the desired solution (non-inf and non-negative)
desired_solution = None
for solution in solutions:
    if not np.isinf(solution[0]) and solution[0] >= 0:
        desired_solution = solution[0]
        break

if desired_solution is not None:
    print("Desired Solution (Flow 1):", desired_solution)
else:
    print("No valid solution found.")

    
# Output the resulting matrix (solutions)
print("Flow 1: ", solutions[0][0])
print("Flow 2: ", solutions[1][0])
print("Flow 3: ", solutions[2][0])
print("Flow 4: ", solutions[3][0])
