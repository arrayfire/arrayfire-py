# cython: language_level=3
# -*- coding: utf-8 -*-
# *****************************************************************************
# Copyright (c) 2016-2024, Intel Corporation
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# - Redistributions of source code must retain the above copyright notice,
#   this list of conditions and the following disclaimer.
# - Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
# THE POSSIBILITY OF SUCH DAMAGE.
# *****************************************************************************

from common import *

ITERATIONS = 1


def generate_arrays(pkgid, count):
    arr_list = []
    pkg = PKGDICT[pkgid]
    pkg = pkg.__name__
    if "cupy" == pkg:
        for i in range(count):
            arr_list.append(cupy.random.rand(NSIZE, NSIZE, dtype=DTYPE))
        cupy.cuda.runtime.deviceSynchronize()
    elif "arrayfire" == pkg:
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
    elif "cupynumeric" == pkg:
        for i in range(count):
            arr_list.append(cupynumeric.random.rand(NSIZE, NSIZE).astype(DTYPE))

    return arr_list


@pytest.mark.parametrize("pkgid", IDS, ids=IDS)
class TestFFT:
    def test_fft(self, benchmark, pkgid):
        initialize_package(pkgid)
        setup = lambda: (generate_arrays(pkgid, 1), {})
        pkg = PKGDICT[pkgid]

        benchmark.extra_info["description"] = f"{NSIZE}x{NSIZE} Matrix"
        result = benchmark.pedantic(target=FUNCS[pkg.__name__], setup=setup, rounds=ROUNDS, iterations=ITERATIONS)


def fft_af(arr):
    res = af.fft(arr)
    af.eval(res)
    af.sync()

    return res


def fft_np(arr):
    return np.fft.fft(arr)


def fft_dpnp(arr):
    return dpnp.fft.fft(arr)


def fft_cupy(arr):
    res = cupy.fft.fft(arr)
    cupy.cuda.runtime.deviceSynchronize()
    return res

def fft_cupynumeric(arr):
    return cupynumeric.fft.fft(arr)

FUNCS = {"dpnp": fft_dpnp, "numpy": fft_np, "cupy": fft_cupy, "arrayfire": fft_af, "cupynumeric": fft_cupynumeric}
