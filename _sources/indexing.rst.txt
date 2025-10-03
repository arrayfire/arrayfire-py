Indexing
========
Indexing in ArrayFire is a powerful but easy to abuse feature of the af.Array class. This feature allows you to reference or copy subsections of a larger array and perform operations on only a subset of elements.

Indexing in ArrayFire can be performed using the parenthesis operator or one of the member functions of the af::array class. These functions allow you to reference one or a range of elements from the original array.

Here we will demonstrate some of the ways you can use indexing in ArrayFire and discuss ways to minimize the memory and performance impact of these operations.

Lets start by creating a new 4x4 matrix of floating point numbers:

.. literalinclude:: indexing.py
    :language: python 
    :start-after: [indexing1-snippet]
    :end-before: [indexing1-endsnippet]

ArrayFire is column-major so the resulting A array will look like this:

.. math::

   \begin{bmatrix}
   0 & 4 & 8 & 12 \\
   1 & 5 & 9 & 13 \\
   2 & 6 & 10 & 14 \\
   3 & 7 & 11 & 15
   \end{bmatrix}

In Python, for a two-dimensional array like a matrix, you can access its first element by providing the indices 0, 0 within the indexing operator of the af.Array object.

.. literalinclude:: indexing.py
    :language: python 
    :start-after: [indexing2-snippet]
    :end-before: [indexing2-endsnippet]

.. math::


    A[0,0] = [0]

    A[2,3] = [14]

.. note::
   :class: warning

   Normally you want to avoid accessing individual elements of the array like this for performance reasons.

   This is a warning note regarding accessing individual elements of arrays.

   


Indexing with negative values will access from the end of the array. For example, the value negative one and negative two(-2) will return the last and second to last element of the array, respectively. ArrayFire provides the end alias for this which also allows you to index the last element of the array.

.. literalinclude:: indexing.py
    :language: python 
    :start-after: [indexing3-snippet]
    :end-before: [indexing3-endsnippet]


Indexing slices and subarrays*
******************************
You can access regions of the array via the af::seq and af::span objects. The span objects allows you to select the entire set of elements across a particular dimension/axis of an array. For example, we can select the third column of the array by passing span as the first argument and 2 as the second argument to the parenthesis operator.

.. literalinclude:: indexing.py
    :language: python 
    :start-after: [indexing4-snippet]
    :end-before: [indexing4-endsnippet]

.. math::

       A[:, 2]=\begin{bmatrix}
                8 \\
                9 \\
               10 \\
                11 \\
            \end{bmatrix}

You can read that as saying that you want all values across the first dimension, but only from index 2 of the second dimension.

You can access the second row by passing [1, :] to the array

.. literalinclude:: indexing.py
    :language: python 
    :start-after: [indexing5-snippet]
    :end-before: [indexing5-endsnippet]

.. math::

       A[1, :]=\begin{bmatrix}
               1,5,9,13\\
            \end{bmatrix}

You can use Python's slicing notation to define a range when indexing in **arrayfire**. For example, if you want to get the first two columns of an array, you can access the array by specifying **':'** for the rows (to select all rows), and **0:2** for the columns (to select columns from index 0 to 1).

.. literalinclude:: indexing.py
    :language: python 
    :start-after: [indexing6-snippet]
    :end-before: [indexing6-endsnippet]

.. math::

       A[:, 0:2]= \begin{bmatrix}
                0 & 4\\
                1 & 5\\
                2 & 6\\
                3 & 7\\
            \end{bmatrix}


Indexing using af.Array 
***************************

In Python with arrayfire, you can also index arrays using other **af.Array** objects. ArrayFire flattens the input and treats the elements inside the array
as column major indices to index the original Array as 1D Array.

.. code-block:: python

    import arrayfire as af

    x = af.randu((10, 10))

    # indices 1, 3, 5
    indices = af.range((3)) * 2 + 1

    # returns entries with indices 1, 3, 5 of x.flat()
    y = x[indices] 


You can also index Arrays using boolean Arrays. ArrayFire will return an Array with length of the number of :literal:`True` elements in the indexing arrays
and entries of in column major order of the elements that correspond to :literal:`True` entries:

