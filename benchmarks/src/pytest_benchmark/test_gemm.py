import os

from common import *

ITERATIONS = 1

alpha = 0.4
beta = 0.6

dim_x = 16
dim_y = 16
blk_m = 64
blk_n = 64
blk_k = 4
dim_xa = 64
dim_ya = 4
dim_xb = 4
dim_yb = 64
assert dim_x * dim_y == dim_xa * dim_ya == dim_xb * dim_yb
config = {
    "DIM_X": dim_x,
    "DIM_Y": dim_y,
    "BLK_M": blk_m,
    "BLK_N": blk_n,
    "BLK_K": blk_k,
    "DIM_XA": dim_xa,
    "DIM_YA": dim_ya,
    "DIM_XB": dim_xb,
    "DIM_YB": dim_yb,
    "THR_M": blk_m // dim_x,
    "THR_N": blk_n // dim_y,
}


def create_cupy_kernel(params):
    sgemm_file = os.path.join(os.path.dirname(__file__), "sgemm.cu")
    code = None
    with open(sgemm_file, "r") as f:
        code = f.read()
        for k, v in params.items():
            code = "#define " + k + " " + str(v) + "\n" + code

    return cupy.RawKernel(code, "sgemm")


kern = create_cupy_kernel(config)


@pytest.mark.parametrize("pkgid", IDS, ids=IDS)
class TestGemm:
    def test_gemm(self, benchmark, pkgid):
        pkg = PKGDICT[pkgid]
        initialize_package(pkgid)

        setup = lambda: (generate_arrays(pkgid, 3), {})

        benchmark.extra_info["description"] = f"{NSIZE}x{NSIZE} Matrix"
        result = benchmark.pedantic(target=FUNCS[pkg.__name__], setup=setup, rounds=ROUNDS, iterations=ITERATIONS)


def generate_arrays(pkgid, count):
    arr_list = []
    pkg = PKGDICT[pkgid]
    pkg = pkg.__name__
    if "cupy" == pkg:
        cupy.random.seed(1)
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
        dpnp.random.seed(1)
        for i in range(count):
            arr_list.append(dpnp.random.rand(NSIZE, NSIZE).astype(DTYPE))
    elif "numpy" == pkg:
        np.random.rand(1)
        for i in range(count):
            arr_list.append(np.random.rand(NSIZE, NSIZE).astype(DTYPE))
    elif "cupynumeric" == pkg:
        for i in range(count):
            arr_list.append(cupynumeric.random.rand(NSIZE, NSIZE).astype(DTYPE))

    return arr_list


def gemm_np(A, B, C):
    return alpha * np.matmul(A, B) + beta * C


def gemm_af(A, B, C):
    x = af.gemm(A, B, alpha=alpha, beta=beta, accum=C)
    af.eval(x)
    af.sync()
    return x


def gemm_dpnp(A, B, C):
    return alpha * dpnp.matmul(A, B) + beta * C


def gemm_cupy(A, B, C):
    m, k = A.shape
    k, n = B.shape

    # Inputs matrices need to be in Fortran order.
    # A = cupy.asfortranarray(A)
    # B = cupy.asfortranarray(B)
    # C = cupy.asfortranarray(C)

    grid = (int(math.ceil(m / blk_m)), int(math.ceil(n / blk_n)), 1)
    block = (dim_x, dim_y, 1)
    args = (m, n, k, A, B, C)
    shared_mem = blk_k * (blk_m + 1) * 4 + blk_n * (blk_k + 1) * 4
    kern(grid, block, args=args, shared_mem=shared_mem)
    cupy.cuda.runtime.deviceSynchronize()
    return C


def gemm_cupynumeric(A, B, C):
    return alpha * cupynumeric.matmul(A, B) + beta * C


FUNCS = {"numpy": gemm_np, "cupy": gemm_cupy, "arrayfire": gemm_af, "dpnp": gemm_dpnp, "cupynumeric": gemm_cupynumeric}
