# arrayfire-python (WIP)
<p align="center"><a href="http://arrayfire.com/"><img src="http://arrayfire.com/logos/arrayfire_logo_whitebkgnd.png" width="800"></a></p>

[ArrayFire](https://github.com/arrayfire/arrayfire) is a high performance library for parallel computing with an easy-to-use API. It enables users to write scientific computing code that is portable across CUDA, OpenCL and CPU devices.  

This project is a **work in progress**. It is meant to provide a numpy-like Python interface for the ArrayFire C library, i.e, it provides array functionality, math operations, printing, etc. This is the front-end python library for using ArrayFire. It is currently supported on Python 3.10+.

Here is an example of the library at work:
```py
# Set backend and device (optional: 'cuda', 'opencl', 'oneapi', 'cpu')
af.setBackend(af.BackendType.cuda)
af.setDevice(0)

# Create two 5x5 arrays on the GPU
a = af.randu((5, 5))
b = af.randu((5, 5))

# Perform element-wise addition and matrix multiplication
c = a + b
d = af.matmul(a, b)

# Print the result
print(c, "Element-wise Sum")
print(d, "Matrix Product")
```

# Installing

**Requirement Details**
This project is separated into 3 different parts:
```
arrayfire-py -> arrayfire-binary-python-wrapper -> ArrayFire C Libraries
```
This means that arrayfire with python each of these parts is needed:
- [`arrayfire-py`](https://github.com/arrayfire/arrayfire-python) is the intended User Interface that provides a numpy-like layer to execute math and array operations with ArrayFire. *** This is the preferred Interface ***
- [`arrayfire-binary-python-wrapper`](https://github.com/arrayfire/arrayfire-binary-python-wrapper) is the wrapper that provides Python direct access to the ArrayFire functions in the C library. This package must have access to ArrayFire binaries.
- [`ArrayFire C Libraries`](https://github.com/arrayfire/arrayfire) are the binaries obtained from compiling the [ArrayFire C/C++ Project](https://github.com/arrayfire/arrayfire). You obtain these easily through [installers in the ArrayFire download page](https://arrayfire.com/download/).

**Install the last stable version of python wrapper:**
```sh
pip install arrayfire_binary_python_wrapper-0.8.0+af3.10.0-py3-none-linux_x86_64.whl # install required binary wrapper with the 3.10 ArrayFire binaries included 
pip install arrayfire-py # install arrayfire python interface library
```

**Install a pre-built wheel:**
```
pip install arrayfire-py -f https://repo.arrayfire.com/python/wheels/arrayfire-python/0.1.0
```

# Building
Building this interface is straight forward using [scikit-build-core](https://github.com/scikit-build/scikit-build-core):
```
python -m pip install -r dev-requirements.txt
python -m build --wheel
```

**Note: Building this project does not require the arrayfire-binary-python-wrapper package; however, the binary wrapper is needed to run any projects with it**

# Running Tests

Tests are located in folder [tests](tests).

To run the tests, use:
```bash
python -m pytest tests/
```

# Contributing

If you are interested in using ArrayFire through python, we would appreciate any feedback and contributions.

The community of ArrayFire developers invites you to build with us if you are
interested and able to write top-performing tensor functions. Together we can
fulfill [The ArrayFire
Mission](https://github.com/arrayfire/arrayfire/wiki/The-ArrayFire-Mission-Statement)
for fast scientific computing for all.

Contributions of any kind are welcome! Please refer to [the
wiki](https://github.com/arrayfire/arrayfire/wiki) and our [Code of
Conduct](33) to learn more about how you can get involved with the ArrayFire
Community through
[Sponsorship](https://github.com/arrayfire/arrayfire/wiki/Sponsorship),
[Developer
Commits](https://github.com/arrayfire/arrayfire/wiki/Contributing-Code-to-ArrayFire),
or [Governance](https://github.com/arrayfire/arrayfire/wiki/Governance).

# Citations and Acknowledgements

If you redistribute ArrayFire, please follow the terms established in [the
license](LICENSE).

ArrayFire development is funded by AccelerEyes LLC and several third parties,
please see the list of [acknowledgements](ACKNOWLEDGEMENTS.md) for an
expression of our gratitude.

# Support and Contact Info

* [Slack Chat](https://join.slack.com/t/arrayfire-org/shared_invite/MjI4MjIzMDMzMTczLTE1MDI5ODg4NzYtN2QwNGE3ODA5OQ)
* [Google Groups](https://groups.google.com/forum/#!forum/arrayfire-users)
* ArrayFire Services:  [Consulting](http://arrayfire.com/consulting)  |  [Support](http://arrayfire.com/download)   |  [Training](http://arrayfire.com/training)

# Trademark Policy

The literal mark "ArrayFire" and ArrayFire logos are trademarks of AccelerEyes
LLC (dba ArrayFire). If you wish to use either of these marks in your own
project, please consult [ArrayFire's Trademark
Policy](http://arrayfire.com/trademark-policy/)
