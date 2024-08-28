add
===
The 'af.add()' function in ArrayFire is used to perform element-wise addition between arrays. This function enables you to add corresponding elements of two arrays or an array and a scalar, resulting in a new array where each element is the sum of the respective elements from the input arrays or the scalar.


Function
--------
:literal:`af.add()`
    - Python interface used to perform element-wise addition.

Detailed Description
--------------------
The 'af.add()' function computes the sum of two arrays or an array and a scalar, element by element. When adding two arrays, both must have the same dimensions, or be broadcastable to a common shape. For array-scalar addition, the scalar value is added to each element of the array. This function is particularly useful for operations requiring element-wise arithmetic.

Function Documentation
----------------------
.. sidebar:: af.add()

    Syntax:
        af.add(array1, array2)
        af.add(array, scalar)
    
    Parameters:
        'array1': The first ArrayFire array in the addition operation.
        'array2': The second ArrayFire array with the same dimensions as 'array1', or compatible for broadcasting.
        'array': An ArrayFire array to which the scalar is added.
        'scalar': A scalar value to be added to each element of 'array'.
        
    Returns:
        An ArrayFire array containing the element-wise sum of the inputs.
