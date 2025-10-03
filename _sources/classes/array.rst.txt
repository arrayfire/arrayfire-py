Array
=====

The 'af.Array()' class provides a powerful framework for performing high-performance numerical computations. It is designed to create an ArrayFire array from various data structures, such as Python lists or other iterable collections.

Function
--------
:literal:`af.Array()`
    - Python interface to form an array.


Detailed Description
--------------------
The 'af.Array()' object allows you to convert a data structure, such as a Python list or tuple, into an ArrayFire array. This conversion is essential for leveraging ArrayFire's optimized computational capabilities. By creating an array from a list or another iterable, you can perform efficient mathematical operations, matrix manipulations, and other numerical computations using ArrayFire's APIs.

It supports multiple data types and can handle multi-dimensional arrays. The ability to create an ArrayFire array from native Python structures makes it easier to integrate ArrayFire into Python-based workflows.

Function Documentation
----------------------
.. sidebar:: af.Array()

    Syntax:
        af.Array(data)
    
    Parameters:
        'data': A list, tuple, or another iterable containing the elements to be converted into an ArrayFire array. The data should be in a format that ArrayFire can interpret, such as nested lists for multi-dimensional arrays.

    Returns:
        An ArrayFire array containing the elements from the input data structure.

.. autoclass:: arrayfire.Array
    :members:
    :undoc-members:
    :show-inheritance:



