Special Functions
====================

Functions for convolutions, creating and applying specific types of filters, commonly used in signal processing and analysis.

.. list-table:: Functions

    * - :doc:`af.anisotropic_diffusion() <functions/anisotropic_diffusion>`
        - Anisotropic Smoothing Filter.
    * - :doc:`af.approx1() <functions/approx1>`
        - Interpolation across a single dimension.
    * - :doc:`af.approx1_uniform() <functions/approx1_uniform>`
        - Interpolation across a single dimension in uniform steps
    * - :doc:`af.approx2() <functions/approx2>`
        - Interpolation along two dimensions.
    * - :doc:`af.approx2_uniform() <functions/approx2_uniform>`
        - Interpolation along two dimensions in uniform steps
    * - :doc:`af.canny() <functions/canny>`
        - Canny Edge Detector.
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
    * - :doc:`af.color_space() <functions/color_space>`
        - Colorspace conversion function.
    * - :doc:`af.confidence_cc() <functions/confidence_cc>`
        - Segment image based on similar pixel characteristics.
    * - :doc:`af.dilate() <functions/dilate>`
        - Dilation(morphological operator) for images.
    * - :doc:`af.fir() <functions/fir>`
        - This function implements a Finite Impulse Filter.
    * - :doc:`af.gaussian_kernel() <functions/gaussian_kernel>`
        - Creates a Gaussian Kernel.
    * - :doc:`af.gloh() <functions/gloh>`
        - SIFT feature detector and GLOH descriptor extractor.
    * - :doc:`af.gradient() <functions/gradient>`
        - Calculate the gradients of the input
    * - :doc:`af.gray2rgb() <functions/gray2rgb>`
        - Grayscale to RGB colorspace converter.
    * - :doc:`af.hamming_matcher() <functions/hamming_matcher>`
        - Calculates Hamming distances between two 2-dimensional arrays
    * - :doc:`af.harris() <functions/harris>`
        - Harris corner detector.
    * - :doc:`af.hsv2rgb() <functions/hsv2rgb>`
        - HSV to RGB colorspace converter.
    * - :doc:`af.hypot() <functions/hypot>`
        - Evaluate the length of the hypotenuse of two inputs.
    * - :doc:`af.is_image_io_available() <functions/is_image_io_available>`
        - Checks if Image IO is available
    * - :doc:`af.iterative_deconv() <functions/iterative_deconv>`
        - Inverse Deconvolution using iterative methods
    * - :doc:`af.load_image() <functions/load_image>`
        - Load an image from disk to an array
    * - :doc:`af.load_image_memory() <functions/load_image_memory>`
        - Load an image from memory which is stored as a FreeImage stream
    * - :doc:`af.load_image_native() <functions/load_image_native>`
        - Load an image as is original type.
    * - :doc:`af.maxfilt() <functions/maxfilt>`
        - Find maximum value from a window.
    * - :doc:`af.mean_shift() <functions/mean_shift>`
        - Edge-preserving smoothing filter commonly used in object tracking and image segmentation.
    * - :doc:`af.medfilt() <functions/medfilt>`
        - Median Filter.
    * - :doc:`af.medfilt1() <functions/medfilt1>`
        - 1D Median Filter.
    * - :doc:`af.medfilt2() <functions/medfilt2>`
        - 2D Median Filter.
    * - :doc:`af.minfilt() <functions/minfilt>`
        - Find minimum value from a window.
    * - :doc:`af.nearest_neighbour() <functions/nearest_neighbour>`
        - Calculates which points in the train are nearest to each other point 
    * - :doc:`af.orb() <functions/orb>`
        - ORB Feature descriptor.
    * - :doc:`af.pad() <functions/pad>`
        - Pad an array.
    * - :doc:`af.regions() <functions/regions>`
        - Find blobs in given image.
    * - :doc:`af.resize() <functions/resize>`
        - Resize an input image.
    * - :doc:`af.rgb2gray() <functions/rgb2gray>`
        - RGB to Grayscale colorspace converter.
    * - :doc:`af.rgb2hsv() <functions/rgb2hsv>`
        - RGB to HSV colorspace converter.
    * - :doc:`af.rgb2ycbcr() <functions/rgb2ycbcr>`
        - RGB to YCbCr colorspace converter.
    * - :doc:`af.rotate() <functions/rotate>`
        - Rotate an input image or array.
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
    * - :doc:`af.sift() <functions/sift>`
        - SIFT feature detector and descriptor extractor.
    * - :doc:`af.sign() <functions/sign>`
        - Return the sign of elements in an array.
    * - :doc:`af.sin() <functions/sin>`
        - Evaluate the sine function.
    * - :doc:`af.skew() <functions/skew>`
        - Skew an input image.
    * - :doc:`af.sobel_operator() <functions/sobel_operator>`
        - Perform a 2-D spatial gradient measurement on an image
    * - :doc:`af.susan() <functions/susan>`
        - SUSAN corner detector.
    * - :doc:`af.transform() <functions/transform>`
        - Transform an input image.
    * - :doc:`af.transform_coordinates() <functions/transform_coordinates>`
        - Transform input coordinates to perspective.
    * - :doc:`af.translate() <functions/translate>`
        - Translate an input image.