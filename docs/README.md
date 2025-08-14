Documentation
==========

We use [`Sphinx`](https://www.sphinx-doc.org/en/master/index.html) for presenting our documentation.

To build the docs follow these steps:

1. Install the required sphinx packages and extensions from the [requirements.txt](../requirements.txt)
```sh
pip install -r requirements.txt # install sphinx and its extensions
```
2. Build docs using sphinx
```sh
sphinx-build -M html docs/ output-docs/ # builds docs as html files stored in output-docs
```
3. Explore the docs starting at `output-docs/index.html`

