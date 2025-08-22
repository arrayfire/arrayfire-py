Functions
=========

.. include:: classes/index
.. include:: functions/index
.. include:: constants/index

.. toctree::
    :hidden:

    array_creation_functions
    array_manipulation_functions
    fourier_transforms_functions
    data_reduction_functions
    linear_algebra_functions
    mathematical_operations_functions
    special_functions
    statistics_functions
    utilities_functions

Documentation grouped by category:


.. collapse:: Arrayfire Classes

    .. list-table::

        * - :doc:`af.Array <classes/array>`
            - Represents an ArrayFire array
        * - :doc:`af.library.random.RandomEngine <classes/RandomEngine>`
            - Reperesents an ArrayFire custom random engine
        * - :doc:`af.library.features.Features <classes/Features>`
            - Represents an ArrayFire Feature Extraction class


.. collapse:: Arrayfire Functions

    .. list-table::

        * - :doc:`af.abs() <functions/abs>`
            - Calculate the absolute value.
        * - :doc:`af.accum() <functions/accum>`
            - Evaluate the cumulative sum (inclusive) along a given dimension.
        * - :doc:`af.acos() <functions/acos>`
            - Evaluate the inverse cosine function (arc cosine).
        * - :doc:`af.acosh() <functions/acosh>`
            - Evaluate the inverse hyperbolic cosine function (area hyperbolic cosine).
        * - :doc:`af.add() <functions/add>`
            - Elementwise addition.
        * - :doc:`af.all_true() <functions/all_true>`
            - Check if all values along a given dimension are true.
        * - :doc:`af.alloc_device() <functions/alloc_device>`
            - Allocate memory on device
        * - :doc:`af.alloc_host() <functions/alloc_host>`
            - Allocate memory on host.
        * - :doc:`af.alloc_pinned() <functions/alloc_pinned>`
            - Allocate pinned memory on device.
        * - :doc:`af.anisotropic_diffusion() <functions/anisotropic_diffusion>`
            - Anisotropic Smoothing Filter.
        * - :doc:`af.any_true() <functions/any_true>`
            - Check if any values along a given dimension are true.
        * - :doc:`af.approx1() <functions/approx1>`
            - Interpolation across a single dimension.
        * - :doc:`af.approx1_uniform() <functions/approx1_uniform>`
            - Interpolation across a single dimension in uniform steps
        * - :doc:`af.approx2() <functions/approx2>`
            - Interpolation along two dimensions.
        * - :doc:`af.approx2_uniform() <functions/approx2_uniform>`
            - Interpolation along two dimensions in uniform steps
        * - :doc:`af.arg() <functions/arg>`
            - Calculate the phase angle (in radians) of a complex array.
        * - :doc:`af.asin() <functions/asin>`
            - Evaluate the inverse sine function (arc sine).
        * - :doc:`af.asinh() <functions/asinh>`
            - Evaluate the inverse hyperbolic sine function (area hyperbolic sine).
        * - :doc:`af.atan() <functions/atan>`
            - Evaluate the inverse tangent function (arc tangent).
        * - :doc:`af.atan2() <functions/atan2>`
            - Evaluate the inverse tangent function (arc tangent).
        * - :doc:`af.atanh() <functions/atanh>`
            - Evaluate the inverse hyperbolic tangent function (area hyperbolic tangent).
        * - :doc:`af.bilateral() <functions/bilateral>`
            - Bilateral Filter.
        * - :doc:`af.bitand() <functions/bitand>`
            - Evaluate the bitwise AND of two arrays.
        * - :doc:`af.bitnot() <functions/bitnot>`
            - Evaluate the bitwise NOT of an array.
        * - :doc:`af.bitor() <functions/bitor>`
            - Evaluate the bitwise OR of two arrays.
        * - :doc:`af.bitshiftl() <functions/bitshiftl>`
            - Shift the bits of integer arrays left.
        * - :doc:`af.bitshiftr() <functions/bitshiftr>`
            - Shift the bits of integer arrays right.
        * - :doc:`af.bitxor() <functions/bitxor>`
            - Evaluate the bitwise XOR of two arrays.
        * - :doc:`af.canny() <functions/canny>`
            - Canny Edge Detector.
        * - :doc:`af.cast() <functions/cast>`
            - Cast an array from one type to another.
        * - :doc:`af.cbrt() <functions/cbrt>`
            - Evaluate the cube root.
        * - :doc:`af.ceil() <functions/ceil>`
            - Rounds up to the least integer greater than or equal to x.
        * - :doc:`af.cholesky() <functions/cholesky>`
            - Perform Cholesky decomposition.
        * - :doc:`af.clamp() <functions/clamp>`
            - Clamp an array between an upper and a lower limit.
        * - :doc:`af.color_space() <functions/color_space>`
            - Colorspace conversion function.
        * - :doc:`af.confidence_cc() <functions/confidence_cc>`
            - Segment image based on similar pixel characteristics.
        * - :doc:`af.conjg() <functions/conjg>`
            - Evaluate the complex conjugate of an input array.
        * - :doc:`af.constant() <functions/constant>`
            - Create an array from a scalar input value.
        * - :doc:`af.convolve1() <functions/convolve1>`
            - Convolution Integral for one dimensional data.
        * - :doc:`af.convolve2() <functions/convolve2>`
            - Convolution Integral for two dimensional data.
        * - :doc:`af.convolve2_gradient_nn() <functions/convolve2_gradient_nn>`
            - Version of convolution that is consistent with the machine learning formulation that will spatially convolve a filter on 2-dimensions against a signal. 
        * - :doc:`af.convolve2_nn() <functions/convolve2_nn>`
            - Version of convolution that is consistent with the machine learning formulation that will spatially convolve a filter on 2-dimensions against a signal. 
        * - :doc:`af.convolve2_separable() <functions/convolve2_separable>`
            - Faster equivalent of the canonical 2D convolution for filters/kernels that can be decomposed into two separate spatial vectors.
        * - :doc:`af.convolve3() <functions/convolve3>`
            - Convolution Integral for three dimensional data.
        * - :doc:`af.copy_array() <functions/copy_array>`
            - Performs a deep copy of the array.
        * - :doc:`af.cos() <functions/cos>`
            - Evaluate the cosine function.
        * - :doc:`af.cosh() <functions/cosh>`
            - Evaluate the hyperbolic cosine function.
        * - :doc:`af.count() <functions/count>`
            - Count non-zero values in an array along a given dimension.
        * - :doc:`af.cplx() <functions/cplx>`
            - Creates complex arrays from real and imaginary parts
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
        * - :doc:`af.diag() <functions/diag>`
            - Extract the diagonal from an array.
        * - :doc:`af.diff1() <functions/diff1>`
            - Calculate the first order difference in an array over a given dimension.
        * - :doc:`af.diff2() <functions/diff2>`
            - Calculate the second order difference in an array over a given dimension.
        * - :doc:`af.dilate() <functions/dilate>`
            - Dilation(morphological operator) for images.
        * - :doc:`af.div() <functions/div>`
            - Elementwise division.
        * - :doc:`af.dog() <functions/dog>`
            - Difference of Gaussians.
        * - :doc:`af.dot() <functions/dot>`
            - Compute the dot product.
        * - :doc:`af.eq() <functions/eq>`
            - Equal to, an elementwise comparison of two arrays.
        * - :doc:`af.erf() <functions/erf>`
            - Evaluate the error function.
        * - :doc:`af.erfc() <functions/erfc>`
            - Evaluate the complementary error function.
        * - :doc:`af.erode() <functions/erode>`
            - Erosion(morphological operator) for images.
        * - :doc:`af.eval() <functions/eval>`
            - Evaluate an expression (nonblocking).
        * - :doc:`af.exp() <functions/exp>`
            - Evaluate the exponential function.
        * - :doc:`af.expm1() <functions/expm1>`
            - Evaluate the exponential function of an array minus 1, exp(in) - 1.
        * - :doc:`af.factorial() <functions/factorial>`
            - Evaluate the factorial.
        * - :doc:`af.fast() <functions/fast>`
            - FAST feature detector.
        * - :doc:`af.fft() <functions/fft>`
            - Fast Fourier Transform.
        * - :doc:`af.fft2() <functions/fft2>`
            - Fast Fourier Transform.
        * - :doc:`af.fft2_c2r() <functions/fft2_c2r>`
            - Fast fourier transform on two dimensional real signals producing complex output
        * - :doc:`af.fft2_r2c() <functions/fft2_r2c>`
            - Fast fourier transform on two dimensional real signals producing complex output
        * - :doc:`af.fft3() <functions/fft3>`
            - Fast Fourier Transform.
        * - :doc:`af.fft3_c2r() <functions/fft3_c2r>`
            - Fast fourier transform on three dimensional real signals producing complex output
        * - :doc:`af.fft3_r2c() <functions/fft3_r2c>`
            - Fast fourier transform on three dimensional real signals producing complex output
        * - :doc:`af.fft_c2r() <functions/fft_c2r>`
            - Fast fourier transform on complex signals producing real output
        * - :doc:`af.fft_convolve1() <functions/fft_convolve1>`
            - FFT-based convolution for one dimensional signals
        * - :doc:`af.fft_convolve2() <functions/fft_convolve2>`
            - FFT-based convolution for two dimensional signals
        * - :doc:`af.fft_convolve3() <functions/fft_convolve3>`
            - FFT-based convolution for three dimensional signals
        * - :doc:`af.fft_r2c() <functions/fft_r2c>`
            - Fast fourier transform on real signals producing complex output
        * - :doc:`af.fir() <functions/fir>`
            - This function implements a Finite Impulse Filter.
        * - :doc:`af.flat() <functions/flat>`
            - Flatten an array.
        * - :doc:`af.flip() <functions/flip>`
            - Flip the input along a specified dimension.
        * - :doc:`af.floor() <functions/floor>`
            - Rounds down to the greatest integer less than or equal to x.
        * - :doc:`af.free_device() <functions/free_device>`
            - Free memory allocated on device internally by ArrayFire.
        * - :doc:`af.free_host() <functions/free_host>`
            - Free memory allocated on host internally by ArrayFire.
        * - :doc:`af.free_pinned() <functions/free_pinned>`
            - Free pinned memory allocated by ArrayFire's memory manager.
        * - :doc:`af.gaussian_kernel() <functions/gaussian_kernel>`
            - Creates a Gaussian Kernel.
        * - :doc:`af.ge() <functions/ge>`
            - Greater than or equal to, an elementwise comparison of two arrays.
        * - :doc:`af.gemm() <functions/gemm>`
            - General matrix multiplication.
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
        * - :doc:`af.gloh() <functions/gloh>`
            - SIFT feature detector and GLOH descriptor extractor.
        * - :doc:`af.gradient() <functions/gradient>`
            - Calculate the gradients of the input
        * - :doc:`af.gray2rgb() <functions/gray2rgb>`
            - Grayscale to RGB colorspace converter.
        * - :doc:`af.gt() <functions/gt>`
            - Greater than comparison, an elementwise comparison of two arrays.
        * - :doc:`af.hamming_matcher() <functions/hamming_matcher>`
            - Calculates Hamming distances between two 2-dimensional arrays
        * - :doc:`af.harris() <functions/harris>`
            - Harris corner detector.
        * - :doc:`af.hist_equal() <functions/hist_equal>`
            - Histogram equalization of input image.
        * - :doc:`af.histogram() <functions/histogram>`
            - Histogram of input data.
        * - :doc:`af.hsv2rgb() <functions/hsv2rgb>`
            - HSV to RGB colorspace converter.
        * - :doc:`af.hypot() <functions/hypot>`
            - Evaluate the length of the hypotenuse of two inputs.
        * - :doc:`af.identity() <functions/identity>`
            - Generate an identity matrix.
        * - :doc:`af.ifft() <functions/ifft>`
            - Fast Fourier Transform.
        * - :doc:`af.ifft2() <functions/ifft2>`
            - Fast Fourier Transform.
        * - :doc:`af.ifft3() <functions/ifft3>`
            - Fast Fourier Transform.
        * - :doc:`af.iir() <functions/iir>`
            - This function implements a Infinite Impulse Filter.
        * - :doc:`af.imag() <functions/imag>`
            - Returns the imaginary part of a complex array.
        * - :doc:`af.imax() <functions/imax>`
            - Finds the maximum value.
        * - :doc:`af.imin() <functions/imin>`
            - Finds the minimum value.
        * - :doc:`af.info() <functions/info>`
            - Display ArrayFire and device info.
        * - :doc:`af.info_string() <functions/info_string>`
            - Returns a string with information of current device and backend
        * - :doc:`af.init() <functions/init>`
            - Initializes ArrayFire
        * - :doc:`af.inv() <functions/inv>`
            - Computes the inverse of a matrix.
        * - :doc:`af.inverse() <functions/inverse>`
            - Invert a matrix.
        * - :doc:`af.inverse_deconv() <functions/inverse_deconv>`
            - Inverse Deconvolution using linear algebra (non-iterative) methods
        * - :doc:`af.iota() <functions/iota>`
            - Generate an array with [0, n-1] values modified to specified dimensions and tiling.
        * - :doc:`af.is_image_io_available() <functions/is_image_io_available>`
            - Checks if Image IO is available
        * - :doc:`af.is_lapack_available() <functions/is_lapack_available>`
            - Check if lapack runtimes are available
        * - :doc:`af.isinf() <functions/isinf>`
            - Check if values are infinite.
        * - :doc:`af.isnan() <functions/isnan>`
            - Check if values are NaN.
        * - :doc:`af.iszero() <functions/iszero>`
            - Check if values are zero.
        * - :doc:`af.iterative_deconv() <functions/iterative_deconv>`
            - Inverse Deconvolution using iterative methods
        * - :doc:`af.join() <functions/join>`
            - Join up to 4 arrays along specified dimension.
        * - :doc:`af.le() <functions/le>`
            - Less than or equal to, an elementwise comparison of two arrays.
        * - :doc:`af.lgamma() <functions/lgamma>`
            - Evaluate the logarithm of the absolute value of the gamma function.
        * - :doc:`af.load_image() <functions/load_image>`
            - Load an image from disk to an array
        * - :doc:`af.load_image_memory() <functions/load_image_memory>`
            - Load an image from memory which is stored as a FreeImage stream
        * - :doc:`af.load_image_native() <functions/load_image_native>`
            - Load an image as is original type.
        * - :doc:`af.log() <functions/log>`
            - Evaluate the natural logarithm.
        * - :doc:`af.log10() <functions/log10>`
            - Evaluate the base 10 logarithm.
        * - :doc:`af.log1p() <functions/log1p>`
            - Evaluate the natural logarithm of 1 + input, ln(1+in).
        * - :doc:`af.log2() <functions/log2>`
            - Evaluate the base 2 logarithm.
        * - :doc:`af.logical_and() <functions/logical_and>`
            - Evaluate the logical and between two arrays
        * - :doc:`af.logical_not() <functions/logical_not>`
            - Evaluate the logical not of an array
        * - :doc:`af.logical_or() <functions/logical_or>`
            - Evaluate the logical or between two arrays
        * - :doc:`af.lookup() <functions/lookup>`
            - Lookup values of an array by indexing with another array.
        * - :doc:`af.lower() <functions/lower>`
            - Return the lower triangular matrix from an input array.
        * - :doc:`af.lt() <functions/lt>`
            - Less than, an elementwise comparison of two arrays.
        * - :doc:`af.lu() <functions/lu>`
            - Perform LU decomposition.
        * - :doc:`af.matmul() <functions/matmul>`
            - Matrix multiplication.
        * - :doc:`af.max() <functions/max>`
            - Return the maximum along a given dimension.
        * - :doc:`af.maxfilt() <functions/maxfilt>`
            - Find maximum value from a window.
        * - :doc:`af.maxof() <functions/maxof>`
            - Elementwise maximum between two arrays
        * - :doc:`af.mean() <functions/mean>`
            - Find the mean of values in the input.
        * - :doc:`af.mean_shift() <functions/mean_shift>`
            - Edge-preserving smoothing filter commonly used in object tracking and image segmentation.
        * - :doc:`af.medfilt() <functions/medfilt>`
            - Median Filter.
        * - :doc:`af.medfilt1() <functions/medfilt1>`
            - 1D Median Filter.
        * - :doc:`af.medfilt2() <functions/medfilt2>`
            - 2D Median Filter.
        * - :doc:`af.median() <functions/median>`
            - Find the median of values in the input.
        * - :doc:`af.min() <functions/min>`
            - Return the minimum along a given dimension.
        * - :doc:`af.minfilt() <functions/minfilt>`
            - Find minimum value from a window.
        * - :doc:`af.minof() <functions/minof>`
            - Elementwise minimum between two arrays
        * - :doc:`af.mod() <functions/mod>`
            - Calculate the modulus.
        * - :doc:`af.moddims() <functions/moddims>`
            - Modify the dimensions of an array without changing the order of its elements.
        * - :doc:`af.mul() <functions/mul>`
            - Elementwise multiply.
        * - :doc:`af.nearest_neighbour() <functions/nearest_neighbour>`
            - Calculates which points in the train are nearest to each other point 
        * - :doc:`af.neg() <functions/neg>`
            - Negate an array.
        * - :doc:`af.neq() <functions/neq>`
            - Not equal to, an elementwise comparison of two arrays.
        * - :doc:`af.norm() <functions/norm>`
            - Find the norm of a matrix.
        * - :doc:`af.ones() <functions/ones>`
            - Creates an array filled with ones.
        * - :doc:`af.orb() <functions/orb>`
            - ORB Feature descriptor.
        * - :doc:`af.pad() <functions/pad>`
            - Pad an array.
        * - :doc:`af.pinverse() <functions/pinverse>`
            - Pseudo-invert (Moore-Penrose) a matrix.
        * - :doc:`af.pow() <functions/pow>`
            - Raise a base to a power (or exponent).
        * - :doc:`af.pow2() <functions/pow2>`
            - Raise 2 to a power (or exponent).
        * - :doc:`af.print_mem_info() <functions/print_mem_info>`
            - Prints buffer details from the ArrayFire Device Manager
        * - :doc:`af.product() <functions/product>`
            - Multiply array elements over a given dimension.
        * - :doc:`af.qr() <functions/qr>`
            - Perform QR decomposition.
        * - :doc:`af.randn() <functions/randn>`
            - Create a random array sampled from normal distribution.
        * - :doc:`af.randu() <functions/randu>`
            - Create a random array sampled from uniform distribution.
        * - :doc:`af.range() <functions/range>`
            - Generate an array with [0, n-1] values along the a specified dimension and tiled across other dimensions.
        * - :doc:`af.rank() <functions/rank>`
            - Find the rank of a matrix.
        * - :doc:`af.read_array() <functions/read_array>`
            - Load an array from a file.
        * - :doc:`af.real() <functions/real>`
            - Returns the real part of a complex array.
        * - :doc:`af.regions() <functions/regions>`
            - Find blobs in given image.
        * - :doc:`af.rem() <functions/rem>`
            - Calculate the remainder of a division.
        * - :doc:`af.reorder() <functions/reorder>`
            - Reorder an array.
        * - :doc:`af.replace() <functions/replace>`
            - Replace elements of an array with elements of another array.
        * - :doc:`af.reshape() <functions/reshape>`
            - Modify the dimensions of an array without changing the order of its elements
        * - :doc:`af.resize() <functions/resize>`
            - Resize an input image.
        * - :doc:`af.rgb2gray() <functions/rgb2gray>`
            - RGB to Grayscale colorspace converter.
        * - :doc:`af.rgb2hsv() <functions/rgb2hsv>`
            - RGB to HSV colorspace converter.
        * - :doc:`af.rgb2ycbcr() <functions/rgb2ycbcr>`
            - RGB to YCbCr colorspace converter.
        * - :doc:`af.root() <functions/root>`
            - Evaluate the nth root.
        * - :doc:`af.rotate() <functions/rotate>`
            - Rotate an input image or array.
        * - :doc:`af.round() <functions/round>`
            - Round numbers to the nearest integer.
        * - :doc:`af.rsqrt() <functions/rsqrt>`
            - Evaluate the reciprocal square root.
        * - :doc:`af.sat() <functions/sat>`
            - Summed Area Tables.
        * - :doc:`af.save_array() <functions/save_array>`
            - Save an array to a binary file
        * - :doc:`af.save_image() <functions/save_image>`
            - Save an array to disk as an image
        * - :doc:`af.save_image_memory() <functions/save_image_memory>`
            - Save an array to memory as an image using FreeImage stream
        * - :doc:`af.save_image_native() <functions/save_image_native>`
            - Save an image as is original type.
        * - :doc:`af.scale() <functions/scale>`
            - Scale an input image.
        * - :doc:`af.scan() <functions/scan>`
            - Scan an array (generalized) over a given dimension.
        * - :doc:`af.select() <functions/select>`
            - Select elements based on a conditional array.
        * - :doc:`af.set_backend() <functions/set_backend>`
            - Set the current backend
        * - :doc:`af.set_device() <functions/set_device>`
            - Change current device to specified device.
        * - :doc:`af.set_fft_plan_cache_size() <functions/set_fft_plan_cache_size>`
            - Sets fft plan cache size
        * - :doc:`af.set_intersect() <functions/set_intersect>`
            - Evaluate the intersection of two arrays
        * - :doc:`af.set_kernel_cache_directory() <functions/set_kernel_cache_directory>`
            - Sets the directory for JIT kernel caching
        * - :doc:`af.set_mem_step_size() <functions/set_mem_step_size>`
            - Get the minimum memory chunk size.
        * - :doc:`af.set_native_id() <functions/set_native_id>`
            - Set the CUDA device with given native id as the active device for ArrayFire
        * - :doc:`af.set_union() <functions/set_union>`
            - Evaluate the union of two arrays
        * - :doc:`af.set_unique() <functions/set_unique>`
            - Return the unique values in an array
        * - :doc:`af.shift() <functions/shift>`
            - Shift an array.
        * - :doc:`af.sift() <functions/sift>`
            - SIFT feature detector and descriptor extractor.
        * - :doc:`af.sign() <functions/sign>`
            - Return the sign of elements in an array.
        * - :doc:`af.sin() <functions/sin>`
            - Evaluate the sine function.
        * - :doc:`af.sinh() <functions/sinh>`
            - Evaluate the hyperbolic sine function.
        * - :doc:`af.skew() <functions/skew>`
            - Skew an input image.
        * - :doc:`af.sobel_operator() <functions/sobel_operator>`
            - Perform a 2-D spatial gradient measurement on an image
        * - :doc:`af.solve() <functions/solve>`
            - Solve a system of equations.
        * - :doc:`af.sort() <functions/sort>`
            - Sort an array over a given dimension.
        * - :doc:`af.sqrt() <functions/sqrt>`
            - Evaluate the square root.
        * - :doc:`af.sttdev() <functions/sttdev>`
            - Find the standard deviation of values in the input.
        * - :doc:`af.sub() <functions/sub>`
            - Elementwise subtraction.
        * - :doc:`af.sum() <functions/sum>`
            - Sum array elements over a given dimension.
        * - :doc:`af.susan() <functions/susan>`
            - SUSAN corner detector.
        * - :doc:`af.svd() <functions/svd>`
            - Perform singular value decomposition.
        * - :doc:`af.sync() <functions/sync>`
            - Blocks until all operations on device are finished.
        * - :doc:`af.tan() <functions/tan>`
            - Evaluate the tangent function.
        * - :doc:`af.tanh() <functions/tanh>`
            - Evaluate the hyperbolic tangent function.
        * - :doc:`af.tgamma() <functions/tgamma>`
            - Evaluate the gamma function.
        * - :doc:`af.tile() <functions/tile>`
            - Generate a tiled array by repeating an array's contents along a specified dimension.
        * - :doc:`af.transform() <functions/transform>`
            - Transform an input image.
        * - :doc:`af.transform_coordinates() <functions/transform_coordinates>`
            - Transform input coordinates to perspective.
        * - :doc:`af.translate() <functions/translate>`
            - Translate an input image.
        * - :doc:`af.transpose() <functions/transpose>`
            - Transpose a matrix.
        * - :doc:`af.trunc() <functions/trunc>`
            - Truncate numbers to nearest integer.
        * - :doc:`af.unwrap() <functions/unwrap>`
            - Rearrange windowed sections of an array into columns (or rows)
        * - :doc:`af.upper() <functions/upper>`
            - Return the upper triangular matrix from an input array.
        * - :doc:`af.where() <functions/where>`
            - Locate the indices of the non-zero values in an array.
        * - :doc:`af.wrap() <functions/wrap>`
            - Performs the opposite of af::unwrap().
        * - :doc:`af.zeros() <functions/zeros>`
            - Creates an array filled with zeros.


