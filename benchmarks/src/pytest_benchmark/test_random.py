from common import *

ITERATIONS = 20


def randn_np():
    arr = np.random.normal(size=(NNSIZE))


def randn_dpnp():
    arr = dpnp.random.normal(size=(NNSIZE))


def randn_cupy():
    arr = cupy.random.normal(size=(NNSIZE))
    cupy.cuda.runtime.deviceSynchronize()


def randn_cupynumeric():
    arr = cupynumeric.random.normal(size=(NNSIZE))


def randn_af():
    arr = af.randn((NNSIZE))
    af.eval(arr)
    af.sync()


def randu_np():
    arr = np.random.uniform(size=(NNSIZE))


def randu_dpnp():
    arr = dpnp.random.uniform(size=(NNSIZE))


def randu_cupy():
    arr = cupy.random.uniform(size=(NNSIZE))
    cupy.cuda.runtime.deviceSynchronize()


def randu_cupynumeric():
    arr = cupynumeric.random.uniform(size=(NNSIZE))


def randu_af():
    arr = af.randu((NNSIZE))
    af.eval(arr)
    af.sync()


@pytest.mark.parametrize("pkgid", IDS, ids=IDS)
class TestRandom:
    def test_normal(self, benchmark, pkgid):
        initialize_package(pkgid)

        pkg = PKGDICT[pkgid]
        FUNCS = {
            "dpnp": randn_dpnp,
            "numpy": randn_np,
            "cupy": randn_cupy,
            "arrayfire": randn_af,
            "cupynumeric": randn_cupynumeric,
        }

        benchmark.extra_info["description"] = f"{NNSIZE:.2e} Samples"
        result = benchmark.pedantic(target=FUNCS[pkg.__name__], rounds=ROUNDS, iterations=ITERATIONS)

    def test_uniform(self, benchmark, pkgid):
        initialize_package(pkgid)

        pkg = PKGDICT[pkgid]
        FUNCS = {
            "dpnp": randu_dpnp,
            "numpy": randu_np,
            "cupy": randu_cupy,
            "arrayfire": randu_af,
            "cupynumeric": randu_cupynumeric,
        }

        result = benchmark.pedantic(target=FUNCS[pkg.__name__], rounds=ROUNDS, iterations=ITERATIONS)
