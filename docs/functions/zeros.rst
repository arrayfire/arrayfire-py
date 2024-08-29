zeros
=====
The 'af.zeros()' function in the ArrayFire library is used to create arrays filled with zeros. This is a common operation when initializing arrays that will be updated or manipulated later in numerical computations. The function allows you to specify the dimensions and data type of the array, making it flexible for various use cases.

Function
--------
:literal:`af.zeros()`
    - Python interface to create array filled with zeros.

Detailed Description
--------------------
The 'af.zeros()' function creates an ArrayFire array where every element is initialized to zero. It is particularly useful when you need to allocate space for an array but want to ensure that all values start from zero. This is often used in numerical methods, data processing, and initialization of variables in scientific computing.

You can specify the dimensions of the array as well as its data type. By default, the function creates arrays with a single precision floating-point type (float), but you can specify other data types if needed.

Function Documentation
----------------------
.. sidebar:: af.zero()

    Syntax:
        af.zeros(dim0, dim1)
    
    Parameters:
        'dim0, dim1': Integers representing the dimensions of the array. You can specify multiple dimensions to create multi-dimensional arrays. For example, dim0 is the number of rows, and dim1 is the number of columns for a 2D array.
    Returns:
        An ArrayFire array with the specified dimensions and data type, where all elements are initialized to zero.