.. collapse:: Arrayfire Functions by Category

    .. list-table::

            * - :doc:`Array Creation <array_creation_functions>`
                - Functions in this category are used to initialize arrays with specific values or patterns.
            * - :doc:`Array Manipulation <array_manipulation_functions>`
                - These functions help modify the structure or arrangement of arrays.
            * - :doc:`Mathematical Operations <mathematical_operations_functions>`
                - Functions for performing fundamental arithmetic and mathematical operations on arrays.
            * - :doc:`Linear Algebra <linear_algebra_functions>`
                - Functions for performing linear algebra operations, essential in many scientific and engineering tasks.
            * - :doc:`Fourier Transforms <fourier_transforms_functions>`
                - Functions for performing Fourier analysis, essential for signal processing and frequency analysis.
            * - :doc:`Statistics <statistics_functions>`
                - Functions for computing statistical metrics and analyzing data distributions.
            * - :doc:`Data Reduction <data_reduction_functions>`
                - Functions for aggregating and reducing data to summarize or condense information.
            * - :doc:`Utilities <utilities_functions>`
                - General-purpose functions for managing arrays and devices.
            * - :doc:`Special Functions <special_functions>`
                - Functions for convolutions, creating and applying specific types of filters, commonly used in signal processing and analysis.

.. collapse:: Arrayfire Constants

    .. list-table::

        * - :doc:`af.BinaryOperator <constants/BinaryOperator>`
        * - :doc:`af.CannyThreshold <constants/CannyThreshold>`
        * - :doc:`af.Connectivity <constants/Connectivity>`
        * - :doc:`af.ConvDomain <constants/ConvDomain>`
        * - :doc:`af.ConvGradient <constants/ConvGradient>`
        * - :doc:`af.CSpace <constants/CSpace>`
        * - :doc:`af.Diffusion <constants/Diffusion>`
        * - :doc:`af.Dtype <constants/Dtype>`
            - ArrayFire supported datatypes
        * - :doc:`af.Flux <constants/Flux>`
        * - :doc:`af.ImageFormat <constants/ImageFormat>`
        * - :doc:`af.Interp <constants/Interp>`
        * - :doc:`af.IterativeDeconv <constants/IterativeDeconv>`
        * - :doc:`af.Match <constants/Match>`
        * - :doc:`af.MatProp <constants/MatProp>`
        * - :doc:`af.Norm <constants/Norm>`
        * - :doc:`af.Pad <constants/Pad>`
        * - :doc:`af.RandomEngineType <constants/RandomEngineType>`
        * - :doc:`af.TopK <constants/TopK>`
        * - :doc:`af.VarianceBias <constants/VarianceBias>`
        * - :doc:`af.YCCStd <constants/YCCStd>`

.. collapse:: Graphics (Coming Soon)

    .. list-table::

            * - **Rendering Function**
                - Rendering Function to draw images, plots etc
            * - **Window Function**
                - Window Creation, modification and destruction of functions

