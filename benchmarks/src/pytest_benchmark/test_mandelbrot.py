# SPDX-FileCopyrightText: 2017 Nicolas P. Rougier
# SPDX-FileCopyrightText: 2021 ETH Zurich and the NPBench authors
# SPDX-FileCopyrightText: 2022 - 2023 Intel Corporation
#
# SPDX-License-Identifier: BSD-3-Clause

# more information at https://github.com/rougier/numpy-book

from common import *

xmin = -2
xmax = 2
ymin = -2
ymax = 2
xn = int(NSIZE / 2)
yn = int(NSIZE / 2)
itermax = 20
horizon = 2.0


@pytest.mark.parametrize("pkgid", IDS, ids=IDS)
class TestMandelbrot:
    def test_mandelbrot(self, benchmark, pkgid):
        initialize_package(pkgid)
        pkg = PKGDICT[pkgid]

        benchmark.extra_info["description"] = f"{xn}x{yn} grid iterated {itermax}x"
        result = benchmark.pedantic(target=FUNCS[pkg.__name__], rounds=ROUNDS, iterations=1)


def mandelbrot_np():
    # Adapted from
    # https://thesamovar.wordpress.com/2009/03/22/fast-fractals-with-python-and-numpy/
    Xi, Yi = np.mgrid[0:xn, 0:yn]
    X = np.linspace(xmin, xmax, xn, dtype=np.float64)[Xi]
    Y = np.linspace(ymin, ymax, yn, dtype=np.float64)[Yi]
    C = X + Y * 1j

    N_ = np.zeros(C.shape, dtype=np.int64)
    Z_ = np.zeros(C.shape, dtype=np.complex128)
    Xi.shape = Yi.shape = C.shape = xn * yn

    Z = np.zeros(C.shape, np.complex128)
    for i in range(itermax):
        if not len(Z):
            break

        # Compute for relevant points only
        np.multiply(Z, Z, Z)
        np.add(Z, C, Z)

        # Failed convergence
        I = abs(Z) > horizon  # noqa: E741 math variable
        N_[Xi[I], Yi[I]] = i + 1
        Z_[Xi[I], Yi[I]] = Z[I]

        # Keep going with those who have not diverged yet
        np.logical_not(I, I)  # np.negative(I, I) not working any longer
        Z = Z[I]
        Xi, Yi = Xi[I], Yi[I]
        C = C[I]
    return Z_.T, N_.T


def mandelbrot_dpnp():
    # Adapted from
    # https://thesamovar.wordpress.com/2009/03/22/fast-fractals-with-python-and-numpy/
    Xi, Yi = dpnp.mgrid[0:xn, 0:yn]
    X = dpnp.linspace(xmin, xmax, xn, dtype=dpnp.float64)[Xi]
    Y = dpnp.linspace(ymin, ymax, yn, dtype=dpnp.float64)[Yi]
    C = X + Y * 1j
    N_ = dpnp.zeros(C.shape, dtype=dpnp.int64)
    Z_ = dpnp.zeros(C.shape, dtype=dpnp.complex128)
    Xi.reshape(xn * yn)
    Yi.reshape(xn * yn)
    C.reshape(xn * yn)

    Z = dpnp.zeros(C.shape, dtype=dpnp.complex128)
    for i in range(itermax):
        if not len(Z):
            break

        # Compute for relevant points only
        dpnp.multiply(Z, Z, Z)
        dpnp.add(Z, C, Z)

        # Failed convergence
        I = abs(Z) > horizon  # noqa: E741 math variable
        N_[Xi[I], Yi[I]] = i + 1
        Z_[Xi[I], Yi[I]] = Z[I]

        # Keep going with those who have not diverged yet
        dpnp.logical_not(I, I)  # dpnp.negative(I, I) not working any longer
        Z = Z[I]
        Xi, Yi = Xi[I], Yi[I]
        C = C[I]

    Z_ = Z_.T
    N_ = N_.T

    return Z_, N_


