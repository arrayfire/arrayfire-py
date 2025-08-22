Overview
========

About ArrayFire
***************

.. image:: images/arrayfire_logo.png
   :alt: ArrayFire Logo
   :align: center
   :class: responsive-img

`ArrayFire <https://github.com/arrayfire/arrayfire>`_ is a high performance library for parallel computing with an easy-to-use API. It enables users to write scientific computing code that is portable across CUDA, OpenCL and CPU devices. This project provides Python bindings for the ArrayFire library.

Installing ArrayFire
********************

Install ArrayFire using either a binary installer for Windows, OSX, or Linux or download it from source:
  * `Download and install Binaries <https://arrayfire.com/download/>`_
  * `Build from source <https://github.com/arrayfire/arrayfire-py>`_

Using ArrayFire
***************

The array object is beautifully simple.

Array-based notation effectively expresses computational algorithms in readable math-resembling notation. Expertise in parallel programming is not required to use ArrayFire.

A few lines of ArrayFire code accomplishes what can take 100s of complicated lines in CUDA, oneAPI, or OpenCL kernels.

Support for multiple domains
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ArrayFire contains hundreds of functions across various domains including:

Vector Algorithms
Image Processing
Computer Vision
Signal Processing
Linear Algebra
Statistics
and more.
Each function is hand-tuned by ArrayFire developers with all possible low-level optimizations.

Support for various data types and sizes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ArrayFire operates on common data shapes and sizes, including vectors, matrices, volumes, and

It supports common data types, including single and double precision floating point values, complex numbers, booleans, and 32-bit signed and unsigned integers.

Extending ArrayFire
~~~~~~~~~~~~~~~~~~~

ArrayFire can be used as a stand-alone application or integrated with existing CUDA, oneAPI, or OpenCL code.

With support for x86, ARM, CUDA, oneAPI, and OpenCL devices, ArrayFire supports for a comprehensive list of devices.

Each ArrayFire installation comes with:

    * a CUDA backend (named 'libafcuda') for `NVIDIA GPUs <https://developer.nvidia.com/cuda-gpus>`_
    * a oneAPI backend (named 'libafoneapi') for `oneAPI devices <https://www.intel.com/content/www/us/en/developer/articles/system-requirements/intel-oneapi-base-toolkit-system-requirements.html>`_
    * an OpenCL backend (named 'libafopencl') for `OpenCL devices <https://www.khronos.org/conformance/adopters/conformant-products#opencl>`_,
    * a CPU backend (named 'libafcpu') to fall back to when CUDA, oneAPI, or OpenCL devices are unavailable.

Vectorized and Batched Operations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ArrayFire supports batched operations on N-dimensional arrays. Batch operations in ArrayFire are run in parallel ensuring an optimal usage of CUDA, oneAPI, or OpenCL devices.

Best performance with ArrayFire is achieved using vectorization techniques.

ArrayFire can also execute loop iterations in parallel with the gfor function.

Just in Time compilation
~~~~~~~~~~~~~~~~~~~~~~~~
ArrayFire performs run-time analysis of code to increase arithmetic intensity and memory throughput, while avoiding unnecessary temporary allocations. It has an awesome internal JIT compiler to make important optimizations.

Read more about how ArrayFire JIT. can improve the performance in your application.


Simple Example
--------------

Here is an example of ArrayFire code that performs a Monte Carlo estimation of PI.

.. literalinclude:: overview.py 
    :language: python 
    :start-after: [pi-example-simple-snippet]
    :end-before: [pi-example-simple-endsnippet]

Product Support
***************

Free Community Options
~~~~~~~~~~~~~~~~~~~~~~
  * `ArrayFire Mailing List <https://groups.google.com/g/arrayfire-users>`_ (recommended)
  * `StackOverFlow <https://stackoverflow.com/questions/tagged/arrayfire>`_

Premium Support
~~~~~~~~~~~~~~~
  * Phone Support - available for purchase(request a quote)

Contact Us
~~~~~~~~~~
  * If you need to contact us, visit our `Contact Us page <https://arrayfire.com/company/#contact-us>`_.

Email
~~~~~
  * Engineering: technical@arrayfire.com
  * Sales: sales@arrayfire.com

Citations and Acknowledgements
******************************

If you redistribute ArrayFire, please follow the terms established in `the license <https://github.com/arrayfire/arrayfire-python/blob/master/LICENSE>`_. If you wish to cite ArrayFire in an academic publication, please use the following reference: