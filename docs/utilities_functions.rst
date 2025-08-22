Utilities
===========

General-purpose functions for managing arrays and devices.

.. list-table:: Functions

    * - :doc:`af.alloc_device() <functions/alloc_device>`
        - Allocate memory on device
    * - :doc:`af.alloc_host() <functions/alloc_host>`
        - Allocate memory on host.
    * - :doc:`af.alloc_pinned() <functions/alloc_pinned>`
        - Allocate pinned memory on device.
    * - :doc:`af.cublas_set_math_mode() <functions/cublas_set_math_mode>`
        - Sets the cuBLAS math mode for the internal handle
    * - :doc:`af.delete_image_memory() <functions/delete_image_memory>`
        - Delete memory created by saveImageMem
    * - :doc:`af.det() <functions/det>`
        - Find the determinant of a matrix.
    * - :doc:`af.device_gc() <functions/device_gc>`
        - Call the garbage collection routine
    * - :doc:`af.device_info() <functions/device_info>`
        - Gets the information about device and platform as strings.
    * - :doc:`af.device_mem_info() <functions/device_mem_info>`
        - Gets information about the memory manager
    * - :doc:`af.free_device() <functions/free_device>`
        - Free memory allocated on device internally by ArrayFire.
    * - :doc:`af.free_host() <functions/free_host>`
        - Free memory allocated on host internally by ArrayFire.
    * - :doc:`af.free_pinned() <functions/free_pinned>`
        - Free pinned memory allocated by ArrayFire's memory manager.
    * - :doc:`af.get_backend() <functions/get_backend>`
        - Gets the backend enum for the active backend.
    * - :doc:`af.get_dbl_support() <functions/get_dbl_support>`
        - Gets if the device supports double floating point
    * - :doc:`af.get_device() <functions/get_device>`
        - Get the current device ID.
    * - :doc:`af.get_device_count() <functions/get_device_count>`
        - Gets the number of compute devices on the system.
    * - :doc:`af.get_half_support() <functions/get_half_support>`
        - Gets if the device supports half floating point
    * - :doc:`af.get_kernel_cache_directory() <functions/get_kernel_cache_directory>`
        - Returns directory where ArrayFire JIT kernels are being stored
    * - :doc:`af.get_mem_step_size() <functions/get_mem_step_size>`
        - Get the minimum memory chunk size.
    * - :doc:`af.get_native_id() <functions/get_native_id>`
        - Get the native device id of the CUDA device with id in ArrayFire context
    * - :doc:`af.get_stream() <functions/get_stream>`
        - Returns the current cuda stream
    * - :doc:`af.info() <functions/info>`
        - Display ArrayFire and device info.
    * - :doc:`af.info_string() <functions/info_string>`
        - Returns a string with information of current device and backend
    * - :doc:`af.init() <functions/init>`
        - Initializes ArrayFire
    * - :doc:`af.is_image_io_available() <functions/is_image_io_available>`
        - Checks if Image IO is available
    * - :doc:`af.is_lapack_available() <functions/is_lapack_available>`
        - Check if lapack runtimes are available
    * - :doc:`af.load_image() <functions/load_image>`
        - Load an image from disk to an array
    * - :doc:`af.load_image_memory() <functions/load_image_memory>`
        - Load an image from memory which is stored as a FreeImage stream
    * - :doc:`af.load_image_native() <functions/load_image_native>`
        - Load an image as is original type.
    * - :doc:`af.print_mem_info() <functions/print_mem_info>`
        - Prints buffer details from the ArrayFire Device Manager
    * - :doc:`af.read_array() <functions/read_array>`
        - Load an array from a file.
    * - :doc:`af.save_array() <functions/save_array>`
        - Save an array to a binary file
    * - :doc:`af.save_image() <functions/save_image>`
        - Save an array to disk as an image
    * - :doc:`af.save_image_memory() <functions/save_image_memory>`
        - Save an array to memory as an image using FreeImage stream
    * - :doc:`af.save_image_native() <functions/save_image_native>`
        - Save an image as is original type.
    * - :doc:`af.set_backend() <functions/set_backend>`
        - Set the current backend
    * - :doc:`af.set_device() <functions/set_device>`
        - Change current device to specified device.
    * - :doc:`af.set_fft_plan_cache_size() <functions/set_fft_plan_cache_size>`
        - Sets fft plan cache size
    * - :doc:`af.set_kernel_cache_directory() <functions/set_kernel_cache_directory>`
        - Sets the directory for JIT kernel caching
    * - :doc:`af.set_mem_step_size() <functions/set_mem_step_size>`
        - Get the minimum memory chunk size.
    * - :doc:`af.set_native_id() <functions/set_native_id>`
        - Set the CUDA device with given native id as the active device for ArrayFire