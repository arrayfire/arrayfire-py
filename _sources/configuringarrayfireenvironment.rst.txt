Configuring ArrayFire Environment
=================================
This page lists environment and runtime configurations that will help enhance your experience with ArrayFire.
The following are useful environment variable that can be used with ArrayFire.

For Device Execution
####################

`AF_CUDA_DEFAULT_DEVICE`
************************

Use this variable to set the default CUDA device. Valid values for this
variable are the device identifiers shown when af::info is run.

.. code-block:: bash

    AF_CUDA_DEFAULT_DEVICE=1 python myprogram_cuda.py


`AF_ONEAPI_DEFAULT_DEVICE`
***************************

Use this variable to set the default oneAPI device. Valid values for this
variable are the device identifiers shown when af::info is run.

.. code-block:: bash

    AF_ONEAPI_DEFAULT_DEVICE=1 python myprogram_oneapi.py


Note: af::setDevice call in the source code will take precedence over this
variable.

`AF_OPENCL_DEFAULT_DEVICE`
**************************

Use this variable to set the default OpenCL device. Valid values for this
variable are the device identifiers shown when af::info is run.

.. code-block:: bash

    AF_OPENCL_DEFAULT_DEVICE=1 python myprogram_opencl.py


Note: af::setDevice call in the source code will take precedence over this
variable.

`AF_OPENCL_DEFAULT_DEVICE_TYPE`
*******************************

Use this variable to set the default OpenCL device type. Valid values for this
variable are: CPU, GPU, ACC (Accelerators).

When set, the first device of the specified type is chosen as default device.

.. code-block:: bash

    AF_OPENCL_DEFAULT_DEVICE_TYPE=CPU python myprogram_opencl.py


Note: `AF_OPENCL_DEFAULT_DEVICE` and af::setDevice takes precedence over this variable.

`AF_OPENCL_DEVICE_TYPE`
***********************

Use this variable to only choose OpenCL devices of specified type. Valid values for this
variable are:

- ALL: All OpenCL devices. (Default behavior).
- CPU: CPU devices only.
- GPU: GPU devices only.
- ACC: Accelerator devices only.

When set, the remaining OpenCL device types are ignored by the OpenCL backend.

.. code-block:: bash

    AF_OPENCL_DEVICE_TYPE=CPU python myprogram_opencl.py


`AF_OPENCL_CPU_OFFLOAD`
************************

When ArrayFire runs on devices with unified memory with the host (ie.
`CL_DEVICE_HOST_UNIFIED_MENORY` is true for the device) then certain functions
are offloaded to run on the CPU using mapped buffers.

ArrayFire takes advantage of fast libraries such as MKL while spending no time
copying memory from device to host. The device memory is mapped to a host
pointer which can be used in the offloaded functions.

This functionality can be disabled by using the environment variable
`AF_OPENCL_CPU_OFFLOAD=0`.

The default bevaior of this has changed in version 3.4.

Prior to v3.4, CPU Offload functionality was used only when the user set
`AF_OPENCL_CPU_OFFLOAD=1` and disabled otherwise.

From v3.4 onwards, CPU Offload is enabled by default and is disabled only when
`AF_OPENCL_CPU_OFFLOAD=0` is set.

For Debugging
#############

`AF_VERBOSE_LOADS`
*******************

The arrayfire binary python wrapper (`arrayfire_wrapper` package) searches for default locations where
the arrayfire binaries may be located for loading. When set to 1, ArrayFire will print the locations
where the backend binaries are being searched and if loading the library at the location was successful.

.. code-block:: bash

    AF_VERBOSE_LOADS=1 python myprogram.py

`AF_PRINT_ERRORS`
******************

When AF_PRINT_ERRORS is set to 1, the exceptions thrown are more verbose and
detailed. This helps in locating the exact failure.

.. code-block:: bash

    AF_PRINT_ERRORS=1 python myprogram.py


