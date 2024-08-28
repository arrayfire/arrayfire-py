ifft
====
The 'af.ifft()' function in ArrayFire computes the inverse Fast Fourier Transform (IFFT) of an array. The IFFT is used to transform data from the frequency domain back to the time domain, which is crucial in many signal processing, image analysis, and scientific computing applications.

Function
--------
:literal:`af.ifft()`
    - Python interface used to compute the inverse Fast Fourier Transform of an array.

Detailed Description
--------------------
The 'af.ifft()' function performs an inverse discrete Fourier transform of the input array. It is essentially the reverse operation of the Fast Fourier Transform (FFT), converting frequency domain data back into the time domain.

Function Documentation
----------------------
.. sidebar:: af.ifft()

    Syntax:
        af.ifft(array, dim=None)
    
    Parameters:
        'array': The ArrayFire array (1D, 2D, or higher-dimensional) to which the inverse FFT is to be applied.
        'dim (optional)'': The dimension along which to compute the inverse FFT. If not specified, the IFFT is computed along all dimensions.

    Returns:
        An ArrayFire array of the same shape as the input array containing the result of the inverse FFT.

