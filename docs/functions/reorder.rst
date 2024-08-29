reorder
=======
The 'af.reorder()' function in ArrayFire is used to rearrange the dimensions of an array. This is useful for changing the order of dimensions to align with the requirements of different operations or to facilitate certain types of computations.

Function
--------
:literal:`af.reorder()`
    - Python interface used to rearrange the dimensions of an array.

Detailed Description
--------------------
The 'af.reorder()' function changes the order of dimensions of the input array. It is often used in conjunction with other functions that require specific data layouts. Reordering dimensions can help optimize performance or compatibility with other libraries and tools.

Function Documentation
----------------------
.. sidebar:: af.reorder()

    Syntax:
        af.reorder(array, \*order)
    
    Parameters:
        'array': The ArrayFire array whose dimensions are to be reordered.
        '\*order': The new order of dimensions specified as a sequence of integers. Each integer represents the index of the dimension in the new order.

    Returns:
        An ArrayFire array with the dimensions reordered according to the specified order.

