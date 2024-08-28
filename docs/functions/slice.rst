slice
=====
The 'af.slice()' function in ArrayFire is used to extract a subarray from a larger array by specifying the start and end indices along each dimension. This function is useful for accessing a portion of an array, which is essential for tasks such as data manipulation, cropping, and partitioning.

Function
--------
:literal:`af.slice()`
    - Python interface used to extract a subarray from a larger array by specifying the start and end indices along each dimension.

Detailed Description
--------------------
The 'af.slice()' function allows you to extract a contiguous subarray from the original array. You specify the starting and ending indices for each dimension to define the subarray. This function provides a way to access specific regions of multi-dimensional arrays efficiently.

Function Documentation
----------------------
.. sidebar:: af.slice()

    Syntax:
        af.slice(array, *start_indices, *end_indices)
    
    Parameters:
        'array': The ArrayFire array from which the subarray will be extracted.
        '*start_indices': A sequence of integers specifying the starting indices for each dimension.
        '*end_indices': A sequence of integers specifying the ending indices for each dimension.

    Returns:
        An ArrayFire array containing the extracted subarray.
