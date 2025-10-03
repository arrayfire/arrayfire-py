set_backend
===========
The 'af.set_backend()' function in ArrayFire is used to specify which backend will be used for subsequent ArrayFire operations. This is useful when working with multiple devices or GPUs to ensure that computations are directed to the desired hardware and software libraries.

Function
--------
:literal:`af.set_backend()`
    - Python interface used to specify which backend will be used for subsequent arrayfire operations.

Detailed Description
--------------------
The 'af.set_backend()' function sets the backend for ArrayFire operations. By default, ArrayFire uses the first available backend in order of priority: 'cuda', 'opencl', 'oneapi', 'cpu' from highest to lowest priority. When you have multiple GPUs or devices, you can use this function to select which backend ArrayFire should use for subsequent operations.
Note that previous instantiated af.Array's or results from functions before the backend has been set will not be migrated to the new backend and device.

Function Documentation
----------------------
.. sidebar:: af.set_backend()

    Syntax:
        af.set_backend(backend)
    
    Parameters:
        'backend': af.BackendType value that corresponds to the ArrayFire backend to be set. Available values are af.BackendType.cuda, af.BackendType.opencl, af.BackendType.oneapi, and af.BackendType.cpu

    Returns:
        None
