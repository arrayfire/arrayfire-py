# [indexing1-snippet]

import arrayfire as af 

data = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

A = af.Array(data)
A = af.moddims(A,(4,4))

# [indexing1-endsnippet]


# [indexing2-snippet]

A[0,0] #Returns an array pointing to the first element


A[2,3] #WARN: avoid doing this. Demo only
# [indexing2-endsnippet]


# [indexing3-snippet]

ref0 = A[2,-1] # 14 second row last column
ref1 = A[2,-2] # 10 Second row, second to last(third) column
# [indexing3-endsnippet]


# [indexing4-snippet]

#Returns an array pointing to the third column
A[:,2]
# [indexing4-endsnippet]



# [indexing5-snippet]

#Returns an array pointing to the second row
A[1, :]
# [indexing5-endsnippet]



# [indexing6-snippet]

 #Returns an array pointing to the first two columns
A[:, 0:2]

# [indexing6-endsnippet]


# [indexing7-snippet]

reference = A[:, 1]
reference2 = A[0:3, 1]
reference3 = A[0:2, :]
# [indexing7-endsnippet]


# [indexing8-snippet]

copy = A[2, :]
copy2 = A[1:3:2, :]

hidx = [0, 1, 2]
idx = af.Array(hidx)
copy3 = A[idx, :]

# [indexing8-endsnippet]


# [indexing9-snippet]

inputA = af.constant(3,(10,10))
inputB = af.constant(2,(10,10))
data = af.constant(1,(10,10))

#Points to the second column of data. Does not allocate memory
ref = data[:,1]

# This call does NOT update data. Memory allocated in matmul
ref = af.matmul(inputA, inputB)
# reference does not point to the same memory as the data array

# [indexing9-endsnippet]


# [indexing10-snippet]

reference = A[:, 2]

A[:, 2] = 3.14
# [indexing10-endsnippet]


# [indexing11-snippet]

ref = A[:, 2]

A[:, 2] = 3.14
# [indexing11-endsnippet]


# [indexing12-snippet]

hidx = [4, 3, 4, 0]
hvals = [9.0, 8.0, 7.0, 6.0]

idx = af.Array(hidx)
vals = af.Array(hvals)
# [indexing12-endsnippet]


# [indexing13-snippet]

A = af.Array[1,2,3,4,5,6,7,8,9]
A = af.moddims(A,(3,3))
# 1.0000 4.0000 7.0000
# 2.0000 5.0000 8.0000
# 3.0000 6.0000 9.0000

print(A[0,0]) # first element
# 1.0000

print(A[0,1]) # first row, second column
# 4.0000
# [indexing13-endsnippet]

