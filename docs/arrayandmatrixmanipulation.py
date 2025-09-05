# [manipulation1-snippet]

import arrayfire as af

# Creates a 3x3 array filled with random numbers between [0, 1)
a = af.randu((3, 3))

# Flattens the array 'a' into a 1-dimensional column vector
flat_a = af.flat(a)

# Display the original array 'a'
print(a)

# [manipulation1-endsnippet]


# [manipulation2-snippet]


import arrayfire as af

# Generate a 5x2 array of uniformly distributed random numbers between [0, 1)
a = af.randu((5, 2))

# Print the original array 'a'
print("Original array 'a' [5 2 1 1]")
print(a)

# Flip the array 'a' along both axes (rows and columns)
flip_a = af.flip(a)

# Print the flipped array 'flip_a'
print("\nFlipped array 'flip_a' [5 2 1 1]")
print(flip_a)

# [manipulation2-endsnippet]


# [manipulation3-snippet]

import arrayfire as af

# Generate a 1-dimensional array 'a' of size 5 filled with uniformly distributed random numbers between [0, 1)
a = af.randu((5,))

# Print the original array 'a'
print("Original array 'a' [5 1 1 1]")
print(a)

# Join the array 'a' with itself along axis 0
a_join = af.join(0, a, a)

# Print the joined array 'a_join'
print("\nJoined array 'a_join' [10 1 1 1]")
print(a_join)
# [manipulation3-endsnippet]


# [manipulation4-snippet]

import arrayfire as af

a = af.randu((8,))

print(a)

moddims_a = af.moddims(a, (2, 4))

print(moddims_a)

moddims_b = af.moddims(a, (len(a),))
print(moddims_b)

# [manipulation4-endsnippet]


# [manipulation5-snippet]


import arrayfire as af

a = af.randu((2, 2, 3, 1))

print(a)

a_reorder = af.reorder(a, ())
# [manipulation5-endsnippet]

# [manipulation6-snippet]

import arrayfire as af

a = af.randu((3, 5))
print(a)

a_shift = af.shift(a, (0, 2))
print(a_shift)

a_shift1 = af.shift(a, (-1, 2))
print(a_shift1)

# [manipulation6-endsnippet]


# [manipulation7-snippet]

import arrayfire as af

a = af.randu((3,))  # [3,1,1,1]

print(a)

a_tile = af.tile(a, (2,))
print(a_tile)

a_tile1 = af.tile(a, (2, 2))
print(a_tile1)

a_tile2 = af.tile(a, (1, 2, 3))
print(a_tile2)
# [manipulation7-endsnippet]


# [manipulation8-snippet]

import arrayfire as af

a = af.randu((3, 3))
print(a)  # [3 3 1 1]

""" 0.3949     0.8465     0.3709
    0.3561     0.9399     0.2751
    0.6097     0.6802     0.2720"""


a_transpose = af.transpose(a)
print(a_transpose)  # [3 3 1 1]

""" 0.3949     0.3561     0.6097
        0.8465     0.9399     0.6802
        0.3709     0.2751     0.2720"""
# [manipulation8-endsnippet]
