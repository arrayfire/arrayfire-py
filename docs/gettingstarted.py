# [gettingstarted1-snippet]
# Arrays may be created using the array constructor and dimensioned
# as 1D, 2D, 3D; however, the values in these arrays will be undefined
import arrayfire as af

array = af.constant(0, (100,))
array_2d = af.constant(0, (10, 100))
array_3d = af.constant(0, (10, 10, 10))
# [gettingstarted1-endsnippet]


# [gettingstarted2-snippet]
import arrayfire as af

# Generate an array of size three filled with zeros.
# If no data type is specified, ArrayFire defaults to f32.
# The constant function generates the data on the device.
zeroes = af.constant(0, (3,))

# Generate a 1x4 array of uniformly distributed [0,1] random numbers
# The randu function generates the data on the device.
rand1 = af.randu((1, 4))

# Generate a 2x2 array (or matrix, if you prefer) of random numbers
# sampled from a normal distribution.
# The randn function generates data on the device.
rand2 = af.randu((2, 2))

# Generate a 3x3 identity matrix. The data is generated on the device.
iden = af.identity((3, 3))

# Lastly, create a 2x1 array (column vector) of uniformly distributed
# 32-bit complex numbers (c32 data type):
randcplx = af.randu((2, 1))
# [gettingstarted2-endsnippet]


# [gettingstarted3-snippet]
import arrayfire as af

# Create a six-element array on the host
hA = [0, 1, 2, 3, 4, 5]

# Which can be copied into an ArrayFire Array using the pointer copy
# constructor. Here we copy the data into a 2x3 matrix:
A = af.moddims(af.Array(hA), (2, 3))


# ArrayFire provides a convenince function for printing array
# objects in case you wish to see how the data is stored:
print(A)

# todo how to create complex numbers
# [gettingstarted3-endsnippet]


# [gettingstarted4-snippet]

import numpy as np
import pycuda.driver as cuda

import arrayfire as af

# Create an array on the host
host_ptr = af.Array([0, 1, 2, 3, 4, 5])


# Create an ArrayFire array 'a' from host_ptr (2x3 matrix)
A = af.moddims(host_ptr, (2, 3))

# Allocate CUDA device memory and copy data from host to device
device_ptr = cuda.mem_alloc(host_ptr.nbytes)
cuda.memcpy_htod(device_ptr, host_ptr)

# Create an ArrayFire array 'b' from CUDA-allocated device memory (2x3 matrix)
b = af.Array(device_ptr, dims=(2, 3), is_device=True)

# Note: ArrayFire takes ownership of `device_ptr`, so no need to free it manually

# Clean up CUDA resources (not necessary due to Python's automatic memory management)
# cuda.mem_free(device_ptr)
# [gettingstarted4-endsnippet]


# [gettingstarted5-snippet]

import arrayfire as af

# Generate two arrays
a = af.randu((2, 2))  # Create a 2x2 array with random numbers between [0, 1]
b = af.constant(1, (2, 1))  # Create a 2x1 array filled with constant value 1

# Print arrays 'a' and 'b' to the console
print("Array 'a':", a)

print("Array 'b':", b)

# Print the results of an expression involving arrays
result = a.col(0) + b + 0.4  # Perform operation: first column of 'a' + 'b' + 0.4
print("Result of expression (a.col(0) + b + 0.4):")
print(result)
# [gettingstarted5-endsnippet]


# [gettingstarted6-snippet]

import arrayfire as af

# Create a 4x5x2 array of uniformly distributed random numbers
a = af.randu((4, 5, 2))

# Determine the number of dimensions using the `numdims()` function
print("numdims(a):", a.numdims())  # Print the number of dimensions (should be 3)

# Print the size of the individual dimensions using the `dims()` function
print("dims =", a.dims())  # Print dimensions as a tuple (4, 5, 2)

# Alternatively, access dimensions using a dim4 object
dims = a.dims()
print("dims =", dims[0], dims[1])  # Print dimensions separately (4, 5)
# [gettingstarted6-endsnippet]


# [gettingstarted7-snippet]

import arrayfire as af

