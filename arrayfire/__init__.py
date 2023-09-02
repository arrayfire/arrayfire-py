# flake8: noqa
from .version import ARRAYFIRE_VERSION, VERSION

__all__ = ["__version__"]
__version__ = VERSION

__all__ += ["__arrayfire_version__"]
__arrayfire_version__ = ARRAYFIRE_VERSION

__all__ += ["Array"]
from .array_object import Array

__all__ += [
    "int8",
    "int16",
    "int32",
    "int64",
    "uint8",
    "uint16",
    "uint32",
    "uint64",
    "float16",
    "float32",
    "float64",
    "complex64",
    "complex128",
    "bool",
]

from .dtypes import (
    bool,
    complex64,
    complex128,
    float16,
    float32,
    float64,
    int8,
    int16,
    int32,
    int64,
    uint8,
    uint16,
    uint32,
    uint64,
)

__all__ += [
    "get_backend",
    "get_active_backend",  # DeprecationWarning
    "get_array_backend_name",
    "get_array_device_id",
    "get_available_backends",  # DeprecationWarning
    "get_backend_count",
    "get_backend_id",  # DeprecationWarning
    "get_device_id",  # DeprecationWarning
    "get_dtype_size",
    "get_size_of",  # DeprecationWarning
    "set_backend",
]

from .backend._backend import get_backend
from .backend._backend_functions import (
    get_active_backend,
    get_array_backend_name,
    get_array_device_id,
    get_available_backends,
    get_backend_count,
    get_backend_id,
    get_device_id,
    get_dtype_size,
    get_size_of,
    set_backend,
)

__all__ += [
    "add",
    "sub",
    "mul",
    "div",
    "mod",
    "pow",
    "bitnot",
    "bitand",
    "bitor",
    "bitxor",
    "bitshiftl",
    "bitshiftr",
    "lt",
    "le",
    "gt",
    "ge",
    "eq",
    "neq",
    "sin",
    "cos",
    "tan",
    "asin",
    "acos",
    "atan",
    "atan2",
    "sinh",
    "cosh",
    "tanh",
    "asinh",
    "acosh",
    "atanh",
    "exp",
    "expm1",
    "log",
    "log1p",
    "log2",
    "log10",
    "sqrt",
    "cbrt",
    "hypot",
    "erf",
    "erfc",
    "tgamma",
    "lgamma",
    "pow2",
    "sign",
    "abs",
    "ceil",
    "floor",
    "round",
    "trunc",
    "isinf",
    "isnan",
    "iszero",
    "isinf",
    "isnan",
    "iszero",
    "isinf",
    "isnan",
    "clamp",
    "arg",
    "conjg",
    "cplx",
    "imag",
    "factorial",
    "maxof",
    "minof",
    "real",
    "rem",
    "root",
    "rsqrt",
    "sigmoid",
    "land",
    "lor",
    "lnot",
]


from .library.operators import (
    abs,
    acos,
    acosh,
    add,
    arg,
    asin,
    asinh,
    atan,
    atan2,
    atanh,
    bitand,
    bitnot,
    bitor,
    bitshiftl,
    bitshiftr,
    bitxor,
    cbrt,
    ceil,
    conjg,
    cos,
    cosh,
    cplx,
    div,
    eq,
    erf,
    erfc,
    exp,
    expm1,
    factorial,
    floor,
    ge,
    gt,
    hypot,
    imag,
    isinf,
    isnan,
    iszero,
    land,
    le,
    lgamma,
    lnot,
    log,
    log1p,
    log2,
    log10,
    lor,
    lt,
    maxof,
    minof,
    mod,
    mul,
    neq,
    pow,
    pow2,
    real,
    rem,
    root,
    round,
    rsqrt,
    sigmoid,
    sign,
    sin,
    sinh,
    sqrt,
    sub,
    tan,
    tanh,
    tgamma,
    trunc,
)

__all__ += ["constant", "range", "identity", "flat"]

from arrayfire.library.data import constant, flat, identity, range

__all__ += ["randu"]

from arrayfire.library.random import randu

__all__ += ["all_true", "any_true"]

from arrayfire.library.vector_algorithms import all_true, any_true
