#!/usr/bin/python

#######################################################
# Copyright (c) 2015, ArrayFire
# All rights reserved.
#
# This file is distributed under 3-clause BSD license.
# The complete license agreement can be obtained at:
# http://arrayfire.com/licenses/BSD-3-Clause
########################################################

from common import *

ITERATIONS = 1

sqrt2 = math.sqrt(2.0)

@pytest.mark.parametrize(
    "pkgid", IDS, ids=IDS
)
class TestBlackScholes:
    def test_black_scholes(self, benchmark, pkgid):
        initialize_package(pkgid)
        setup = lambda: (generate_arrays(pkgid, 5), {})
        pkg = PKGDICT[pkgid]

        benchmark.extra_info["description"] = f"{NSIZE}x{NSIZE} Matrix"
        result = benchmark.pedantic(
            target=FUNCS[pkg.__name__],
            setup=setup,
            rounds=ROUNDS,
            iterations=ITERATIONS
        )

def black_scholes_numpy(S, X, R, V, T):
    # S = Underlying stock price
    # X = Strike Price
    # R = Risk free rate of interest
    # V = Volatility
    # T = Time to maturity
    def cnd(x):
        temp = (x > 0)
        erf = lambda arr : np.exp(-arr * arr)
        return temp * (0.5 + erf(x/sqrt2)/2) + (1 - temp) * (0.5 - erf((-x)/sqrt2)/2)
    
    d1 = np.log(S / X)
    d1 = d1 + (R + (V * V) * 0.5) * T
    d1 = d1 / (V * np.sqrt(T))

    d2 = d1 - (V * np.sqrt(T))
    cnd_d1 = cnd(d1)
    cnd_d2 = cnd(d2)

    C = S * cnd_d1 - (X * np.exp((-R) * T) * cnd_d2)
    P = X * np.exp((-R) * T) * (1 - cnd_d2) - (S * (1 -cnd_d1))

    return (C, P)

def black_scholes_dpnp(S, X, R, V, T):
    def cnd(x):
        temp = (x > 0)
        return temp * (0.5 + dpnp.erf(x/sqrt2)/2) + (1 - temp) * (0.5 - dpnp.erf((-x)/sqrt2)/2)

    d1 = dpnp.log(S / X)
    d1 = d1 + (R + (V * V) * 0.5) * T
    d1 = d1 / (V * dpnp.sqrt(T))

    d2 = d1 - (V * dpnp.sqrt(T))
    cnd_d1 = cnd(d1)
    cnd_d2 = cnd(d2)

    C = S * cnd_d1 - (X * dpnp.exp((-R) * T) * cnd_d2)
    P = X * dpnp.exp((-R) * T) * (1 - cnd_d2) - (S * (1 -cnd_d1))

    return (C, P)

def black_scholes_cupy(S, X, R, V, T):
    def cnd(x):
        temp = (x > 0)
        erf = lambda arr : cupy.exp(-arr * arr)
        return temp * (0.5 + erf(x/sqrt2)/2) + (1 - temp) * (0.5 - erf((-x)/sqrt2)/2)
    
    d1 = cupy.log(S / X)
    d1 = d1 + (R + (V * V) * 0.5) * T
    d1 = d1 / (V * cupy.sqrt(T))

    d2 = d1 - (V * cupy.sqrt(T))
    cnd_d1 = cnd(d1)
    cnd_d2 = cnd(d2)

    C = S * cnd_d1 - (X * cupy.exp((-R) * T) * cnd_d2)
    P = X * cupy.exp((-R) * T) * (1 - cnd_d2) - (S * (1 -cnd_d1))

    cupy.cuda.runtime.deviceSynchronize()

    return (C, P)

def black_scholes_arrayfire(S, X, R, V, T):
    def cnd(x):
        temp = (x > 0)
        return temp * (0.5 + af.erf(x/sqrt2)/2) + (1 - temp) * (0.5 - af.erf((-x)/sqrt2)/2)

    d1 = af.log(S / X)
    d1 = d1 + (R + (V * V) * 0.5) * T
    d1 = d1 / (V * af.sqrt(T))

    d2 = d1 - (V * af.sqrt(T))
    cnd_d1 = cnd(d1)
    cnd_d2 = cnd(d2)

    C = S * cnd_d1 - (X * af.exp((-R) * T) * cnd_d2)
    P = X * af.exp((-R) * T) * (1 - cnd_d2) - (S * (1 -cnd_d1))

    af.eval(C)
    af.eval(P)
    af.sync()

    return (C, P)


def generate_arrays(pkgid, count):
    arr_list = []
    pkg = PKGDICT[pkgid]
    pkg = pkg.__name__
    if "cupy" == pkg:
        for i in range(count):
            arr_list.append(cupy.random.rand(NSIZE, NSIZE, dtype=DTYPE))
        cupy.cuda.runtime.deviceSynchronize()
    elif "arrayfire" == pkg:
        af.device_gc()
        for i in range(count):  
            x = af.randu((NSIZE, NSIZE), dtype=getattr(af, DTYPE))
            af.eval(x)
            arr_list.append(x)
        af.sync()
    elif "dpnp" == pkg:
        for i in range(count):
            arr_list.append(dpnp.random.rand(NSIZE, NSIZE).astype(DTYPE))
    elif "numpy" == pkg:
        for i in range(count):
            arr_list.append(np.random.rand(NSIZE, NSIZE).astype(DTYPE))

    return arr_list

FUNCS = { "dpnp" : black_scholes_dpnp, "numpy" : black_scholes_numpy, \
         "cupy" : black_scholes_cupy , "arrayfire" : black_scholes_arrayfire}