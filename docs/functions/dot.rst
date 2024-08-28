dot
===
The 'af.dot()' function in ArrayFire computes the dot product of two arrays. This function is used for calculating the scalar product of two vectors or the matrix multiplication when applied to matrices. It is a fundamental operation in linear algebra with applications in various fields such as machine learning, physics, and numerical computing.

Function
--------
:literal:`af.dot()`
    - Python interface to compute dot product of two arrays.

Detailed Description
--------------------
The af.dot() function computes the dot product, which can refer to different operations depending on the type of input:

**Dot Product of Two Vectors:** For 1D arrays (vectors), the function calculates the scalar product. This is the sum of the products of corresponding elements of the vectors.

**Matrix Multiplication:** For 2D arrays (matrices), it performs matrix multiplication, which is also referred to as the dot product in this context.

Function Documentation
----------------------
.. sidebar:: af.dot()

    Syntax:
        af.dot(array1, array2)
    
    Parameters:
        'array1': The first ArrayFire array (vector or matrix) in the dot product operation.
        'array2': The second ArrayFire array (vector or matrix) in the dot product operation. Must be compatible with 'array1' for dot product or matrix multiplication.

    Returns:
        - For vectors: A scalar value representing the dot product of the vectors.
        - For matrices: An ArrayFire array representing the result of matrix multiplication.