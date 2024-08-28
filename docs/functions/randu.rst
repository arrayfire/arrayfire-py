randu
=====
The af.randu() function in ArrayFire is used to generate arrays with uniformly distributed random numbers. The numbers are drawn from a uniform distribution in the interval 
[0,1). This function is useful for initializing random data for simulations, stochastic processes, or for testing algorithms that require random inputs.

Function
--------
:literal:`af.randu()`
    - Python interface for making a rray with random units.

Detailed Description
--------------------
The 'af.randu()' function creates an ArrayFire array filled with random numbers that follow a uniform distribution between 0 and 1 (excluding 1). This function allows you to specify the dimensions of the array and optionally the data type. By default, the generated numbers are single-precision floating-point values (float), but other data types can be specified if needed.

Random number generation is a fundamental aspect of many computational tasks, and 'af.randu()' provides an efficient way to create random datasets with uniform distribution.

Function Documentation
----------------------
.. sidebar:: af.randu()

    Syntax:
        af.randu(dim0, dim1)
    
    Parameters:
        'dim0, dim1': Integers representing the dimensions of the array. You can provide multiple dimensions to create multi-dimensional arrays. For example, dim0 represents the number of rows, and dim1 represents the number of columns for a 2D array.

    Returns:
        An ArrayFire array with the specified dimensions and data type, where all elements are initialized with random values uniformly distributed between 0 and 1.

