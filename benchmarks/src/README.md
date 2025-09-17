Benchmarks
===========

## Setting up environment

Create a python environment and install pytest and the compute libraries:
```sh
    python -m pip install -r requirements.txt
```

If running `dpnp` with Nvidia or AMD devices, you must install the oneapi toolkit along with the corresponding oneapi pluging:

```sh
    # install oneapi toolkit and plugins
    source /opt/intel/oneapi/setvars.sh
```

## Benchmark parameters

The benchmark packages, rounds, array sizes, and numeric type may be specified on the constants at the top of [pytest_benchmark/common.py](pytest_benchmark/common.py).

Alternatively, they may be specified individually at the top of each test file.


## Running

These are the steps to run the benchmarks, and produce the graphs 

Run the benchmarks and store the results in `results.json`
```sh
    pytest ./pytest_benchmark --benchmark-json=results.json
```

To create graphs and store the timing results after creating the `results.json`, run:
```sh
    mkdir img
    python graphs.py
```

To modify the tests being shown, modify the `TESTS` list at the top of the `graphs.py` file.
To modify the legend of the package labels shown, modify `PKG_LABELS`
To modify the name of the tests shown, modify `TESTS_GRAPH_NAME`
To modify the hardware display, modify `HARDWARE` 

## Notes
When running with `dpnp`, set the environment variable `DPNP_RAISE_EXCEPION_ON_NUMPY_FALLBACK` to 0.