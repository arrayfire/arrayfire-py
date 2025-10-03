mean
====
The 'af.mean()' function in ArrayFire computes the mean (average) value of elements in an array or along a specified dimension. It is a fundamental statistical operation used in various data analysis and processing tasks.

Function
--------
:literal:`af.mean()`
    - Python interface used to compute the average value of elements in an array or specified dimension.

Detailed Description
--------------------
The 'af.mean()' function calculates the average value of elements in the input array. The mean is computed by summing all elements and dividing by the number of elements. The function can compute the mean over the entire array or along a specified dimension.

Function Documentation
----------------------
.. sidebar:: af.mean()

    Syntax:
        af.mean(array)

    
    Parameters:
        'array': The ArrayFire array for which the mean is to be computed.

    Returns:
        An ArrayFire array containing the mean values. If 'axis' is specified, the result will have the specified dimension reduced.

