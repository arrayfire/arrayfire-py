log
===
The 'af.log()' function in ArrayFire computes the natural logarithm (base 𝑒) of each element in the input array. This function is commonly used in mathematical and scientific computing for transformations, normalization, and statistical analysis.

Function
--------
:literal:`af.log()`
    - Python interface used to compute the natural logarithm of each base element in the input array.

Detailed Description
--------------------
The af.log() function applies the natural logarithm operation element-wise to the input array. The natural logarithm is the logarithm to the base 
𝑒, where 𝑒 is approximately equal to 2.71828. The function operates on each element of the array independently.

Function Documentation
----------------------
.. sidebar:: af.log()

    Syntax:
        af.log(array)
    
    Parameters:
        'array': An ArrayFire array (1D, 2D, or higher-dimensional) containing the values for which the natural logarithm is to be computed.
    
    Returns:
        An ArrayFire array of the same shape as the input array, with each element replaced by its natural logarithm.
