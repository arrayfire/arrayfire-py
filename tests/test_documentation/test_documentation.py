import pytest
import arrayfire as af
import math




def test_array_shapes():
    # [gettingstarted1-snippet]
    # Arrays may be created using the array constructor and dimensioned
    # as 1D, 2D, 3D; however, the values in these arrays will be undefined
    import arrayfire as af

    array = af.constant(0, (100,))
    array_2d = af.constant(0, (10, 100))
    array_3d = af.constant(0, (10, 10, 10))
    # [gettingstarted1-endsnippet]
    assert array.shape == (100,)  # Check shape of 1D array
    assert array_2d.shape == (10, 100)  # Check shape of 2D array
    assert array_3d.shape == (10, 10, 10)  # Check shape of 3D array


    # [pi-example-simple-snippet]
    # Monte Carlo estimation of pi
def calc_pi_device(samples) -> float:
    # Simple, array based API
    # Generate uniformly distributed random numers
    x = af.randu(samples)
    y = af.randu(samples)
    # Supports Just In Time Compilation
    # The following line generates a single kernel
    within_unit_circle = (x * x + y * y) < 1
    # Intuitive function names
    return 4 * af.count(within_unit_circle) / samples
    # [pi-example-simple-endsnippet]

def test_calc_pi_device():
    samples = 100000
    x = af.randu(samples)
    y = af.randu(samples)
    within_unit_circle = (x * x + y * y) < 1
    result = 4 * af.count(within_unit_circle) / samples
    assert isinstance(result, float)
    error = abs(result - math.pi)
    tolerance = 0.01
    assert error < tolerance, f"Error ({error}) exceeds tolerance ({tolerance})"


# [gettingstarted2-snippet]
import arrayfire as af

# Generate an array of size three filled with zeros.
# If no data type is specified, ArrayFire defaults to f32.
# The constant function generates the data on the device.
zeroes = af.constant(0,(3,))

# Generate a 1x4 array of uniformly distributed [0,1] random numbers
# The randu function generates the data on the device.
rand1 = af.randu((1,4)) 

# Generate a 2x2 array (or matrix, if you prefer) of random numbers
# sampled from a normal distribution.
# The randn function generates data on the device.
rand2 = af.randu((2,2)) 

# Generate a 3x3 identity matrix. The data is generated on the device.
iden = af.identity((3,3))

# Lastly, create a 2x1 array (column vector) of uniformly distributed
# 32-bit complex numbers (c32 data type):
randcplx = af.randu((2,1))
# [gettingstarted2-endsnippet]

import pytest
import arrayfire as af

def test_arrayfire_operations():
    # Generate an array of size three filled with zeros
    zeroes = af.constant(0, (3,))
    assert zeroes.shape == (3,)  # Check shape
    
    # Generate a 1x4 array of uniformly distributed [0,1] random numbers
    rand1 = af.randu((1, 4))
    assert rand1.shape == (1, 4)  # Check shape
    
    # Generate a 2x2 array of random numbers sampled from a normal distribution
    rand2 = af.randn((2, 2))
    assert rand2.shape == (2, 2)  # Check shape
    
    # Generate a 3x3 identity matrix
    iden = af.identity((3,3))
    assert iden.shape == (3, 3)  # Check shape
    
    # Generate a 2x1 array (column vector) of uniformly distributed 32-bit complex numbers
    randcplx = af.randu((2, 1))
    assert randcplx.shape == (2, )  # Check shape

# [gettingstarted3-snippet]
import arrayfire as af
# Create a six-element array on the host
hA = ([0, 1, 2, 3, 4, 5])

# Which can be copied into an ArrayFire Array using the pointer copy
# constructor. Here we copy the data into a 2x3 matrix:
A = af.moddims(af.Array(hA),(2,3))


# ArrayFire provides a convenince function for printing array
# objects in case you wish to see how the data is stored:
print(A)

#todo how to create complex numbers
# [gettingstarted3-endsnippet]


def test_arrayfire_conversion():
    # Create a six-element array on the host
    hA = ([0, 1, 2, 3, 4, 5])
    
    # Copy data from host array to an ArrayFire array and reshape to 2x3 matrix
    A = af.moddims(af.Array(hA),(2,3))
    
    # Assert that the shape of A is (2, 3)
    assert A.shape == (2, 3)
    
    # Assert that the elements in A match hA
    for i in range(2):
        for j in range(3):
            assert A[i, j] == hA[i * 3 + j]

# [gettingstarted11-snippet]

import arrayfire as af

# Create an array consisting of 3 random numbers
a = af.randu(3)

# Get the scalar value of the array
val = a.scalar()

# Print the scalar value
print(f"scalar value: {val}")
# [gettingstarted11-endsnippet]


import pytest
import arrayfire as af

