set_device
==========
The 'af.set_device()' function in ArrayFire is used to specify which device (GPU or CPU) will be used for subsequent ArrayFire operations. This is particularly useful when working with multiple devices or GPUs to ensure that computations are directed to the desired hardware.

Function
--------
:literal:`af.set_device()`
    - Python interface used to specify which device will be used for subsequent arrayfire operations.

Detailed Description
--------------------
The 'af.set_device()' function sets the device ID for ArrayFire operations. By default, ArrayFire uses the first available device (usually device ID 0). When you have multiple GPUs or devices, you can use this function to select which device ArrayFire should use for subsequent operations.

Function Documentation
----------------------
.. sidebar:: af.set_device()

    Syntax:
        af.set_device(device_id)
    
    Parameters:
        'device_id': An integer representing the ID of the device to be set. This ID corresponds to the device index in the ArrayFire device list.

    Returns:
        None
