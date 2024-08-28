multiply
========
The 'af.multiply()' function in ArrayFire performs element-wise multiplication between two arrays. This means each element of the first array is multiplied by the corresponding element of the second array. It supports both scalar and array inputs for flexible use.

Function
--------
:literal:`af.multiply()`
    - Python interface used to perform element-wise multiplication between two arrays.

Detailed Description
--------------------
The 'af.multiply()' function computes the product of two input arrays element-wise. If the inputs are arrays, they must have the same dimensions or be broadcastable to compatible dimensions. If one of the inputs is a scalar, it multiplies each element of the other array by that scalar.

Function Documentation
----------------------
.. sidebar:: af.multiply()

    Syntax:
        af.multiply(array1, array2)
        af.multiply(array, scalar)
        af.multiply(scalar, array)

    
    Parameters:
        'array1': The first input array.
        'array2': The second input array. Must have the same dimensions as array1 or be broadcastable to the dimensions of array1.
        'array': The input array if using scalar multiplication.
        'scalar': The scalar value to multiply with the array.

    Returns:
        An ArrayFire array containing the result of the element-wise multiplication.