def mandelbrot_cupy():
    # Adapted from
    # https://thesamovar.wordpress.com/2009/03/22/fast-fractals-with-python-and-numpy/
    Xi, Yi = cupy.mgrid[0:xn, 0:yn]
    X = cupy.linspace(xmin, xmax, xn, dtype=cupy.float64)[Xi]
    Y = cupy.linspace(ymin, ymax, yn, dtype=cupy.float64)[Yi]
    C = X + Y * 1j
    N_ = cupy.zeros(C.shape, dtype=cupy.int64)
    Z_ = cupy.zeros(C.shape, dtype=cupy.complex128)
    Xi.shape = Yi.shape = C.shape = xn * yn

    Z = cupy.zeros(C.shape, cupy.complex128)
    for i in range(itermax):
        if not len(Z):
            break

        # Compute for relevant points only
        cupy.multiply(Z, Z, Z)
        cupy.add(Z, C, Z)

        # Failed convergence
        I = abs(Z) > horizon  # noqa: E741 math variable
        N_[Xi[I], Yi[I]] = i + 1
        Z_[Xi[I], Yi[I]] = Z[I]

        # Keep going with those who have not diverged yet
        cupy.logical_not(I, I)  # cupy.negative(I, I) not working any longer
        Z = Z[I]
        Xi, Yi = Xi[I], Yi[I]
        C = C[I]

        if i % 2 == 1:
            mempool = cupy.get_default_memory_pool()
            mempool.free_all_blocks()

    Z_ = Z_.T
    N_ = N_.T

    cupy.cuda.runtime.deviceSynchronize()
    return Z_, N_


def mandelbrot_cupynumeric():
    # Adapted from
    # https://thesamovar.wordpress.com/2009/03/22/fast-fractals-with-python-and-numpy/
    Xi, Yi = np.mgrid[0:xn, 0:yn]
    X = cupynumeric.linspace(xmin, xmax, xn, dtype=cupynumeric.float64)[Xi]
    Y = cupynumeric.linspace(ymin, ymax, yn, dtype=cupynumeric.float64)[Yi]
    C = X + Y * 1j

    N_ = cupynumeric.zeros(C.shape, dtype=cupynumeric.int64)
    Z_ = cupynumeric.zeros(C.shape, dtype=cupynumeric.complex128)
    Xi.shape = Yi.shape = C.shape = xn * yn

    Z = cupynumeric.zeros(C.shape, cupynumeric.complex128)
    for i in range(itermax):
        if not len(Z):
            break

        # Compute for relevant points only
        cupynumeric.multiply(Z, Z, Z)
        cupynumeric.add(Z, C, Z)

        # Failed convergence
        I = abs(Z) > horizon  # noqa: E741 math variable
        N_[Xi[I], Yi[I]] = i + 1
        Z_[Xi[I], Yi[I]] = Z[I]

        # Keep going with those who have not diverged yet
        cupynumeric.logical_not(I, I)  # np.negative(I, I) not working any longer
        Z = Z[I]
        Xi, Yi = Xi[I], Yi[I]
        C = C[I]

    return Z_.T, N_.T


def mandelbrot_af():
    Xi = af.flat(af.range((xn, yn), axis=0, dtype=af.int64))
    Yi = af.flat(af.range((xn, yn), axis=1, dtype=af.int64))
    X = af.iota((xn, 1), tile_shape=(1, yn), dtype=af.float64) * (xmax - xmin) / (xn - 1) + xmin
    Y = af.iota((1, yn), tile_shape=(xn, 1), dtype=af.float64) * (ymax - ymin) / (yn - 1) + ymin

    C = af.cplx(X, Y)
    N_ = af.constant(0, (xn, yn))
    Z_ = af.constant(0, (xn, yn), dtype=af.complex64)
    Z = af.constant(0, (xn, yn), dtype=af.complex64)
    for i in range(itermax):
        if not len(Z):
            break

        # Compute for relevant points only
        Z = Z * Z
        Z = Z + C

        # Failed convergence
        I = af.abs(Z) > horizon  # noqa: E741 math variable

        if not af.any_true(I):
            break

        N_[Xi[I] * yn + Yi[I]] = i + 1
        Z_[Xi[I] * yn + Yi[I]] = Z[I]

        # Keep going with those who have not diverged yet
        I = af.logical_not(I)
        Z = Z[I]
        Xi = Xi[I]
        Yi = Yi[I]
        C = C[I]

        if i % 2 == 1:
            af.device_gc()

    Z_ = Z_.T
    N_ = N_.T
    af.eval(Z_)
    af.eval(N_)
    af.sync()
    return Z_, N_


FUNCS = {
    "dpnp": mandelbrot_dpnp,
    "numpy": mandelbrot_np,
    "cupy": mandelbrot_cupy,
    "arrayfire": mandelbrot_af,
    "cupynumeric": mandelbrot_cupynumeric,
}
