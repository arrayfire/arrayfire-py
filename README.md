# arrayfire-py
<p align="center"><a href="http://arrayfire.com/"><img src="http://arrayfire.com/logos/arrayfire_logo_whitebkgnd.png" width="800"></a></p>

[ArrayFire](https://github.com/arrayfire/arrayfire) is a high performance library for parallel computing with an easy-to-use API. It enables users to write scientific computing code that is portable across CUDA, OpenCL, oneAPI and CPU devices.  

This project is meant is meant to provide an easy to use Python interface for the ArrayFire C library, i.e, it provides array functionality, math operations, printing, etc. This is the front-end python library for using ArrayFire. It is currently supported on Python 3.10+.

Here is an example of the library at work:
```py
import arrayfire as af

# Set any backend and device (optional: 'cuda', 'opencl', 'oneapi', 'cpu')
af.set_backend(af.BackendType.cuda)
af.set_device(0)

# Monte Carlo estimation of pi
def calc_pi_device(samples):
    # Simple, array based API
    # Generate uniformly distributed random numers
    x = af.randu(samples)
    y = af.randu(samples)
    # Supports Just In Time Compilation
    # The following line generates a single kernel
    within_unit_circle = (x * x + y * y) < 1
    # Intuitive function names
    return 4 * af.count(within_unit_circle) / samples
```
Find out more in our [examples](https://github.com/arrayfire/arrayfire-py/tree/master/examples) directory or just read the [documentation](https://arrayfire.org/arrayfire-py/overview.html). 

# Prequisites and Installing

This project provides the python interface to ArrayFire, however it requires access to the ArrayFire binaries as a prequisite. The dependency chain can be separated into 3 different parts as follows:
```
arrayfire-py -> arrayfire-binary-python-wrapper -> ArrayFire C Libraries
```
To run arrayfire with python each of these parts is needed:
- [`arrayfire-py`](https://github.com/arrayfire/arrayfire-python) is the ***intended User Interface*** that provides a numpy-like layer to execute math and array operations with ArrayFire.
- [`arrayfire-binary-python-wrapper`](https://github.com/arrayfire/arrayfire-binary-python-wrapper) is a thin wrapper that provides Python direct access to the ArrayFire functions in the C library. This package must have access to ArrayFire binaries, either through a system-wide install, or through a pre-bundled wheel that includes binaries. 
- [`ArrayFire C Libraries`](https://github.com/arrayfire/arrayfire) are the binaries obtained from compiling the [ArrayFire C/C++ Project](https://github.com/arrayfire/arrayfire) or more simply by downloading [installers in the ArrayFire download page](https://arrayfire.com/download/). Binaries can also be obtained as part of a pre-packaged arrayfire-binary-python-wrapper wheel.

**Install the python wrapper with existing ArrayFire install:**
```sh
# install required binary wrapper, assumes ArrayFire binaries will be installed on the system
pip install arrayfire-binary-python-wrapper
pip install arrayfire-py # install arrayfire python interface library
```

**Install wrapper with a pre-built wheel:**
```sh
# will grab a binary wrapper with included pre-built binaries
pip install arrayfire-binary-python-wrapper -f https://repo.arrayfire.com/python/wheels/3.10.0/ 
pip install arrayfire-py
```
# Running Tests

Tests are located in folder [tests](tests).

To run the tests, use:
```bash
python -m pytest tests/
```

# Building
```
python -m pip install -r dev-requirements.txt
python -m build --wheel
```
**Note: Building this project does not require the arrayfire-binary-python-wrapper package; however, the binary wrapper is needed to run any projects with it**

## Experimental Array API support
This wrapper is exploring an experimental implementation of the [DataAPIs](https://data-apis.org) [array API](https://data-apis.org/array-api/latest) standard [in this directory](https://github.com/arrayfire/arrayfire-py/tree/master/arrayfire/array_api) with the goal of allowing ArrayFire to seamlessly interoperate with the broader Python landscape. Some portions of the standard are still unimplemented however some simpler examples are working. 

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
