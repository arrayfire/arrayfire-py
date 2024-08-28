max
===
The 'af.max()' function in ArrayFire is used to find the maximum value within an array or along a specific dimension. It can also return the indices of the maximum values if requested.



Function
--------
:literal:`af.max()`
    - Python interface used to find the maximum value within an array or specific dimension.

Detailed Description
--------------------
The af.max() function performs one of the following operations:

- Finds the maximum value in the entire array.
- Finds the maximum value along a specified dimension.
- Returns both the maximum values and their indices if requested.

Function Documentation
----------------------
.. sidebar:: af.max()

    Syntax:
       af.max(array)
    
    Parameters:
        'array': The ArrayFire array from which to find the maximum values.

    Returns:
        An ArrayFire array containing the maximum element from the input data structure.
