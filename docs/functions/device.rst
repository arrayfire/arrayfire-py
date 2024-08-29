device
======
The 'af.device()' function in the ArrayFire library is used to get or set the current device or device properties. This function provides an interface to interact with the GPU or CPU device being used for computations. It allows you to select a particular device from available options or query the properties of the current device.

Function
--------
:literal:`af.device()`
    - Python interface to get or set device properties.

Detailed Description
--------------------
The 'af.device()' function is useful for managing and querying the device that ArrayFire is using for computations. This function can perform various tasks related to device management, such as:

- Getting the Current Device: Retrieve the index of the currently selected device.
- Setting the Current Device: Select a specific device for computations.
- Querying Device Properties: Obtain information about the current device.

This functionality is important for applications that need to explicitly choose between multiple GPUs or check device capabilities.

Function Documentation
----------------------
.. sidebar:: af.device()

    Syntax:
        af.device(option=None, value=None)
    
    Parameters:
        'option' (optional): Specifies the type of information or action. Can be one of the following:

        - "device": Get the current device index.
        - "set": Set the current device index.
        - "count": Get the number of available devices.
        - "name": Get the name of the current device.
        - "info": Get detailed information about the current device.

        'value (optional)': The index of the device to set. Used only when the option is "set". If option is "set", this parameter should be an integer representing the device index.

    Returns:
        Depending on the option, the function returns various types of information:
        - If 'option' is "device": The index of the current device.
        - If 'option' is "count": The number of available devices.
        - If 'option' is "name": The name of the current device.
        - If 'option' is "info": Detailed information about the current device.
