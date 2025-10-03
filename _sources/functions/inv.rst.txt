inv
===
The 'af.inv()' function in ArrayFire computes the inverse of a square matrix. Matrix inversion is a fundamental operation in linear algebra with applications in solving systems of linear equations, optimization problems, and various computational tasks.

Function
--------
:literal:`af.inv()`
    - Python interface used to find inverse of a square matrix.

Detailed Description
--------------------
The af.inv() function calculates the inverse of a given square matrix. For a matrix 
𝐴, the inverse is denoted as 𝐴−1, and it satisfies the following property:

A⋅A−1=I
where I is the identity matrix. The matrix A must be square (i.e., the number of rows must be equal to the number of columns) for its inverse to exist.

Function Documentation
----------------------
.. sidebar:: af.inv()

    Syntax:
        af.inv(matrix)
    
    Parameters:
        'matrix:'' A 2D ArrayFire array representing the square matrix for which the inverse is to be computed. The matrix must be square.

    Returns:
        An ArrayFire array of the same shape as the input matrix, containing the inverse of the input matrix.

