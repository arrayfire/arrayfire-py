Documentation (WIP)
==========

**This documentation is a work in progress and may not contain all currently supported operations. Please check the functions signature and description for more info on it**

We use [`Sphinx`](https://www.sphinx-doc.org/en/master/index.html) for presenting our documentation.

To build the docs follow these steps:

1. Install the required sphinx packages and extensions from the [dev-requirements.txt](../dev-requirements.txt)
```sh
pip install -r dev-requirements.txt # install sphinx and its extensions
pip install -r requirements.txt # install arrayfire-binary-python-wrapper
```
2. Build docs using sphinx
```sh
sphinx-build -M html docs/ output-docs/ # builds docs as html files stored in output-docs
```
3. Explore the docs starting at `output-docs/index.html`

