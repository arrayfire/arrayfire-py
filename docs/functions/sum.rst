sum
===
The 'af.sum()' function in ArrayFire computes the sum of the elements in an array. This function can perform the summation over all elements or along a specified dimension. It is useful for aggregating data, calculating totals, and summarizing results in numerical computations.

Function
--------
:literal:`af.sum()`
    - Python interface used to compute the sum of the elements in an array.

Detailed Description
--------------------
The 'af.sum()' function calculates the sum of array elements. You can choose to compute the sum across all elements of the array or along a specific dimension. This function supports both reducing the array to a single value and computing sums along specified axes.

Function Documentation
----------------------
.. sidebar:: af.sum()

    Syntax:
        af.sum(array)
    
    Parameters:
        'array': The ArrayFire array for which the sum will be computed.
        'dim': An optional integer specifying the dimension along which to compute the sum. By default, it is set to 0, which means the function will sum along the first dimension.
    
    Returns:
        An ArrayFire array containing the sum of the elements.
