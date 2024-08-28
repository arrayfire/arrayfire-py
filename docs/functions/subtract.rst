subtract
========
The 'af.subtract()' function in ArrayFire is used to perform element-wise subtraction between two arrays or between an array and a scalar. This operation is fundamental in many computational tasks, including data manipulation, feature scaling, and mathematical operations.

Function
--------
:literal:`af.subtract()`
    - Python interface used to perform element-wise subtraction between two arrays or between an array and a scalar.

Detailed Description
--------------------
The 'af.subtract()' function subtracts the elements of one array from the corresponding elements of another array, or subtracts a scalar value from each element of an array. The function performs this operation element-wise, meaning that each element of the first operand is subtracted by the corresponding element of the second operand.

Function Documentation
----------------------
.. sidebar:: af.subtract()

    Syntax:
        af.subtract(array1, array2)
        af.subtract(array, scalar)

    Parameters:
        'array1': The ArrayFire array from which elements will be subtracted.
        'array2': The ArrayFire array to subtract from array1. This should have the same shape as array1 or be broadcast-compatible.
        'scalar': A scalar value to subtract from each element of array.

    Returns:
        An ArrayFire array containing the result of the subtraction.

