exp
===
The 'af.exp()' function in ArrayFire computes the element-wise exponential of an array. This function calculates the exponential of each element in the input array, using the base of the natural logarithm (e ≈ 2.71828). It is commonly used in scientific computing, machine learning, and numerical analysis where exponential transformations are required.

Function
--------
:literal:`af.exp()`
    - Python interface used to compute the exponential of each element in an array.

Detailed Description
--------------------
The af.exp() function performs the exponential operation on each element of the input array. If 
𝑥 is an element in the array, then exp⁡(𝑥) computes 𝑒𝑥, where 𝑒 is the base of the natural logarithm.

This function supports:

- **Element-wise Operations:** Applying the exponential function to each element of the array independently.
- **Broadcasting:** Automatically handling arrays of different shapes for operations where applicable.

Function Documentation
----------------------
.. sidebar:: af.exp()

    Syntax:
        af.exp(array)
    
    Parameters:
        'array': An ArrayFire array (1D, 2D, or higher-dimensional) for which the exponential is to be computed.

    Returns:
        An ArrayFire array with the same shape as the input array, where each element is the exponential of the corresponding element in the input array.

