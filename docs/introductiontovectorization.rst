Introduction to Vectorization
=============================
Programmers and Data Scientists want to take advantage of fast and parallel computational devices. Writing vectorized code is necessary to get the best performance out of the current generation parallel hardware and scientific computing software. However, writing vectorized code may not be immediately intuitive. ArrayFire provides many ways to vectorize a given code segment. In this tutorial, we present several methods to vectorize code using ArrayFire and discuss the benefits and drawbacks associated with each method.

Generic/Default Vectorization
*****************************

By its very nature, ArrayFire is a vectorized library. Most functions operate on arrays as a whole – on all elements in parallel. Wherever possible, existing vectorized functions should be used opposed to manually indexing into arrays. For example consider the following code:

.. literalinclude:: introductiontovectorization.py 
    :language: python 
    :start-after: [vectorization1-snippet]
    :end-before: [vectorization1-endsnippet]

Although completely valid, the code is very inefficient as it results in a kernel kernels that operate on one datum. Instead, the developer should have used ArrayFire's overload of the + operator:

.. literalinclude:: introductiontovectorization.py 
    :language: python 
    :start-after: [vectorization2-snippet]
    :end-before: [vectorization2-endsnippet]

This code will result in a single kernel that operates on all 10 elements of :literal:`a` in parallel.

Most ArrayFire functions are vectorized. A small subset of these include:

+---------------------------------------+--------------------------------------------+
| Operator Category                     |         Functions                          |
+=======================================+============================================+
| Arithmetic Operations                 | +, -, \*, /, %, >, <                       |
+---------------------------------------+--------------------------------------------+
| Logical Operations                    | &&, ||(or), <, >, ==, != etc.              |
+---------------------------------------+--------------------------------------------+
| Numeric functions                     | abs(), floor(), round(), min(), max(), etc.|
+---------------------------------------+--------------------------------------------+
| Complex Operations                    | real(), imag(), conj(), etc.               |
+---------------------------------------+--------------------------------------------+
| Exponential and logarithmic functions | exp(), log(), expm1(), log1p(), etc.       |
+---------------------------------------+--------------------------------------------+
| Logical Operations                    | sin(), cos(), tan(), etc.                  |
+---------------------------------------+--------------------------------------------+
| Hyperbolic Functions                  | sinh(), cosh(), tanh(), etc.               |
+---------------------------------------+--------------------------------------------+

In addition to element-wise operations, many other functions are also vectorized in ArrayFire.

Notice that even that perform some form of aggregation (e.g. :literal:`sum()` or :literal:`min()`), signal processing (like :literal:`convolve()`), and even image processing functions (i.e. :literal:`rotate()`) all support vectorization on different columns or images. For example, if we have :literal:`NUM` images of size :literal:`WIDTH` by :literal:`HEIGHT`, one could convolve each image in a vector fashion as follows:

.. literalinclude:: introductiontovectorization.py 
    :language: python 
    :start-after: [vectorization3-snippet]
    :end-before: [vectorization3-endsnippet]


Similarly, one can rotate 100 images by 45 degrees in a single call using code like the following:

.. literalinclude:: introductiontovectorization.py 
    :language: python 
    :start-after: [vectorization4-snippet]
    :end-before: [vectorization4-endsnippet]

Although most functions in ArrayFire do support vectorization, some do not. Most notably, all linear algebra functions. Even though they are not vectorized linear algebra operations still execute in parallel on your hardware.

Using the built in vectorized operations should be the first and preferred method of vectorizing any code written with ArrayFire.

Batching
********
Consider the following example. Here we create a filter which we would like to apply to each of the weight vectors. The naive solution would be using a for-loop as we have seen previously:

.. literalinclude:: introductiontovectorization.py 
    :language: python 
    :start-after: [vectorization9-snippet]
    :end-before: [vectorization9-endsnippet]

However, as we have discussed above, this solution will be very inefficient. One may be tempted to implement a vectorized solution as follows:

.. literalinclude:: introductiontovectorization.py 
    :language: python 
    :start-after: [vectorization10-snippet]
    :end-before: [vectorization10-endsnippet]

However, the dimensions of :literal:`filter` and :literal:`weights` do not match, thus ArrayFire will generate a runtime error.

The correct solution is to use `batch operations with matmul <https://arrayfire.org/docs/group__blas__func__matmul.htm#gac061af289fcd39a07a3efba0f33fb17f>`_
By tiling on the third dimension, matmul is done in the first 2 dimensions and batched on the third to obtain the filtered weights:

.. literalinclude:: introductiontovectorization.py 
    :language: python 
    :start-after: [vectorization11-snippet]
    :end-before: [vectorization11-endsnippet]


Advanced Vectorization
**********************
We have seen the different methods ArrayFire provides to vectorize our code. Tying them all together is a slightly more involved process that needs to consider
data dimensionality and layout, memory usage, nesting order, etc. An excellent example and discussion of these factors can be found on our blog:
`How to write vectorized code <https://arrayfire.com/blog/how-to-write-vectorized-code/>`_ (Ignore GFOR section as it is not applicable to Python).
