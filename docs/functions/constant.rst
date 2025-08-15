constant
========
The 'af.constant()' function in the ArrayFire library is used to create arrays filled with a specific scalar value. This is a common operation when initializing arrays that will be updated or manipulated later in numerical computations. The function allows you to specify the dimensions and data type of the array, making it flexible for various use cases.

Function
--------
:literal:`af.constant()`
    - Python interface to create a multi-dimensional array filled with a constant value.

Detailed Description
--------------------
The 'af.constant()' function creates an ArrayFire array where every element is initialized to the scalar (integer, floating point, or complex) value specified. It is particularly useful when you need to allocate space for an array but want to ensure that all values start from zero. This is often used in numerical methods, data processing, and initialization of variables in scientific computing.

You can specify the dimensions of the array as well as its data type. By default, the function creates arrays with a single precision floating-point type (float), but you can specify other data types if needed.

Function Documentation
----------------------
.. sidebar:: af.constant()

    Syntax:
        af.constant(scalar, dims, dtype)
    
    Parameters:
        'scalar': value that will be used to initialize 
        'dims': List of integers representing the dimensions of the array. You can specify multiple dimensions to create multi-dimensional arrays. For example, dim0 is the number of rows, and dim1 is the number of columns for a 2D array, etc.
        'dtype': type that will be used to store the value internally. For example, af.int64 for signed 64-bit integer, af.float32 for 32-bit floating-point, and af.float64 for 64-bit floating-point

    Returns:
        An ArrayFire array with the specified dimensions and data type, where all elements are initialized to a scalar value.