.. code-block:: python

    import arrayfire as af

    # Creates a random array
    x = af.randu((10, 10))

    # returns an array with all the entries of x that contain values greater than 0.5
    y = x[x > 0.5] 

References and copies
*********************
All indexing operations in ArrayFire return **af.Array** objects, which are instances of the array_proxy class. These objects can either be newly created arrays or references to the original array, depending on the type of indexing operation applied to them

* When an array is indexed using another **af.Array** , a new array is created instead of referencing the original data.
* If an array was indexed using a scalar, **sequential '0:2'** or **span ':'**, then the resulting array will reference the original data IF the first dimension is continuous. The following lines will not allocate additional memory.

.. note::
   :class: warning

   The new arrays wither references or newly allocated arrays, are independent of the original data. Meaning that any changes to the original array will not propagate to the references. Likewise, any changes to the reference arrays will not modify the original data.

.. literalinclude:: indexing.py
    :language: python 
    :start-after: [indexing7-snippet]
    :end-before: [indexing7-endsnippet]

The following code snippet shows some examples of indexing that will allocate new memory.

.. literalinclude:: indexing.py
    :language: python 
    :start-after: [indexing8-snippet]
    :end-before: [indexing8-endsnippet]

Even though the copy3 array references continuous memory in the original array, using an **af.Array** for indexing in ArrayFire results in the creation of a new array

Assignment
**********
In Python with ArrayFire, assigning an **af.Array** replaces the array on the left-hand side of :literal:`=` with the result from the right-hand side. This can lead to changes in type and shape compared to the original array. Notably, assignments do not update arrays previously referenced through indexing operations.

.. literalinclude:: indexing.py
    :language: python 
    :start-after: [indexing9-snippet]
    :end-before: [indexing9-endsnippet]


The :literal:`ref` array is created by indexing into the data array. The initialized :literal:`ref` array points to the data array and does not allocate memory when it is created. After the matmul call, the :literal:`ref` array will not be pointing to the data array. The matmul call will not update the values of the data array.

You can update the contents of an **af.Array** by assigning with the operator parenthesis. For example, if you wanted to change the third column of the :literal:`A` array you can do that by assigning to :literal:`A[:, 2]`.

.. literalinclude:: indexing.py
    :language: python 
    :start-after: [indexing10-snippet]
    :end-before: [indexing10-endsnippet]

.. math::

       ref= \begin{bmatrix} 
               8\\
               9\\
               10\\
               11\\
            \end{bmatrix} A = \begin{bmatrix} 
                                    0 & 4 & 3.14 & 12\\
                                    1 & 5 & 3.14 & 13\\
                                    2 & 6 & 3.14 & 14\\
                                    3 & 7 & 3.14 & 15\\
                                    \end{bmatrix}

This will update only the array being modified. If there are arrays that are referring to this array because of an indexing operation, those values will remain unchanged.

Allocation will only be performed if there are other arrays referencing the data at the point of assignment. In the previous example, an allocation will be performed when assigning to the :literal:`A` array because the :literal:`ref` array is pointing to the original data. Here is another example demonstrating when an allocation will occur:

.. literalinclude:: indexing.py
    :language: python 
    :start-after: [indexing11-snippet]
    :end-before: [indexing11-endsnippet]


In this example, no allocation will take place because when the :literal:`ref` object is created, it is pointing to :literal:`A`'s data. Once it goes out of scope, no data points to A, therefore when the assignment takes place, the data is modified in place instead of being copied to a new address.

You can also assign to arrays using another af::arrays as an indexing array. This works in a similar way to the other types of assignment but care must be taken to assure that the indexes are unique. Non-unique indexes will result in a race condition which will cause non-deterministic values.

.. literalinclude:: indexing.py
    :language: python 
    :start-after: [indexing12-snippet]
    :end-before: [indexing12-endsnippet]


Member Functions
*********************

Check the :doc:`Array Class <classes/array>` for more details on other functions that the Array object provides.

Additional examples
*******************
See Assignment & Indexing operation on arrays for the full listing.

.. literalinclude:: indexing.py
    :language: python 
    :start-after: [indexing13-snippet]
    :end-before: [indexing13-endsnippet]
    