ones
====
The 'af.ones()' function in the ArrayFire library is used to create arrays where every element is initialized to one. This function is useful for various numerical and scientific computing tasks where you need an array filled with ones, such as initializing weights in machine learning algorithms or setting up identity matrices.

Function
--------
:literal:`af.ones()`
    - Pyhton interface to create an array filled with ones.

Detailed Description
--------------------
The 'af.ones()' function creates an ArrayFire array in which all the elements are set to one. This function is versatile and can create arrays of different shapes and data types. By default, the function creates arrays with single precision floating-point numbers (float), but you can specify different data types as needed.

The dimensions of the array are specified as arguments to the function, allowing you to create both one-dimensional and multi-dimensional arrays.

Function Documentation
----------------------
.. sidebar:: af.ones()

    Syntax:
        af.ones(dim0, dim1)
        
    Parameters:
            'dim0, dim1': Integers representing the dimensions of the array. You can provide multiple dimensions to create multi-dimensional arrays. For instance, 'dim0' represents the number of rows, and 'dim1' represents the number of columns for a 2D array.
    Returns:
            An ArrayFire array with the specified dimensions and data type, where all elements are initialized to one.
