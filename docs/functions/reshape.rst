reshape
=======
The 'af.reshape()' function in ArrayFire is used to change the shape of an array. This function allows you to rearrange the dimensions of an array while keeping the underlying data intact. It is particularly useful for preparing data for operations that require specific shapes or for transforming data between different formats.

Function
--------
:literal:`af.reshape()`
    - Python interface used to change the shape of an array.

Detailed Description
--------------------
The 'af.reshape()' function changes the shape of an existing array to a new shape specified by the user. The total number of elements in the original array must match the total number of elements in the reshaped array. The function does not alter the data but reinterprets it under a new shape.

Function Documentation
----------------------
.. sidebar:: af.reshape()

    Syntax:
        af.reshape(array,*new_shape)    
        
    Parameters:
        'array': The ArrayFire array to be reshaped.
        '*new_shape': The new shape for the array, specified as a sequence of integers. The product of these dimensions must equal the total number of elements in the original array.
    Returns:
        An ArrayFire array with the specified new shape.