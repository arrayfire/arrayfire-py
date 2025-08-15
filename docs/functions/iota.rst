iota
=======
The 'af.iota()' function in ArrayFire generates a multi-dimensional ArrayFire array with values populated based on their linear index within the array, optionally tiling the result to create larger arrays. 

Function
--------
:literal:`af.iota()`
    - Python interface used to generate linear indices with optional tiling

Detailed Description
--------------------
The 'af.iota()' function is used to generate array of a sequence of indices starting at 0 and ending at (exclusive) the size of the 'shape' dimensions specified, filling the array in column major ordering to the 'shape' specified that it is then duplicated as specified by the 'tile_shape'.

Function Documentation
----------------------
.. sidebar:: af.iota()

    Syntax:
        af.iota(shape, tile_shape, dtype)
    
    Parameters:
        'shape': List of Integers specifying the dimensions for which the sequence of integers is generated.
        'tile_shape': List of integers specifying the number of times the indices should be tiled in each dimension.
        'dtype': type that will be used to store the value internally. For example, af.int64 for signed 64-bit integer, af.float32 for 32-bit floating-point, and af.float64 for 64-bit floating-point

    Returns:
        An ArrayFire array of linear indices with the dimensions 'shape * tile_shape'

