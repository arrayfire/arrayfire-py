from common import *

ITERATIONS = 1


@pytest.mark.parametrize("pkgid", IDS, ids=IDS)
class TestPi:
    def test_pi(self, benchmark, pkgid):
        initialize_package(pkgid)
        pkg = PKGDICT[pkgid]

        benchmark.extra_info["description"] = f"{NNSIZE:.2e} Samples"
        result = benchmark.pedantic(target=FUNCS[pkg.__name__], rounds=ROUNDS, iterations=ITERATIONS, args=[NNSIZE])


# Having the function outside is faster than the lambda inside
def in_circle(x, y):
    return (x * x + y * y) < 1


def calc_pi_af(samples):
    x = af.randu(samples)
    y = af.randu(samples)
    result = 4 * af.sum(in_circle(x, y)) / samples

    af.sync()

    return result


def calc_pi_numpy(samples):
    x = np.random.rand(samples).astype(np.float32)
    y = np.random.rand(samples).astype(np.float32)
    return 4.0 * np.sum(in_circle(x, y)) / samples


def calc_pi_cupy(samples):
    x = cupy.random.rand(samples, dtype=np.float32)
    y = cupy.random.rand(samples, dtype=np.float32)
    res = 4.0 * cupy.sum(in_circle(x, y)) / samples
    cupy.cuda.runtime.deviceSynchronize()
    return res


def calc_pi_dpnp(samples):
    x = dpnp.random.rand(samples).astype(dpnp.float32)
    y = dpnp.random.rand(samples).astype(dpnp.float32)
    return 4.0 * dpnp.sum(in_circle(x, y)) / samples


def calc_pi_cupynumeric(samples):
    x = cupynumeric.random.rand(samples).astype(cupynumeric.float32)
    y = cupynumeric.random.rand(samples).astype(cupynumeric.float32)
    return 4.0 * cupynumeric.sum(in_circle(x, y)) / samples


FUNCS = {
    "dpnp": calc_pi_dpnp,
    "numpy": calc_pi_numpy,
    "cupy": calc_pi_cupy,
    "arrayfire": calc_pi_af,
    "cupynumeric": calc_pi_cupynumeric,
}
