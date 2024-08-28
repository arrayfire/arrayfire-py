transpose
=========
The 'af.transpose()' function in ArrayFire is used to compute the transpose of a matrix or higher-dimensional array. Transposing a matrix involves swapping its rows and columns. This function is fundamental in linear algebra operations and many computational tasks.

Function
--------
:literal:`af.transpose()`
    - Python interface used to compute the transpose of a matrix or higher-dimensional array.

Detailed Description
--------------------
The 'af.transpose()' function computes the transpose of a given array. For 2D matrices, this means converting rows into columns and columns into rows. For higher-dimensional arrays, the function permutes dimensions according to the specified order.

Function Documentation
----------------------
.. sidebar:: af.transpose()

    Syntax:
        af.transpose(array, *permutation)
    
    Parameters:
        'array': The ArrayFire array to be transposed.
        '*permutation': An optional sequence of integers specifying the new order of dimensions. If not provided, the function defaults to transposing the last two dimensions.

    Returns:
        An ArrayFire array that is the transpose of the input array, with dimensions permuted according to the provided permutation.

