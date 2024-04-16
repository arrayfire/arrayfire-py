SRC = arrayfire

ifeq ($(shell uname),Darwin)
ifeq ($(shell which gsed),)
$(error Please install GNU sed with 'brew install gnu-sed')
else
SED = gsed
endif
else
SED = sed
endif

.PHONY : version
version : 
	@python -c 'from arrayfire.version import VERSION; print(f"ArrayFire Python v{VERSION}")'

.PHONY : build
build :
	@python -m build

# Dev

.PHONY : pre-commit
pre-commit :
	black --check . && isort --check . && flake8 . && mypy . --cache-dir=/dev/null

# Testing

.PHONY : tests
tests :
	pytest --color=yes -v -rf --durations=40 --cov-config=.coveragerc --cov=$(SRC) --cov-report=xml

# Cleaning

.PHONY : clean
clean :
	rm -rf .pytest_cache/
	rm -rf arrayfire.egg-info/
	rm -rf dist/
	rm -rf build/
	find . | grep -E '(\.mypy_cache|__pycache__|\.pyc|\.pyo$$)' | xargs rm -rf
