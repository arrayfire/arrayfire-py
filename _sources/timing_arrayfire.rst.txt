Timing ArrayFire
=================

Preamble
########

As shown in other sections, ArrayFire leverages Just-in-Time (JIT) compilation of kernels to speedup many array operations.
This means that after a function is called, the operation may not have finished (or even started) after execution continues
to the next line. Furthermore, the first time an operation is done, as it may be slowed down due to the JIT compilation of 
the combined operations; later operations will not have this problem as the compiled kernel is cached.

So benchmarking ArrayFire is not as straight forward as just wrapping an operation in between timers.

Setup
#######

For benchmarking we will utilize two functions: `af.sync()` and `af.eval(arr)`.

- :doc:`af.sync <functions/sync>`: The purpose of this function is to stall the current thread until all awaiting operations have finished and the result is accessable by the host. It synchronizes the host and the device, similar to what cuda.Stream.synchronize() does in cupy.

- :doc:`af.eval <functions/eval>`: This function takes in an array which will be forced to be evaluated immediately. This forces the JIT tree to be cut at the point of this function calls and any later operations will not be considered in this current JIT tree.


Using these two function we can make sure that we are benchmarking the correct operations by making sure that no operation is running
before or after we want our timers to measure.

Example
##########

The following is an examples of timing how long an addition takes

.. code-block:: python

    import arrayfire as af
    import time

    # Generate a random array
    x = af.randn(1000000)
    
    # Make sure the numbers have been generated before the timing starts
    af.eval(x)
    af.sync()

    # Start timer
    start = time.perf_counter()
    y = x + x

    # Make sure the computation has finished before the timing ends
    af.eval(y)
    af.sync()

    # End timer
    end = time.perf_counter()

    print(f"Elapsed time: {end - start:.6f} seconds")


Benchmarking JIT vs non-JIT
############################

For timing JIT operations against non-JIT operations, please take a look at page on JIT :doc:`arrayfirejitcodegeneration` and
the code in :download:`afjit.py`.