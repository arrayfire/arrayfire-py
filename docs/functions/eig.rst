eig
===
The 'af.eig()' function in ArrayFire computes the eigenvalues and eigenvectors of a square matrix. This function is essential in linear algebra for analyzing matrices and is used in various applications including machine learning, physics, and numerical analysis.

Function
--------
:literal:`af.eig()`
    - Python interface for computing the eigenvalues and eigenvectors of a square matrix.

Detailed Description
--------------------
The 'af.eig()' function computes the eigenvalues and eigenvectors of a square matrix. For a given matrix 
A, eigenvalues and eigenvectors are defined such that:

𝐴𝑣 = 𝜆𝑣


where:
- λ represents an eigenvalue.
- v represents the corresponding eigenvector.
The function returns two arrays:
- An array containing the eigenvalues of the matrix.
- An array containing the eigenvectors of the matrix. Each column in this array corresponds to an eigenvector.

Function Documentation
----------------------
.. sidebar:: af.eig()

    Syntax:
        eigenvalues, eigenvectors = af.eig(matrix)
    
    Parameters:
        'matrix': A 2D ArrayFire array (matrix) for which eigenvalues and eigenvectors are to be computed. The matrix must be square (i.e., the number of rows must be equal to the number of columns).

    Returns:
        - eigenvalues: An ArrayFire array containing the eigenvalues of the input matrix.
        - eigenvectors: An ArrayFire array containing the eigenvectors of the input matrix. Each column of this array is an eigenvector corresponding to the eigenvalues.
