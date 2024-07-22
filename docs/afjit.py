# [jit-snippet]

# As JIT is automatically enabled in ArrayFire, this version of the function
# forces each expression to be evaluated. If the eval() function calls are
# removed, then the execution of this code would be equivalent to the
# following function.

def pi_no_jit(x, y, temp, samples):
    temp = x * x
    temp.eval()
    temp += y * y
    temp.eval()
    temp = sqrt(temp)
    temp.eval()
    temp = temp < 1
    temp.eval()
    return 4.0 * sum(temp) / samples

def pi_jit(x, y, temp, samples):
    temp = sqrt(x * x + y * y) < 1
    temp.eval()
    return 4.0 * sum(temp) / samples

# [jit-endsnippet]