def test_arrayfire_scalar_value():
    # Create an array consisting of 3 random numbers
    a = af.randu(3)
    
    # Get the scalar value of the array
    val = a.scalar()
    
    # Assert that the scalar value is a float
    assert isinstance(val, float)
    
    # Assert that the scalar value is between 0 and 1 (inclusive)
    assert 0 <= val <= 1

def test_vectorization():

    # [vectorization2-snippet]

    import arrayfire as af

    #[0, 9]
    a = af.range(10)

    # [1, 10]
    a = a+ 1
    # [vectorization2-endsnippet]
    # Assertion: Verify the elements of the array 'a'
    expected_result = af.Array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    assert a == expected_result

def test_apply_filter():
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
    assert filtered_weights.shape == (5, 5)
    



def test_filtered_weights():  
    # [vectorization10-snippet]

    import arrayfire as af

    # Create the filter and weight vectors
    filter = af.randu((1, 5))   # Shape: 1x5
    weights = af.randu((5, 5))  # Shape: 5x5

    # Transpose the filter to align dimensions for broadcasting
    filter_transposed = af.transpose(filter)  # Shape: 5x1

    # Element-wise multiplication with broadcasting
    filtered_weights = filter_transposed * weights

    expected_shape = (5, 5)  # Expected shape of filtered_weights
    
    # Assertions
    assert filtered_weights.shape == expected_shape

    # Print the filtered weights array
    print("Filtered weights:")
    print(filtered_weights)
    # [vectorization10-endsnippet]

def test_flatten_array():
    # [manipulation1-snippet]

    import arrayfire as af

    # Creates a 3x3 array filled with random numbers between [0, 1)
    a = af.randu((3, 3))

    # Flattens the array 'a' into a 1-dimensional column vector
    flat_a = af.flat(a)

    # Display the original array 'a'
    print(a)

    # [manipulation1-endsnippet]
    assert flat_a.shape == (9,)  # Check if it's a 1-dimensional array
    assert len(flat_a) == 9  # Check if it has 9 elements (3x3 array)


def test_flip_array():
   
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
    assert flip_a.shape == a.shape
    assert af.flip(flip_a) == a
    assert af.min(a) >= 0
    assert af.max(a) < 1
    assert af.min(flip_a) >= 0
    assert af.max(flip_a) < 1

def test_join_array():
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
    assert a_join.shape == (10,)



def test_moddims_operations():
    # [manipulation4-snippet]

    import arrayfire as af

    a = af.randu((8,))

    print(a)

    moddims_a = af.moddims(a,(2,4))

    print(moddims_a)

    moddims_b = af.moddims(a,(len(a),))
    print(moddims_b)

    # [manipulation4-endsnippet]
    assert moddims_a.shape == (2, 4)
    assert moddims_b.shape == (8,)
    assert a == af.moddims(moddims_a, (8,))
    assert a == moddims_b



def test_arrayfire_shift():
    # [manipulation6-snippet]

    import arrayfire as af

    a = af.randu((3,5))
    print(a)

    a_shift = af.shift(a,(0,2))
    print(a_shift)

    a_shift1 = af.shift(a,(-1,2))
    print(a_shift1)

    # [manipulation6-endsnippet]

    # Check if arrays are equal by comparing element-wise
    assert a != a_shift 
    assert a != a_shift1
    assert a_shift.shape == (3,5)
    assert a_shift1.shape == (3,5)


def transpose_arrayifre():
    # [manipulation8-snippet]

    import arrayfire as af

    a = af.randu((3,3))
    print(a)  #[3 3 1 1]

    ''' 0.3949     0.8465     0.3709
        0.3561     0.9399     0.2751
        0.6097     0.6802     0.2720'''
        

    a_transpose = af.transpose(a)
    print(a_transpose) #[3 3 1 1]

    ''' 0.3949     0.3561     0.6097
            0.8465     0.9399     0.6802
            0.3709     0.2751     0.2720'''
    # [manipulation8-endsnippet]
    # Convert arrays to Python lists for comparison
    a_list = a.to_array().tolist()
    a_transpose_list = a_transpose.to_array().tolist()

    # Compute the expected transpose manually
    expected_a_transpose = list(zip(*a_list))

    # Check if the transpose operation is correct
    assert a_transpose_list == expected_a_transpose




def test_moddims():
    # [indexing1-snippet]

    import arrayfire as af 

    data = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

    A = af.Array(data)
    A = af.moddims(A,(4,4))

# [indexing1-endsnippet]
    expected_result = [
        [0, 1, 2, 3],
        [4, 5, 6, 7],
        [8, 9, 10, 11],
        [12, 13, 14, 15]
    ]
        
    dims = A.shape
    A_list = [[A[i, j] for j in range(dims[1])] for i in range(dims[0])]

    # Check if the reshaped array matches the expected result
    assert A_list == expected_result


    

