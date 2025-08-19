Functions
=========

Documentation grouped by category:


.. collapse:: Arrayfire Classes

    .. list-table::

        * - `af.Array`
            - Represents an ArrayFire array


.. collapse:: Arrayfire Functions

    .. list-table::

        * - :doc:`af.array() <functions/array>`
            - Creates an array from a list or other data structure.
        * - :doc:`af.zeros() <functions/zeros>`
            - Creates an array filled with zeros.
        * - :doc:`af.ones() <functions/ones>`
            - Creates an array filled with ones.
        * - :doc:`af.constant() <functions/constant>`
            - Creates an array filled with a scalar value.
        * - :doc:`af.iota() <functions/iota>`
            - Creates an array filled with a range of linear indices along multiple dimensions
        * - :doc:`af.range() <functions/range>`
            - Creates an array filled with a range of linear indices along a dimension.
        * - :doc:`af.identity() <functions/identity>`
            - Creates an identity matrix or batch of identity matrices.
        * - :doc:`af.add() <functions/add>`
            - Performs element-wise addition.
        * - :doc:`af.subtract() <functions/subtract>`
            - Performs element-wise subtraction.
        * - :doc:`af.multiply() <functions/multiply>`
            - Performs element-wise multiplication.
        * - :doc:`af.divide() <functions/divide>`
            - Performs element-wise division.
        * - :doc:`af.mod() <functions/mod>`
            - Calculate the modulus of two arrays or a scalar and an array.
        * - :doc:`af.sqrt() <functions/sqrt>`
            - Computes the square root of each element.
        * - :doc:`af.exp() <functions/exp>`
            - Computes the exponential of each element.
        * - :doc:`af.log() <functions/log>`
            - Computes the natural logarithm of each element.
        * - :doc:`af.accum() <functions/accum>`
            - Calculate the cumulative sum of elements along a specified dimension.
        * - :doc:`af.sum() <functions/sum>`
            - Computes the sum of elements.
        * - :doc:`af.product() <functions/product>`
            - Computes the product of elements.
        * - :doc:`af.diff1() <functions/diff1>`
            - Computes the first-order differences of an ArrayFire array along a specified dimension.
        * - :doc:`af.diff2() <functions/diff2>`
            - Computes the second-order differences of an ArrayFire array along a specified dimension.
        * - :doc:`af.gradient() <functions/gradient>`
            - Computes the horizontal and vertical gradients of a 2D ArrayFire array or a batch of 2D arrays.
        * - :doc:`af.mean() <functions/mean>`
            - Computes the mean of elements.
        * - :doc:`af.median() <functions/median>`
            - Computes the median value.
        * - :doc:`af.stdev() <functions/sttdev>`
            - Computes the standard deviation.
        * - :doc:`af.min() <functions/min>`
            - Finds the minimum value.
        * - :doc:`af.max() <functions/max>`
            - Finds the maximum value.
        * - :doc:`af.imin() <functions/imin>`
            - Finds the minimum value.
        * - :doc:`af.imax() <functions/imax>`
            - Finds the maximum value.
        * - :doc:`af.all_true() <functions/all_true>`
            - Check if all the elements along a specified dimension are true.
        * - :doc:`af.any_true() <functions/any_true>`
            - Check if any of the elements along a specified dimension are true.
        * - :doc:`af.isinf() <functions/isinf>`
            - Returns a boolean array with entries as the boolean result from checking for infinity
        * - :doc:`af.randu() <functions/randu>`
            - Creates an array with random uniform values.
        * - :doc:`af.randn() <functions/randn>`
            - Creates an array with random normal values.
        * - :doc:`af.inv() <functions/inv>`
            - Computes the inverse of a matrix.
        * - :doc:`af.dot() <functions/dot>`
            - Computes the dot product of two arrays.
        * - :doc:`af.matmul() <functions/matmul>`
            - Matrix multiplication.
        * - :doc:`af.gemm() <functions/gemm>`
            - General matrix multiplication.
        * - :doc:`af.eig() <functions/eig>`
            - Computes eigenvalues and eigenvectors.
        * - :doc:`af.det() <functions/det>`
            - Computes the determinant of a matrix.
        * - :doc:`af.fft() <functions/fft>`
            - Computes the Fast Fourier Transform.
        * - :doc:`af.ifft() <functions/ifft>`
            - Computes the Inverse Fast Fourier Transform.
        * - :doc:`af.count() <functions/count>`
            - Count the number of non-zero elements in an ArrayFire array along a specified dimension.
        * - :doc:`af.sort() <functions/sort>`
            - Sorts the elements of an ArrayFire array along a specified dimension.
        * - :doc:`af.set_intersect() <functions/set_intersect>`
            - Calculates the intersection of two ArrayFire arrays, returning elements common to both arrays.
        * - :doc:`af.set_union() <functions/set_union>`
            - Computes the union of two 1D ArrayFire arrays, effectively combining the elements from both arrays and removing duplicates.
        * - :doc:`af.set_unique() <functions/set_unique>`
            - Extracts unique elements from a 1D ArrayFire array.
        * - :doc:`af.pad() <functions/pad>`
            - Pads an ArrayFire array with specified sizes of padding around its edges and fills the padding with a specified value.
        * - :doc:`af.orb() <functions/orb>`
            - Extracts ORB features and their descriptors from an image.
        * - :doc:`af.sift() <functions/sift>`
            - Extracts SIFT features and their descriptors from an image using the ArrayFire library.
        * - :doc:`af.fast() <functions/fast>`
            - Detects corners and interest points in an image using the Features from Accelerated Segment Test algorithm.
        * - :doc:`af.dog() <functions/dog>`
            - Performs the Difference of Gaussians (DoG) operation on an image.
        * - :doc:`af.gloh() <functions/gloh>`
            - Implements the GLOH (Gradient Location and Orientation Histogram) feature detection and descriptor extraction for images.
        * - :doc:`af.harris() <functions/harris>`
            - Detects corners in an image using the Harris corner detection algorithm.
        * - :doc:`af.susan() <functions/susan>`
            - Detects corners and edges in an image using the SUSAN corner detection algorithm.
        * - :doc:`af.hamming_matcher() <functions/hamming_matcher>`
            - Finds the nearest neighbors for each descriptor in a query set from a training set, based on the Hamming distance.
        * - :doc:`af.nearest_neighbour() <functions/nearest_neighbour>`
            - Finds the nearest neighbors for each descriptor in a query set from a training set based on a specified metric.
        * - :doc:`af.upper() <functions/upper>`
            - Extract the upper triangular part of a given multi-dimensional ArrayFire array.
        * - :doc:`af.lower() <functions/lower>`
            - Extract the lower triangular part of a given multi-dimensional ArrayFire array.
        * - :doc:`af.diag() <functions/diag>`
            - Extract a diagonal from or create a diagonal matrix based on an input array.
        * - :doc:`af.transpose() <functions/transpose>`
            - Transposes an array.
        * - :doc:`af.join() <functions/join>`
            - Joins arrays along a specified dimension.
        * - :doc:`af.reorder() <functions/reorder>`
            - Reorders dimensions of an array.
        * - :doc:`af.slice() <functions/slice>`
            - Extracts a slice of an array.
        * - :doc:`af.reshape() <functions/reshape>`
            - Reshapes an array.
        * - :doc:`af.device() <functions/device>`
            - Returns the device identifier.
        * - :doc:`af.get_device() <functions/get_device>`
            - Matrix multiplication.
        * - :doc:`af.set_device() <functions/set_device>`
            - Gets the current device.
        * - :doc:`af.set_backend() <functions/set_backend>`
            - Sets the current backend.
        * - :doc:`af.get_backend() <functions/get_backend>`
            - Gets the current backend.
        * - :doc:`af.get() <functions/get>`
            - Copies data from the GPU to the CPU.


.. collapse:: Arrayfire Functions by Category

    .. list-table::

            * - **Array Creation**
                - Functions in this category are used to initialize arrays with specific values or patterns.
            * - **Array Manipulation**
                - These functions help modify the structure or arrangement of arrays.
            * - **Mathematical Operations**
                - Functions for performing fundamental arithmetic and mathematical operations on arrays.
            * - **Linear Algebra**
                - Functions for performing linear algebra operations, essential in many scientific and engineering tasks.
            * - **Fourier Transforms**
                - Functions for performing Fourier analysis, essential for signal processing and frequency analysis.
            * - **Statistics**
                - Functions for computing statistical metrics and analyzing data distributions.
            * - **Data Reduction**
                - Functions for aggregating and reducing data to summarize or condense information.
            * - **Utilities**
                - General-purpose functions for managing arrays and devices.
            * - **Special Functions**
                - Functions for creating and applying specific types of filters, commonly used in signal processing and analysis.


.. collapse:: Graphics

    .. list-table::

            * - **Rendering Function**
                - Rendering Function to draw images, plots etc
            * - **Window Function**
                - Window Creation, modification and destruction of functions
