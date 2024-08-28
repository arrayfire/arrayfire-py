get_device
==========
The 'af.get_device()' function in ArrayFire is used to retrieve the device object associated with the ArrayFire context. This function provides information about the current active device, such as its ID, name, and properties. It is useful for managing and querying the status of devices in a multi-device environment.

Function
--------
:literal:`af.get_device()`
    - Python interface used to retrieve the device object associated with the ArrayFire context.

Detailed Description
--------------------
The 'af.get_device()' function provides access to the device object in ArrayFire. This device object contains various details about the GPU or other computational device that ArrayFire is using for computations. This function is particularly useful in environments where multiple devices are available and you need to query or manage device-specific information.

Function Documentation
----------------------
.. sidebar:: af.get_device()

    Syntax:
        device = af.get_device()

    
    Parameters:
        This function does not take any parameters.

    Returns:
        An ArrayFire device object representing the current active device in the ArrayFire context.

