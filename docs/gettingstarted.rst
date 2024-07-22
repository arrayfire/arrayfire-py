Getting Started
========================

Introduction
============

ArrayFire is a high performance software library for parallel computing with an easy-to-use API. ArrayFire abstracts away much of the details of programming parallel architectures by providing a high-level container object, the array, that represents data stored on a CPU, GPU, FPGA, or other type of accelerator. This abstraction permits developers to write massively parallel applications in a high-level language where they need not be concerned about low-level optimizations that are frequently required to achieve high throughput on most parallel architectures.

Supported data types
====================

ArrayFire provides one generic container object, the array on which functions and mathematical operations are performed. The :literal:`array` can represent one of many different basic data types:

* f32 real single-precision (:literal:`float`)
* c32 complex single-precision (:literal:`cfloat`)
* f64 real double-precision (:literal:`double`)
* c64 complex double-precision (:literal:`cdouble`)
* f16 real half-precision (:literal:`half_float::half`)
* b8 8-bit boolean values (:literal:`bool`)
* s32 32-bit signed integer (:literal:`int`)
* u32 32-bit unsigned integer (:literal:`unsigned`)
* u8 8-bit unsigned values (:literal:`unsigned char`)
* s64 64-bit signed integer (:literal:`intl`)
* u64 64-bit unsigned integer (:literal:`uintl`)
* s16 16-bit signed integer (:literal:`short`)
* u16 16-bit unsigned integer (:literal:`unsigned short`)
Most of these data types are supported on all modern GPUs; however, some older devices may lack support for double precision arrays. In this case, a runtime error will be generated when the array is constructed.

If not specified otherwise, :literal:`array`s are created as single precision floating point numbers (:literal:`f32`).

Creating and populating an ArrayFire array
==========================================

ArrayFire arrays represent memory stored on the device. As such, creation and population of an array will consume memory on the device which cannot freed until the :literal:`array` object goes out of scope. As device memory allocation can be expensive, ArrayFire also includes a memory manager which will re-use device memory whenever possible.

Arrays can be created using one of the array constructors. Below we show how to create 1D, 2D, and 3D arrays with uninitialized values:

.. literalinclude:: gettingstarted.py 
    :language: python 
    :start-after: [gettingstarted1-snippet]
    :end-before: [gettingstarted1-endsnippet]



However, uninitialized memory is likely not useful in your application. ArrayFire provides several convenient functions for creating arrays that contain pre-populated values including constants, uniform random numbers, uniform normally distributed numbers, and the identity matrix:

.. literalinclude:: gettingstarted.py 
    :language: python 
    :start-after: [gettingstarted2-snippet]
    :end-before: [gettingstarted2-endsnippet]
    

A complete list of ArrayFire functions that automatically generate data on the device may be found on the functions to create arrays page. As stated above, the default data type for arrays is f32 (a 32-bit floating point number) unless specified otherwise.

ArrayFire arrays may also be populated from data found on the host. For example:

.. literalinclude:: gettingstarted.py 
    :language: python 
    :start-after: [gettingstarted3-snippet]
    :end-before: [gettingstarted3-endsnippet]

ArrayFire also supports array initialization from memory already on the GPU. For example, with CUDA one can populate an :literal:`array` directly using a call to :literal:`cudaMemcpy`:

.. literalinclude:: gettingstarted.py 
    :language: python 
    :start-after: [gettingstarted4-snippet]
    :end-before: [gettingstarted4-endsnippet]

Similar functionality exists for OpenCL too. If you wish to intermingle ArrayFire with CUDA or OpenCL code, we suggest you consult the CUDA interoperability or OpenCL interoperability pages for detailed instructions.

ArrayFire array contents, dimensions, and properties
====================================================

ArrayFire provides several functions to determine various aspects of arrays. This includes functions to print the contents, query the dimensions, and determine various other aspects of arrays.

The print function can be used to print arrays that have already been generated or any expression involving arrays:

.. literalinclude:: gettingstarted.py 
    :language: python 
    :start-after: [gettingstarted5-snippet]
    :end-before: [gettingstarted5-endsnippet]

The dimensions of an array may be determined using either a dim4 object or by accessing the dimensions directly using the dims() and numdims() functions:


.. literalinclude:: gettingstarted.py 
    :language: python 
    :start-after: [gettingstarted6-snippet]
    :end-before: [gettingstarted6-endsnippet]



In addition to dimensions, arrays also carry several properties including methods to determine the underlying type and size (in bytes). You can even determine whether the array is empty, real/complex, a row/column, or a scalar or a vector:

.. literalinclude:: gettingstarted.py 
    :language: python 
    :start-after: [gettingstarted7-snippet]
    :end-before: [gettingstarted7-endsnippet]

For further information on these capabilities, we suggest you consult the full documentation on the array.


Writing mathematical expressions in ArrayFire
=============================================

