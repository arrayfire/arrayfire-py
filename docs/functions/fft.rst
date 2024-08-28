fft
===
The 'af.fft()' function in ArrayFire computes the Fast Fourier Transform (FFT) of an array. The FFT is an efficient algorithm to compute the discrete Fourier transform (DFT) and its inverse. The function is used to transform signals from the time domain to the frequency domain, which is essential in signal processing, image analysis, and many other fields.

Function
--------
:literal:`af.fft()`
    - Python interface for transforming signals from the time domain to the frequency domain.

Detailed Description
--------------------
The 'af.fft()' function performs a discrete Fourier transform of the input array. The FFT is commonly used for:

- Signal Processing: Analyzing the frequency components of a signal.
- Image Processing: Transforming images to the frequency domain for various processing tasks.
- Numerical Analysis: Solving differential equations and other problems where Fourier methods are applicable.
The function supports:

- 1D FFT: Transforming 1D arrays (vectors).
- 2D FFT: Transforming 2D arrays (matrices).
- 3D FFT: Transforming 3D arrays (volumes).
- Multi-dimensional FFTs: Transforming arrays of higher dimensions.
The FFT can be computed along specified dimensions or all dimensions of the input array.

Function Documentation
----------------------
.. sidebar:: af.fft()

    Syntax:
        af.fft(array, dim=None, is_inverse=False)
    
    Parameters:
        - array: The ArrayFire array (1D, 2D, or higher-dimensional) to transform.
        - dim (optional): The dimension along which to compute the FFT. If not specified, the FFT is computed along all dimensions.
        - is_inverse (optional): A boolean flag indicating whether to compute the inverse FFT. If True, the function computes the inverse FFT; otherwise, it computes the forward FFT.

    Returns:
        An ArrayFire array of the same shape as the input array containing the FFT of the input array.

