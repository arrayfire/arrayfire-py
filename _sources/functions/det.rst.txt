det
===
The 'af.det()' function in ArrayFire computes the determinant of a square matrix. The determinant is a scalar value that provides important properties of the matrix, such as whether it is invertible. It is a fundamental operation in linear algebra with applications in areas such as system of equations, matrix inversion, and eigenvalue problems.

Function
--------
:literal:`af.det()`
    - Python interface to find determinant of a square matrix.

Detailed Description
--------------------
The 'af.det()' function calculates the determinant of a square matrix. The matrix must be square, meaning the number of rows must be equal to the number of columns. The determinant of a matrix is a scalar that can provide information about the matrix, such as its invertibility. If the determinant is zero, the matrix is singular (non-invertible); if it is non-zero, the matrix is invertible.

Function Documentation
----------------------
.. sidebar:: af.det()

    Syntax:
        af.det(matrix)
    
    Parameters:
        'matrix': A 2D ArrayFire array (matrix) whose determinant is to be calculated. The matrix must be square, i.e., the number of rows must be equal to the number of columns.

    Returns:
        A scalar value representing the determinant of the input matrix. The type of the result will be the same as the input matrix data type.
