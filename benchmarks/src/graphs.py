import json

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

BENCHMARKS_JSON = "results.json"

# Hardware details shown in title
HARDWARE = "Intel Xeon Gold 5315Y (8 Processors) @ 3.201GHz 63032 MB\noneAPI 2025.2.1 NVIDIA RTX A4000, 16222 MB, CUDA 12.8 Compute 8.6"

# Show speedup in graph
SHOW_NUMBERS = True

# Round to digits after decimal
ROUND_NUMBERS = 1

# package list in graph order; arrayfire packages are added later
PKG_NAMES = ["numpy", "dpnp", "cupy", "cupynumeric"]

# color used in graphs
PKG_COLOR = {
    "numpy": "tab:blue",
    "cupy": "tab:green",
    "cupynumeric": "green",
    "dpnp": "tab:red",
    "afcpu": "tab:orange",
    "afopencl": "tab:orange",
    "afcuda": "tab:orange",
    "afoneapi": "tab:orange",
}

# labels displayed in the graph
PKG_LABELS = {
    "numpy": "numpy[cpu]",
    "dpnp": "dpnp[cuda:gpu]",
    "cupy": "cupy",
    "cupynumeric": "cupynumeric",
    "afcpu": "afcpu",
    "afcuda": "afcuda",
    "afopencl": "afopencl[opencl:gpu]",
    "afoneapi": "afoneapi[opencl:gpu]",
}

AFBACKENDS = ["afcpu", "afcuda", "afopencl", "afoneapi"]

# Tests to be shown in graphs
TESTS = [
    "group_elementwise",
    "neural_network",
    "black_scholes",
    "mandelbrot",
    "nbody",
    "pi",
    "normal",
    "gemm",
    "fft",
    "qr",
    # Other tests
    # 'svd
    # 'cholesky',
    # 'det',
    # 'norm',
    # 'uniform',
    # 'inv'
]

# Reverse list so it appears in order on graph
TESTS.reverse()

TESTS_GRAPH_NAME = {
    "group_elementwise": "Group_elementwise (JIT)",
    "neural_network": "Neural Network (JIT)",
    "black_scholes": "Black Scholes (JIT)",
    "mandelbrot": "Mandelbrot (JIT)",
    "nbody": "Nbody (JIT)",
    "pi": "Montecarlo Pi (JIT)",
    "normal": "Normal Distribution",
    "gemm": "General Matrix Multiplication",
    "fft": "2D FFT",
    "qr": "QR Decomposition",
}

for name in TESTS:
    if name not in TESTS_GRAPH_NAME:
        TESTS_GRAPH_NAME[name] = name


def get_benchmark_data():
    results = {}
    descriptions = {}
    with open(BENCHMARKS_JSON) as f:
        js = json.load(f)
        for bench in js["benchmarks"]:
            test_name = bench["name"]
            test_name = test_name[test_name.find("_") + 1 : test_name.find("[")]

            key = bench["param"]
            val = bench["stats"]["ops"]

            if len(bench["extra_info"]) != 0 and (not test_name in descriptions):
                descriptions[test_name] = bench["extra_info"]["description"]

            if test_name not in results:
                results[test_name] = {key: val}
            else:
                results[test_name][key] = val

    return results, descriptions


def create_graph(test_name, test_results):
    names = []
    values = []
    for name in test_results:
        names.append(name)
        values.append(test_results[name])

    bar = plt.bar(names, values)
    plt.title(test_name)

    plt.savefig("img/" + test_name + ".png")
    plt.close()


def generate_individual_graphs():
    results, descriptions = get_benchmark_data()

    for test in results:
        create_graph(test, results[test])


# Stores the timing results in a csv file
def store_csv():
    data_dict = {}
    data_dict["Test(seconds)"] = []
    results = {}
    for pkg in PKG_LABELS.keys():
        data_dict[pkg] = []
        results[pkg] = {}

    with open(BENCHMARKS_JSON) as f:
        js = json.load(f)
        for bench in js["benchmarks"]:
            test_name = bench["name"]
            test_name = test_name[test_name.find("_") + 1 : test_name.find("[")]

            pkg = bench["param"]
            time = bench["stats"]["mean"]

            if not test_name in data_dict["Test(seconds)"]:
                data_dict["Test(seconds)"].append(test_name)

            results[pkg][test_name] = time

    for test in data_dict["Test(seconds)"]:
        for pkg in PKG_LABELS.keys():
            if test in results[pkg]:
                data_dict[pkg].append(results[pkg][test])
            else:
                data_dict[pkg].append(np.nan)

    df = pd.DataFrame(data_dict)
    df.to_csv("summary.csv")


def generate_group_graph(test_list=None, show_numbers=False, filename="comparison"):
    results, descriptions = get_benchmark_data()

    width = 1 / (1 + len(PKG_NAMES))
    multiplier = 0

    tests = None
    if test_list:
        tests = test_list
    else:
        tests = results.keys()

    tests_values = {}
    x = np.arange(len(tests))

    for name in PKG_NAMES:
        tests_values[name] = []

    max_val = 1
    for test in tests:
        for name in PKG_NAMES:
            base_value = results[test]["numpy"]
            if name in results[test]:
                val = results[test][name] / base_value

                if ROUND_NUMBERS:
                    val = round(val, ROUND_NUMBERS)

                if max_val < val:
                    max_val = val

                tests_values[name].append(val)
            else:
                tests_values[name].append(np.nan)

    fig, ax = plt.subplots(layout="constrained")

    for name in PKG_NAMES:
        offset = width * multiplier
        rects = ax.barh(x + offset, tests_values[name], width, label=PKG_LABELS[name], color=PKG_COLOR[name])

        if show_numbers:
            ax.bar_label(rects, padding=3, rotation=0)
        multiplier += 1

    xlabels = []
    for test in tests:
        xlabels.append(TESTS_GRAPH_NAME[test] + "\n" + descriptions[test])

    ax.set_xlabel("Speedup")
    ax.set_xscale("log")
    ax.set_title(f"Runtime Comparison\n{HARDWARE}")
    ax.set_yticks(x + width, xlabels, rotation=0)
    xmin, xmax = ax.get_xlim()
    ax.set_xlim(xmin, xmax * 2)

    ax.legend(loc="lower right", ncols=len(PKG_NAMES))
    fig.set_figheight(8)
    fig.set_figwidth(13)
    fig.savefig(f"img/{filename}.png")
    plt.show()


def main():
    store_csv()
    for backend in AFBACKENDS:
        try:
            filename = f"comparison_{backend}"
            if not backend in PKG_NAMES:
                PKG_NAMES.insert(1, backend)
            generate_group_graph(TESTS, SHOW_NUMBERS, filename)
            PKG_NAMES.remove(backend)
        except Exception as e:
            print(e)
            print("No data for", backend)


if __name__ == "__main__":
    main()