ArrayFire leverages an advanced Just-In-Time (JIT) compilation engine that optimizes array operations by minimizing the number of CUDA/OpenCL kernels used. In Python, ArrayFire functions operate similarly to a vector library. This means that typical element-wise operations, such as :literal:`c[i] = a[i] + b[i]` in C, can be expressed more succinctly as :literal:`c = a + b`, eliminating the need for explicit indexing.

When multiple array operations are involved, ArrayFire's JIT engine consolidates them through "kernel fusion". This technique not only reduces the frequency of kernel invocations but also optimizes memory usage by eliminating redundant global memory operations. The JIT functionality extends seamlessly across Python function boundaries, continuing until a non-JIT function is encountered or a synchronization operation is explicitly invoked in the code.

ArrayFire provides a broad spectrum of functions tailored for element-wise operations. It supports standard arithmetic operators (+, -, *, /) as well as a variety of transcendental functions (sin, cos, log, sqrt, etc.). These capabilities empower users to perform complex computations efficiently and effectively.

.. literalinclude:: gettingstarted.py 
    :language: python 
    :start-after: [gettingstarted8-snippet]
    :end-before: [gettingstarted8-endsnippet]

To see the complete list of functions please consult the documentation on mathematical, linear algebra, signal processing, and statistics.

Mathematical constants
======================

In Python, ArrayFire provides several platform-independent constants such as Pi, NaN, and Inf. If ArrayFire lacks a specific constant you require, you can create it using the `af.constant` array constructor.

These constants are universally applicable across all ArrayFire functions. Below, we illustrate their usage in element selection and a mathematical expression:

.. literalinclude:: gettingstarted.py 
    :language: python 
    :start-after: [gettingstarted9-snippet]
    :end-before: [gettingstarted9-endsnippet]

Please note that our constants may, at times, conflict with macro definitions in standard header files. When this occurs, please refer to our constants using the :literal:`af::` namespace.

Indexing
========
Like all functions in ArrayFire, indexing is also executed in parallel on the OpenCL/CUDA devices. Because of this, indexing becomes part of a JIT operation and is accomplished using parentheses instead of square brackets (i.e. as :literal:`A(0)` instead of :literal:`A[0]`). To index :literal:`af::` arrays you may use one or a combination of the following functions:

* integer scalars
* seq() representing a linear sequence
* end representing the last element of a dimension
* span representing the entire description
* row(i) or col(i) specifying a single row/column
* rows(first,last) or cols(first,last) specifying a span of rows or columns

Please see the indexing page for several examples of how to use these functions.

Getting access to ArrayFire array memory on the host and device
===============================================================

Memory in :literal:`af::arrays` may be accessed using the host() and device() functions. The :literal:`host` function copies the data from the device and makes it available in a C-style array on the host. As such, it is up to the developer to manage any memory returned by :literal:`host`. The :literal:`device` function returns a pointer/reference to device memory for interoperability with external CUDA/OpenCL kernels. As this memory belongs to ArrayFire, the programmer should not attempt to free/deallocate the pointer. For example, here is how we can interact with both OpenCL and CUDA:

.. literalinclude:: gettingstarted.py 
    :language: python 
    :start-after: [gettingstarted10-snippet]
    :end-before: [gettingstarted10-endsnippet]


ArrayFire also provides several helper functions for creating :literal:`af::arrays` from OpenCL :literal:`cl_mem` references and :literal:`cl::Buffer` objects. See the :literal:`include/af/opencl.h` file for further information.

Lastly, if you want only the first value from an :literal:`af::array` you can use get it using the scalar() function:

.. literalinclude:: gettingstarted.py 
    :language: python 
    :start-after: [gettingstarted11-snippet]
    :end-before: [gettingstarted11-endsnippet]


Bitwise operators
=================
In addition to supporting standard mathematical functions, arrays that contain integer data types also support bitwise operators including and, or, and shift:

.. literalinclude:: gettingstarted.py 
    :language: python 
    :start-after: [gettingstarted12-snippet]
    :end-before: [gettingstarted12-endsnippet]


Using the ArrayFire API in Python
=================================

The ArrayFire library in Python is seamlessly integrated into the Python environment. To start using the library, simply :literal:`import arrayfire` and begin coding!

# todo @stf talk about arrayapi implementation

Sample using Python API
~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: gettingstarted.py 
    :language: python 
    :start-after: [gettingstarted13-snippet]
    :end-before: [gettingstarted13-endsnippet]

    

What to read next?
==================

Now that you have a general introduction to ArrayFire, where do you go from here? In particular you might find these documents useful

* Building an ArrayFire program on Linux
* Building an ArrayFire program on Windows
* Timing ArrayFire code

Where to go for help?
=====================

* Google Groups: https://groups.google.com/forum/#!forum/arrayfire-users
* ArrayFire Services: `Consulting <http://arrayfire.com/consulting/>`_ | `Support <http://arrayfire.com/support/>`_ | `Training <http://arrayfire.com/training/>`_
* ArrayFire Blogs: http://arrayfire.com/blog/
* Email: technical@arrayfire.com