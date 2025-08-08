from common import *

ITERATIONS = 1
G = 1
dt = 1e-3
softening = 1e-4
M = 1

@pytest.mark.parametrize(
    "pkgid", IDS, ids=IDS
)
class TestNbody:
    def test_nbody(self, benchmark, pkgid):
        pkg = PKGDICT[pkgid]
        setup = lambda: (generate_arrays(pkgid), {})

        benchmark.extra_info["description"] = f"{NSIZE:.2e} Bodies"
        result = benchmark.pedantic(
            target=nbody,
            setup=setup,
            rounds=ROUNDS,
            iterations=ITERATIONS
        )

def acceleration(pkg, mass, pos):
    x = pos[:, 0:1]
    y = pos[:, 1:2]
    z = pos[:, 2:3]

    # matrix that stores all pairwise particle separations: r_j - r_i
    dx = x.T - x
    dy = y.T - y
    dz = z.T - z

    # matrix that stores 1/r^3 for all particle pairwise particle separations
    inv_r3 = dx**2 + dy**2 + dz**2 + softening**2
    inv_r3[inv_r3 > 0] = inv_r3[inv_r3 > 0] ** (-1.5)

    ax = G * (dx * inv_r3) @ mass
    ay = G * (dy * inv_r3) @ mass
    az = G * (dz * inv_r3) @ mass

    return pkg.hstack((ax, ay, az))

def acceleration_af(mass, pos):
    x = pos[:, 0:1]
    y = pos[:, 1:2]
    z = pos[:, 2:3]

    # matrix that stores all pairwise particle separations: r_j - r_i
    dx = af.moddims(x, (1, x.shape[0])) - x
    dy = af.moddims(y, (1, x.shape[0])) - y
    dz = af.moddims(z, (1, x.shape[0])) - z

    # matrix that stores 1/r^3 for all particle pairwise particle separations
    # inv_r3 = dx**2 + dy**2 + dz**2 + softening**2
    inv_r3 = dx*dx + dy*dy + dz*dz + softening*softening
    inv_r3 = af.pow(inv_r3, -1.5)

    ax = G * af.matmul((dx * inv_r3), mass)
    ay = G * af.matmul((dy * inv_r3), mass)
    az = G * af.matmul((dz * inv_r3), mass)

    return af.join(1, ax, ay, az)

def nbody(pkg, mass, pos, vel):
    vel -= pkg.mean(mass * vel, axis=0) / pkg.mean(mass)

    acc = None
    if pkg.__name__ == 'arrayfire':
        acc = acceleration_af(mass, pos)
    else:
        acc = acceleration(pkg, mass, pos)

    for i in range(ITERATIONS):
        vel += acc * dt / 2.0
        pos += vel * dt
        vel += acc * dt / 2.0

    energy = 0.5 * pkg.sum(mass * vel ** 2)

    return float(energy)

def generate_arrays(pkgid):
    arr_list = []
    pkg = PKGDICT[pkgid]
    
    initialize_package(pkgid)
    pkgname = pkg.__name__
    count = 2
    if "cupy" == pkgname:
        arr_list.append(M * cupy.ones((NSIZE, 1), dtype=DTYPE))
        for i in range(count):
            arr_list.append(cupy.random.rand(NSIZE, 3, dtype=DTYPE))
        cupy.cuda.runtime.deviceSynchronize()
    elif "arrayfire" == pkgname:
        af.device_gc()
        arr_list.append(M * af.constant(1, (NSIZE,1), dtype=getattr(af, DTYPE)))
        for i in range(count):  
            arr_list.append(af.randu((NSIZE, 3), dtype=getattr(af, DTYPE)))
        for arr in arr_list:
            af.eval(arr)
        af.sync()
    elif "dpnp" == pkgname:
        arr_list.append(M * dpnp.ones((NSIZE, 1), dtype=DTYPE))
        for i in range(count):
            arr_list.append(dpnp.random.rand(NSIZE, 3).astype(DTYPE))
    elif "numpy" == pkgname:
        arr_list.append(M * np.ones((NSIZE, 1), dtype=DTYPE))
        for i in range(count):
            arr_list.append(np.random.rand(NSIZE, 3).astype(DTYPE))

    return (pkg, arr_list[0], arr_list[1], arr_list[2])