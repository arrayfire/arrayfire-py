median
======
The af.median() function in ArrayFire computes the median value of elements in an array or along a specified dimension. The median is a measure of central tendency that provides a robust statistic by identifying the middle value in a sorted list of numbers.

Function
--------
:literal:`af.median()`
    - Python interface used to compute the median value of elements in an array or specified dimension.

Detailed Description
--------------------
The 'af.median()' function finds the median value of elements in the input array. The median is defined as the middle value in a sorted sequence of numbers. If the number of elements is even, it is the average of the two middle numbers. The function can compute the median over the entire array or along a specified dimension.

Function Documentation
----------------------
.. sidebar:: af.median()

    Syntax:
        af.median(array)

    
    Parameters:
        'array': The ArrayFire array for which the median is to be computed.

    Returns:
        An ArrayFire array containing the median values. If 'axis' is specified, the result will have the specified dimension reduced.