# Create an example ArrayFire array 'a'
a = af.randu((4, 5))  # Example array of dtype float32

# Get the type stored in the array
print("underlying type:", a.type())

# Check if the array contains complex or real values
print("is complex?", a.iscomplex(), "   is real?", a.isreal())

# Check if the array is a vector, column vector, or row vector
print("is vector?", a.isvector(), "  column?", a.iscolumn(), "  row?", a.isrow())

# Check if the array is empty, and determine its total elements and memory usage
print("empty?", a.isempty(), "  total elements:", a.elements(), "  bytes:", a.bytes())
# [gettingstarted7-endsnippet]


# [gettingstarted8-snippet]

import arrayfire as af

# Generate a 3x3 array of uniformly distributed random numbers
R = af.randu((3, 3))
print(af.constant(1, (3, 3)) + af.join(af.sin(R)))  # will be c32

# Rescale complex values to unit circle
a = af.randn(5)
print(a / af.abs(a))

# Calculate L2 norm of vectors
X = af.randn((3, 4))
print(af.sqrt(af.sum(af.pow(X, 2))))  # norm of every column vector
print(af.sqrt(af.sum(af.pow(X, 2), 0)))  # same as above
print(af.sqrt(af.sum(af.pow(X, 2), 1)))  # norm of every row vector

# [gettingstarted8-endsnippet]


# [gettingstarted9-snippet]

import math

import arrayfire as af

# Generate a 5x5 array of uniformly distributed random numbers
A = af.randu((5, 5))

# Set elements in A greater than 0.5 to NaN
A[af.where(A > 0.5)] = af.NaN

# Generate arrays x and y with 10 million random numbers each
x = af.randu(int(10e6))
y = af.randu(int(10e6))

# Estimate Pi using Monte Carlo method
pi_est = 4 * af.sum(af.hypot(x, y) < 1) / 10e6

# Print the estimation error compared to math.pi
print("estimation error:", abs(math.pi - pi_est))
# [gettingstarted9-endsnippet]


# [gettingstarted10-snippet]

import arrayfire as af

# Create an array consisting of 3 random numbers of type f32 (float)
a = af.randu(3)

# Copy array data from device to host
host_a = a.host_ptr()  # Get host pointer
print("host_a[2] =", host_a[2])  # Access host data as a normal array
a.unlock()  # Unlock array to allow garbage collection if necessary

# Access device memory for CUDA kernel
d_cuda = a.device_ptr()  # Get device pointer (no need to free)
value = af.sum(d_cuda[2])  # Access device memory data
print("d_cuda[2] =", value)

# For OpenCL, accessing memory is similar but with a different syntax
# Note: ArrayFire handles these details internally, no explicit OpenCL handling in Python

# No need to free pointers in ArrayFire Python interface as memory management is automatic
# [gettingstarted10-endsnippet]


# [gettingstarted11-snippet]

import arrayfire as af

# Create an array consisting of 3 random numbers
a = af.randu(3)

# Get the scalar value of the array
val = a.scalar()

# Print the scalar value
print(f"scalar value: {val}")
# [gettingstarted11-endsnippet]


# [gettingstarted12-snippet]

import arrayfire as af

# Define host arrays
h_A = [1, 1, 0, 0, 4, 0, 0, 2, 0]
h_B = [1, 0, 1, 0, 1, 0, 1, 1, 1]

# Create ArrayFire arrays A and B from host arrays
A = af.Array(h_A, dims=(3, 3))
B = af.Array(h_B, dims=(3, 3))

# Print arrays A and B
print(A)
print(B)

# Perform bitwise operations
A_and_B = A & B
A_or_B = A | B
A_xor_B = A ^ B

# Print results of bitwise operations
print(A_and_B)
print(A_or_B)
print(A_xor_B)
# [gettingstarted12-endsnippet]


# [gettingstarted13-snippet]

import arrayfire as af


def main():
    # Generate random values
    a = af.randu(10000, dtype=af.Dtype.f32)

    # Sum all the values
    result = af.sum(a)
    print(f"sum: {result}\n")


# [gettingstarted13-endsnippet]