`AF_TRACE`
**********
This is a comma separated
list of modules to trace. If enabled, ArrayFire will print relevant information
to stdout. Currently the following modules are supported:

- all: All trace outputs
- jit: Logs kernel fetch & respective compile options and any errors.
- mem: Memory management allocation, free and garbage collection information
- platform: Device management information
- unified: Unified backend dynamic loading information

Tracing displays the information that could be useful when debugging or
optimizing your application. Here is how you would use this variable:

.. code-block:: bash

    AF_TRACE=mem,unified python myprogram.py

This will print information about memory operations such as allocations,
deallocations, and garbage collection.

All trace statements printed to the console have a suffix with the following
pattern.

:literal:`[category][Seconds since Epoch][Thread Id][source file relative path] \<Message\>`

`AF_OPENCL_SHOW_BUILD_INFO`
***************************

This variable is useful when debugging OpenCL kernel compilation failures. When
this variable is set to 1, and an error occurs during a OpenCL kernel
compilation, then the log and kernel are printed to screen.

`AF_MEM_DEBUG`
**************

When AF_MEM_DEBUG is set to 1 (or anything not equal to 0), the caching
mechanism in the memory manager is disabled. The device buffers are allocated
using native functions as needed and freed when going out of scope.

When the environment variable is not set, it is treated to be zero.

.. code-block::

    AF_MEM_DEBUG=1 python myprogram.py

`AF_MAX_BUFFERS`
*****************

When AF_MAX_BUFFERS is set, this environment variable specifies the maximum
number of buffers allocated before garbage collection kicks in.

Please note that the total number of buffers that can exist simultaneously can
be higher than this number. This variable tells the garbage collector that it
should free any available buffers immediately if the treshold is reached.

When not set, the default value is 1000.

`AF_OPENCL_MAX_JIT_LEN`
*************************

When set, this environment variable specifies the maximum height of the OpenCL
JIT tree after which evaluation is forced.

The default value, as of v3.4, is 50 on OSX, 100 everywhere else. This value was
20 for older versions.

`AF_CUDA_MAX_JIT_LEN`
*********************

When set, this environment variable specifies the maximum height of the CUDA JIT
tree after which evaluation is forced.

The default value, as of v3.4, 100. This value was 20 for older versions.

`AF_CPU_MAX_JIT_LEN`
********************

When set, this environment variable specifies the maximum length of the CPU JIT
tree after which evaluation is forced.

The default value, as of v3.4, 100. This value was 20 for older versions.

`AF_BUILD_LIB_CUSTOM_PATH`
**************************

When set, this environment variable specifies a custom path along which the
symbol manager will search for dynamic (shared library) backends to load. This
is useful for specialized build configurations that use the unified backend and
build shared libraries separately.

By default, no additional path will be searched for an empty value.


`AF_JIT_KERNEL_TRACE`
**********************

When set, this environment variable has to be set to one of the following
three values:

- stdout : generated kernels will be printed to standard output
- stderr : generated kernels will be printed to standard error stream
- absolute path to a folder on the disk where generated kernels will be stored

CUDA backend kernels are stored in files with cu file extension.

OpenCL backend kernels are stored in files with cl file extension.

`AF_JIT_KERNEL_CACHE_DIRECTORY`
*******************************

This variable sets the path to the ArrayFire cache on the filesystem. If set
ArrayFire will write the kernels that are compiled at runtime to this directory.
If the path is not writeable, the default path is used.

This path is different from AF_JIT_KERNEL_TRACE which stores strings. These
kernels will store binaries and the content will be dependent on the
backend and platforms used.

The default path is determined in the following order:
  Unix:
      1. $HOME/.arrayfire
      2. /tmp/arrayfire
  Windows:
      1. ArrayFire application Temp folder(Usually
          C:\\Users\\\<user_name\>\\AppData\\Local\\Temp\\ArrayFire)