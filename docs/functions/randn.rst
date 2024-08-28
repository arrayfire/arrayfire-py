randn
=====
The 'af.randn()' function in the ArrayFire library is used to generate arrays filled with random numbers drawn from a normal (Gaussian) distribution with mean 0 and standard deviation 1. This is useful in statistical simulations, machine learning, and other applications where normally distributed random values are required.

Function
--------
:literal:`af.python()`
    - Python interface to form an array filled with numbers.

Detailed Description
--------------------
The 'af.randn()' function creates an ArrayFire array where each element is a random number sampled from a standard normal distribution, also known as a Gaussian distribution. The distribution has a mean of 0 and a standard deviation of 1. This function allows you to specify the dimensions of the array and optionally the data type. By default, the function generates numbers in single precision floating-point format (float), but other data types can be specified if needed.

Function Documentation
----------------------
.. sidebar:: af.randn()

    Syntax:
        af.randn(dim0, dim1)

    
    Parameters:
        'dim0, dim1': Integers representing the dimensions of the array. You can specify multiple dimensions to create multi-dimensional arrays. For example, dim0 represents the number of rows, and dim1 represents the number of columns for a 2D array.
    
    Returns:
        An ArrayFire array with the specified dimensions and data type, where all elements are initialized with random values sampled from a normal distribution with mean 0 and standard deviation 1.
