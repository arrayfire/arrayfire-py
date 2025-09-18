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

import gc
import math

import cupy
import cupynumeric
import dpctl
import dpnp
import numpy as np
import pytest

import arrayfire as af

# modify parameters for most benchmarks
ROUNDS = 30
NSIZE = 2**11
NNSIZE = NSIZE**2
DTYPE = "float32"

# comment a line to remove that package from testing
PKGDICT = {
    "numpy": np,
    "cupy": cupy,
    # "afcpu": af,
    "afopencl": af,
    "afoneapi": af,
    "dpnp": dpnp,
    "cupynumeric": cupynumeric,
}

PKGS = []
IDS = []

for key, value in PKGDICT.items():
    IDS.append(key)
    PKGS.append(value)


# Initialize packages and cleanup memory before each round
def initialize_package(PKG_ID):
    pkg = PKGDICT[PKG_ID]

    try:
        # Free all unused memory
        gc.collect()
        af.device_gc()
        mempool = cupy.get_default_memory_pool()
        mempool.free_all_blocks()
    except Exception as e:
        print(e)

    if PKG_ID == "afcpu":
        af.set_backend(af.BackendType.cpu)
        af.device_gc()
        af.info()
    elif PKG_ID == "afopencl":
        af.set_backend(af.BackendType.opencl)
        af.device_gc()
        af.info()
    elif PKG_ID == "afcuda":
        af.set_backend(af.BackendType.cuda)
        af.device_gc()
        af.info()
    elif PKG_ID == "afoneapi":
        af.set_backend(af.BackendType.oneapi)
        af.device_gc()
        af.info()
    elif PKG_ID == "numpy":
        np.random.seed(0)
    elif PKG_ID == "dpnp":
        dpnp.random.seed(0)
        print(dpctl.get_devices()[0])
    elif PKG_ID == "cupy":
        cupy.random.seed(0)
        print(cupy.cuda.Device())
        mempool = cupy.get_default_memory_pool()
        mempool.free_all_blocks()
    elif PKG_ID == "cupynumeric":
        pass
    else:
        raise NotImplementedError()
