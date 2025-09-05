# [vectorization1-snippet]
import arrayfire as af

# Create an ArrayFire array 'a' using af.range()
a = af.range(10)  # Creates an array [0, 1, 2, ..., 9]

# Loop through the elements of 'a' and increment each element by 1
for i in range(a.dims()[0]):
    a[i] = a[i] + 1  # Increment each element by 1

# Print the modified array 'a'
print("Modified array 'a':")
print(a)
# [vectorization1-endsnippet]


# [vectorization2-snippet]

import arrayfire as af

# [0, 9]
a = af.range(10)

# [1, 10]
a = a + 1
# [vectorization2-endsnippet]


# [vectorization3-snippet]

import arrayfire as af

# Define the filter coefficients as a list
g_coef = [1, 2, 1, 2, 4, 2, 1, 2, 1]

# Convert the coefficients list to an ArrayFire array and scale it
filter = (1.0 / 16.0) * af.Array(3, 3, g_coef)

# Generate a random signal array of dimensions WIDTH x HEIGHT x NUM
WIDTH = 100
HEIGHT = 100
NUM = 3
signal = af.randu(WIDTH, HEIGHT, NUM)

# Perform 2D convolution of signal with filter
conv = af.convolve2(signal, filter)

# Print the result if needed
print("Convolution result:")
print(conv)
# [vectorization3-endsnippet]


# [vectorization4-snippet]

import arrayfire as af

# Define dimensions
WIDTH = 256
HEIGHT = 256
NUM_IMAGES = 100

# Generate an array of 100 WIDTH x HEIGHT images of random numbers
imgs = af.randu((NUM_IMAGES, (WIDTH, HEIGHT)))

# Rotate all of the images in a single command (rotate by 45 degrees)
rot_imgs = af.rotate(imgs, 45)

# Print the shape of rot_imgs to verify the result
print("Shape of rotated images:", rot_imgs.shape())

# Optionally, print the rotated images
# print(rot_imgs)

# Optionally, display or further process `rot_imgs` as needed

# [vectorization4-endsnippet]


# [vectorization5-snippet]

import arrayfire as af

# Create an ArrayFire array 'a' using af.range()
a = af.range(10)  # Creates an array [0, 1, 2, ..., 9]

# Perform element-wise addition using vectorized operations
a = a + 1  # Increment each element by 1

# Print the modified array 'a'
print("Modified array 'a':")
print(a)
# [vectorization5-endsnippet]

# [vectorization7-snippet]

import arrayfire as af

# Calculate accumulative sum along columns of A
B = af.accum(A)


# [vectorization7-endsnippet]


# [vectorization9-snippet]

import arrayfire as af

# Create the filter and weight vectors
filter = af.randu((1, 5))
weights = af.randu((5, 5))

# Apply the filter using a for-loop equivalent
filtered_weights = af.constant(0, (5, 5))
for i in range(weights.shape[1]):
    filtered_weights[:, i] = af.matmul(filter, weights[:, i])

# Print the filtered weights array
print("Filtered weights:")
print(filtered_weights)
# [vectorization9-endsnippet]


# [vectorization10-snippet]

import arrayfire as af

# Create the filter and weight vectors
filter = af.randu((1, 5))  # Shape: 1x5
weights = af.randu((5, 5))  # Shape: 5x5

# Transpose the filter to align dimensions for broadcasting
filter_transposed = filter.T  # Shape: 5x1

# Element-wise multiplication with broadcasting
filtered_weights = filter_transposed * weights

# Print the filtered weights array
print("Filtered weights:")
print(filtered_weights)  # Incorrect
# [vectorization10-endsnippet]

# [vectorization11-snippet]

import arrayfire as af

# Create the filter and weight vectors
filter = af.randu((1, 5))  # Shape: 1x5
batched_filter = af.tile(filter, (1, 1, 5))  # batch on the third dimension
weights = af.randu((5, 5))  # Shape: 5x5

# Leverage matmul batching
filtered_weights = af.matmul(batched_filter, weights)  # shape 1x5x5
filtered_weights = af.moddims(filtered_weights, (5, 5))  # reshape to 2d 5x5

# Print the filtered weights array
print("Filtered weights:")
print(filtered_weights)
# [vectorization11-endsnippet]
