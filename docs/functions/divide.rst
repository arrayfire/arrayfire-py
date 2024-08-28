divide
======
The 'af.divide()' function in the ArrayFire library performs element-wise division of two arrays. This function allows you to divide one array by another, or to divide each element of an array by a scalar value. It supports operations on arrays of the same shape or on a scalar and an array.

Function
--------
:literal:`af.divide`
    - Python interface for dividing one array by another.

Detailed Description
--------------------
The af.divide() function is used to perform element-wise division of arrays or between an array and a scalar. This operation divides each element of the first array by the corresponding element of the second array, or divides each element of the array by the scalar value.

**Element-wise Division:** When dividing two arrays, the function performs the division for each corresponding element of the arrays.

**Scalar Division:** When dividing an array by a scalar, the function divides each element of the array by the scalar value.

The function handles broadcasting automatically when the dimensions of the arrays are compatible.

Function Documentation
----------------------
.. sidebar:: af.divide

    Syntax:
        af.divide(array1, array2)
        af.divide(array, scalar)

    
    Parameters:
        - array1: The first ArrayFire array (numerator) in the division operation.
        - array2: The second ArrayFire array (denominator) in the division operation. Must have the same shape as array1 or be a scalar.
        - array: The ArrayFire array to be divided by a scalar.
        - scalar: The scalar value used to divide each element of array.

    Returns:
        An ArrayFire array containing the results of the element-wise division. The resulting array will have the same shape as the input arrays.
