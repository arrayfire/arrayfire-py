join
====
The 'af.join()' function in ArrayFire is used to concatenate multiple arrays along a specified dimension. This operation is useful for combining data from different arrays into a single array, which can be particularly useful in data processing, machine learning, and numerical analysis.



Function
--------
:literal:`af.join`
    - Python interface used to concatenate multiple arrays along a specified dimension.

Detailed Description
--------------------
The 'af.join()' function allows you to concatenate multiple arrays along a specified dimension. The arrays being concatenated must have compatible shapes along all dimensions except for the dimension along which concatenation is performed.

Function Documentation
----------------------
.. sidebar:: af.join()

    Syntax:
        af.join(dim, \*arrays)
    
    Parameters:
        'dim': The dimension along which the arrays will be concatenated. This is an integer indicating the axis along which the join operation will take place.
        '\*arrays': The arrays to be concatenated. These can be 1D, 2D, or higher-dimensional arrays, and they must be compatible in all dimensions except the specified dimension.
    Returns:
        An ArrayFire array that is the result of concatenating the input arrays along the specified dimension.
