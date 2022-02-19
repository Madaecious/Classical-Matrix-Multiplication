###################################################################################
# Implementation of Classical Matrix Multiplication
# Mark Barros - BID 013884117
# CS3310 - Design and Analysis of Algorithms
# Cal Poly Pomona: Spring 2021
###################################################################################


# These are imported modules. -----------------------------------------------------
import numpy as np
import time

# These are global variables. -----------------------------------------------------

start = 0       # start is the "time" when an iteration of
                # classicalMultiply begins.
finish = 0      # finish is the "time" when an iteration of
                # classicalMultiply ends.
period = 0      # period is the amount of time, in seconds, that
                # classicalMultiply took to complete an iteration.

# This generates an nxn matrix. ---------------------------------------------------

def matrixGenerator(n):
        return np.random.randint(100,999, size=(n, n))

# This iterates by rows of Matrix A. ----------------------------------------------

def classicalMultiply(matrixA, matrixB):

    result = [[0 for x in range(n)] for y in range(n)]
        
    for i in range(len(matrixA)): 
        for j in range(len(matrixB[0])): 
            for k in range(len(matrixB)): 
                result[i][j] += matrixA[i][k] * matrixB[k][j]

    return result

# This is the driver code. --------------------------------------------------------

if __name__ == '__main__':

    product = 0 
    n = 2               # n is both dimensions of each 2D array (matrix).

    # This is the output header.
    print("------------------------------------------------------")
    print("Mark Barros")
    print("Implementation of Classical Matrix Multiplication")
    print("CS3310 - Design and Analysis of Algorithms")
    print("Cal Poly Pomona: Spring 2021")
    print("------------------------------------------------------")

    # This loop provides the option of repeatedly performing matrix
    # multiplication (doubling the size of the matrices each time).
    while n <= 2:

        # This generates two randomly populated matrices.
        MatrixA = matrixGenerator(n)
        MatrixB = matrixGenerator(n)

        # This outputs to the console the matrices.
        print("Matrix A:")
        for row in MatrixA:
            print(*row)
        print("\nMatrix B:")
        for row in MatrixB:
            print(*row)
        
        # This multiplies the matrices and times the operation.
        start = time.perf_counter_ns()
        product = classicalMultiply(MatrixA, MatrixB)
        finish = time.perf_counter_ns()

        # This outputs to the console the product.
        print("\nProduct:")
        for row in product:
            print(*row)

        # This calculates the elapsed time in seconds.
        period = ((finish - start) * (10**-9))

        # This outputs to the console the length of the matrix sides in each
        # instance and the corresponding time it took to multiply them.
        print("------------------------------------------------------")
        print("Execution Time: For n = ", f'{n:1,}', "   t = ", f'{period:.3}')
        print("------------------------------------------------------")

        # This doubles the sides of the matrices to be multipied
        # after each iteration.
        n = 2 * n
# End of Script ###################################################################