Array and Matrix Manipulation
=============================
ArrayFire provides several different methods for manipulating arrays and matrices. The functionality includes:

* moddims() - change the dimensions of an array without changing the data
* array() - create a (shallow) copy of an array with different dimensions.
* flat() - flatten an array to one dimension
* flip() - flip an array along a dimension
* join() - join up to 4 arrays
* reorder() - changes the dimension order within the array
* shift() - shifts data along a dimension
* tile() - repeats an array along a dimension
* transpose() - performs a matrix transpose
* T() - transpose a matrix or vector (shorthand notation)
* H() - Hermitian Transpose (conjugate-transpose) a matrix

Below we provide several examples of these functions and their use.

flat()
======
The **flat()** function flattens an array to one dimension:

.. literalinclude:: arrayandmatrixmanipulation.py 
    :language: python 
    :start-after: [manipulation1-snippet]
    :end-before: [manipulation1-endsnippet]

The **flat** function can be called from Python as follows:

.. admonition:: Function

   af.flat(array) - Python function for flattening an array

flip()
======
The **flip()** function flips the contents of an array along a chosen dimension. In the example below, we show the 5x2 array flipped along the zeroth (i.e. within a column) and first (e.g. across rows) axes:


.. literalinclude:: arrayandmatrixmanipulation.py 
    :language: python 
    :start-after: [manipulation2-snippet]
    :end-before: [manipulation2-endsnippet]

The **flip** function can be called from Python as follows:

.. admonition:: Function

   af.flip(array) - Python function for flipping an array


join()
======

The **join()** function joins arrays along a specific dimension. The C++ interface can join up to four arrays whereas the C interface supports up to 10 arrays. Here is an example of how to use join an array to itself:

.. literalinclude:: arrayandmatrixmanipulation.py 
    :language: python 
    :start-after: [manipulation3-snippet]
    :end-before: [manipulation3-endsnippet]


The **join** function can be called from Python as follows:

.. admonition:: Function

   af.join(0, array, array1) - Python function for joining arrays along a specified axis

moddims()
=========

The **moddims()** function changes the dimensions of an array without changing its data or order. Note that this function modifies only the metadata associated with the array. It does not modify the content of the array. Here is an example of moddims() converting an 8x1 array into a 2x4 and then back to a 8x1:

.. literalinclude:: arrayandmatrixmanipulation.py 
    :language: python 
    :start-after: [manipulation4-snippet]
    :end-before: [manipulation4-endsnippet]

The moddims function has a single form in the Python API:

.. admonition:: Function

   af.moddims(array, (3,2)) - Python function for modifying dimensions of an array


reorder()
=========
The **reorder()** function modifies the order of data within an array by exchanging data according to the change in dimensionality. The linear ordering of data within the array is preserved.

.. literalinclude:: arrayandmatrixmanipulation.py 
    :language: python 
    :start-after: [manipulation5-snippet]
    :end-before: [manipulation5-endsnippet]

shift()
=======
The **shift()** function shifts data in a circular buffer fashion along a chosen dimension. Consider the following example:


.. literalinclude:: arrayandmatrixmanipulation.py 
    :language: python 
    :start-after: [manipulation6-snippet]
    :end-before: [manipulation6-endsnippet]

The shift function can be called from Python as follows:
.. admonition:: Function

   af.shift(array, (3,2)) - Python function for shifting arrays along specified dimension

tile()
======
The **tile()** function repeats an array along the specified dimension. For example below we show how to tile an array along the zeroth and first dimensions of an array:

.. literalinclude:: arrayandmatrixmanipulation.py 
    :language: python 
    :start-after: [manipulation7-snippet]
    :end-before: [manipulation7-endsnippet]

.. admonition:: Function

   af.tile(array, (3,2)) - Python function that tiles arrays along specified dimensions


transpose()
===========
The **transpose()** function performs a standard matrix transpose. The input array must have the dimensions of a 2D-matrix.

.. literalinclude:: arrayandmatrixmanipulation.py 
    :language: python 
    :start-after: [manipulation8-snippet]
    :end-before: [manipulation8-endsnippet]

    
The python interface for transpose is as follows:

.. admonition:: Function

   af.transpose(array) - Python function to transpose matrix in place
        


array()
=======
**array()** can be used to create a (shallow) copy of a matrix with different dimensions. The total number of elements must remain the same. This function is a wrapper over the moddims() function discussed earlier.

