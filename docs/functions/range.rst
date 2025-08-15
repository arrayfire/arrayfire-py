range
=======
The 'af.range()' function in ArrayFire generates a multi-dimensional ArrayFire array of linear indices using the length of a dimension as a range, tiling the indices on the other dimensions.

Function
--------
:literal:`af.range()`
    - Python interface used to generate a range in one dimension while tiling other dimensions

Detailed Description
--------------------
The 'af.range()' function is used to generate array of a sequence of indices starting at 0 and ending at (exclusive) the size of the length of the dimension specified, then it is duplicated on the remaining dimensions specified by 'shape'.

Function Documentation
----------------------
.. sidebar:: af.range()

    Syntax:
        af.range(shape, tile_shape, dtype)
    
    Parameters:
        'shape': List of Integers specifying the dimensions for which the sequence of integers is generated.
        'axis': Integer from 0 to 3 (by default 0) specifying the dimension to use to generate the linear index range
        'dtype': type that will be used to store the value internally. For example, af.int64 for signed 64-bit integer, af.float32 for 32-bit floating-point, and af.float64 for 64-bit floating-point

    Returns:
        An ArrayFire array of linear indices along 'axis' with the dimensions of 'shape'


