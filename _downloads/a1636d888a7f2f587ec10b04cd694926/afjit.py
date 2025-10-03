# [jit-snippet]

# As JIT is automatically enabled in ArrayFire, this version of the function
# forces each expression to be evaluated. If the eval() function calls are
# removed, then the execution of this code would be equivalent to the
# following function.

import time

import arrayfire as af

samples = int(9e8)
x = af.randu((samples))
y = af.randu((samples))


def pi_no_jit(x, y, samples):
    temp = x * x
    af.eval(temp)
    temp += y * y
    af.eval(temp)
    temp = af.sqrt(temp)
    af.eval(temp)
    temp = temp < 1
    af.eval(temp)
    return 4.0 * af.sum(temp) / samples


def pi_jit(x, y, samples):
    temp = af.sqrt(x * x + y * y) < 1
    af.eval(temp)
    return 4.0 * af.sum(temp) / samples


# Print device info
af.info()

# Time JIT code
start = time.perf_counter()
res = pi_jit(x, y, samples)
af.sync()
end = time.perf_counter()

print("jit:", end - start, res)
af.device_gc()

# Time no JIT code
start = time.perf_counter()
res = pi_no_jit(x, y, samples)
af.sync()
end = time.perf_counter()
print("no jit:", end - start, res)

# [jit-endsnippet]
