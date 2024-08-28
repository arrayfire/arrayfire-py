matmul
======
The 'af.matmul()' function in ArrayFire performs matrix multiplication between two arrays. Matrix multiplication is a fundamental operation in linear algebra and is widely used in various scientific and engineering computations.

Function
--------
:literal:`af.matmul()`
    - Python interface used to perform matrix multiplication between two arrays.

Detailed Description
--------------------
The af.matmul() function computes the matrix product of two input arrays. Matrix multiplication is defined for two matrices 𝐴 and 𝐵 where the number of columns in 𝐴 is equal to the number of rows in 𝐵. The result is a matrix where each element is computed as the dot product of rows of
𝐴 with columns of 𝐵.

Function Documentation
----------------------
.. sidebar:: af.matmul()

    Syntax:
        af.matmul(A, B)

    Parameters:
        'A': The first input array (matrix) to be multiplied.
        'B': The second input array (matrix) to be multiplied.

    Returns:
        An ArrayFire array representing the result of the matrix multiplication.
