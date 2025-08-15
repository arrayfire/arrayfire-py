gemm
======
The 'af.matmul()' function in ArrayFire performs general matrix multiplication. General Matrix multiplication is a fundamental operation in linear algebra and is widely used in various neural networks, scientific and engineering computations.

Function
--------
:literal:`af.gemm()`
    - Python interface used to perform general matrix multiplication

Detailed Description
--------------------
The af.gemm() function computes the general matrix product of various input arrays. General Matrix multiplication is defined for three matrices A, B, C and two scalars alpha and beta as the operation alpha * A * B + beta * C where the number of columns in A is equal to the number of rows in B, while C has the same number of columns as B and same number of rows as A. The result is that is a weighted average of the matrix multiplication between A and B, and the accumulator matrix C.

Function Documentation
----------------------
.. sidebar:: af.gemm()

    Syntax:
        af.matmul(A, B, alpha=alpha, beta=beta, accum=C, lhs_opts=lhs_opts, rhs_opts=rhs_opts)

    Parameters:
        'A': The first input array (matrix) to be multiplied.
        'B': The second input array (matrix) to be multiplied.
        'alpha': scalar that will be multiplied with the matrix multiplication. If not specified, this is taken to be one and the output is the same as 'matmul'
        'beta': scalar that will be multiplied with the accumulator. If not specified, this is taken to be zero and the output is the same as 'matmul'
        'C': The accumulator input array that will be added to the matrix multiplication. If not specified, this behaves as array full of zeros and the output is the same as 'matmul'
        'lhs_opts': specifies any type of transpose operation should be executed on 'A' prior to the matrix multiplication
        'rhs_opts': specifies any type of transpose operation should be executed on 'B' prior to the matrix multiplication

    Returns:
        An ArrayFire array representing the result of the general matrix multiplication:
