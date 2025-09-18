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

eps = 1e-3


def generate_arrays(pkgid, count, posdef=False):
    arr_list = []
    pkg = PKGDICT[pkgid]
    pkg = pkg.__name__
    if "cupy" == pkg:
        for i in range(count):
            x = cupy.random.rand(NSIZE, NSIZE, dtype=DTYPE)
            if posdef:
                x = x @ x.T + x.T @ x + eps
            arr_list.append(x)
        cupy.cuda.runtime.deviceSynchronize()
    elif "arrayfire" == pkg:
        for i in range(count):
            x = af.randu((NSIZE, NSIZE), dtype=getattr(af, DTYPE))
            if posdef:
                x = af.matmul(x, x.T) + af.matmul(x.T, x) + eps
            af.eval(x)
            arr_list.append(x)
        af.sync()
    elif "dpnp" == pkg:
        for i in range(count):
            x = dpnp.random.rand(NSIZE, NSIZE).astype(DTYPE)
            if posdef:
                x = x @ x.T + x.T @ x + eps
            arr_list.append(x)
    elif "numpy" == pkg:
        for i in range(count):
            x = np.random.rand(NSIZE, NSIZE).astype(DTYPE)
            if posdef:
                x = x @ x.T + x.T @ x + eps
            arr_list.append(x)
    elif "cupynumeric" == pkg:
        for i in range(count):
            x = cupynumeric.random.rand(NSIZE, NSIZE).astype(DTYPE)
            if posdef:
                x = x @ x.T + x.T @ x + eps
            arr_list.append(x)
    return arr_list


def svd_np(arr):
    return np.linalg.svd(arr)


def svd_dpnp(arr):
    return dpnp.linalg.svd(arr)


def svd_af(arr):
    x = af.svd(arr)
    for r in x:
        af.eval(r)
    af.sync()
    return x


def svd_cupy(arr):
    x = cupy.linalg.svd(arr)
    cupy.cuda.runtime.deviceSynchronize()
    return x


def svd_cupynumeric(arr):
    return cupynumeric.linalg.svd(arr)


def qr_np(arr):
    return np.linalg.qr(arr)


def qr_dpnp(arr):
    return dpnp.linalg.qr(arr)


def qr_af(arr):
    x = af.qr(arr)
    for r in x:
        af.eval(r)
    af.sync()
    return x


def qr_cupy(arr):
    x = cupy.linalg.qr(arr)
    cupy.cuda.runtime.deviceSynchronize()
    return x


def qr_cupynumeric(arr):
    return cupynumeric.linalg.qr(arr)


def cholesky_np(arr):
    return np.linalg.cholesky(arr)


def cholesky_dpnp(arr):
    return dpnp.linalg.cholesky(arr)


def cholesky_af(arr):
    x, info = af.cholesky(arr)
    af.eval(x)
    af.sync()
    return x


def cholesky_cupy(arr):
    x = cupy.linalg.cholesky(arr)
    cupy.cuda.runtime.deviceSynchronize()
    return x


def cholesky_cupynumeric(arr):
    return cupynumeric.linalg.cholesky(arr)


def inv_np(arr):
    return np.linalg.inv(arr)


def inv_dpnp(arr):
    return dpnp.linalg.inv(arr)


def inv_af(arr):
    x = af.inverse(arr)
    af.eval(x)
    af.sync()
    return x


def inv_cupy(arr):
    x = cupy.linalg.inv(arr)
    cupy.cuda.runtime.deviceSynchronize()
    return x


def inv_cupynumeric(arr):
    return cupynumeric.linalg.inv(arr)


def det_np(arr):
    return np.linalg.det(arr)


def det_dpnp(arr):
    return dpnp.linalg.det(arr)


def det_af(arr):
    x = af.det(arr)
    af.sync()
    return x


def det_cupy(arr):
    x = cupy.linalg.det(arr)
    cupy.cuda.runtime.deviceSynchronize()
    return x


def det_cupynumeric(arr):
    return cupynumeric.linalg.det(arr)


def norm_np(arr):
    return np.linalg.norm(arr)


def norm_dpnp(arr):
    return dpnp.linalg.norm(arr)


def norm_af(arr):
    x = af.norm(arr)
    af.sync()
    return x


def norm_cupy(arr):
    x = cupy.linalg.norm(arr)
    cupy.cuda.runtime.deviceSynchronize()
    return x


def norm_cupynumeric(arr):
    return cupynumeric.linalg.norm(arr)


@pytest.mark.parametrize("pkgid", IDS, ids=IDS)
class TestLinalg:
    def test_cholesky(self, benchmark, pkgid):
        initialize_package(pkgid)
        setup = lambda: (generate_arrays(pkgid, 1, True), {})

        benchmark.extra_info["description"] = f"{NSIZE}x{NSIZE} Matrix"
        pkg = PKGDICT[pkgid]

        CHOLESKY_FUNCS = {
            "numpy": cholesky_np,
            "cupy": cholesky_cupy,
            "arrayfire": cholesky_af,
            "dpnp": cholesky_dpnp,
            "cupynumeric": cholesky_cupynumeric,
        }
        result = benchmark.pedantic(
            target=CHOLESKY_FUNCS[pkg.__name__], setup=setup, rounds=ROUNDS, iterations=ITERATIONS
        )

    def test_svd(self, benchmark, pkgid):
        initialize_package(pkgid)
        setup = lambda: (generate_arrays(pkgid, 1), {})

        benchmark.extra_info["description"] = f"{NSIZE}x{NSIZE} Matrix"
        pkg = PKGDICT[pkgid]

        SVD_FUNCS = {
            "numpy": svd_np,
            "cupy": svd_cupy,
            "arrayfire": svd_af,
            "dpnp": svd_dpnp,
            "cupynumeric": svd_cupynumeric,
        }
        result = benchmark.pedantic(target=SVD_FUNCS[pkg.__name__], setup=setup, rounds=ROUNDS, iterations=ITERATIONS)

    def test_qr(self, benchmark, pkgid):
        initialize_package(pkgid)
        setup = lambda: (generate_arrays(pkgid, 1), {})

        benchmark.extra_info["description"] = f"{NSIZE}x{NSIZE} Matrix"
        pkg = PKGDICT[pkgid]

        QR_FUNCS = {
            "numpy": qr_np,
            "cupy": qr_cupy,
            "arrayfire": qr_af,
            "dpnp": qr_dpnp,
            "cupynumeric": qr_cupynumeric,
        }
        result = benchmark.pedantic(target=QR_FUNCS[pkg.__name__], setup=setup, rounds=ROUNDS, iterations=ITERATIONS)

    def test_inv(self, benchmark, pkgid):
        initialize_package(pkgid)
        setup = lambda: (generate_arrays(pkgid, 1), {})

        benchmark.extra_info["description"] = f"{NSIZE}x{NSIZE} Matrix"
        pkg = PKGDICT[pkgid]

        INV_FUNCS = {
            "numpy": inv_np,
            "cupy": inv_cupy,
            "arrayfire": inv_af,
            "dpnp": inv_dpnp,
            "cupynumeric": inv_cupynumeric,
        }
        result = benchmark.pedantic(target=INV_FUNCS[pkg.__name__], setup=setup, rounds=ROUNDS, iterations=ITERATIONS)

    def test_det(self, benchmark, pkgid):
        initialize_package(pkgid)
        setup = lambda: (generate_arrays(pkgid, 1), {})

        benchmark.extra_info["description"] = f"{NSIZE}x{NSIZE} Matrix"
        pkg = PKGDICT[pkgid]

        DET_FUNCS = {
            "numpy": det_np,
            "cupy": det_cupy,
            "arrayfire": det_af,
            "dpnp": det_dpnp,
            "cupynumeric": det_cupynumeric,
        }
        result = benchmark.pedantic(target=DET_FUNCS[pkg.__name__], setup=setup, rounds=ROUNDS, iterations=ITERATIONS)

    def test_norm(self, benchmark, pkgid):
        initialize_package(pkgid)
        setup = lambda: (generate_arrays(pkgid, 1), {})

        benchmark.extra_info["description"] = f"{NSIZE}x{NSIZE} Matrix"
        pkg = PKGDICT[pkgid]

        NORM_FUNCS = {
            "numpy": norm_np,
            "cupy": norm_cupy,
            "arrayfire": norm_af,
            "dpnp": norm_dpnp,
            "cupynumeric": norm_cupynumeric,
        }
        result = benchmark.pedantic(target=NORM_FUNCS[pkg.__name__], setup=setup, rounds=ROUNDS, iterations=ITERATIONS)
